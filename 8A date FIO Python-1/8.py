x = int(input('Введите трех значное число '))
ct = x // 100
x = x - ct * 100
de = x // 10
ed = x % 10
print('Разложили на числа -', ct, de, ed)
tot_3 = ct + de + ed
print('Cумма цифр заданного трехзначного числа', tot_3)
