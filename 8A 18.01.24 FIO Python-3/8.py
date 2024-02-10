dlina = int(input('Введите длину: '))
shirina = int(input('Введите ширину: '))
vibor = input('Код программы (P или S): ')

if vibor == 'P':
    print(2 * (dlina + shirina))
elif vibor == 'S':
    print(dlina * shirina)
else:
    print('Ошибка, введите P или S')
