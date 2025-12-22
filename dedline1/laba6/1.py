fio = input("Введите ФИО через пробел: ")
parts = fio.split()
formatted_surname = parts[0].capitalize()
formatted_name = parts[1].capitalize()
formatted_patronymic = parts[2].capitalize()
formatted_fio = formatted_surname + " " + formatted_name + " " + formatted_patronymic
print("Добро пожаловать", formatted_fio)