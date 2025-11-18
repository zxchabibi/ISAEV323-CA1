count_numbers = 0
current_input = -1 

while current_input != 0:
    input_str = input("Введите число (0 для завершения): ")
    current_input = int(input_str)
    
    if current_input != 0:
        count_numbers = count_numbers + 1
print(f"Вы ввели {count_numbers} чисел до нуля.")
