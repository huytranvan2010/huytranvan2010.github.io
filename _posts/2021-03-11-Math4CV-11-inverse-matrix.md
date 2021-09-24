---
layout: post
mathjax: true
title: "[Math4CV-11] Inverse matrix"
tags: [Math4CV]
comments: true
---

Ma trận vuông là ma trận có số hàng bằng với số cột. $\mathbb{R}^{n \times n}$ là không gian các ma trận vuông với số chiều là $n$.

Ma trận vuông $\textbf{A} \in \mathbb{R}^{n \times n}$ tạo ra 2 phép ánh xạ tuyến tính:
- Từ $\mathbb{R}^{n \times 1}$ vào $\mathbb{R}^{n \times 1}$, được xác định bởi $\textbf{y} = \textbf{A} \textbf{x}$, trong đó $\textbf{x}$, $\textbf{y}$ là các vector cột
- Từ $\mathbb{R}^{1 \times n}$ vào $\mathbb{R}^{1 \times n}$, được xác định bởi $\textbf{y} =  \textbf{x} \textbf{A}$, trong đó $\textbf{x}$, $\textbf{y}$ là các vector hàng

Trường hợp đặc biệt của ma trận vuông là ma trận đường chéo (diagonal matrix) $\textbf{D} = diag(d_1, d_2, \dots, d_n)$

$\textbf{D} \cdot \textbf{A}$ được ma trận với hàng $i_{th}$ là tích của $d_i$ và hàng $i^{th}$ của ma trận $\textbf{A}$, $i=1 \dots n$

$\textbf{A} \cdot \textbf{D}$ được ma trận với cột $j_{th}$ là tích của $d_j$ và cột $j^{th}$ của ma trận $\textbf{A}$, $j=1 \dots n$

**Ma trận đường chéo (identity matrix)**

$\textbf{I}_n = diag(1, 1, \dots, 1)$

Một số tính chất:
- $rank(\textbf{I}_n) = n$
- $\textbf{I}_n \cdot \textbf{A} = \textbf{A} \cdot \textbf{I}_n = \textbf{A}$
- $\textbf{I}_n \cdot \textbf{x} = \textbf{x}$, $\textbf{x}$ là vector cột
- $\textbf{x} \cdot \textbf{I}_n = \textbf{x}$, $\textbf{x}$ là vector hàng

Ma trận vuông $\textbf{A}$ được gọi là đối xứng nếu:

$$\textbf{A} = \textbf{A}^T$$

Ma trận vuông $\textbf{A}$ gọi là ma trận trực giao nếu:

$$\textbf{A} \cdot \textbf{A}^T = \textbf{A}^T \cdot \textbf{A} = \textbf{I}$$

nhận thấy $a_{i *} \cdot a_{j * }^T = 0, ~ i \neq j$ ngược lại $a_{i * } \cdot a_{j * }^T = 1, ~ i = j$ 

Một số tính chất:
- Các hàng của ma trận trực giao tạo thành cơ sở trực chuẩn của $\mathbb{R}^{1 \times n}$
- Các cột của ma trận trực giao tạo thành cơ sở trực chuẩn trong $\mathbb{R}^{n \times 1}$
- Nếu ma trận $\textbf{A}$ trực giao thì $(\textbf{A} \textbf{u}, \textbf{A} \textbf{v}) = (\textbf{u}, \textbf{v})$, $\Vert\textbf{A} \textbf{u} \Vert_2 = \Vert \textbf{u} \Vert_2$. Ánh xạ tuyến tính bằng ma trận trực giao giữ nguyên khoảng cách và tích vô hướng trong không gian Euclid.
- Frobenius norm của ma trận trực giao: $\Vert \textbf{A} \Vert_F = \sqrt{n}$






