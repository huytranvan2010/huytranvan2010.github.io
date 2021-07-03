---
layout: post
title: "YOLOv3 Core Ideas"
tags: [Object Detection, YOLO]
comments: true
---

YOLOv3 có kiến trúc khá giống YOLOv2. Tác giả đã thêm các cải tiến mới trong các nghiên cứu object detection thời điểm đó vào YOLOv2 để tạo ra YOLOv3. Các cải tiến đó bao gồm:

**1. Logistic regression cho confidence score:** - YOLOv3 predict độ tin cậy của bounding box (có chứa vật hay không) cho mỗi bounding box sử dụng logistic regression trong khi YOLOv1 và YOLOv2 sử dụng sum of squared errors.

**2. Darknet + ResNet as the base model:** - Darknet-53 vẫn dựa trên sự thành công của `3x3`, `1x1` Conv layers giống như kiến trúc Darknet cũ, tuy nhiên ở đây sử dụng thêm residual blocks. Model mới có 53 Conv layers nên gọi là **DarkNet-53**.

**3. Multi-scale prediction** - YOLOv3 sử dụng kiến trúc Feature Pyramid Networks (FPN) để đưa ra các dự đoán từ nhiều scale khác nhau của feature map (3 scales). Việc này giúp YOLOv3 tận dụng các feature map với độ thô - tinh khác nhau cho việc dự đoán. Số predicted boxes sẽ là 3, mỗi predicted boxes có tổng số `NxN(5+80)` (4 coorfinates + 1 objetcness score, 80 classes).
 
**4. Skip-layer concatenation** - YOLOv3 cũng thêm các liên kết giữa các lớp dự đoán. Mô hình upsample các lớp dự đoán ở các tầng sau và sau đó concatenate với các lớp dự đoán ở các tầng trước đó. Phương pháp này giúp tăng độ chính xác khi predict các object nhỏ.

Focal loss không giúp được nhiều cho YOLOv3, điều này có thể do việc sử dụng $\lambda_\text{noobj}$, $\lambda_\text{coord}$ - nó tăng loss dự đoán vị trí của bounding box và giảm loss dự đoán độ tin cậy của background boxes (không chứa object)

<img src="https://aicurious.io/posts/tim-hieu-yolo-cho-phat-hien-vat-tu-v1-den-v5/yolo-v3-darknet-53.png">

*Kiến trúc của YOLOv3*

Về tổng thể YOLOv3 chạy nhanh hơn, chính xác hơn so với SSD. YOLOv3 không chính xác bằng RetinaNet nhưng nhanh hơn gần 4 lần.

<img src="https://lilianweng.github.io/lil-log/assets/images/yolov3-perf.png">

*So sánh tốc độ và mAP của các onject detection model*

### Tài liệu tham khảo
1. https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html#ssd-single-shot-multibox-detector

