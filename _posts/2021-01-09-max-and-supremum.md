---
layout: post
title: "Sự khác nhau giữa max và supremum"
tags: [Giải Tích]
comments: true
---

Đây chỉ một ghi chú nhỏ mình muốn note lại trong quá trình tìm hiểu. Mọi thứ sẽ không được liền mạch lắm.

Giá trị lớn nhất (maximum) của một tập hợp phải là phần tử của tập hợp đó. Điều này không đúng với supremum.

Nếu $X$ là tập được sắp một phần (partially ordered set), $S$ là tập con (subset), $s_0$ là supremum của $S$ khi và chỉ khi:
- $s \leq s_0$ với mọi $ s \in S$ 
- Nếu $t \in X$ mà $s \leq t$ với mọi $s \in S$ thì $s_0 \leq t$

Ngược lại, phần tử $m$ được gọi là maximum của $S$ khi và chỉ khi:
- $s \leq m$ với mọi $s \in S$
- $m \in S$

Để ý rằng nếu S có maximum thì maximum đó chính là supremum vì nó thỏa mãn điều kiện của supremum:
- Tất cả $s \in S$ thì $s \leq m$
- Nếu $t \in X$ mà $s \leq t$ với mọi $s \in S$ thì rõ ràng $m \leq t$ vì $m \in S$.

**Kết luận**: maximum và supremum là hai khái niệm khác nhau. Mối quan hệ giữa maximum và supremum như sau:
- Nếu $S$ có maximum $m$ thì $S$ cũng có supremum và $m$ chính là supremum của $S$.
- Ngược lại nếu $S$ có supremum $s$ thì $S$ có maximum khi và chỉ khi $s \in S$, trong trường hợp này thì maximum cũng chính là $s$.

Một số ví dụ
- $\text{sup} \{ 1, 2, 3\} = 3$
- $\text{sup} \{ x \in \mathbb{R}: 0 \leq x \leq 1\} = 1$
- $\text{sup}\{ (-1)^n - \frac{1}{n}: n \in N^*\} = 1$
- $\text{sup} \{a+b: a \in A ~ \text{và} ~ b \in B \} = \text{sup}(A) + \text{sup}(B)$
- $\text{sup}\{x \in Q: x^2 < 2 \} = \sqrt{2}$ 

Nếu tập $S$ rỗng thì $\text{sup}(S) = - \infty$, nếu $S$ không bị chặn trên thì $\text{sup}(S) = + \infty$

