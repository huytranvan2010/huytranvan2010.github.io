---
layout: post
mathjax: true
title: "Transfer Learning"
tags: [Transfer learning, Feature Extractor]
comments: true
---

Transfer learning - dựa vào việc đã học trên một bộ dữ liệu lớn ta có thể áp dụng sang cho các bài toán khác (sử dụng pre-trained model).

Transfer learning bao gồm 2 loại: Fine tuning và feature extractor

Fine tuning được thực hiện thông qua các bước sau:
1. Tiền huấn luyện một mô hình mạng nơ-ron, tức là là mô hình gốc, trên tập dữ liệu gốc (chẳng hạn tập dữ liệu ImageNet).
2. Tạo mô hình mạng nơ-ron mới gọi là mô hình mục tiêu. Mô hình này sao chép tất cả các thiết kế cũng như các tham số của mô hình gốc, ngoại trừ tầng đầu ra. Ta giả định rằng các tham số mô hình chứa tri thức đã học từ tập dữ liệu gốc và tri thức này sẽ áp dụng tương tự đối với tập dữ liệu mục tiêu. Ta cũng giả định là tầng đầu ra của mô hình gốc có liên hệ mật thiết với các nhãn của tập dữ liệu gốc và do đó không được sử dụng trong mô hình mục tiêu.
3. Thêm vào một tầng đầu ra cho mô hình mục tiêu mà kích thước của nó là số lớp của dữ liệu mục tiêu, và khởi tạo ngẫu nhiên các tham số mô hình của tầng này.
4. Huấn luyện mô hình mục tiêu trên tập dữ liệu mục tiêu, chẳng hạn như tập dữ liệu ghế. Chúng ta sẽ huấn luyện tầng đầu ra từ đầu, trong khi các tham số của tất cả các tầng còn lại được tinh chỉnh từ các tham số của mô hình gốc.


- Học truyền tải chuyển kiến thức học được từ tập dữ liệu gốc sang tập dữ liệu mục tiêu. Tinh chỉnh là một kỹ thuật phổ biến trong học truyền tải.
- Mô hình mục tiêu tái tạo toàn bộ thiết kế mô hình và các tham số của mô hình gốc, ngoại trừ tầng đầu ra, và tinh chỉnh các tham số này dựa vào tập dữ liệu mục tiêu. Ngược lại, tầng đầu ra của mô hình mục tiêu cần được huấn luyện lại từ đầu.
- Thông thường việc tinh chỉnh các tham số sử dụng tốc độ học nhỏ, trong khi việc huấn luyện lại tầng đầu ra từ đầu có thể sử dụng tốc độ học lớn hơn.
https://d2l.aivivn.com/chapter_computer-vision/fine-tuning_vn.html
