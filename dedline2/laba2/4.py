try:
    n = int(input("Введите высоту пирамиды (n): "))

    if n < 1:
        print("Высота должна быть положительным числом.")
    else:
        print("Вывод:")
        for i in range(1, n + 1):
            row_str = ""
            for j in range(1, i + 1):
                row_str += str(j)
            for k in range(i - 1, 0, -1):
                row_str += str(k)
            print(row_str)

except ValueError:
    print("Ошибка: Введите целое число.")
