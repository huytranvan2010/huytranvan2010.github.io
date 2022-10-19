---
layout: post
title: "Tạo chương trình đơn giản với PyQt và Qt Designer"
tags: [Python tutorial, GUI Application]
comments: true
---

## Hướng dẫn cài đặt pyqt5 và Qtdesigner trên Ubuntu

Cài đặt pyqt5:
```python
sudo apt-get install python3-pyqt5
```
Xem thêm ở link sau: https://pythonbasics.org/install-pyqt/

Cài đặt designer:
```python
sudo apt-get install qttools5-dev-tools
sudo apt-get install qttools5-dev
```
Xem thêm ở link sau: https://pythonbasics.org/qt-designer-python/ 

Hoặc có thể tạo môi trưởng ảo chạy trên đó:
```python
conda create -n myenv python=3.7
```
Sau đó cài đặt PyQt5
```python
pip install pyqt5
```
Ở đây vẫn cài QtDesigner trên máy luôn chứ không cài trong môi trường ảo vì lần sau mình còn dùng.

## Export file .ui sang .py
```python
pyuic5 /home/linux/helloworld.ui -o helloworld.py
```
Tham số thứ 2 là tên file (ở đây ghi cả path). Nếu chuyển dạng này:
```python
pyuic5 -x /home/linux/helloworld.ui -o helloworld.py
```
Nó sẽ tạo ra kiểu hàm main để chạy trong file mới tạo ra luôn. Thông thường ta sẽ sử dụng file giao diện tạo ta trong một file khác nên hay dùng cách thứ nhất.

## Sườn bài
Dưới đây là sườn của file main.py, cứ áp vào là chạy để kiểm tra xem giao diện ok không, sau đó mình đi thay đổi functionality.
```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator import Ui_MainWindow    # chính là file chuyển từ .ui

class MainWindow:   # tạo class nên thêm dấu ngoặc (), nếu super class có thể không cần
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)    # trong này truyền list tham số
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())    # trong python 3 ko cần phải exec_()
    
```

## Hướng dẫn đóng gói thành file .exe
Có một số cách đóng gói chương trình Python như pyinstaller, py2exe (khá cũ) hay cx_Freeze (nhẹ hơn nhưng không đóng gói được một số thư viện thứ 3). Ở đây mình xin giới thiệu cách đóng gói theo pyinstaller (cái này được được dùng khá phổ biến).

Cài đặt thư viện này trước khi đóng gói (mình vẫn cài trong môi trường ảo)
```python
pip install pyinstaller
```
Nếu không cài thư viện kia, khi đóng gói vẫn ra chương trình nhưng không chạy được mà lại không có thông báo gì.

Cuối cùng chúng ta đi đóng gói.
```python
pyinstaller main.py
```
Khi đó nó sẽ tạo ra thư mục `build`, `dist` và file `*.spec`.

**Một số tùy chỉnh**
```python
pyinstaller main.py --name new_name
```
Tham số `--name` giúp chúng ta thay đổi tên tệp thực thi. 

```python
pyinstaller main.py  --onefile
```
Tham số `--onefile` chúng ta ta nhóm dự án thành tệp duy nhất. Lúc này trong thư mục `dist` sẽ chỉ có một tập tin này thay vì nhiều file như ban đầu.

```python
pyinstaller main.py  -w
```
Tham số `-w` giúp tránh tự động mở cửa sổ bảng điều khiển. Điều này chỉ hữu ích khi đang xây dựng ứng dụng hỗ trợ GUI. Điều này giúp ẩn chi tiết việc triển khai, người dùng không biết được các thiết bị đầu cuối. 

Mình hay dùng
```python
pyinstaller main.py --onefile -w
```
Trên đây mình đã giới thiệu cách cài đặt cũng như tạo ứng dụng đơn giản với PyQt và QT Designer. Các bạn tham khảo thêm source code ở [github-huytranvan2010](https://github.com/huytranvan2010/PyQt-QtDesigner-Beginner).

## Tài liệu tham khảo
1. https://v1study.com/python-bai-hoc-core-su-dung-pyinstaller-de-de-dang-phan-phoi-cac-ung-dung-python.html
2. https://laptrinhcanban.com/python/nhap-mon-lap-trinh-python/dong-goi-chuong-trinh-python/dong-goi-chuong-trinh-python-pyinstaller/
3. https://www.youtube.com/watch?v=UFwID9-nUEo&list=PLGf7gEjelw-kA3DT8o-tHusqviFelrcG5&index=7










