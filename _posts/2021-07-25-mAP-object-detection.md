---
layout: post
title: "mAP - mean Average Precision for Object Detection"
tags: [Object Detection]
comments: true
---

**mAP** (mean average precision) là độ đo phổ biến để đánh giá độ chính xác của bài toán object detection như Faster R-CNN, SSD... mAP chính là trung bình của các average precision của từng class. Trước khi tìm hiểu về mAP chúng ta cùng nhắc lại một số khái niệm như precision, recall trong bài toán phân loại.

Ví dụ bài toán phân loại phụ nữ có thai hay không thì việc có thai coi là Positive, việc không có thai coi là Negative. True/False thể hiện sự dự đoán đúng hay sai. 
- True Positive: dự đoán có thai - Positive, thực tế thì có thai (True)
- False Positive: dự đoán có thai - Positive, thực tế thì không có thai (False). Dự đoán người không có thai thành có thai.
- True Negative: dự đoán không có thai - Negative, thực tế không có thai (True)
- False Negative: dự đoán không có thai - Negative, thực tế thì có thai (False)

<img src="https://skappal7.files.wordpress.com/2018/08/confusion-matrix.jpg?w=748" style="display:block; margin-left:auto; margin-right:auto">


### Precision và Recall

$$\text{Precision} = \frac{TP}{TP+FP}$$

$$\text{Recall} = \frac{TP}{TP+FN}$$

$$\frac{2}{F1} = \frac{1}{\text{Precision}} + \frac{1}{\text{Recall}}$$

trong đó: $TP$ - True Positive, $TN$ - True Negative, $FP$ - False Positive, $FN$ - False Negative.

### IoU - Intersection over union

IoU (còn có tên khác là Jaccard index) là giá trị đo độ chồng chập giữa 2 bounding boxes. Chúng ta thường dùng IoU để đo độ khớp của predicted box và ground-truth box. Đối với bài toán object detection chúng ta hay dùng IoU để xác định precision và recall. 

<img src="https://www.pyimagesearch.com/wp-content/uploads/2016/09/iou_equation.png" style="display:block; margin-left:auto; margin-right:auto">

Đối với bài toán object detection:
- **TP** (True Positive): phát hiện chính xác, detection với IoU ≥ threshold
- **FP** (False Positive): phát hiện sai, detection với IoU < threshold
- **FN** (False Negative): groudth-truth box không được gắn với predicted bounding box nào
- **TN** (True Negative): không được dùng. Đây là những phần của ảnh không chứa đối tượng (không được gán ground-truth box) và được dự đoán không chứa đối tượng (thực chất mô hình chỉ đưa ra các vùng có khả năng chứa đối tượng). Điều này có nghĩa rằng các vùng khác trong ảnh được dự đoán là không chứa đối tượng. Số lượng TN như vậy là vô số.

Ví dụ như hình dưới nếu IoU threshold là 0.5, IoU cho dự đoán là 0.7 khi đó chúng ta phân loại đúng (TP). Ngược lại nếu IoU là 0.3 chúng ta phân loại sai (FP). Tạm thời chưa quan tâm đến confidence score.

<img src="https://miro.medium.com/max/941/1*S8osGaPdGMnJc-WFIqR3eA.jpeg" style="display:block; margin-left:auto; margin-right:auto">

> Predicted boxes phải được phân loại đúng class trước và sau đó chúng ta mới đi xác định precision và recall dựa trên IoU. Phân loại sai class mà xác định IoU thì không có ý nghĩa.

Và khi chúng ta thay đổi IoU threshold, False Positive có thể chuyển thành True Positive như hình dưới đây.

<img src="https://miro.medium.com/max/941/1*dGhkFQLNvIeib_Fg8SwndA.jpeg" style="display:block; margin-left:auto; margin-right:auto">

### AP - average precision
> Average Precision (AP) is the area under the precision-recall curve - diện tích nằm dưới đường precision-recall.

Chúng ta sẽ tính AP (average precision) thông qua một ví dụ dưới đây. Trong tập dữ liệu chỉ chứa 5 quả táo. Chúng ta thu thập tất cả các dự đoán cho tất cả các hình ảnh và xếp hạng theo thứ tự giảm dần của confidence score tương ứng với mỗi predicted bounding box. Cột thứ hai thể hiện dự đoán đúng hay không. Trong ví dụ này dự đoán được coi là đúng nếu có $IoU \geq 0.5$

<img src="https://miro.medium.com/max/941/1*9ordwhXD68cKCGzuJaH2Rg.png" style="display:block; margin-left:auto; margin-right:auto">

Cùng xem dòng rank#3, precision và recall được tính như nào mà có kết quả như vậy:
- **Precision** = 2/3 = 0.67 (dự đoán đúng được 2 quả táo TP và dự đoán một quả khác thành quả táo FP)
- **Recall** = 2/5 = 0.4 (do có tổng cộng 5 quả táo $TP + FN = \# \text{ground-truth boxes}$ và dự đoán đúng được 2 quả táo TP)

Nhận thấy gía trị của recall không giảm khi chúng ta đi xuống theo chiều giảm confidence score tuy nhiên precision lại đi theo đường zigzag (có thể tăng lên nhưng xu hướng chung là giảm).

<img src="https://miro.medium.com/max/941/1*ODZ6eZMrie3XVTOMDnXTNQ.jpeg" style="display:block; margin-left:auto; margin-right:auto">

Vẽ sự phụ thuộc của precision và giá trị của recall (lấy từ bảng trên cùng).

<img src="https://miro.medium.com/max/941/1*VenTq4IgxjmIpOXWdFb-jg.png" style="display:block; margin-left:auto; margin-right:auto">

*Precision-recall curve*

Định nghĩa chung của Average Precision (AP) là area under the precision-recall curve (diện tích dưới đường precision-recall):

$$ AP = \int_{0}^{1} P(r) dr $$

trong đó $P(r)$ thể hiện sự phụ thuộc của precision vào recall.

Giá trị của precision và recall luôn nằm trong [0, 1] do đó AP cũng nằm trong [0, 1]. Trước khi tính AP cho bài toán object detection người ta người làm trơn đường zigzag trước (loại bỏ một số điểm precision tăng khi confidence giảm).

<img src="https://miro.medium.com/max/941/1*zqTL1KW1gwzion9jY8SjHA.png" style="display:block; margin-left:auto; margin-right:auto">

Nhìn trên hình nhận thấy tại mỗi mức recall chúng ta sẽ thay thế precision bằng giá trị max precision ở bên phải mức recall đó (ví dụ recall trong [0.4, 0.8] sẽ lấy precision max là 0.57 tại recall = 0.8 do nó nằm bên phải, recall trong [0.8, 1] sẽ lấy precision max là 0.5 do nó nằm bên phải). Đến đây chắc cũng đã dễ hiểu hơn.

<img src="https://miro.medium.com/max/941/1*pmSxeb4EfdGnzT6Xa68GEQ.jpeg" style="display:block; margin-left:auto; margin-right:auto">

Như vậy đường màu cam sẽ chuyển thành đường màu xanh. Giá trị AP tính được sẽ ít bị ảnh hưởng bởi các thay đổi nhỏ. Tổng quát ta có thể ghi lại

$$ p_{interp}(r) = \underset{\tilde{r} \geq r} {\text{max} ~ P(\tilde{r})} $$

### 11-Interpolated AP

PASCAL VOC là bộ dataset phổ biến cho object detection. Trước VOC Challenge 2010 dùng mAP được tính dựa trên 11-interpolateded AP. Dự đoán được coi là positive nếu $IoU \geq 0.5$. Nếu multiple detections của cùng object được phát hiện, nó chỉ tính một cái, các cái còn lại được coi là negative.

>Chú ý: Ở đây đang nói tới giai đoạn sau cùng, sau khi thực hiện inference, NMS rồi còn lại bao nhiêu bounding boxes chúng ta sẽ đi so sánh với groud-truth boxes để xác định positive, negative.

Trong PASCAL VOC 2008, trung bình của 11 điểm interpolated AP được xác định.

<img src="https://miro.medium.com/max/941/1*naz02wO-XMywlwAdFzF-GA.jpeg" style="display:block; margin-left:auto; margin-right:auto">

Đầu tiên chúng ta chia các giá trị recall trong [0, 1] thành 11 điểm - 0, 0.1, ..., 0.9, 1.0. Sau đó chúng ta tính trung bình của các interpolated precisions cho 11 giá trị recall đó.

$$AP = \frac{1}{11} (AP_r(0) + AP_r(0.1)+...+AP_r(1.0))$$

Trong ví dụ này $AP = (5 \times 1.0 + 4 \times 0.57 + 2 \times 0.5)/11$

Công thức tổng quát ở đây:

$$AP = \frac{1}{11} \sum_{r\in 0, 0.1, ... ,1.0} AP_r = \frac{1}{11} \sum_{r\in 0, 0.1, ... ,1.0} P_{interp}(r)$$

trong đó $ P_{interp}(r) = \underset{\tilde{r} \geq r} {\text{max} ~ P(\tilde{r})} $

Đối với 20 classes trong PASCAL VOC chúng tá sẽ tính $AP$ cho từng class. Interpolated method (phương pháp nội suy) này là phương pháp tính gần đúng tuy nhiên nó gặp một số vấn đề. Đầu tiên nó ít chính xác, thứ hai nó mất khả năng đo lường sự khác nhau giữa các phương pháp mà AP thấp. Do đó cần một cách tính AP khác được áp dụng sau năm 2008 cho PASCAL VOC.

## AP - Area under the curve AUC

Đối với PASCAL VOC 2010-2012 chúng ta sẽ lấy các giá trị recall $r_1, r_2...$ bất cứ khi nào maximum precision bị giảm xuống. Với sự thay đổi này chúng ta đo được chính xác diện tích dưới precision-area curve sau khi loại bỏ đường zigzag. 

Thay vì lấy 11 điểm, chúng ta sẽ lấy $p(r_i)$ mỗi khi nó giảm xuống và tính $AP$ như tổng diện tích của tất cả các blocks hình chữ nhật:

$$ AP = \sum (r_{n+1}-r_n) ~ P_{interp}(r_{n+1})$$

$$ P_{interp}(r) = \underset{\tilde{r} \geq r} {\text{max} ~ P(\tilde{r})} $$

Định nghĩa này được gọi là Area Under Curve (AUC). 

<img src="https://miro.medium.com/max/941/1*TAuQ3UOA8xh_5wI5hwLHcg.jpeg" style="display:block; margin-left:auto; margin-right:auto">


## COCO mAP

Các nghiên cứu mới nhất hay đưa ra kết quả trên mỗi tập dữ liệu COCO. Trong COCO mAP interpolated AP cho 100 điểm được tính. Đối với COCO, AP là trung bình trên nhiều IoU (IoU nhỏ nhất được coi là positive). **AP@[.5:.95]** tương ứng với average AP cho $IoU$ từ 0.5 đến 0.95 với step là 0.05. Trong các cuộc thi COCO, AP là trung bình của 10 $IoU$ trên 80 categories. Dưới đây là một số metrics cho COCO dataset:

<img src="https://miro.medium.com/max/941/1*_IkyrFHlqt_xCovk7l0rQQ.png" style="display:block; margin-left:auto; margin-right:auto">

Kí hiệu $AP^{small/medium/large}$: AP cho small/medium/large object (object có kích thước: nhỏ hơn 32×32; từ 32×32 đến 96×96; lớn hơn 96×96).

Dưới đây là kết quả AP cho YOLOv3:

<img src="https://miro.medium.com/max/941/1*09w7--mzDQ3Nqd81t-XOjw.png" style="display:block; margin-left:auto; margin-right:auto">

Trong hình trên $AP_{75}$ tương với với AP với $IoU=0.75$.

mAP (mean average precision) là trung bình của AP. Trong một số trường hợp chúng ta tính AP cho mỗi class và lấy trung bình. Nhưng trong một số trường hợp khác AP và mAP lại giống nhau. 
> AP is averaged over all categories. Traditionally, this is called “mean average precision” (mAP). We make no distinction between AP and mAP (and likewise AR and mAR) and assume the difference is clear from context

mAP được tính bằng cách lấy trung bình AP trên tất cả các class và/hoặc trên tất cả IoU threshold (phụ thuộc vào từng hoàn cảnh).

Trong PASCAL VOC2007 challenge, AP cho một class được tính cho một IoU threshold. Do đó mAP là trung bình của AP trên toàn bộ các classes (duy nhất 1 IoU threshold).

Trong COCO 2017 challenge, mAP là trung bình trên toàn bộ các clasess và 10 IoU thresholds.

<img src="https://miro.medium.com/max/765/1*BSyRF9Cvs4xlRKVxEOPyvA.png" style="display:block; margin-left:auto; margin-right:auto">

*Precision-recall curve for SSD model for 4 object classes, where IoU threshold is 0.5. Van Etten, A. (2019, January)*

Có một repo rất hay giúp chúng ta tính mAP cho các bài toán object detection, các bạn xem [ở đây](https://github.com/rafaelpadilla/Object-Detection-Metrics).

## Tài liệu tham khảo
1. https://github.com/rafaelpadilla/Object-Detection-Metrics
2. https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173
3. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.average_precision_score.html
4. https://towardsdatascience.com/map-mean-average-precision-might-confuse-you-5956f1bfa9e2#:~:text=mAP%20(mean%20average%20precision)%20is,averaged%20to%20get%20the%20mAP.&text=The%20mean%20Average%20Precision%20or,different%20detection%20challenges%20that%20exist.
5. https://pro.arcgis.com/en/pro-app/2.7/tool-reference/image-analyst/how-compute-accuracy-for-object-detection-works.htm#:~:text=In%20object%20detection%20and%20classification,can%20be%20true%20or%20false.&text=True%20positive—The%20model%20predicted,tree%2C%20and%20it%20is%20incorrect.

