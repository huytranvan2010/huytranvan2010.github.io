---
layout: post
mathjax: true
title: "[Math4CV-8] Matrix multiplication"
tags: [Math4CV]
comments: true
---

Ma trận $\mathbf{A} \in \mathbb{R}^{m \times p} $, ma trận $\mathbf{B} \in \mathbb{R}^{p \times n} $. $\mathbf{C} \in \mathbb{R}^{m \times n}$ là tích của ma trận $\mathbf{A}$ với ma trận $\mathbf{B}$. Các phần tử của ma trận $\mathbf{C}$ được xác định như sau:

$$c_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj} $$

**Nhận xét:** $c\_{ij}$ sẽ là tích vô hướng của vector hàng  $\mathbf{a}\_{i * }$ của ma trận $\mathbf{A}$ với vector cột $\mathbf{b}\_{ * j}$ của ma trận $\mathbf{B}$ 

Một số tính chất $\mathbf{A}, \mathbf{E} \in \mathbb{R}^{m \times p} $, $\mathbf{B} \in \mathbb{R}^{p \times n} $:

$$ (\mathbf{A} + \mathbf{E})\mathbf{B} = \mathbf{A} \mathbf{B} + \mathbf{E} \mathbf{B} $$

$$ (\mathbf{A} \mathbf{B})^T = \mathbf{B}^T \mathbf{A}^T $$

**Tips**: ngoài cách nhân ma trận ở trên có thể nhân ma trận đơn giản theo 2 cách nữa như sau:
- Cột của ma trận $\mathbf{C}$ là tích của ma trận $\mathbf{A}$ và cột ma trận $\mathbf{B}$ tương ứng. 
- Hàng của ma trận $\mathbf{C}$ là tích của hàng ma trận $\mathbf{A}$ tương ứng và ma trận $\mathbf{B}$. 

Hãy thử xem, điều trên là đúng đấy. Cách xác định này rất hay dùng để biểu diễn phép nhân ma trận trong một số biến đổi, ví dụ trong eigendecomposition của matrix.

$\mathbf{a} $ là vector hàng có chiều $1 \times n, \mathbf{a} \in \mathbb{R}^{1 \times n}$  (hiểu là matrix cũng được).
$\mathbf{b} $ là vector cột có chiều $n \times 1, \mathbf{a} \in \mathbb{R}^{n \times 1}$.

$\mathbf{a} \cdot \mathbf{b}$ là ma trận có chiều $1 \times 1$ (real number), $rank(\mathbf{a} \cdot \mathbf{b}) = 1$

$$
\begin{bmatrix}
 a_1&  a_2&  ...& a_n&\\
\end{bmatrix} 
\begin{bmatrix}
 b_1\\
 b_2\\
 ...\\
 b_n\\
\end{bmatrix} = 
\begin{bmatrix}
 \sum_{a_i b_i}\\
\end{bmatrix}
$$

$\mathbf{b} \cdot \mathbf{a}$ là ma trận có chiều $n \times n$ (real number), $rank(\mathbf{a} \cdot \mathbf{b}) = 1$ (điều này khá rõ ràng vì chỉ có 1 vector độc lập tuyến tính).

$$
\begin{bmatrix}
 b_1\\
 b_2\\
 \vdots \\
 b_n
\end{bmatrix}
\begin{bmatrix}
 a_1&  a_2& \dots& a_n
\end{bmatrix} = 
\begin{bmatrix}
 b_1 a_1&  b_1 a_2& \dots&  b_1 a_n\\
 b_2 a_1&  b_2 a_2& \dots&  b_2 a_n\\
 \dots& \dots& \dots& \dots\\
 b_n a_1&  b_n a_2& \dots& b_n a_n\\
\end{bmatrix}
$$

Có thể dùng matrix multiplication để thể hiện dot product của 2 vector. Ví dụ $\mathbf{x}, \mathbf{y} $ là 2 vector hàng  $\in \mathbb{R}^{1 \times n}$:

$$ (\mathbf{x}, \mathbf{y}) =  \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^{n}x_i y_i = \mathbf{x} \cdot \mathbf{y}^T$$

thường để vector hàng nhân với vector cột.






