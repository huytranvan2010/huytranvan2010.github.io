---
layout: post
title: "Matrix calculus"
tags: [Giải Tích, Đạo Hàm]
comments: true
---

Trong bài này chúng ta sẽ tìm hiểu về matrix calculus. Đây là kiến thức hữu ích cho chúng ta để có thể tiếp cận dễ hơn với các thuật toán. Liên quan đến việc tính đạo hàm theo vector có hai quy ước: **numerator layout (Jacobian formulation)** và **denominator layout (Hessian formulation)**. Hai quy ước này khác nhau trong việc đạo hàm scalar theo vector, đạo hàm của vector theo scalar để theo vector hàng hay cột. Trong bài này chúng ta sẽ dùng theo quy ước numerator layout.

Chúng ta có vector $\mathbf{x}$:

$$ \mathbf{x} = 
\begin{bmatrix}
x_1\\ 
x_2\\ 
\vdots\\ 
x_3
\end{bmatrix} = [x_1 ~x_2 \dots x_n]^T
$$   

## Đạo hàm của hàm cho giá trị là số vô hướng

**Đạo hàm của scalar theo scalar**

$f(x): \mathbb{R} \rightarrow \mathbb{R}$

$$\frac{\partial f}{\partial x}$$

Ví dụ

$$\frac{\partial (3x^2 +2)}{\partial x} = 6x$$

**Đạo hàm của scalar theo vector**

$f(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}$

$$\frac{\partial f}{\partial \mathbf{x}} = \left [ \frac{\partial f}{\partial x_1} ~~\frac{\partial f}{\partial x_2} \dots \frac{\partial f}{\partial x_n} \right ] ~~~~~ (1) $$

Nhớ nhé ở đây chúng ta nhận được vector hàng.

Ví dụ  

$$\frac{\partial f}{\partial \mathbf{x}}(x_1^2 + 2x_2^2) = \left [ \frac{\partial f}{\partial x_1} ~~ \frac{\partial f}{\partial x_2} \right ] = \left [ 2x_1 ~~ 4x_2 \right ]$$

**Đạo hàm của scalar theo matrix**

**Đạo hàm của vector theo scalar**

$\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^m$

$$ \frac{\partial \mathbf{f}}{\partial x} = 
\begin{bmatrix}
\frac{\partial f_1}{\partial x}\\ 
\frac{\partial f_2}{\partial x}\\ 
\vdots\\ 
\frac{\partial f_m}{\partial x}
\end{bmatrix} ~~~~~ (2) $$

Ví dụ 

$$ \frac{\partial \mathbf{f}}{\partial x} = 
\begin{bmatrix}
\frac{\partial x_2}{\partial x}\\  
\frac{\partial x_3 + x}{\partial x}
\end{bmatrix} =
\begin{bmatrix}
\frac{\partial 2x}{\partial x}\\  
\frac{\partial 3x^2 + 1}{\partial x}
\end{bmatrix}
$$

**Đạo hàm của vector theo vector**

$\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$

$$ \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \nabla_{\mathbf{x}} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_1(\mathbf{x})}{\partial x_n}\\ 
\frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_2(\mathbf{x})}{\partial x_n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_m(\mathbf{x})}{\partial x_1}&  \frac{\partial f_m(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} \in \mathbb{R}^{m \times n} ~~~~~ (3) $$

Chúng ta có thể suy ra công thức này từ các công thức trên như sau. Từ công thức (1) gradient của $\mathbf{f}$ theo vector $\mathbf{x}$ là một vector hàng.
$$\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \left [ \frac{\partial \mathbf{f}}{\partial x_1} ~~\frac{\partial \mathbf{f}}{\partial x_2} \dots \frac{\partial \mathbf{f}}{\partial x_n} \right ] ~~~~~ (4) $$

Đạo hàm của một vector theo một số vô hướng là vector cột như sau.

$$ \frac{\partial \mathbf{f}}{\partial x_i} = 
\begin{bmatrix}
\frac{\partial f_1}{\partial x_i}\\ 
\frac{\partial f_2}{\partial x_i}\\ 
\vdots\\ 
\frac{\partial f_m}{\partial x_i}
\end{bmatrix} $$

Thay công thức trên vào công thức (4) chúng ta sẽ nhận được (3). Không phức tạp quá phải không nào?

Ở đây chúng ta cũng có khái niệm **Jacobian** của $\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$ là ma trận các đạo hàm riêng bậc  một có kích thước $m \times n$.

$$\mathbf{J} = \nabla_\mathbf{x} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_1(\mathbf{x})}{\partial x_n}\\ 
\frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_2(\mathbf{x})}{\partial x_n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_m(\mathbf{x})}{\partial x_1}&  \frac{\partial f_m(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} ~~~~~~ J_{ij} = \frac{\partial f_i}{\partial x_j}
$$

Trường hợp đặc biệt $m=1$ chúng ta có Jacobian của $f(\mathbf{x})$ là một vector hàng (ma trận với kích thước $1 \times n$) như công thức (1).

Ví dụ:


## Một số ví dụ

**Ví dụ 1**

Cho hàm số $\mathbf{f}(\mathbf{x}) = \mathbf{A}\mathbf{x}$, trong đó $\mathbf{f}(\mathbf{x}) \in \mathbb{R}^m$, $\mathbf{A} \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$. Xác định gradient $\nabla_\mathbf{x} \mathbf{f} = d\mathbf{f} / d\mathbf{x}$

>Chú ý: ở đây khi ghi $\mathbb{R}^n$ chúng ta hiểu mặc định đó là vector có $n$ chiều, vector cột hay matrix có kích thước $\mathbb{R}^{n \times 1}$.

Bởi vì $\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$ nên theo công thức (3), $\nabla_\mathbf{x} \mathbf{f}$ sẽ có kích thước là $\mathbb{R}^{m \times n}$.

Theo đề bài chúng ta sẽ có $f_i(\mathbf{x}) = \sum_{j=1}^{n}A_{ij}x_j \Rightarrow \frac{\partial f_i}{\partial x_j} = A_{ij}$

$$\nabla_\mathbf{x} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_1(\mathbf{x})}{\partial x_n}\\ 
\frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_2(\mathbf{x})}{\partial x_n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_m(\mathbf{x})}{\partial x_1}&  \frac{\partial f_m(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} =
\begin{bmatrix}
A_{11}&  A_{12}&  \dots& A_{1n}\\ 
A_{21}&  A_{22}&  \dots& A_{2n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
A_{m1}&  A_{m2}&  \dots& A_{mn}\\ 
\end{bmatrix} = \mathbf{A} \in \mathbb{R}^{m \times n}
$$

$$\nabla_\mathbf{x} \mathbf{Ax} = \mathbf{A}$$

**Ví dụ 2**

$\mathbf{X} \in \mathbb{R}^{m \times n}$, $\mathbf{w} \in \mathbb{R}^{n}$,  $\mathbf{y} \in \mathbb{R}^{m}$. Loss function:

$$ L = ||\mathbf{X}\mathbf{w} - \mathbf{y}||^2$$

đi tính $\frac{\partial L}{\partial \mathbf{w}}$.

Đặt $\mathbf{a} = \mathbf{X} \mathbf{w}$, $\mathbf{b} = \mathbf{a} - \mathbf{y}$, khi đó $L = ||\mathbf{b}||^2$.

$$
\begin{align*}
\frac{\partial L}{\partial \mathbf{w}} & = \frac{\partial L}{\partial \mathbf{b}} ~ \frac{\partial \mathbf{b}}{\partial \mathbf{a}} ~ \frac{\partial \mathbf{a}}{\partial \mathbf{w}} \\ 
 &= \frac{\partial ||\mathbf{b}||^2}{\partial \mathbf{b}} ~ \frac{\partial (\mathbf{a} - \mathbf{y})}{\partial \mathbf{a}} ~ \frac{\partial \mathbf{X} \mathbf{w}}{\partial \mathbf{w}} \\
 &= 2\mathbf{b}^T ~ \mathbf{I} ~ \mathbf{X} \\
 &= 2(\mathbf{X}\mathbf{w} - \mathbf{y})^T ~ \mathbf{X}
\end{align*}
$$

Công thức này nhìn hơi khác một chút do với công thức chúng ta thường thấy trong các khóa học ML. Lý do bởi vì trong các khóa ML sử dụng denominator layout.


## Tài liệu tham khảo
1. https://en.wikipedia.org/wiki/Matrix_calculus#Numerator-layout_notation 