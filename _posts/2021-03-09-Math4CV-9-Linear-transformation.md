---
layout: post
mathjax: true
title: "[Math4CV-9] Linear transformations"
tags: [Math4CV]
comments: true
---

**Linear transformations of vector spaces - Ánh xạ tuyến tính**

Cho ma trận $\mathbf{A} \in \mathbb{R}^{m \times n} $. Có thể sử dụng ma trận $\mathbf{A}$ để chuyển đổi từ không gian $\mathbb{R}^{n \times 1} $ vào không gian $ \mathbb{R}^{m \times 1} $ bằng phép nhân ma trận:

$$ \mathbf{y} = \mathbf{A} \mathbf{x} $$

Vector cột $ \mathbf{x} \in \mathbb{R}^{n \times 1} $ được chuyển thành vector cột $ \mathbf{y} \in \mathbb{R}^{m \times 1} $ bằng cách nhân với ma trận $\mathbf{A}$.

$$ y_i = a_{i1}x_1 + a_{i2}x_2 + ... + a_{im}x_m = a_{i*} \cdot \mathbf{x} $$

Phần tử thứ $i^{th}$của vector $\mathbf{y}$ bằng dot product của hàng $i^{th}$ ma trận $\mathbf{A}$ với vector cột $\mathbf{x}$.

**Chú ý**: Nếu chúng ta biểu diễn data dưới dạng ma trận $\mathbf{X}$ với **mỗi cột là một example**, lúc này áp dụng linear transformation với ma trận $\mathbf{A}$ lên data $\mathbf{X}$ ta nhận được transformaed data $\mathbf{Y}$:

$$
\mathbf{Y} = \mathbf{A} \mathbf{X}
$$

Lúc này mỗi cột của ma trận $\mathbf{Y}$ tương ứng với một example mới.

Bất kỳ ánh xạ (transformation) nào cũng được đặc trưng bởi 2 không gian con. Một cái được gọi là **Kernel** hay (null space of transformation), một cái được gọi là **Range** hay image space of transformation.

**Kernel** của matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ (hay kernel của transformation) là tập con của $\mathbb{R}^{n \times 1}$:

$$Ker(\mathbf{A}) = \left\{ \mathbf{x} \in \mathbb{R}^{n \times 1}: ~~\mathbf{A}\mathbf{x} = 0 \right\}$$

Kernel của matrix $\mathbf{A}$ là không gian con tuyến tính của $\mathbb{R}^{n \times 1}$.

**Range** của matrix $\mathbf{A} \in \mathbb{R}^{m \times n}$ là tập con của $\mathbb{R}^{m \times 1}$:

$$Range(\mathbf{A}) = \left\{ \mathbf{y} \in \mathbb{R}^{m \times 1}: \text{tồn tại} ~ \mathbf{u} \in \mathbb{R}^{n \times 1}, \mathbf{y} = \mathbf{A} \mathbf{u} \right\}$$

Range của matrix $\mathbf{A}$ là không gian con tuyến tính của $\mathbb{R}^{m \times 1}$.

**Formula of dimension**

$$\dim(Ker(\mathbf{A})) + \dim(Range(\mathbf{A})) = n$$

Số chiều của $Range(\mathbf{A})$ bằng với $Rank(\mathbf{A})$. Thực chất $Range(\mathbf{A})$ là span các cột của matrix $\mathbf{A}$.

$$Range(\mathbf{A}) = span(a_{*1}, a_{*1}, \dots, a_{*n})$$

Để tìm ảnh của bất kì vector $\mathbf{x} \in \mathbb{R}^{n \times 1}$ bằng ánh xạ qua matrix $\mathbf{A}$ chúng ta đi tìm ảnh các của vector của cơ sở chuẩn $\mathbf{u}_1, \mathbf{u}_2, \dots, \mathbf{u}_n$ của không gian $\mathbb{R}^{n \times 1}$:

$$\mathbf{x} = (x_1, x_2, \dots, x_n)^T = x_1 \mathbf{u}_1 + x_2 \mathbf{u}_2 + \dots + x_n \mathbf{u}_n$$

Do đó

$$\mathbf{A} \mathbf{x} = x_1 \mathbf{A}\mathbf{u}_1 + x_1 \mathbf{A}\mathbf{u}_1 + \dots + x_n \mathbf{A}\mathbf{u}_n$$

Theo định nghĩa của cơ sở chuẩn $\mathbf{A}\mathbf{u}\_i$ chính là cột $a\_{ * i}$ của matrix $\mathbf{A}$.





