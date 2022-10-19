---
layout: post
mathjax: true
title: "[Math4CV-6] Vector space of matrices. Frobenius norm"
tags: [Math4CV]
comments: true
---

Matrix có thể hiểu là các vector xếp cạnh nhau hoặc bảng có $n$ hàng và $m$ cột. Sparse matrix là ma trận với phần lớn các phần tử bằng 0.

Ảnh đen trắng có thể được biểu diễn bởi ma trận. Đối với ảnh màu chúng ta cần dùng tensor để biểu diễn.

$\mathbb{R}$ là tập hợp các số nguyên. $\mathbb{R}^{m \times n}$ là không gian ma trận thực với chiều $m \times n$. $ A \in \mathbb{R}^{m \times n}, A = (a_{ij})$. $a_{i j}$ là phần tử của ma trận ở hàng $i$ và cột $j$.

Tổ hợp tuyến tính của hai ma trận:
$$ \alpha \textbf{A} + \beta \textbf{B} = (\alpha a_{ij} + \beta b_{ij}) $$

**Vector space of matrices**

Dưới đây là 2 phép toán giúp chúng ta coi không gian các matrix là không gian vector:
- Zero matrix là ma trận với tất cả các phần tử bằng 0:

$$\textbf{A} + \textbf{0} = \textbf{A} $$

- Matrix ($\mathbf{-A}$) được định nghĩa là  $\mathbf{-A} = (-\alpha_{ij})$ và ta có:

$$(\mathbf{-A}) + \mathbf{A} = 0$$

Ngoài ra chúng ta cũng có $dim(\mathbb{R}^{n \times m}) = n \cdot m$. Cái này có thể chứng minh bằng cách coi vector là raster representation của matrix.

**Frobenius norm** 

$\mathbb{R}^{m \times n}$ là một không gian vector, nó có thể trang bị cho mình một loại norm là Frobenius.

Frobenius norm của ma trận $ A \in \mathbb{R}^{m \times n} , A = (a_{i j})$:

$$ \left\| \textbf{A} \right\|_F = \left ( \sum_{i=1}^{m}\sum_{j=1}^{n}\left|a_{ij} \right|^2 \right )^\frac{1}{2} $$

Các bạn có thể xem thêm khái niệm norm 1 và norm 2 của ma trận [tại đây](https://huytranvan2010.github.io/Math4CV-2-Norm-distance-similarity/).
