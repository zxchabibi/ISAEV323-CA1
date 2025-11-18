
fio = input("Введите ФИО через пробел: ")
try:
    surname, name, patronymic = fio.split()
except ValueError:
    print("Ошибка: Введите ФИО полностью, разделив пробелами.")
else:
    print(surname.upper())
    print(name.upper())
    print(patronymic.upper())