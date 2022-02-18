---
layout: post
title: "Multi-label classification"
tags: [Classification]
comments: true
---

Nhóm mình đang có bài toán liên quan đến multi-label classification. Do đó mình viết bài này để chia sẻ một số vấn đề xung quanh multi-label classification.

## Multi-label classification khác gì multi-class classification

Chắc mọi người đã quen với bài toán multi-class classification như phân loại chữ số viết tay MNIST chẳng hạn. Trong bài toán này mỗi ảnh sẽ chứa **duy nhất một class** từ 0 đến 9 đại diện cho các chữ số. Số units của output layer sẽ bằng với số classes muốn phân loại. Thường sẽ áp dụng softmax activation function cho output layer.

Trong khi đó, bài toán multi-label classification, mỗi dữ liệu có thể chứa nhiều class. Ví dụ đối với dữ liệu ảnh chẳng hạn, ảnh có thể được gán nhãn vừa chứa chó vừa chứa mèo. Số units của output layer bằng với số classes có thể chứa trong mỗi ảnh. Thường chúng ta sẽ dùng sigmoid activation function cho output layer.

<img src="https://gombru.github.io/assets/cross_entropy_loss/multiclass_multilabel.png">

## Metrics cho multi-label classification

### Exact match ratio (EMR) - tỉ lệ khớp chính xác

$$acc = \frac{\text{số dự đoán đúng}}{\text{tổng số dự đoán}} = \frac{1}{n}\sum_{i=1}^{n}[\mathbf{I}(\mathbf{y}^{(i)} =\mathbf{\hat{y}}^{(i)}]$$

trong đó, $n$ là số training examples
$\mathbf{y}^{(i)}$ là true labels cho training example $i$
$\mathbf{\hat{y}}^{(i)}$ là prediction cho training example $i$
Exact match ratio được implement trong scikit-learn, các bạn có thể xem thêm [tại đây](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html).

Dữ liệu được coi là dự đoán đúng nếu prediction trùng với nhãn ban đầu. Ví dụ ảnh ban đầu chứa chó, mèo, cừu, khi dự đoán cũng chứa chó, mèo, cừu thì được coi là dự đoán đúng. Nếu dự đoán ảnh chỉ chứa chó, mèo thì là dự đoán sai.

EMR giúp chúng ta đánh giá tổng thể các classes, không phản ánh được đối với từng class riêng lẻ.

```python
def emr(y_true, y_pred):
    row_indicators = np.all(y_true == y_pred, axis = 1) # axis = 1 will check for equality along rows. y_true == y_pred trả về matrix chứa True, False, nếu tất cả các ptử trên một hàng là True thì trả về True cho hàng đó
    exact_match_count = np.sum(row_indicators)	# row_indicators contains only True or False
    return exact_match_count/len(y_true)
```

### Harming loss

Harming loss tính tỉ lệ các labels dự đoán không chính xác trên tổng số labels.

$$ \text{Harming loss} = \frac{1}{nL}\sum_{i=1}^{n} \sum_{j=1}^{L}I(y^{(i)}_j \neq \hat{y}^{(i)}_j )$$

trong đó
$y^{(i)}_j$ là true labels cho training example $i$ và class $j$
$\hat{y}^{(i)}_j$ là prediction cho training example $i$ và class $j$
$L$ chính là số chiều của một label của dữ liệu

## Label-based metrics (các metrics dựa trên label)

Không giống với example-based metrics, label-based metrics được thực hiện cho mỗi class riêng rẽ, sau đó sẽ lấy trung bình trên tất cả các classes.
Tất cả các metrics dùng cho binary classification đều có thể dùng được cho label-based metrics.
- Những metrics được tính trên class, sau đó mới lấy trung bình trên toàn bộ classes được gọi là **macro-average**
- Những metrics được tính trên toàn bộ các classes luôn được gọi là **micro average**.

Chúng ta cùng đi chi tiết vào các metrics để dễ hiểu hơn.

### Macro-average
**Macro-average accuracy**

Công thức chung của accuracy

$$A = \frac{TP + TN}{\text{no of examples}}$$

Tuy nhiên trong bài toán multi-label classification đôi khi chỉ quan tâm tới các example có true label hoặc predicted labels bằng 1, do đó công thức cho accuracy sẽ hơi khác chút.

$$A = \frac{TP}{TP + FP + FN}$$

Xác định accuracy cho mỗi class trong bài toán multi-label classifcation:

$$A_{macro}^j = \frac{\sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{i=1}^n [y^{(i)}_j \vee \hat{y}^{(i)}_j]} ~~~ (1)$$

trong đó:
- $\wedge$ - logical AND operator
- $\vee$ - logical OR operator

$$ \text{Accuracy\_macro} = \frac{\sum_{j=1}^{k}A_{macro}^j}{k}$$

Đơn giản có thể lấy riêng dự đoán của từng class (tương ứng một cột trong ma trận true labels hay prediction) rồi xác định accuracy cho class đó. Nhìn vào công thức (1) có thể nhận thấy điều này vì:
- Tử số chính là $TP$ - tổng số lần class đó (true label = 1) được dự đoán là class đó (predicted label = 1). Đây là lý do dùng toán tử logic AND. Chỗ này cần phải hiểu là khi nói tới từng class (chó chẳng hạn), nếu ảnh chứa chó được coi là Positive (vị trí tương ứng class chó bằng 1), không chứa chó được coi là negative (vị trí tương ứng với class chó bằng 0). Ở đây chỉ quan tâm đến chính class đó nên không tính $TN$.
- Mẫu số tương ứng với $TP + FP + FN$, không tính $TN$. Điều này có nghĩa rằng chỉ khi nào true label là 1 hoặc predicted label là 1 mới tính. Nếu true label và predicted label đều bằng 0 (tương ứng TN) thì không tính vào mẫu số. Việc xác định như này chỉ ám chỉ labels phải có liên quan đến class (label = 1).

**Macro-average precision** là trung bình cộng của các precision theo class.
Nhớ lại công thức của precision:

$$Precison = \frac{TP}{TP + FP}$$

Xác định precision cho mỗi class trong bài toán multi-label classifcation:

$$P_{macro}^j = \frac{\sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{i=1}^n [\hat{y}^{(i)}]} ~~~ (1)$$

$$ \text{Precision\_macro} = \frac{\sum_{j=1}^{k}P_{macro}^j}{k}$$

trong đó:
- $n$ - số training examples
- $y^{(i)}_j$ - true label cho training example $i$ và class $j$
- $\hat{y}^{(i)}_j$ - predicted label cho training example $i$ và class $j$
- $\wedge$ - AND operator
- $P_{macro}^j$ - precision cho class $j$, ở đây thêm chữ macro để ám chỉ nó dùng cho macro-average
- $k$ - số classes

<!-- **Chú ý**: kí hiệu $\left[ a \right] = \left\{\begin{matrix}
 0, a=0 \\
 1, a=1
\end{matrix}\right.$ -->

Đơn giản có thể lấy riêng dự đoán của từng class (tương ứng một cột trong ma trận true labels hay prediction) rồi xác định precision cho class đó. Nhìn vào công thức (1) có thể nhận thấy điều này vì:
- Tử số chính là $TP$ - tổng số lần class đó (true label = 1) được dự đoán là class đó (predicted label = 1). Đây là lý do dùng toán tử logic AND. Chỗ này cần phải hiểu là khi nói tới từng class (chó chẳng hạn), nếu ảnh chứa chó được coi là Positive (vị trí tương ứng class chó bằng 1), không chứa chó được coi là negative (vị trí tương ứng với class chó bằng 0) 
- Mẫu số là số lần dự đoán class $j$ là 1, nó chính là $TP + FP$ cho class đó

**Macro-average Recall**

Nhớ lại công thức của Recall:

$$Recall = \frac{TP}{TP + FN}$$

Xác định Recall cho mỗi class trong bài toán multi-label classifcation:

$$R_{macro}^j = \frac{\sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{i=1}^n [y^{(i)}]} ~~~ (2)$$

$$ \text{Recall\_macro} = \frac{\sum_{j=1}^{k}R_{macro}^j}{k}$$

Tương tự như trên, có thể lấy riêng dự đoán của từng class (tương ứng một cột trong ma trận true labels hay prediction) rồi xác định Recall cho class đó. Nhìn vào công thức (2) có thể nhận thấy điều này vì:
- Tử số chính là $TP$ - tổng số lần class đó (true label = 1) được dự đoán là class đó (predicted label = 1). Đây là lý do dùng toán tử logic AND. Chỗ này cần phải hiểu là khi noi tới từng class (chó chẳng hạn), nếu ảnh chứa chó được coi là Positive (vị trí tương ứng class chó bằng 1), không chứa chó được coi là negative (vị trí tương ứng với class chó bằng 0) 
- Mẫu số là số lần true labels cho class $j$ là 1, nó chính là $TP + FN$ cho class đó - số lần Positive thực tế.

**Macro-average F-Score** 
Macro-average F-Score được tính tương tự như F-score nhưng dựa trên macro-average precision và macro-average recall

Nhắc lại công thức tổng quát cho $F_\beta$ score:

$$F_{\beta} = ( 1 + \beta^2)\frac{\text{precision}\cdot\text{recall}}{\beta^2\cdot\text{precision} + \text{recall}}$$

do đó

$$F_{\beta}^{\text{macro}} = ( 1 + \beta^2)\frac{\text{Precision\_macro}\times \text{Recall\_macro}}{\beta^2\cdot\text{Precision\_macro} + \text{Recall\_macro}}$$

### Micro-average

**Micro-average accuracy**

Công thức tổng quát chung

$$
\text{micro-average accuracy} = \frac{\sum_{c=1}^C\text{TP}c}{\sum_{c=1}^C(\text{TP}c + \text{FP}c)}
$$

Multi-label classification:

$$\text{Accuracy\_micro} = \frac{\sum_{j=1}^k \sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{j=1}^k \sum_{i=1}^n [y^{(i)}_j \vee \hat{y}^{(i)}_j]} ~~~ (1)$$

Nhìn lên công thức tính accracy cho từng class ở phần macro-average accuracy, ta thấy tử số và mẫu số của nó bây giờ được lấy tổng theo các classes giống như công thức tổng quát bên trên.

**Micro-average precision**

Công thức tổng quát:
$$
\text{micro-average precision} = \frac{\sum_{c=1}^C\text{TP}c}{\sum_{c=1}^C(\text{TP}c + \text{FP}c)}
$$

Multi-label classification:
$$\text{Precision\_micro} = \frac{\sum_{j=1}^k \sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{j=1}^k \sum_{i=1}^n [\hat{y}^{(i)}]} ~~~ (1)$$

**Micro-average recall**
Công thức tổng quát:
$$
\text{micro-average recall} = \frac{\sum_{c=1}^C\text{TP}c}{\sum_{c=1}^C(\text{TP}c + \text{FN}c)}
$$

Multi-label classification:
$$R_{macro}^j = \frac{\sum_{j=1}^k  \sum_{i=1}^n [y^{(i)}_j \wedge \hat{y}^{(i)}_j]}{\sum_{j=1}^k \sum_{i=1}^n [y^{(i)}]}$$

Micro-average F-score cũng được tính dựa trên micro-average precision và micro-average recall.

### $\alpha$ - evaluation score

Boutell et.al. in [Learning multi-label scene](https://www.rose-hulman.edu/~boutell/publications/boutell04PRmultilabel.pdf) đã giwois thiệu phiên bản tổng quát của **Jaccard Similarity** để đánh giá multi-label prediction.

$$ \alpha - \text{evaluation score} = \left(1 - \frac{\beta M_x + \gamma F_x}{Y_x \vee P_x} \right)^\alpha$$

$$\alpha \geq 0, 0 \leq \beta, \gamma \leq 1, \beta=1 | \gamma =1$$

trong đó:
- $M_x$ - number of missed labels / False Negatives
- $F_x$ - False positive
- $Y_x$ - TP + FN
- $P_x$ - TP + FP
- $\vee$ - logical OR operator

## Tài liệu tham khảo
1. https://towardsdatascience.com/journey-to-the-center-of-multi-label-classification-384c40229bff
2. https://machinelearningmastery.com/multi-label-classification-with-deep-learning/
3. https://medium.datadriveninvestor.com/a-survey-of-evaluation-metrics-for-multilabel-classification-bb16e8cd41cd
4. https://viblo.asia/p/multi-label-classification-cho-bai-toan-tag-predictions-oOVlY2Lr58W
5. https://vnopenai.github.io/ai-doctor/vision/lung-abnormalities-classification-xray/models-and-experiments/
