n = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)
max_num = numbers[0]
min_num = numbers[0]
sum_num = 0
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
    sum_num += num
average = sum_num / n
count = 0
for num in numbers:
    if num > average:
        count += 1
print("Результаты:")
print(f"Максимальное: {max_num}")
print(f"Минимальное: {min_num}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {count}")