numbers = [15, 67, 42, 88, 31, 90, 23, 76, 55, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

big_numbers = []
for num in numbers:
    if num > 50:
        big_numbers.append(num)
print(f"Все числа: {numbers}")
print(f"Четные числа: {even_numbers}")
print(f"Числа больше 50: {big_numbers}")