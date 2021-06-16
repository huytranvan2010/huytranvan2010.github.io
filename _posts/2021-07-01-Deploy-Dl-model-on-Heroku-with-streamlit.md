---
layout: post
title: "Deploy Deel Learning Model on Heroku with Streamlit"
tags: [Deploy Model, Streamlit, Heroku]
comments: true
---

Bài trước chúng ta đã tìm hiểu sơ bộ về Streamlit. Trong bài này mình muốn chia sẻ cách deploy model (thực ra cái gì cũng được) lên Heroku với Streamlit thông qua Github.

Để deploy lên Heroku ngoài các file của project để chạy thông qua Streamlit như bình thường chúng ta cần tạo thêm 3 file:
* `Procfile` (procurement file) chứa thông tin `web: sh setup.sh && streamlit run [name_app].py`. Ở đây `[name_app].py` là file chạy của bạn. Trong này chứa các câu lệnh để thực thi khi mở app.
* `requirements.txt` chứa các packages dùng cho project, có thể tạo file này qua lệnh sau hoặc bạn cài packages nào thì ghi vào.
```python
pip freeze > requirements.txt
```
* `setup.sh` - chứa shell script dùng để thiết lập shell environment. Nội dùng của file `setup.sh` như sau.
```python
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

Tất nhiên rồi chúng ta cần tạo một repository chứa toàn bộ files của project để Heroku kết nối. Thực chất Heroku cung cấp 3 cách để có thể kết nối với project và ở đây mình chia sẻ cách dùng với Github.

**Chú ý:** Nếu dùng project của bạn dùng đến OpenCV thì khi deploy trên Heroku trong file `requirements.txt` nên để `opencv-python-headless` chứ không phải `opencv-contrib-python`, điều này giúp tránh lỗi `ImportError: libGL.so.1: cannot open shared object file: No such file or directory`.

Các bạn có thể xem thêm demo của mình tại [github-huytranvan2010](https://github.com/huytranvan2010/Deploy-DLmodel-with-Streamlit) hoặc tự tạo cho mình một project để chạy thử.

Thật tuyệt vời phải không nào, rất nhanh với vài câu lệnh chúng ta đã có thể chuyển đổi từ python script sang chạy với Streamlit và cũng với vài thao tác đơn giản chúng ta đã deploy được project trên Heroku để share với mọi người, đối tác.
##### Tài liệu tham khảo
1. https://www.geeksforgeeks.org/deploy-your-machine-learning-web-app-streamlit-on-heroku/
2. https://github.com/huytranvan2010/Deploy-DLmodel-with-Streamlit
