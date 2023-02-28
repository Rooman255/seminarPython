from logger import input_data, print_data, filter_data, change_data, delete_data

print("""Выберите режим работы:
             1 - запись данных,
             2 - вывод данных,
             3 - поиск данных по параметрам
             4 - изменение данных
             5 - удаление данных
             """)
command_number = int(input("Введите номер команды: "))
while command_number < 1 or command_number > 7:
    print("Введите корректный номер команды: ")
    command_number = int(input("Введите номер команды: "))
if command_number == 1:
    input_data()
elif command_number == 2:
    print_data()
elif command_number == 3:
    print("Введите параметры поиска через '; ': ")
    filter_string = input()
    filter_data(filter_string)
elif command_number == 4:
    change_data()
elif command_number == 5:
    delete_data()
