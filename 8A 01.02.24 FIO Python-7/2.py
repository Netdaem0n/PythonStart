# Вариант-1
# n - произвольное число, кол-во учеников

flag = 0  # 1 - 10 из 10, 0 - 10 баллов никто не получил
k = 0  # счетчик двоек

n = int(input('n = '))

for _ in range(n):
    temp = int(input())  # временная переменная
    if temp < 5:
        k += 1
    elif temp == 10:
        flag = 1

print('Кол-во «2» =', k)

if flag == 1:  # проверка флага
    print('YES')
else:
    print('NO')
