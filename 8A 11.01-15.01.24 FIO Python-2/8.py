# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число
# totall - количество четных чисел

x1 = int(input())
x2 = int(input())
x3 = int(input())
totall = 0

if x1 % 2 == 0:
    totall = totall + 1
if x2 % 2 == 0:
    totall = totall + 1
if x3 % 2 == 0:
    totall = totall + 1

print('кол-во четных чисел =', totall)
