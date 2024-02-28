# minutes - произвольное кол-во минут
# t_hours - кол-во часов
# t_minutes - кол-во минут

minutes = int(input())
t_hours = minutes // 60
t_minutes = minutes % 60
print('час =', t_hours)
print('мин =', t_minutes)
