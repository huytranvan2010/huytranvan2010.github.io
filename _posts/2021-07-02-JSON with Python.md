---
layout: post
title: "JSON with Python"
tags: [Python tutorial]
comments: true
---

**JSON (JavaScript Object Notation)** là một định dạng để cấu trúc dữ liệu. Nó thường được sử dụng để lưu trữ, truyền dữ liệu giữa web và server (sử dụng trong database và APIs). JSON đọc được đối với cả người và máy. JSON tồn tại dưới dạng "chuỗi byte" rất hữu ích khi cần truyền data qua mạng. So với XML, JSON nhẹ hơn khá nhiều.

JSON hỗ trợ primitive types (strings, numbers, boolean) cũng như nested arrays và objects.
Ví dụ về JSON:
```python
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}
```

Python cũng hỗ trợ JSON với built-in package gọi là `json`. Package này cung cấp tất cả các công cụ cần thiết để hoạt động với JSON objects bao gồm parsing, serializing, deserializing... Hãy cũng xem một số ví dụ đơn giản về cách chuyển từ JSON object về Python object và ngược lại.

* **Serialization:** - encoding data into JSON format. Ví dụ chuyển Python list về JSON
* **Deserialization:** - decoding JSON data. Ví dụ chuyển JSON data thành Python list

### 1. Serialization
Có thể dùng 2 methods sau để chuyển Python data về JSON format:
* `dump()`: ghi dữ liệu vào một đối tượng như file ở dạng JSON format (thường lưu ra file bên ngoài)
* `dumps()`: ghi dữ liệu về JSON format (thường để sử dụng JSON ở trong chương trình)

Python và JSON không chia sẻ tất cả kiểu dữ liệu giống nhau. 

Python | JSON
------------ | -------------
dict | object
list, tuple | array
str | string
int, long, float | number
True | true
False | false
None | null

Cùng xem ví dụ đơn giản trước đã:

```python
import json
print("From dict: ", json.dumps({'name': "Huy", 'age': 30}))
print("From list: ", json.dumps(["1", "a"]))
print("From tuple: ", json.dumps(('anh', 'em')))
print("From string: ",json.dumps("Hello"))
print("From int: ",json.dumps(100))
print("From float: ", json.dumps(23.8))
print("From True: ", json.dumps(True))
print("From False: ", json.dumps(False))
print("From None: ", json.dumps(None))
```

Đầu ra nhận được như sau: 
```python
From dict:  {"name": "Huy", "age": 30}
From list:  ["1", "a"]
From tuple:  ["anh", "em"]
From string:  "Hello"
From int:  100
From float:  23.8
From True:  true
From False:  false
From None:  null
```

Cả `dump()` và `dumps()` đều cho phép chúng ta chỉ định `indent` (thụt lề tùy chọn). `indent` xác định số khoảng trắng được sử dụng để thụt dòng, điều này giúp JSON dễ đọc hơn.

```python
json_str = json.dumps(data, indent=4)
```

Dưới đây là ví dụ về serialization với JSON:

```python
import json

data = {
    "user": {
        "name": "Huy",
        "age": 30
    }
}

# lưu file JSON bên ngoài
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)   #  theem indent nhìn dexw hơn

# chuyển thành string JSON
json_str = json.dumps(data)
print(json_str)
```

Thêm một ví dụ nữa 

```python
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON, nếu để mặc định hơi khó nhìn
person_json = json.dumps(person)

# use different formatting style, chỉnh sửa chút cho dễ nhìn nào
# nên dùng sort_keys=True, bt mặc định là False để sắp xếp các keys theo alphabet, indent số khoảng trắng thụt dòng
# ở đây không khuyến khích dùng separators (dạng tuple), "; " sẽ thay ", ", "= " sẽ thay ": "
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json) 
print(person_json2) 

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)      # nên để indent=4 cho dễ nhìn
```

Và đầu ra như này:

```python
{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}
{
    "age"= 30; 
    "city"= "New York"; 
    "hasChildren"= false; 
    "name"= "John"; 
    "titles"= [
        "engineer"; 
        "programmer"
    ]
}
```

### 2. Deserializing JSON format
Deserialization là quá trình chuyển JSON formar về Python object. `json` cung cấp 2 methods để thực hiện việc này:
* `load()` load JSON format từ file (dùng cái này khi đọc data từ file)
* `loads()` load JSON data từ string chứa JSON encoded-data. String dạng JSON được đặt trong dấu nháy `''` và chứa các cặp key-value đặt trong `{}` giống như dictionary.

Dưới đây là chuyển đổi giữa các kiểu dữ liệu từ JSON format sang Python object:

JSON | Python
------------ | -------------
object | dict
array | list
string | str
number(int) | int
number(real) | float
true | True
false | False
null | None

Dưới đây là ví dụ
```python
import json

# taoj tuple
anh = (8, "Q")

# chuyển Python object về JSON format
encoded_anh = json.dumps(anh)
print(encoded_anh)
# chuyển JSON format về Python object
decoded_anh = json.loads(encoded_anh)

print("Nhận được list từ tuple ban đầu: ", decoded_anh)
```
Bạn có thể thấy từ tuple ban đầu chuyển sang JSON format rồi chuyển lại Python object, cái chúng ta nhận được là Python list chứ không phải tuple.

### 3. Working with custom object
Encoding a custom object với `JSONEncoder` mặc định sẽ gây ra lỗi `TypeError`. Chúng ta có thể xác định custom encoding function nó sẽ lưu tên class và tất cả các object variables vào dictionary. Sử dụng function này cho `default` argument trong `json.dump()`.

Cùng xem ví dụ sau:
```python
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age 


user = User('Max', 27)

"""
Serializarion thông thường sẽ báo lỗi như này
TypeError: Object of type User is not JSON serializable
"""
# userJSON = json.dumps(user)

# cần viết custom encoding function
def encode_user(o):
    if isinstance(o, User):     # kiểm tra o có phải instance của class User không
        return {'name': o.name, 'age': o.age, o.__class__.__name__:True}   # nếu có trả về dict
    else:
        raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)
print(userJSON)
```

Cách thứ hai là thực hiện custom JSONEncoder. 
```python
""" Cách 2: custom JSONEncoder """
from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__:True}    # cái cuối là User class name (trick để tí decode)
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls=UserEncoder)

# hoặc dùng thẳng luôn
userJSON = UserEncoder().encode(user)
print(userJSON)
```
Sau đó nếu chúng ta muốn decode thì sao, nếu decode như bình thường nó sẽ trả về dictionary trong khi đó ta muốn nhận được object ban đầu. Hãy xem ví dụ bên dưới
```python
""" Muốn decode thì sao (deserialization) """
# Khi decode trở lại sẽ nhận được dictionary chứ không phải object như ta mong muốn
# ko dùng được như user.name, do đó cần viết custom decoding method
user = json.loads(userJSON)
print(user)
print(type(user))

def decode_user(dct):
    if User.__name__ in dct:   # tìm tên class User có thuộc keys của dict không
        return User(name=dct['name'], age=dct['age'])
    return dct 

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)
print(user)
```

Ở đây chúng ta lợi dụng tên class để check xem nó có thuộc class ban đầu không (đây chỉ là trick thôi).

Các bạn xem thêm tại [Github-huytranvan2010](https://github.com/huytranvan2010/Python-Tutotial/tree/master/JSON) mình có để code mẫu ở đó.
##### Tài liệu tham khảo 
1. https://www.geeksforgeeks.org/python-json/?ref=lbp 
3. https://www.python-engineer.com/courses/advancedpython/11-json/ 