# Требуется вывести все целые степени двойки (т.е. числа вида 2k ), не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input('введите N:'))
list = []
k = 0
while 2**k < N:
    list.append(2**k)
    k+=1
print(*list) 