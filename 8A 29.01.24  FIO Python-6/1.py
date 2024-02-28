# Вариант-1
# n - произвольное число, кол-во чисел в последовательности

k = 0  # счетчик двухзначных чисел
n = int(input('n = '))

for i in range(n):
    temp = input()
    if len(temp) == 2:
        k = k + 1
print('k =', k)
