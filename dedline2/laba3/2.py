text = input("Введите произвольную строку: ")
text = text.lower()
char_counts = {}
for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1
print("Вывод:")
print(char_counts)
