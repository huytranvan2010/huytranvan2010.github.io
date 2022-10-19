---
layout: post
title: "Nhận diện văn bản với EAST và Tesseract OCR"
tags: [OCR, OpenCV, Tesseract, EAST]
comments: true
---

Trong bài này chúng ta đi giải quyết bài toán OCR với sự kết hợp của EAST và Tesseract.
* EAST sẽ đảm nhận vai trò text detector
* Tessseract sẽ thực hiện text recognition

Trong project này có file `frozen_east_text_detection.pb` - EAST text detector, đây là pre-trained model CNN cho text detection. 
Tóm tắt một số bước chính như sau:
* Load EAST text detector
* Load ảnh, chuyển kích thước ảnh về số chia hết cho 32
* Chuyển ảnh về blob, đưa qua network để nhận được predictions: geometry và scores
* Thực hiện NMS để nhận được boxes (so với kích thước ảnh đầu vào)
* Rescale lại boxes so với kích thước ảnh gốc, trích xuất text ROI 
* Đưa text ROI qua Tesseract, sau đó in kết quả ra (text ROI được đưa trực tiếp vào Tesseract chưa qua xử lý, các bạn có thể thử pre-processing)

Dưới đây là inplementation [github-huytranvan2010](https://github.com/huytranvan2010/Text-recognition-with-Tesseract-and-EAST)
```python
import pytesseract
import argparse
import cv2
from hammiu import decode_prediction
import numpy as np
from imutils.object_detection import non_max_suppression

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True, help="Path to the input image")
parser.add_argument("-c", "--min_confidence", type=float, default=0.5, help="min confidence score for bbox to consider")
parser.add_argument("-p", "--padding", type=float, default=0.0, help="amount of padding to add to each border of ROI")
parser.add_argument("-w", "--width", type=int, default=320, help="nearest multiple of 32 for resized width")
parser.add_argument("-e", "--height", type=int, default=320, help="nearest multiple of 32 for resized height")
args = vars(parser.parse_args())

print("[INFO] loading EAST detector...")
net = cv2.dnn.readNet("frozen_east_text_detection.pb")

# Chuẩn bị ảnh, chuyển về kích thước // 32
image = cv2.imread(args["image"])
# copy một ảnh để xử lý trên đó, tí so sánh với ảnh gốc
orig = image.copy()
# lưu lại kích thước ảnh gốc ban đầu
(orig_h, orig_w) = image.shape[:2]

# Nếu dùng cách này hoặc chọn height, width không thích hợp sẽ cho kết quả không tốt
# Đã thử và xác nhận điều này
# new_h = (h // 32) * 32
# new_w = (w // 32) * 32

new_h = args["height"]
new_w = args["width"]
# chủ yếu để chú ý sẽ làm việc với image mới được resize rồi, điều này thực chất ko cần do bên dưới đã chuyển thành blob có kích thước đó
image = cv2.resize(image, (new_w, new_h))   

# lưu lại ratio để còn rescale lên so với ảnh ban đầu, do ảnh đưa vào mạng phải resize lại cho cạnh chia hết cho 32
ratio_h = orig_h / new_h
ratio_w = orig_w / new_w

# chuyển về 4D blob (batch, channels, H, W), convert BRG => RGB
# substratc mean from image, input của EAST là bội của 32, nếu ko sẽ không nối được ở phần feature-merging branch
blob = cv2.dnn.blobFromImage(image, 1, (new_w, new_h), (123.68, 116.78, 103.94), swapRB=True, crop=False)
# cho blob qua network
net.setInput(blob)

output_layer_names = net.getUnconnectedOutLayersNames()
(geometry, scores) = net.forward(output_layer_names)

# lấy final boxes sau khi đã loại bỏ box có score nhỏ và áp dụng NMS
final_boxes = decode_prediction(geometry, scores, min_score=args["min_confidence"])     # để overThreshold mặc định nhé

# Tạo list để lưu kết quả
results = []

# Phải nhân với hệ số scale ban đầu mới khớp được với ảnh ban đầu, do kích thước ảnh ban đầu có thể không chia hết cho 32
# nên cần resize để chia hết cho 32
# duyệt qua các boxes

for(xmin, ymin, xmax, ymax) in final_boxes:
    """ Lấy tọa độ của bounding box trên ảnh gốc (do đã nhân với hệ số tỉ lệ). Từ đây chuyển về hết kích thước ảnh gốc"""
    xmin = int(xmin * ratio_w)
    ymin = int(ymin * ratio_h)
    xmax = int(xmax * ratio_w)
    ymax = int(ymax * ratio_h)

    # áp dụng padding vào bounding box nhằm mở rộng bounding box
    # nhiều khi bounding box ăn sâu vào bên trong text, cần mở rộng ra
    """ 
    Ở đây để padding tỉ lệ theo chiều cao và chiều rộng (ví dụ 5%) của bounding box
    Điều này có nghĩa rằng chiều nào lớn hơn sẽ mở rộng hơn.
    Tuy nhiên mình nghĩ ko cần thiết, có thể mở rộng 2 chiều như nhau, truyền vào số pixel cũng được
    Ở đây truyên tỉ lệ
    """
    dx = int((xmax - xmin) * args["padding"])
    dy = int((ymax - ymin) * args["padding"])

    # sau khi áp dụng padding cần dùng min, max để tránh tràn ra khỏi kích thước ảnh
    xmin = max(0, xmin - dx)
    ymin = max(0, ymin - dy)
    xmax = min(orig_w, xmax + 2 * dx)
    ymax = min(orig_h, ymax + 2 * dy)

    # trích xuất text ROI
    roi = orig[ymin:ymax, xmin:xmax]
    # roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)     # nên nhớ orig vẫn đang ở BGR

    # set config for Tesseract
    config = "-l eng --oem 1 --psm 7"
    text = pytesseract.image_to_string(roi, config=config)

    # lưu bounding box và text tương ứng vào list
    results.append(((xmin, ymin, xmax, ymax), text))

""" Sắp xếp results theo tọa độ của bounding boxes từ trên xuống """
results = sorted(results, key=lambda x: x[0][1])    # sắp xếp theo ymin

# duyệt qua kết quả
for ((xmin, ymin, xmax, ymax), text) in results:
    print("{}\n".format(text))
    
    # strip out non-ASCII text so we can draw the text on the image using OpenCV
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    output = orig.copy()

    cv2.rectangle(output, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
    cv2.putText(output, text, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, ), 3)

    cv2.imshow("Output", output)
    cv2.waitKey(0)
```

Thử test với một số ảnh trong thư mục `images` nhận thấy nhiều ảnh phải thêm padding vào mới nhận biết được. Có một số chữ không nhận dạng được. Một số nguyên nhân có thể là:
* Chữ bị nghiêng, xoay
* Phông chữ của text không được trained trong Tesseract

Có lẽ chúng ta cần thực hiện [a perspective transform to correct the view](https://www.pyimagesearch.com/2016/10/03/bubble-sheet-multiple-choice-scanner-and-test-grader-using-omr-python-and-opencv/). Nên nhớ rằng trong bài này chúng ta cũng không đưa ra **rotated bounding boxes**. Như các bạn đã thấy bounding boxes khi in ra có dạng nằm ngang. Bản thân nó có góc xoay, ở đây mình chưa tính đến điều này.

Một số lựa chọn thay thế cho Tesseract OCR:
* Google Vision API OCR Engine
* Amazon Rekognition
* Microsoft Cognitive Services

Ngoài ra có thể xem xét thên EasyOCR package. EasyOCR có thể:
* Vừa thực hiện text detection và text recognition (Tesseract cũng có thể làm vậy, ở đây mình sử dụng thêm EAST để crop text ROI)
* EasyOCR có thể hỗ trợ nhiều ngôn ngữ
* Pythonic API (dễ dàng làm việc)
* Sử dụng state-of-the-art model
* Vẫn tiếp tục được phát triển, sớm hỗ trợ chữ viết tay

Tùy vào từng bài toán các bạn có thể chọn các phương pháp phù hợp cho chính mình.

### Tài liệu tham khảo
1. https://theailearner.com/2019/10/19/efficient-and-accurate-scene-text-detector-east/
2. https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/