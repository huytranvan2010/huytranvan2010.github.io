---
layout: post
title: "Introduction to PyQt"
tags: [Python tutorial, GUI Application]
comments: true
---

Ngoài web app và mobile app đang chiếm lĩnh thị trường phần mềm vẫn còn nhiều nhu cầu cho **Graphical User Interface (GUI)** desktop application. Đối với các nhà phát triển xây dựng ứng dụng dựa trên Python sẽ có rất nhiều lựa chọn như Tkinter, PyQt, PySide2, wxPython... Trong bài này chúng ta cùng tìm hiểu về GUI application với Python và PyQt.

**PyQt** như là một liên kết của Python với Qt (bộ các thư viện C++ và các công cụ phát triển cho GUI, network, threads, regulaar expressions, SQL databases, SVG, OpenGL, XML...). PyQt tương thích với Windows, Unix, Linux, macOS, iOS và Android. Có thể cài PyQt với cú pháp sau:
```python
pip install pyqt
```

Một số khái niệm chính trong PyQt:
* Widgets
* Layout managers
* Dialogs
* Main windows
* Applications
* Event loops
* Signals and slots

Những thành phần này là các building blocks của PyQt GUI applications, hầu hết chúng được thể hiện như các classes. `PyQt5.QtWidgets` là module cung cấp tất cả các class này.

### 1. Widgets
`QWidget` là bass class cho tất cả user interface objects (widgets). **Đó là các thành phần có hình chữ nhật mà bạn có thể đặt lên window để xây dựng GUI**. Widgets chứa các attributes và methods cho phép bạn thực hiện các hành vi và sự xuất hiện.

Widgets nhận mouse clicks, keypresses và các events khác từ người dùng, hệ thống và từ nhiều nguồn khác nữa. Mỗi lần widget bắt được event, nó đưa ra các signal (tín hiệu) để thông báo sự thay đổi trạng thái. PyQt5 có bộ sưu tập đa dạng các widgets phục vụ cho nhiều mục đích khác nhau. Dưới đây là một số widgets hữu ích và thông dụng:
* Buttons
* Labels
* Line edits
* Combo boxes
* Radio buttons

Hãy cùng nhau xem các widgets này hoạt động ra sao.
##### 1.1. Button
Khởi tạo buttton thông qua `QPushButton`. Các typical buttons là OK, Cancel, Apply, Yes, No và Close. 
<img src="https://files.realpython.com/media/buttons.40e5948189f6.png" style="display:block; margin-left:auto; margin-right:auto">

Khi bạn click vào các buttons đó bạn có thể ra lệnh cho máy tính thực hiện các actions. 

##### 1.2. Labels
Có thể tạo labels thông qua `QLabel`. **Labels giúp chúng ta hiển thị các thông tin ở dạng văn bản hoặc hình ảnh.**
<img src="https://files.realpython.com/media/labels.f7818e2fa725.png" style="display:block; margin-left:auto; margin-right:auto">

Bạn có thể sử dụng labels để giải thchs mục đích và cách sử dụng GUI được tốt hơn. Bận cũng có thể thay đổi sự xuất hiện của chúng bằng một số cách, nó có thể chấp nhận **HTML text**. 

##### 1.3. Line edits
A single-line text box có thể được tạo thông qua `QLineEdit`. Line edits hữu ích khi bạn cần người dùng điền hoặc chỉnh sửa dữ liệu ở định dạng văn bản thuần túy (in plain text format).
<img src="https://files.realpython.com/media/line-edits.41e67fc77d2b.png" style="display:block; margin-left:auto; margin-right:auto">

Line edits giống như này cung cấp các hoạt động chỉnh sửa cơ bản như copy, paste, undo, redo, drag.... Trong hình trên hàng đầu tiên có show placeholder text để thông báo loại inputs người dùng cần nhập vào.

##### 1.4. Combo boxes
Combo boxes có thể được tạo thông qua `QComboBox`. **Combo box** đưa cho chúng ta danh sách các lựa chọn. Dưới đây là ví dụ:
<img src="https://files.realpython.com/media/combo-box.442ec954da54.gif" style="display:block; margin-left:auto; margin-right:auto">

Loại combo box này chỉ **read-only**, điều này có nghĩa người dùng chỉ được chọn một lựa chọn mà không được add thêm vào. Tuy nhiên cũng có loại combo boxes **editable** cho phép người dùng add thêm sự lựa chọn. 

##### 1.5. Radio button
Radio button có thể được tạo thông qua **QRadioButton**. QRadioButton object là loại option button có thể chuyển đổi giữa chọn và không chọn. Radio button hữu ích khi cần người dùng chọn một trong các option. Trong trường hợp này tất cả các option được hiện ra cùng lúc.
<img src="https://files.realpython.com/media/radio-buttons.dc2424d696dc.gif" style="display:block; margin-left:auto; margin-right:auto">

### 2. Layout Managers
Bạn đã biết rất nhiều widgets, làm sao có thể sắp xếp chúng một cách mạch lạc? Có rất nhiều kỹ thuật có thể sử dụng để sắp xếp các widgets. Ví dụ sử dụng `.resize()` và `.move()` để cho widget có kích thước tuyệt đối và vị trí. Tuy nhiên cách này có một số nhược điểm như sau:
* Phải thực hiện nhiều tính toán thủ công để xác định kích thước chính xác và vị trí của mỗi widget
* Phải thực hiện thêm nhiều tính toán để phản hồi (respond) chính xác những thay đổi về kích thước
* Phải làm lại tất cả các tính toan bất cứ khi nào thay đổi layout, thêm hoặc xóa widgets

Có một cách thay thế là sử dụng `.resizeEvent()` để tính widget size và vị trí động. Tuy nhiên cách thay thế hiệu quả nhất là sử dụng **layout manager**, giúp tăng hiệu suất và cải thiện khả năng bảo trì code (maintainability).

**Layout managers** là các classes cho phép chúng ta định kích thước và vị trí của widgets để trên application form. Layout managers tự động điều chỉnh (adapt) để thay đổi kích thước events và nội dung. Các widgets trong layout sẽ tự động được thay đổi kích thước bất cứ khi bào form thay đổi kích thước.

PyQt cung cấp 4 basic layout manager classes:
* `QHBoxLayout`
* `QVBoxLayut`
* `QGridLayout`
* `QFormLayout`

###### 2.1. QHBoxLaypit
QHBoxLayout sắp xếp các widgets theo chiều ngang từ trái qua phải:
<img src="https://files.realpython.com/media/horizontal-layout.39d78929812f.png" style="display:block; margin-left:auto; margin-right:auto">

Dưới đây là code hướng dẫn sử dụng QHBoxLayout:
```python
# Filename: h_layout.py

"""Horizontal layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QHBoxLayout')

# tạo QHBoxLauout object
layout = QHBoxLayout()

# thêm các buttons vào layout với .addWidget()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))

# set layout là window's layout
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
```
Khi bạn chạy file `h_layout.py` từ commnad line, bạn sẽ nhận được output như dưới đây:
<img src="https://files.realpython.com/media/h-layout.3471b0b63bc8.png" style="display:block; margin-left:auto; margin-right:auto">

Các buttons được sắp xếp từ trái sang phải theo thứ tự giống như mình thêm vào ở phần code.

##### 2.2 QVBoxLayout
QVBoxLayout sắp xếp các widgets theo chiều dọc từ trên xuống dưới.
<img src="https://files.realpython.com/media/vertical-layout.c173d779b79d.png" style="display:block; margin-left:auto; margin-right:auto">

Dưới đây là hướng dẫn tạo và sử dụng QVBoxLayout object:
```python
# Filename: v_layout.py

"""Vertical layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QVBoxLayout')

# tạo QVBoxLayout object
layout = QVBoxLayout()

# thêm 3 buttons vào layout
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))

# set layout cho window
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
```
Đầu ra chúng ta nhận được như này:
<img src="https://files.realpython.com/media/v-layout.366271060ab3.png" style="display:block; margin-left:auto; margin-right:auto">

##### 2.3. QGridLayout
QGridLayout sắp xếp các widgets ở dạng lưới (grid) theo hàng và cột. Mỗi widget có một vị trí tương đối trong grid. Bạn có thể xác định vị trí của widget thông qua dạng `(row, column)`. Các giá trị này là các số nguyên. Nó xác định ô (cell) sẽ đặt widget vào đó.
<img src="https://files.realpython.com/media/grid-layout.3bbf850cab1e.png" style="display:block; margin-left:auto; margin-right:auto">

QGridLayout lấy không gian có sẵn do parent tạo ta, chia thành các cột và hàng, đặt mỗi widget vào ô riêng của nó. Dưới đây là các sử dụng QGridLayout:
```python
# Filename: g_layout.py

"""Grid layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')

# tạo QGridLayout object
layout = QGridLayout()

# thêm các widgets vào thông qua .addWidget(), tham số thứ hai và ba là row và column => xác định vị trí widget
layout.addWidget(QPushButton('Button (0, 0)'), 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)

# set layout cho window
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
```
Chú ý
```python
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
```
có thêm 2 arguments ở cuối là `rowSpan` và `columnSpan`. Chúng được sử dụng để widget có thể chiếm nhiều hơn 1 hàng hoặc 1 cột.
<img src="https://files.realpython.com/media/g-layout.d3784adad447.png" style="display:block; margin-left:auto; margin-right:auto">

##### 2.4. QFormLayout
QFormLayout sắp xếp các widgets thành 2 cột. Cột đầu tiên thường hiển thị các messages trong labels. Cột thứ hai thường chứa các widgets như `QLineEdit, QComboBox, QSpinBox...`. Những widgets này cho phép người dùng nhập hoặc chỉnh sửa dữ liệu liên quan (regerding) đến thông tin ở cột đầu tiên.
<img src="https://files.realpython.com/media/form-layout.6e168f74cdcd.png" style="display:block; margin-left:auto; margin-right:auto">

Nếu bạn đang làm việc với **database application** dạng layout này trực quan sẽ giúp ích nhiều cho bạn. Dưới đây là ví dụ cách tạo ứng dụng có sử dụng QFormLayout obejct để sắp xếp widgets:
```python
# Filename: f_layout.py

"""Form layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QFormLayout')

# tạo QFormLayout object
layout = QFormLayout()

# thêm các widgets theo hàng, một hàng có 2 cột tương ứng 2 widgets
layout.addRow('Name:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job:', QLineEdit())
layout.addRow('Hobbies:', QLineEdit())

# set layout cho window
window.setLayout(layout)

window.show()
sys.exit(app.exec_())
```
Cùng phân tích chi tiết hơn
```python
layout.addRow('Name:', QLineEdit())
```
QFormLayout cung cấp phương thức tiện lợi `.addRow()` để thêm 2 widgets vào một dòng của layout. Đối số đầu tiên trong `.addRow()` là label, đối số thứ hai là bất kỳ widget nào cho phép người dùng nhập hay chỉnh sửa data.

Nếu chạy đoạn code trên chúng ta sẽ nhận được output như sau:
<img src="https://files.realpython.com/media/f-layout.5bc3a560d54c.png" style="display:block; margin-left:auto; margin-right:auto">

Cột đầu tiên để hỏi người dùng một số thông tin. Cột thứ hai cho phép người dùng nhập hoặc chỉnh sửa thông tin mà bạn đã hỏi.

### 3. Dialogs
Với PyQt bạn có thể phát triển 2 dạng của GUI desktop application. Phụ thuộc vào class bạn sử dụng để tạo main form hay window bạn sẽ có một trong những cái sau:
* **Main window-style application**: main window của ứng dụng kế thừa từ `QMainWindow`.
* **Dialog-style aplication**: main window của ứng dụng kế thừa từ `QDialog`.

Chúng ta sẽ làm quen với dialog-style application trước. Trong phần tiếp theo sẽ làm quen với window-style application.

Để phát triển Dialog-style application bạn cần tạo GUI class kế thừa từ `QDialog` (base class của tất cả dialog windows). **Dialog window** luôn là top-level window bạn có thể sử dụng như main window cho dialog-style application.
> **Chú ý**: Dialog window cũng hay được sử dụng trong Main window-style application để giao tiếp và tương tác với người dùng. Khi dialog window được sử dụng để giao tiếp với người dùng nó có thể là:
> * **Modal dialogs:** block input to any other visible windows in the same application. Bạn có thể hiển thị modal dialog bằng cách gọi `.exec_()`
> * **Modeless dialogs: hoạt động độc lập với các windows khác trên cùng ứng dụng. Bạn có thể hiển thị modeless dialog bằng cách gọi `.show()`
> Dialog window cũng cung cấp giá trị trả về và nó có các buttons mặc định (ví dụ **OK** và **Cancel**)

Dialog luôn là top-level widget (widget trên cùng). Nếu nó có parent thì vị trí mặc định của nó là ở trung tâm trên cùng của các widgets thuộc parent. Loại dialog này sẽ chia sẻ parent's taskbar entry. 

Dưới đây là cách sử dụng QDialog để phát triển Dialog-Style application:
```python
# Filename: dialog.py

"""Dialog-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

# xây dựng full class dialog cho GUI, kết thừa từ QDialog
class Dialog(QDialog):
    """Dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('QDialog')

        # tạo 2 object layout
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # thêm các widgets vào formLayout thông qua .addRow()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())
        formLayout.addRow('Hobbies:', QLineEdit())

        # sử dụng dlgLayout để sắp xếp các widgets trên biểu mẫu (form)
        # layout trong layout
        dlgLayout.addLayout(formLayout)

        # object để đặt dialog buttons
        btns = QDialogButtonBox()

        # thêm 2 buttons chuẩn Ok và Cancel
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()      # giống window.show()
    sys.exit(app.exec_())
```

Kết quả chúng ta nhận được khi chạy mã:
<img src="https://files.realpython.com/media/dialog-style-app.d453259dee67.png" style="display:block; margin-left:auto; margin-right:auto">

GUI chúng ta vừa tạo ra sử dụng `QFormLayout` cho widgets và `QVBoxLayout` cho layout chung của ứng dụng.

### 4. Main Windows
Hầu hết các GUI application sẽ là **Main window-style**. Điều này có nghĩa rằng chúng ta sẽ có [menu bar](https://realpython.com/python-menus-toolbars/) (thanh menu), một số toolbars (thanh công cụ) và status bar (thanh trạng thái) và một widget trung tâm cái là thành phần chính của GUI. Thông thường (it's common) apps của bạn sẽ có một vài dialog windows để thực hiện tác vụ thứ cấp phụ thuộc vào user input.

Bạn sẽ dùng QMainWindow để phát triển Main Window-Style application. Bạn cần kế thừa từ `QMainWindow` để tạo cho mình class GUI chính. Class này có built-in layout cho phép bạn đặt những cái sau:
* **One menu bar** ở trên đỉnh của window. [Menu bar](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qmenubar.html) chứa menu chính của ứng dụng
* **Several toolbars** ở bên cạnh của window. [Toolbars](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtoolbar.html) thích hợp để chứa [tool buttons](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qtoolbutton.html) và một số loại widgets khác như QComboBox, QSpinBox...
* **One central widget** ở tâm của window. Widget trung tâm có thể là bất kỳ loại nào hoặc có thể là  một widget tổng hợp.
* **Several dock widgets** nằm xung quanh **central widget**. [Dock widgets](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qdockwidget.html) là các windows nhỏ và có thể di chuyển.
* **One status bar** nằm ở cuối window. [Status bar](https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtwidgets/qstatusbar.html) hiển thị thông tin về trạng thái của ứng dụng.

Bạn không thể tạo một main window mà không có **central widget**. Bạn phải có central widget ngay cả khi nó là placeholder. Bạn có thể sử dụng `QWidget` object làm central widget. Bạn có thể đặt main window's central widget với method `.setCentralWidget()`. Layout của main window chỉ cho phép duy nhất 1 central widget, tuy nhiên nó có thể là widget tổng hợp.

Ví dụ sau trình bày cách sử dụng `QMainWindow` để tạo Main Window-style application:
```python
# Filename: main_window.py

"""Main Window-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar

# tạo class window kế thừa từ QMainWindow
class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        # set title
        self.setWindowTitle('QMainWindow')
        # set central widget là QLabel
        self.setCentralWidget(QLabel("I'm the Central Widget"))
        # các private methods để tạo các GUI elements
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
```

Đây chính là kết quả của đoạn mã trên
<img src="https://files.realpython.com/media/main-window-app.53142a356307.png" style="display:block; margin-left:auto; margin-right:auto">

Bạn có thể thấy Main Window-style application có các thành phần sau:
* Main menu gọi là *Menu*
* Toolbar với tool button *Exit*
* Central widget (`QLabel` object)
* Status bar ở đáy của window

### 5. Applications
Class cơ bản nhất bạn sẽ sử dụng khi phát triển PyQt GUI application là `QApplication`. Nó quản lý các luồng kiểm soát của ứng dụng (control flow) cũng như các cài đặt chính. Trong PyQt bất cứ instance nào của `QApplication` được xem là **application**.  Mỗi PyQt GUI application phải có một `QApplication` object. Một số nhiệm vụ của `QApplication` object bao gồm:
* Xử lý khởi tạo và kết thúc
* Cung cấp event loop (vòng lặp sự kiện) và xử lý sự kiện
* Xử lý hầu hết các cài đặt trên toàn hệ thống (system-wide) và trên toàn ứng dụng (application-wide)
* Cung cấp truy cập đến thông tin tổng như thư mục của ứng dụng, kích thước màn hình...
* Truyền đối số vào command line
* Xác định hình dáng của application
* Providing localization capabilities

Trên đây là một số nhiệm vụ chính của `QApplication`. 

### 6. Event Loops (vòng lặp sự kiện)
Các GUI application là **event-driven** (hướng sự kiện). Điều này có nghĩa rằng các hàm và phương thức được thực thi để phản hồi hanh động của người dùng như nhấn buttons, chọn item từ combo box, nhập hoặc update văn bản trong text edit, nhận phím trên bàn phím... Những hành động này của người dùng thường gọi chung là **events (sự kiện)**.

Events thường được xử lý bằng **event loop** hay **main loop**. Even loop là vòng lặp vô hạn (infinite loop) trong đó tất cả các events từ người dùng, hệ thống và bất kỳ nguồn nào khác được xử lý và gửi đi. Event loop đợi event xảy ra sau đó thực hiện một số nhiệm vụ (task). Event loop tiếp tục hoạt động cho đến khi application dừng lại. 

Event loop được sử dụng bởi tất cả GUI applications. Event loop là một loại vòng lặp vô hạn cais mà chờ sự kiện xảy ra. Nếu sự kiện xảy ra vòng lặp sẽ kiểm tra đó có phải là `Terminate` event. Nếu đúng như vậy application sẽ kết thức. Ngược lại event sẽ được gửi tới application's event queue (firt in first out) cho xử lý khác và vong lặp lại bắt đầu lại từ đầu.

Trong PyQt bạn có thể chạy application's event loop bằng cách gọi `.exec_()` trên `QApplication` object (thường ở cuối chương trình).
> **Chú ý:** `exec_()` dùng cho Python 2 vì trong Python 2 có keyword `exec`. Trong Python 3 không có keyword đó, vì vậy có thể sử dụng cả 2 cách: `exec_()` hoặc `exec()`

**Bạn cần kết nối event với action bạn muốn thực hiện** khi có event (nhấn phím, click chuột...). Trong PyQt5 bạn có thể thiết lập kết nối này bằng cách sử dụng **signals** và **slots** mechanism (cơ chế).

### 7. Signals and Slots
PyQt widget hoạt động như **event-catchers** (bộ bắt sự kiện). Điều này có nghĩa rằng mỗi widget có thể bắt một số events nhất định như mouse clicks, keypresses... Để phản hồi các events đó widgets luôn đưa ra **signal** (tín hiệu) - một loại message để thông báo sự thay đổi trạng thái.

Bản thân **signal** không thực hiện action. Nếu bạn muốn signal kích hoạt action thì cần kết nối signal với **slot**. Slot là hàm hoặc phương thức để thực hiện action bất cứ khi nào connecting signal được đưa ra. Bạn có thể sử dụng bất cứ Python callable (or **callback**) như slot.

Nếu signal được kết nối với slot thì slot sẽ được gọi bất cứ khi nào signal được đưa ra. Nếu signal không được kết nối với bất kỳ slot nào, sẽ không có điều gì xảy ra và signal bị bỏ qua. Dưới đây là một số tính năng hữu ích nhất của cơ chế này:
* Signal có thể được kết nối tới một hoặc nhiều slots
* Signal cũng có thể được kết nối tới signal khác
* Slot có thể được kết nối tới một hoặc nhiều signal

Bạn có thể sử dụng cú pháp (syntax) sau để kết nối signal với slot:
```python
widget.signal.connect(slot_function)
```

Cú pháp này giúp kết nối `slot_function` với `widget.signal`. Bất cứ khi nào signal được đưa ra `slot_fuunction()` sẽ được gọi.

Đoạn mã dưới đây đưa ra ví dụ các sử dụng cơ chế signal và slot:
```python
# Filename: signals_slots.py

"""Signals and slots example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Hello World!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(greeting)  # Connect clicked to greeting()

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
```

Ở đoạn mã trên `greeting()` được sử dụng như slot. Sau đó nó được kết nối với `clicked` signal. Theo cách này bất cứ khi nào người dùng click vào button, `greeting()` sẽ được gọi và `msg` sẽ thay thế giữa `Hello world!` và chuỗi rỗng.

Nếu slot function cần nhận thêm nhiều đối số (arguments) bạn có thể truyền vào chúng bằng cách sử dụng `functools.partial`. Ví dụ bạn có thể thay đổi `greeeting()` như sau:
```python
    """Slot function."""
    if msg.text():
        msg.setText('')
    else:
        msg.setText(f'Hello {who}')
```

Bây giời `greetin()` cần nhận thêm argument gọi là `who`. Nếu bạn muốn kết nối phiên bản mới của `greetin()` đến `btn.clicked` signal, bạn có thể thực hiện như sau:
```python
btn.clicked.connect(functools.partial(greeting, 'World!'))
```

Để đoạn mã trên hoạt động cần import `functools` trước đã. Việc gọi tới `functools.partial()` trả về đối tượng tương tự như gọi `greeting()` với `who='World!'`. Bây giwof người dùng click vào button, tin nhắn `Hello World!` sẽ hiện ra.

> **Chú ý:**
Bạn có thể sử dụng [lambda](https://realpython.com/python-lambda/) để kết nối dignal với slot cần nhiều arguments.

Cơ chế signal, slot chp phép bạn chuyển user event thành hành động thực sự. 

Như vậy chúng ta đã làm quen cới những thành phần quan trọng nhất của PyQt. Bây giờ các bạn có thể bắt tay vào để xây dựng một GUI applicaition cho riêng mình được rồi.

### Tài liệu tham khảo
1. https://realpython.com/python-pyqt-gui-calculator/







