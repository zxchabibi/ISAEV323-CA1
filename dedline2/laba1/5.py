user_string = input("Введите строку: ")
vowels = "aoeyuiv"
filtered_string = ""
i = 0
while i < len(user_string):
    char = user_string[i]
    if char.lower() not in vowels:
        filtered_string += char
    i += 1
print(f"Строка без гласных: {filtered_string}")
