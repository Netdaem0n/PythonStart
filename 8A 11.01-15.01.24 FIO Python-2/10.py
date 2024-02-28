# x1 - произвольное число
# x2 - произвольное число
# x3 - произвольное число
# d - произвольное число
# totall - счетчик чисел по условию


x1 = int(input())
x2 = int(input())
x3 = int(input())
d = int(input())
totall = 0

if (x1 % d == 0) and (x1 % 10 == d):
    totall = totall + 1
if (x2 % d == 0) and (x2 % 10 == d):
    totall = totall + 1
if (x3 % d == 0) and (x3 % 10 == d):
    totall = totall + 1

print('результат =', totall)
