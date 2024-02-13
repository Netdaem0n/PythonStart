# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число

x1 = int(input('Введите число Х1: '))
x2 = int(input('Введите число x2: '))
x3 = int(input('Введите число x3: '))
totall = 0

if (x1 % 8 == 0) and (x1 % 10 == 4):
    totall = totall + 1
if (x2 % 8 == 0) and (x2 % 10 == 4):
    totall = totall + 1
if (x3 % 8 == 0) and (x3 % 10 == 4):
    totall = totall + 1

print('количество чисел, кратных 8 и оканчивающихся на цифру 4 -', totall)
