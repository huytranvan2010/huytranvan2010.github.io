---
layout: post
title: "Lập trình hướng đối tượng với Python - Phần 2"
tags: [Python tutorial]
comments: true
---

Trong phần trước chúng ta đã tìm hiểu về constructor, attribute, methods, tính đóng gói, tính kế thừa. Bài này sẽ đề cập đến một số chính còn lại của lập trình hướng đối tượng trong Python.

### 6. Polymorphism (tính đa hình)
Hai hay nhiều lớp có phương thức giống nhau (tên gọi) nhưng có thể thực thi khác nhau.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meomeo"

mydog = Dog("Tuni")
mycat = Cat("Hani")

print(mydog.speak())   
print(mycat.speak())
```
Nhận thấy cả 2 object `mydog` và `mycat` đều có phương thức `speak()`, tuy nhiên cách thực thi của chúng là khác nhau.

### 7. Property
Property là một thành phần đặc biệt trong class Python cho phép truy xuất và kiểm soát truy xuất *một attribute cụ thể*.

Đầu tiên hãy làm quen với hai khái niệm **getters** và **setters**.
* **Getters** - các method được dùng trong OOP để giúp truy cập các *private attribute* từ class
* **Setters** - các method sử dụng trong OOP giúp cài đặt giá trị cho các *private attribute* trong class.

Cùng xem ví dụ sau:
```python
class Person:

    def __init__(self, fname, lname, age):
        # private attribute __a
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    # getter method để truy cập giá trị của attribute __age
    def get_age(self):
        return self.__age
    # setter method để thay đổi giá trị của attribute __age
    def set_age(self, age):
        if age > 0 :
            self.__age = age

    def get_fname(self):
        return self.__fname

    def set_fname(self, fname):
        if fname.isalpha():
            self.__fname = fname
    
    def get_lname(self):
        return self.__lname

    def set_lname(self, lname):
        if lname.isalpha():
            self.__lname = lname
        
toi = Person("Huy", "Tran", 30)
print(toi.get_age())

toi.set_age(25)
print(toi.get_age())
    
```
Đầu ra sẽ nhận được
```python
30
25
```
Attribute cần kiểm soát dữ liệu sẽ đặt mức truy cập là private. Ứng với mỗi biến private sẽ xây dựng 2 phương thức getter và setter để xuất và nhập dữ liệu. Tuy nhiên có thể nhận thấy code chứa nhiều lời gọi hàm khiến khó đọc. Do đó ta có thể điều chỉnh như sau nhờ vào **property**.

```python
class Person:

    def __init__(self, fname: str = '', lname: str = '', age: int = 23):
        # private attribute __a
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    # getter method để truy cập giá trị của attribute __age
    def get_age(self):
        return self.__age
    # setter method để thay đổi giá trị của attribute __age
    def set_age(self, age):
        if age > 0 :
            self.__age = age

    def get_fname(self):
        return self.__fname

    def set_fname(self, fname):
        if fname.isalpha():
            self.__fname = fname
    
    def get_lname(self):
        return self.__lname

    def set_lname(self, lname):
        if lname.isalpha():
            self.__lname = lname
    
    def get_name(self):
        return self.__fname + self.__lname
        
    first_name = property(get_fname, set_fname)
    last_name = property(get_lname, set_lname)
    full_name = property(get_name)
    age = property(get_age, set_age)

toi = Person()
toi.first_name = "Huy"
toi.last_name = "Tran"
toi.age = 30

print(toi.full_name, toi.age)
```
Đâu ra ta nhận được
```python
HuyTran 30
```

Ở trên chúng ta đã nhóm các lệnh getter/setter vào một nhóm như này:
```python
first_name = property(get_fname, set_fname)
last_name = property(get_lname, set_lname)
full_name = property(get_name)
age = property(get_age, set_age)
```
Lúc này ta có thể viết các lệnh sau:
```python
toi = Person()
toi.first_name = "Huy"
toi.last_name = "Tran"
toi.age = 30
print(toi.full_name, toi.age)
```
Lúc này `first_name`, `last_name`, `age` trở thành các **property** trong class Python. Trong class Python property là một dạng giao tiếp tới các instance attribute để thực hiện xuất/nhập dữ liệu qua bộ getter/setter. Mỗi property cung cấp cách xuất dữ liệu thông thường và cách nhập dữ liệu thông qua phép gán (ở trên chúng ta có gán first_name, last_name và age). Khi thực hiện property hoàn toàn che đi lời gọi hàm getter/setter.

Như vậy khi sử dụng property `first_name` bạn có thể viết tự nhiên `toi.first_name` giống như một biến thành viên thông thường để truy xuất dữ liệu từ biến private `__fname`. Phép gán giá trị cho `first_name` sẽ chuyển thành lời gọi hàm `set_fname`.

Ở trên trong hàm property() chúng ta chỉ để 1 hoặc 2 tham số. Đầy đủ thì hàm property() nhận vào 3 tham số tương ứng với tên hàm **getter**, **setter** và **deleter**. Hàm **deleter** ít được sử dụng, nó tương đương với `del` trong Python. Nếu thiếu setter và deleter, property sẽ trở thành read-only (chỉ đọc) như bên trên đối với `fullname`.

Ngoài cách sử dụng hàm `property()` như trên chúng ta có thể dụng decorator **@property** để có tác dụng tương tự.

```python
class Person:

    def __init__(self, fname: str = '', lname: str = '', age: int = 23):
        # private attribute __a
        self.__fname = fname
        self.__lname = lname
        self.__age = age

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age > 0 :
            self.__age = age

    @property
    def first_name(self):
        return self.__fname
    @first_name.setter
    def first_name(self, fname):
        if fname.isalpha():
            self.__fname = fname
    
    @property
    def last_name(self):
        return self.__lname
    @last_name.setter
    def last_name(self, lname):
        if lname.isalpha():
            self.__lname = lname
    
    @property
    def full_name(self):
        return self.__fname + self.__lname
        

toi = Person()
toi.first_name = "Huy"
toi.last_name = "Tran"
toi.age = 30

print(toi.full_name, toi.age)
```
Đâu ra sẽ nhận được
```python
HuyTran 30
```

Chúng ta cùng để ý khối code sau:
```python
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age > 0 :
            self.__age = age
```
Một số điểm cần lưu ý:
* Getter, setter (cả deleter) đều sử dụng chung một tên, đó cũng là tên của property để gọi. Ví dụ ở trên có tạo `age` property để truy xuất cho attribute `__age` thì cần tạo getter, setter và deletre với cùng một tên `age`.
* Phương thức getter cần đánh dấu với **@property**
* Phương thức setter cần đánh dấu với **@tên property.setter**, phương thức deleter cần đánh dấu với **@tên property.deleter**. Ví dụ với `age` property thì setter phải đánh dấu **@age.setter**, deleter phải đánh dấu **@age.deleter**.

### 8. Magic method (dunder method)
Magic method hay dunder method là các method có tiền tố và hậu tố là 2 dấu gạch dưới `__`. Một số ví dụ của dunder method như `__init__`, `__add__`, `__len__`, `__repr__` etc.

```python
mylist = [1, 2, 3]
print(len(mylist))

class Sample:
    pass

mysample = Sample()
print("Trả về vị trí lưu object trong memory: ", mysample)
# print("Bao loi: ", len(mysample))
```
Nhận thấy việc dùng `len` đối với object bị báo lỗi. Nếu chúng ta muốn sử dụng một số hàm đó cho object thì phải làm thế nào?

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book = Book("Python bok", "Huy", 212)

print(book)     # khi in ra thông báo có object in memory

""" Nên khi khi gọi hàm print() nó sẽ in ra string thể hiện book 
Chuyển book về string là biết ngay """
print(str(book))

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"     # hoặc để string thông thường

    # tương tự làm với len
    def __len__(self):
        return self.pages

    # thêm del (xóa object)
    def __del__(self):
        print("The book has been deleted")  # thông báo khi xóa

book = Book("Python book", "Huy", 212)
print(book)    # kết quả đã khác rồi

print(len(book))

del book  # xóa object
# print(book)     # đã xóa rồi không còn nữa
```

Ở bên trên chúng ta đã định nghĩa một số magic method (dunder) như `__str__`, `__len__`, `__del__`. Lúc này chúng ta có thể in thông tin của object... (nói chung tùy theo mình điều chỉnh).

### Nạp chồng toán tử

Toán tử Python làm việc bằng các hàm được dựng sẵn, nhưng một toán tử có thể được sử dụng để thực hiện nhiều hoạt động khác nhau. Ví dụ với toán tử ' + ', bạn có thể cộng số học hai số với nhau, có thể kết hợp hai danh sách, hoặc nối hai chuỗi khác nhau lại…

Tính năng này trong Python gọi là nạp chồng toán tử, cho phép cùng một toán tử được sử dụng khác nhau tùy từng ngữ cảnh.

Bên trên chúng ta đã tìm hiểu một số magic method rồi. Trong phần này chúng ta sẽ áp dụng magic method để thực hiện nạp chồng toán tử. 

Ví dụ để nạp chồng toán tử + chúng ta sử dụng phương thức `__add__()` như sau:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Tọa độ: ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

point_1 = Point(1, 1)
point_2 = Point(2, 2)

print(point_1 + point_2)
```

Kết quả nhận được là:
```python
Tọa độ: (3, 3)
```

Khi thực hiện point_1 + point_2, Python sẽ gọi ra `p1.__add__(p2)`.

<img src="https://1.bp.blogspot.com/-FnIuZ0OPYk8/VcJSm4w254I/AAAAAAAAIpA/Y6_3b2r53TA/s1600/operator_overloading.PNG" style="display:block; margin-left:auto; margin-right:auto">

Chúng ta thử một ví dụ cho nạp chồng phép toán so sánh cho khoảng cách từ một điểm đến gốc tọa độ:

```python
class Point:
     def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

     def __str__(self):
        return "({},{})".format(self.x, self.y)

     def __lt__(self, other):
        self_dis = (self.x ** 2) + (self.y ** 2)
        other_dis = (other.x ** 2) + (other.y ** 2)
        return self_dis < other_dis

point_1 = Point(1, 1)
point_2 = Point(2, 2)
print(point_1 < point_2)
print(point_2 < point_1)
```
Kết quả là 
```python
True
False
```

Phần cuối này mình muốn bổ sung thêm khái niệm:
* **Class** − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.
* **Instance** − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.
* **Object** − A unique instance of a data structure that's defined by its class. An object comprises both data members (class variables and instance variables) and methods.

Như vậy chúng ta đã tìm hiểu những khái niệm quan trong nhất của OOP với Python. Hy vọng bài viết này hữu ích với các bạn.
#### Tài liệu tham khảo
1. https://www.w3schools.com/python/python_inheritance.asp
2. https://tuhocict.com/class-trong-python-khai-niem-khai-bao/
3. https://www.tutorialsteacher.com/python/property-function 
4. https://www.tutorialspoint.com/python/python_classes_objects.htm
5. https://quantrimang.com/nap-chong-toan-tu-trong-python-160450

