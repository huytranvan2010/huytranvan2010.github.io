---
layout: post
title: "Matrix calculus - Numerator layout"
tags: [Giải Tích, Đạo Hàm]
comments: true
---

Trong bài trước chúng ta đã tìm hiểu về matrix calculus với denominator layout. Các bạn có thể xem lại [tại đây](https://huytranvan2010.github.io/Maxtrix-calculus/). Thực tế rằng việc lấy đạo hàm của hàm phức hợp theo cách biểu diễn này thường khá phức tạp, không tự nhiên vì khi biến đổi cần phải lấy transpose. Trong mạng NN đi từ layer này qua layer khác phải trải qua nhiều bước, tạm gọi là nhiều "hàm" và việc lấy đạo hàm theo cách này mình cảm thấy khá phức tạp và không tường minh. Do đó trong bài này chúng ta sẽ quay trở lại với **numerator layout**. Mình có tìm hiểu một số tài liệu thì thấy đạo hàm theo vector hay matrix thường được diễn giải theo cách này, rất tường minh và tự nhiên khi có hàm phức hợp. 

Chia sẻ một chút, mình mất một thời gian để tìm hiểu về matrix calculus. Thực tế có hai quy ước về lấy đạo hàm là **numerator layout (Jacobian formulation)** và **denominator layout (Hessian formulation)**, nhiều tài liệu không ghi rõ và khi đọc nhiều tài liệu sẽ gây nhầm lẫn. 

Trong bài này chúng ta sẽ dùng theo quy ước **numerator layout** và tìm hiểu về backpropagation trong mạng NN.

Chúng ta có vector $\mathbf{x}$ có kích thước $n \times 1$:

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

Ví dụ hàm số $f(x): \mathbb{R} \rightarrow \mathbb{R}$, $f(x) = 3x^2 + 2$

$$\frac{\partial (3x^2 +2)}{\partial x} = 6x$$

**Đạo hàm của scalar theo vector**

$f(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}$

$$\nabla_\mathbf{x} f(\mathbf{x}) = \frac{\partial f}{\partial \mathbf{x}} = \left [ \frac{\partial f}{\partial x_1} ~~\frac{\partial f}{\partial x_2} \dots \frac{\partial f}{\partial x_n} \right ] ~~~~~ (1) $$

Nhớ nhé ở đây chúng ta nhận được **vector hàng**.

Ví dụ hàm số $f(\mathbf{x}): \mathbb{R}^2 \rightarrow \mathbb{R}$, $f(\mathbf{x}) = x_1^{2} + x_2^{2}$

$$\frac{\partial f}{\partial \mathbf{x}}(x_1^2 + 2x_2^2) = \left [ \frac{\partial f}{\partial x_1} ~~ \frac{\partial f}{\partial x_2} \right ] = \left [ 2x_1 ~~ 4x_2 \right ]$$

**Đạo hàm của scalar theo matrix**

$ f(\mathbf{X}): \mathbb{R}^{n \times m} \rightarrow \mathbb{R} $

$$
\nabla_\mathbf{X} f(\mathbf{X}) = 
\begin{bmatrix}
\frac{\partial f(\mathbf{X})}{\partial x_{11}}&  \frac{\partial f(\mathbf{X})}{\partial x_{21}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{n1}}\\ 
\frac{\partial f(\mathbf{X})}{\partial x_{12}}&  \frac{\partial f(\mathbf{X})}{\partial x_{22}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{n2}}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial f(\mathbf{X})}{\partial x_{1m}}&  \frac{\partial f(\mathbf{X})}{\partial x_{2m}}&  \dots& \frac{\partial f(\mathbf{X})}{\partial x_{nm}}
\end{bmatrix} \in \mathbb{R}^{m \times n}
$$

## Đạo hàm của hàm cho giá trị là số vô hướng

**Đạo hàm của vector theo scalar**

$\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^m$

$$ 
\nabla_x \mathbf{f}(x) = 
\frac{\partial \mathbf{f}}{\partial x} = 
\begin{bmatrix}
\frac{\partial f_1}{\partial x}\\ 
\frac{\partial f_2}{\partial x}\\ 
\vdots\\ 
\frac{\partial f_m}{\partial x}
\end{bmatrix} ~~~~~ (2) 
$$

Ví dụ $\mathbf{f}(x): \mathbb{R} \rightarrow \mathbb{R}^m$, $\mathbf{f}(x) = \begin{bmatrix}
x^2\\  
x^3 + x
\end{bmatrix} $

$$ \frac{\partial \mathbf{f}}{\partial x} = 
\begin{bmatrix}
\frac{\partial x^2}{\partial x}\\  
\frac{\partial x^3 + x}{\partial x}
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
\end{bmatrix} =
\begin{bmatrix}
\nabla_{\mathbf{x}}f_1(\mathbf{x})\\
\nabla_{\mathbf{x}}f_2(\mathbf{x})\\
\vdots\\
\nabla_{\mathbf{x}}f_m(\mathbf{x})
\end{bmatrix}~~~~~~ J_{ij} = \frac{\partial f_i}{\partial x_j}
$$

Trường hợp đặc biệt $m=1$ chúng ta có Jacobian của $f(\mathbf{x})$ là một vector hàng (ma trận với kích thước $1 \times n$) như công thức (1).

Ví dụ:


## Một số ví dụ

**Ví dụ 1**

Cho hàm số  $\mathbf{f}(\mathbf{x}) = \mathbf{a}^T\mathbf{x}$. Khi đó dễ dàng nhận thấy $\nabla_\mathbf{x} (\mathbf{a}^T\mathbf{x}) = \mathbf{a}^T $, tương tự cũng có $\nabla_\mathbf{x} (\mathbf{x}^T\mathbf{a}) = \mathbf{a}^T $

**Ví dụ s**

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

**Chain rule** trong numerator layout thật tự nhiên phải không nào. Công thức này nhìn hơi khác một chút do với công thức chúng ta thường thấy trong các khóa học ML. Lý do bởi vì trong các khóa ML sử dụng denominator layout. Như định nghĩa bên trên chúng ta có $\frac{\partial L}{\partial \mathbf{w}}$ là một vector hàng giống với những gì nhận được bên vế phải. Tuy nhiên trong NN hay để dạng vector cột nên kết quả cuối cùng được chuyển về vector cột. Có thể viết lại thành:

$$ 
\frac{\partial L}{\partial \mathbf{w}} = 
2\mathbf{X}^T(\mathbf{X}\mathbf{w} - \mathbf{y})
$$

## Mở rộng

**Trường hợp vô hướng**

Cho hàm số $f(x): \mathbb{R} \rightarrow \mathbb{R}$. Đạo àm (derivative) của $f$ tại $x \in \mathbb{R}$ được xác định như sau:

$$ f'(x) = \lim_{h \to 0} = \frac{f(x+h) - f(x)} {h}$$

Đạo hàm của $f$ tại $x$ sẽ cho chúng ta biết độ thay đổi của hà $f$ khi $x$ thay đổi một lượng nhỏ $\varepsilon$:

$$f(x+\varepsilon) \approx f(x) + \varepsilon f'(x)$$

Để đơn giản đặt $y = f(x)$ và viết $\frac{\partial y}{\partial x}$ cho đạo hàm của $y$ theo $x$. Kí hiệu $\frac{\partial y}{\partial x}$ cũng đã nhấn mạnh tốc độ thay đổi của $y$ theo $x$. Nếu $x$ thay đổi một lượng $\varepsilon = \Delta x$ thì $y$ sẽ thay đổi một lượng $\varepsilon \frac{\partial y}{\partial x}$. CHúng ta có thể ghi lại như sau:

$$
x \rightarrow x + \Delta x \Rightarrow y \rightarrow \approx y + \frac{\partial y}{\partial x} \Delta x
$$

Chain rule cho phép chúng ta tính đạo hàm của hàm phức hợp (kết hợp nhiều hàm với nhau). Ví dụ $f, g: \mathbb{R} \rightarrow \mathbb{R}$ và $y=f(x)$, $z = g(y)$. Chúng ta có thể ghi lại $z = (g \circ f)(x)$ và vẽ computational graph như sau:

$$ x \overset{f}{\rightarrow} y \overset{g}{\rightarrow} z$$

Theo chain rule (scalar) ta có:

$$ \frac{\partial z}{\partial x} = \frac{\partial z}{\partial y}  \frac{\partial y}{\partial x} $$

Phân tích một chút

$$
x \rightarrow x + \Delta x \Rightarrow y \rightarrow \approx y + \frac{\partial y}{\partial x} \Delta x
$$

$$
y \rightarrow y + \Delta y \Rightarrow z \rightarrow \approx z + \frac{\partial z}{\partial y} \Delta y
$$

Kết hợp 2 điều này chúng ta có thể tính được ảnh hưởng của $x$ lên $z$. Nếu $x$ thay đổi $\Delta x$ thì $y$ sẽ thay đổi $\frac{\partial y}{\partial x} \Delta x$ và chúng ta có $\Delta y = \frac{\partial y}{\partial x} \Delta x$. Nếu $y$ thay đổi thì $z$ sẽ thay đổi một lượng $\frac{\partial z}{\partial y} \Delta y = \frac{\partial z}{\partial y} \frac{\partial y}{\partial x} \Delta x $$

**Gradient: vector in, scalar out**

Đầu vào là một vector, đầu ra là một số vô hướng.

Cho hàm số $f(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}$. Đạo hàm của $f$ tạo điểm $\mathbf{x} \in \mathbb{R}^n$ được gọi là **gradient** và được xác định như sau:

$$
\nabla_\mathbf{x} f(\mathbf{x}) = \lim_{\mathbf{h} \to 0}\frac{f(\mathbf{x} + \mathbf{h}) - f(\mathbf{x})}{\mathbf{||h||}}
$$

Gradient $\nabla_\mathbf{x} f(\mathbf{x}) \in \mathbb{R}^n$ cũng là một vector. Đặt $y = f(\mathbf{x})$ chúng ta sẽ có:

$$
\mathbf{x} \rightarrow \mathbf{x} + \Delta \mathbf{x} \Rightarrow y \rightarrow \approx y + \frac{\partial y}{\partial \mathbf{x}} \Delta \mathbf{x}
$$

Ở đây $\frac{\partial y}{\partial \mathbf{x}} \in \mathbb{R}^n $ là một vector hàng. $\frac{\partial y}{\partial \mathbf{x}} \Delta \mathbf{x}$ ở đây là **dot product** để nhận được số vô hướng.

Nếu tưởng tượng $\Delta \mathbf{x}$ là $i^{th}$ basis vector, điều này tương đương với tọa độ $i^{th}$ của $\varepsilon = \Delta \mathbf{x}$ là 1, các tọa còn lại bằng 0. Dot product $\frac{\partial y}{\partial \mathbf{x}} \Delta \mathbf{x}$ đơn giản là tọa độ $i^{th}$ của $\frac{\partial y}{\partial \mathbf{x}}$. Do đó tọa độ $i^{th}$ của$\frac{\partial y}{\partial \mathbf{x}}$ sẽ cho chúng ta biết lượng $y$ thay đổi nếu chúng ta dịch chuyển $\mathbf{x}$ theo  trục tọa độ $i^{th}$.

$$
\frac{\partial y}{\partial \mathbf{x}} = 
\left [ \frac{\partial y}{\partial x_1} ~~\frac{\partial y}{\partial x_2} \dots \frac{\partial y}{\partial x_n} \right ] $$

**Jacobian: vector in, vector out**

Đầu vào là vector, đầu ra cũng là vector.


$\mathbf{y} = \mathbf{f}(\mathbf{x}): \mathbb{R}^n \rightarrow \mathbb{R}^m$

$$ 
\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \nabla_{\mathbf{x}} \mathbf{y} = 
\begin{bmatrix}
\frac{\partial y_1(\mathbf{x})}{\partial x_1}&  \frac{\partial y_1(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial y_1(\mathbf{x})}{\partial x_n}\\ 
\frac{\partial y_2(\mathbf{x})}{\partial x_1}&  \frac{\partial y_2(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial y_2(\mathbf{x})}{\partial x_n}\\ 
 \vdots&  \vdots&  \vdots& \vdots\\ 
\frac{\partial y_m(\mathbf{x})}{\partial x_1}&  \frac{\partial y_m(\mathbf{x})}{\partial x_2}&  \dots& \frac{\partial y_m(\mathbf{x})}{\partial x_n}
\end{bmatrix} = J \in \mathbb{R}^{m \times n} 
$$

Jacobian cho chúng ta biết mối quan hệ giữa mỗi phần tử của $\mathbf{x}$ và mỗi phần tử của $\mathbf{y}$. 

$$\frac{\partial y_i}{\partial x_j} = J_{ij} $$

Jacobian cũng cho ta biết mối quan hệ giữa sự thay đổi của input và sự thay đổi của output:

$$
\mathbf{x} \rightarrow \mathbf{x} + \Delta \mathbf{x} \Rightarrow \mathbf{y} \rightarrow \approx \mathbf{y} + \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \Delta \mathbf{x}
$$

Ma trận $\frac{\partial \mathbf{y}}{\partial \mathbf{x}}$ là ma trận $m \times n$, $\Delta \mathbf{x}$ là vector có $n$ phân tử, do đó *dot product* $\frac{\partial \mathbf{y}}{\partial \mathbf{x}} \Delta \mathbf{x}$ là tích ma trận với vector ta nhận được vector có $m$ phần tử. 

Chain rule có thể mở rộng cho trường hợp vector bằng cách sử dụng Jacobian. Giả sử $\mathbf{f}: \mathbb{R}^n \rightarrow \mathbb{R}^m$ và $\mathbf{g}: \mathbb{R}^m \rightarrow \mathbb{R}^k$. $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{y} \in \mathbb{R}^m$ và $\mathbf{z} \in \mathbb{R}^k$ với $\mathbf{y} = \mathbf{f}(\mathbf{x})$ và $\mathbf{z} = \mathbf{g}(\mathbf{y}$. Chúng ta cũng có computational graph như sau:

$$ \mathbf{x} \overset{\mathbf{f}}{\rightarrow} \mathbf{y} \overset{\mathbf{g}}{\rightarrow} \mathbf{z}$$

Chain rule cũng có dạng giống với scalar case:

$$ \frac{\partial \mathbf{z}}{\partial  \mathbf{x}} = \frac{\partial  \mathbf{z}}{\partial  \mathbf{y}}  \frac{\partial  \mathbf{y}}{\partial  \mathbf{x}} $$

Mỗi thành phần bây giờ là ma trận. $\frac{\partial  \mathbf{z}}{\partial  \mathbf{y}}$ có kích thước $k \times m$, $\frac{\partial  \mathbf{y}}{\partial  \mathbf{x}}$ có kích thước $m \times n$, $\frac{\partial  \mathbf{z}}{\partial  \mathbf{x}}$ có kích thước $k \times n$. Vế phải là matrix multiplication.

**Generalized Jacobian: tensor in, tensor out**

Nhiều phép toán trong DL nhận vào tensor và trả về tensor. Ví dụ ảnh thường được biểu diễn dưới dạng tensor 3 chiều, do đó chúng ta sẽ đi phét triển đạo hàm để tương thích với các phép tính trên tensor.

Giả sử có hàm $f: \mathbb{R}^{n_1 \times \dots \times n_{d_x}} \rightarrow \mathbb{R}^{m_1 \times \dots \times m_{d_y}}$. Input của hàm $f$ là $d_x$ - dimensional tensor có shape $n_1 \times \dots \times n_{d_x}$, output là $d_y$ - dimensional tensor có shape $m_1 \times \dots \times m_{d_y}$. Đặt $y=f(x)$, khi đó $\frac{\partial y}{\partial x}$ là **generalized Jacobian** và nó có shape là:

$$ (m_1 \times \dots \times m_{d_y}) \times (n_1 \times \dots \times n_{d_x})$$

>Chú ý: Ở đây do tensor nhiều chiều nên kí hiệu chúng là $y=f(x)$ không có in đậm ở đây. Tuy nhiên khi lấy đạo hàm cần phải để ý đến bản chất của hàm và của biến được lấy đạo hàm là vector, matrix, tensor hay scalar để thực hiện chính xác.

Chúng ta tách chiều của $\frac{\partial y}{\partial x}$ thành 2 nhóm:
- nhóm 1 khớp với chiếu của $y$
- nhóm 2 khớp với chiếu của $x$

Với việc nhóm chiều như này chúng ta có thể nghĩ *generalized Jacobian* là ma trân với "row" có shape giống với $y$ và "column" có shape giống $x$.

Giả sử $i \in \mathbb{Z}^{d_y}$ và $j \in \mathbb{Z}^{d_x}$ là các vector chỉ số, khi đó có thể ghi:

$$\left ( \frac{\partial y}{\partial x}  \right )_{i,j} =  \frac{\partial y_i}{\partial x_j} $$

Ở đây $y_i$ và $x_j$ là các số vô hướng ($y_i$ giống như lấy giá trị cảu $y$ theo ở vị trí i - vector các chỉ số). Do đó $\frac{\partial y_i}{\partial x_j}$ là số vô hướng. Giống như Jacobian tiêu chuẩn, generalized Jacobian cho chúng ta biết tốc độ thay đổi giữa tất cả thành phần của $x$ và các thành phần của $y$.

$$
x \rightarrow x + \Delta x \Rightarrow y \rightarrow \approx y + \frac{\partial y}{\partial x} \Delta x
$$

$\Delta x$ bây giờ là tensor với shape $n_1 \times \dots \times n_{d_x}$ và $\frac{\partial y}{\partial x}$ là generalized matrix với shape $ (m_1 \times \dots \times m_{d_y}) \times (n_1 \times \dots \times n_{d_x})$. Product $\frac{\partial y}{\partial x} \Delta x$ là *generalized matrix-vector multiply*, cái này sẽ dẫn đến tensor có shape $(m_1 \times \dots \times m_{d_y})$.

Generalized matrix-vector multiply tuân thủ theo các quy luật giống với phép nhân ma trận - vector truyền thống.

$$\left ( \frac{\partial y}{\partial x} \Delta x \right )_{j} = \sum_j \left ( \frac{\partial y}{\partial x} \right )_{ji} (\Delta x)_i = \left ( \frac{\partial y}{\partial x} \right )_{j,:} \Delta x$$

Chú ý ở đây $i$ và $j$ không phải số vô hướng mà là vectors các chỉ số. Trong công thức trên $\left ( \frac{\partial y}{\partial x} \right )_{j,:}$ là $j^{th}$ "row" của generalized matrix $\left ( \frac{\partial y}{\partial x} \right )$ - đây là tensor có shape giống với $x$. Ở đây cũng sử dụng quy ước dot product của hai tensors có cùng shape là *element-wise product* theo sau là lấy tổng (tương tự dot product giữa hai vectors).

Chain rule cho trường hợp tensor-valued function cũng tương tự như vậy. Giả sử $y=f(x)$ và $z=g(y)$, $x$ và $y$ có chiều giống như trên và $z$ có shape là $k_1 \times \dots \times k_{d_z}$.

$$ \frac{\partial z}{\partial x} = \frac{\partial z}{\partial y}  \frac{\partial y}{\partial x} $$

Sự khác biệt ở đây: $\frac{\partial z}{\partial y}$ là generalized matrix có shape là $ (k_1 \times \dots \times k_{d_z}) \times (m_1 \times \dots \times m_{d_y})$, $\frac{\partial y}{\partial x}$ là generalized matrix có shape là $ (m_1 \times \dots \times m_{d_y}) \times (n_1 \times \dots \times n_{d_x})$. Product $\frac{\partial z}{\partial y}  \frac{\partial y}{\partial x}$ là generalized matrix-matrix multiply, tạo ra object có shape là $ (k_1 \times \dots \times k_{d_z}) \times (n_1 \times \dots \times n_{d_x})$. Giống như generalized matrix-vector multiply như trên, generalized matrix-matrix multiply tuân theo các quy luật đại số giống phép trên matrix-matrix truyền thống.

$$\left ( \frac{\partial z}{\partial x}  \right )_{i,j} = \sum_k \left ( \frac{\partial z}{\partial y}  \right )_{i,k} \left ( \frac{\partial y}{\partial x}  \right )_{k,j} = \left ( \frac{\partial z}{\partial y}  \right )_{i,:} \left ( \frac{\partial y}{\partial x}  \right )_{:,j}$$

trong đó $i, j, k$ là các vectors chỉ số, $\left ( \frac{\partial z}{\partial y}  \right )_{i,:}$ là $i^{th}$ "row" của $\left ( \frac{\partial z}{\partial y}  \right )$ , $\left ( \frac{\partial z}{\partial y}  \right )_{:,j}$ là $j^{th}$ "column" của $\left ( \frac{\partial y}{\partial x}  \right )$.

**Backpropagation with tensors**

Khi nói về NN, layer $f$ thường là hàm của inputs $x$ (tensor) và weights $w$, tensor output của layer $y = f(x, w)$. Layer $f$ thường được đưa vào mạng NN lớn với scalar loss $L$.

Trong backpropagation, giả sử chúng ta đã có $\frac{\partial L}{\partial y}$, mục tiêu của chúng ta là tính $\frac{\partial L}{\partial y}$ và $\frac{\partial L}{\partial w}$. Theo chain rule chúng ta có:

$$
\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial x}  ~~~~~~~~ \frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial w}
$$

Chúng ta sẽ đi tìm generalized Jacobian $\frac{\partial y}{\partial x}$, $\frac{\partial y}{\partial w}$ và sử dụng generalized matrix multiplication để tính $\frac{\partial L}{\partial x}$, $\frac{\partial L}{\partial w}$. Tuy nhiên ở đây có một vấn đề là Jacobian matrices $\frac{\partial y}{\partial x}$ và $\frac{\partial y}{\partial w}$ thường quá lớn để phù hợp với bộ nhớ.

Lấy ví dụ giả sử rằng $f$ là linear layer nhận vào input là minibatch với $n$ vectors, mỗi vector có dimension $d$ và tạo ra output là minibatch $n$ vectors, mỗi vector có dimension $m$. $x$ là ma trận có kích thước $n \times d$, $w$ là weights có kích thước $d \times m$ và hàm số $y = f(x, w) = xw$ là ma trận có kích thước $n \times m$. Cách biểu diễn này giống với một số thư viện làm như Tensorflow. Một số tài liệu có cách biểu diễn khác.

>Chú ý: Dễ nhận thấy trong cách biểu diễn này example được coi như một hàng (số cột tương ứng với các features). Cách biểu diễn này ngược với cách biểu diễn trong khóa học DL của Andrew Ng. Không quan trọng cách nào miễn là chúng ta có thể giả quyết vấn đề một cách nhanh gọn. 

Khi đó Jacobian $\frac{\partial y}{\partial x}$ có shape là $(n \times m) \times (n \times d)$. Ví dụ trong mạng NN ta có $n=64$, $m=d=4096$ lúc này $\frac{\partial y}{\partial x}$ chứa $64 \cdot 4096 \cdot 64 \cdot 4096 $ giá trị vô hướng, khoảng hơn 68 tỉ số. Nếu sử dụng 32-bit floating point, Jacobian này chiếm khoảng 256 GB memory. Việc lưu trữ và thao tác trên Jacobian này gần như là không thể.

Tuy nhiên trong các mạng NN thông thường chúng ta có thể dẫn ra công thức có thể tính $\frac{\partial L}{\partial y} \frac{\partial y}{\partial x}$ mà không cần tạo Jacobian matrix $\frac{\partial y}{\partial x}$. Trong nhiều trường hợp chúng ta sẽ làm với trường hợp đơn giản sau đó có thể tổng quát hóa lên được.

Ví dụ linear layer $y = f(x,w) = xw$. Đặt $n=1$, $d=2$, $m=3$. Khi đó

$$
\begin{align*}
y &= \left [y_{1,1} ~~ y_{1,2} ~~ y_{1,3}  \right ]= xw \\ 
 &= [x_{1,1} ~~ x_{1,2}] \begin{bmatrix} w_{1,1}& w_{1,2}& w_{1,3}\\ w_{2,1}& w_{2,2}& w_{2,3}\end{bmatrix} \\
 &= \left [ x_{1,1}w_{1,1}+x_{1,2}w_{2,1} ~~~~ x_{1,1}w_{1,2}+x_{1,2}w_{2,2} ~~~~ x_{1,1}w_{1,3}+x_{1,2}w_{2,3}\right ]
\end{align*}
$$

Như đã nói ở trên ở đây có 1 example và $y$ được biểu diễn theo hàng.

Trong backpropagation giả sử chúng ta đã có $\frac{\partial L}{\partial y}$ có shape là $(1) \times (n \times m)$. Để thuận tiện cho việc ghi chú chúng ta có thể nghĩ nó là ma trận có shape là $n \times m$. Chúng ta có thể ghi thành:

$$
\frac{\partial L}{\partial y} =
\left [ dy_{1,1} ~~~ dy_{1,2} ~~~ dy_{1,3} \right ]
$$

Chúng ta biết rằng $\frac{\partial L}{\partial x}$ có shape là $(1) \times (n \times d)$, để biểu dễn gradient hay để $\frac{\partial L}{\partial x}$ như ma trận có shape $n \times d$. 

$$
\frac{\partial L}{\partial x} =
\left [ dx_{1,1} ~~~ dx_{1,2}  \right ]
$$

$$
\frac{\partial L}{\partial x} =
\begin{bmatrix}
dx_{1,1}\\
dx_{1,2}
\end{bmatrix}
$$

Xác định cho từng phần tử chúng ta có:
$$
\frac{\partial L}{\partial x_{1,1}} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial x_{1,1}}  ~~~~~~~~ \frac{\partial L}{\partial x_{1,2}} = \frac{\partial L}{\partial y} \frac{\partial y}{\partial x_{1,2}}
$$

Xem các đạo hàm dưới dạng generalized matrices, $\frac{\partial L}{\partial y}$ có shape là $(1) \times (n \times m)$, $\frac{\partial y}{\partial x_{1,1}}$ có shape là $(n \times m) \times 1$ do đó product $\frac{\partial y}{\partial x_{1,1}}$ có shape là $(1) \times (1)$. Nếu chúng ta xem $\frac{\partial L}{\partial y}$ và $\frac{\partial y}{\partial x_{1,1}}$ như các ma trận có kích thước $n \times m$ thì generalized matrix product đơn giản là dot product $\frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial x_{1,1}} $.

Bây giờ chúng ta tính:

$$
\frac{\partial y}{\partial x_{1,1}} = \left ( \frac{\partial y_{1,1}}{\partial x_{1,1}} ~~ \frac{\partial y_{1,2}}{\partial x_{1,1}} ~~ \frac{\partial y_{1,3}}{\partial x_{1,1}}\right ) = 
\left ( w_{1,1} ~~ w_{1,2} ~~ w_{1,3} \right )
$$

$$
\frac{\partial y}{\partial x_{1,2}} = \left ( \frac{\partial y_{1,1}}{\partial x_{1,2}} ~~ \frac{\partial y_{1,2}}{\partial x_{1,2}} ~~ \frac{\partial y_{1,3}}{\partial x_{1,2}}\right ) = 
\left ( w_{2,1} ~~ w_{2,2} ~~ w_{2,3} \right )
$$

Nên nhớ ở đây $y$ là vector hàng nên các gradient nhận được cũng là vector hàng. Bây giờ kết hợp các kết quả lại chúng ta có:


$$
\frac{\partial L}{\partial x} =
\begin{bmatrix}
dx_{1,1}\\
dx_{1,2}
\end{bmatrix} = 
\begin{bmatrix}
dy_{1,1} w_{1,1} + dy_{1,2} w_{1,2} + dy_{1,3} w_{1,3}\\
dy_{1,1} w_{2,1} + dy_{1,2} w_{2,2} + dy_{1,3} w_{2,3}
\end{bmatrix}
$$

## Tài liệu tham khảo
1. https://en.wikipedia.org/wiki/Matrix_calculus#Numerator-layout_notation 
2. https://explained.ai/matrix-calculus/
3. http://cs231n.github.io/optimization-2/
4. http://cs231n.stanford.edu/handouts/derivatives.pdf