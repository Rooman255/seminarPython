# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_num = int(input('введите первое число: '))
dif_num = int(input('введите разность чисел: '))
len_num = int(input('введите длину массива: '))
for i in range(len_num):
    print(first_num + i * dif_num)