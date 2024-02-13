# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число

x1 = int(input('Введите число Х1: '))
x2 = int(input('Введите число x2: '))
x3 = int(input('Введите число x3: '))
totall = 0

if x1 % 2 == 0:
    totall = totall + 1
if x2 % 2 == 0:
    totall = totall + 1
if x3 % 2 == 0:
    totall = totall + 1

print('Количество четных чисел -', totall)
