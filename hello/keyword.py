'''
                           with

            in
'''

''' and     or      not
    Các toán tử này làm công việc mang tính logic
    Tương đương trong java
        and - &&
        or - ||
        not - !
'''

'''try     except      finally
Làm việc với các ngoại lệ

finally có tác dụng thực thi các câu lệnh cho dù có lỗi hay không có lỗi xảy ra
'''

'''del 
Từ khóa del có tác dụng xóa một đối tượng.
'''

'''pass
    có tác dụng… không làm gì cả :D.
'''

'''import       as      from

sử dụng để tích hợp module cần sử dụng vào chương trình.

as được dùng để đổi tên module mà chúng ta muốn sử dụng thành tên mà chúng ta thích.

Trong một module có rất nhiều hàm, biến, lớp…
 khi dùng từ khóa import mặc nhiên chúng ta được sử dụng toàn bộ mọi thứ có trong module.
 Nhưng nếu bạn chỉ muốn dùng một vài thứ nhất định trong module đó thì sử dụng từ khóa from.
 
 from sys import version
 print (version)
 có nghĩa là chỉ sử dụng biến version trong module sys. Và khi in ra màn hình thì chúng ta 
 không cần đưa tên module ra trước. Lúc này biến version có đặc tính y hệt như những biến thông thường.
 
'''

'''     global
Khi định nghĩa một hàm thì các biến trong hàm đó chỉ tồn tại bên trong hàm, khi kết thúc hàm chúng bị xóa khỏi bộ nhớ.
 Tuy nhiên nếu muốn sử dụng chúng ngoài thân hàm thi chúng ta có thể sử dụng từ khóa global.
'''

'''     assert
assert được dùng trong quá trình debug. Thường chúng ta dùng từ khóa này để kiểm tra các trạng thái của đối tượng.
 Ví dụ chúng ta có một chương trình tính lương, vì lương không thể bé hơn 0 nên nếu chúng ta có thể dùng từ khóa 
 assert để kiểm tra xem lương có lớn hơn 0 hay không. Nếu sai thì trình thông dịch sẽ báo lỗi.
'''

'''     is
Toán tử == kiểm tra xem 2 đối tượng có cùng giá trị hay không.
 Từ khóa is kiểm tra xem 2 đối tượng có cùng bộ nhớ hay không vì trong
  lập trình một địa chỉ bộ nhớ có thể được tham chiếu bởi nhiều đối tượng.
  
  print ([] == [])
  print ([] is [])

 do Python tự động tối ưu bộ nhớ nên những string có giá trị giống nhau sẽ được sử dụng chung bộ nhớ, kết quả trả về True.
'''
# for i in (1, 2, 3, 4, 5):
#     a = lambda x: print(x)
#     print(a(i), )

'''lambda
 có tác dụng tạo một hàm ẩn, hàm ẩn là hàm không dính tới một cái tên cụ thể nào.
 Trong các ngôn ngữ khác thì hàm này được gọi là hàm nội tuyến (inline function).
'''

# class YesNoException(Exception):
#     def __init__(self):
#         print('Invalid value')
#
#
# answer = 'y'
#
# if (answer != 'yes' and answer != 'no'):
#     raise YesNoException
# else:
#     print('Correct value')

'''     raise
Trong Python có rất nhiều các exception được định nghĩa sẵn, nhưng tất nhiên sẽ có trường hợp chúng ta cần các exception
 riêng cho chúng ta tự định nghĩa. Từ khóa raise có tác dụng “phát” exception khi cần.
'''

exec("for i in [1, 2, 3, 4, 5]: print(i, end=' ')")
exec("print('xin chào')")
'''exec
Dùng để chạy chương trình vơi chuối string truyên vào là chuỗi code python
'''

'''     yield
Ví dụ:

>>> def dummy():
...     print "You won't see me when created"
...     yield 1
...     print "You didn't see me"
...     yield 2
...     print "Bye bye"
...
>>> gen = dummy()
>>> gen.next()
You won't see me when created
1
>>> gen.next()
You didn't see me
2
>>> yield
Trước khi sử dụng yield, bạn phải biết về bộ lặp (iterator) và bộ sinh (generator).

Một hàm mà có sử dụng từ khóa yield thì hàm đó sẽ trở thành một bộ sinh. Bộ sinh là một đối tượng khả lặp (iterable).
Ở dòng gán biến gen, các đoạn mã trong hàm dummy chưa được thực thi. Đến khi gọi gen.next thì dummy 
mới được chạy, nhưng chỉ chạy đến từ khóa yield đầu tiên và trả về kết quả là tham số của yield. 
Đến khi gọi gen.next lần thứ hai thì mã của dummy mới tiếp tục được chạy tiếp bắt đầu từ sau yield 1.

Sau đoạn ví dụ trên, nếu ta gọi gen.next() một lần nữa thì trên màn hình sẽ hiện câu Bye bye,
 đồng thời cũng xuất hiện biệt lệ StopIteration cho biết là bộ sinh này đã không còn khả năng
  sinh ra giá trị mới. Lý do là sau câu lệnh print “Bye bye” thì hàm dummy đã kết thúc.

'''

'''     in
Toán tử kiểm tra phần tử trong một tập hợp: - in kiểm tra
có tồn tại - not in kiểm không tồn tại
'''

dict = {
    'name': "duong",
    "age": 21,
    "que": [
        {
            "thon": "donglu",
            "xã ": "an lam"
        }
    ]
}
print(dict)

import hello

print(hello.b)
