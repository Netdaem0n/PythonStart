# total - Первое число - к-во чисел
# k - сумма двухзначных чисел

total = int(input())
k = 0

for _ in range(total):
    temp = int(input())
    if 1 <= (temp // 10) <= 9:
        if ((temp // 10) - (temp % 10)) == 2:
            k = k + temp

print(k)
