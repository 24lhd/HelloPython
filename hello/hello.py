#   comment trong python sử dụng dau # để comment 1 dòng

#                    Biến
#   biển trong python không phải khai bảo kiểu dữ liệu,
#   trình thông dịch sẽ tự động nhận biết kiểu dữ kiệu khi gán giá trị cho biến
#   python phân biệt chữ thường chữ hoa
#   Ex:

day_la_bien = 1

#                       Giá trị
#   Nếu chúng ta không gán các giá trị vào biến thì chúng sẽ bị hủy bỏ.
str = " chuỗi"
ngay = 18
chamDong = 20.1

#                Toán tử
# +    -    ~    *    **    /    %
# << >>    &    |    ^
# and    or    not    in    not in
# is    is not    < >    !=    <>
# ==    <= >=


#       Khối lệnh
# Trong các ngôn ngữ lập trình khác như Pascal, Java… một khối lệnh được nằm trong cặp dấu {}
#  hoặc cặp từ khóa BEGIN–END. Còn Python thì dùng khoảng trắng, bạn có thể dùng dấu tab hoặc
# dấu cách (space) đều được. Trên hướng dẫn của Python khuyến khích dùng 4 dấu cách.

age = 2
if age > 1 and age > 2:
    print("nó lớn hơn 1 và lớn hơn 2")
for i in range(5):
    print(i)

    # Ký hiệu
    #
    # Các ký hiệu dùng để bao bọc lấy các biểu thức, điều kiện… Trong các ví dụ trước có hàm print chúng ta
    # phải dùng cặp ký hiệu () để bao bọc lấy nội dung cần được in ra màn hình. Thực ra đối với Python 2.x
    # thì lệnh print không cần cặp ký tự này, nhưng Python 3.x thì phải có cặp ký tự này, lý do là vì trong phiên
    # bản 2.x, print là một câu lệnh nhưng trong 3.x thì print đã được phát triển thành một hàm riêng.


    # (       )       [       ]       {       }
    # ,       :       .       `       =       ;
    # +=      -=      *=      /=      //=     %=
    # <= |= ^= >>=     <<=     **=
    # '       "       \       @

# Từ khóa
#
# Từ khóa là các từ dành riêng cho Python. Từ khóa thường được dùng để thi hành một lệnh nào đó, hoặc tên của một
# thành phần trong Python. Chẳng hạn từ khóa if thi hành lệnh so sánh. Từ khóa for để bắt đầu một vòng lặp, từ khóa
# and là tên của toán tử and… Bạn không được đặt tên biến hay tên hàm trùng với tên của các từ khóa.

# and       del       from      not       while
# as        elif      global    or        with
# assert    else      if        pass      yield
# break     except    import    print
# class     exec      in        raise
# continue  finally   is        return
# def       for       lambda    try

b = "hello duong"
