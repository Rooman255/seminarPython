# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def revert(n):
    if n ==0:
        return ''
    k = int(input('введите элемент: '))
    return revert(n-1) + f' {k}' #f"{', ' if n > 1 else ''} {k}"

l = int (input('введите числа: '))
print(revert(l))