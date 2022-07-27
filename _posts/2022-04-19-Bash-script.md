---
layout: post
mathjax: true
title: "Bash script"
tags: [Linux]
comments: true
---

Trong này là các hướng dẫn cho hệ điều hành Ubuntu.
1. Tại virtual enviroment với `virtualenv`. Trong thư mục chứa project của mình chạy.
```python
python3 -m venv env
```
Nếu ko được thì chạy 
```python
python3 -m pip install --user virtualenv 
hoặc 
sudo apt-get install python3-virtualenv 
```
trước đã.
Activate môi trường, đưngs trong project 
```python 
source env/bin/activate
```
Deactivate môi trường 
```python 
deactivate
```
Xem thêm [link này](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Đóng lại các packages đã dùng
```python
pip freeze > requirements.txt
```
Cài các packages từ file chứa
```python
pip install -r requirements.txt
```
2. Tại virtual environment với conda

Đầu tiên xem cài đặt miniconda tại đây: https://varhowto.com/install-miniconda-ubuntu-20-04/. Ở đây khá đơn giản thay đổi quyền và thực thi bash script.

Sử dụng conda (nhẹ hơn) hoặc anaconda 
```python
conda create --name myenv python=3.5
``` 
Có thể chỉ định phiên bản python
Activate môi trường
```python 
conda activate myenv
```
Deactivate môi trường
```python 
conda deactivate
```
Xem thêm [ở đây](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

Trong Ubuntu, muốn mở anaconda thì làm như sau:
```python
conda activate
```
Lệnh này sẽ vào **base environment**. Nếu cài bản Conda full thay vì miniconda có thể vào giao diện của nó bằng cách nhập tiếp.
Anaconda-navigator

3. Lệnh Curl: 
dùng -O sẽ lấy tên trong đường dẫn để lưu (curl -O link_tải)
dùng -o sẽ set tên cho file được lưu ví dụ (curl -o custom.zip link_tải)

Xem thêm [link này](https://www.hostinger.vn/huong-dan/curl-la-gi-cac-lenh-curl-curl-command-can-biet-trong-linux).

4. Cách thêm các virtual environment vào kernel cho jupyter notebook.
Xem ở [link này](https://queirozf.com/entries/jupyter-kernels-how-to-add-change-remove).

5. Nếu bị lỗi jupyter notebook thì gỡ đi cài lại. Để ý có thể báo lỗi các packages đi kèm không đúng phiên bản. Cài lại các packages đó cho đúng phiên bản rồi cài lại jupyter notebook như [bình thường](https://stackoverflow.com/questions/69809832/ipykernel-jupyter-notebook-labs-cannot-import-name-filefind-from-traitlets).

6. Tạo SSH để kết nối với GitHub hoặc GitLab.
Xem [link này](https://shareprogramming.net/cach-them-ssh-key-vao-github/) và xem thêm docs chính chủ

7. Cách kết nối với server thông qua SSH
Cái này cũng tương tự như dùng cho Github và GitLab 

8. Lệnh tar 

https://www.hostinger.vn/huong-dan/tar-command
https://kb.hostvn.net/vi-d-co-ban-v-lnh-tar-trong-linux_59.html giải thích các flags 

9. Cài đặt zsh 

Zsh: cài đặt và set up
https://dev.to/nicoh/installing-oh-my-zsh-on-ubuntu-362f
https://viblo.asia/p/cai-oh-my-zsh-powerlevel10k-toi-uu-va-su-dung-phim-tat-cho-terminal-ORNZqowM50n#_422-cai-dat-theme-12 

Nếu lệnh conda không dùng được trong zsh thì update rồi init nó. Nên nhớ về base trước (conda deactivate)
```python 
conda update conda
conda init zsh
```
https://github.com/conda/conda/issues/8492 

10. Một số khái niệm 
```python 
.. - parent directory
. - current directory
~ - home directory, ví dụ /home/huytranvan2010
```
11. Lệnh copy 
```pyhton
cp file.txt rename.txt
```
Câu lệnh trên tạo một bản copy của `file.txt` và đặt tên là `rename.txt`, nếu trong thư mục đó tồn tại `rename.txt` rồi thì ghi đè. Nên thực hành luôn thì dễ nhớ.

```python 
cp file1.txt file2.txt path_des
```
sẽ copy tất cả các file vào thư mục `path_des`.

Vừa copy đổi tên luôn 
```python
cp src_path des_path 
```

12. Lệnh move 

```python
mv file1.txt file2.txt des_folder 
```
`des_folder` chỉ cần chỉ ra path đến thư mục sẽ chứa các files được di chuyển. 

Lệnh `mv` cũng có thể được dùng để thay đổi tên file. 
```python
mv old_file new_file
```
Thử luôn, giống như lệnh `cp` nó sẽ ghi đè file cũ nên cẩn thận.

13. Lệnh delete 
```python
rm file1.txt file2.txt 
```
Ví dụ muốn xóa một directory **rỗng** thì dùng câu lệnh sau
```python 
rmdir empty_dir 
```
Nếu dùng `rm empty_dir` sẽ báo lỗi.

14. Lệnh mkdir 
```python 
mkdir dir 
```
Nếu tạo directory tron directory khác thì directory bên ngoài phải tồn tại đã.

15. Lệnh cat 
Lệnh cat (kí hiệu của concatenate - to link tings together, bởi vì nó sẽ in ra tất cả các files được liệt kê lần lượt)
```python
cat file1.txt file2.txt`
```
**Chú ý**: Nó nối liền contents với nhau luôn không có dấu cách giữa nội dung các files.

Thay vì in ra hết output một lần như `cat` có thể dùng lệnh `less` để in ra lần lượt từng page 
```python 
less file1.txt file2.txt
```
sau đó nhấn `:n` để di chuyển đến nội dung file tiếp theo, `:p` để quay lại nội dung trước và `:q` để thoát.

16. Lệnh head khi muốn xem nội dung đầu file (10 rows)
```python 
head file.txt
```

Mặc định hiển thị 10 dòng nếu đủ. Trong trường hợp muốn thay đối số rows muốn hiển thị thì sử dụng **command-line flag**
```python 
head -n 5 file1.txt
```
thay đổi số dòng cần hiển thị. `n` ở đây có nghĩa là numẻ of lines. Thường tất cả các flags được đặt trước filenames.


17. Mẹo nhỏ dùng `tab` để hoàn thành path. nNeeus path mà ambigious thì nhấn `tab` thêm một lần nữa, nó sẽ hiển thị tất cả các paths có thể.

18. Lệnh ls
```python
ls -R
```
- `-R` hiển thị tất cả các file trong tất cả các thư mục
- `F` tương tự như `-R` nhưng thêm đầy đủ đường dẫn và có `*` cho runnable program. 

```python
ls -a
``` 
hiển thị tất cả files và thư mục trong thư mục vào.

```python 
ls -l
```
Hiển thị ngày sửa đổi tên user, hiển thị các quyền, có 9 thông số cho user, group và everyone. Nếu có thêm chữ d là hiển thị cho directory.

19. Để xem command làm gì chungs ta sử dụng command `man` (viết tắt cho manual)
```python 
man head 
```
Lệnh `main` tự động gọi `less` do đó cần nhấn spacebar để di chuyển đến các trang khác và nhấn `:q` để thoát ra.

20. Lệnh tail để in các dòng cuối cùng của file 
```python 
tail file1.txt
```
Có một câu lệnh
```python 
tail -n +6 file1.txt
```
sẽ in ra các dòng bắt đầu từ dòng thứ n trở đi. `+` không có trong câu lệnh head. Xem thêm thông tin [tại đây](https://quantrimang.com/lenh-tail-trong-linux-178005). Nếu muốn xử lý nhiều files thì cần thêm flag `-q`.

21. Câu lệnh cut nếu muốn chọn mốt số lượng cột của file
```python 
cut -f 2-5,8 -d , values
```
ở đây chọn cột từ 2 đến 5 và cột 8, sử dụng dấu phẩy làm sepeerator. `-f` đại diện cho fields để xác định các columns và `-d` đại diện cho delimiter (ví dụ file csv có thể có nhiều loại seperators khác nhau).

22. Lệnh grep sẽ chọn các dòng theo thông tin nhập vào. Lệnh grep cũng tìm kiếm được theo pattern. Một số flags của grep:
- `-c` in ra số lượng dòng khớp 
- `-h` không tin ra tên files khi tìm kiếm nhiều files 
- `-i` bỏ qua phân biệt hoa thường (ví dụ "anh" với "Anh" như nhau)
- `-l` in tên các files chứa các thông tin khớp
- `-n` in số dòng khớp
- `v` chỉ hiển thị các dòng không khớp

```python
grep từ_tìm_kiếm file_sẽ_tìm_kiếm_trong_này
```

```python
grep -v  molar seasonal/autumn.csv
```
In ra các dòng không chứa `molar`.
**Chú ý**: tốt nhất nên để tất cả các flags trước tên files và search term.

Ví dụ đếm số dòng khớp của mẫu tìm kiếm trong từng file 
```python
grep -c incisor seasonal/autumn.csv seasonal/winter.csv
``` 
22. Muốn lưu đầu ra của command vào file thì dùng `>`
```python 
head -n 5 file1.txt
```
Câu lệnh trên in ra 5 dòng đầu tiên của file1.txt. Nếu muốn lưu chúng vào một file khác ta làm như sau
```python
head -n 5 file1.txt > file2.txt
```
`>` có nghĩa là chuyển hướng (redirect) output của command vào file. `>` hoạt động với tất cả các commands.

Xem ví dụ kết hợp các câu lệnh như sau
```python
head -n 5 file1.txt > file2.txt
tail -n 3 file2.txt
```
Câu lệnh trên sẽ in ra 3 dòng từ 3-5 của file1.txt. Tuy nhiên cách này cần tạo file trung gian. Chúng ta có thể sử dụng **pipe** `|` để kết sử dụng output của câu lệnh trước.
```python
head -n 5 seasonal/summer.csv | tail -n 3
```

Ví dụ kết hợp nhiều commands:
```python
cut -d , -f 1 seasonal/spring.csv | grep -v Date | head -n 10
```
Câu lệnh trên sẽ thực hiện
- Chọn cột đầu tiên
- Loại bỏ các header line chứa từ "Date"
- chọn 10 dòng đầu tiên của actual data.

```python
cut -d , -f 2 seasonal/summer.csv | grep -v Tooth
```
Chọn cột thứ hai rồi chỉ lấy các giá trị không khớp với "Tooth".

23. Đếm số kí tự, số từ và số dòng trong file.
```python 
wc file1.txt
```
wc - word count. Cos theer dungf cacs flag sau `-c`, `-w`, `-l` để lấy các target mong muốn.

24. Liệt ê files trong command không phải cách tốt. Có thể dùng **wildcards** đẻ chỉ định list các files. Hay dùng nhất là `*` đại diện cho khớp với 0 hoặc nhiều kí tự. 
```python
cut -d , -f 1 seasonal/winter.csv seasonal/spring.csv seasonal/summer.csv seasonal/autumn.csv
```
Câu lệnh trên có thể được thu gọn lại như sau:
```python
cut -d , -f 1 seasonal/*
```
Một số wildcard khác như:
- `?` khớp cho 1 kí tự, `201?.txt` sẽ khớp với `2017.txt` hoặc `2018,txt`
- `[...]` sẽ khớp với 1 trong các kí tụ bên trong dấu ngoặc vuông nên `201[78].txt` khớp với `2017.txt` hoặc 2018.txt` nhưng không khớp với `2016.txt`
- `{...}` khớp với bất kì patterns nào bên trong dấu ngoặc nhọn, ví dụ `{*.txt, *.csv}` khớp với bất kì file nào kết thúc với `.txt` hoặc `.csv` nhưng không khớp với file `.pdf`.

25. Để sắp xếp các lines chúng ta dùng lệnh sort. Mặc định nó sắp xếp theo chiều tăng dần của chữ cái, có tùy chọn `-n` để sắp xếp số và `-r` để đảo ngược thứ tự của output, `-b` bỏ qua leading blanks và `-f` nói có tính đến in hoa thường (fold case). Có thể sử dụng trong sự kết hợp với các lệnh như sau:
```python
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort -r
```


Nếu muốn loại bỏ các lines bị lặp lại thì sử dụng lệnh `uniq`. Nếu có thêm flag `-c` sẽ đếm số phần tử duy nhất.
```python
cut -d , -f 2 seasonal/winter.csv | grep -v Tooth | sort | uniq -c
```
Nên nhớ `Ctrl + C` giống với `^C` - thường được ghi trong Unix documentation.

26. Shell lưu thông tin bên trong các biến, một trong số chúng được gọi là **environment variables**, chúng có giá trị trong suốt thời gian. Theo quy ước, teenc ủa environment variable được viết hoa. Ví dụ `HOME` đại diện cho user's home directory, giá trị của nó là `home/repl` (ví dụ tùy thuộc vào user), `PWD` đại diện cho present working directory, `SHELL` đại diện cho shell program nào được sử dụng, giá trị của nó là `/bin/bash/, `USER` là user's id, ví dụ ở đây là `repl`. Để hiển thị tất cả có thể dùng lệnh set trong shell.
```python
set | grep HISTFILESIZE 
```
Xem số lệnh được lưu trong command history.

25. Có thể in ra cá giá trị của variables bằng câu lệnh echo như sau:
```python
echo $USER
```
**Chú ý**: Phải có dấu `$`, nếu không có nó chỉ in ra chữ USER. Điều này ám chỉ mình đang lấy giá trị của biến.

Xem operating system là gì dùng câu lệnh sau
```python
echo $OSTYPE 
```
Một loại biến khác được gọi là **shell variable**, nó giống kiểu local variable trong lập trình. Để tại shell variable chúng ta đơn giản gán giá trị cho chúng
```python
training=seasonal/summer.csv
```
**Chú ý**: không được có dấu cách trước và sau dấu `=`. Quy tắc này cũng vây khi viết bash script. Khi làm điều này xong có thể kiểm tra giá trị của biến
```python
echo $training
```

Các shell variables có thể được dùng trong **loops** (lặp lại nhiều lần). Nếu chạy câu lệnh sau:
```python
for filetype in gif jpg png; do echo $filetype; done
```
nó sẽ in ra
```python
gif
jpg 
png
```
Cấu trúc như này `for` …variable… `in` …list… `; do` …body… `; done`

**Chú ý**: trong phần bo dy phải sử dụng `$filetype` do chúng ta đang lấy giá trị.

Hoàn toàn có thể lặp lại một câu lệnh cho mỗi file như sau:
```python
for filename in seasonal/*.csv; do echo $filename; done
``` 

Có thể sử dụng variable với wildcard expression để lưu list of filenames, ví dụ
```python
dataset=seasonal/*.csv
```
Lúc này có thể hiển thiện tên các file như sau:
```python
for filename in $dataset; do echo $filename; done
```

Chạy nhiều command trong một vòng lặp
```python
for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
```
Ví dụ câu lệnh này sẽ in ra dòng thứ hai của mỗi file.
```python
for file in seasonal/*.csv; do grep 2017-07 $file | tail -n 1; done
```

**Chú ý**: không nên sử dụng khoangr trắng trong tên file. Ví dụ câu leenhj rename file với mv.
```python
mv July 2017.csv 2017 July data.csv
```
Do có khoảng trắng nên sheell sẽ hiểu di chuyển 4 files đến `data.csv`, để tránh điều này cần thêm dấu nháy vào 2 tên files.
```python
mv 'July 2017.csv' '2017 July data.csv'
```

Nên nhớ phần body bên trong loop có thể chứa nhiều commands như sau:
```python
for f in seasonal/*.csv; do echo $f; head -n 2 $f | tail -n 1; done
```
```python
seasonal/autumn.csv
2017-01-05,canine
seasonal/spring.csv
2017-01-25,wisdom
seasonal/summer.csv
2017-01-11,canine
seasonal/winter.csv
2017-01-03,bicuspid
```
Ở đây in ra tên file và lấy ra dòng thứ hai của mỗi file.

26. Làm việc với nano file
```python
nano filename
```
Nó sẽ mở file để edit (hoặc tạo ra nếu nó chưa tồn tại). Sử dụng một số control-key combination sau để thực hiện nhanh một số tác vụ:
- `Ctrl + K`: xóa một dòng 
- `Ctrl + U`: un-delele một dòng
- `Ctrl + O`: lưu file, nhấn Enter để xác nhận tên file
- `Ctrl + X` để thoát 
Bôi đen các từ cần copy (cái này có thể dùng tổ hợp `Alt + M + A` để có thể bắt đầu hightlight từ vị trí cursor), nhấn `Alt + 6` để copy rồi `Ctrl + U` để paste vào chỗ khác.

```python
grep -h -v Tooth spring.csv summer.csv > temp.csv
```
`-h` để không tin ra tên các files, `-v` để lọc lấy các lines không chứa "Tooth` và sẽ redirect đến file `temp.csv`

Ví dụ câu lệnh này sẽ lưu 3 commands cuối cùng vào file `steps.txt`:
```python
history | tail -n 3 > steps.txt
```

Lưu commanf để có thể chạy sau này nên thường viết bash script.
Ví dụ lưu câu lệnh `head-n 1 seasonal/*csv` vào file `headers.sh`, sau này có thể chạy bash script với cú pháp sau:
```python 
bash headers.sh
```
Nó sẽ nói cho shell (ở đây là `bash`, tất nhiên còn có một số loại shell khác nhau zsh) để chạy commands chứa trong script `headers.sh`.

**Chú ý**: shell script không nhất thiết có đuôi là `.sh`, tuy nhiên quy ước nên để `.sh` cho dễ track được.

Ví dụ `all-dates.sh` 
```python
cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq
```
sau đó chạy
```python
bash all-dates.sh > dates.out
```
sẽ sẽ trích xuất tất cả các dates duy nhất từ seasonal data files và lưu chúng vào `dates.out`.

Ví dụ có thể để trống trong shell script với các kí tự `$@` và khi chạy shell script chúng ta sẽ truyền một số files theo sau. Ví dụ shell script `count-records.sh` như sau:
```python
tail -q -n +2 $@ | wc -l
```
có thể chạy lệnh sau
```python
bash count-records.sh seasonal/*.csv > num-records.out
```

Tài liệu xem thêm:
- https://blogd.net/linux/lap-trinh-bash-shell-sieu-co-ban/ 

Cũng có thể sử dụng `$1`, `$2`... để ám chỉ các parameters của command. Bên dưới chúng ta sẽ tạo shell script `column.sh` cái mà chọn một cột từ CSV file khi nguwoif dùng cung cấp tên file như parameter đầu tiên và column như parameter thứ hai
```python
cut -d , -f $2 $1
```
rõ ràng `$2` đi sau `-f` nên nó sẽ đại diện cho column. Bây giờ chúng ta chạy câu lệnh sau:
```python
bash column.sh seasonal/autumn.csv 1
```
27. Viết loops trong shell script
```python
# Print the first and last data records of each file.
for filename in $@
do
    head -n 2 $filename | tail -n 1
    tail -n 1 $filename
done
```
**Chú ý**: không cần thiết phải có thụt dòng, tuy nhiên viết cho dễ nhìn.

Trang web này giúp giải thích regular expression. https://regex101.com/

```python
cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay' | wc -l
```
**Chú ý**: chỗ `'Sydney Carton|Charles Darnay'` là khớp với `'Sydney Carton'` hoặc `'Charles Darnay'`.

`egrep` chính là `grep -E`.

28. Lệnh sed để thay thế văn bản
```python
echo text 's/old_word/new_word'
```
nó sẽ tìm kiếm old_word và thay thế bằng new_word.

29. Bash script

Bash (or shell) scringting là cách rất hay để tự động các tasks lặp lại và có thể tiết kiệm rất nhiều thời gian.

Bash scripts thực thị trong Bash shell interpreter terminal.  Bất kì command nào có thể chạy trong terminal đều có thể chạy trong Bash script. Khi có command hay tập hợp cách commands hay dùng, có thể xem xét viết Bash script để thực thi.

Có một số quy ước (conventions) cần tuần theo để máy tính có thể tìm và thực thi Bash scripts. Mở đầu của script file cần phải là `#!/bin/bash`. Cái này nói cho computer loại trình thông dịch (interpreter) sử dụng cho script. Khi lưu script file, good practice là nên đặt các scripts hay sử dụng trong `~/bin/` directory.

Script files cũng cần có "execute" permission (quyền thực thi) để cho phép chúng được chạy. Để thêm quyền này vào file với filename: `script.sh` dùng
```
chmod +x script.sh
```
Terminal sẽ chạy file mỗi lần nó được mở đẻ load cấu hình. Trên Linux style shells nó là `~/.bashrc`, trên OSX nó là `~/.bash_profile`. Để đảm bảo scripts này trong `~/bin/`, chúng ta cần thêm directory này vào `PATH` trong configuration file:
```python
PATH=~/bin:$PATH
```

Bây giờ bất kì scripts nào trong `~/bin/` directory có thể chạy bất kì đây bằng cách gõ tên của nó. Bên dưới là nội dung file `script.sh`.

Bash script thường bắt đầu với dòng `#!/usr/bash`, nó cho computer biết interpreter nào được sử dụng, ở đây là Bash và nằm ở `/usr/bash`. Mình kiểm tra trên máy mình bằng lệnh `which bash` thì ra `/usr/bin/bash`, kiểm tra zsh bằng `which zsh`. Chú ý cái này tùy thuộc vào máy.

Chạy bash script
```python
bash file1.sh
# hoặc dùng (nếu có #!/usr/bash ở đầu)
./file1.sh
```
Ví dụ bash scipt
```python
#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

# Now save and run!
```
Ở đây dùng `tail -n +2` để bắt đầu lấy từ dòng thứ hai do dòng đầu tiên là tên các cột.

Ví dụ này
```python
#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
```
sẽ thay thế Cherno thành Cherno City và Arda thành Arda United.

Bash script có thể nhận **arguments** để sử dụng bên trong nó bằng cách thêm spacebar sau execution call. ARGV là array của tất cả các arguments. Có thể truy cập vào mỗi argument thông qua kí hiệu `$`, ví dụ `$1` để truy cập vào argument đầu tiên... `$@` và `$*` đưa ra tất cả arguments trong ARGV. `$#` đưa ra chiều dài của arguements. **Điều này có nghĩa là chúng ta truyền arguments khi chạy bash script và chúng ta có thể truy cập vào các arugment này trong bash script thông qua `$` như đã nói.**

```python
# Echo the first and second ARGV arguments
echo $1
echo $2

# Echo out the entire ARGV array
echo $@

# Echo out the size of ARGV
echo $#
```
Khi chạy nên dùng bash
```python
bash file1.sh arg_1 arg_2
```

Dưới đây là ví dụ như vậy
```python
# Echo the first ARGV argument
echo $1

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "cityname".csv
```
30. Basic varibales in Bash
```python
var1="Moon"
echo $var1
```
**Chú ý**: khi lấy giá trị phải có kí tự `$` đứng trước tên biến thì Bash mới hiểu được. Trước và sau `=` không có dấu cách.

**Chú ý**: cách sử dụng single quate `''`, double quote `""` và backticks ``
- `sometext` - Bash sẽ hiểu bên trong là text
```python
now_var='NOW'
var='$now_var'
echo var2
# lúc này khi chạy bash script thì sẽ nhận được $now_var
```
- "sometext" - Bash sẽ hiểu bên trong là text ngoại trừ `$` và ``.
```python
now_var='NOW'
var="$now_var"
echo var2
# lúc này khi chạy bash script thì sẽ nhận được NOW
```
**Chú ý**: Tuy nhiên thường sẽ thêm `()` vào trong tên biến, kiểu như này `var="$(now_var) di choi"`. Đây cũng là một kiểu shell-in-shell
- backticks `` - kiểu chạy shell-in-shell, shell sẽ chạy command và lấy STDOUT để đưa vào biến.
```python
alo = "Date: `date`"
```

Numeric varriable in Bash. Ở đây sẽ sử dụng `expr` (tuwongt ự như `cat`).
**Chú ý**: Giới hạn của `expr`: không sử dụng được cho số thập phân.

Có thể sử dụng `bc` (basic calculator) là công cụ command-line hữu ích (nhấn `quit` để thoát `bc`). Ngoài ra 
```python
echo "5 + 3.5" | bc
```
`bc` có `scale` argument để chỉ số lượng chữ số thập phân cho giá trị trả về.
```python
ech "10 / 3" bc
# trả về 3
```
```python
echo "scale=3; 10 / 3" | bc
```
```python
# trong bash script
var="alo"
var_1=6     # cái này là numeric value
var_2="6"   # cái này là string
```

Chuyển đổi độ F sang độ C, dùng bash script.
```python
# Get first ARGV into variable
temp_f=$1

# Subtract 32, lấy giá trị $
temp_f2=$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9
temp_c=$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the celsius temp
echo $temp_c
```
```python
bash script.sh 108
```

```python
# Create three variables from the temp data files' contents
temp_a=$(cat temps/region_A)
temp_b=$(cat temps/region_B)
temp_c=$(cat temps/region_C)

# Print out the three variables
echo "The three temperatures were $temp_a, $temp_b, and $temp_c"
```
31. Tạo array trong bash
```python
declare -a my_first_array
```
Khởi tạo array mà không thêm các elements. Chú ý có flag `-a`.

```python
my_first_array=(1 2 3)
```
**Chú ý**:
- không có khoảng trắng trước và sau dấu `=`.
- không sử dụng comma giữa các phân từ mà chỉ có khoảng trắng thôi

Lấy tất cả các phần tử của array `array[@]`
```python
my_array=(1 2 3 4)
echo ${my_array[@]}
```
**Chú ý**: phải có dấu ngoặc nhọn quanh tên array.

Lấy length của array thông qua `#array[@]`
```python
echo ${my_array[@]}
```
Lấy element của array
```python
echo ${my_array[2]}
```
Nhớ index đánh từ 0.

Apppend vào array
```python
array+=(elements)
```

Lấy theo slicing
```python
array[@]:N:M
```
Trong đó `N` là starting index, `M` là số elements được trả về.

Tạo associative array (giống dict trong Python)
```python
bdeclare -A city_details``# khởi tạo trước, có -A
city_detauls=([key_1]="Ha Noi" [key_2]="HCM)
```
**Chú ý**: ở đây keys ở trong dấu ngoặc vuông.

Có thể khai báo và khởi tạo cùng lúc luôn:
```python
declare -A city_detauls=([key_1]="Ha Noi" [key_2]="HCM)
```
Truy cập vào các keys bằng cách sử dụng `!`
```python
echo ${!city_details[@]}
```

Ví dụ khởi tạo array trước và thêm phần tử sau:
```python
# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities

# Add (append) the elements
capital_cities+=("Sydney")
capital_cities+=("Albany")
capital_cities+=("Paris")
```

In ra tất cả array và chiều dài của array
```python
# Create a normal array with the mentioned elements using the declare method
declare -a capital_cities

# Add (append) the elements
capital_cities+=("Sydney")
capital_cities+=("Albany")
capital_cities+=("Paris")
```

Tạo associative array
```python
# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82
```

Truy cập vào tất cả các keys của associative array.
```python
# An associative array has been created for you
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out just the keys
echo ${!model_metrics[@]}
```

Tính nhiệt độ trung bình:
```python
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps=($temp_b $temp_c)

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps+=($average_temp)

# Print out the whole array
echo ${region_temps[@]}
```
**Chú ý**: Cần xem lại một lần nữa về cách dùng dấu ngoặc đơn trong chương này.

30. Control Statements in Bash Scripting

Dùng conditionals để kiểm sỏát các commands trong script được chạy. 
- Dùng `if` để bắt đầu conditional, theo sau bởi condition trong square brackets `[  ]`. 
- `then` bắt đầu code sẽ được chạy nếu điều kiện thỏa mãn.
- `else` bắt đầu code sẽ chạy nếu điều kiện không thỏa mãn
- Cuối cùng điều kiện sẽ được kết thúc với ngược của if là `fi`.

```python
if [ CONDITION ]; then
    # SOME CODE
else
    # SOME OTHER CODE
fi
# đại diện cho finish
```
**Chú ý**:
- Nhớ có semicolon `;`
- Nhớ có hai khoảng trắng trong ngoặc vuông

Ví dụ
```python
x="Queen"
if [ $x == "King ]; then
    echo "$x is a King!"
else
    echo "$x is not a King!"
fi
```

**Arithmetic IF statements** có thể sử dụng double-parenthesis structure `(())` như sau:
```python
x=10
if (($x > 5)); then
    echo "$x is more than 5!"
fi
```
Arithmetic IF statements có thể sử dụng ngoặc vuông và arithmetic flag thay vì (rather than) sử dụng <, =, >, != (cái này sử dụng khi dùng `(())`)
- `-eq` for "equal to"
- `-ne` for "not equal to"
- `-lt` for "less than"
- "-lhan"
- "-ge" for "greatee" for "less than or equal to"
- `-gt` for "grater tr than or equal to"

Cùng xem ví dụ sau:
```python
x=10
if [ $x -gt 5 ]; then
    echo "$x is more than 5!"
fi
```

**Một số Bash conditional flags** khác:
- `-e` nếu file tồn tại
- `-s` nếu file tồn tại và có kích thước lớn hơn 0
- `-r` nếu file tồn tại và đọc được
- `-w` nếu file tồn tại và ghi được

Xem thêm ở [link này](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html).

Để sử dụng AND hoặc OR statement trong Bash dùng các kí hiệu sau đây:
- `&&` cho AND
- `||` cho OR

Để sử dụng được multiple conditions (sử dụng AND, OR) chúng ta có thể nối chúng hoặc sử dụng double-square-bracket conditions như sau:
- Nối các điều kiện

```python
x=10
if [ $x -gt 5 ] && [ $x -lt 11 ]; then
    echo "$x is more than 5 and less than 11!"
fi
```
- Sử dụng double square-bracket

```python
x=10
if [[ $x -gt 5 && $x -lt 11 ]]; then
    echo "$x is more than 5 and less than 11!"
fi
```

**Chú ý**: có thể sử dụng luôn command-line programs **trực tiếp** trong conditional, lúc này có thể loại bỏ square brackets
```python
if grep -q Hello words.txt; then
    echo "Hello is inside!"
fi
```
`grep -q` không trả về các lines khớp mà trả về True khi có line nào đó khớp.

IF với shell-within-a-shell
```python
if $(grep -q Hello words.txt); then
    echo "Hello is inside!"
fi
```

**Chú ý:** Khi so sánh các chuỗi, best practive là đặt variable trong quotes `"`. Điều này tránh lỗi nếu variable là null hoặc chứa spaces. 

Ví dụ sử dụng bash script để di chuyển file đến các folder phù hợp dựa vào accuracy được lưu trong mỗi file
```python
# Extract Accuracy from first ARGV element
accuracy=$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -gt 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi
```

**Moving relevant files**
Di chuyển các file các chứa `SRVM_` và `vpt` vào folder `good_logs/`.

```python
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on sfile's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi 
```
**Chú ý**: flag `-q` không trả về các matched lines mà chỉ trả về True nếu có bất kỳ dòng nào khớp.

31. Loops in Bash script
**FOR loop in Bash**

```python
for x in 1 2 3 
do
    echo $x
done 
```

Bash cung cấp cách tạo numeric range gọi là ""brace expansion" `{START..STOP..INCREMENT}` (included STOP nếu có thể):
```python
for x in {1..5..2}
do 
    echo $x
done 
```
Mổ cách thông dụng khác để viết FOR loop là sử dụng **three expression** syntax. Bao quanh three expression là **2 cặp ngoặc đơn**.
```python
for ((x=2;x<=4;x+=2))
do
    echo $x 
done
```

Bash cũng hỗ trợ **pattern-matching expansions** trong for loop với kí hiệu `*` như files trong thư mục. Ví dụ có 2 files trong folder `/books`
```python
for book in books/*
do
    echo $book 
done 
```

**Chú ý**: Tạo shell-in-a-shell cần sử dụng `$()` notation. Ví dụ chỉ in ra những files trong folder `books/` và chứa `air`
```python
for book in $(ls books/ | grep -i 'air')
do
    echo $book 
done 
```

**Vòng lặp WHILE**: 

- sử dụng `while`, 
- xung quanh condition cần có square brackets `[]`, 
- có thể sử dụng flags cho numerical comparison giống IF statements (như `-le`).
- Nhiều điều kiện có thể được nối với nhau hoặc sử dụng double-brackets như IF statement cùng với `&&` (AND) hoặc `||` (OR)

```python
x=1
while [ $x -le 3 ]
do 
    echo $x
    ((x+=1))
done
```
Ở trên phép toán số học trong bash scritp được dùng theo cú pháp `(())`. Bên trong dấu ngoặc không cần thêm `$`.
In ra tên các files trong folder `inherited_folder`. Ở đây in ra relative paths.
```python
# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do  
    # Echo out each file
    echo $file
done
```

Ví dụ di chuyển các Python files trong thư mục `rob_files` chứa `RandomForestClassifier` vào thư mục `to_keep`
```python
# Create a FOR statement on files in directory
for file in robs_files/*.py
do   
    # Create IF statement using grep
    if grep -q 'RandomForestClassifier' $file ; then
        # Move wanted files to to_keep/ folder
        mv $file to_keep/
    fi
done
```

**until**

`until` thì ngược lại so với `while`, nó sẽ lặp lại cho đến khi điều kiện đúng, có nghĩa là điều kiện sai mới thực hiện.

```python
until [ $index -eq 5 ]
do
  echo $index
  index=$((index + 1))
done
```

**CASE statement** thường được sử dụng để thay thế cho IF statement trong trường hợp có nhiều điều kiện và phức tạp (cả TH nhiều IF lồng nhau).

```python
if grep -q 'sydney' $1; then 
    mv $1 sydney/   # di chuyển vào folder
fi 
if grep -q 'melbourne|brisbane' $1; then 
    rm $1   # xóa bỏ
fi 
if grep -q 'canberra' $1; then
    mv $1 "IMPORTANT_$1"    # đổi tên
fi
```

Xây dựng CASE statement: cần xác định được variable và string để khớp (có thể gọi shell-withn-a-shell)

```python
case 'STRINGVAR' in
    PATTERN1)
    COMMAND1;;
    PATTERN2)
    COMMAND2;;
    *)
    DEFAULT COMMAND;;
esac
```

**Chú ý**:
- Ngăn cách giữa pattern và code to run là **close-parenthesis**
- Cần kết thúc commands với hai dấu chấm phấy `;;`
- Có thể sử dụng regex trong `PATTERN` như `Air*`, `*hat*`
- Thường (nhưng không bắt buộc) kết thúc với default command mà chạy khi không có pattern nào được khớp.

Đoạn code phía trên được viết lại với CASE statement như sau:
```python
case $(cat $1) in
    *sydney*)
    mv $1 sydney/ ;;
    *melbourne*|*brisbane*)
    rm $1 ;;
    *canberra*)
    mv $1 "IMPORTANT_$1" ;;
    *)
    echo "No cities found" ;;
esac
```

Ví dụ kiểm tra ngày nhập vào là Weekday hay Weekend.
```python
# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday|Tuesday|Wednesday|Thursday|Friday)
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  *) 
  echo "Not a day!";;
esac
```

Ví dụ duyệt qua các files trong folder. Nếu các file chứa thông tin về tree model thì đưa vào folder `tree_models`, nếu chứa thông tin model `Logistic` hay `KNN` thì xóa các files đó đi.
```python
# Use a FOR loop for each file in 'model_out/'
for file in model_out/*
do
    # Create a CASE statement for each file's contents
    case $(cat $file) in
      # Match on tree and non-tree models
      *"Random Forest"*|*GBM*|*XGBoost*)
      mv $file tree_models/ ;;
      *KNN*|*Logistic*)
      rm $file ;;
      # Create a default
      *) 
      echo "Unknown model in $file" ;;
    esac
done
```

**Functions và animations in Bash**: phần này sẽ giúp chúng ta thực hiện các tác vụ thường xuyên, đã được lên schedule.

anatomy: giải phẫu học 
Cấu trúc của function trong Bash
```python
function_name () {
    #function_code
    return #sỏmthing
}
```
**Chú ý**: return ở đây không hẳn giống với các ngôn ngữ khác 

Có cách thay thế (alaternate way) để viết function trong Bash:
```python
function function_name {
    #function_code
    return #something
}
```
Sự khác biệt ở đây là sử dụng từ `function` ở đầu và có thể loại bỏ parathesis (nhiều người vẫn để lại).

Ví dụ
```python
function print_hello() {
    echo "Hello world!"
}

print_hello
```
Để gọi function trong Bash chỉ việc viết tên của function ra như ví dụ trên.

Ví dụ hàm chuyển Fahrenheit to Celsius 
```python
temp_f=30
function convert_temp () {
    temp_c=$(echo "scale=2; ($temp_f - 32) * 5 / 9" | bc)
}
convert_temp # call the function
```

```python
# Create function
function upload_to_cloud () {
  # Loop through files with glob expansion
  for file in output_dir/*results*
  do
    # Echo that they are being uploaded
    echo "Uploading $file to cloud"
  done
}

# Call the function
upload_to_cloud

```

Ví dụ lấy ra ngày hiện tại
```python
# Create function
function what_day_is_it {

  # Parse the results of date
  current_day=$(date | cut -d " " -f1)

  # Echo the result
  echo $current_day
}

# Call the function
what_day_is_it

```
Ở đây có sử dụng thêm câu lệnh `cut`. Xem thêm [tại đây](https://hocdevops.com/commands/lenh-cut-trong-linux/).

**Passing arguments into Bassh functions**
- Truyền arguments vào functions tương tự như truyền vào script, sử dụng kí hiệu `$1`. Cungx ta cũng truy cập vào `ARGV` properties mà trước đây đã đề cập:
- Mỗi argument có thể được truy cập thông qua `$1`, `$2`
- `$@` và `$*` trả về tất cả arguments trong `ARGV`
- `$#` trả về chiều dài của arguments 

```python 
function print_filename {
    echo "The first file was $1"
    for file in $@
    do 
        echo "This file has name $file"
    done
}
print_filename "LORT.txt" "mod.txt" "A.py"
# chỗ này nhận arguments như bình thường
```
Scope: thể hiện nơi nào varibale có thể được truy cập
- Global scope
- Local scopr
**Chú ý**: không giống như các ngôn ngữ lập trình khác, tất cả các biến trong Bash đều có global scope theo mặc định. Điều này có thể dẫn đến một số rủi ro không mong muốn. Để giới hạn scope trong Bash functions có thể sử dụng keyword `local`
```python
function print_filename {
    local first_name=$1
}
print_name "LOTR.txt" "model.txt"
echo $file_name
# đầu ra là blank line do bên trên dùng local để giới hạn scope của biến
# Đâu ra là blank line do first_name sẽ được gán cho global first ARGV element `$1` khi chạy scrpit. Ví dụ chạy bash script.sh thì không có arguments rồi.
```
`return` option trong Bash chỉ có ý nghĩa các định hàm thành công (0) hoặc thất bại (các giá trị từ 1-255). Nó được chấp nhận trong global variable `$?`, do đó có thể:
- Gán cho global varibale
- Hoặc dùng `echo` đưa ra cái chúng ta mong muốn (trong dòng cuối của hàm) và lấy chúng bằng cách sử udnjg shell-within-a-shell 

```python 
function convert_temp {
    echo $(echo "scale=2; ($1 - 32) * 5 / 9" | bc)
}
converted=$(convert_temp 30)
echo "30F in Celsius is $converted C"
```

Xác định % dựa trên hai số:
```python
# Create a function 
function return_percentage () {

  # Calculate the percentage using bc
  percent=$(echo "scale=2; 100 * $1 / $2" | bc)

  # Return the calculated percentage
  echo $percent
}

# Call the function with 456 and 632 and echo the result
return_test=$(return_percentage 456 632)
echo "456 out of 632 as a percent is $return_test%"
```

```python
# Create a function
function get_number_wins () {

  # Filter aggregate results by argument
  win_stats=$(cat soccer_scores.csv | cut -d "," -f2 | egrep -v 'Winner'| sort | uniq -c | egrep "$1")

}

# Call the function with specified argument
get_number_wins "Etar"

# Print out the global variable
echo "The aggregated stats are: $win_stats"
```
Tính tổng của array:
```python
# Create a function with a local base variable
function sum_array () {
  local sum=0
  # Loop through, adding to base variable
  for number in "$@"
  do
    sum=$(echo "$sum + $number" | bc)
  done
  # Echo back the result
  echo $sum
  }
# Call function with array
test_array=(14 12 23.5 16 19.34)
total=$(sum_array "${test_array[@]}")
echo "The total sum of the test array is $total"
```
**Scheduling your scripts with Cron - Lên kế hoặc với Cron**

Một số trường hợp mà scheduling scripts có thể hữu ích:
- Các tasks thường xuyên cần được thực hiện: hàng ngày, hàng tuần, nhiều lần trong ngày
- Tối ưu tài nguyên (ví dụ chạy vào buổi sáng sớm...)

Scheduling scripts với `cron` (bắt nguồn từ Greek là chronos) là kỹ năng cần thiết trong modern data infrastructure. Nó được thúc đẩy bởi cái gọi là `crontab`, đây là file chứa `cronjobs` nó nói cho `crontab` biết code nào được chạy và khi nào.

Có thể xem những lịch trình (`cronjobs`) nào đã được lập trình 
```python
crontab -l`
```

Dưới đây là cách tạo `cronjob` bên trong `crontab` file. Có thể tạo nhiều cronjobs, mỗi cái một dòng. Xem thêm link [tại đây](https://en.wikipedia.org/wiki/Cron) để rõ hơn. `*` có nghĩa là every. Cùng xem một số ví dụ
```python
5 1 * * * bash myscript.sh
```
- Minutes star là 5(5 minutes past the hour). Hours star là 1 (sau 1 am). 3 dấu * cuối nghĩa là mỗi ngày, mỗi tháng. Điều này có nghĩa là chạy mỗi ngày vào lúc 1:05am.
```python
15 14 * * 7 bash myscirp.sh
```
- Minutes star là 15 (15 minutes past the hour). Hours star là 14 (sau 2 pm). 2 dấu * tiếp theo là mỗi ngày trong thánh, mỗi tháng trong năm. * cuối cùng là ngày 7 (on Sundays). Điều này có nghĩa là chạy script vào lúc 2:15pm mỗi chủ nhật.

Nếu muốn chạy nhiều lần trong ngày hoặc sau mỗi lần tăng nào đó:
- Sử dụng dấu phảy `,` cho các khoảng cụ thể
```python
15,30,45 * * * *
```
sẽ chạy ở phut 15, 30, 35 của mỗi giờ được xác định bởi dấu * thứ hai. Ở đây là mỗi giờ, mỗi ngày...
- Dùng slash `/` cho **every X increment**
```python
*/15 * * * * 
```
nó sẽ chạy sau mỗi 15 phút cho mỗi giờ...

Ví dụ thử lên lịch trình chạy script `extract_data.sh` mỗi buổi sáng vào lúc 1.30am. Các bước thực hiện như sau:
- Trên terminal nhập `crontab -e` để chỉnh sửa list of cronjobs. Nếu trong lần đầu tiên nó có thể hỏi editor muốn sử dụng, chọn `nano` cho đơn giản
- Tạo cronjob trên blank line
```python
30 1 * * * bash extract_data.sh
```
- Thoát editor vào lưu lại crontab 
- Kiểm tra lại xem đã thêm cronjob với câu lệnh sau
```python
crontab -l
```

Có ví dụ sau đây
```python
15 * * * 6,7 bash script.sh
```
sẽ chạy ở phút thứ 15 của mỗi giờ vào ngày thứ bảy và chủ nhật.

Đôi khi phải chạy lại bash script vào mỗi sáng (có lịch test code chẳng hạn), dùng `cron` sẽ giúp ích nhiều. Trang web có thể hỗ trợ chúng ta xây dựng cronb.

```python
# Create a schedule for 30 minutes past 2am every day
30 2 * * * bash script1.sh

# Create a schedule for every 15, 30 and 45 minutes past the hour
15,30,35 * * * * bash script2.sh

# Create a schedule for 11.30pm on Sunday evening, every week
30 11 * * * bash script3.sh
```
Nghĩa là chúng ta lưu các dòng trên vào một bash script và chạy nó.

Kiểm tra xem có tồn tại `cronjobs` nào không
```python 
crontab -l
```
Muốn lập lịch trình chạy cho các script nhì nhập
```python
crontab -e
```
sau đó mình sẽ thêm các dòng để schedule cho các bash script, ví dụ như
```python
30 2 * * * bash anh.sh
```
Để chạy lúc 2:30am every day cho bash script.

**Aliases trong Bash script**

Có thể setup aliases (tham chiếu) cho bash script bên trong `.bashrc` hoặc `.bash_profile` file để cho phép gọi scripts mà không cần tên file đầy đủ. Ví dụ có `saycolors.sh` script, chúng ta có thể alias (tham chiếu) nó đến từ từ `saycolors` bằng cách sử dụng cú pháp sau:
```python
alias saycolors='./saycolors.sh'
```
Cái này là thay đổi trong file trên.
Thâm chí chúng ta có thể thêm đối số đầu vào tiêu chuẩn (standard input arguments) đến alias của nó. Ví dụ nếu chúng ta luôn muốn "green" được thêm vào làm input đầu tiên của scripts `saycolors` chúng ta sẽ thay đổi như sau:
```python
alias saycolors='./saycolors.sh "green"'
```
Tất nhiên lúc nào có thể truy cập "green" thông qua `$1`.

```python
#!/bin/bash
first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=0
greeting_limit=$1
while [ $greeting_occasion -lt $greeting_limit ]
do
  if [ $greeting_occasion -lt 1 ]
  then
    echo $first_greeting
  else
    echo $later_greeting
  fi
  greeting_occasion=$((greeting_occasion + 1))
done
```

Thay đổi alias trong `~/.bashrc`
```python
$ alias greet3="./script.sh 3"
$ greet3
```

**Inputs trong Bash script**

Để làm bash scripts hữu ích hơn, chúng ta cần có khả năng truy cập data bên ngoài bash script. 
- Cách đầu tiên là nhắc nhở user nhập input. Để làm điều này chúng ta dùng `read` syntax. Để hỏi người dùng nhập input và lưu vào `number` variable, chúng ta sử dụng code sau:
```python
echo "Guess a number"
read number
echo "You guessed $number"
```


Dưới đây là một ví dụ
```python
#!/bin/bash
firstline=$(head -n 1 source/changelog.md)
read -a splitfirstline <<< $firstline
version=${splitfirstline[1]}
echo $version
echo 'Do you want to continue? (enter "1" for yes, "0" for no)'
read versioncontinue
if [ $versioncontinue -eq 1 ];
then
  for filename in source/*
  do
    echo $filename
    if [ "$filename" == "source/secretinfo.md"]
    then
      echo "Not copying" $filename
    else
      echo "Copying" $filename
      cp $filename build/.
    fi
  done
  cd build/
  echo "Build version $version contains:"
  ls
  cd ..
else
  echo "Please come back when you are ready"
fi
```

- https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements


Xem thêm:
- Đọc một số dòng của file http://www.linfo.org/head.html
- Chia dòng thành aray http://linuxcommand.org/lc3_man_pages/readh.html

ĐỌc thêm một số link hướng dẫn hay:
- https://www.codecademy.com/article/command-line-interface
- https://www.codecademy.com/article/command-line-setup
- https://www.codecademy.com/article/git-setup
- https://www.codecademy.com/article/ready-command-line-commands
- https://www.codecademy.com/article/command-line-commands
- https://www.codecademy.com/article/f1-u3-cli-setup

**Cài đặt SVN cho ubuntu**:
- https://www.vultr.com/docs/install-apache-subversion-on-ubuntu-20-04/
- https://blog.eldernode.com/install-subversion-on-ubuntu/
- https://meetawaiszafar.medium.com/install-configure-svn-server-on-ubuntu-20-04-with-apache2-6dcd7d9a49e9


## Sử dụng curl và wget

https://freetuts.net/cai-dat-curl-tren-linux-3314.html
https://blogd.net/linux/tai-file-tren-linux-dung-wget-va-curl/ 

Curl: 
dùng -O sẽ lấy tên trong đường dẫn để lưu (curl -O link_tải)
dùng -o sẽ set tên cho file được lưu ví dụ (curl -o custom.zip link_tải)

Ví dụ
```python
!curl -O https:/ /ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
```

nó sẽ lưu file với tên trong link tải.

## Sử dụng tar để nén và giải nén

Link này https://phptravels.vn/chuan-tat-tan-tat-ve-nen-va-giai-nen-zip-gzip-tar-rar-7-zip-tren-linux-lenh-tar-trong-linux-xac-minh/ có giới thiệu về các flags đọc dễ hiểu hơn.


https://www.hostinger.vn/huong-dan/tar-command

## Lệnh cat

https://quantrimang.com/lenh-cat-trong-linux-181056#:~:text=L%E1%BB%87nh%20cat%20(vi%E1%BA%BFt%20t%E1%BA%AFt%20c%E1%BB%A7a,ra%20trong%20terminal%20ho%E1%BA%B7c%20file.
