import random

original_numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Исходный список: {original_numbers}")

even_numbers = [num for num in original_numbers if num % 2 == 0]
print(f"Четные числа: {even_numbers}")

greater_than_50 = [num for num in original_numbers if num > 50]
print(f"Числа больше 50: {greater_than_50}")
