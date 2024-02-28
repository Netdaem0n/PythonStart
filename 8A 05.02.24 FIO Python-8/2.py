# x - произвольное число
# summa - сумма максимального и минимального чисел

x = int(input('Введите число '))
minx = None  # устанавливаем минимум
maxx = None  # устанавливаем максимум
summa = 0

while x != 0:  # пока не получили стоп символ
    if x % 8 == 0:
        if minx:  # проверка существования числа minx
            minx = min(minx, x)
        else:
            minx = x
        if maxx:  # проверка существования числа maxx
            maxx = max(maxx, x)
        else:
            maxx = x
    x = int(input('Введите число '))

if maxx and minx:  # проверка существования числа minx и maxx
    summa = maxx + minx
print('Сумма максимального и минимального чисел, кратных 8:', summa)
