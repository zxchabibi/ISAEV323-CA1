try:
    n = int(input("Введите число n: "))
    if n < 1:
        print("Пожалуйста, введите положительное целое число.")
    else:
        total_sum = n * (n + 1) // 2
        sum_components = " + ".join(str(i) for i in range(1, n + 1))
        print(f"Вывод: {total_sum} ({sum_components})")
except ValueError:
    print("Ошибка: Введите целое число.")
