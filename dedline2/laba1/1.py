original_number = int(input("Введите положительное целое число: "))
sum_of_digits = 0
working_number = original_number

while working_number > 0:
 digit = working_number % 10
 sum_of_digits += digit
 working_number //= 10

print(f"Сумма цифр числа {original_number}: {sum_of_digits}")