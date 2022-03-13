---
layout: post
title: "Faster R-CNN"
tags: [Object detection]
comments: true
---

Trong hai bài trước chúng ta đã tìm hiểu về models R-CNN, Fast R-CNN và một số nhược điểm của chúng. Trong bài này hãy cùng tìm hiểu về model Faster R-CNN, một model mới hơn, cải thiện được nhược điểm của những người anh em trước đó.

Model Faster R-CNN được phát triển năm 2016 do Shaoqing Ren et al. Tương tự như Fast R-CNN, nó sử dụng mạng CNN để trích xuất feature map. Tuy nhiên thay vì sử dụng selective search để xác định region proposals thì Faster R-CNN sử dụng **Region proposal network (RPN)** để dự đoán các region proposals. Các predicted region proposals này được reshape lại bằng RoI pooling layer và được dùng để phân loại và xác định các giá trị offsets của bounding boxes.

Kiến trúc của Faster R-CNN có thể được miêu tả bằng hai mạng chính sau:
1. Region proposal network (RPN) - Selective search được thay thế bằng ConvNet. RPN có hai outputs là: objectness score (object or no object) và box location
2. Fast R-CNN - chứa các thành phần chủ yếu của Fast R-CNN:
    - Base network cho feature extraction: thường là pretrained CNN model để có được feature map
    - RoI pooling layer để có được fixed-size RoIs
    - Output layer: chứa 2 FC layers cho softmax classifier và bounding box regression

<img src="https://imgdetail.ebookreading.net/20201209/5/9781617296192/9781617296192__deep-learning-for__9781617296192__OEBPS__Images__7-11.png" style="display:block; margin-left:auto; margin-right:auto">

Như hình trên nhận thấy feature map vừa được đưa vào RPN xác định region proposals và được đưa vào RoI pooling layer để trích xuất fixed-size window of features.

**Base network để trích xuất features**

Tương tự Fast R-CNN, bước đầu tiên trong Faster R-CNN kà sử dụng pre-trained CNN model đẻ trích xuất features từ input image. Ở đây có thể sử dụng nhiều pre-trained models được, trong bài báo tác giả sử dụng ZF và VGG trên ImageNet. Ngày nay có nhiều models cải tiến hơn được sử dụng làm backbone như ResNet, DenseNet...

**Region proposal network (RPN)**

RPN xác định các regions có khả năng chứa objetcs dựa trên feature map nhận được từ base network. RPN còn được biết với tên gọi **attention network** bởi vì nó hướng network tập trung vào các vùng quan tâm.

Kiến trúc của RPN thường bao gồm 2 layers:
- `3x3` fully convolutional layer (FCN) với 512 channels
- Hai convolutional layers `1x1` song song với nhau: classification layer được sử dụng để dự đoán region chứa object (ở đâu có score tương ứng với background - không chứa object và foreground - chứa object. Nó chỉ quan tâm chứa object hay không) và layer cho regression hoặc bounding box prediction.

<img src="https://imgdetail.ebookreading.net/20201209/5/9781617296192/9781617296192__deep-learning-for__9781617296192__OEBPS__Images__7-12.png">

*Convolutional implementation cho RPN architectur, k là số achors*

**Chú ý**: FCN có hai lợi ích chính:
- Tính toán nhanh hơn so với FC layer
- Có thể nhận image với bất kì spatial resolution (width và height). Tuy nhiên thông thường chúng ta thường cố định kích thước của input.

Nhiệm vụ của RPN là xác định xem region có chứa object hay không.

Thông thường vị trí của bounding box được xác định bởi $(x, y, w, h)$, $x, y$ là tọa độ tâm, $w$ là width và $h$ là height của bounding box. Tuy nhiên nếu xác định bounding box kiểu này thì khi xây dựng model chúng ta cần có một số giới hạn để các giá trị nằm trong khoảng cho phép. Để không phải làm điều đó, chúng ta đi tạo các **anchor boxes**, regression layer sẽ đi dự đoán offsets tính từ boxes này $(\Delta_x, \Delta_y, \Delta_w, \Delta_h)$, từ đó xác được vị trí dự đoán cả region proposal đầu ra.

**Anchor boxes**

Bằng cách sử dụng window approach, RPN tạo ra $k$ regions cho mỗi vị trí trong feature map. Các vùng này được gọi là **anchor boxes**. Cụ thể trong Faster R-CNN có 9 anchor boxes được định nghĩa với kích thước và tỉ lệ khác nhau. Tổng số lượng anchors sẽ phụ thuộc vào kích thước của feature map.

<img src="https://miro.medium.com/max/1204/1*XyPFZnb88Taag29iVQDBng.png">



<img src="https://imgdetail.ebookreading.net/20201209/5/9781617296192/9781617296192__deep-learning-for__9781617296192__OEBPS__Images__7-15.png">

**Training RPN**

RPN được train để phân loại anchor box, nó đưa ra objectnes score và các tọa độ xấp xỉ.

Các anchor boxes được gán nhãn **positive** và **negative** dựa trên IoU của nó với ground-truth bounding boxes:
- Các anchor có IoU lớn nhất với ground-truth box được coi là positive
- Các anchors có $IoU > 0.7$ được coi là positive
- Các anchors có $IoU < 0.3$ được coi là negative
- Các anchors có $0.3 < IoU < 0.7$ không được xếp vào hai loại kia và không được sử dụng trong quá trình training.

**Chú ý**: có điều kiện IoU lớn nhất làm positive để đảm bảo trường hợp các IoU nhỏ hơn 0.7 thì chúng ta vẫn có positive example.

Nếu anchor overlap lớn với ground-truth box thì coi nó chứa object và được gán nhán **positive**. Anchor có overlap nhỏ với ground-truth thì coi không chứa object và được gán nhãn **negative**. Những anchor có IoU trong khoảng $(0.3, 0.7)$ không được sử dụng trong quá trình training.

Với 2 output layers, RPN đưa ra $2k$ scores và $4k$ coordinates, ở đây $k$ là tổng số lượng anchors. Ví dụ mỗi vị trí lấy 9 anchors, input của RPN có kích thước $w \times h$, khi đó $k= w \times h \times 9$. 

<img src="https://www.researchgate.net/publication/329263432/figure/fig3/AS:698144681623558@1543462071466/Region-Proposal-Network-RPN.png">

Sau RPN chúng ta thu được region proposals, rất nhiều trong số chúng bị overlap với nhau nên cần có phương pháp để loại bỏ bớt các region proposals trước khi đưa nó vào phần sau. Ở đây sẽ dùng Non-max suppression (NMS):
- **Bước 1:** Ví dụ có tập hợp các RoIs thu được R với các confidence scores tương ứng S và voverlap threshold N. Có list rỗng D
- **Bước 2:** Chọn RoI có confidence score lớn nhất, xóa khỏi R và cho vào D.
- **Bước 3:** So sánh IoU của RoI vừa được thêm vào D và các RoIs còn lại trong R với threshold IoU, nếu IoU > threshold IoU thì loại bỏ các RoIs đó khỏi R
- **Bước 4:** Lặp lại các bước 2 và 3 cho đến khi hết RoIs trong R. Các RoIs cuối cùng chúng ta nhận được là các RoIs trong list D.

<img src="https://929687.smushcdn.com/2633864/wp-content/uploads/2016/09/iou_equation.png?lossy=1&strip=1&webp=1">

Tuy nhiên thuật toán NMS ban đầu có một số nhược điểm, giả sử có threhsold IoU là 0.5:
- Ví dụ RoI có IoU = 0.51 nhưng có confidence score cao vẫn bị loại bỏ (ở bước 3)
- Có RoI có IoU < 0.5 nhưng có confidence score nhỏ vẫn được giữ lại (ở bước so sánh 3)
Chính những nhược điểm này làm cho chất lượng của model giảm xuống. Cần có phương pháp mới cải tiến NMS ban đầu này.

Thông thường khi training mỗi lần chúng ta sẽ load mini-batch size các ảnh vào. Tuy nhiên đối với Faster R-CNN mỗi lần chúng ta chỉ sử dụng duy nhất một ảnh, và trong một ảnh này chúng ta sẽ lấy ra $k=256$ anchors bao gồm 128 positive anchors và 128 negative anchors. Thông thường số lượng positve anchors nhỏ và có thể không đủ 128 cho một ảnh. Trong trường hợp đó chúng ta sẽ bổ sung thêm các negative anchors cho đủ $k=256$ anchors.

**Multi-task loss function**

Tương tự Fast-RCNN, Faster R-CNN được tối ưu dựa trên multi-task loss function:

$$L = L_{cls} + L_{loc}$$

$$
L(\{p_i\}, \{t_i\}) = \frac{1}{N_{cls}}\sum L_{cls}(p_i, p_i^{*}) + \frac{\lambda}{N_{loc}}\sum p_i^{*} \times L1_{smooth}(t_i - t_i^{*})
$$_
trong đó:
- $p_i$ và $p_i^{*}$
- $t_i$ là 4 predicted parameters cái xác định bounding box, $t_i^{*}$ là các parameters cho ground truth box
- $N_{cls}$ - normalization term, được set cho mini-batch size 256. Thực chất mỗi lần chạy chỉ có một ảnh và 256 là tổng số positive và negative anchors cho ảnh đó. Một nửa cho positive anchors, một nửa cho negative anchors. Nếu số lượng positive anchors không đủ thì sẽ lấy negative anchors thay thế.
- $N_{loc}$ - normalization term, được set cho số anchors (~2400) theo bài báo.
- $L_{cls}(p_i, p_i^{*})$ - log loss function cho 2 classes. Chúng ta có thể dễ dàng chuyển multi-class classification thành binary classification bằng cách dự đoán xem sample có phải là object không.

$$L_{cls}(p_i, p_i^{*}) = -p_i^{*}\log p_i - (1 - p_i^{*}) \log (1 - p_i)$$
- $L1_{smooth}$ - function đo lường sự khác nhau giữa predicted và true location parameters $(t_i, t_i^{*})$
- $\lambda$ - balancing parameter, bài báo set bằng 10, $\lambda$ thể hiện đóng góp của classification loss và regressio loss.

**Model workflow**
1. Pre-train a CNN network treên image classification tasks
2. Fine-tune RPN cho region proposal task, cái này được khởi tạo bằng pre-train image classifier với các positive và negative examples như đã nói ở trên
3. Train Fast R-CNN object detection model bằng cách sử dụng proposal được tạo ra từ RPN
4. Sử dụng Fast R-CNN network để khởi tạo RPN training. Trong khi vẫn giữ việc chia sẻ convolutional layers, chỉ thực hiện fine-tune RPN-specific layers. Tại bước này, RPN và detection network đã chia sẻ convolutional layers.
5. Fine-tune unique layers của Fast R-CNN
6. Các bước 4-5 có thể lặp lịa để train RPN và Fast R-CNN thay thế nhau nếu cần.

<img src="https://miro.medium.com/max/1200/1*1Mj0C4wzi57Z6Z933gb6vA.png">


<img src="https://www.researchgate.net/publication/332079570/figure/fig1/AS:741805058437122@1553871516307/The-architecture-of-Faster-R-CNN-The-conv-represents-convolutional-layer-the-relu.ppm">

**Tài liệu tham khảo**
1. https://datascience.stackexchange.com/questions/27277/faster-rcnn-how-anchor-work-with-slider-in-rpn-layer
2. https://youtu.be/_GfPYLNQank
3. https://lilianweng.github.io/posts/2017-12-31-object-recognition-part-3/
4. Deep Learning for Vision Systems


