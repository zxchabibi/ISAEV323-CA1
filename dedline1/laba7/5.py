import math
expression = input("Введите выражение (число1 знак число2 через пробел): ")
parts = expression.split()
try:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '%':
        result = num1 % num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '%%':
        result = (num1 / 100) * num2
    elif operator == '/**':
        result = math.sqrt(num1)
    else:
        raise ValueError
    print(result)
except:
    print("Ошибка")

