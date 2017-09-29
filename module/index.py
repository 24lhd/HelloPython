import tong2so

print(tong2so.tong(1, 4))

'''
Lấy danh sách thuộc tính và phương
thức của một module


Để lấy được danh sách các thuộc tính và phương thức mà
module hỗ trợ, sử dụng hàm dir(modulename)

Có thể gọi hàm dir() không truyền tham số để lấy các
thuộc tính và phương thức của scope hiện tại đang thực
thi.
'''

print(dir(tong2so))
print(dir())

'''
Đường dẫn tìm để load module

'''

for obj in dir(tong2so):
    print("\n\n")
    print(obj)
    exec("print(tong2so." + obj + ")")

print(tong2so.__file__)
