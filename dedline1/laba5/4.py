print("Введите 5 чисел: ")
numbers = []
for i in range(5):
    n = float(input(f"Введите число {i+1}: "))
    numbers.append(n)
min_n = min(numbers)
max_n = max(numbers)
print(f"\nМинимальное число: {min_n}")
print(f"\nМaксимальное число: {max_n}")