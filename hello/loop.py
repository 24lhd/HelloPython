#             Câu lệnh If
# Cú pháp
# if (biểu thức):
#     các câu lệnh


#           Câu lệnh If..elif..else


# if (biểu thức 1):
#     các câu lệnh
# elif (biểu thức 2):
#     các câu lệnh
# elif (biểu thức n):
#     các câu lệnh
# else:
#     các câu lệnh



#   Vòng lặp while

# while (biểu thức):
#     các câu lệnh


# Vòng lặp while thường dùng khi bạn chưa biết trước số lượng vòng lặp cần dùng.
# Ý nghĩa của câu lệnh này là trong khi điều kiện còn đúng thì thực hiện các câu lệnh.
i = 0;
while (i < 10):
    i = i + 1
print(i)

# Bạn có thể dùng while…else trong Python, cú pháp này có tác dụng thực thi các câu lệnh sau khi rời khỏi vòng lặp.

i = 0;
while (i < 10):
    i = i + 1
else:
    print(i)

    # Vòng lặp for

    # for biến lặp in tập hợp:
    #     các câu lệnh

    # Biến lặp có thể là bất cứ biến nào.
    #  Bạn chỉ cần đưa vào một cái tên là Python sẽ tự ngầm hiểu kiểu dữ liệu.
    #  Còn tập hợp có thể là bất kỳ kiểu tập hợp nào

    for letter in 'Python':
        print('Current Letter :', letter)

    fruits = ['banana', 'apple', 1, True]
    for fruit in fruits:
        print('Current fruit :', fruit)

        # Bạn cũng có thể dùng vòng lặp for theo chỉ số.

    fruits = ['banana', 'apple', 'mango']
    for index in range(len(fruits)):
        print('Current fruit :', fruits[index])


        # Cũng giống như vòng lặp while, bạn cũng có thể dùng else cho vòng lặp for.
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, i, j))
            break
    else:
        print(num, 'is a prime number')

        # Câu lệnh Break
        # Khi bạn muốn dừng vòng lặp giữa chừng thì dùng câu lệnh break.

        for letter in 'Python':
            if letter == 'h':
                break
            print('Current Letter :', letter)

        var = 10
        while var > 0:
            print('Current variable value :', var)
            var = var - 1
            if var == 5:
                break

# Câu lệnh Continue
# Câu lệnh continue có tác dụng nhảy sang lần lặp kế tiếp. Các câu lệnh phía sau contine sẽ không được thực thi.

for letter in 'Python':
    if letter == 'h':
        continue
    print('Current Letter :', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)
