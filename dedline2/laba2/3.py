text = input("Введите текст: ")
letters_count = 0
digits_count = 0
punctuation_count = 0
spaces_count = 0
punctuation_chars = ".,!?:;"
for char in text:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1
    elif char == ' ':
        spaces_count += 1
    elif char in punctuation_chars:
        punctuation_count += 1
print(f"Вывод:")
print(f"букв = {letters_count}")
print(f"цифр = {digits_count}")
print(f"знаков препинания = {punctuation_count}")
print(f"пробелов = {spaces_count}")

