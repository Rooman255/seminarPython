# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
'''
list1 = [1, 1, 2, 0, -1, 3, 4, 4]
unic = []
count = 0
for element in list1:
    if element not in unic:
        unic.append(element)

print(len(unic))
'''

list1 = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list1)))

# list1 = list(map(int, input('Введите числа: ').split(' ')))
# print(list1)
