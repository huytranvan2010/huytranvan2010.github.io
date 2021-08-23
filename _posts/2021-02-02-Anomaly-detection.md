---
layout: post
mathjax: true
title: "Anomaly detection"
tags: [Autoencoder]
comments: true
---
Trong bài này chúng ta sẽ tìm hiểu về Anomaly detection với autoencoder.  Thông thường để detect anomalies có thể sử dụng các phương pháp như Isolation Forests, One-class SVMs, Elliptic Envelopes, Local Outlier Factor và đây là những phương pháp machine learning truyền thống. Nếu chúng ta sử dụng Deep Learning thì sao?

Trong 2 bài trước chúng ta đã tìm hiểu về autoencoder. Khi train autoencoder chúng ta thường tính mean squared error (MSE) dựa trên
- Input image
- Ảnh tái tạo được từ autoencoder

**Chú ý**: 
- Đối với bài toán denoising autoencoder input image là original image được thêm vào và khi tính loss function sẽ được tính dữa trên original image và ảnh được tái tạo từ encoder.
- Ngoài MSE cho cả ảnh còn có một số measure khác như SSIM...

Loss càng nhỏ chứng tỏ autoencoder hoạt động tốt với việc tái tạo ảnh. Giả sử chúng ta đã huấn luyện autoencoder trên bộ dữ liệu MNIST.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2014/06/mnist_sample.jpg" style="display:block; margin-left:auto; margin-right:auto">

Sau đó sử dụng pre-trained autoencoder để tái tạo lại ảnh đầu vào.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2020/03/autoencoder_anomaly_detection_digit.png" style="display:block; margin-left:auto; margin-right:auto">

Nhận thấy autoencoder làm việc rất tốt khi tái tạo ảnh các số. Khi chúng ta nhìn vào MSE giữa input image và reconstructed image thấy giá trị này nhỏ.

<img src="https://www.pyimagesearch.com/wp-content/uploads/2020/03/autoencoder_anomaly_detection_elephant.png" style="display:block; margin-left:auto; margin-right:auto">

Thử tưởng tượng xem nếu chúng ta dùng autoencoder đó để tái tạo một ảnh mới (ảnh con voi này chẳng hạn). Bởi vì autoencoder chưa bao giờ thấy con voi trước đó nên MSE ở đât sẽ rất cao. Khi MSE cao thì chúng ta có thể kết luận ảnh đưa vào là **outlier**. Điều này giống như autoencoder học **format rule** (quy luật định dạng) từ input data và khi có anomaly nó sẽ phát hiện ra ngay.

Nói chung có 2 bước để sử dụng autoencoder để phát hiện anomaly:
- Chúng ta đưa data vào autoencoder để train làm sao có thể tái tạo được input data với minimum error
- Đưa data mới vào autoencoder và kiểm tra error của reconstructed data so với data đầu vào. Nếu error lớn điều này có nghĩa rằng chúng ta đang có outlier.

## Tài liệu tham khảo
1. https://towardsdatascience.com/a-keras-based-autoencoder-for-anomaly-detection-in-sequences-75337eaed0e5
2. https://medium.com/analytics-vidhya/image-anomaly-detection-using-autoencoders-ae937c7fd2d1
3. https://www.pyimagesearch.com/2020/03/02/anomaly-detection-with-keras-tensorflow-and-deep-learning/
4. https://www.analyticsvidhya.com/blog/2021/05/anomaly-detection-using-autoencoders-a-walk-through-in-python/