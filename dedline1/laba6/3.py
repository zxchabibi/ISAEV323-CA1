def step_text():
  text = input("Введите произвольный текст: ")
  try:
    step = int(input("Введите шаг: "))
  except ValueError:
    print("Некорректный ввод. Шаг должен быть целым числом.")
    return
  new_text = text[::step]
  print(new_text)
step_text()