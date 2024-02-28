# Вариант-1
# n - произвольное число, кол-во чисел в последовательности

summa = 0  # сумма чисел, удовлетворяющих условию
n = int(input('n = '))

for _ in range(n):
    temp = int(input())  # временная переменная
    if temp % 10 == 7:
        summa += temp

print('sum = ', summa)
