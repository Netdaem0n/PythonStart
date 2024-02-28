# Вариант-1
# n - произвольное число, кол-во чисел в последовательности

x_max = 0  # максимальное число кратное 4, но не кратное 7
k = 0  # счетчик чисел

n = int(input('n = '))

for _ in range(n):
    temp = int(input())  # временная переменная
    if temp % 4 == 0 and temp % 7 != 0:
        k += 1
        x_max = max(x_max, temp)

print('k = ', k)
print('x_max = ', x_max)
