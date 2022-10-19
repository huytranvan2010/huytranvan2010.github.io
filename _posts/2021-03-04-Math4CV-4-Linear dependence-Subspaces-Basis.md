---
layout: post
mathjax: true
title: "[Math4CV-4] Linear dependence. Subspaces. Basis"
tags: [Math4CV]
comments: true
---

**Linear dependence** (phụ thuộc tuyến tính) cho phép chúng ta giảm chiều của vấn đề quan tâm và loại bỏ các thông tin dư thừa.
Ví dụ: cho 2 vector biểu diễn các mảng dữ liệu:
$$ \mathbf{x} = (1, 2, -2, 3), \mathbf{y} = (2, 4, -4, 6) $$

Nhận thấy $ \mathbf{y} = 2 \mathbf{x} $. Điều này có nghĩa rằng $ \mathbf{y} $ không mang lại thông tin gì mới.

Cùng xem một ví dụ khác, cho 3 vector 
$$ \mathbf{x} = (1, 2, -2, 3), \mathbf{y} = (1, 3, 7, 5), \mathbf{z} = (2, 5, 5, 8) $$

Nhận thấy $ \mathbf{z} = \mathbf{x} + \mathbf{y} $. Điều này có nghĩa rằng chúng ta có thể xây dựng $ \mathbf{z} $ khi biết 2 vector $ \mathbf{x}, \mathbf{y} $. Đối với xử lý dữ liệu các thông tin quan trọng được cho bởi 2 vector $ \mathbf{x}, \mathbf{y} $.

**Linear combination** (tổ hợp tuyến tính). Cho các vector $ \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k \in \mathbb{R}^n $ và $ \alpha_1, \alpha_2 ... \alpha_n$ là các số vô hướng. Tổ hợp tuyến tính của các vector được định nghĩa như sau:

$$ \alpha_1 \mathbf{x}_1 + \alpha_2 \mathbf{x}_2 + ... + \alpha_k \mathbf{x}_k = \sum_{i=1}^{k}\alpha_i \mathbf{x}_i $$

Tổ hợp tuyến tính này là một vector. Tổ hợp tuyến tính gọi là tầm thường nếu tất cả các hệ số $ \alpha_i = 0$ và cho về một vector $\mathbf{0}$. Tổ hợp tuyến tính là không tầm thường nếu có ít nhất hệ số nào đó khác 0 và nó cũng có thể trả về một vector $\mathbf{0}$.

Bộ các vector $ \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k $ gọi là **phụ thuộc tuyến tính** nếu tồn tại bộ tổ hợp tuyến tính không tầm thường bằng 0 (ít nhất một hệ số khác 0). 

$$ \alpha_1 \mathbf{x}_1 + \alpha_2 \mathbf{x}_2 + ... + \alpha_n \mathbf{x}_n = 0 $$

Bộ các vector $ \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k $ gọi là **độc lập tuyến tính** nếu chỉ có tổ hợp tuyến tính tầm thường của các vector đó bằng 0 (tất cả các hệ số bằng 0).

**Bổ đề:** Bộ các vector là phụ thuộc tuyến tính khi và chỉ khi một vector là tổ hợp tuyến tính của các vector khác.

Ví dụ $\mathbf{u} = (1, 1)$, $\mathbf{v} = (1, 2)$, $\mathbf{z}=(2, 3)$. Nhận thấy $\mathbf{u} + \mathbf{v} - \mathbf{z} = 0$, $\mathbf{u}, \mathbf{v}, \mathbf{z}$ là một tổ hợp tuyến tính không tầm thường. Một vector là tổ hợp tuyến tính của các vector khác, ví dụ như $\mathbf{z} = \mathbf{u} + \mathbf{v}$.

**Subspaces** (không gian con)

Tập hợp con $ V \subset \mathbb{R}^n $ được gọi là không gian con của không gian vector $\mathbb{R}^n $ nếu bản thân $ V $ cũng là một không gian vector với phép cộng vector và phép nhân vô hướng được định nghĩa trên $ \mathbb{R}^n $. Điều này có nghĩa rằng với bất kì $ \mathbf{x}, \mathbf{y} \in V $ và 2 số vô hướng $\alpha, \beta$ chúng ta sẽ có $ \alpha \mathbf{x} + \beta \mathbf{y} \in V $. 

Linear operation (phép toán tuyến tính) trên vector $\in V$ cũng tạo ra một vector $\in V$, do đó $V$ là một không gian tuyến tính.

Bất kì tổ hợp các vector $ \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k \in \mathbb{R}^n $ đều tạo ra một không gian con trong $ \mathbb{R}^n $. Không gian con này được gọi là **span** của bộ các vector đó.
$$ span(\mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k) = { \mathbf{x} \in \mathbb{R}^n: \mathbf{x} =\alpha_1 \mathbf{x}_1 + \alpha_2 \mathbf{x}_2 + ... + \alpha_n \mathbf{x}_n} $$

Ví dụ 2 vector $\mathbf{x}_1=(1, 0, 0, 0, 0)$ và $\mathbf{x}_2 = (0, 1, 0, 0, 0)$. Nhận thấy **span** của 2 vectors đó là tập hợp các vector có dạng $(a, b, 0, 0, 0)$. Chúng thỏa mãn điều kiện về phép cộng vector và phép nhân vô hướng nên nó là không gian con của không gian vector $\mathbb{R}^5$.

**Basis** (cơ sở)

$ V \subset \mathbb{R}^n $ là không gian con của $\mathbb{R}^n$. Bộ các vectors $\mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m \in V$ được gọi là cơ sở của $V$ nếu:

**1.** Vectors $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m $ độc lập tuyến tính
**2.** $span(\mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m) = V $ (không gian con được tạo ra bởi tổ hợp các vector đó chính là $V$)

**Định lý:** $V$ là không gian con của không gian vector. Số lượng vector của bất kì cơ sở nào của không gian con $V$ đều như nhau và được gọi là số chiều (dimensionality) của $V$, kí hiệu là $dim(V)$.

Có thể thấy:
* $dim(\mathbb{R}^n) = n$
* Bất kì không gian con $ V \subset \mathbb{R}^n $, $dim(V) \leq n$

Ví dụ cơ sở trong $\mathbb{R}^n$ (thỏa mãn 2 điều kiện):

$$
\begin{matrix}
 \mathbf{u}_1 = (1, 0,..., 0)\\
 \mathbf{u}_2 = (0, 1,..., 0)\\
 \dots\\
 \mathbf{u}_n = (0, 0,..., 1)\\
\end{matrix}
$$
- Các vectors $\mathbf{u}_1$, $\mathbf{u}_2$,..., $\mathbf{u}_n$ độc lập tuyến tính:

$$ \alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + ... + \alpha_n \mathbf{u}_n = (\alpha_1, \alpha_2, ..., \alpha_n) = \mathbf{0} \leftrightarrow \alpha_s = 0$$
- $span(\mathbf{u}_1$, $\mathbf{u}_2$,..., $\mathbf{u}_n) = \mathbb{R}^n$

$$\mathbf{x} = (x_1, x_2,..., x_n) = x_1 \mathbf{u}_1 + x_2 \mathbf{u}_2 + ... + x_n \mathbf{u}_n $$

Cơ sở trên được gọi là cơ sở chuẩn hay tự nhiên của không gian $\mathbb{R}$.

**Ví dụ 1:** $\mathbf{x}_1 = (1, 2, 3)$, $\mathbf{x}_2 = (3, 6, 9)$

$V = span(\mathbf{x}_1, \mathbf{x}_2)$, nhận thấy $\mathbf{x}_1$, $\mathbf{x}_2$ phụ thuộc tuyến tính, do đó $dim(V) = 1$ và cơ sở của V là $\mathbf{u}_1 = (1, 2, 3)$

**Ví dụ 2:** $\mathbf{x}_1 = (1, 1, -1)$, $\mathbf{x}_2 = (1, 2, 1)$, $\mathbf{x}_3 = (2, 3, 0)$

$V = span(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3)$, nhận thấy $\mathbf{x}_1$, $\mathbf{x}_2$ , $\mathbf{x}_3$ phụ thuộc tuyến tính, do đó $dim(V) = 2$ và cơ sở của V là $\mathbf{u}_1 = (1, 1, -1)$ và $\mathbf{u}_2 = (1, 2, 1)$. Ở đây chúng ta có $\mathbf{x}_3 = \mathbf{u}_1 + \mathbf{u}_2$.