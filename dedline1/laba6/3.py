text = input("Введите текст: ")
step = int(input("Введите шаг: "))
result = ""
for i in range(0, len(text), step):
    result += text[i]
print(result)