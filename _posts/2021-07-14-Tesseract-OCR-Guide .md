---
layout: post
title: "Nhận diện văn bản với Tesseract OCR"
tags: [OCR, OpenCV, Tesseract]
comments: true
---

Hôm nay chúng ta sẽ cùng tìm hiểu một công cụ nhận dạng văn bản Tesseract OCR. Tesseract OCR được bắt đầu phát triển từ những năm 80 của thế kì trước. Sau khi về tay Google nó tiếp tục được phát triển và phát hành dưới dạng open-source. Đây là cung cụ hữu ích giúp nhận dạng văn bản. Chúng ta sẽ xem cách cài đặt và chạy thử với Tesseract xem thế nào.

### Cài đặt 
Trên Ubuntu có thể dùng lệnh sau:
```python
sudo apt-get install tesseract-ocr
```
Cài xong kiểm tra xem đã cài được ok chưa thông qua lệnh
```python
tesseract -v
```
Khi ok nó sẽ hiện ra version của Tesseract và một số file.
```python
tesseract 4.1.1
 leptonica-1.79.0
  libgif 5.1.4 : libjpeg 8d (libjpeg-turbo 2.0.3) : libpng 1.6.37 : libtiff 4.1.0 : zlib 1.2.11 : libwebp 0.6.1 : libopenjp2 2.3.1
 Found AVX2
 Found AVX
 Found FMA
 Found SSE
 Found libarchive 3.4.0 zlib/1.2.11 liblzma/5.2.4 bz2lib/1.0.8 liblz4/1.9.2 libzstd/1.4.4
```
Nếu không có lẽ bạn phải cài lại từ đầu, xem nguyên nhân gây ra lỗi. 

Sau khi cài đặt xong, do nó không tự cài đặt ngôn ngữ tiếng Việt để nhận dạng (nếu window khi cài sẽ có tùy chọn). Ở trên Ubuntu chúng ta sẽ phải tải thêm về để có thể nhận dạng được tiếng Việt. Vào [link sau](https://github.com/tesseract-ocr/tessdata) chọn lấy file `vie.traineddata` và tải về máy. Trên máy mình nằm ở `/usr/share/tesseract-ocr/4.00/tessdata` (mình vào Computer tìm **tessdata**). Dungf `sudo` mới di chuyển file được.
```
huytranvan2010@hammiu:/usr/share/tesseract-ocr/4.00/tessdata$ sudo mv /home/huytranvan2010/Downloads/vie.traineddata ./
```

Chúng ta sẽ tạo môi trường riêng để làm việc.

```python
conda create -n myenv python=3.8
```

Chú ý **Tesseract** liên hệ với Python qua thư viện **pytesseract**, do đó chúng ta cần cài đặt nó (cài luôn OpenCV và Pillow):

```python
pip install pytesseract
pip install pillow
pip install opencv-contrib-python
```

Chạy thử với ảnh `image2.png` với blur
```python
python tesseract_ocr.py --image image2.png
```

Ở trong hàm chuyển từ ảnh sang string có thể set một số thông số config. Đọc thêm [link này](http://manpages.ubuntu.com/manpages/bionic/man1/tesseract.1.html) để hiểu rõ hơn.
```python
# Hướng dẫn chạy
# python tesseract_ocr.py --image image1.png
from PIL import Image
import pytesseract
import argparse
import cv2
import os

""" Ảnh nên được xử lý trước như khử nhiễu, chuyển về đen trắng... sẽ cho kết quả tốt hơn đới với Tesseract """
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="kind of image pre-processing")
args = vars(ap.parse_args())

# Đọc ảnh và convert về grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# Kiểm tra xem có chuyển về ảnh đen trắng 
if args["preprocess"] == "thresh":
	_, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)		# trả về 2 tham số threshold và image
 
# Có blur không
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)	# tham số thứ hai là kernel size, giảm salt và pepper noise

# Lưu ảnh trong ổ cứng như file tạm để có thể apply OCR
filename = "{}.png".format(os.getpid())		# os.getpid() method in Python is used to get the process ID of the current process, trả về 1 số nguyên
cv2.imwrite(filename, gray)		# ghi ảnh gray vào filename

# Load ảnh và apply nhận dạng bằng Tesseract OCR
text = pytesseract.image_to_string(Image.open(filename), lang='vie')	# có nhiều ngông ngữ thì trong lang các ngôn ngữ cách nhau bằng dấu  +
""" Cần chú ý các chế độ nhận diện được điều chỉnh bằng config """

# Thực hiện chuyển đổi xong thì xóa ảnh tạm
os.remove(filename)

# In dòng chữ nhận dạng được
print(text)
 
# Hiển thị ảnh ban đầu, ảnh đã được pre-processing
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
```

Cho kết quả như sau
```
Tesseract VVill
Faill With Noisy
Dackgrounds
```
Khi sử dụng `thresh` lại cho kết quả như sau:
```
Tesseract VVill
Faill With Noisy
Dackgrounds
```
Nhận thấy cùng một ảnh đầu vào nhưng với các pre-processing techniques khác nhau thì kết quả cũng khác nhau. Tuy thuộc vào từng trường hợp mà có lựa chọn kỹ thuật tiền xử cho phù hợp (có thể kết hợp lại với nhau).

### Lấy các box xung quanh kí tự.
```python
""" Lấy bounding boxes xung quanh các kí tự """
import cv2
import pytesseract

img = cv2.imread('image1.png')

h, w, c = img.shape

boxes = pytesseract.image_to_boxes(img) 
""" 
    Hàm trên trả về string gồm các dòng, một số dòng có định dạng như sau
    O 199 19 230 51 0
    C 232 19 261 51 0
    R 265 20 295 50 0
"""
print(type(boxes))
print(boxes)

for b in boxes.splitlines():
    b = b.split(' ')    # loại bỏ các kí tự khoảng trắng ở đầu và cuối
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
```
### Lấy các box xung quanh các từ

```python
# python python get_bboxes_word.py
import pytesseract
from pytesseract import Output
import cv2

img = cv2.imread('image1.png')

d = pytesseract.image_to_data(img, output_type=Output.DICT)     # ở đây để output_type=Output.DICT để trả về dạng dictionary

# in ra để biết các keys trong dict là gì
print(d)

# số bounding boxes trả về
n_boxes = len(d['level'])

# duyệt qua các bounding boxes đó
for i in range(n_boxes):
    # lấy x, y, w, h cho từng bounding box
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # vẽ

cv2.imshow('img', img)
cv2.waitKey(0)
```
Ví dụ trên trả về dictionary d có dạng
```python
{'level': [1, 2, 3, 4, 5, 5, 4, 5, 5, 4, 5, 5], 'page_num': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'block_num': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'par_num': [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'line_num': [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], 'word_num': [0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 1, 2], 'left': [0, 24, 24, 51, 51, 161, 106, 106, 150, 24, 24, 199], 'top': [0, 19, 19, 19, 19, 19, 67, 68, 67, 108, 109, 108], 'width': [318, 271, 271, 216, 99, 106, 105, 33, 61, 271, 164, 96], 'height': [159, 121, 121, 41, 41, 41, 28, 27, 28, 32, 31, 32], 'conf': ['-1', '-1', '-1', '-1', 95, 96, '-1', 96, 96, '-1', 96, 96], 'text': ['', '', '', '', 'Noisy', 'image', '', 'to', 'test', '', 'Tesseract', 'OCR']}
```

Các bạn xem thêm tại [github-huytranvan2010](https://github.com/huytranvan2010/Tesseract-Guide).

Như vậy chúng ta đã tìm hiểu cách cài đặt cũng như chạy Tesseract với python. Muốn đầu ra cho kết quả tốt thì ảnh cần rõ nét, có độ phân giải cao. Ảnh trước khi đưa vào Tesseract cần được tiền xử lý để có kết quả tốt nhất.

### Tài liệu tham khảo
1. https://newbedev.com/getting-the-bounding-box-of-the-recognized-words-using-python-tesseract
2. http://manpages.ubuntu.com/manpages/bionic/man1/tesseract.1.html
3. https://tesseract-ocr.github.io/tessdoc/FAQ.html
4. https://github.com/huytranvan2010/Tesseract-Guide
