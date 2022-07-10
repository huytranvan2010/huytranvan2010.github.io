---
layout: post
mathjax: true
title: "[Math4CV-1] Rank of a matrix"
tags: [Math4CV]
comments: true
---

Bài trước chúng ta đã tìm hiểu về khái niệm định thức (được xây dựng cho ma trận vuông). Trong bài này sẽ đi tìm hiểu khái niệm về hạng của ma trận.

**Định nghĩa**: Hạng của ma trận $\mathbf{A}$ là cấp cao nhất của định thức con khác 0 của $\mathbf{A}$. Hạng của ma trận được kí hiệu là $\text{rank}(\mathbf{A})$.

Đối với ma trận $\mathbf{A} \in \mathbb{R}^{m \times n}$, nhận thấy cấp cao nhất của định thức con của $\mathbf{A}$ sẽ là $\min(m, n)$ (sẽ đi lấy định thức cho ma trận vuông). Do đó 

$$\text{rank}(\mathbf{A}) \leq \min(m, n)$$

Xem ví dụ với ma trận 

$$
\mathbf{A} = 
\begin{bmatrix}
1& 2& 3& 4\\
3& 4& 5& 6\\
4& 6& 8& 10
\end{bmatrix}_{3 \times 4}
$$

Ma trận  $\mathbf{A}$ sẽ có các định thức con cấp 1, 2, 3. Chúng ta sẽ đi xét từ định thức có cấp lớn nhất đến cấp nhỏ nhất, dừng lại ở cái nào có giá trị khác 0.

Nhận thấy $\text{r3} = \text{r1} + \text{r2}$, do đó mọi định thức con cấp 3 đều bằng 0. Xét đến định thức con cấp hai. Nhận thấy

$$
\begin{vmatrix}
 1& 2\\ 
 3& 4
\end{vmatrix} = 4 - 6 = 2 \neq 0
$$

Do đó $\text{rank}(\mathbf{A}) = 2$.

Cùng xem ví dụ thứ hai

$$
\mathbf{A} = 
\begin{bmatrix}
1& 2& 3& 4\\
0& 0& 5& 6\\
0& 0& 0& 0
\end{bmatrix}_{3 \times 4}
$$

Nhận thấy hàng thứ 3 bằng 0 nên mọi định thức con bậc 3 bằng 0. Xét định thức con bậc hai.

$$
\begin{vmatrix}
 1& 3\\ 
 0& 5
\end{vmatrix} = 5 - 0 = 5 \neq 0
$$

Do đó $\text{rank}(\mathbf{A}) = 2$

**Chú ý**: 
- Khi lấy định thức con chỉ cần thỏa mãn số hàng số cột, các cột và hàng được lấy không nhất thiết liên tiếp nhau như cách mình lấy ở ví dụ trên.
- Hạng của ma trận bậc thang bằng số hàng khác 0 của nó. *Dựa vào điều này chúng ta có thể biến đổi ma trận ban đầu về dạng ma trận bậc thang để xác định hạng của ma trận thông qua các phép biến đổi sơ cấp.*

Phép biến đổi sơ cấp có làm thay đổi hạng của ma trận? Một số phép biển sơ cấp:
- **Đổi chỗ hai hàng hoặc hai cột**. Cách này làm thay đổi dấu của định thức, tuy nhiên nó không ảnh hưởng đến tính khác 0 của định thức, vì nếu định thức ban đầu khác 0 thì nó vẫn khác 0, bằng 0 thì nó vẫn bằng 0
- **Nhân một hàng hay cột với $k \neq 0$.** Nhận thấy nó cũng không ảnh hưởng đến tính khác 0 của định thức.
- **Cộng vào một hàng (hoặc cột) tổ hợp tuyến tính của các hàng khác (hoặc cột khác)** thì định thức không đổi

**Chú ý**: Nhận thấy điều này không những đúng cho định thức của ma trận ban đầu mà còn đúng cho cả các định thức con của nó nữa.

Ví dụ tìm hạng của ma trận

$$
\mathbf{A} = 
\begin{bmatrix}
1& 2& 3& 4\\
2& -1& 1& 2\\
3& 1& -1& 1\\
4& 3& -3& 3\\
\end{bmatrix} 
\xrightarrow[]{\begin{matrix}
-2r1 + r2\\ 
-3r1 + r3\\
-4r1 + r4 
\end{matrix}}
\begin{bmatrix}
1& 2& 3& 4\\
0& -5& -5& -6\\
0& -5& -10& -11\\
0& -5& -15& -13\\
\end{bmatrix} 
\xrightarrow[]{\begin{matrix}
-r2 + r3\\ 
-r2 + r4 
\end{matrix}}
\begin{bmatrix}
1& 2& 3& 4\\
0& -5& -5& -6\\
0& 0& -5& -5\\
0& 0& -10& -7\\
\end{bmatrix} 
\xrightarrow[]{\begin{matrix} 
-2r3 + r4 
\end{matrix}}
\begin{bmatrix}
1& 2& 3& 4\\
0& -5& -5& -6\\
0& 0& -5& -5\\
0& 0& 0& 3\\
\end{bmatrix} 
$$

Ở đây chỉ dùng phép biến đổi sơ cấp thứ ba, ma trận bậc thang nhận được có hạng bằng 4, do đó $\text{rank}(\mathbf{A}) = 4$.

Có thể sử dụng thư viện Numpy để check lại hạng của matrix $\mathbf{A}$ như sau:

```python
from numpy.linalg import matrix_rank
import numpy as np

A = np.array([
[1, 2, 3, 4],
[2, -1, 1, 2],
[3, 1, -1, 1],
[4, 3, -3, 3]
])

print("Rank of A: ", matrix_rank(A))
```
```
Rank of A: 4
```

**Chú ý**:
- Phép biến đổi sơ cấp này chỉ giúp chúng ta xác định hạng của ma trận ban đầu chứ không giúp chúng ta xác định định thức của ma trận.

<!--
https://www.youtube.com/watch?v=vN6jkfbcWGI&list=PL5g_dfwUnO84IehDgeDlXbwd0pLzhTWSZ&index=9
https://vted.vn/tin-tuc/cac-dang-toan-ve-hang-cua-ma-tran-va-phuong-phap-giai-4791.html
https://vi.wikipedia.org/wiki/H%E1%BA%A1ng_(%C4%91%E1%BA%A1i_s%E1%BB%91_tuy%E1%BA%BFn_t%C3%ADnh)
-->








