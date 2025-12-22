text = input("Введите текст: ")
segment = input("Введите отрезок (число1 число2): ")
start, end = map(int, segment.split())
result = text[start:end]
print(result)