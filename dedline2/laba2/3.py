text = input("Введите текст: ")
let = 0
digit = 0
punct = 0
spac = 0
letters ='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
puncts = '.,!&:;'
spaces = ' '
for char in text:
    if char in letters:
        let += 1
    elif char in digits:
        digit += 1
    elif char in puncts:
        punct += 1
    elif char in spaces:
        spac += 1
print("n\Результат анализа текста: ")
print(f"Букв:{let}")
print(f"Цифр:{digit}")
print(f"Знаков препинания:{punct}")
print(f"Пробелов:{spac}")