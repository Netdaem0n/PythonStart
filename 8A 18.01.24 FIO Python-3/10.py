# x - произвольное число
# y - произвольное число
# vibor - символ 1,2 или 3


x = int(input())
y = int(input())
vibor = input()

if vibor == '1':
    x = x - y
    print('Новые числа: х=', x, 'у=', y)
elif vibor == '2':
    x = x + y
    print('Новые числа: х=', x, 'у=', y)
elif vibor == '3':
    x, y = y, x
    print('Новые числа: х=', x, 'у=', y)
