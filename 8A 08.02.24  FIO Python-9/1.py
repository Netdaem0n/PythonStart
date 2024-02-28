# total - Первое число - к-во чисел
# k - счетчик для задания

total = int(input())
k = 0

for _ in range(total):
    temp = int(input())
    if 1 <= (temp // 100) <= 9:
        if temp // 100 == 3 and temp % 5 == 0:
            k = k + 1

print(k)
