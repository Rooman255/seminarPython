# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def simple_num(n):
    n = abs(n)
    if n < 2: return 'No'
    for i in range(2, n):
        if n % i == 0:
            return 'No'
    return 'Yes'
n = int(input("введите число: "))
print(simple_num(n))