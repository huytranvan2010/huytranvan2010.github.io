---
layout: post
mathjax: true
title: "[Math4CV-1] Ma trận"
tags: [Math4CV]
comments: true
---

### Giới thiệu về vector

Có thể hiểu đơn giản **vector là một mảng các giá trị số**. Mỗi giá trị trong mảng được gọi là tọa độ hay thành phần của vector. Chiều của vector (dimension) chính là số thành phần (hay số tọa độ của nó). Ví dụ  $(1, 2, 3.3)$ là vector có 3 chiều.

**Sparse vector** - vector mà các thành phần của nó chủ yếu là 0, ví dụ $(0, 1, 0, 0, 0, 0, 0.1)$ - sparse vector có chiều là 7.

Số chiều của sparse vector có thể rất lớn nhưng nó chỉ mang lượng nhỏ thông tin (chỉ một số thành phần khác 0).

Định nghĩa chính thức của **sparse vector**: vector có n chiều được coi là sparse nếu số thành phần khác 0 của nó bị giới hạn bởi $\alpha n$, ở đây $\alpha \ll 1$.

### Không gian vector (vector space)

Tập hợp các vectors có cùng chiều tạo thành một không gian vector - vector space (còn gọi là không gian tuyến tính - linear space). Nó được gọi là không gian vector do tồn tại hai phép toán:
- **Phép nhân vector với số vô hướng (scalar)**: nhân mỗi thành phần của vector với số vô hướng để được vector với. Ví dụ $2 \times (1, 1) = (2, 2)$
- **Phép cộng hai vector được vector mới.** Thành phần (tọa độ) của vector mới bằng tổng 2 thành phần tương ứng các các vector ban đầu. Ví dụ $(2, 2) + (1, 1) = (3,3)$

Ngoài ra hai phép toán này thỏa mãn 8 tiên đề. Bên dưới mình sẽ trình bày rõ hơn.

**Real vector space** - tập hợp $V$, mỗi phần tử của $V$ được gọi là vector, tồn tại 2 phép tính:
* Nhân vô hướng: cho vector $\textbf{x}\in V$ và số thực $c \in \mathbb{R}$, tích của $\textbf{x}$ và $c$ là vector $c\textbf{x}$ cũng thuộc $V$
* Cộng: cho vectors $\textbf{x}, \textbf{y} \in V$, tổng của $\textbf{x}$ và $\textbf{y}$ là một vector thuộc $V$ 

**Tiên đề cho phép cộng vector**:
* Phép cộng có tính giao hoán (commutative): $\textbf{x}+\textbf{y} = \textbf{y}+\textbf{x}$
* Phép cộng có tính kết hợp (associative): $(\textbf{x}+\textbf{y})+\textbf{z}=\textbf{x}+(\textbf{y}+\textbf{z})$
* Phần tử $\mathbf{0}$. Tồn tại phần tử $\mathbf{0}$ sao cho $\textbf{x}+ \mathbf{0}=\mathbf{0}+\textbf{x}=\textbf{x}$
* Phần tử nghịch đảo. Cho mỗi phần tử $\textbf{x}$ tồn tại $(-\textbf{x})$ sao cho $\textbf{x}+(-\textbf{x})=(-\textbf{x})+\textbf{x}=\mathbf{0}$

**Tiên đề cho phép nhân vô hướng**:
- Cho vector $\textbf{x} \in V$ và các số nguyên $c, d$ ta có: 
    - $1 \cdot \textbf{x}= \textbf{x} $
    - $(cd)\textbf{x}=c(d\textbf{x})$
- Tính phân phối: Cho vectors $\textbf{x}, \textbf{y} \in V$ và các số nguyên $c, d$:
    * $c(\textbf{x}+\textbf{y})=c\textbf{x}+c\textbf{y}$
    * $(c+d)\textbf{x}=c\textbf{x}+d\textbf{x}$

Một số ví dụ của không gian vector như: không gian các mảng số thực với số chiều cho trước, không gian các ma trận với kích thước cho trước, không gian các hàm số, không gian các biến ngẫu nhiên. Khái niệm vector bây giờ không còn bị giới hạn như những gì chúng ta đã học, nó có thể là bất cứ thứ gì thỏa mãn định nghĩa cho không gian vector bên trên.

**Một số kí hiệu toán học**

- $\mathbb{R}$ - tập hợp các số thực
Vector, mảng các số thực có thể được biểu theo hàng hoặc theo cột.
- $\mathbb{R}^{1\times n}$ - không gian vector hàng có n chiều (tùy thuộc vào lĩnh vực có thể hiểu khác nhau, ví dụ như đây là biểu diễn ma trận có 1 hàng n cột)
- $\mathbb{R}^{n\times 1}$ - không gian vector cột có n chiều
- $\mathbb{R}^{n}$ - không gian vector n chiều

Vector hàng có thể được biểu diễn như sau $\textbf{x}=(x_1, x_2,...,x_n)$, ở đây $x_i$ là tọa tọa $i^{th}$ của vector $\textbf{x}$.

**Linear combination** của 2 vector $\textbf{x}, \textbf{y}$:

$$\alpha \textbf{x} + \beta \textbf{y} =\alpha(x_1, x_2,...,x_n)+\beta(y_1, y_2,...,y_n)=(\alpha x_1 + \beta y_1, \alpha x_2 + \beta y_2,...,\alpha x_n + \beta y_n)$$

Vector cột có thể được biểu diễn như sau $\textbf{x}=\begin{bmatrix}
 x_1\\
 x_2\\
 ...\\
 x_n\\
\end{bmatrix}$

**Linear combination** của 2 vector cột được biểu diễn như sau: 

$$\alpha \textbf{x} + \beta \textbf{y} = \begin{bmatrix}
 \alpha x_1\\
 \alpha x_2\\
 ...\\
 \alpha x_n\\
\end{bmatrix} + \begin{bmatrix}
 \beta y_1\\
 \beta y_2\\
 ...\\
 \beta x_n\\
\end{bmatrix} = \begin{bmatrix}
 \alpha x_1 + \beta y_1\\
 \alpha x_2 + \beta y_2\\
 ...\\
 \alpha x_n + \beta y_n\\
\end{bmatrix}$$

Vector hàng có thể chuyển thành vector cột và ngược lại bằng chuyển vị, chuyển vị của $\textbf{x}$ là $\textbf{x}^T$.
Ví dụ $\textbf{x}=(1, 2, 3, 4)$ thì $\textbf{x}^T=\begin{bmatrix}
 1\\
 2\\
 3\\
 4\\
\end{bmatrix}$. Ở đây đối với vector hàng có thể dùng ngoặc vuông cũng được không sao cả.

<!--
Có thể xem thêm khái niệm không gian vector ở đây.
Chi tiết hơn phải định nghĩa không gian vector trên một trường nào đó như số thực, số phức, số hữu tỉ gì đấy.
https://www.youtube.com/watch?v=B3hg2u2zpSs
https://www.youtube.com/watch?v=1QNBsEiFsA4
-->






















