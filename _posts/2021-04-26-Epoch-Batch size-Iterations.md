---
layout: post
mathjax: true
title: "Epochs, Batch size, Iterations"
tags: [Gradient Descent]
comments: true
---

Khi mới học Machine Learning và sau này là Deep Learning chúng ta gặp phải các khái niệm như `Epoch`, `Batch size` và `Iterations`. Để khỏi nhầm lẫn mình xin chia sẻ với các bạn sự khác nhau giữa các khái niệm này.

Trước khi đi vào chủ đề chính, chúng ta xem lại thuật toán **Gradient Descent**. Các tham số của mạng được khởi tạo ban đầu, dữ liệu được truyền vào trong mạng Neural Network, thông qua forward propagation xác định được đầu ra, so sánh đầu ra với nhãn ban đầu để tính hàm mất mát. Thông qua back propagation các tham số của mạng được cập nhật. Các quá trình trên được lặp lại nhằm giảm hàm mất mát xuống giá trị thấp nhất có thể.

Một số biến thể của Gradient Descent:
- Batch Gradient Descent
- Stochastic Gradient Descent
- Mini-Batch Gradient Descents

Sự khác nhau chính giữa 3 thuật toán trên chính là số lượng dữ liệu được sử dụng cho mỗi lần cập nhật tham số. Batch Gradient Descent sử dụng toàn bộ dữ liệu cho mỗi lần cập nhật. Stochastic Gradient Descent sử dụng 1 dữ liệu để cập nhật tham số, còn Mini-Batch Gradient Descent sử dụng `Batch size` dữ liệu để cập nhật tham số trong 1 lần. Do đó
- **Batch size:** số lượng dữ liệu Mini-Batch Gradient Descent sử dụng trong 1 lần để cập nhật tham số
- **Epoch:** 1 epoch là một lần duyệt qua hết các dữ liệu trong tập huấn luyện
- **Iterations:** số lượng các Batch size mà mô hình phải duyệt trong 1 epoch.

Ví dụ tập huấn luyện có 32.000 dữ liệu. Nếu Batch size = 32 (mỗi lần cập nhật trọng số sẽ sử dụng 32 dữ liệu), khi đó Iterations =32.000/32=1000 để có thể duyệt qua hết các dữ liệu (hoàn thành 1 epoch). Các giá trị Batch size thường dùng là 32, 64, 128, 256... (2^n để việc tính toán được nhanh hơn). Tổng quát hơn thì đối với Stochastic Gradient Descent, Batch size = số dữ liệu trong tập huấn luyện, đối với Stochastic Gradient Descent, Batch size = 1.

**Lưu ý**
- Nếu tập huấn luyện lớn không thể load hết tất cả dữ liệu một lần để cập nhật có thể sử dụng Batch size nhỏ hơn
- Batch size càng lớn thì càng tận dụng được tính toán vectorization
- Batch size = 1 (Stochastic Gradient Descent) mô hình hội tụ nhanh hơn, tuy nhiên hàm mất mát dao động quanh mimimum chứ không hội tụ về nó được, bên cạnh đó cũng không tận dụng được tính toán vectorization.

**Kết luận**

Hi vọng thông qua bài viết này mọi người không còn nhầm lẫn giữa các khái niệm trên. Các bạn cho mình 1 like để ủng hộ mình.