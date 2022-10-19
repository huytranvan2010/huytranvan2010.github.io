---
layout: post
mathjax: true
title: "[Math4CV-10] Square matrix"
tags: [Math4CV]
comments: true
---

Ma trận vuông là ma trận có số hàng bằng với số cột. $\mathbb{R}^{n \times n}$ là không gian các ma trận vuông với số chiều là $n$.

Ma trận vuông $\mathbf{A} \in \mathbb{R}^{n \times n}$ tạo ra 2 phép ánh xạ tuyến tính:
- Từ $\mathbb{R}^{n \times 1}$ vào $\mathbb{R}^{n \times 1}$, được xác định bởi $\mathbf{y} = \mathbf{A} \mathbf{x}$, trong đó $\mathbf{x}$, $\mathbf{y}$ là các vector cột
- Từ $\mathbb{R}^{1 \times n}$ vào $\mathbb{R}^{1 \times n}$, được xác định bởi $\mathbf{y} =  \mathbf{x} \mathbf{A}$, trong đó $\mathbf{x}$, $\mathbf{y}$ là các vector hàng

Trường hợp đặc biệt của ma trận vuông là ma trận đường chéo (diagonal matrix) 

$$\mathbf{D} = diag(d_1, d_2, \dots, d_n)$$

$\mathbf{D} \cdot \mathbf{A}$ được ma trận với hàng $i_{th}$ là tích của $d_i$ và hàng $i^{th}$ của ma trận $\mathbf{A}$, $i=1 \dots n$

$\mathbf{A} \cdot \mathbf{D}$ được ma trận với cột $j_{th}$ là tích của $d_j$ và cột $j^{th}$ của ma trận $\mathbf{A}$, $j=1 \dots n$

**Ma trận đơn vị (identity matrix)**

$$\mathbf{I}_n = diag(1, 1, \dots, 1)$$

Một số tính chất:
- $rank(\mathbf{I}_n) = n$
- $\mathbf{I}_n  \mathbf{A} = \mathbf{A} \mathbf{I}_n = \mathbf{A}$
- $\mathbf{I}_n  \mathbf{x} = \mathbf{x}$, $\mathbf{x}$ là vector cột
- $\mathbf{x} \mathbf{I}_n = \mathbf{x}$, $\mathbf{x}$ là vector hàng

Ma trận vuông $\mathbf{A}$ được gọi là đối xứng nếu:

$$\mathbf{A} = \mathbf{A}^T$$

Ma trận vuông $\mathbf{A}$ gọi là ma trận trực giao nếu:

$$\mathbf{A} \cdot \mathbf{A}^T = \mathbf{A}^T \cdot \mathbf{A} = \mathbf{I}$$

nhận thấy $a_{i * } \cdot a_{j * }^T = 0, ~ i \neq j$ ngược lại $a_{i * } \cdot a_{j * }^T = 1, ~ i = j$, chỗ này là hàng nhân với cột để được một phần tử.

Một số tính chất:
- Các hàng của ma trận trực giao tạo thành cơ sở trực chuẩn của $\mathbb{R}^{1 \times n}$
- Các cột của ma trận trực giao tạo thành cơ sở trực chuẩn trong $\mathbb{R}^{n \times 1}$
- Nếu ma trận $\mathbf{A}$ trực giao thì $(\mathbf{A} \mathbf{u}, \mathbf{A} \mathbf{v}) = (\mathbf{u}, \mathbf{v})$, $\Vert \mathbf{A} \mathbf{u} \Vert_2 = \Vert \mathbf{u} \Vert_2$. Ánh xạ tuyến tính bằng ma trận trực giao giữ nguyên khoảng cách và tích vô hướng trong không gian Euclid.
- Frobenius norm của ma trận trực giao: $\Vert \mathbf{A} \Vert_F = \sqrt{n}$






