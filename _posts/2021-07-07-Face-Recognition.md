---
layout: post
title: "Face Recognition là gì?"
tags: [Face Recognition]
comments: true
---

Face recognition (nhận diện khuôn mặt) là quá trình lấy một bức ảnh chứa mặt người và xác định ai trong đó.

Ban đầu hệ thống nhận diện khuôn mặt dựa trên **facial landmarks** từ ảnh như vị trí, kích thước của mắt, mũi, miệng, má. Tuy nhiên độ chính xác của phương pháp này không cao. Sau này các kỹ thuật toán ML phát triển các đặc trưng được tách ra từ khuôn mặt, các model được huấn luyện để phân loại từ đó xác định khuôn mặt tương ứng với ai. Gần đây nhất các kỹ thuật Deep Learning được sử dụng để nhận dạng khuôn mặt như model FaceNet, OpenFace dựa trên kiến trúc Siamese Network cho kết quả rất tốt.

### Nhận diện khuôn mặt khác phát hiện khuôn mặt
Phát hiện khuôn mặt là xác định vị trí của khuôn mặt trong hình ảnh, video.
Nhận diện khuôn mặt là vừa xác định vị trí khuôn mặt vừa xác định đó là ai. Bài toàn này phức tạp hơn và bao trùm phát hiện khuôn mặt (face detection).
Quá trình nhận diện khuôn mặt bao gồm 2 bước:
* Face detection: sử dụng các phương pháp như **Harr cascades**, **HOG + Linear SVM**, deep learning (MTCNN...)
* Lấy khuôn mặt phát hiện được rồi xác định ai trong đó: ví dụ sử dụng **model FaceNet dựa trên Siamese Network, Local Bianry Patterns (LBPs), Eigenfaces...**

<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/03/what_is_face_reco_steps.png" style="display:block; margin-left:auto; margin-right:auto">

Thực chất có thể gộp 2 bước làm một tuy nhiên làm như vậy ảnh sẽ có nhiều nhiễu (background) ảnh hưởng đến độ chính xác.

Chúng ta sẽ tìm hiểu qua một số thuật toán nhận diện khuôn mặt.

### Eigenfaces
<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/03/what_is_face_reco_eigenfaces_combo.png" style="display:block; margin-left:auto; margin-right:auto">

Thuật toán Eigenfaces sử dụng PCA (principal component analysis) để xây dựng low-dimensional representation của ảnh khuôn mặt.

Quá trình này liên quan đến thu thập bộ dữ liệu các khuôn mặt với nhiều ảnh khuôn mặt đối với mỗi người cần xác định. Với tập dữ liệu các khuôn mặt, giả sử có cùng chiều dài, rộng và lý tưởng với mặt và cấu trúc mặt được căn chỉnh ở cùng toạn độ, chúng ta sẽ áp dụng **eigencalue decomposition** lên tập dữ liệu đó, giữ lại các eigenvectors tương ứng với các eigenvalues lớn nhất.

Có được những eigenvectors, khuôn mặt có thể được biểu diễn bằng tổ hợp tuyến tính của eigenfaces.

**Face identification** được thực hiện dựa trên tính Eucidean distance** giữa eigenface representations (coi như bài toán kNN). 

### LBPs for face recognition

Eigenfaces algorithm dựa trên PCA để xây dựng low-dimensional representation của ảnh khuôn mặt, Local Binary Patterns (LBPs) lại dựa trên feature extraction.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/03/what_is_face_reco_lbps_samples.png" style="display:block; margin-left:auto; margin-right:auto">

LBPs sẽ chia ảnh ta thành $7 \times 7$ grid cells. Bằng việc chia ảnh thành cách grid cells chúng ta có thể đưa **locality** (tính cục bộ) vào trong final feature vector. Một số cells sẽ có trọng số lớn hơn đóng góp vào final feature (ví dụ các vùng góc mang ít thông tin nhận diện khuôn mặt hơn sơ với các vùng bên trong như mắt, mũi, miệng). Xem hình bên dưới để thấy rõ hơn.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2021/03/what_is_face_reco_lbps_cells.png" style="display:block; margin-left:auto; margin-right:auto">

Cuối cùng chúng ta nối các LBP histograms có trọng số từ 49 cells để hình thành nên final feature vector.

Quá trình nhận dạng khuôn mặt được thực hiện bởi kNN sử dụng $\chi^{2}$ distance (**do chúng ta đang so sánh giwuax các histogram nên dùng $\chi^{2}$ distance sẽ tốt hơn so với Euclidean distance**).

So với Eigenfaces thì LBPs chống nhiễu và cho kết quả tốt hơn do nó không dựa trên các raw pixels.

### Deep learning-based face recogtion
<img src="https://miro.medium.com/max/651/1*hWBNCVbG-ngJ2aAiqg4Nzw.png" style="display:block; margin-left:auto; margin-right:auto">

Model ở đây dựa trên Siamese network, triplet loss. Trong các bài sau mình sẽ nói rõ hơn về nhận diện khuôn mặt với Deep learning.

Kết thúc được rồi, tuy nhiên mình muốn nhấn mạnh thêm rằng thường trước khi áp dụng Eigenface, LBPs hay Deep learning Model chúng ta cần thực hiện Face Detection trước đã để trích xuất ROI face, sau đó mới đưa ROI face vào các thuật toán nói ở trên.

### Kết luận
Như vậy chúng ta đã cùng tìm hiểu về khá niệm nhận diện khuôn mặt cũng như một số thuật toán chính để thực hiện. Cùng chờ đón các bài tiếp theo của mình nhé.







