def replace_string():
  text = input("Введите произвольный текст: ")
  replace_input = input("Введите две строки через пробел (строка1 строка2): ")
  replace_parts = replace_input.split()
  if len(replace_parts) != 2:
    print("Некорректный ввод. Пожалуйста, введите две строки через пробел.")
    return
  string1 = replace_parts[0]
  string2 = replace_parts[1]
  new_text = text.replace(string1, string2)
  print(new_text)
replace_string()