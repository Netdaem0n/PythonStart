x = int(input('Введите число - часы (0 - 24): '))
# (утро, день, вечер, ночь)

if (x >= 5) and (x <= 12):
    print('Утро')
elif (x >= 13) and (x <= 17):
    print('день')
elif (x >= 18) and (x <= 22):
    print('вечер')
elif ((x >= 0) and (x <= 4)) or ((x >= 23) and (x <= 24)):
    print('ночь')
