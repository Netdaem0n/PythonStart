# x - произвольное целое трехзначное число
# y - произвольное целое трехзначное число
# z - произвольное целое трехзначное число
# temp - минимальное число

x = int(input())
y = int(input())
z = int(input())
temp = 0

if x > y:
    temp = y
else:
    temp = x
if temp > z:
    temp = z

print('минимальное число =', temp)
