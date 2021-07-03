---
layout: post
title: "YOLOv3 - Pre-trained Model"
tags: [Object Detection, YOLO]
comments: true
---
Trong bài này mình không đi vào lý thuyết mà sử dụng luôn pre-trained model YOLOv3 có sẵn để thực hiện phát hiện vật thể trong ảnh và video.

Đối với bài này các bạn cần tải 3 file sau:
- `coco.names`: chứa tên các class mà YOLO được huấn luyện [link](https://github.com/pjreddie/darknet/blob/master/data/coco.names)
- `yolov3.cfg`: configuration file chứa các cài đặt cho YOLO [link](https://pjreddie.com/darknet/yolo/)
- `yolov3.weights`: các pre-trained weights [link](https://pjreddie.com/darknet/yolo/). Do file lớn quá các bạn không upload lên Github được, các bạn tải về theo link mình đính kèm.

Các bước chính khi triển khai pre-trained YOLO v3:
* Load model (cần file weights và configuration)
* Load ảnh, tiền xử lý trước khi đưa vào model
* Lấy tên các output layers, dựa vào đây chúng ta sẽ xác định được các bounding boxes
* Thực hiện Non-max suppression để loại bỏ các bounding boxes chồng chập
* Vẽ các bounding boxes và confidence lên ảnh.

Dưới đây là phần nhận diện vật thể với pre-trained YOLOv3 trong ảnh. Đối với video cũng làm tương tự.
```python
import numpy as np
import argparse
import cv2
import os
import time 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-y", "--yolo", required=True, help="base path to the YOLO directory")
ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.3, help="threshold when applying non-maxima suppression")
args = vars(ap.parse_args())

labelsPath = os.path.sep.join([args["yolo"], "coco.names"])  
LABELS = open(labelsPath).read().strip().split("\n")    

# khởi tạo list các màu để biểu diễn labels
np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(LABELS), 3))  

# lấy đường dẫn đến YOLO weights và model configuration
weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])

# load YOLO detector đã pre-trained trên COCO dataset (80 classes) bằng OpenCV
print(["[INFO] loading YOLO from the disk..."])
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

# load ảnh rồi đưa vào network
image = cv2.imread(args["image"])
(H, W) = image.shape[:2]    # lấy height và width

""" Lấy layer names của các output layers (chỉ các output layers thôi) """
# Cách 1
layer_names = net.getLayerNames()   # tên của tất cả các layers trong YOLO
output_layer_names = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]    # getUnconnectedOutLayers() - it gives you the final layers number in the list from, lấy index trừ 1

# # Cách 2
# output_layer_names = net.getUnconnectedOutLayersNames()

""" Tiền xử lý ảnh, đưa vào model và đưa ra output """
# construct a blob from the input image and then perform a forward pass of the YOLO
# object detector, giving us our bounding boxes and associated probabilities
# tiền xử lý ảnh: rescale, resize, swapRB vì lúc ở trên đọc bằng OpenCV, không crop
blob = cv2.dnn.blobFromImage(image, 1/255., (416, 416), swapRB=True, crop=False)    # tiền xử lý ảnh để tí cho vào YOLO
# Truyền input vào mạng
net.setInput(blob)
start = time.time()
# Lấy đầu ra ở các output layers bằng cách truyền tên của output layers vào method forward
layerOutputs = net.forward(output_layer_names)
end = time.time()

# show timing information on YOLO
print("[INFO] YOLO look {:.6f} seconds".format(end - start))

""" Khởi tạo list các detected bounding boxes, confidences và class IDs """
boxes = []
confidences = []
classIDs = []   # detected object's class label

# Duyệt qua các layer outputs, có mấy outputs để có thể phát hiện được các kích thước khác nhau
for output in layerOutputs:
    # duyệt qua each of the detections, trong mỗi output lại phát hiện được nhiều object
    for detection in output:
        # trích xuất the class ID và confidence của the current object detection
        # bỏ qua 5 cái đầu là x, y, w, h và objectness score, những cái sau là class scores, detection có 85 elements
        scores = detection[5:]      
        classID = np.argmax(scores)
        confidence = scores[classID]

        # chỉ quan tâm predictions nào có confidence đủ lớn (> threshold)
        if confidence > args["confidence"]:
            # scale the bounding box back to the size of the image
            # YOLO trả về  relative size
            box = detection[0:4] * np.array([W, H, W, H])   # element-wise (center_x, center_y, w, h)
            centerX, centerY, width, height = box.astype("int")     # int về cần vẽ pixel

            # Use the center coordinates, width and height to get the coordinates of the top left corner
            # tính toạ độ góc trên bên trái
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))

            # update our list of bouding boxes (x, y, w, h), cập nhật list
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)

""" Áp  dụng non-max suppression để loại bỏ bớt các overlapping bounding boxes mà cùng vật thể """
idxs = cv2.dnn.NMSBoxes(boxes, confidences, args["confidence"], args["threshold"])

# Vẽ các box vad class text lên ảnh
# cần đảm bảo có ít nhất 1 detection
if len(idxs) > 0:
    # duyệt qua các indexes 
    for i in idxs.flatten():    # flatten() ra nó mới về dạng list
        # lấy ra các thông tin của bounding boxes
        x, y, w, h = boxes[i]   # vì ở trên lưu boxes là list of list x, y, w, h

        # draw the bounding box and label on the image
        color = [int(c) for c in COLORS[classIDs[i]]]   # lấy 1 hàng nhưng duyệt qua để tạo list
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
        cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv2.imshow("image", image)
cv2.waitKey(0)
```
Các bạn có thể xem code chi tiết ở github của mình [YOLOv3 Object Detection](https://github.com/huytranvan2010/YOLOv3-Object-Detection)

Nhược điểm của YOLOv3:
- Khó phát hiện được các vật thể nhỏ (Faster RCNN làm rất tốt nhưng lại chậm)
- Khó xử lý các vật thể sát nhau

# Tài liệu tham khảo
1. https://www.youtube.com/watch?v=1LCb1PVqzeY
2. https://gilberttanner.com/blog/yolo-object-detection-with-opencv
3. https://www.pyimagesearch.com/2018/11/12/yolo-object-detection-with-opencv/
4. https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html
5. https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/






