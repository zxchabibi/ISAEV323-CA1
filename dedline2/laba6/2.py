def simple_calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: Деление на ноль!"
    else:
        return "Неизвестный оператор"

result = simple_calculator(10, 5, '*')
print(result)