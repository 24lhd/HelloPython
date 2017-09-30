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
print("---------------Đối tượng ")
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


class Dog:
    pass


# tạo ra đối tượng dog từ lớp Dong
dog = Dog()
print(type(dog))
print(type(Dog))

'''Thuộc tính

Trong Python có một phương thức đặc biệt gọi là  __init__()
 dùng để khởi tạo giá trị cho các thuộc tính của một đối tượng.
 
  Phương thức __init__() là phương thức khởi tạo của tất cả các lớp,
   mỗi khi tạo một đối tượng phương thức này sẽ tự động được gọi.
   
   Bất cứ phương thức nào của Python cũng đều phải có tham số đầu
    tiên là self rồi mới đến các tham số khác. self thực ra chỉ là biến đối tượng đã gọi phương thức này mà thôi
    


'''
print("---------------Thuộc tính")


class Cat:
    def __init__(self, name):
        self.name = name
        pass


pi = Cat("pi")
print(
    pi.name)  # Để truy xuất đến thuộc tính của một đối tượng thì chúng ta ghi tên đối tượng, dấu chấm và tên thuộc tính.

'''
Ngoài ra bạn có thể gán giá trị cho các thuộc tính ở bất cứ đâu sau
 phần định nghĩa lớp chứ không chỉ riêng bên trong phương thức khởi tạo.
'''

pi.age = 2
print(pi.age)

'''
 bạn có thể định nghĩa các thuộc tính chung cho mọi đối tượng.

'''


class Annimal:
    màuLong = "xanh"

    def move(self):
        print("di chuyen")


hulk = Annimal()
hulk.move()
print(hulk.màuLong)

'''
Có hai cách để truy xuất thuộc tính lớp, thứ nhất là thông qua tên lớp, cách thứ hai là thông qua một thuộc tính đặc biệt nữa là thuộc tính __class__.
'''

print(hulk.__class__.màuLong)

'''
khi bạn thay đổi giá trị của thuộc tính chia sẻ trong một đối tượng thì tất cả các thuộc tính chia sẻ đó trong các đối tượng khác cũng thay đổi theo
'''

hulk.__class__.màuLong = "đỏ"

spider = Annimal()
print(spider.__class__.màuLong)
print(hulk.__class__.màuLong)

'''Phương thức
- chẳng qua là các hàm chỉ khác hàm bình thường ở chỗ chúng được định nghĩa bên trong một lớp.
-  Phương thức là một thành phần quan trọng trong khái niệm Encapsulation (đóng gói)
- bạn chỉ quan tâm rằng phương thức này chức năng thế nào chứ không quan tâm đến việc nó kết nối như thế nào
'''

'''Kế thừa
- Kế thừa là định nghĩa một lớp dựa trên một lớp đã được định nghĩa trước đó
- Lớp kế thừa từ lớp khác được gọi là lớp dẫn xuất, lớp được các lớp khác kế thừa mình thì gọi là lớp cơ sở
- Kế thừa trong lập trình hướng đối tượng cho phép chúng ta sử dụng lại mã nguồn và giảm độ phức tạp của chương trình
- Lớp dẫn xuất có thể kế thừa hoặc mở rộng các tính năng của lớp cơ sở.
- Để kế thừa một lớp thì chúng ta đặt tên lớp đó bên trong cặp dấu ngoặc tròn () ngay phía sau phần định nghĩa tên lớp
'''
print("---------------Kế thừa")


class Animal:
    canNang = 24

    def __init__(self, name):
        self.name = name


class Dog2(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


class Cat2(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)


dog = Dog2("Dog2")
cat = Cat2("cat2")

'''Đa hình

'''
print("---------------Đa hình")


class Animal:
    def __init__(self, name=''):
        self.name = name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Meow!")


class Dog(Animal):
    def talk(self):
        print("Woof!")


a = Animal()
a.talk()

c = Cat("Missy")
c.talk()

d = Dog("Rocky")
d.talk()

print("---------------Các phương thức đặc biệt")
'''
    - Tất cả các lớp dù là có sẵn hay do chúng ta định nghĩa đều kế thừa từ một lớp gốc trong Python có tên là object
    - Lớp này có sẵn một số phương thức và đương nhiên là các lớp do chúng ta định nghĩa đều kế thừa các phương thức này,
    - khi chúng ta gọi đến các hàm hay toán tử được xây dựng sẵn như print(), del… 
    chúng sẽ gọi đến các phương thức gốc của lớp object
    - Chính vì các lớp do chúng ta định nghĩa đều được kế thừa từ lớp object nên chúng ta cũng có thể dùng các
     hàm hay toán tử có sẵn trong Python với các lớp của chúng ta
    - Ví dụ:
'''


class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s , author:%s, pages:%s " % \
               (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


book = Book("Inside Steve's Brain", "Leander Kahney", 304)

print(book)
print(len(book))
del book
# Trong ví dụ trên, chúng ta định nghĩa lớp Book. Bên trong lớp này chúng ta định nghĩa 4 phương thức được kế thừa từ lớp object là __init__(),__str__(), __len__() và __del__().
#
# print (book)
# Khi sử dụng hàm print(), hàm này sẽ gọi đến phương thức __str__(), do đó khi chúng ta kế thừa lại phương thức này, hàm print() sẽ gọi đến phương thức __str__() trong lớp Book của chúng ta.
#
# print (len(book))
# Tương tự, hàm len() gọi đến phương thức __len__()
#
# del book
# Từ khóa del gọi đến phương thức __del__() và trên thực tế là phương thức này làm công việc hủy bỏ một đối tượng ra khỏi bộ nhớ
# . Nhưng ở đây chúng ta kế thừa phương thức này chỉ làm công việc là in ra một đoạn text.


class Vector:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)

    def __add__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] + other.data[j])
        return Vector(data)

    def __sub__(self, other):
        data = []
        for j in range(len(self.data)):
            data.append(self.data[j] - other.data[j])
        return Vector(data)


x = Vector([1, 2, 3])
y = Vector([3, 0, 2])
print(x + y)
print(y - x)

# Chúng ta định nghĩa lớp Vector, lớp vector này kế thừa hai phương thức __add__() và __sub__().
# phương thức __add__() sẽ được gọi khi sử dụng toán tử + và phương thức __sub__() sẽ được gọi khi sử dụng toán tử -