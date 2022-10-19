---
layout: post
mathjax: true
title: "Covariance matrix - Part 2"
tags: [Math4CV]
comments: true
---

Bài trước chúng ta đã tìm hiểu sơ bộ về covariance matrix và ví dụ về cách tính trên dữ liệu mẫu. Các bạn có thể xem lại [tại đây](https://huytranvan2010.github.io/Covariance-matrix/). Trong phần này cùng biểu diễn covariance matrix thông qua vectorization.

## Covariance matrix

Covariance matrix $\mathbf{C}$ là ma trận vuông với các phần tử $C_{i,j} = \sigma(x_i,x_j)$, trong đó $\mathbf{C} \in \mathbb{R}^{d \times d}$, $d$ là số dimensions hay số lượng random variables của data (số lượng features như chiều cao, cân nặng). Ví dụ mỗi data về object của chúng ta là vector 3 chiều thể hiện chiều cao, độ dài, độ rộng, khi đó covariance matrix sẽ thuộc $\mathbf{C} \in \mathbb{R}^{3 \times 3}$.

Tổng quát, mỗi data point của chúng ta là vector cột $\mathbf{x}^{(i)}$ $\in \mathbb{R}^{d \times 1}$. Tổng cộng có $N$ data points. Khi đó covariance matrix cho data được biểu diễn như sau:

$$\mathbf{C} = \frac{1}{N-1}\sum_{i=1}^N \left(\mathbf{x}^{(i)} - \bar{\mathbf{x}}\right) \left(\mathbf{x}^{(i)} - \bar{\mathbf{x}})\right)^T ~~~~~(1)$$

Dễ dàng kiểm tra lại shape phù hợp, ở đây $d \times 1$ và $1 \times d$ nên chúng ta có covariance matrix với shape là $d \times d$

$$
\mathbf{x}^{(i)} = \begin{bmatrix}
 x_1^{(1)}&  x_2^{(1)}& \dots& x_d^{(1)}
\end{bmatrix}^T ~~~~~(2)
$$ 

là một vector cột $\mathbf{x}^{(i)} \in \mathbb{R}^{d \times 1}$

Lúc này ta có thể biểu diễn ma trận dữ liệu $\mathbf{X} \in \mathbb{R}^ {d \times N}$ với mỗi cột đại diện cho một example

$$
\mathbf{X} = 
\begin{bmatrix}
|& |& & |\\
\mathbf{x}^{(1)}& \mathbf{x}^{(2)}& \dots & \mathbf{x}^{(N)}\\ 
|& |& & |
\end{bmatrix} ~~~~~~(3)
$$

Chuyển vị của ma trận $\mathbf{X}$
$$
\mathbf{X}^T = 
\begin{bmatrix}
-\mathbf{x}^{(1)T}-\\ 
-\mathbf{x}^{(1)T}-\\ 
\vdots \\
-\mathbf{x}^{(N)T}-
\end{bmatrix} ~~~~~~(4)
$$

Lúc này dễ nhận thấy covariance matrix $\mathbf{C}$ trong công thức (1) sẽ trở thành.

$$
\mathbf{C} = \frac{1}{N-1} \left(\mathbf{X} - \bar{X}\right) \left( \mathbf{X} - \bar{X} \right)^T ~~~~~~(5)
$$

Có thể viết gọn lại như sau:

$$
\mathbf{C} = \frac{1}{N-1} \mathbf{\bar{X}} \mathbf{\bar{X}}^T ~~~~~(8)
$$

trong đó ma trận $\mathbf{\bar{X}}$ nhận được từ ma trận $\mathbf{X}$ bằng cách trừ các cột đi trung bình của các cột (nhớ mỗi cột là một example). Cách chúng ta biểu diễn này cũng chính là cách Numpy sử dụng để xác định covariance matrix của data.

Quay lại với ví dụ bên trên chúng ta có data.

|STT  | Chiều cao (m)| Cân nặng (kg)|
|:---:| :-----------:| :----------: |
|1    | 1.6          | 50           |
|2    | 1.7          | 52           |
|3    | 1.75         | 55           |
|4    | 1.63         | 49           |

Đi xây dựng ma trận $\mathbf{X}$ với mỗi cột là một example.

$$
\mathbf{X} = 
\begin{bmatrix}
1.6& 1.7& 1.75& 1.63&\\
50& 52& 55& 49
\end{bmatrix}
$$

$$
\mathbf{X}^T = 
\begin{bmatrix}
1.6& 50\\
1.7& 52\\
1.75& 55\\
1.63& 49\\
\end{bmatrix}
$$

Xác định vector cột trung bình của ma trận $\mathbf{X}$ ta có:

$$
\bar{X} = 
\begin{bmatrix}
1.67\\ 
51.5
\end{bmatrix}
$$

Lấy ma trận $\mathbf{X}$ trừ đi trung bình của các cột $\bar{X}$ ta có 

$$
\mathbf{\bar{X}} = \mathbf{X} - \bar{X} = 
\begin{bmatrix}
-0.07& 0.03& 0.08& -0.04\\
-1.5& 0.5& 3.5& -2.5
\end{bmatrix}
$$

$$
\mathbf{\bar{X}}^T = 
\begin{bmatrix}
-0.07& -1.5\\
0.03& 0.5\\
0.08& 3.5\\
-0.04& -2.5\\
\end{bmatrix}
$$

Covariance matrix:

$$
C = \frac{1}{N-1} \mathbf{\bar{X}} \mathbf{\bar{X}}^T = 
\frac{1}{3}
\begin{bmatrix}
-0.07& 0.03& 0.08& -0.04\\
-1.5& 0.5& 3.5& -2.5
\end{bmatrix} 
\begin{bmatrix}
-0.07& -1.5\\
0.03& 0.5\\
0.08& 3.5\\
-0.04& -2.5\\
\end{bmatrix} =
\begin{bmatrix}
0.0046& 0.1667\\
0.1667& 7
\end{bmatrix}
$$

Chúng ta đi xây dựng lại hàm xác định covariance matrix của data.

```python
X = np.array([ 
    [1.6, 50],
    [1.7, 52],
    [1.75, 55],
    [1.63, 49],
]).T

def get_cov(X):
    X = X - X.mean(axis=1, keepdims=True) 
    C = 1 / (X.shape[1] - 1) * np.dot(X, X.T)
    return C 

get_cov(X)
```
```python
array([[4.60000000e-03, 1.66666667e-01],
       [1.66666667e-01, 7.00000000e+00]])
```
So sánh lại kết quả với [phần 1](https://huytranvan2010.github.io/Covariance-matrix/) nhận thấy các tính của chúng ta là chính xác.

Phía bên trên chúng ta đang xây dựng ma trận $\mathbf{X}$ với cột tương ứng với example. Chúng ta hoàn toàn có thể xây dựng theo kiểu hàng tương ứng với example, lúc này cần đổi chỗ các ma trận. Cách đơn giản nhất để check xem đúng hay không là kiểm tra shape.

<!-- https://www.utdallas.edu/~Herve/Abdi-EVD2007-pretty.pdf
-->