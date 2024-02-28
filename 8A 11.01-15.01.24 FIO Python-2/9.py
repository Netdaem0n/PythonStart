# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число
# totall - счетчик чисел по условию

x1 = int(input())
x2 = int(input())
x3 = int(input())
totall = 0

if (x1 % 8 == 0) and (x1 % 10 == 4):
    totall = totall + 1
if (x2 % 8 == 0) and (x2 % 10 == 4):
    totall = totall + 1
if (x3 % 8 == 0) and (x3 % 10 == 4):
    totall = totall + 1

print('результат =', totall)
