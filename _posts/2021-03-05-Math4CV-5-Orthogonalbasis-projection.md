---
layout: post
mathjax: true
title: "[Math4CV-5] Orthogonal basis. Projection"
tags: [Math4CV]
comments: true
---

## Orthogonal basis (cơ sở trực giao). Projection (hình chiếu)

**Orthogonal system** of vectors (hệ vector trực giao). Giả sử $E$ là không gian Euclid. Bộ các vector $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_k $ khác 0 được gọi là hệ trực giao nếu các vector đôi một trực giao với nhau:

$$ \left< \mathbf{u}_i, \mathbf{u}_j \right> = 0, \text{với}~~ i\neq j,~~ i,j=1,2...k  $$

Hệ vector trực giao luôn **độc lập tuyến tính**. Cái này chứng minh bằng phản ứng. Giả sử nếu hệ vector trực giao phụ thuộc tuyến tính thì $\mathbf{u}\_i = \sum_{j} \mathbf{u}\_j$, nhân cả 2 vế với $\mathbf{u}\_i$ được vế trái lớn hơn 0 (do $ \textbf{u}\_i \neq \textbf{0} $), vế phải bằng 0, điều này không đúng. Do đó hệ vector trực giao là độc lập tuyến tính.

Một cơ sở là hệ trực giao thì gọi là cơ sở trực giao (vừa là cơ sở, vừa có tính chất trực giao).

$ V \subset \mathbb{R}^n $. Bộ các vector $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_n $ được gọi là cơ sở trực giao của $V$ nếu:
- $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m $ là hệ trực giao (như nói ở trên hệ trực giao thì độc lập tuyến tính)
- $span(\mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m) = V$ (không gian con tạo bởi các vector này chính là $V$ hay có thể tạo ra các vector thuộc $V$ từ bộ các vector đó).

**Ví dụ 1**: cơ sở chuẩn của $\mathbb{R}^n$ là cơ sở trực giao (xem lại cơ sở chuẩn của $\mathbb{R}^n$ ở đây).

**Ví dụ 2**: $\mathbf{x}_1=(2, 2, 0)$, $\mathbf{x}_2=(0, -2, 2)$, $\mathbf{x}_3=(3, 2, 1)$. $V = span(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3)$. Bộ các vector $\mathbf{u}_1 = (1, 0, 1)$, $\mathbf{u}_2 = (1, 2, -1)$ là cơ sở trực giao của V, bởi vì chúng ta có:

$$\left< \mathbf{u}_1, \mathbf{u}_2\right> = 0$$

và $\mathbf{x}_1 = \mathbf{u}_1 +\mathbf{u}_2$, $\mathbf{x}_2 = \mathbf{u}_1 - \mathbf{u}_2$, $\mathbf{x}_3 = 2\mathbf{u}_1 +\mathbf{u}_2$. Do đó $span(\mathbf{u}_1,  \mathbf{u}_2) = span(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3)$.  

**Orthomormal system** (hệ trực chuẩn) 

Hệ trực giao $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_k $ được gọi là trực chuẩn nếu :
$$ \left< \mathbf{u}_i, \mathbf{u}_i \right> = 1 $$

Đối với hệ trực chuẩn ta có: $\left\| \mathbf{u}_i \right\| = 1$

Làm sao để chuyển hệ trực giao thành trực chuẩn? Đơn giản chúng ta chỉ cần chia mỗi vector trong hệ trực giao cho norm của chúng.

**Gram-Schmidt algorithm**: chuyển hệ vector $ \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k $ thành hệ trực chuẩn $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m $ sao cho:

$$ span( \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k ) = span( \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m )$$

Trong trường hợp này $dim(span( \mathbf{x}_1, \mathbf{x}_2 ... \mathbf{x}_k )) = m$. Các bạn tự tìm hiểu thêm cách chuyển hệ vector thành hệ trực chuẩn.

**Tính chất**: Nếu $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m $ là cơ sở trực chuẩn của không gian con $V$ khi đó với mọi $\mathbf{u} \in V$ ta có:

$$ \mathbf{u} = \left< \mathbf{u}, \mathbf{u}_1 \right> \mathbf{u}_1 + \left< \mathbf{u}, \mathbf{u}_2 \right> \mathbf{u}_2 + ... + \left< \mathbf{u}, \mathbf{u}_m \right> \mathbf{u}_m   $$

Các bạn có thể tìm hiểu cách chứng minh công thức này.

Ví dụ: cơ sở chuẩn trong $\mathbb{R}$, với $\mathbf{x} = (x_1,..., x_n) \in \mathbb{R}^n$

$$
\begin{matrix}
 \mathbf{u}_1 = (1, 0,..., 0)\\
 \mathbf{u}_2 = (0, 1,..., 0)\\
 \dots\\
 \mathbf{u}_n = (0, 0,..., 1)\\
\end{matrix}
$$

Ta có $\left< \mathbf{x}, \mathbf{u}_1\right> = x_1$, $\left< \mathbf{x}, \mathbf{u}_2\right> = x_2$..., $\left< \mathbf{x}, \mathbf{u}_n\right> = x_n$, khi đó $\mathbf{x} = (x_1,..., x_n) = x_1 \mathbf{u}_1 + ... + x_n \mathbf{u}_n$

## Projection

Sử dụng tính trực giao trong không gian Euclid giúp chúng ta xác định projection của vector lên không gian con.

Cho $V$ là không gian con của không gian Euclid và $\mathbf{x} \in E$. Projection (hình chiếu) của $\mathbf{x}$ lên $V$ là vector $\mathbf{x}^* \in V$ gần với vector $\mathbf{x}$ nhất:

$$|| \mathbf{x} - \mathbf{x}^* || = \underset{\mathbf{u} \in V}{\text{min}} ||\mathbf{x} - \mathbf{u}||  ~~~ (1)$$

Làm sao để tìm projection? Trong các không gian khác, không dễ để tìm $\mathbf{x}^*$, tuy nhiên trong không gian Euclid chúng ta có thể tìm projection thông qua tính chất trực giao như trình bày bên dưới.

Nếu $ \mathbf{u}_1, \mathbf{u}_2 ... \mathbf{u}_m $ là cơ sở của $V$. Khi đó $\mathbf{x}^*$ có thể tìm được thông qua hệ phương trình tuyến tính (được suy ra từ (1)):

$$\left< \mathbf{x} - \mathbf{x}^*, \mathbf{u}_j \right> = 0, ~~~~ j =1,2..., m$$

Đặt $ \mathbf{x}^* = \alpha_1 \mathbf{u}_1 + \alpha_2 \mathbf{u}_2 + ... + \alpha_m \mathbf{u}_m $. Khi đó $\alpha$ có thể tìm được từ hệ phương trình sau (chuyển vế rồi thay j lần lượt = 1...m):

$$
\begin{matrix}
 \left< \mathbf{u}_1, \mathbf{u}_1 \right> \alpha_1 + \left< \mathbf{u}_1, \mathbf{u}_2 \right> \alpha_2 +...+ \left< \mathbf{u}_1, \mathbf{u}_m \right> \alpha_m = \left< \mathbf{u}_1, \mathbf{x} \right> \\
 \left< \mathbf{u}_2, \mathbf{u}_1 \right> \alpha_1 + \left< \mathbf{u}_2, \mathbf{u}_2 \right> \alpha_2 +...+ \left< \mathbf{u}_2, \mathbf{u}_m \right> \alpha_m = \left< \mathbf{u}_2, \mathbf{x} \right>\\
 ...................................................\\
 \left< \mathbf{u}_m, \mathbf{u}_1 \right> \alpha_1 + \left< \mathbf{u}_m, \mathbf{u}_2 \right> \alpha_2 +...+ \left< \mathbf{u}_1, \mathbf{u}_m \right> \alpha_m = \left< \mathbf{u}_m, \mathbf{x} \right>\\
\end{matrix}
$$

Hệ phương trình này có m ẩn và m phương trình. Ma trận của hệ phương trình này là ma trận của inner product các thành phần của cơ sở không gian con $V$ - gọi là Gram matrix. Cơ sở của không gian độc lập tuyến tính nên định thức của Gram matrix khác 0, hệ phương trình có một nghiệm duy nhất.

Hệ phương trình cho projection trong không gian Euclid được đơn giản hóa nếu cơ sở của không gian con là trực giao.

Ví dụ: Tìm projection của vector $\mathbf{x}$ lên không gian con $V=span(\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_2)$, ở đây $\mathbf{x}_1 = (2, 0, 2, 3, 3, -1, 4, -2, 0, 2)$, $\mathbf{x}_2 = (0, -2, 2, -3, -1, -3, -4, 2, 2, 0)$, $\mathbf{x}_3 = (3, -1, 4, 3, 4, -3, 4, -2, 1, 3)$

Nhận thấy bộ vector $\mathbf{u}\_1 = (1, -1, 2, 0, 1, -2, 0, 0, 1, 1)$, $\mathbf{u}\_2 = (1, 1, 0, 3, 2, 1, 4, -2, -1, 1)$ là cơ sở trực giao của $V$ (có thể biểu diễn $\mathbf{x}\_1$, $\mathbf{x}\_2$, $\mathbf{x}\_3$ thông qua $\mathbf{u}\_1$ và $\mathbf{u}\_2$). Chúng ta tìm $\mathbf{x}\_ * = \alpha\_1 \mathbf{u}\_1 + \alpha\_2 \mathbf{u}\_2$

$$
\begin{matrix}
13 \alpha_1 + 0 \cdot \alpha_2 = \left< \mathbf{u}_1, \mathbf{x} \right>\\
0 \cdot \alpha_1 + 38 \alpha_2 = \left< \mathbf{u}_2, \mathbf{x} \right>\\
\end{matrix}
$$

Đi tìm projection cho $\mathbf{x} = (1, -1, 2, -2, 0, -2, 0, 0, 1, 2)$ ta nhận được $\alpha_1 = 1$, $\alpha_2 = -7/38$
