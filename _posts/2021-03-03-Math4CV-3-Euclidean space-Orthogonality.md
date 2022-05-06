---
layout: post
mathjax: true
title: "[Math4CV-3] Euclidean spaces. Orthogonality"
tags: [Math4CV]
comments: true
---

Không gian Euclid là một trường hợp của không gian vector, ở trong đó xác định thêm phép tính đặc biệt đó là **inner product (scalar product) (tích vô hướng)**. Inner product của 2 vector $ \mathbf{x}, \mathbf{y} $ được kí hiệu là $ \left< \mathbf{x}, \mathbf{y} \right> $ và phải thỏa mãn 4 tính chất sau:
- Inner product không âm. $ \left< \mathbf{x}, \mathbf{x} \right> \geq 0$, dấu = xảy ra khi và chỉ khi $\mathbf{x} = \mathbf{0}$
- Có tính đối xứng: $ \left< \mathbf{x}, \mathbf{y} \right> = \left< \mathbf{y}, \mathbf{x} \right> $
- $ \left< \alpha \mathbf{x}, \mathbf{y} \right> = \alpha \left< \mathbf{x}, \mathbf{y} \right> $, 
- $ \left< \mathbf{x+z}, \mathbf{y} \right> = \left< \mathbf{x}, \mathbf{y} \right> + \left< \mathbf{z}, \mathbf{y} \right>$

**Chú ý**: Công thức cho tích vô hướng có thể thay đổi tuy nhiên phải thỏa mãn 4 tính chất phía trên.

Norm liên hệ với inner product thông qua công thức sau:
$$ || \mathbf{x} || = \sqrt{\left< \mathbf{x}, \mathbf{x} \right>} $$

Norm này thỏa mãn các tiên đề về norm, cụ thể như sau:
- $ \Vert \mathbf{x} \Vert = \sqrt{\left< \mathbf{x}, \mathbf{x} \right>} \geq 0$. Dấu bằng xảy ra khi và chỉ khi $ \mathbf{x} = \mathbf{0} $
- $ {\alpha} \Vert \mathbf{x} \Vert = \sqrt{ \left< \alpha \mathbf{x}, \alpha \mathbf{x} \right>} = \sqrt{ \alpha^2 \left< \mathbf{x}, \mathbf{x} \right>} = \left\| \alpha \right\|  \cdot \Vert \mathbf{x} \Vert $
- Bất đẳng thức Cauchy - Bunyakovsky - Schwartz: 

$$ \left\| \left< \mathbf{x}, \mathbf{y} \right> \right\| \leq \Vert \mathbf{x} \Vert \cdot \Vert \mathbf{y} \Vert $$

Một ví dụ của inner product là **dot product**. Cho $ \mathbf{x}, \mathbf{y} \in \mathbb{R}^n$. Dot product được kí hiệu là $  (\mathbf{x}, \mathbf{y})$ hay $ \mathbf{x} \cdot \mathbf{y} $:

$$ (\mathbf{x}, \mathbf{y}) =  \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^{n}x_i y_i$$

Euclidean norm:

$$ \left\|\mathbf{x} \right\| = \left (\sum_{i=1}^{n}\left| x_i \right|^2  \right )^\frac{1}{2} = ||\mathbf{x} ||_{2}  $$

$C[a, b]$ là tập hợp các hàm liên tục $x(t)$ trên đoạn $[a, b]$. Đây là không gian vector tuyến tính. Inner product trong $C[a, b]$ có thể được định nghĩa như sau:

$$\left< \mathbf{x}, \mathbf{y}\right> = \int_{a}^{b}x(t)y(t)dt$$

Euclidean norm liên quan là:

$$||x||_2 = (\int_{a}^{b}|x(t)|^2 dt)^{1/2}$$

Đối với inner product chúng ta sẽ có loại similarity tương ứng là **cosine similarity**:

$$ cos(\mathbf{x} , \mathbf{y} ) = \frac{\left< \mathbf{x}, \mathbf{y} \right>}{||\mathbf{x} || \cdot ||\mathbf{y} ||}  $$

$$ -1 \leq cos(\mathbf{x} , \mathbf{y} ) \leq  1 $$

Cosine similarity có thể được sử dụng trong nhiều ứng dụng ví dụ đo độ tương đồng giữa face encodings trong bài toán nhận diện khuôn mặt.

**Orthogonality - tính trực giao**

Trong không gian Euclid hai vector được gọi là trực giao nếu $ \left< \mathbf{x}, \mathbf{y} \right> = 0 \Leftrightarrow cos(\mathbf{x} , \mathbf{y} ) = 0 $

Đối với không gian $\mathbb{R}$ với dot product, trực giao của hai vector $\mathbf{x}$ và $\mathbf{y}$ có thể được biểu diễn như sau:

$$\sum_{i=1}^{n}x_i y_i = x_1 y_1 + x_2 y_2 + ... + x_n y_n = 0 $$

Trong data mining, sự trực giao gần với khái niệm independence (độc lập) của 2 mảng dữ liệu. 

Tương tự như vậy $C[a, b]$ - không gian Euclid của các hàm liên tục trong $[a, b]$, inner product:

$$\left< x, y\right> = \int_{a}^{b}x(t)y(t) dt)$$

chúng ta có thể kiểm tra các hàm có trực giao với nhau trong không gian này hay không.








