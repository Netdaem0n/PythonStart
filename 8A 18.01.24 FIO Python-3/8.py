# dlina - произвольное число длина
# shirina - произвольное число ширина
# vibor - произвольное число периметр или площадь

dlina = int(input())
shirina = int(input())
vibor = input()

if vibor == 'P':
    print('P =', 2 * (dlina + shirina))
elif vibor == 'S':
    print('S =', dlina * shirina)
else:
    print('Ошибка, введите P или S')
