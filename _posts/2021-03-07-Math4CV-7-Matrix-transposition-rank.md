---
layout: post
mathjax: true
title: "[Math4CV-7] Rows and columns of matrix. Transposition. Rank"
tags: [Math4CV]
comments: true
---

$\mathbb{R}^{1 \times m}$ - không gian vector hàng với dimension $m$.

$\mathbb{R}^{n \times 1}$ - không gian vector cột với dimension $n$.

Bất kì ma trận  $\mathbf{A} \in \mathbb{R}^{m \times n} , \mathbf{A} = (a_{ij})$ cũng có thể được biểu diễn thông qua các vector hàng hoặc vector cột của chúng.

Ví dụ biểu diễn ma trận như cột của các vector hàng:
$$ \mathbf{A} = 
\begin{bmatrix}
a_{1*} \\
a_{2*} \\
\vdots \\
a_{m*}
\end{bmatrix}, ~~ 
a_{i*} = 
\begin{bmatrix}
a_{i1}& a_{i2}& \dots& a_{in}
\end{bmatrix}, i=1, 2, ..., m  $$

Frobenius norm: $ \Vert \mathbf{A} \Vert_F^{2} = \Vert a_{1 * } \Vert_2^{2} + \Vert a_{2 * } \Vert_2^{2} + ... + \Vert a_{m * } \Vert_2^{2} $

Ví dụ biểu diễn ma trận như hàng của các vector cột:

$$ \mathbf{A} = 
\begin{bmatrix} 
a_{* 1}& a_{* 2}& \dots& a_{*n}
\end{bmatrix},~~ 
a_{*j} = 
\begin{bmatrix}
a_{1j} \\ 
a_{2j} \\
\vdots \\
a_{mj} 
\end{bmatrix}, j=1, 2, ..., n  $$

Frobenius norm: $ \Vert \mathbf{A} \Vert_F^{2} = \Vert a_{* 1} \Vert_2^{2} + \Vert a_{ * 2} \Vert_2^{2} + ... + \Vert a_{ * n} \Vert_2^{2} $


Ma trận  $A \in \mathbb{R}^{m \times n} $ có ma trận chuyển vị là ma trận  $A^{T} \in \mathbb{R}^{n \times m} $. Ma trận ban đầu viết dưới dạng vector cột của các hàng, khi chuyển vị hàng sẽ biến thành cột, do đó ma trận chuyển vị có các cột là chuyển vị của các hàng.

$$ \mathbf{A} = 
\begin{bmatrix}
a_{1*} \\
a_{2*} \\
... \\
a_{m*}
\end{bmatrix} ~~~~~~~~~~ 
\mathbf{A}^T = 
\begin{bmatrix}
a_{1*}^T& a_{2*}^T& \dots& a_{m*}^T 
\end{bmatrix}$$

Ma trận ban đầu viết dưới dạng vector hàng của các cột, khi chuyển vị cột sẽ biến thành hàng, do đó ma trận chuyển vị có các hàng là chuyển vị của các cột.

$$ \mathbf{A} = 
\begin{bmatrix} 
a_{*1}& a_{*2}& \dots& a_{*n}
\end{bmatrix} ~~~~~~~~~~  
\mathbf{A}^T = 
\begin{bmatrix}
a_{*1}^T \\
a_{*2}^T \\
\vdots \\
a_{*m}^T 
\end{bmatrix}$$

Một số tính chất của ma trận chuyển vị:
- $(\mathbf{A}^T)^T = \mathbf{A}$
- $(\mathbf{A} + \mathbf{B})^T = \mathbf{A}^T + \mathbf{B}^T$
- $ (c \mathbf{A})^T= c \mathbf{A}^T$

Frobenius norm: $ \lVert \mathbf{A} \rVert_F = \lVert \mathbf{A}^T \rVert_F $

## Rank of matrix (Hạng của ma trận)

**Motivation:** Trong xử lý số liệu các quan sát thường được biểu diễn dưới dạng matrix. Mỗi hàng của matrix là một quan sát, giá trị ở các cột tương ứng với features (hoặt attributes) của quan sát.

$ \mathbf{X} = (a_{i j})$, $i=1..n $ là số thự tự quan sát, $j=1..m$ là số thứ tự của features.

**Dimension reduction problem**: chúng ta có thể giảm số lượng features hay số lượng quan sát mà vẫn không mất thông tin. Rank of matrix (hạng của ma trận) giúp ta giải quyết vấn đề này.

**Hạng của ma trận** $\mathbf{A} \in \mathbb{R}^{m \times n} $ là số lượng lớn nhất các cột độc lập tuyến tính, đó cũng chính là số lượng lớn nhất các hàng độc lập tuyến tính, như vậy thì

$$rank(\mathbf{A}) \leq \min\left\{m, n \right\}$$

Hạng của ma trận bằng số chiều của:
* Không gian con $\text{span}(a_{1 * }, a_{2 * }...a_{m * }) \in \mathbb{R}^{1 \times n}$ - không gian con của các vector hàng (tìm ra số lượng vector lớn nhất độc lập tuyến tính)
* Không gian con $\text{span}(a_{ * 1}, a_{ * 2}...a_{ * n}) \in \mathbb{R}^{m \times 1}$ - không gian con của các vector cột (tìm ra số lượng vector lớn nhất độc lập tuyến tính)

Một số tính chất:
* $rank(\mathbf{A}^T) = rank(\mathbf{A})$
* $rank(\mathbf{A}) = \dim(span(a_{1 * }, a_{2 * }...a_{m * }))$
* $rank(\mathbf{A}) = \dim(span(a_{ * 1}, a_{ * 2}...a_{ * n}))$

Ví dụ ma trận

$$\mathbf{A} = \begin{bmatrix}
 &2  &0  &-1  &3  &0  &1\\
 &6  &0  &-3  &9  &0  &3\\
\end{bmatrix}$$

có $rank(\mathbf{A}) = 1$ do $a_{2 * } = 3a_{1 * }$

Để xác định hạng của ma trận có thể dùng phương pháp Gaussian (giống khi giải hệ phương trình). Các bạn tự tìm hiểu thêm cách thực hiện nhé. 


