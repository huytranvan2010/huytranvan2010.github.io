---
layout: post
mathjax: true
title: "Image pyramid with Python"
tags: [OpenCV, Object Detection, Scikit image]
comments: true
---

## 1. Mở đầu
**Image pyramid** là cách biểu diễn hình ảnh với nhiều tỉ lệ khác nhau. Sử dụng image pyramid cho phép chúng ta có thể tìm thấy vật thể với nhiều kích thước khác nhau trong ảnh. Kết hợp với sliding window có thể tìm được vật thể ở các vị trí khác nhau.

<img src="https://pyimagesearch.com/wp-content/uploads/2015/03/pyramid_example.png" style="display:block; margin-left:auto; margin-right:auto">

Ở đáy là ảnh với kích thước ban đầu. Ở mỗi layer tiếp theo là ảnh đã được resize lại (subsample) có kết hợp với làm mở (tùy chon, ví dụ Gaussian blurring). Khi nào kích thước của ảnh thỏa mãn điều kiện thì không giảm nữa. Trong bài này sẽ giới thiệu 2 phương pháp để lấy image pyramid:
- Dùng OpenCV
- Dùng Scikit image

## 2. Thực hiện
Viết một hàm riêng khi lấy image pyramid với OpenCV.

```python
def pyramid(image, scale=1.5, minSize=(30, 30)):    # minSize là (width, height)
    """ Tạo image pyramid bằng OpenCV """
    # xuất ra ảnh gốc
    yield image     # dùng yield xuất xong ảnh gốc khi gọi đến nó tiếp nó sẽ chạy xuống dưới

    while True:
        # tính size mới và resize ảnh
        w = int(image.shape[1] / scale)     # thay đổi width này
        image = imutils.resize(image, width=w)

        # nếu kích thước ảnh nhỏ hơn minimum size yêu cầu (theo bất cứ chiều nào) thì dừng, thoát luôn
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break 

        # xuất ra ảnh tiếp theo với size nhỏ hơn
        yield image
```

Bên dưới sẽ gộp luôn cả 2 phương pháp, bên Scikit image có áp dụng Gaussian blurring.
```python
# Cách chạy
# python image_pyramid.py --image images/dog.jpg
import cv2
from skimage.transform import pyramid_gaussian
from hammiu import pyramid
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
ap.add_argument("-s", "--scale", type=float, default=2, help="scale factor size")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Cách 1: Tạo image pyramid sử dụng OpenCV
for (i, resized) in enumerate(pyramid(image, scale=args["scale"])):
    cv2.imshow("Layer {}".format(i + 1), resized)
    cv2.waitKey(0)

# Cách 2: Tạo image pyramid sử dụng scikit image
# Chú ý phần này ngoài resize còn áp dụng thêm Gaussian smoothiing
for (i, resized) in enumerate(pyramid_gaussian(image, downscale=2, multichannel=True)):
    # nếu chiều nào của ảnh nhỏ hơn min thì thoát khỏi vòng lặp
    if resized.shape[0] < 30 or resized.shape[1] < 30:
        break 

    # hiển thị các ảnh đã resize
    cv2.imshow("Layer {}".format(i + 1),  resized)
    cv2.waitKey(0)
```
## 3. Kết luận
Như vậy chúng ta đã cùng tìm hiểu về `image pyramid`, bài tiếp theo sẽ tìm hiểu về sliding window - một cung cụ hay dùng chung với image pyramide trong computer vision.

## 4. Tài liệu tham khảo
1. https://www.pyimagesearch.com/2015/03/16/image-pyramids-with-python-and-opencv/
