'''
Trong OOP có các khái niệm cơ bản sau đây:

Trừu tượng (Abstraction)
Đa hình (Polymorphism)
Đóng gói (Encapsulation)
Kế thừa (Inheritance)
'''

'''
Đối tượng là các thực thể của một lớp nào đó. Lớp là khuôn mẫu của các đối tượng. 

Ví dụ như list, tuple, dictionary, string, int… là các lớp.

 Khi chúng ta khai báo biến thuộc các lớp này thì chúng là các đối tượng.
 
 Tất cả mọi thứ trong Python đều là đối tượng
'''

import sys

print(dir(sys))


def function(): pass


print(type(1))
print(type(""))
print(type([]))
print(type({}))
print(type(()))
print(type(object))
print(type(function))
print(type(sys))
'''
Trong ví dụ trên nhờ vào hàm type() mà chúng ta biết được thực chất 
tất cả các kiểu dữ liệu và các module mà chúng ta đã học thực chất đều là các đối tượng.
'''

