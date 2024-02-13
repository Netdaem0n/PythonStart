# x - произвольное число

x = int(input('Введите число X '))

if (x % 2 != 0) and (x % 3 == 0):
    print(x ** 2 - 50)
else:
    print((x - 50) * 2)
