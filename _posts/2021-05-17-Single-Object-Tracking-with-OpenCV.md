---
layout: post
mathjax: true
title: "Single Object Tracking with OpenCV"
tags: [Object Tracking, OpenCV]
comments: true
---

**Tracking và Detection**

* **Tracking nhanh hơn detection:** Khi tracking vật thể được phát hiện ở khung hình trước đó, chúng ta đã biết rất nhiều thông tin về hình dạng của vật thể, vị trí, hướng của chuyển động. Do đó chúng ta có thể sử dụng các thông tin này để dự đoán vị trí của vật thể trong các khung hình tiếp theo và chỉ cần tìm kiếm một chút để xác định vị trí chính xác của vật thể. 
* **Tracking có thể hỗ trợ khi detection thất bại:** Nếu chúng ta chạy face detector trên video và mặt người bị gần sát vật thể khác, lúc này face detector có thể không phát hiện được. Một thuật toán tracking tốt có thể giải quyết được phần nào sự occlusion.
* **Tracking duy trì identity (định danh):** detection chỉ xác định các bounding box quanh vật thể, tuy nhiên tracking có thể giúp chúng ta duy trì đình danh cho từng vật thể (gắn ID cho nó)

Trong bài trước chúng ta đã tìm hiểu về `centroid tracking algorithm`. Nó hoạt động khá tốt, tuy nhiên nó cần chạy `object detection` cho mỗi khung hình. Điều này sẽ làm tăng khối lượng tính toán hơn.

Chúng ta mong muốn chỉ thực hiện object detection một lần, sau đó sẽ thực hiện tracking. Phương pháp này sẽ hiệu quả và nhanh hơn. 

OpenCv cung cấp cho chúng ta 8 object tracking algorithms:
* **BOOOSTING tracker**: sử dụng các thuật toán AdaBoost (tương tự như Haar cascades sử dụng cho face detector). Tracker này chậm và không hoạt động tốt
* **MIL tracker**: độ chính xác cao hơn BOOSTIG nhưng nói chung vẫn kém
* **KCF tracker**: Kernelized Correlation Filters. Nhanh hơn BOOSTING và MILL. KCF và MIL đều không xử lý hoàn toàn được occlusion (hiện tượng các vật thể quá gần nhau dường như nối thành một, điều này gây khó khăn cho việc tracking)
* **CSRT tracker:** Discrimitive Correlation Filter (with Channel and Spatial Reliability). CSRT chính xác hơn KCF nhưng chậm hơn một chút
* **MedianFlow tracker:** hoạt đồng tương đối tốt, tuy nhiên nếu có nhiều sự thay đổi trong hành động như di chuyển nhanh của vật thể hoặc vật thể thay đổi nhanh chóng về hình dạng thì model có thể thất bại trong việc tracking
* **TLD tracker:** rất hay bị False-Positive (dương tính giả). Không nên sử dụng caí này.
* **MOSSE tracker:** rất nhanh, tuy nhiên độ chính xác không tốt như KCF và CSRT
* **GOTURN tracker:** dựa trên deep learning, cần nhiều files để chạy, khó sử dụng.

Các bạn xem code ở github của mình cho dễ nhìn [huytranvan2010](https://github.com/huytranvan2010/OpenCV-Object-Tracking)
```python
# Cách dùng
# python opencv_object_tracking.py --tracker CSRT
# python opencv_object_tracking.py --video videos/traffic.mp4 --tracker CSRT

import cv2
import argparse
import imutils
import time
from imutils.video import FPS

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, help="path to input video file")
ap.add_argument("-t", "--tracker", type=str, default="KCF", help="OpenCV object tracker type")
args = vars(ap.parse_args())

# tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = args["tracker"]

if int(minor_ver) < 3:
    tracker = cv2.Tracker_create(tracker_type)
else:
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

# Khởi tạo tọa độ bounding box của obejct muốn theo dõi, nếu điền vào ở dưới sẽ xử lý 
initBB = None

if not args.get("video", False):
    print("[INFO] starting video stream...")
    video = cv2.VideoCapture(0)     # lấy webcam
    time.sleep(1.)      # warm up
else:
    video = cv2.VideoCapture(args["video"])     # lấy video truyền vào

# khởi tạo bộ đếm fps
fps = None

while True:
    ok, frame = video.read()    # đọc video

    # Nếu ko đọc đọc được frame
    if not ok:
        break
    
    # Nếu đọc đến cuối video
    if frame is None:
        break
    
    # resize lại để có tốc độ tốt hơn
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    # kiểm tra nếu chúng ta đang theo dõi vật thể, ban đầu khởi tạo ininBB
    if initBB is not None:
        # lấy new bounding box của vật thể đó - update tracker
        # chú ý xem bên dưới mình mới khởi tạo tracker
        (success, box) = tracker.update(frame)

        # nếu sự theo dõi thành công thì vẽ rectangle
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # update the FPS counter
        fps.update()
        fps.stop()
        
        # định nghĩa một số thông tin để vẽ lên frame
        info = [
            ("Tracker", tracker_type),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]
        # Duyệt qua info để ghi một số thông tin lên frame
        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H - ((i * 20) + 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # hiển thị frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    # Nhấn "s" để chọn bounding box theo dõi
    if key == ord("s"):
        # Chọn bounding box muốn theo dõi (kéo bằng chuột), nhớ nhấn ENTER hoặc SPACE để hoàn thành
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        
        # bắt đầu tracking bằng cách cung cấp tọa độ bounding box
        # then start the FPS throughput estimator as well
        """ Đây chính là khởi tạo tracker cho bounding boxes đó """
        tracker.init(frame, initBB)
        fps = FPS().start()

    # Nhấn nhấn "q" sẽ thoát ra
    elif key == ord("q"):
        break

# Nếu sử dụng webcam thì dừng lại
if not args.get("video", False):
    video.stop()
# nếu dùng video thì release nó
else:
    video.release()

# Đóng tất cả các cửa sổ
cv2.destroyAllWindows()

```

**Lời khuyên:**
- Sử dụng CSRT khi cần độ chính xác cao hơn và chịu giảm FPS một chút
- Dùng KCF nếu cần FPS cao nhưng độ chính xác có thể thấp hơn
- Dùng MOSSE khi cần tốc độ

## Tài liệu tham khảo
1. https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
2. https://learnopencv.com/object-tracking-using-opencv-cpp-python/ 
