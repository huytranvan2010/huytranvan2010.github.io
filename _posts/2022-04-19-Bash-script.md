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
```python
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

Ngoài việc copy bằng `cp` chúng ta có thể sử dụng lệnh `rsync` (mình gặp trong một số code). Có thể xem thêm ở [link này](https://kblinux.com/13-lenh-rsync-trong-linux-ban-nen-biet/) và [ở đây](https://kblinux.com/13-lenh-rsync-trong-linux-ban-nen-biet/)
```python
rsync -avzh alo des
```
Như ví dụ trên sẽ copy cả thư mục `alo` vào thư mục `des`. Tuy nhiên nếu thực hiện như sau
```python
rsync -avzh alo/ des
```
thì nó chỉ copy các thư mục và files bên trong `alo` vào `des` (lúc này trong `des` không có `alo`)
Cứ dùng `-avzh` cho đơn giản:
- `a`: cho phép copy dữ liệu recursively, đồng thời giữ nguyên được tất cả các thông số của thư mục và file
- `v`: verbose 
- `h`: đưa ra output người đọc được
- `z`: nén dữ liệu khi transfer, tiết kiệm băng thông tuy nhiên tốn thêm một chút thời gian
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


17. Mẹo nhỏ dùng `tab` để hoàn thành path. Nếu path mà ambigious thì nhấn `tab` thêm một lần nữa, nó sẽ hiển thị tất cả các paths có thể.

18. Lệnh ls liệt kê mọi thứ trong directory
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

19. Để xem command làm gì chúng ta sử dụng command `man` (viết tắt cho manual)
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
- `-v` chỉ hiển thị các dòng **không khớp**
- `q` trả về True nếu có bất kỳ dòng nào khớp


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

**Chú ý**: không nên sử dụng khoảng trắng trong tên file. Ví dụ câu lệnh rename file với mv.
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
`-h` để không tin ra tên các files, `-v` để lọc lấy các lines không chứa "Tooth" và sẽ redirect đến file `temp.csv`

Ví dụ câu lệnh này sẽ lưu 3 commands cuối cùng vào file `steps.txt`:
```python
history | tail -n 3 > steps.txt
```
**Chú ý**: flag `-n` trong câu lệnh tail ám chỉ lines

Lưu command để có thể chạy sau này nên thường viết bash script.
Ví dụ lưu câu lệnh `head -n 1 seasonal/*csv` vào file `headers.sh`, sau này có thể chạy bash script với cú pháp sau:
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

## Bash script

Bash (or shell) scripting là cách rất hay để tự động các tasks lặp lại và có thể tiết kiệm rất nhiều thời gian.

Bash scripts thực thị trong Bash shell interpreter terminal.  Bất kì command nào có thể chạy trong terminal đều có thể chạy trong Bash script. Khi có command hay tập hợp cách commands hay dùng, có thể xem xét viết Bash script để thực thi.

Có một số quy ước (conventions) cần tuần theo để máy tính có thể tìm và thực thi Bash scripts. Mở đầu của script file cần phải là `#!/bin/bash`. Cái này nói cho computer loại trình thông dịch (interpreter) sử dụng cho script. Khi lưu script file, good practice là nên đặt các scripts hay sử dụng trong `~/bin/` directory.

Script files cũng cần có "execute" permission (quyền thực thi) để cho phép chúng được chạy. Để thêm quyền này vào file với filename: `script.sh` dùng
```python
chmod +x script.sh
```

Terminal sẽ chạy file mỗi lần nó được mở đẻ load cấu hình. Trên Linux style shells nó là `~/.bashrc`, trên OSX nó là `~/.bash_profile`. Để đảm bảo scripts này trong `~/bin/`, chúng ta cần thêm directory này vào `PATH` trong configuration file:
```python
PATH=~/bin:$PATH
```
**Chú ý**: PATH chính là environtment variable, nó là list danh sách các directory và khi một câu lệnh nào được thực thi, nó sẽ đi tìm kiếm trên danh sách đó gặp directory nào đầu tiên phù hợp thì lấy.

Bây giờ bất kì scripts nào trong `~/bin/` directory có thể chạy bất kì đây bằng cách gõ tên của nó. Bên dưới là nội dung file `script.sh`.

Bash script thường bắt đầu với dòng `#!/usr/bash`, nó cho computer biết interpreter nào được sử dụng, ở đây là Bash và nằm ở `/usr/bash`. Mình kiểm tra trên máy mình bằng lệnh `which bash` thì ra `/usr/bin/bash`, kiểm tra zsh bằng `which zsh`. Chú ý cái này tùy thuộc vào máy.

**Chạy bash script**
```python
bash file1.sh
# hoặc dùng (nếu có #!/usr/bash ở đầu)
./file1.sh  # nhiều khi cần cấp quyền cho nó chmod +x .file1.sh
```
Ví dụ bash scipt
```python
#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

# Now save and run!
```
Ở đây dùng `tail -n +2` để bắt đầu lấy từ dòng thứ hai do dòng đầu tiên là tên các cột. Lệnh `cut` sẽ lấy cột thứ hai (các cột ngăn cách nhau bằng dấu phẩy).

Ví dụ này
```python
#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
```
sẽ thay thế Cherno thành Cherno City và Arda thành Arda United.

Bash script có thể nhận **arguments** để sử dụng bên trong nó bằng cách thêm spacebar sau execution call. **ARGV** là array của tất cả các arguments. Có thể truy cập vào mỗi argument thông qua kí hiệu `$`, ví dụ `$1` để truy cập vào argument đầu tiên... `$@` và `$*` đưa ra tất cả arguments trong ARGV. `$#` đưa ra chiều dài của arguements. **Điều này có nghĩa là chúng ta truyền arguments khi chạy bash script và chúng ta có thể truy cập vào các arugment này trong bash script thông qua `$` như đã nói.**

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
## Variables in Bash Scripting
### Basic varibales in Bash
```python
var1="Moon"
echo $var1
```
**Chú ý**: khi lấy giá trị phải có kí tự `$` đứng trước tên biến thì Bash mới hiểu được. Trước và sau `=` không có dấu cách.

**Chú ý**: cách sử dụng single quate `''`, double quote `""` và backticks ``
- 'sometext' - Bash sẽ hiểu bên trong là text
```python
now_var='NOW'
var='$now_var'
echo var2
# lúc này khi chạy bash script thì sẽ nhận được $now_var do trong dấu nháy đơn nó coi là text
```
- "sometext" - Bash sẽ hiểu bên trong là text ngoại trừ `$` và ``.
```python
now_var='NOW'
var="$now_var"
echo var2
# lúc này khi chạy bash script thì sẽ nhận được NOW vì nó lấy giá trị của $now_var là NOW
```
**Chú ý**: Good practice thường sẽ thêm `{}` vào trong tên biến, kiểu như này `var="${now_var} di choi"` để dễ quan sát
- backticks `` - kiểu chạy **shell-in-shell**, shell sẽ chạy command và lấy STDOUT để đưa vào biến. Ở đây nó lấy gía trị của `date` trước.
```python
alo="Date: `date`"
echo $alo
# output: Date: Sat 30 Jul 2022 02:30:22 PM +07
```
**Chú ý**: có thể chạy shell-in-shell** với `$(command)` nó sẽ có tác dụng tương tự như backticks ``
```python
alo="Date: $(date)"
echo $alo
# output: Date: Sat 30 Jul 2022 02:35:15 PM +07
```

### Numeric variable in Bash

Số không được hỗ trợ chính thức trong terminal. Ở đây sẽ sử dụng `expr` (tương tự như `cat` hoặc `grep`), hữu ích cho numeric variables.
```python
expr 3 + 5
# output: 8
```
Tuy nhiên chạy như sau
```python
expr 3+5
# output 3+5
```
Chú ý với `expr` lại cần cách nhau bằng khoảng trắng.
**Chú ý**: Giới hạn của `expr`: **không sử dụng được cho số thập phân.**
```python
expr 3.1 + 5
# output: expr: non-integer argument
```

Có thể sử dụng `bc` (basic calculator) là công cụ command-line hữu ích (nhấn `quit` để thoát `bc`). Trên terminal nhập `bc` để gọi chương trình, sau đó nhập vào các phép toán là ok.

Ngoài ra có thể sử dụng `bc` mà không cần mở chương trình thông qua pipe vì nó nhận vào aruguments là các số và operations.
```python
echo "5 + 3.5" | bc
#output: 8.5
```

`bc` có `scale` argument hữu ích để chỉ số lượng chữ số thập phân cho giá trị trả về.

```python
ech "10 / 3" bc
# output: 3
```

```python
echo "scale=2; 10 / 3" | bc
#output: 3.33
```
**Chú ý**: phải có `;` ngẵn cách phần scale argument và operations.

Có thể gán numeric variable như sau (Không để dấu nháy để phân biệt với string)
```python
# trong bash script
var="alo"
var_1=6     # cái này là numeric value
var_2="6"   # cái này là string
```
Phần trước chúng ta tìm hiểu `$(command)` là shell-in-shell. Bây giờ với double bracket nó sẽ thực hiện phép toán
```python
expr 2 + 3
echo $((2+3))   # cái này hiện đã hỗ trợ số thập phân
#output: 5
# 5
```

Sẽ kết hợp shell-in-shell `$()` với `bc` xem sao
```python
a1=12.1
a2=12.2
echo "Total score is $(echo $a1 + $a2 | bc)"
# output: Total score is 24.3
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
temp_a=$(cat temps/region_A)  # shell-in-shell $(), ở đây đang lấy content
temp_b=$(cat temps/region_B)
temp_c=$(cat temps/region_C)

# Print out the three variables
echo "The three temperatures were $temp_a, $temp_b, and $temp_c"
```

### Tạo array trong bash
https://linuxconfig.org/how-to-use-arrays-in-bash-script
Có 2 cách tạo array với index số trong Bash như sau:
1. Tạo array mà chưa có elements nào
```python
declare -a my_first_array
echo my_first_array
#output: empty line
```
Chú ý có flag `-a`.
Sau đó có thể thêm elements như này
```python
my_first_array+=(1)
my_first_array+=(3)
```
2. Tạo array với element luôn
```python
arr1=(1 2 3)
echo $arr1
# output: 1 2 3
```
**Chú ý**:
- không có khoảng trắng trước và sau dấu `=`.
- không sử dụng comma `,` giữa các phân từ mà chỉ có khoảng trắng thôi

though do note: mặc dù vậy hãy lưu ý

**Array có một số tính chất:**
- Lấy tất cả các phần tử của array `array[@]`
```python
my_array=(1 2 3 4)
echo ${my_array[@]}
# mình test thì vẫn dùng được echo $my_array[@]
```
**Chú ý**: phải có dấu ngoặc nhọn quanh tên array nếu dùng Bash (dùng zsh có thể không cần)

- Lấy length của array thông qua `#array[@]`
```python
my_array=(1 2 3 4)
echo ${#my_array[@]}
# output: 4
# Vẫn có thể bỏ đi {} được nếu dùng zsh thay vì Bash
```

- Lấy element của array
```python
echo ${my_array[2]}
```
Nhớ index đánh từ 0 trong Bash vẫn phải có dấu ngoặc nhọn.

- Append vào array
```python
array+=(elements)
```
**Chú ý**: phải đặt element bên trong `()` nếu không sẽ được kết quả không mong muốn (nó thêm vào phần tử đầu tiên, kiểu concatenate)
- Lấy theo slicing
```python
array[@]:N:M
```
Trong đó `N` là starting index, `M` là số elements được trả về.
```python
arr=(1 2 3 4)
echo ${arr[@]:0:2}
#output: 1 2 # bắt đầu từ index 0 lấy 2 phần tử
```
- Thay đổi giá trị phần tử tại vị trí nào đó
```python
arr=(1 2 3 4)
arr[4]=30
echo ${arr[4]}
# output: 30
```
Một loại array thứ hai nữa trong Bas là **associative array** (giống dict trong Python) (dùng key để truy cập)
```python
bdeclare -A city_details# khởi tạo trước, có -A
city_detauls=([key_1]="Ha Noi" [key_2]="HCM")  # thêm elements
echo ${city_detauls[key_1]}
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

## Control Statements in Bash Scripting

Dùng conditionals để kiểm soát các commands trong script được chạy. 
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
if [ $x == "King" ]; then
    echo "$x is a King!"
else
    echo "$x is not a King!"
fi
```
Có thể dùng `!=` để kiểm tra không bằng.

**Arithmetic IF statements** có thể sử dụng **double-parenthesis** structure `(())` như sau:
```python
x=10
if (($x > 5)); then
    echo "$x is more than 5!"
fi
```
Arithmetic IF statements có thể sử dụng ngoặc vuông (square brackets nhưng bình thường) và arithmetic flag thay vì (rather than) sử dụng <, =, >, != (cái này sử dụng khi dùng `(())`)
- `-eq` for "equal to"
- `-ne` for "not equal to"
- `-lt` for "less than"
- "-lhan"
- "-ge" for "greatee" for "less than or equal to"
- `-gt` for "grater tr than or equal to"

Mình kiểm tra thấy vẫn dùng các dấu <, >, = với quare brackets, nhưng thôi cứ dùng flag cho numeriacal condition trong square brackets.

Cùng xem ví dụ sau:
```python
x=10
if [ $x -gt 5 ]; then
    echo "$x is more than 5!"
fi
```

**Một số Bash conditional flags** hỗ trợ cho file khác:
- `-e` nếu file tồn tại
- `-s` nếu file tồn tại và có kích thước lớn hơn 0
- `-r` nếu file tồn tại và đọc được
- `-w` nếu file tồn tại và ghi được

Xem thêm ở [link này](https://www.gnu.org/software/bash/manual/html_node/Bash-Conditional-Expressions.html).

Ngoài ra có flag `-d` để kiểm tra có phải directory hay không, `-f` để kiểm tra có phải file hay không, `!` để kiểm tra có phải empty string hay không

```python
#!/bin/bash

x=""
if [ ! ${x} ]; then     # kiểm tra #{x} có empty hay không
    echo "$x is empty"
else 
    echo "$x is not empty"
fi
```

Để sử dụng AND hoặc OR statement trong Bash dùng các kí hiệu sau đây:
- `&&` cho AND
- `||` cho OR

Để sử dụng được multiple conditions (sử dụng AND, OR) chúng ta có thể nối chúng hoặc sử dụng double-square-bracket conditions như sau:
- Nối các điều kiện (vẫn dùng single brackets)

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

Sử dụng shell-within-a-shell bên trong If condition statement
```python
if $(grep -q Hello words.txt); then
    echo "Hello is inside!"
fi
```

**Chú ý:** Khi so sánh các chuỗi, best practive là đặt variable trong quotes `""`. Điều này tránh lỗi nếu variable là null hoặc chứa spaces. 

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

### Loops in Bash script
**FOR loop in Bash**

```python
for x in 1 2 3 
do
    echo $x
done 
```

Bash cung cấp cách tạo numeric range gọi là **brace expansion** `{START..STOP..INCREMENT}` (included STOP nếu có thể):
```python
for x in {1..5..2}
do 
    echo $x
done 
```
Một cách thông dụng khác để viết FOR loop là sử dụng **three expression** syntax. Bao quanh three expression là **2 cặp ngoặc đơn**.
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
    echo $book  # ở đây in cả đường dẫn, ví dụ books.a.txt
done 
```

**Chú ý**: Tạo shell-in-a-shell cần sử dụng `$()` notation. Ví dụ chỉ in ra những files trong folder `books/` và chứa `air`
```python
for book in $(ls books/ | grep -i 'air')  # chỗ này books/ cũng thể hiện là directory rồi
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
  # nhớ bên trên $((2+3)) cái này sẽ thực hiện tính toán với expr
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

Xây dựng CASE statement: cần xác định được variable và string để khớp (có thể gọi shell-withn-a-shell). Xem thêm [ở đây](https://linuxize.com/post/bash-case-statement/) hoặc [ở đây](https://phoenixnap.com/kb/bash-case-statement#:~:text=The%20case%20statement%20starts%20with,the%20case%20keyword%20backwards%20%2D%20esac%20.&text=The%20script%20compares%20the%20input,until%20it%20finds%20a%20match.).

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
- Ngăn cách giữa pattern và code to run là **close-parenthesis** (dấu đóng ngoặc)
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
  Monday|Tuesday|Wednesday|Thursday|Friday)   # dùng | để có nhiều lựa chọn hơn
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  *) 
  echo "Not a day!";;
esac
```

```python
x="anh"
case $x in 
    "anhoi"|"anh")
    echo "alo";;
    "anhem")
    echo "alooooo";;
    *)
    echo "Okkkkkkkkkkkk";;
esac
#output: alo
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

## Functions và animations in Bash

Phần này sẽ giúp chúng ta thực hiện các tác vụ thường xuyên, đã được lên schedule. Có thể xem thêm [ở đây](https://linuxize.com/post/bash-functions/).

anatomy: giải phẫu học 
Cấu trúc của function trong Bash
```python
function_name () {
    #function_code
    return #something
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
- Truyền arguments vào functions tương tự như truyền vào script, sử dụng kí hiệu `$1` (bắt đầu từ 1). Cũng truy cập vào `ARGV` properties mà trước đây đã đề cập:
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
- Local scope

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
`return` option trong Bash chỉ có ý nghĩa xác định hàm thành công (0) hoặc thất bại (các giá trị từ 1-255). Nó được chấp nhận trong global variable `$?`
```python
#!/bin/bash
x=10
function hello () {
    return 23
}
hello
echo $?   # in ra giá trị trả về của function, sẽ là 23
```

Chúng ta có 2 options để lấy gía trị mong muốn từ function:
- Gán cho global varibale
- Hoặc dùng `echo` đưa ra cái chúng ta mong muốn (trong dòng cuối của hàm) và lấy chúng bằng cách sử dụng shell-within-a-shell `$(command)`

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
  for number in "$@"  # $@ hay $* trả về tất cả arguments cảu hàm
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
### Scheduling your scripts with Cron - Lên kế hoặc với Cron

Một số trường hợp mà scheduling scripts có thể hữu ích:
- Các tasks thường xuyên cần được thực hiện: hàng ngày, hàng tuần, nhiều lần trong ngày
- Tối ưu tài nguyên (ví dụ chạy vào buổi sáng sớm...)

Scheduling scripts với `cron` (bắt nguồn từ Greek là chronos) là kỹ năng cần thiết trong modern data infrastructure. Nó được thúc đẩy bởi cái gọi là `crontab`, đây là file chứa `cronjobs` nó nói cho `crontab` biết code nào được chạy và khi nào.

Có thể xem những lịch trình (`cronjobs`) nào đã được lập trình 
```python
crontab -l
```

Dưới đây là cách tạo `cronjob` bên trong `crontab` file. Có thể tạo nhiều cronjobs, mỗi cái một dòng. Xem thêm link [tại đây](https://en.wikipedia.org/wiki/Cron) để rõ hơn. `*` có nghĩa là every. Cùng xem một số ví dụ
```python
5 1 * * * bash myscript.sh
```
- Minutes star là 5 (5 minutes past the hour). Hours star là 1 (sau 1 am). 3 dấu * cuối nghĩa là mỗi ngày, mỗi tháng. Điều này có nghĩa là chạy mỗi ngày vào lúc 1:05am.
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
nó sẽ chạy sau mỗi 15 phút cho mỗi giờ (ví dụ 15, 30, 45 sẽ chạy chẳng hạn)

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
Thậm chí chúng ta có thể thêm đối số đầu vào tiêu chuẩn (standard input arguments) đến alias của nó. Ví dụ nếu chúng ta luôn muốn "green" được thêm vào làm input đầu tiên của scripts `saycolors` chúng ta sẽ thay đổi như sau:
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

Một số kí hiệu `<<`, `<<<` trong linux:
- https://unix.stackexchange.com/questions/80362/what-does-mean 

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

# Data processing in shell
## Sử dụng curl và wget

https://campus.datacamp.com/courses/data-processing-in-shell/downloading-data-on-the-command-line?ex=1

https://freetuts.net/cai-dat-curl-tren-linux-3314.html
https://blogd.net/linux/tai-file-tren-linux-dung-wget-va-curl/ 

Curl: Clients for urls, dùng để transfer data từ server và đến server, downnload data từ HTTP(s) sites và FTP servers.

Kiểm tra đã được install chưa
```python
man curl
```
Tìm hiểu về flag 
```python
curl --help
```
```python
curl [option tags] [url]
```
url là bắt buộc HTTP, HTTPs, FTP, SFTP.
Curl: 
dùng `-O` sẽ lấy tên trong đường dẫn để lưu (curl -O link_tải)
dùng `-o` sẽ set tên cho file được lưu ví dụ (curl -o custom.zip link_tải)

Ví dụ
```python
curl -O https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
```
nó sẽ lưu file với tên trong link tải.

```python
curl -o rename.tar.gz https:/ /ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
```

Nếu download nhiều files cùng một lúc, có thể dùng regex
```python
curl -O https://sites.com/data_*.txt
```
Ví dụ download files từ 001 đến 100
```python
curl -O https://sites.com/data_[001-100].txt
```
hay từ 001 đến 100 nhưng tăng 10 chỉ số (sẽ lấy cả cái cuối nếu có thể)
```python
curl -O https://sites.com/data_[001-100:10].txt
```
timeout: hết giờ

curl có 2 flags hữu ích trong TH timeout
- `-L` sẽ điều hướng HTTPS nếu có 300 code error
- `-C` sẽ phục hỗi transfer nếu hết giờ trước khi hoàn thành

**Wget** tương tự như vậy nhưng tốt hơn curl khi download nhiều files recursively.

Kiểm tra được install ở đâu
```python
which wget
```
nếu chưa có thì install
```python
sudo apt-get install wget
```
nếu dùng win thì thông qua `gnuwin32`. Sau khi install xong có thể chạy 
```python
man wget 
```
để xem các thông tin

```python
wget [optional flags] [url]
```
Wget cũng hỗ trợ HTTP, HTTPS, FTP, SFTP.
Xem đầy đủ list of flags
```python
wget --help
```

**Download nhiều files với wget**
Lưu tất cả các urls muốn download vào một file `d.txt` chẳng hạn vào download như sau
```python
wget -i d.txt
```
Nó sẽ download tất cả các urls trong `d.txt`.
**Chú ý**: không đặt flag nào nữa giữa `-i` và `d.txt`, nếu có thì đặt trước `-i`.

Đôi khi sẽ hữu ích nếu đảm bảo Wget không sử dụng hết bandwidth với file download, có thể giới hạn bằng `--limit-rate` (mặc định là bytes per second)
```python
wget --limit-rate={rate}k {file-location}
```
```python
wget --limit-rate=200k -i d.txt
```
ở đây sẽ đảm bảo tốc độ download không vượt quá 200 kilobytes per second.

Để tránh overtaxing of file hosting server, mình sẽ thêm thời gian chờ giữa các lần download files
```python
wget --wait={seconds} {file_location}
```

```python
wget --wait=2.5 -i d.txt
```
**Lợi thế của curl so với wget**:
- Hỗ trợ download và upload cho hơn 20 protocols (giao thức)
- Dễ dàng install ở các OS khác nhau

**Lợi thế của Wget so với curl**:
- Nhiều chức năng để xử lý download nhiều files
- Có thể xử lý nhiều format của files (HTML page hay full directory)


Set up thời gian chờ giữa các lần download files
```python
# View url_list.txt to verify content
cat url_list.txt

# Create a mandatory 1 second pause between downloading all files in url_list.txt
wget --wait=1 -i url_list.txt

# Take a look at all files downloaded
ls
```



Một số flag hay của wget:
- `-c`: tiếp tục download cái lần trước bị broken
- `-b` vào background ngay sau khi start up (cho phép downlaod xảy ra trong background
- `-q` turn off Wget output

Có thể kết hợp các flags vào như sau
```python
wget -bqc url
```

```python
# Use curl, download and rename a single file from URL
curl -o Spotify201812.zip -L https://assets.datacamp.com/production/repositories/4180/datasets/eb1d6a36fa3039e4e00064797e1a1600d267b135/201812SpotifyData.zip

# Unzip, delete, then re-name to Spotify201812.csv
unzip Spotify201812.zip && rm Spotify201812.zip
mv 201812SpotifyData.csv SpotifyData201812.csv

# View url_list.txt to verify content
cat url_list.txt

# Use Wget, limit the download rate to 2500 KB/s, download all files in url_list.txt
wget --limit-rate=2500k -i url_list.txt

# Take a look at all files downloaded
ls
```

## Data cleaning and Munging on the command line 
Sử dụng csvkit để convert, preview, filter và manipulate files để chuẩn bị data cho các phân tích khác.

```python
pip install csvkit 
```
Upgrade cho version mới nhất
```python
pip install --upgrade csvkit 
```
https://csvkit.readthedocs.io/en/latest/tutorial.html 

**Lệnh `in2csv`** dùng để convert tabular data files như text hoặc excel về CSV.
```python
in2csv --help
```

Syntax như sau
```python
in2csv source.xlsx > destination.csv
```
còn lệnh 
```python
in2csv source.xlsx
```
chỉ in ra sheel đầu tiên của file chứ không chuyển thành file mới.

Khi muốn in ra **tên của tất cả các sheeet** chúng ta dùng lệnh 
```python
in2csv -n SpotifyData.xlsx
```
Có thể dùng `-n` hoặc `--name`.

Để chuyển một sheet cụ thể sang csv file chúng ta sử dụng `--sheet` option và theo sau bởi tên sheet
```python
in2csv source.xlsx --sheet sheet_name > des.csv
```
Do `in2csv` không đưa ra output nên cần sanity check bằng lệnh
```python
ls
```

Lệnh `csvlook` để display data
```python
csvlook --help
```
```python
csvlook filename.csv
```

`csvstat` in ra các thông tin thống kê của mỗi cột (mean, median..)
```python
csvstat filename.csv
```
### Filtering data using csvkit

Lọc data theo column và row:
- `csvcut`: lọc data theo column (giống lệnh `cut`), cắt csv file theo **column name** hoặc **column position**
- `csvgrep`: lọc data theo row

Sử dụng flag `--name` hoặc `-n` để xem tên của các column trong csv file
```python
csvcut -n filename.csv
```
Output nhận được 
```python
1: id
2: name
3: age
```
Có thể trả về column đầu tiên theo **position** như sau:
```python 
csvcut -c 1 filename.csv
```
Lấy theo tên thì thay position bằng name ở trong nháy kép
```python
csvcut -c "id" filename.csv
```

Trả về nhiều columns theo position (column thứ hai và ba)
```python 
csvcut -c 2,3 filename.csv
```
Nếu sử dụng column names
```python
csvcut -c "name","age" filename.csv
```

Khi lọc theo row thì nó sẽ khớp theo pattern và phải kết hợp với một trong các options sau:
- `-m` theo sau bởi giá trị hàng chính xác muốn lọc
- `-r` theo sau bởi regex pattern
- `-f` theo sau bởi path của file

Muốn lọc hàng có `id=53`
```python
csvgrep -c "id" -m 53 filename.csv
```
ở đây nó sẽ trả về toàn bộ dòng có `id=53` (53 không có dấu nháy), có thể truyền vào column position như sau:
```python
csvgrep -c 1 -m 53 filename.csv
```

```python
# Print a list of column headers in the data 
csvcut -n Spotify_MusicAttributes.csv

# Filter for row(s) where danceability = 0.812
csvgrep -c "danceability" -m 0.812 Spotify_MusicAttributes.csv
```

### Stacking data and chaining commands with csvkit

Nối nhiều commands với nhau và xử lý nhiều files.

Lệnh `csvstack` dùng để nối các rows của hai hoặc nhiều csv files (cùng cấu trúc nhưng có thể do download nhiều lần).
**Chú ý**: các csv files phải có cùng số columns, đúng thứ tự columns và data type phải như nhau, có thể check bằng `csvloook filename.csv`

```python
csvstack file1.csv file2.csv > final.csv
```
Để biết được các rows từ file nào, có thể thêm flag `-g` với tên các group của từng file như sau:
```python
csvstack -g "FILE1","FILE2" file1.csv file2.csv > fina.csv
```
Lúc này sẽ tạo thêm một cột mới `group`. Nếu muốn thay đổi tên cọt mới `group` thành tên khác thì thêm flag `-n`
```python
csvstack -g "FILE1","FILE2" -n "new_name" file1.csv file2.csv > fina.csv
```

**Chú ý**: để chạy các commands nối tiếp nhau trên một dòng chúng ta dùng semicolon `;` như sau:
```python
csvlook filename.csv; csvstat filename.csv
```
Với `;` câu lệnh thứ hai vẫn chạy khi câu lệnh thứ nhất không thành công.

Nếu sử dụng `&&` để nối các commands thì câu lệnh thứ hai chỉ chạy khi câu lệnh thứ nhất thành công.

`|` (pipe operator) sử dụng output của command thứ nhất làm input của command thứ hai.

`>` (re-direct operator) chuyển output của command thứ nhất và lưu vào vị trí trong command thứ hai (là file đó).

Nối các rows của 2 files lại với nhau và lưu vào một file mới
```python
# Stack the two files and save results as a new file
csvstack SpotifyData_PopularityRank6.csv SpotifyData_PopularityRank7.csv > SpotifyPopularity.csv
```

```python
# Take top 15 rows from sorted output and save to new file
# sắp xếp các rows theo cột thứ hai, rồi lấy 15 dòng đầu tiên (|), sau đó lưu 15 dòng đó vào file mới (>)
csvsort -c 2 Spotify_Popularity.csv | head -n 15 > Spotify_Popularity_Top15.csv

# Preview the new file 
csvlook Spotify_Popularity_Top15.csv
```

File chứa 2 sheet, mỗi sheet có thông tin cho một tháng
```python
# Convert the Spotify201809 tab into its own csv file 
# chuyển 1 sheet về csv file
in2csv Spotify_201809_201810.xlsx --sheet "Spotify201809" > Spotify201809.csv

# Check to confirm name and location of data file
ls

# Preview file preview using a csvkit function
csvlook Spotify201809.csv

# Create a new csv with 2 columns: track_id and popularity
# lấy 2 cột của csv file lưu vào csv file khác
csvcut -c "track_id","popularity" Spotify201809.csv > Spotify201809_subset.csv

# While stacking the 2 files, create a data source column
# Nối 2 csv files và track nó thuộc về file nào
csvstack -g "Sep2018","Oct2018" Spotify201809_subset.csv Spotify201810_subset.csv > Spotify_all_rankings.csv
```

## Database Operations on the Command Line

Trong phần này tập trung vào database operation mà csvkit cung cấp bao gồm tạo bảng, data pull, và nhiều ETL transformation.

Pull data từ database bằng cách sử dụng lệnh `sql2csv` (lệnh trong csvkit):
- Thực thi SQL queries trên nhiều database khác nhau (truy cập data mà không qua database clients như PgAdmin, Tableplus...)
- Lưu kết quả ra csv file

Cú pháp như sau:
```python
sql2csv --db "sqlite:///Alo.db" \
        --query "SELECT * FROM table_name" \
        > new_file.csv
```
**Chú ý**: back slash \ là để nối tiếp câu lệnh khi xuống dòng.
Cái đầu tiên cho database connection và tùy thuộc vào database phần string có thể khác nhau:
- SQLite bắt đầu với `sqlite:///` và kết thúc với `.db`
- Postgres và MySQL bắt đầu với `postgre:///` hoặc `mysql:///` và kết thúc không có `.db`.

Phần thứ hai là câu lệnh SQL, cái này cũng thay đổi tùy thuộc vào database. **Chú ý viết chugs trên một dòng không sẽ báo lỗi**.

```python
# Verify database name 
ls

# Query first 5 rows of Spotify_Popularity and print in log
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        | csvlook         
```

```python
# Verify database name 
ls

# Save query to new file Spotify_Popularity_5Rows.csv
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity LIMIT 5" \
        > Spotify_Popularity_5Rows.csv

# Verify newly created file
ls

# Print preview of newly created file
csvlook Spotify_Popularity_5Rows.csv
```

### Manipulating data using SQL syntax

Ở đây mình có csv file và mình muốn dùng SQL syntax để làm việc với nó thay vì sử dụng các methods trong pandas chẳng hạn. Có `csvsql` sẽ hỗ trợ điều này:
- Áp dụng SQL statements vào một hay nhiều csv files
- Tạo SQL database trong bộ nhớ và tạm thời host csv file đang được xử lý
- Vì lý do trên nó không thích hợ cho các files có kích thước lớn và complex query.

Để in ra dòng đầu tiên của csv file
```python
csvsql --query "SELECT * FROM finame.csv LIMIT 1" filename.csv
```
Để có thể nhìn dễ hơn chúng ta sử dụng pipe operator
```python
csvsql --query "SELECT * FROM finame.csv LIMIT 1" filename.csv | csvlook
```

Nếu muốn lưu kết quả vào một file khác thì dùng re-direct operator
```python
csvsql --query "SELECT * FROM finame.csv LIMIT 1" filename.csv > newfile.csv
```
Nếu muốn làm việc với nhiều files
```python
csvsql --query "SELECT * FROM file1 INNER JOIN file2..." file1.csv file2.csv
```
- SQL query chỉ viết trên một dòng
- Thứ tự các files trùng với thứ tự xuất hiện trong SQL query

```python
# Re-direct output to new file: ShortestSong.csv
csvsql --query "SELECT * FROM Spotify_MusicAttributes ORDER BY duration_ms LIMIT 1" \
	Spotify_MusicAttributes.csv > ShortestSong.csv
    
# Preview newly created file 
csvlook ShortestSong.csv
```

Thường sẽ lưu câu query vào shell variable để vượt qua giới hạn không được có linebreak trong SQL query.

```python
# Store SQL query as shell variable
sql_query="SELECT ma.*, p.popularity FROM Spotify_MusicAttributes ma INNER JOIN Spotify_Popularity p ON ma.track_id = p.track_id"

# Join 2 local csvs into a new csv using the saved SQL
csvsql --query "$sql_query" Spotify_MusicAttributes.csv Spotify_Popularity.csv > Spotify_FullData.csv

# Preview newly created file
csvstat Spotify_FullData.csv
```
Nhìn vào ở đây thì thấy ghi câu query kiểu này rất rối và khó nhìn. Phân tích data với csvkit kiểu SQL không phải là sự lựa chọn tốt.

### Pushing data back to database 

`csvsql` sẽ:
- thực thi SQL statements trực tiếp trên database 
- hỗ trợ tạo tables và insert data
`csvsql` có thêm một số options:
- `--insert`
- `--db`
- `--no-ìnerence` và `--no-constraints` - tạo schema mà không có giới hạn về chiều dài và không có null checks

Ví dụ push dât vào database cho csvfile
```python
csvsql --db "sqlite:///data.sb" \
       --insert filename.csv
```

```python
csvsql --no-inference --no-constraints \
       --db "sqlite:///data.sb" \
       --insert filename.csv
```

```python
# Preview file
ls

# Upload Spotify_MusicAttributes.csv to database
# đưa csv file vào database
csvsql --db "sqlite:///SpotifyDatabase.db" --insert Spotify_MusicAttributes.csv

# Store SQL query as shell variable
sqlquery="SELECT * FROM Spotify_MusicAttributes"

# Apply SQL query to re-pull new table in database
# lấy data từ database
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery" 
```

### Data Pipeline on the Command Line

Trong phần này chungs ta sẽ kết nối command line và các ngôn ngữ khác để chúng làm việc cùng nhau, ở đây sử dụng Python.

Một cách để tương tác với Python ở command line là activate Python session `python`
```python
python
```
Bên trong Python interactive session thì chỉ sử dụng Python syntax.

Upgrade pip
```python
pip install --upgrade pip
```

Liệt kê tất cả các Python packages trong environtment hiện tại
```python
pip list
```
Ví dụ muốn upgrade package nào đó trong environtment hiện tại
```python
pip install --upgrade scikit-learn
```
Install các packaages được ghi trong file có sẵn
```python
pip install -r requirements.txt
```
hoặc dùng `--requirement`.

### Data job automation with cron

Chúng ta có thể tự động hóa tất cả các quá trình đã tìm hiểu.

Crontab là central file để theo dõi các cronjobs (các lịch trình đã lên). Kiểm tra danh sách các cronjobs.
```python
crontab -l
```
Thêm job vào crontab
- Cách 1: sử dụng lệnh `crontab -e` sau đó edit bằng Nano hay gì đó
- Cách 2: echo vào crontab
```python
echo "* * * * * python create_model.py" | crontab
```
Ví dụ như trên là chạy mỗi phút, mỗi giờ, mỗi ngày trong tháng và mỗi ngày trong tuân (có thể mỗi ngày trong tháng nhưng mình set chạy thứ nào đó trong tuần)
<img src="1.png">





under the hood: bên dưới mui xe (nghĩa đen nhìn dưới mui xe là động cơ sẽ hiểu rõ hơn, từ đó nhìn vào bên dưới vào bản chất vấn đề sẽ thấy rõ hơn.)







## Sử dụng tar để nén và giải nén


Link này https://phptravels.vn/chuan-tat-tan-tat-ve-nen-va-giai-nen-zip-gzip-tar-rar-7-zip-tren-linux-lenh-tar-trong-linux-xac-minh/ có giới thiệu về các flags đọc dễ hiểu hơn.


https://www.hostinger.vn/huong-dan/tar-command

## Lệnh cat

https://quantrimang.com/lenh-cat-trong-linux-181056#:~:text=L%E1%BB%87nh%20cat%20(vi%E1%BA%BFt%20t%E1%BA%AFt%20c%E1%BB%A7a,ra%20trong%20terminal%20ho%E1%BA%B7c%20file.


Link cài đặt singularity: https://singularity-tutorial.github.io/01-installation/ 

Trình quản lý gói **pyenv** có tích hợp **virtualenv**:
- https://viblo.asia/p/su-dung-pyenv-de-quan-li-cac-phien-ban-python-4dbZNNpLZYM
- https://kipalog.com/posts/Pyenv---Virtualenv--Cap-doi-hoan-hao
Mình thì quen dùng với miniconda hơn, cài đúng phiên bản, dùng cũng khá dễ dàng.

**Tạo subfolders với mkdir**
Ví dụ đang đứng trong `~/Desktop/anhem`
```python
mkdir -p save/kitti-object-detection/yolo3tiny/model1
```
Chúng ta sẽ có `~/Desktop/anhem/save/kitti-object-detection/yolo3tiny/model1`. `-p` đại diện cho parents, nó sẽ tạo bất kỳ parents directories nếu cần để tạo được subfolder cuối.

Sau khi đã tạo subfoler kia rồi mà chạy thêm
```python
mkdir -p save/kitti-object-detection/yolo3tiny/model2
```
thì nó sẽ tạo subfolder mới `model2` ngang hàng với `model1`.

Xem thêm ở đây https://stackoverflow.com/questions/9242163/bash-mkdir-and-subfolders.
Nếu chạy nhiều model có thể chỉ cần tạo một lần như post có trong linhk trên.

Muốn thực hiện copy cả folders (gồm tất cả các files và subfolders trong đó) thì dùng thêm flag `-R` (recursive) trong lênh cp
```python
cp -R ~/Desktop/save/kitti-object-detection/yolo3tiny/model1/test ~/Desktop/anhem/save/kitti-object-detection/yolo3tiny/model1
```
Ở đây nó sẽ copy cả folder `test` vào folder `model1` như trên. 

```python
if [ -d ${dir} ]; then   # kiểm tra là dir hay không
  # do st
else
  #do st
fi
# if [ ! -d ${dir} ]; then   # kiểm tra không phải dir
```

```python
if [ -f ${file} ]; then   # kiểm tra là file hay không
  # do st
else
  #do st
fi
# if [ ! -f ${dir} ]; then   # kiểm tra không phải file
```

```python 
if [ ! ${dir} ]; then   # kiểm tra xem dir của phải empty hay không
  # do st
else
  #do st
fi
```

**Để chạy nhiều lệnh trong sungularity dùng exec**, ví dụ
```python
/usr/local/bin/singularity --nv container.img script.sh !& tee ${filename}
```
Đôi khi để chạy được cần thêm `bash`, `/bin/sh` hoặc thêm flag `-C` vào thì mới chạy được trong singularity và không báo lỗi
```python
/usr/local/bin/singularity --nv container.img bash script.sh !& tee ${filename}
```

**Chú ý**: Khi làm việc với bash script và hay chuyển file thì quy tắc nên nhớ là khi di chuyển vào một file và có sử dụng path ở trong file đó thì vị trí lúc đó chính là vị trí của file vừa vào chứ không phải là vị trí của file đầu tiên gọi đến file vừa vào.

**Cách viết đường dẫn và file**
```python
/home/hammiu/data
```
Cách viết như này thì `data` có thể là directory hoặc file (ko có extension)
```python
/home/hammiu/data/
```
Thêm slash `/` ở cuối thì data chỉ có thể là directory.

# Makefile

References nên đọc:
- https://makefiletutorial.com/
- https://www.linode.com/docs/guides/gnu-make-tutorial-automate-tasks/
- https://dev.to/matthewepler/using-makefiles-to-automate-workflows-acd#:~:text=Makefiles%20are%20used%20to%20automate,projects%20and%20across%20projects%2Fteams. 
- https://www.digitalocean.com/community/tutorials/how-to-use-makefiles-to-automate-repetitive-tasks-on-an-ubuntu-vps 
- https://opensource.com/article/18/8/what-how-makefile

Mình quen với shell script hơn, tuy nhiên một số project có sử dụng Makefile. Shell script có thể thực hiện được các chức năng của Makefile, tuy nhiên Makefie sẽ không build lại những cái đã có rồi và thay đổi. Ở đây chỉ là những notes trong quá trình làm việc gặp phải:
- `.PHONY` target, kiểu có dạng
```python
.PHONY: test-1
test-1:
  sh test_script.sh
```
Khi gọi `make test-1` thì nó sẽ đi thực thi `sh test_script.sh` bên trong Makefile. Nó sẽ luôn chạy ngay cả khi có file `test-1` tồn tại rồi.

Đối với các trường hợp khác cho nhiều targets:
```python
.PHONY: unittest fulltest
unittest:
  sh unittest_script.sh

fulltest:
  sh fulltest_scirp.sh
```
- https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
- https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile

Mình có hỏi ở đây: https://daynhauhoc.com/t/chay-file-script-chua-doan-make/127063  có bác trả lời rất kỹ và mình đã hiểu được.

Em mới tiếp xúc với makefile gặp case này mong các bác hỗ trợ. Em có cây thư mục kiểu này.
```python
 ~/project  tree
.
├── ma
│   └── tests
│       └── Makefile
├── Makefile
└── script.sh
```
Em đang trong thư mục `~/project` có file bash script `script.sh`, em cần chạy script này và file script này có chứa đoạn mã
```python
# trong script.sh
make test_1 test_2
```
**Makefile** của em trong `~/project` lại chứa đoạn mã kiểu
```python
.PHONY test_1
test_1:
   $(MAKE) -C ma/tests $@
.PHONY test_2
test_2:
  $(MAKE) -C ma/tests $@
```
Và **Makefile** của em trong `~/project/ma.tests` lại chứa đoạn mã kiểu
```python
.PHONY: test_1
test_1:
	sh script_1.sh

.PHONY: test_2
test_2:
	sh script_2.sh
```

Đọc thấy `.PHONY` để tránh conflict với file cùng tên và cải thiện performance.

Xem thêm recursive use of make, ví dụ trong `subdir` có Makefile, và ở trong thư mục hiện tại có Makefile, chúng ta muốn sử dụng `make` như command trong Makefile
```python
subsystem:
  $(MAKE) -C subdir
```
**Chú ý**: flag `-C` ở đây ám chỉ directory (có thể thay bằng `--directory`). Để hoạt động tốt cần kết hợp với `.PHONY` ở trên. `$(MAKE)` chính là make variable.

Đọc thêm bài này để có cái nhìn rõ hơn về [Makefile](https://dev.to/matthewepler/using-makefiles-to-automate-workflows-acd#:~:text=Makefiles%20are%20used%20to%20automate,projects%20and%20across%20projects%2Fteams.). Nói tóm lại:
- Khi dự án nhỏ có thể tự động workflow với Bash script, Python file...
- Khi sự án lớn, phức tạp hơn, có sự kết hợp của nhiều ngôn ngữ thì nên sử dụng Makefile
- Bash script tương tự như những gì chúng ta làm trên shell nên dễ tiếp cận hơn, tuy nhiên đối với Makefile chúng ta cần tìm hiểu nhiều hơn dù vẫn có sự tương đồng.

**Chú ý**: trong Makefile thụt dòng thì dùng TAB không dùng spaces.

**Syntax trong Makefile** có dạng sau:
```python
targets: prerequisites
	command
	command
	command
```
- Targets là một hoặc nhiều files (thường là 1), **nhớ nó sẽ liên quan đến file nhé**, mình còn gặp lại nó khi có file khác cùng tên trong thư mục
- Prerequisites (/ˌpriːˈrekwəzɪt/: điều kiện tiên quyết) là một hoặc nhiều files ngăn cách bằng space (phải tồn tại trước khi thực hiện các commands bên dưới), có còn được gọi là dependencies.

**Variables** trong Makefile chỉ ở dạng string, thường sẽ dùng `:=` để gán
```python
files := file1 file2
some_file: $(files)
	echo "Look at this variable: " $(files)
	touch some_file

file1:
	touch file1
file2:
	touch file2

clean:
	rm -f file1 file2 some_file
```
**Khi truy cập đến các biến có thể sử dụng `${}` hoặc `$()` đều được**. Không nên dùng `$x` mặc dù nó vẫn hoạt động. 

```python
hello: 
	echo "hello world"

anhem:
	echo "anhem"

# Chạy make mà không chỉ định rule (hay function) thì sẽ chạy rule đầu tiên với target là `hello`
# bởi vì không chỉ định gì theo mặc định sẽ chạy rule đầu tiên
# có thể chỉ định rule `make anhem` thì nó chỉ thực thi như bên dưới

unitest: depen
	bash script.sh

# ở đây hiểu `depen` là depecdency của rule `unittest` và khi chạy `make unitest`
# nếu không có `depen` sẽ báo lỗi

# tạo một file alo qua lệnh `touch alo`
# và khi chạy `make alo` sẽ báo là "make: 'alo' is up to date." do đã có file alo rồi
# nên nó sẽ không chạy vào rule `alo` nữa.
alo:
	echo "Hello alo"

# Để tránh điều trên chúng ta sẽ dùng .PHONY, lúc này make sẽ chạy target alo ngay
# cả khi bên ngoài đã có file alo
.PHONY: alo
alo:
	echo "Hello alo"

files := file1 file2 

some_file: $(files)
	echo "toi day"

file1:
	touch file1
file2:
	touch file2
```

**Targets** trong Makefile

Nếu chúng ta có nhiều targets và muốn chạy tất cả chúng thì có thể gom chúng vào target `all` như sau:
```python
all: one two three

one:
	touch one
two:
	touch two
three:
	touch three

clean:
	rm -f one two three
```
Ví dụ luôn
```python
all: one two 

one:
	echo "toi"
two:
	echo "ban"
```
nhận được output
```python
echo "toi"
toi
echo "ban"
ban
```
Rõ ràng là nó đi chạy target `one` và target `two`.

**Multiple targets**: khi có nhiều targets trong cùng một rule, thì các commands bên trong rule sẽ chạy lần lượt cho mỗi target `$@` - cái này chứa tên của target.
```python
all: f1.o f2.o

f1.o f2.o:
	echo $@
# ở đây tạm gọi có 2 targets f1.0 và f2.o, sẽ lần lượt chạy echo f1.o và echo f2.o chõ mỗi target tương ứng. Ở đây có thể hiểu tách thành 2 rules như bên dưới
# Equivalent to:
# f1.o:
#	 echo f1.o
# f2.o:
#	 echo f2.o
```

Có thể thêm `@` vào trước echo để nó không hiển thị lại câu lệnh echo
```python
.PHONY: all em

all: hello anh

hello:
	@echo $@
	@echo "alooooooooo"

anh:
	@echo "TOIDAY"

em:
	@echo "Cohienthi"

# make all em   # chạy trong .PHONY
```

### Automation Python project với Makefile
- https://antonz.org/makefile-automation/
- https://swcarpentry.github.io/make-novice/reference.html
- https://www.digitalocean.com/community/tutorials/how-to-use-makefiles-to-automate-repetitive-tasks-on-an-ubuntu-vps 


# Hướng dẫn sử dụng pyenv để tạo môi trường ảo với Python
Được cái cái này có thể cài nhiều versions dễ dàng. Mình thì quen dùng conda nhưng có project cần

Nhớ cái này chạy trong Bash, nếu muốn cho Zsh thì cần cài kiểu khác

```python
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

```python
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

```python
exec "$SHELL"
```

Muốn cài phiên bản Python mới
```python
pyenv install 3.8.0
```
Tạo môi trường ảo với phiên bản Python 3.8.0 được chỉ định
```python
pyenv virtualenv 3.8.0 name_of_env
```
Cần cài virtualenv nếu chưa có
```python
sudo apt install python3-virtualenv
```

```python
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

exec bash
```
Kích hoạt như sau:
```python
pyenv local name_of_env
```

Để deactivate
```python
pyenv local system
```

**Lấy full path của current file's directory trong python**

Ví dụ trong `~/Desktop/toi` có file `main.py` với nội dụng như sau:
```python
import os

print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))
```
Nếu đứng trong `~/Desktop/toi` chạy lệnh `python3 main.py` thì nhận được output
```python
/home/huytranvan2010/Desktop/toi
/home/huytranvan2010/Desktop/toi
```
Tuy nhiên nếu chúng ta đứng với thư mục home chẳng hạn rồi chạy `python3 main.py` thì kết quả sẽ là
```python
/home/huytranvan2010
/home/huytranvan2010/Desktop/toi
```
Điều này cho thấy `os.getcwd()` sẽ trả về path của current directory mà chúng ta đang đứng trong terminal để chạy lệnh python3. Còn `os.path.dirname(os.path.abspath(__file__))` sẽ cho chúng ta full path của directory đang chứa file python của chúng ta. Cần chú ý điều này để tránh nhầm lần path khi code. Xem thêm ở [link này](https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory).

**SSH cho Gitlab và Github**
Đã tạo SSH key trên local và add trên remote (trên này lấy public key) rồi. Có thể sử dụng SSH key đó trên máy local khác bằng cách copy **private key** trên máy local kia sang bên máy local này. Thư mục chứa SSH key là `/.ssh`.
- https://www.codelean.vn/2020/01/cai-at-ssh.html
- https://blog.nguyenary.dev/cach-tao-ssh-key-va-su-dung-no-voi-gitlab-va-github.html
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- https://shareprogramming.net/cach-them-ssh-key-vao-gitlab/
