# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def number(A, B):
    if B == 0:
        return 1
    return A * number(A, B -1)
print(number(int(input('Число A ')), int(input('Число B '))))
