---
layout: post
title: "YOLOv2/YOLO9000 Core Ideas"
tags: [Object Detection, YOLO]
comments: true
---

YOLOv2 ([Redmon & Farhadi, 2016](https://arxiv.org/abs/1612.08242)) được Joseph Redmon và Ali Farhadi công bố vào cuối năm 2016. YOLO9000 được xây dựng trên top của YOLOv2 được train kết hợp bởi COCO detection dataset và ImageNet classification dataset. Cải tiến chính của phiên bản này tốt hơn, nhanh hơn, tiên tiến hơn để bắt kịp faster R-CNN (phương pháp sử dụng Region Proposal Network), xử lý được những vấn đề gặp phải của YOLOv1.

## YOLOv2
Sự thay đổi chính của YOLOv2 với YOLOv1 như sau:

### 1. Batch Normalization 
Batch Normalization được thêm vào sau các lớp Conv layers trong YOLOv2. Nó giảm sự thay đổi giá trị unit trong hidden layer, do đó sẽ cải thiện được tính ổn định của neural network. Việc thêm Batch Normalization giúp mAP tăng thêm 2%.

### 2. Higher Resolution Classifier
Kích thước đầu vào trong YOLOv2 được tăng từ `224x224` lên `448x448`. Điều này giúp mAP tăng lên 4%.

### 3. Anchor boxes
Đây là thay đổi đáng chú ý nhất của YOLOv2 so với YOLOv1. Các anchor boxes này chịu trách nhiệm cho việc dự đoán các bounding boxes. Anchor boxes được thiết kế cho bộ dataset có sẵn dựa trên phân nhóm clustering (K-means clustering). Điều này xuất phát từ việc các vật thể có một số boundng boxes tương đồng ví dụ như ô tô, xe đẹp có bounding box dạng hình chữ nhật nằm ngang, người có bounding box dạng hình chữ nhật đứng...

#### 3.1 Convolutional anchor box detection
Thay vì dự đoán vị trí của bounding box với FC layers trong YOLOv1, YOLOv2 sử dụng Conv layers để dự đoán vị trí của anchor boxes như trong Faster R-CNN. Thay đổi này làm giảm mAP một chút nhưng tăng recall. 

#### 3.2 Direct location prediction
YOLOv1 không hạn chế trong việc dự đoán vị trí của bounding box. Khi các trọng số được khởi tạo ngẫu nhiên, bounding box có thể được dự đoán ở bất kỳ đâu trong ảnh. Điều này khiến mô hình không ổn định trong giai đoạn đầu của quá trình huấn luyện. Vị trí của bounding box có thể ở rất xa so với vị trí của grid cell.

YOLOv2 sử dụng hàm sigmoid để hạn chế giá trị trong khoảng 0 đến 1, từ đó có thể hạn chế các dự đoán bounding box ở xung quanh grid cell, từ đó giúp mô hình ổn định hơn trong quá trình huấn luyện.

YOLOv2 sẽ dự đoán 5 bounding boxes cho mỗi grid cell. Mỗi bounding box  mô hình lại dự đoán $(t_x, t_y, t_w, t_h)$ và $t_o$. Cho anchor box có kích thước $(p_w, p_h)$ nằm tại grid cell với tọa độ của góc trên bên trái là 
$(c_x, c_y)$, bounding box được dự đoán $b$ có tâm là $(b_x, b_y)$, kích thước $(b_w, b_h)$. Độ tin cậy (confidence) của dự đoán là sigmoid($\sigma$) của ouptut khác $t_o$, khi đó

$$ \begin{aligned}
b_x &= \sigma(t_x) + c_x\\
b_y &= \sigma(t_y) + c_y\\
b_w &= p_w e^{t_w}\\
b_h &= p_h e^{t_h}\\
\text{Pr}(\text{object}) &\cdot \text{IoU}(b, \text{object}) = \sigma(t_o)
\end{aligned} $$

<img src="https://lilianweng.github.io/lil-log/assets/images/yolov2-loc-prediction.png">

*Hình 1. YOLOv2 bounding box location prediction*

### 4. Fine-Grained Features
YOLOv1 gặp vấn đề khó khăn khi phát hiện các vật thể nhỏ (chia ảnh thành `7x7` grid cells). YOLOv2 chia ảnh thành `13x13` grid cells, do đó có thể phát hiện được những vật thể nhỏ hơn, đồng thời cũng hiệu quả đối với các vật thể lớn.

### 5. Multi-Scale Training
YOLOv1 có điểm yếu khi phát hiện các đối tượng với các kích cỡ đầu vào khác nhau. Ví dụ YOLOv1 được huấn luyện với các ảnh có kích thước nhỏ của cùng loại vật thể, nó sẽ gặp vấn đề khi phát hiện vật thể tương tự trong ảnh có kích thước lớn hơn. Điều này được giải quyết với YOLOv2, nó được train với kích thước ảnh ngẫu nhiên trong khoảng `320x320` đến `608x608`. Điều này cho phép model học và dự đoán chính xác đối tượng với nhiều kích thước khác nhau. *Kích thước mới của ảnh đầu vào được lấy ngẫu nhiên cứ sau 10 batches.* Do Conv layers YOLOv2 giảm kích thước của ảnh đầu vào theo hệ số 32 nên kích thước mới cần là số chia hết cho 32.
**6. Darknet 19**: YOLOv1 sử dụng 24 Conv layers và 2 FC layers. Trong khi đó YOLOv2 sử dụng kiến trúc Darknet 19 với 19 Conv layers, 5 MaxPooling layers và 1 softmax layer cho phân loại vật thể. Darknet được viết bằng ngôn ngữ C và CUDA.

Với những cải tiến như vậy YOLOv2 chính xác hơn, nhanh hơn so với phiên bản YOLOv1.

## YOLO9000
Bởi vì việc vẽ các bounding boxes trên ảnh cho object detection tốn kém hơn nhiều so với việc tag images cho phân loại, bài báo đã đề xuất một cách kết hợp tập small object detection dataset với larget ImagNet để model có thể phát hiện được nhiều classes hơn. Trong suốt quá trình training nếu ảnh đầu vào đến từ classification dataset nó sẽ chỉ backpropagates the classification loss.

Để có thể kết nối ImageNet labels (1000 classes, fine-grained) với CÔC/PASCAL (< 100 classes, coarse-grained), YOLO9000 xây dựng hierarchical tree từ [WordNet](https://wordnet.princeton.edu/), các labels chung gần với các node gốc còn fin-grained class labels là các node lá (classes trong ImageNet).

<img src="https://lilianweng.github.io/lil-log/assets/images/word-tree.png">

*Hình 2. The WordTree hierarchy merges labels from COCO and ImageNet. Blue nodes are COCO labels and red nodes are ImageNet labels.*

Để dự đoán xác suất rơi vào một class, ta nhân các xác suất từ node gốc của đồ thị, đi theo các nhánh và dừng lại khi gặp class đó
> Pr("persian cat" | contain a "physical object") 
= Pr("persian cat" | "cat") 
  Pr("cat" | "animal") 
  Pr("animal" | "physical object") 
  Pr(contain a "physical object")    # confidence score.

### Tài liệu tham khảo
1. https://medium.com/@venkatakrishna.jonnalagadda/object-detection-yolo-v1-v2-v3-c3d5eca2312a
2. 



