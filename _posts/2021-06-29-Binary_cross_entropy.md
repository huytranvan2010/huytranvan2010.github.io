---
layout: post
title: "Binary crossentropy"
tags: [Loss Function]
comments: true
---

**Binary crossentropy** là loss function được sử dụng cho các bài toán binary classification (output layer có duy nhất 1 unit). Các bài toán này đi trả lời câu hỏi với duy nhất 2 sự lựa chọn (yes or no, A or B, 0 or 1, left or right) ví dụ bài toán phân loại chó mèo hay phân loại người ngựa. Một số câu hỏi độc lập có thể được trả lời cùng một lúc. Cái này hay được sử dụng trong bài toán Multi-label classification (một ảnh có thể chứa nhiều nhãn) hay binary image segmentation.

**Chú ý**: Đối với bài toán binary classification chúng ta hoàn toàn có thể dùng catagorical crossentropy với output layer có 2 units và ở đây sẽ dùng softmax activation function.


<img src="https://peltarion.com/static/binary_crossentropy_setup.svg">

$$ Loss = \frac{-1}{output ~ size } \sum_{i=1}^{output~size}y_i\ast log(\hat{y}_i) + (1-y_i) \ast log(1-\hat{y}_i)  $$

Trong đó $\hat{y}_i$ là scalar value trong model output, $y_i$ là target value tương ứng, $output ~ size$ là số scalar values trong model output (tương ứng với số output units). Ở đây loss đang tính cho một example, khi cần tính loss cho nhiều examples thì chúng ta chỉ việc lấy trung bình thôi.

## Activation function
**Sigmoid** là activation function duy nhất tương thích với binary crossentropy loss function. Chúng ta cần sử dụng nó ở layer cuối cùng. Có điều này do tương ứng với mỗi units của output layer chúng ta cần dự đoán một nhãn. Xem loss function ở trên có hàm $log$ do đó giá trị của $\hat{y}_i$ cần nằm trong $[0, 1]$. Hàm softmax có thể đảm bảo các giá trị nằm trong khoảng này nhưng không thể hiện được tính phân loại cho từng unit của output layer.

$$ sigmoid = \frac{1}{1+e^{-x}} $$

**Chú ý**: $\hat{y}_i$ nằm trong $[0, 1]$. Do đó layer cuối cùng chúng ta sẽ áp dụng `activation='sigmoid'`.

## Làm việc với Keras
```python
tf.keras.losses.BinaryCrossentropy(
    from_logits=False,
    label_smoothing=0,
    axis=-1,
    reduction="auto",
    name="binary_crossentropy",
)
```
Sử dụng cross-entropy này cho binary (0 or 1) classification problem. Loss function này cần inputs:
- `y_true`: 0 hoặc 1
- `y_pred`: số thực biểu thị giá trị (`[-inf, inf]` nếu để `from_logits=True` hoặc xác suất $[0, 1]$ nếu để `from_logits=False`).

## Tài liệu tham khảo
1. https://peltarion.com/knowledge-center/documentation/modeling-view/build-an-ai-model/loss-functions/binary-crossentropy 
2. https://keras.io/api/losses/probabilistic_losses/ 





