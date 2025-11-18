try:
    count = int(input("Сколько чисел вы хотите ввести? "))
    if count <= 0:
        print("Количество чисел должно быть больше нуля.")
    else:
        nums = [int(input(f"Введите число {i+1}: ")) for i in range(count)]

        maximum = max(nums)
        minimum = min(nums)
        average = sum(nums) / count
        greater_avg = sum(1 for n in nums if n > average)

        print("Вывод:")
        print("Результаты:")
        print(f"Максимальное: {maximum}")
        print(f"Минимальное: {minimum}")
        print(f"Среднее: {average}")
        print(f"Чисел больше среднего: {greater_avg}")
except ValueError:
    print("Ошибка: Введите целое число.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
