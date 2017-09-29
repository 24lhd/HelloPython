# Kiểu Boolean
isTrue = False
isFalse = True

print(bool(True))
print(bool(False))
print(bool("text"))
print(bool(""))
print(bool(' '))
print(bool(0))
print(bool())
print(bool(3))
print(bool(None))


# Kiểu None
# Đây là một kiểu đặc biệt trong Python.
#  Ý nghĩa của kiểu này là không có giá trị gì cả, không tồn tại, rỗng…v..v
def function():
    pass


print(function())

# Kiểu số
# Trong Python, kiểu số có 3 loại là số nguyên, số thực và số phức.


# Kiểu String
# String là kiểu dữ liệu lưu trữ văn bản.
# Chúng ta có thể tạo ra một string bằng dấu nháy đơn,
#  nháy kép
# hay 3 dấu nháy kép.
#  Khi dùng 3 dấu nháy kép, chúng ta cũng có thể ghi một chuỗi trên nhiều dòng mà không cần dùng dấu \.

nhayKep = "Đây là chuỗi"
nhayDon = 'day la chuoi'
nhay3 = """
Đây 
là 
chuỗi được hiển thị thành nhiều dòng
"""

# Kiểu Tuple
# Kiểu Tuple là kiểu tập hợp nhiều phần tử,
# kiểu này lưu trữ các phần tử một cách có thứ tự và có thể lưu nhiều kiểu giá trị khác nhau trong một tuple.
#  Giá trị trong tuple không thể thay đổi được.
# Tuple có thể lưu trữ các kiểu dữ liệu khác nhau một cách linh hoạt.
# Có 2 cách tạo tuple
# tuple của chúng ta có số nguyên, string và cả một tuple khác.
# Để truy xuất phần tử của tuple bên trong một tuple, bạn dùng hai cặp dấu [].

menu = ("Táo, Lê , Dừa")
print(menu)
menu = "Táo", "Lê", "Dừa"
print(menu)

# Kiểu List

# Kiểu list cũng là một kiểu lưu các giá trị tuần tự, một list cũng có thể lưu nhiều giá trị khác nhau.
#  Do đó list và tuple có nhiều điểm tương đồng. Điểm khác biệt giữa list và tuple là các phần tử trong list có thể thay đổi giá trị,
# ngoài ra list có một số phương thức mà tuple không có.

# Để tạo một list thì ta dùng cặp ký tự []


# Kiểu từ điển

#  Kiểu này lưu trữ các phần tử theo dạng các cặp khóa-giá trị (key–value).
#  Các chỉ số trong từ điển là các khóa.
#  Do đó các khóa phải khác nhau, chúng ta sẽ có một bài riêng để nói về kiểu này.

words = {'girl': 'Maedchen', 'house': 'Haus', 'death': 'Tod'}


