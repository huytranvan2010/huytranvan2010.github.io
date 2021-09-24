---
layout: post
mathjax: true
title: "[Math4CV-9] Linear transformations"
tags: [Math4CV]
comments: true
---

**Linear transformations of vector spaces - Ánh xạ tuyến tính**

Cho ma trận $\textbf{A} \in \mathbb{R}^{m \times n} $. Có thể sử dụng ma trận $\textbf{A}$ để chuyển đổi từ không gian $\mathbb{R}^{n \times 1} $ vào không gian $ \mathbb{R}^{m \times 1} $ bằng phép nhân ma trận:

$$ \textbf{y} = \textbf{A} \textbf{x} $$

Vector cột $ \textbf{x} \in \mathbb{R}^{n \times 1} $ được chuyển thành vector cột $ \textbf{y} \in \mathbb{R}^{m \times 1} $ bằng cách nhân với ma trận $\textbf{A}$.

$$ y_i = a_{i1}x_1 + a_{i2}x_2 + ... + a_{im}x_m = a_{i*} \cdot \textbf{x} $$

Phần tử thứ $i^{th}$của vector $\textbf{y}$ bằng dot product của hàng $i^{th}$ ma trận $\textbf{A}$ với vector cột $\textbf{x}$.

Bất kỳ ánh xạ (transformation) nào cũng được đặc trưng bởi 2 không gian con. Một cái được gọi là **Kernel** hay (null space of transformation), một cái được gọi là **Range** hay image space of transformation.

**Kernel** của matrix A (hay kernel của transformation) là tập con của $\mathbb{R}^{n \times 1}$:

$$Ker(\textbf{A}) = \left\{ \textbf{x} \in \mathbb{R}^{n \times 1}: ~~\textbf{A}\textbf{x} = 0 \right\}$$

Kernel của matrix $\textbf{A}$ là không gian con tuyến tính của $\mathbb{R}^{n \times 1}$.

**Range** của matrix A là tập con của $\mathbb{R}^{m \times 1}$:

$$Range(\textbf{A}) = \left\{ \textbf{y} \in \mathbb{R}^{m \times 1}: \text{tồn tại} ~ \textbf{u} \in \mathbb{R}^{n \times 1}, \textbf{y} = \textbf{A} \textbf{u} \right\}$$

Range của matrix $\textbf{A}$ là không gian con tuyến tính của $\mathbb{R}^{m \times 1}$.

**Formula of dimension**

$$dim(Ker(\textbf{A})) + dim(Range(\textbf{A})) = n$$

Số chiều của $Range(\textbf{A})$ bằng với $Rank(\textbf{A})$. Thực chất $Range(\textbf{A})$ là span các cột của matrix $\textbf{A}$.

$$Range(\textbf{A}) = span(a_{*1}, a_{*1}, \dots, a_{*n})$$

Để tìm ảnh của bất kì vector $\textbf{x} \in \mathbb{R}^{n \times 1}$ bằng ánh xạ qua matrix $\textbf{A}$ chúng ta đi tìm ảnh các của vector của cơ sở chuẩn $\textbf{u}_1, \textbf{u}_2, \dots, \textbf{u}_n$ của không gian $\mathbb{R}^{n \times 1}$:

$$\textbf{x} = (x_1, x_2, \dots, x_n)^T = x_1 \textbf{u}_1 + x_2 \textbf{u}_2 + \dots + x_n \textbf{u}_n$$

Do đó

$$\textbf{A} \textbf{x} = x_1 \textbf{A}\textbf{u}_1 + x_1 \textbf{A}\textbf{u}_1 + \dots + x_n \textbf{A}\textbf{u}_n$$

Theo định nghĩa của cơ sở chuẩn $\textbf{A}\textbf{u}\_i$ chính là cột $a\_{ * i}$ của matrix $\textbf{A}$.





