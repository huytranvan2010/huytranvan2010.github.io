---
layout: post
mathjax: true
title: "[Math4CV-2] Norm of vectors. Distance. Similarity"
tags: [Math4CV]
comments: true
---

**Norm of vector**
Cho vector $\mathbf{x}\in \mathbb{R}^{n}$. Làm sao để xác định vector $\mathbf{x}$ nằm xa vector $\mathbf{0}$. Hay vector "lớn", "nhỏ" có nghĩa là gì? Để trả lời câu hỏi đó chúng ta cùng tìm hiểu khái niệm **norm**.

**Norm** của vector $\mathbf{x}$ được kí hiệu là $\left\|\mathbf{x} \right\|$.

**Các tiên đề về norm:**

- Norm không âm: $\left\|\mathbf{x} \right\| \geq 0$, $\left\|\mathbf{x} \right\| = 0$ khi và chỉ khi $\mathbf{x} = \mathbf{0}$
- $\Vert  \alpha \mathbf{x} \Vert  = \left\| {\alpha} \right\| \cdot \Vert  \mathbf{x} \Vert $, với $\alpha \in \mathbb{R}$
- Bất đẳng thức tam giác: $\left\| \mathbf{x} + \mathbf{y} \right\| \leq \left\|\mathbf{x} \right\| + \left\|\mathbf{y} \right\|$

Ở đây chỉ đưa ra các tiên đề về norm chứ không có định nghĩa cụ thể do chúng ta có nhiều không gian và có nhiều loại norm.

Có rất nhiều loại norm khác nhau, hay dùng nhất là norm $L1$ và norm $L2$.

**Manhattan norm**: cho vector $\mathbf{x}\in \mathbb{R}^{n}$

$$ \left\| \mathbf{x} \right\|_{1} = \sum_{i=1}^{n}\left| x_i \right| $$

**Euclidean norm**: cho vector $\mathbf{x}\in \mathbb{R}^{n}$

$$ \Vert \mathbf{x} \Vert_{2} = \left (\sum_{i=1}^{n} \left\| x_i \right\|^2  \right )^\frac{1}{2} $$

**Minkowski norm**: cho vector $\mathbf{x}\in \mathbb{R}^{n}$

$$ \Vert \mathbf{x} \Vert_p = \left (\sum_{i=1}^{n} \left\| x_i \right\|^p  \right )^\frac{1}{p}, p \geq 1 $$, 

**Chebyshev norm**: cho vector $\mathbf{x}\in \mathbb{R}^{n}$
$$ \left\| \mathbf{x} \right\|_{\infty}=\underset{1\leq i\leq n}{max} \left\|x_{i} \right\| $$

**Negative infinity norm:** cho vector $\mathbf{x}\in \mathbb{R}^{n}$

$$ \left\|\mathbf{x} \right\|_{-\infty}=\underset{1\leq i\leq n}{min}\left\| x_{i} \right\| $$

**Norm trong không gian của các hàm liên tục**

$C[a, b]$ là tập hợp các hàm liên tục $x(t)$ trên đoạn $[a, b]$. Đây là không gian vector tuyến tính (để dễ hiểu có thể coi hàm liên tục là một mảng có số chiều vô cùng lớn).
- Minkovski norm ($p \geq 1$):

$$\Vert x \Vert _p = (\int_{a}^{b}|x(t)|^p dt)^{1/p}$$

- Manhetten norm ($p \geq 1$):

$$\Vert x \Vert _1 = (\int_{a}^{b}|x(t)| dt)$$

- Chebyshev norm:

$$\Vert x \Vert _\infty = \underset{a \leq t \leq b}{\text{max}}|x(t)|$$

**Distance (dissimilarity)**

Khoảng cách giữa hai vector $\mathbf{x}, \mathbf{y} \in \mathbb{R}^{n}$ có thể được xác định như sau:
$$ d(\mathbf{x} , \mathbf{y}) = \left\|\mathbf{x} - \mathbf{y} \right\|  ~~~ (1)$$

**Các tiên đề về khoảng cách:**

* Khoảng cách không âm, $d(\mathbf{x} , \mathbf{y}) \geq 0$, dấu $=$ xảy ra khi và chỉ khi $\mathbf{x} = \mathbf{y}$
* Khoảng cách có tính đối xứng: $d(\mathbf{x} , \mathbf{y}) = d(\mathbf{y} , \mathbf{x})$ 
* Bất đẳn thưc tam giác: $d(\mathbf{x} , \mathbf{y}) \leq d(\mathbf{x} , \mathbf{z}) + d(\mathbf{z} , \mathbf{y})$

Các norm khác nhau tạo ta khoảng cách giữa các vector khác nhau. Khoảng cách được xác định bởi norm là đồng nhất (homogeneous) và bất biến khi dịch chuyển (invariant under transslation in $\mathbb{R}$): 

$$d(\alpha \mathbf{x}, \alpha \mathbf{y}) = \alpha d( \mathbf{x},\mathbf{y})$$

$$d(\mathbf{x} + \mathbf{a}, \mathbf{y} + \mathbf{a}) =d( \mathbf{x},\mathbf{y})$$

Có thể dễ dàng chứng minh được 2 công thức này từ định nghĩa (1).

Trong xử lý ảnh có thể biểu diễn ảnh dưới dạng vector (được duỗi ra), sau đó chúng ta có thể đo lường độ tương đồng giữa các ảnh thông qua khoảng cách của các vector đó.

Có nhiều cách để chuyển đổi khoảng cách $d(\mathbf{x} , \mathbf{y})$ giữa 2 vector $\mathbf{x}, \mathbf{y}$ sang độ tương đồng (similarity) giữa 2 vector đó. Một trong những cách chuyển đó là Gaussian:

$$\text{sim}(\mathbf{x}, \mathbf{y}) = \text{exp}\left( \frac{-d^{2}(\mathbf{x},\mathbf{y})}{\sigma ^{2}} \right)$$

ở đây $\sigma$ là tham số tỉ lệ được chọn cho từng mục đích khác nhau, $0 \leq \text{sim}(\mathbf{x}, \mathbf{y}) \leq 1$




























