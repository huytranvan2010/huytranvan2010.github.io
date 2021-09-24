---
layout: post
title: "Face Recognition with LBPs and OpenCV"
tags: [Face Recognition]
comments: true
---
Trong bài trước chúng ta đã tìm hiểu về Face Recognition và một số thuật tán. Trong bài này chúng ta sẽ đi xây dựng hệ thống nhận diện khuôn mặt với Local Bianry Patterns (LBPs) và OpenCV.

### Local Binary Patterns (LBPs)
Thuật toán nhận diện khuôn mặt LBPs lần đầu tiên được giới thiệu vào năm 2004 bởi [Ahonen et al.](https://link.springer.com/chapter/10.1007/978-3-540-24670-1_36)

LBPs sẽ chia ảnh ta thành $7 \times 7$ grid cells. Đối với cell sẽ thực hiện tính **Local Binary Histogram**. Việc tính các histogram có thể đánh mất spatial information (thông tin về không gian), tuy nhiên việc tính histogram có thể mã hóa một số thông tin của mắt, mũi, miệng... Bằng việc chia ảnh thành cách grid cells chúng ta có thể đưa **locality** (tính cục bộ) vào trong final feature vector. Một số cells sẽ có trọng số lớn hơn đóng góp vào final feature (ví dụ các vùng góc mang ít thông tin nhận diện khuôn mặt hơn sơ với các vùng bên trong như mắt, mũi, miệng). Điều này cho phép chúng ta có một công cụ mạnh để phân biệt các features của khuôn mặt. Xem hình bên dưới để thấy rõ hơn.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/04/face_reco_lbps_weighting.png" style="display:block; margin-left:auto; margin-right:auto">

*Ảnh gốc được chia thành các grid cells và sơ đồ trọng số*

Ảnh có 49 grid cells, mỗi cell sẽ có trọng số riêng của nó khi tính feature chung của khuôn mặt:
* LBP histogram cho cell trắng (như mắt) có trọng số lớn hơn **4 lần** các cell khác. Đơn giản chỉ cần nhân 4 lần LBP histogram của cell trắng (có tính đến scaling và normalization.
* Cell xám nhạt (ligh gray cell) - vùng tai, miệng có trọng số 2
* Cell xám đậm (dark gray cell) - vùng má trong và trán có trọng số 1
* Các cell đen còn lại như mũi, vùng má ngoài... bị bỏ qua, không đóng góp gì vào feeature chung.

Những trọng số này được tìm ra bằng thực nghiệm bởi Ahonen et al. bằng cách hyperparameter tuning trên các tập dữ liệu.

Cuối cùng chúng ta nối các LBP histograms có trọng số từ 49 cells (có một số cell bị bỏ qua như nói ở trên) để hình thành nên final feature vector.

Quá trình nhận dạng khuôn mặt được thực hiện bởi kNN ($k=1$) sử dụng $\chi^{2}$ distance (**do chúng ta đang so sánh giữa các histogram nên dùng $\chi^{2}$ distance sẽ tốt hơn so với Euclidean distance**).

So với Eigenfaces thì LBPs chống nhiễu và cho kết quả tốt hơn do nó không dựa trên các raw pixels.
<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/03/what_is_face_reco_lbps_samples.png" style="display:block; margin-left:auto; margin-right:auto">

Nhận thấy face recognition với LBPs khá đơn giản:
* Trích xuất face ROI (dùng face detection)
* LBPs được trích xuất, có trọng số được nối lại
* kNN (k=1) với $\chi^{2}$ distance
* Đưa ra tên người với $\chi^{2}$ distance nhỏ nhất

Khi có khuôn mặt mới LBPs không cần retrain lại từ đầu như Eigenfaces, đây là lợi thế rất lớn.

Để thực hành chúng ta sẽ sử dụng bộ dữ liệu [Caltech faces](http://www.vision.caltech.edu/html-files/archive.html) với khoảng 450 ảnh (27 người). Mỗi ảnh được chụp dưới điều kiện ánh sáng, background, các biểu cảm khuôn mặt (facial expression) khác nhau.

Phần implementation các bạn có thể tham khảo tại đây [Github-huytranvan2010](https://github.com/huytranvan2010/Face-Recognition-with-LBPs-and-OpenCV)

### Kết luận
Chúng ta vừa thực hiện xong face recognition với LBPs. Quá trình training khá nhanh, tuy nhiên quá trình inference chậm do phải duyệt qua tất cả các ảnh trong bộ dữ liệu. Để cải thiện tốc độ chúng ta có thể phải thay đổi thuật toán nearest neighbor.

### Tài liệu tham khảo
1. https://www.pyimagesearch.com/2021/05/03/face-recognition-with-local-binary-patterns-lbps-and-opencv/
2. https://www.pyimagesearch.com/2018/02/26/face-detection-with-opencv-and-deep-learning/
3. https://github.com/huytranvan2010









