n = int(input("Введите число: "))
print(f"Таблица умножения для числа {n}:")
for i in range(1, 11):
    result = n * i
    print(f"{n} * {i} = {result}")