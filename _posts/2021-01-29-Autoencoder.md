---
layout: post
mathjax: true
title: "Autoencoder"
tags: [Autoencoder]
comments: true
---

Bài này chúng ta sẽ cùng tìm hiểu về **autoencoder** bao gồm **convolutional autoencoder** được áp dụng như thế nào lên ảnh. Chúng ta cũng tìm hiểu về sự khác nhau giữa autoencoder và **Generative Adversarial Networks (GANs)**.

Autoencoder là một unsupervised learning algorithm. Nó thực hiện các công việc sau:
- Nhận input data
- Nén input data thành latent-space representation (vector nén và đặc trưng cho ảnh đầu vào)
- Tái tạo lại input data từ latent representation.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2020/02/keras_autoencoder_arch_flow.png" style="display:block; margin-left:auto; margin-right:auto">

Như hình trên nhận thấy autoencoder có 2 thành phần chính là:
- Encoder $E$, $s=E(x)$, trong đó $s$ là latent representation, $x$ là input data.
- Decoder $D$, $D(s)=o$, trong đó $o$ là output data

## Ứng dụng của Autoencoder
Autoencdoer thường được sử dụng cho:
- Dimensionality reduction (gần tương tự như PCV nhưng mạnh mã hơn)
- Denoising (loại bỏ noise và tiền xử lý ảnh để tăng độ chính xác cho bài toán OCR)
- Anomaly/outlier detection (phát hiện các điểm dữ liệu được gán nhãn sai hay điểm dữ liệu nằm ngoài phân phố dữ liệu điển hình)

<img src="https://www.pyimagesearch.com/wp-content/uploads/2020/02/keras_autoencoders_applications.png" style="display:block; margin-left:auto; margin-right:auto">

Ngoài ứng dụng trong Computer Vision, autoencoder còn được sử dụng trong NLP để tạo ra các word wmbeddings.

## Sự khác nhau giữa Autoencoder và GANs
Cả GANs và autoencoders đều là generative models (mô hình sinh), tuy nhiên autoencoder về bản chất là việc học một hàm **identity function** thông qua việc nén. 

Thông thường latent-space representation trong autoencoder sẽ có số dimensions nhỏ hơn nhiều so với original input data.

Ngược lại **GANs**:
- Chấp nhận input có dimension thấp
- Tạo ra high dimensional space từ nó
- Tạo ta final output, tuy nhiên final output này không được giống hẳn so với input data (chỗ này hiểu đơn giản là GANs cố tạo ra một fake image mà gần giống với original image nhất).

Trong bài này mình sẽ không trình bày cách implementation autoencoder. BÀi sau mình sẽ thực hiện điều đó với ảnh có noise. Để đơn giản trong bài sau nếu không muốn noise chúng ta có thể train autoencoder xem nó hoạt động như thế nào [Denoising autocoder](https://huytranvan2010.github.io/Denoising-autoencoder/).

## Tài liệu tham khảo
1. https://www.pyimagesearch.com/2020/02/17/autoencoders-with-keras-tensorflow-and-deep-learning/ 
