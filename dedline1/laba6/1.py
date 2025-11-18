def format_fio():
  fio = input("Введите ФИО через пробел: ")
  fio_parts = fio.split()
  if len(fio_parts) != 3:
    print("Некорректный ввод. Пожалуйста, введите Фамилию Имя Отчество через пробел.")
    return
  formatted_fio = []
  for part in fio_parts:
    formatted_part = part[0].upper() + part[1:].lower()
    formatted_fio.append(formatted_part)
  print("Добро пожаловать", " ".join(formatted_fio))
format_fio()
