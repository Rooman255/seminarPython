# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

a = int(input('введите a:'))
b = 0
c = 0
d = 1
i = 2
while b < a:
    b = c + d
    c = d
    d = b
    i+=1
    if c > a:
        i = 0
if i == 0:
    print(-1)
else:
    print(i)
