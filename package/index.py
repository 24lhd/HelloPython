import package.MyMath as m

print(m.nhan(10, 2))

'''Package module

Có thể gom nhiều module .py vào một thư mục và tên thư
mục là tên của package và tạo một file __init__.py trong
thư mục này.


Khi sử dụng một module thuộc một package thì các lệnh
trong file __init__.py sẽ được thực hiện trước. Thông
thường thì file __init__.py sẽ rỗng.
Có thể tạo các subpackage bên trong một package theo
đúng cấu trúc thư mục, có file __init__.py
'''
