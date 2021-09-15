---
layout: post
title: "Matrix calculus"
tags: [Giải Tích, Đạo Hàm]
comments: true
---

Trong bài này chúng ta sẽ tìm hiểu về matrix calculus. Đây là kiến thức hữu ích cho chúng ta để có thể tiếp cận dễ hơn với các thuật toán. Liên quan đến việc tính đạo hàm theo vector có hai quy ước: **numerator layout (Jacobian formulation)** và **denominator layout (Hessian formulation)**. Hai quy ước này khác nhau trong việc đạo hàm scalar theo vector, đạo hàm của vector theo scalar để theo vector hàng hay cột. Trong bài này chúng ta sẽ dùng theo quy ước denominator layout. Tuy nhiên cũng có rất nhiều các tài liệu khác sử dụng numerator layout. Khi sử dụng nên nhất quán một cách để tránh nhầm lẫn.

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

**Ví dụ.**

$$\frac{\partial (3x^2 +2)}{\partial x} = 6x$$

**Đạo hàm của scalar theo vector**

$f(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}$

$$
\frac{\partial f}{\partial \mathbf{x}} = 
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\ 
\frac{\partial f}{\partial x_2}\\ 
\vdots\\ 
\frac{\partial f}{\partial x_n}
\end{bmatrix} ~~~~~ (1)
$$

Đạo hàm của scalar theo vector là một **vector cột**.

Khi lấy đạo hàm theo chuyển vector hàng (chuyển vị của vector cột) chúng ta nhận được vector hàng.

$$
(\frac{\partial f}{\partial \mathbf{x}})^T = \frac{\partial f}{\partial \mathbf{x}^T} = [\frac{\partial f}{\partial x_1} ~\frac{\partial f}{\partial x_2} \dots \frac{\partial f}{\partial x_n}]
$$

**Ví dụ.** $f(\mathbf{x}): \mathbb{R}^2 \rightarrow \mathbb{R}$, $f(\mathbf{x}) = x_1^{2} + 2x_2^{2}$

$$
\frac{\partial f}{\partial \mathbf{x}}(x_1^2 + 2x_2^2) = 
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\ 
\frac{\partial f}{\partial x_2}
\end{bmatrix} = 
\begin{bmatrix}
2x_1\\ 
4x_2
\end{bmatrix}
$$

Đạo hàm bậc hai của hàm số $f(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}$ là một **Hessian**.

$$
\nabla_\mathbf{x}^2 f(\mathbf{x}) = 
\begin{bmatrix}
\frac{\partial^2 f(\mathbf{x})}{\partial x_1^{2}}&  \frac{\partial^2 f(\mathbf{x})}{\partial x_1 \partial x_2}&  \dots& \frac{\partial^2 f(\mathbf{x})}{\partial x_1 \partial x_n}\\ 
\frac{\partial^2 f(\mathbf{x})}{\partial x_2 \partial x_1}&  \frac{\partial^2 f(\mathbf{x})}{\partial x_2^{2}}&  \dots& \frac{\partial^2 f(\mathbf{x})}{\partial x_2 \partial x_n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial^2 f(\mathbf{x})}{\partial x_n \partial x_1}&  \frac{\partial^2 f(\mathbf{x})}{\partial x_n \partial x_2}&  \dots& \frac{\partial^2 f(\mathbf{x})}{\partial x_n^{2}}
\end{bmatrix} \in \mathbb{S}^n
$$

Ma trận $\mathbb{S}^n \in \mathbb{R}^{n \times n} $là ma trận đối xứng có số cột bằng n. Công thức đạo hàm bậc hai phía trên dễ dàng chứng minh được khi khi lấy đạo hàm bậc một được một vector, sau đó lấy tiếp đạo hàm của vector đó ta được *Hessian*.

**Ví dụ.** $f(\mathbf{x}): \mathbb{R}^2 \rightarrow \mathbb{R}$, $f(\mathbf{x}) = x_1^{3} + x_1 x_2 + x_2^{2}$

$$
\nabla_\mathbf{x}^2 f(\mathbf{x}) = 
\begin{bmatrix}
\frac{\partial^2 f(\mathbf{x})}{\partial x_1^{2}}& \frac{\partial^2 f(\mathbf{x})}{\partial x_1 \partial x_2}\\
\frac{\partial^2 f(\mathbf{x})}{\partial x_2 \partial x_1}& \frac{\partial^2 f(\mathbf{x})}{\partial x_2^{2}}
\end{bmatrix} = 
\begin{bmatrix}
6x_1& 1\\
1& 2
\end{bmatrix}
$$

**Đạo hàm của scalar theo matrix**

$ f(\mathbf{X}): \mathbb{R}^{n \times m} \rightarrow \mathbb{R} $

$$
\nabla_\mathbf{X} f(\mathbf{X}) = 
\begin{bmatrix}
\frac{\partial f(\mathbf{X})}{\partial x_{11}}&  \frac{\partial f(\mathbf{X})}{\partial x_{12}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{1m}}\\ 
\frac{\partial f(\mathbf{X})}{\partial x_{21}}&  \frac{\partial f(\mathbf{X})}{\partial x_{22}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{2m}}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f(\mathbf{X})}{\partial x_{n1}}&  \frac{\partial f(\mathbf{X})}{\partial x_{n2}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{nm}}
\end{bmatrix}
$$

Nhận thấy đạo hàm của hàm số (scalar) theo ma trận là ma trận có chiều giống với ma trận ban đầu. Từng thành phần của ma trận kết quả là đạo hàm của $f(\mathbf{X})$ đối với thành phần tương ứng với ma trận input.

**Ví dụ.** Hàm số $ f(\mathbf{X}): \mathbb{R}^{2 \times 2} \rightarrow \mathbb{R} $, $f(\mathbf{X}) = x_{11} + x_{12} + x_{21} + x_{22}$

$$ 
\mathbf{X} = 
\begin{bmatrix}
x_{11}& x_{12}\\
x_{21}& x_{22}
\end{bmatrix} ~~~~~~~~~~~~
\nabla_\mathbf{X} f(\mathbf{X}) = 
\begin{bmatrix}
1& 1\\
1& 1
\end{bmatrix}
$$

## Đạo hàm của hàm cho giá trị là vector

**Đạo hàm của vector theo scalar**

$\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^m$


$$
\nabla_{x} \mathbf{f}(x) =
\left [ \frac{\partial f_1}{\partial x} ~~\frac{\partial f_2}{\partial x} \dots \frac{\partial f_m}{\partial x} \right ] ~~~~~ (2)
$$

Đạo hàm của vector theo scalar là một **vector hàng**.

**Ví dụ.** $\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^2$, $\mathbf{f}(x) = \begin{bmatrix} x^2 \\ x^3 + x\end{bmatrix}$
$$
\nabla_{x} \mathbf{f}(x) =
\frac{\partial \mathbf{f}}{\partial x} = 
\left [ \frac{\partial f_1}{\partial x} ~~\frac{\partial f_2}{\partial x} \right ] = 
\left [ \frac{\partial x^2}{\partial x} ~~\frac{\partial x^3 + x}{\partial x} \right ] = 
\left [ 2x ~~ 3x^2 + 1 \right ]
$$

Đạo hàm bậc hai của hàm số $\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^m$ cũng là một vector hàng có chiều $m$. 

$$
\nabla_{x} \mathbf{f}(x) =
\left [ \frac{\partial^2 f_1}{\partial x^2} ~~\frac{\partial^2 f_2}{\partial x^2} \dots \frac{\partial^2 f_m}{\partial x^2} \right ] ~~~~~ (2)
$$

**Đạo hàm của vector theo vector**

$\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$

$$ 
\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \nabla_{\mathbf{x}} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_1}\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_2}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_n}&  \frac{\partial f_2(\mathbf{x})}{\partial x_n}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} \in \mathbb{R}^{n \times m} ~~~~~ (3) 
$$

Chúng ta có thể suy ra công thức này từ các công thức trên như sau. Từ công thức (1) gradient của $\mathbf{f}$ theo vector $\mathbf{x}$ là một vector cột.

$$
\frac{\partial \mathbf{f}}{\partial \mathbf{x}} = 
\begin{bmatrix}
\frac{\partial \mathbf{f}}{\partial x_1}\\ 
\frac{\partial \mathbf{f}}{\partial x_2}\\ 
\vdots\\ 
\frac{\partial \mathbf{f}}{\partial x_n}
\end{bmatrix} ~~~~~ (4)
$$

Đạo hàm của một vector theo một số vô hướng là vector hàng như sau.

$$ \frac{\partial \mathbf{f}}{\partial x_i} = 
\left [ \frac{\partial f_1}{\partial x_i} ~~\frac{\partial f_2}{\partial x_i} \dots \frac{\partial f_m}{\partial x_i} \right ]
$$

Thay công thức trên vào công thức (4) chúng ta sẽ nhận được (3). Không phức tạp quá phải không nào?

Ở đây chúng ta cũng có khái niệm **Jacobian** của $\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$ là ma trận các đạo hàm riêng bậc  một có kích thước $n \times m$.

$$
\mathbf{J} = \nabla_\mathbf{x} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_1}\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_2}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_n}&  \frac{\partial f_2(\mathbf{x})}{\partial x_n}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} =
\left [ \nabla_{\mathbf{x}} f_1(\mathbf{x})  ~~\nabla_{\mathbf{x}} f_2(\mathbf{x})  \dots \nabla_{\mathbf{x}} f_m(\mathbf{x}) \right ] ~~~(5) ~~~~~~~~~ J_{ij} = \frac{\partial f_j}{\partial x_i} 
$$

Trường hợp đặc biệt $m=1$ chúng ta có Jacobian của $f(\mathbf{x})$ là một vector cột (ma trận với kích thước $n \times 1$) như công thức (1).

Ở đây chúng ta không đưa vào các khái niệm đạo hàm của vector theo matrix, đạo hàm của matrix theo vector và đạo hàm của matrix theo matrix vì lúc này chúng ta cần số chiều lớn hơn 2 (tensor). 

## Chain rule

**Product rule**

$\mathbf{X}$ là ma trận. Tuy nhiên những công thức bên dưới có thể áp dụng cho vector và số thực đều được.

$$ \nabla\left( f(\mathbf{X})^Tg(\mathbf{X}) \right) = \left(\nabla f(\mathbf{X})\right) g(\mathbf{X}) + \left(\nabla g(\mathbf{X})\right) f(\mathbf{X}) ~~~ (6) $$

Công thức này tương tự như công thức $\left(f(x)g(x)\right)’ = f’(x)g(x) + g’(x)f(x)$.

**Chain rule**

$$ \nabla_{\mathbf{X}} g(f(\mathbf{X})) = \nabla_{\mathbf{X}} f^T \nabla_{f}g ~~~ (7) $$

Công thức này tương tự với $(g(f(x))’ = f’(x)g’(f)$. Do tất cả các công thức trong bài này theo quy ước *denominator layout* nên trông hơi ngược so với các tính chất của hàm thông thường. Nếu sử dụng *numerator layout* thì mọi thứ trông tự nhiên hơn. 

## Một số ví dụ

**Ví dụ 1**

Cho hàm số  $\mathbf{f}(\mathbf{x}) = \mathbf{a}^T\mathbf{x}$. Khi đó dễ dàng nhận thấy $\nabla_\mathbf{x} (\mathbf{a}^T\mathbf{x}) = \mathbf{a} $, tương tự cũng có $\nabla_\mathbf{x} (\mathbf{x}^T\mathbf{a}) = \mathbf{a} $

**Ví dụ 2**

Cho hàm số $\mathbf{f}(\mathbf{x}) = \mathbf{A}\mathbf{x}$, trong đó $\mathbf{f}(\mathbf{x}) \in \mathbb{R}^m$, $\mathbf{A} \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$. Xác định gradient $\nabla_\mathbf{x} \mathbf{f} = d\mathbf{f} / d\mathbf{x}$

>Chú ý: ở đây khi ghi $\mathbb{R}^n$ chúng ta hiểu mặc định đó là vector có $n$ chiều, vector cột hay matrix có kích thước $\mathbb{R}^{n \times 1}$.

Bởi vì $\mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$ nên theo công thức (3), $\nabla_\mathbf{x} \mathbf{f}$ sẽ có kích thước là $\mathbb{R}^{n \times m}$.

Theo đề bài chúng ta sẽ có $f_i(\mathbf{x}) = \sum_{j=1}^{n}A_{ij}x_j \Rightarrow \frac{\partial f_i}{\partial x_j} = A_{ij}$

$$
\nabla_\mathbf{x} \mathbf{f} = 
\begin{bmatrix}
\frac{\partial f_1(\mathbf{x})}{\partial x_1}&  \frac{\partial f_2(\mathbf{x})}{\partial x_1}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_1}\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_2}&  \frac{\partial f_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_2}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f_1(\mathbf{x})}{\partial x_n}&  \frac{\partial f_2(\mathbf{x})}{\partial x_n}&  \dots& \frac{\partial f_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} =
\begin{bmatrix}
A_{11}&  A_{21}&  \dots& A_{m1}\\ 
A_{12}&  A_{22}&  \dots& A_{m2}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
A_{1n}&  A_{2n}&  \dots& A_{mn}\\ 
\end{bmatrix} = \mathbf{A}^T \in \mathbb{R}^{n \times m}
$$

$$ \nabla_\mathbf{x} \mathbf{Ax} = \mathbf{A}^T $$

 $\mathbf{a_i}$ là vector hàng thứ $i$ của ma trận $\mathbf{A}$ ta có thể ghi gọn hơn như sau: 

$$\mathbf{Ax} = 
\begin{bmatrix}
\mathbf{a_1}\mathbf{x}\\
\mathbf{a_2}\mathbf{x}\\
\vdots\\
\mathbf{a_m}\mathbf{x}
\end{bmatrix}
$$

Từ công thức (5) chúng ta có 

$$
\nabla_\mathbf{x} \mathbf{Ax} = 
\left [ \nabla_{\mathbf{x}} \mathbf{a_1}\mathbf{x}  ~~\nabla_{\mathbf{x}} \mathbf{a_2}\mathbf{x}  \dots \nabla_{\mathbf{x}} \mathbf{a_m}\mathbf{x} \right ] =
\begin{bmatrix}
\mathbf{a_1}^T& \mathbf{a_2}^T& \dots & \mathbf{a_m}^T\\
\end{bmatrix} = \mathbf{A}^T
$$

**Ví dụ 2**

$\mathbf{X} \in \mathbb{R}^{m \times n}$, $\mathbf{w} \in \mathbb{R}^{n}$,  $\mathbf{y} \in \mathbb{R}^{m}$. Loss function:

$$ L = ||\mathbf{X}\mathbf{w} - \mathbf{y}||^2$$

đi tính $\frac{\partial L}{\partial \mathbf{w}}$.

$$ L = ||\mathbf{X}\mathbf{w} - \mathbf{y}||^2 = (\mathbf{X}\mathbf{w} - \mathbf{y})^T (\mathbf{X}\mathbf{w} - \mathbf{y})$$

Đặt $f = \mathbf{X}\mathbf{w} - \mathbf{y}$, $g = \mathbf{X}\mathbf{w} - \mathbf{y}$. Theo công thức (6) chúng ta có.

$$ 
\frac{\partial L}{\partial \mathbf{w}} = \nabla f(\mathbf{w}) g(\mathbf{w}) + \nabla g(\mathbf{w}) f(\mathbf{w}) = 
\mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y}) + \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y}) = 2 \mathbf{X}^T (\mathbf{X}\mathbf{w} - \mathbf{y})  
$$

Đây chính là gradient của loss function cho Linear Regression model.

**Ví dụ 3:**

Cho hàm số $f(\mathbf{x}) = \mathbf{a}^T\mathbf{x}\mathbf{x}^T\mathbf{b}$

$$f(\mathbf{x}) = (\mathbf{x}^T \mathbf{a})^T (\mathbf{x}^T \mathbf{b}) $$

Đặt $f = \mathbf{x}^T \mathbf{a}$, $g = \mathbf{x}^T \mathbf{b}$. Theo công thức (6) chúng ta có.


$$ 
\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}} = \nabla f(\mathbf{x}) g(\mathbf{x}) + \nabla g(\mathbf{x}) f(\mathbf{w}) = \mathbf{a} \mathbf{x}^T \mathbf{b} + \mathbf{b} \mathbf{x}^T \mathbf{a} 
$$

do $\mathbf{p}^T \mathbf{q} = \mathbf{q}^T \mathbf{p}$ (tích vô hướng) nên phương trình trên viết lại thành:

$$
\frac{\partial f(\mathbf{x})}{\partial \mathbf{x}} =
\mathbf{a} \mathbf{b}^T \mathbf{x} + \mathbf{b} \mathbf{a}^T \mathbf{x} = (\mathbf{a} \mathbf{b}^T + \mathbf{b} \mathbf{a}^T)\mathbf{x} 
$$

## Tài liệu tham khảo
1. https://en.wikipedia.org/wiki/Matrix_calculus#Numerator-layout_notation 
2. https://machinelearningcoban.com/math/
3. https://ccrma.stanford.edu/~dattorro/matrixcalc.pdf