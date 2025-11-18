try:
    num = int(input("Введите число: "))
    print("Вывод:")
    for i in range(1, 11):
        print(f"{num} * {i} = {num * i}")
except ValueError:
    print("Ошибка: Введите целое число.")
