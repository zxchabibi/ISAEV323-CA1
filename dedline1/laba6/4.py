def substring_from_range():
    text = input("Введите произвольный текст: ")
    range_input = input("Введите отрезок (число1 число2): ")
    try:
        start, end = map(int, range_input.split())
        if not (1 <= start <= len(text) and 1 <= end <= len(text) and start <= end):
            print("Некорректный диапазон.")
            return
        substring = text[start-1:end]
        print(" ".join(substring))
    except ValueError:
        print("Некорректный ввод. Введите два целых числа через пробел.")
substring_from_range()