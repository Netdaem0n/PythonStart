# Вариант-1
# x - произвольное число (трехзначное)
# y - произвольное число (трехзначное)

x = int(input('х ='))
y = int(input('y ='))

if (x % 3) == (y % 3):
    # вычислить произведение этих чисел
    print(x * y)
else:
    # иначе вычислить частное этих чисел
    # (разделить большее на меньшее число с точностью два знака после запятой).
    if x > y:
        print(round(x / y, 2))
    else:
        print(round(y / x, 2))

