# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число
# d - произвольное число

x1 = int(input('Введите число Х1: '))
x2 = int(input('Введите число x2: '))
x3 = int(input('Введите число x3: '))
d = int(input('Введите число d: '))
totall = 0

if (x1 % d == 0) and (x1 % 10 == d):
    totall = totall + 1
if (x2 % d == 0) and (x2 % 10 == d):
    totall = totall + 1
if (x3 % d == 0) and (x3 % 10 == d):
    totall = totall + 1

print('количество чисел, кратных', d, 'и оканчивающихся на цифру', d, '-', totall)
