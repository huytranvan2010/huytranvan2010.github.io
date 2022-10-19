---
layout: post
title: "Lập trình hướng đối tượng với Python - Phần 1"
tags: [Python tutorial]
comments: true
---

**Class (lớp)** là kiểu dữ liệu do người dùng tự định nghĩa, tập hợp nhiều thuộc tính đặc trưng cho mọi đối tượng được tạo ra từ lớp đó.

Phân biệt Object và class:
* Object có trạng thái và hành vi (attributes và methods)
* Class: template mô tả trạng thái và hành vi của loại đối tương mà lớp hỗ trợ. Một đối tương là một thực thể (instance) của một lớp.

Cùng tìm hiểu trước một số khái niệm quan trọng trong lập trình hướng đối tượng với Python.

**Constructor (hàm khởi tạo)** - hàm gọi trong quá trình tạo object của class. Hàm tạo có tác dụng tạo các instance attribute.

**Attribute (biến, đặc tính)** - là thành phần chứa dữ liệu trong class. Có 2 loại attribte là instance attribute và class attribute. **Class attribute** được khởi tạo trong thân class, đại diện cho class và toàn bộ object thuộc class đó. **Instance class** sẽ gắn liền với object khi được khởi tạo (được khởi tạo và gán giá trị trong hàm khởi tạo)

**Method (phương thức**) - là thành phần xử lý dữ liệu trong class (có thể gọi là function in class). Python phân biệt các khái niệm instance method, class method và static method.
* **Instance method** - hàm xử lý trạng thái của object. Instance method gắn liền với object và sử dụng các instance attribute (dữ liệu gắn với object).
* **Class method** - hàm xử lý của class và gắn liền với class. Class method dùng để xử lý các class attribute.
* **Static method** - không sử dụng bất kỳ thông tin nào của class và object (mặc dù vẫn nằm trong class), thường được dùng để xử lý logic nào đó liên quan đến đối tượng.

**Tính đóng gói (encapsulation)** - cho phép kiểm soát việc truy cập và thay đổi dữ liệu.

**Tính kế thừa (Inheritance)**
Tính kế thừa cho phép chúng ta định nghĩa class mà kế thừa các phương thức và thuộc tính từ class khác. Class mẹ gọi là base class (class cơ sở), class con (kế thừa từ class mẹ) gọi là derived class (class kế thừa).

**Tính đa hình (polymorphism)** - hai hay nhiều lớp có phương thức giống nhau (tên gọi) nhưng có thể thực thi khác nhau.

### 1. Constructor (hàm khởi tạo)
```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

toi = Person("Huy", "Tran")
```
` __init__()` là một hàm khởi tạo trong Python. Nó có ít nhất một tham số, thường đặt là `self`. Bạn hoàn toàn có thể dùng các tên khác để thay thế `self`. Khi có nhiều tham số trong hàm khởi tạo thì `self` là tham số đứng đầu tiên. `self` này khá giống với con trỏ `this` trong C++. 

> Thực sự về bản chất `__init__()` không phải là constructor (khởi tạo object) mà là initilizer (khởi tạo các giá trị cho object). 
Python sử dụng magic method `__new__()` để tạo object cho class. `__new__()` mới chính là constructor thực sự của class. 
Do vậy ở bên trên khi thực hiện lệnh `toi = Person("Huy", "Tran")` đầu tiên Python sẽ gọi `__new__()` để khởi tạo object, sau đó mới tới `__init__()` để gán các giá trị cho object đó.

### 2. Attribute
Attribute bao gồm 2 loại là class attribute và instance attribute.
* **Class attribute** được khởi tạo trong thân class, đại diện cho class và toàn bộ object thuộc class đó. 
* **Instance class** sẽ gắn liền với object khi được khởi tạo (được khởi tạo và gán giá trị trong hàm khởi tạo)

```python
class Person:
    """ docs string """
    count = 0   # class attribute

    def __init__(self, fname, lname):
        self.firstname = fname      # instance attribute
        self.lastname = lname
        Person.count += 1       # cứ khởi tạo instance thì tăng lên 1

toi = Person("Huy", "Tran")
ban = Person("Ni", "Tu")
print("Class attribute: ", Person.count)    # truy cập class attribute thông qua tên class
print("Access through instance: ", toi.count)   # truy cập class attribute qua instance
```

Đầu ra nhận được

```python
Class attribute:  2
Access through instance:  2
```

Instance attribute ngoài việc được tạo trong `__init()__` nó còn có thể được tạo cho object cụ thể sau khi đã khởi tạo object. Cùng xem ví dụ sau:

```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname      # instance attribute
        self.lastname = lname

toi = Person("Huy", "Tran")
toi.new_instance = "Anh"    # tạo bên ngoài chỉ riêng cho đối tượng toi
print(toi.new_instance)
ban = Person("Ni", "Ha")
print(ban.new_instance)     # báo lỗi
```
Việc tạo instance attribute ở bên ngoài chỉ có ý nghĩa cho một object cụ thể, nếu một object khác được tạo từ class thì nó không có attribute đó (như ở trên sẽ báo lỗi). Tốt nhất các instance attribute nên được tạo trong hàm `__init__()` để có thể chia sẻ cho tất cả các object.

### 3. Methods (các phương thức)
Python phân biệt các khái niệm instance method, class method (thường xử lý các class attribute) và static method (không liên quan gì đến object và class mặc dù nằm trong đó, xử lý các logic liên quan đến object).

Cũng tương tự như instance attribute có thể khai báo riêng cho từng object (ngoài class) thì **instance method** cũng có thể làm tương tự. Tuy nhiên khuyến khích khai báo bên trong class để cho tất cả object có phương thức đó.

**Instance method** - gắn liền với đối tượng
```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname      # instance attribute
        self.lastname = lname

    # instance method
    def printname(self)
        return self.lastname + self.firstname

toi = Person("Huy", "Tran")
print(toi.printname())      # nhận được Tran Huy
```
Chú ý trong instance method ở trên tham số đầu tiên luôn là `self` vì nó gắn liền đối tượng. Ở bên dưới khi gọi method thì không cần truyền `self` vào nữa vì Python tự hiểu đó là đối tượng đang dùng.

**Class method** - gắn liền class, thường dùng để xử lý class attribute.

```python
class Person:
    """ docs string """
    count = 0   # class attribute

    def __init__(self, fname, lname):
        self.firstname = fname      # instance attribute
        self.lastname = lname
        Person.count += 1       # cứ khởi tạo instance thì tăng lên 1

    # tạo class method chú ý có @classmethod trước khi định nghĩa
    @classmethod
    def show_count(cls):
        print("Có {} người trong class".format(cls.count))

toi = Person("Huy", "Tran")
ban = Person("Ni", "Tu")

Person.show_count()
```

Đầu ra nhận được là 
```python
Có 2 người trong class
```
**@classmethod** trong Python là một **decorator** (hàm đặc biệt có thể nhận một hàm khác làm tham số để bổ sung tính năng cho hàm đó). Để có được class method từ method thông thường ta chỉ việc thêm **@classmethod** ngay bên trên định nghĩa.

Trong ví dụ trên nhận thấy class method cũng có một biến đặc biệt trong danh sách tham số đó là **cls** (viết tắt của class). Biến **cls** chứa thông tin của class, tương tự `self` chứa thông tin của object. Truy xuất attribute qua biến **cls** cũng giống như truy xuất attribute thông qua tên class.

> Chúng ta hoàn toàn có thể gọi class method thông qua tên của object (`toi.show_count()`). Tuy nhiên khuyến khích nên dùng tên class đối với các class method cũng như class attribute.

**Static method** - nằm trong class nhưng hoàn toàn tự do, không bị ràng buộc dữ liệu với class hay object, thường được sử dụng để xử lý các logic.
Để tạo static method trong Python chúng ta sử dụng decorator **@staticmethod**.
```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname      # instance attribute
        self.lastname = lname

    @staticmethod
    def calculate_birth_year(age):
        import datetime
        year = datetime.datetime.now().year
        return year - age

print("The birth year: ", Person.calculate_birth_year(30))
```
Đầu ra nhận được là
```python
The birth year:  1991
```

Phương thức `calculate_birth_year()` không sử dụng bất kì thông tin nào của class hay object, nó hoạt động độc lập. Có thể gọi static method thông qua tên của class (hoặc object cũng được nhưng không khuyến khích).

### 4. Tính đóng gói (Encapsulation) - public, private, protected 
Tính đóng gói hạn chế quyền truy cập vào trạng thái bên trong của đối tượng. Điều này ngăn chặn dữ liệu bị sửa đổi trực tiếp. 
Bên C++ chúng ta có các khái niệm public (truy cập bất kì đâu), protected (truy cập trong class nội bộ và class kế thừa), private (truy cập trong class bộ). Trong Python không có các khái niệm này, thay vào đó nó sử dụng kỹ thuật **name mangling**. 

Mặc định các thành viên trong class có thể truy cập từ mọi chỗ (giống public). Để hạn chế quyền truy cập có thể thực hiện như sau:
* Thêm `_` (dấu gạch dưới) trước tên thành viên để chỉ cho phép truy cập trong class nội bộ và class kế thừa (giống protected)
* Thêm `__` (2 dấu gạch dưới) trước tên thành viên để chỉ cho phép truy cập nội bộ (giống private) tránh việc thay đổi không mong muốn.

```python
class Shoes:
    """ create a Shoes class """
    def __init__(self):
        # thuộc tính private ngăn chặn sửa đổi trực tiếp
        self.__maxprice = 900

    def sell(self):
        print("Giá sản phẩm: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Shoes()
c.sell()

# Thay đổi giá trị tiếp thông qua attribute
# Do đang để private cho thuộc tính nên không thay đổi được
c.__maxprice = 1000     # chỗ này kiểu như tạo một attribute mới bên ngoài
c.sell()

# Phải sử dụng hàm setter để thay đổi giá maxprice
c.setMaxPrice(1000)
c.sell()
```
Đầu ra sẽ là 
```python
Giá sản phẩm: 900
Giá sản phẩm: 900
Giá sản phẩm: 1000
```

Nhận thấy phải dùng một hàm giống setter trong C++ để thay đổi giá trị của biến private (bắt đầu bằng __).

Thêm ví dụ nữa:
```python
class Student:
    def __init__(self, name):
        self.__name = name
  
    def displayName(self):
        print(self.__name)
  
s = Student("Santhosh")
s.displayName()
  
# Báo lỗi
print(s.__name)
```
Đầu ra như sau:
```python
Santhosh
Traceback (most recent call last):
  File "test.py", line 138, in <module>
    print(s.__name)
AttributeError: 'Student' object has no attribute '__name'
```
Khi chúng ta truy cập trực tiếp nó sẽ báo lỗi ngay.

### 5. Inheritance (tính kế thừa)
Tính kế thừa cho phép chúng ta định nghĩa class mà kế thừa các phương thức và thuộc tính từ class khác. Class mẹ gọi là base class (class cơ sở), class con (kế thừa từ class mẹ) gọi là derived class (class kế thừa). Class con có thể kế thừa từ nhiều base class gọi là đa kế thừa (multiple inheritance).

```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname + self.lastname)

class Student(Person):
    pass    # khi ko muốn add thêm attribute hay methods nào, kế thừa toàn bộ base class

x = Student("Mike", "Olsen")
x.printname()
```
Class Student sẽ có đầy đủ các phương thức, attributes như class Person (truyền `pass` vào). Bây giờ chúng ta sẽ thay đổi một chút hàm tạo `__init__()`.
```python
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
```
Khi thêm  hàm `__init__()` class Student không còn kế thừa hàm  hàm `__init__()` của class Person nữa. Nếu vẫn muốn kế thừa chúng ta có thể thêm hàm  hàm `__init__()` của Parent như sau:

```python
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)     # có self ở đây để lưu attributes cho object, ko có sẽ báo lỗi
```

Hoặc vừa kế thừa vừa thêm attributes mới (vẫn đang ghi đè, cái này hay sử dụng hơn)
```python
class Student(Person):
    def __init__(self, fname, lname, age):
        # có self ở đây để còn lưu attribute cho object
        # phải có self không sẽ báo lỗi
        Person.__init__(self, fname, lname)
        self.age = age

    def printage(self):
        print(self.age)

x = Student("John", "Doe", 15)
x.printname()
x.printage()
```

Hoặc có thể sử dụng hàm `super()` để kế thừa toàn bộ thuộc tính và phương thức của base class. Mình thích dùng cái này hơn.
```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # sử dụng super sẽ không cần tên của class cha, ở đây ko cần dùng self

anh = Student("Huy", "Tran")
anh.printname()
```

Ở đây vừa thêm ở attribute, vừa thêm cả method
```python
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
```

Chú ý ở trên chúng ta đã tìm hiểu cơ chế **name mangling** liên quan tới tính đóng gói. Cùng xem qua một ví dụ
```python
class Person:
    """ docs string """
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self._protected = True 
        self.__private = True

    def printname(self):
        print(self.firstname + self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
print(x._protected)
print(x.__private)
```

Đầu ra ta sẽ nhận được
```python
True
Traceback (most recent call last):
  File "OOP/oop.py", line 437, in <module>
    print(x.__private)
AttributeError: 'Student' object has no attribute '__private'
```
Rõ ràng attribute `_protected` vẫn được kế thừa còn attribute `__private` không được kế thừa nên đã báo lỗi.

Có hàm `issubclass(classA, classB)` để kiểm tra class A có phải là class con của class B hay không. `isinstance(obj, classA)` để kiểm tra obj có phải là instance của class A hoặc class con của class A hay không.

**Đa kế thừa (Multiple Inheritance)**

Giống như C++ thì trong Python một lớp có thể được định nghĩa từ nhiều lớp cha. Điều này được gọi là đa kế thừa.

```python
class LopCha1:
     pass

class LopCha2:
     pass

class LopCon(LopCha1, LopCha2):
     pass
```

<img src="https://st.quantrimang.com/photos/image/2018/12/03/INHERITANCE-1.jpg" style="display:block; margin-left:auto; margin-right:auto">

Lớp con được định nghĩa từ nhiều lớp cha và kế thừa đặc tính của cả hai lớp cha.

Các lớp cha có thể có các thuộc tính hoặc các phương thức giống nhau. Lớp con sẽ ưu tiên thừa kế thuộc tính, phương thức của **lớp đứng đầu tiên** trong danh sách thừa kế.

**Kế thừa đa cấp (Multilevel Inheritance)**

Ngoài việc có thể kế thừa từ các lớp cha, bạn còn có thể tạo lớp con mới kế thừa các lớp con trước đó. Đây gọi là kế thừa đa cấp (Multilevel Inheritance).

```python
class LopCha:
     pass

class LopCon1(LopCha):
     pass

class LopCon2(LopCon1):
     pass
```

<img src="https://st.quantrimang.com/photos/image/2018/12/03/INHERITANCE-2.jpg" style="display:block; margin-left:auto; margin-right:auto">

**Thứ tự truy xuất phương thức (Method Resolution Order)**

Thứ tự truy xuất phương thức (MRO) là thứ tự mà Python tìm kiếm một phương thức trong hệ thống phân cấp các lớp. Đặc biệt nó đóng vai trò quan trọng đa kế thừa vì phương thức đơn có thể được tìm thấy trong nhiều lớp.

Trong đa thừa kế, bất kỳ thuộc tính cần được truy xuất nào, đầu tiên nó sẽ được tìm kiếm trong lớp hiện tại. Nếu không tìm thấy, tìm kiếm tiếp tục vào lớp cha đầu tiên rồi tiếp tục từ trái qua phải. Vậy thứ tự truy xuất sẽ là **[LopCon, LopCha1, LopCha2, object]**.

Nói một cách dễ hiểu, MRO dùng để hiển thị danh sách/tuple các class cha của một class nào đó. MRO được sử dụng theo hai cách (phải lấy tên class để gọi):
- `__mro__`: trả về một tuple
- `mro()`: trả về một danh sách.

```python
class A:
    def process(self):
        print('A process()')

class B:
    def process(self):
        print('B process()')

class C(A, B):
    pass

obj = C()
obj.process()

print(C.__mro__)     # print MRO for class C
```
Kết quả là:
```python
A process()
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

Thêm một ví dụ nữa:
```python
class A:
    def process(self):
        print('A process()')

class B:
    def process(self):
        print('B process()')

class C(A, B):
    def process(self):
        print('C process()')

class D(C,B):
    pass

obj = D()
obj.process()
print(D.mro())
```
Kết quả là:
```python
C process()
[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```

<img src="http://www.srikanthtechnologies.com/blog/python/mro_3.jpg" style="display:block; margin-left:auto; margin-right:auto">

Khá nhiều rồi, tạm thời tìm hiểu đến đây thôi để bài sau chiến tiếp.
#### Tài liệu tham khảo
1. https://www.w3schools.com/python/python_inheritance.asp
2. https://tuhocict.com/class-trong-python-khai-niem-khai-bao/
3. https://www.tutorialsteacher.com/python/property-function 
4. https://www.tutorialspoint.com/python/python_classes_objects.
5. http://www.srikanthtechnologies.com/blog/python/mro.aspx

