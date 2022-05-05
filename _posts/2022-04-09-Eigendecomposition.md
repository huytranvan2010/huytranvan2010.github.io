---
layout: post
mathjax: true
title: "Eigendecomposition của ma trận"
tags: [Math4CV]
comments: true
---

Một số ma trận có thể được phân tách thành tích các ma trận "đẹp" khác nhau. Eigendecomposition chỉ hoạt động cho ma trận vuông, không giống như Singular Value Decomposition hoạt động cho cả ma trận hình chữ nhật (kích thước 2 chiều không nhất thiết bằng nhau). Hơn thế nữa ma trận cần có tập hợp các eigenvectors là độc lập tuyến tính.

Nếu ma trận $\mathbf{A} \in \mathbb{R}^{d \times d}$ thỏa mãn điều kiện trên, chúng ta sắp xếp các eigenvectors của ma trận $\mathbf{A}$ thành một ma trận như sau:

$$
\mathbf{S} = 
\begin{bmatrix}
\mathbf{x}_1& \mathbf{x}_2& \dots& \mathbf{x}_d\\
\end{bmatrix}~~~~~(1)
$$

$\mathbf{S}$ được biểu diễn dưới dạng vector hàng của các vector cột. Các eigenvector $\mathbf{x}_1$ là các vector $\in \mathbb{R}^{d \times 1}$.

Nhân ma trận $\mathbf{A}$ với ma trận $\mathbf{S}$ ta có:

$$
\mathbf{A} \mathbf{S} = 
\begin{bmatrix}
\mathbf{A}\mathbf{x}_1& \mathbf{A}\mathbf{x}_2& \dots& \mathbf{A}\mathbf{x}_d\\
\end{bmatrix}~~~~~(2)
$$

Cột của ma trận mới bằng ma trận $\mathbf{A}$ nhân với từng cột của ma trận $\mathbf{S}$. Các bạn có thể xem lại một số biểu diễn của tích hai ma trận.

Kết hợp với định nghĩa của eigenvector và eigenvalue cho ma trận $\mathbf{A}$ chúng ta có:

$$
\mathbf{A} \mathbf{S} = 
\begin{bmatrix}
\lambda\mathbf{x}_1& \lambda\mathbf{x}_2& \dots& \lambda\mathbf{x}_d\\
\end{bmatrix}~~~~~(3)
$$

Chúng ta có thể viết lại (3) như sau:

$$
\mathbf{A} \mathbf{S} = 
\begin{bmatrix}
\mathbf{x}_1& \mathbf{x}_2& \dots& \mathbf{x}_d\\
\end{bmatrix} 
\begin{bmatrix}
\lambda_1& 0& \dots& 0\\
0& \lambda_2& \dots& 0\\
\vdots& \vdots& \ddots& \vdots\\
0& 0& \dots& \lambda_n
\end{bmatrix} = 
\mathbf{S} \Lambda~~~~~(4)
$$

Do $\mathbf{S}$ là ma trận vuông với các cột độc lập tuyến tính nên nó khả nghịch. Do đó chúng ta có:

$$
\mathbf{A} = \mathbf{S} \Lambda \mathbf{S}^{-1}
$$

Biểu thức này được gọi là **eigendecomposition** của ma trận $\mathbf{A}$ thành tích ma trận $\mathbf{S}$ với các cột được tạo bởi các eigenvectors của ma trận $\mathbf{A}$, ma trận đường chéo với các phần tử trên đường chéo là eigenvalues của ma trận $\mathbf{A}$ và nghịch đảo của ma trận $\mathbf{S}$. Do 3 ma trận này đặc biệt nên eigendecomposition có một số ứng dụng rất hữu ích.

**Ứng dụng của eigendecomposition trong việc tính $\mathbf{A}^k$**

Nhận thấy tính bình phương của ma trận đường chéo chỉ cần đơn giản lấy bình phương của các phần tử trên đường chéo chính là được.

Theo định nghĩa của eigenvector cho ma trận $\mathbf{A}$ chúng ta có:

$$
\mathbf{A} \mathbf{x} = \lambda \mathbf{x}
$$

Nhân vào bên trái cả hai vế với $\mathbf{A}$ ta nhận được:

$$
\mathbf{A}^2 \mathbf{x} = \lambda^2 \mathbf{x}
$$

Điều này đồng nghĩa với việc $\mathbf{A}^2$ có cùng eigenvectors như $\mathbf{A}$, eigenvalues sẽ là bình phương eigenvalues của $\mathbf{A}$. 

Bởi vì $\mathbf{A}^2$ có cùng eigenvectors như $\mathbf{A}$, chúng ta có thể sử dụng eigendecomposition của $\mathbf{A}$ để biểu diễn $\mathbf{A}^2$ như sau:

$$
\mathbf{A}^2 = \mathbf{S} \Lambda \mathbf{S}^{-1} \mathbf{S} \Lambda \mathbf{S}^{-1} = \mathbf{S} \Lambda^2 \mathbf{S}^{-1}
$$

Nên nhớ $\mathbf{S}$ là ma trận với cột chính là các eigenvectors của ma trận $\mathbf{A}$.

Lặp lại quá trình này hay dùng quy nạp chúng ta có 

$$
\mathbf{A}^k = \mathbf{S} \Lambda^k \mathbf{S}^{-1}
$$

Lúc này việc xác định $\mathbf{A}^k$ rất dễ dàng khi đã biết eigenvectors của ma trận ban đầu $\mathbf{A}$.

Ví dụ trong [bài trước](https://huytranvan2010.github.io/Eigenvectors-eigenvalues/) có ma trận 

$$\mathbf{A} = \begin{bmatrix}2& 3\\ 2& 1 \end{bmatrix}$$ 
xác định được hai eigenvectors 

$$\mathbf{v}_1 = 
\begin{bmatrix}
-1\\
1
\end{bmatrix} ~~~~~
\mathbf{v}_2 = 
\begin{bmatrix}
3\\
2
\end{bmatrix}$$

tương ứng với eigenvalues $\lambda_1 = -1$ và $\lambda_2 = 4$. Lúc này ta có:

$$
\mathbf{A}^{20} = \mathbf{S} \Lambda^{20} \mathbf{S}^{-1} = 
\begin{bmatrix}
-1& 3\\
1& 2
\end{bmatrix}
\begin{bmatrix}
1& 0\\
0& 4^{20}
\end{bmatrix}
\begin{bmatrix}
-1& 3\\
1& 2
\end{bmatrix}^{-1}
$$

Như vậy chúng ta đã tìm hiểu về eigendecomposition của ma trận và một số ứng dụng của nó. Trong bài sau chúng ta sẽ nói về một trường hợp đặc biệt là eigendecomposition của covariance matrix, nó có ứng dụng trong Principal Component Analysis (PCA) để giảm chiều dữ liệu.

<!--
https://blueblazin.github.io/math/2016/08/18/eigenvalue-decomposition.html
https://guzintamath.com/textsavvy/2019/02/02/eigenvalue-decomposition/
https://www.utdallas.edu/~Herve/Abdi-EVD2007-pretty.pdf
https://www.math.usm.edu/lambers/cos702/cos702_files/docs/PCA.pdf   Lý thuyết hay đầy đủ
https://blog.clairvoyantsoft.com/eigen-decomposition-and-pca-c50f4ca15501
-->