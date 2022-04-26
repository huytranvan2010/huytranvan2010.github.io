---
layout: post
mathjax: true
title: "Object Tracking with Meanshift"
tags: [Object Tracking, OpenCV]
comments: true
---

Meanshift chính là một thuật toán phân cụm trong machine learning, khác với K-Means cần biết số cụm trước Meanshift có thể tự động phân chia dữ liệu theo cụm. Meanshift có nhiều ứng dụng, một trong số đó là object tracking.

Ý tưởng phía sau Meanshift cũng khá đơn giản. Giả sử có tập hợp các điểm (có thể là phân bố pixel như histogram backprojection). Một window nhỏ được cho (có thể là vòng tròn), nhiệm vụ là di chuyển window đó đến nơi có mật độ pixel lớn nhất (số lượng điểm lớn nhất)
<img src="https://docs.opencv.org/master/meanshift_basics.jpg" style="display:block; margin-left:auto; margin-right:auto">

Window đầu "C1" có màu xanh, center của nó là "C1_o", tuy nhiên centroid của nó là "C1_r" (trung bình các tọa độ của các điểm trong window màu xanh). "C1_o" và "C1_r" không khớp với nhau. Bây giờ sẽ dịch chuyển window sau cho center của window mới trùng với centroid của window trước đó. Tuy nhiên center của window hiện tại lại không trùng với centroid của window hiện tại. Cứ thực hiện như vậy cho đến khi center và centroid của window trùng nhau (có sai số). Cuối cùng chúng ta đạt được window với phân bố pixel lớn nhất, được đánh dấu bằng màu xanh lá "C2".
<img src="https://docs.opencv.org/master/meanshift_face.gif" style="display:block; margin-left:auto; margin-right:auto">

Để sử dụng meanshift trong OpenCV, đầu tiên chúng ta cần xác định mục tiêu tracking, tìm histogram của nó để mà có thể backproject mục tiêu lên mỗi frame để phục vụ tính toán meanshift. Chúng ta cũng cần cung cấp vị trí đầu tiên của window (chứa mục tiêu). Đối với histogram cúng ta sẽ sử dụng **Hue**, ở đây không sử dụng **Saturation và Value** vì chúng bị ảnh hưởng bởi điều kiện sáng môi trường.

Meanshift có một số nhược điểm như sau:
- Phải tạo trước window, cần xác định vị trí của mục tiêu
- Khi vật thể ra khỏi khung hình, window vẫn còn, khi vật thể quay lại phải ở vị trí gần window nó mới track được
- Kích thước của window không đổi khi vật thể đi xa gần camera. Trong bài tiếp theo chúng ta sẽ nói về Camshift để giải quyết vấn đề này.

Dưới đây là implementation của meanshift trong OpenCV [github-huytranvan2010](https://github.com/huytranvan2010/Object-Tracking-with-MeanShift)

```python
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help='path to the video')
args = vars(ap.parse_args())

# Đọc video
video = cv2.VideoCapture(args["video"])

# Lấy frame đầu tiên
ret, frame = video.read()

# Xác định vị trí đầu tiên của window
x, y, w, h = 300, 200, 100, 50      # hardcode, tùy thuộc vào video
track_window = (x, y, w, h)

# vùng ROI để tracking
roi = frame[y:y+h, x:x+w]

# chuyển ROI về HSV space nhé
hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Tạo mask, để tránh ảnh hưởng điều kiện sáng tối, ở đây để H chạy toàn dải từ 0 đến 180
# Có thể bỏ mask đi, khi đó phần lấy roi_hist ở dòng 28 phải chuyển thành None
mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))

# Lấy histogram chỉ của vùng ROI, ở đây chỉ lấy histogram cho duy nhất 1 kênh H - Hue
# 1-st parameter là ảnh, 2-nd parameter thể hiện lấy 1 kênh, 3-st parameter là mask, 4-th là số bins, 5-th là khoảng giá trị
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])

# normalize histogram về khoảng giá trị 0-255, tham số thứ hai là giá trị trả về, cuối cùng là norm type
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    ret, frame = video.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        img = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == ord("q"):       # nhấn q để thoát
            break
    else:
        break

cv2.destroyAllWindows()
```
##### Tài liệu tham khảo
1. https://docs.opencv.org/master/d7/d00/tutorial_meanshift.html
2. https://www.youtube.com/watch?v=EDT0vHsMy34


