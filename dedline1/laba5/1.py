print ("Введите два числа")
n1 = float(input("Первое число :"))
n2 = float(input("Второе число :"))
print("\nРезультаты вычислений")
print(f"{n1} + {n2} = {n1 + n2}")
print(F"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
if n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print(f"{n1} / {n2} = Ошибка: деление на ноль!")

