# Требуется определить, можно ли от шоколадки размером n ×m долек отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры:
# Примечание: каждое считывание производится с новой строки
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('количество n долек:'))
m = int(input('количество m долек:'))
k = int(input('количество k долек:'))
if(m*n) > k and (k%n == 0 or k%m == 0):
    print('yes')
else:
    print('no')
