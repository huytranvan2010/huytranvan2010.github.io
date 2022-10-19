---
layout: post
mathjax: true
title: "Sliding windows for Object Detection"
tags: [Object detection, OpenCV]
comments: true
---

# 1. Mở đầu
Trong Computer Vision, cửa sổ trượt (sliding window) là các hình chữ nhật với kích thước cố định trượt trên toàn bộ bức ảnh từ trái qua phải, từ trên xuống dưới.
Đối với mỗi cửa sổ trượt đó chúng ta thường áp dụng `image classifier` để xác định trong cửa sổ có chứa vật thể ta quan tậm hay không.

![image](https://pyimagesearch.com/wp-content/uploads/2014/10/sliding_window_example.gif)

Khi kết hợp `image pyramid` với sliding window chúng ta có thể tạo ra bộ phân loại ảnh để có thể nhận biết vật thể với nhiều kích thước và vị trí khác nhau trong ảnh.

# 2. Thực hiện 

Cùng code một chút xem như thế nào:
```python
def pyramid(image, scale=1.5, minSize=(30, 30)):    # minSize là (width, height)
    # xuất ra ảnh gốc
    yield image 

    while True:
        # tính size mới và resize ảnh
        w = int(image.shape[1] / scale)     # thay đổi width này
        image = imutils.resize(image, width=w)

        # nếu kích thước ảnh nhỏ hơn minimum size yêu cầu (theo bất cứ chiều nào) thì dừng, thoát luôn
        if image.shape[0] < minSize[1] or image.shape[1] > minSize[0]:
            break 

        # xuất ra ảnh tiếp theo với size nhỏ hơn
        yield image

def sliding_window(image, stepSize, windowSize):    # windowSize = (width, height)
    # trượt các cửa sổ theo ảnh
    for y in range(0, image.shape[0], stepSize):    # duyệt theo hàng -  height
        for x in range(0, image.shape[1], stepSize):    # duyệt theo cột - width
            # xuất ra từng cửa sổ
            yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])   # có cả vị trí cho window và sliding window
```

Bài này sẽ tập trung nói về sliding window nên sẽ tạm bỏ qua phần image pyramid. Hàm `sliding_window` cần 3 tham số đầu vào là `image, stepSize, windowSize`.
- `stepSize` - số pixels của sổ trượt sẽ nhảy qua mỗi lần. `stepSize` hay để 4-8. Nếu `stepSize` nhỏ quá, có nhiều sliding windows được tạo ra tính toán sẽ tăng, nếu quá lớn nhiều khi không xác định được toàn bộ vật thể mà chỉ một bộ phần nào đó. Tùy bài toán mà có sự điều chỉnh phù hợp.
- `windowSize` - (width, height) kích thước mong đợi của sliding window được trích xuất từ ảnh ban đầu.

**Chú ý:** 
- Ở phần trên có sử dụng `yield` chức năng tương tự `return` trong hàm. Tuy nhiên khi sử dụng `yield` ta đang muốn trả về một `generator`, mỗi khi gọi nó sẽ sinh ra giá trị, lưu lại trạng thái đó để tiếp tục cho lần sau.
- Khi `width` và `height` của ảnh không chia hết cho `stepSize` thì hàm `sliding_window` vẫn trả về phần dư (bên phải và bên dưới)

Phần tiếp theo sẽ đi tạo ra các sliding window và in ảnh ra với các cửa sổ trượt trên ảnh.

```python
image = cv2.imread(args["image"])
# định nghĩa windowSize
(winW, winH) = (128, 128)

# Duyệt qua image pyramid
for resized in pyramid(image, scale=1.5):
    # Duyệt qua các sliding windows cho mỗi layer của image pyramid
    for (x, y, window) in sliding_window(image, stepSize=32, windowSize=(winW, winH)):
        # Nếu như window không thỏa mãn kích thước mong đợi của chúng ta thì bỏ qua
        if window.shape[0] != winH or window.shape[1] != winW:
            continue    # tiếp tục vòng lặp for
            # thực chất phần này sẽ dành cho việc khác
        
        clone = resized.copy()
        cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
        cv2.imshow("window", clone)
        cv2.waitKey(1)
        time.sleep(0.025)
```
# 3. Kết luận
Sliding window cùng với image pyramid là những công cụ rất mạnh trong thời gian đầu để phát hiện vật thể. Hiện nay do số lượng sliding tạo ra nhiều, việc tính toán lớn nên nó dần được thay thế bằng những công cụ mạnh mẽ hơn như họ R-CNN hay YOLO. Tuy nhiên cũng rất đáng để tìm hiểu những công cụ này.

# 4. Tài liệu tham khảo
1. https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
2. https://www.pyimagesearch.com/2015/03/23/sliding-windows-for-object-detection-with-python-and-opencv/
