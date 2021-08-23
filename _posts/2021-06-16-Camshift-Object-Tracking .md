---
layout: post
mathjax: true
title: "Object Tracking with Camshift"
tags: [Object Tracking, OpenCV]
comments: true
---

Trong bài trước chúng ta đã tìm hiểu về object tracking với meanshift. Meanshift có vấn đề là kích thước của window không đổi trong suốt quá trình tracking dù vật ở xa hay gần camera. Một giải pháp ra đời có tên là CAMshift (continously Adaptive Meanshift).

CAMshift đầu tiên vẫn áp dụng Meanshift trước. Sau đó khi Meanshift hội tụ nó sẽ update kích thước của window, nó cũng tính tới hướng để khớp tốt nhất. Sau đó nó lại áp dụng meanshift cho window đã được scale với vị trí window trước. Quá trình cứ tiếp tục cho đến khi đạt được độ chính xác yêu cầu.

<img src="https://docs.opencv.org/master/camshift_face.gif" style="display:block; margin-left:auto; margin-right:auto">

Dưới đây là phân object tracking với Camshift trong OpenCV [github-huytranvan2010](https://github.com/huytranvan2010/Object-Tracking-with-Camshift)

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
# sau khi các gía trị ban đầu được nắm bắt điều kiện dừng cần được thiết lập
# nếu centroid ROI ko di chuyển thì dừng hoặc số iteration hơn 10 cũng dừng (vì quá trình dịch chuyển) - nhiều thì tốn thời gian
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while True:
    ret, frame = video.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        # apply camshift to get the new location
        # ret_val - return value để xác định vị trí của đối tượng
        ret_val, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on image
        pts = cv2.boxPoints(ret_val)    # trả về 4 đỉnh của rectangle
        pts = np.int0(pts)      # chuyển từ float về int để nó còn vẽ được
        # Vẽ tracking window lên frame
        img = cv2.polylines(frame, [pts], True, 255, 2)
        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == ord("q"):       # nhấn q để thoát
            break
    else:
        break

video.release()
cv2.destroyAllWindows()
```
Không giống như có mô hình Deep Leanring cả Meanshift và Camshift đều không cần training. Ví dụ cần tracking quả quá chúng ta không cần đưa các hình ảnh quả bóng vào thuật toán. Thay vào đó ở đay thuật toán sẽ phân tích màu săc ban đầu của quả bóng và theo dõi nó ngay sau đó.

Tuy nhiên nếu màu sắc hoặc texture (họa tiết) thay đổi nhiều sẽ rất khó để theo dõi đối tượng. Nói chung 2 thuật toán Meanshift và Camshift nên được thiện hiện đối với môi trường ổn định về ánh sáng có thể kiểm soát được.
##### Tài liệu tham khảo
1. https://docs.opencv.org/master/d7/d00/tutorial_meanshift.html
2. https://www.geeksforgeeks.org/track-objects-with-camshift-using-opencv/
3. https://codelungtung.wordpress.com/2018/03/06/object-tracking-in-video/
