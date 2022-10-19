---
layout: post
mathjax: true
title: "[Math4CV-12] Trace của ma trận"
tags: [Math4CV]
comments: true
---

### Định nghĩa

**Trace** của ma trận vuông $\mathbf{A} \in \mathbb{R}^{n \times n}$ bằng tổng các phần tử trên đường chéo chính:

$$
\text{trace}(\mathbf{A}) = a_{11}+a_{22}+\dots+a_{nn} = \sum_{i=1}^n a_{ii}
$$

Trace chỉ được định nghĩa cho ma trận vuông.

Ví dụ chúng ta có ma trận $\mathbf{A}$:

$$
\mathbf{A} = 
\begin{bmatrix}
1& 2& 3\\
4& 5& 6\\
17& 8& 9
\end{bmatrix}
$$

thì $\text{trace}(\mathbf{A}) = 1 + 5 + 9 = 15$

### Tính chất

Một số tính chất của trace với điều kiện các ma trận trong hàm $trace$ là vuông và phép nhân ma trận thực hiện được:

**1.** $\text{trace}(\mathbf{A}) = \text{trace}(\mathbf{A}^T)$

Điều này hiển nhiên vì các phần tử trên đường chéo chính của ma trận chuyển vị và ma trận ban đầu như nhau.

**2.** $\text{trace}(k\mathbf{A}) = k\text{trace}(\mathbf{A})$ với $k$ bất kỳ

Điều này cũng hiển nhiên vì các phần tử trên đường chéo chính nhân thêm với $k$.

**3.** $\text{trace}(\mathbf{A} + \mathbf{B}) = \text{trace}(\mathbf{A}) + \text{trace}(\mathbf{B}) $

**4.** Cho ma trận $\mathbf{A} \in \mathbf{R}^{m \times n}$ và ma trận $\mathbf{B} \in \mathbf{R}^{n \times m}$ thì:

$$
\text{trace}(\mathbf{A} \mathbf{B}) = \text{trace}(\mathbf{B} \mathbf{A})
$$

Thật vậy

$$\text{trace}(\mathbf{A} \mathbf{B}) = \sum_{i=1}^m \mathbf{a}_{i*} \mathbf{b}_{*i} = \sum_{i=1}^m \sum_{j=1}^n a_{ij} b_{ji}$$

$$\text{trace}(\mathbf{B} \mathbf{A}) = \sum_{j=1}^n \mathbf{b}_{j*} \mathbf{a}_{*j} = \sum_{j=1}^n \sum_{i=1}^m b_{ji} a_{ij} $$

Có thể đổi vị trí lấy tổng sigma do đó ta có biểu thức trên. Để dễ hiểu hơn có thể viết tường minh hai công thức trên là thấy ngay.

**5.** $\text{trace}(\mathbf{ABC}) = \text{trace}(\mathbf{CAB}) = \text{trace} (\mathbf{BCA})$

Cái này được suy ra từ tính chất 4.

**5.** Trace của ma trận liên hợp.

Cho $\mathbf{A}$ là ma trận vuông cấp $n$, $\mathbf{P}$ là ma trận vuông cấp $n$ và khả nghịch. Liên hợp của $\mathbf{A}$ theo $\mathbf{P}$ là $\mathbf{P} \mathbf{A} \mathbf{P}^{-1}$, khi đó ta có:

$$
\text{trace}(\mathbf{A}) = \text{trace}(\mathbf{P} \mathbf{A} \mathbf{P}^{-1})
$$

Điều này có nghĩa là khi lấy liên hợp thì trace của ma trận không đổi.

Chứng mình: Nhận thấy theo tính chất (4) ta sẽ có:

$$
\text{trace}(\mathbf{P} \mathbf{A} \mathbf{P}^{-1}) = \text{trace}(\mathbf{P}^{-1} \mathbf{P} \mathbf{A}) = \text{trace}(\mathbf{I}_n \mathbf{A}) = \text{trace}(\mathbf{A})
$$
**6.** Trace của ma trận $\mathbf{A}$ bằng tổng các giá trị riêng của nó.

$$
\text{trace}(\mathbf{A}) = \sum_{i=1}^n \lambda_i
$$

Có thể xem lại về giá trị riêng [tại đây](https://huytranvan2010.github.io/Eigenvectors-eigenvalues/).

Tính chất này có thể chứng minh dựa trên [eigendecomposition](https://huytranvan2010.github.io/Eigendecomposition/) của ma trận vuông $\mathbf{A}$. Ma trận $\mathbf{A}$ có thể phân tích thành:

$$\mathbf{A} = \mathbf{S} \Lambda \mathbf{S}^{-1}$$

Với $\mathbf{S}$ là ma trận mà các cột chính là các eigenvectors của ma trận $\mathbf{A}$, còn $\Lambda$ là ma trận đường chéo, các phần tử trên đường chéo là các eigenvalues tương ứng. Theo tính chất 4 ta có,

$$
\text{trace}(\mathbf{A}) = \text{trace}(\mathbf{S^{-1}S \Lambda}) = \text{trace}(\Lambda) = \sum_{i=1}^n \lambda_i
$$
**7.** Liên hệ trace với Frobenius norm của ma trận.

$$
\lVert\mathbf{A} \rVert_F^2 = \text{trace}(\mathbf{A}^T\mathbf{A}) = \text{trace}(\mathbf{A}\mathbf{A}^T)
$$ 

với $\mathbf{A}$ là ma trận bất kỳ, có thể không vuông

Chứng minh: Có thể biểu diễn ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$ dưới dạng như sau:

$$
\mathbf{A} = 
\begin{bmatrix}
a_{11}& a_{12}& \dots& a_{1n}\\
a_{21}& a_{22}& \dots& a_{2n}\\
\vdots& \vdots& \ddots& \vdots\\
a_{m1}& a_{m2}& \dots& a_{mn}\\
\end{bmatrix}_{m \times n} = 
\begin{bmatrix}
\mathbf{a}_{1*}\\
\mathbf{a}_{2*}\\
\vdots\\
\mathbf{a}_{m*}\\
\end{bmatrix}_{m \times n}
$$

$$
\mathbf{A}^T = 
\begin{bmatrix}
\mathbf{a}_{1*}^T& \mathbf{a}_{2*}^T \dots& \mathbf{a}_{m*}^T
\end{bmatrix}_{n \times m}
$$

ở đây $\mathbf{a}_{i*}$ là vector hàng thứ $i$, $\mathbf{a}_{i*}^T$ là vector cột. Chúng ta đang biểu diễn $\mathbf{A}$ dưới dạng vector cột của các vector hàng, ma trận $\mathbf{A}^T$ dưới dạng vector hàng của các vector cột. Mục đích để lấy hàng nhân với cột để được scalar.

$$
\text{trace}(\mathbf{A} \mathbf{A}^T) = \sum_{i=1}^m \mathbf{a}_{i*}\mathbf{a}_{i*}^T = \sum_{i=1}^m \sum_{j=1}^n a_{ij} a_{ij} = \lVert \mathbf{A} \rVert_F^2
$$

Như vậy chúng ta đã tìm hiểu khái niệm về trace và một số tính chất của nó.

