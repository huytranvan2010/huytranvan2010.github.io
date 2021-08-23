---
layout: post
title: "[Math4CV-8] Matrix multiplication"
tags: [Math4CV]
comments: true
---

Ma trận $\textbf{A} \in \mathbb{R}^{m \times p} $, ma trận $\textbf{B} \in \mathbb{R}^{p \times n} $. $\textbf{C} \in \mathbb{R}^{m \times n}$ là tích của ma trận $\textbf{A}$ với ma trận $\textbf{B}$. Các phần tử của ma trận $\textbf{C}$ được xác định như sau:

$$c_{ij} = \sum_{k=1}^{p} a_{ik} b_{kj} $$

**Nhận xét:** $c_{ij}$ sẽ là tích vô hướng của vector hàng  \\(\textbf{a}_{i*}\\) của ma trận $\textbf{A}$ với vector cột $textbf{b}_{*j}$ của ma trận $\textbf{B}$ 

Một số tính chất $\textbf{A}, \textbf{E} \in \mathbb{R}^{m \times p} $, $\textbf{B} \in \mathbb{R}^{p \times n} $:

$$ (\textbf{A} + \textbf{E})\textbf{B} = \textbf{A} \textbf{B} + \textbf{E} \textbf{B} $$

$$ (\textbf{A} \textbf{B})^T = \textbf{B}^T \textbf{A}^T $$

**Tip**: có ngoài cách nhân ma trận ở trên có thể nhân ma trận đơn giản theo 2 cách nữa như sau:
- Cột của ma trận $\textbf{C}$ là tích của ma trận $\textbf{A}$ và cột ma trận $\textbf{B}$ tương ứng. 
- Hàng của ma trận $\textbf{C}$ là tích của hàng ma trận $\textbf{A}$ tương ứng và ma trận $\textbf{B}$. 

Hãy thử xem, điều trên là đúng đấy.

$\textbf{a} $ là vector hàng có chiều $1 \times n, \textbf{a} \in \mathbb{R}^{1 \times n}$  (hiểu là matrix cũng được).
$\textbf{b} $ là vector cột có chiều $n \times 1, \textbf{a} \in \mathbb{R}^{n \times 1}$.

$\textbf{a} \cdot \textbf{b}$ là ma trận có chiều $1 \times 1$ (real number), $rank(\textbf{a} \cdot \textbf{b}) = 1$

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

$\textbf{b} \cdot \textbf{a}$ là ma trận có chiều $n \times n$ (real number), $rank(\textbf{a} \cdot \textbf{b}) = 1$ (điều này khá rõ ràng vì chỉ có 1 vector độc lập tuyến tính).

$$
\begin{bmatrix}
 b_1\\
 b_2\\
 ...\\
 b_n\\
\end{bmatrix}
\begin{bmatrix}
 a_1&  a_2&  ...& a_n&\\
\end{bmatrix} = 
\begin{bmatrix}
 b_1 a_1&  b_1 a_2&  ...&  b_1 a_n&\\
 b_2 a_1&  b_2 a_2&  ...&  b_2 a_n&\\
 ...&  ...&  ...&  ...&\\
 b_n a_1&  b_n a_2&  ...&  b_n a_n&\\
\end{bmatrix}
$$

Có thể dùng matrix multiplication để thể hiện dot product của 2 vector. Ví dụ $\textbf{x}, \textbf{y} $ là 2 vector hàng  $\in \mathbb{R}^{1 \times n}$:

$$ (\mathbf{x}, \mathbf{y}) =  \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^{n}x_i y_i = \mathbf{x} \cdot \mathbf{y}^T$$

thường để hàng nhân với cột.






