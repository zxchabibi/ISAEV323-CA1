n = int(input("Введите число n: "))
num = 0
for i in range(1, n+1):
    num += i
print(f"Сумма чисел от 1 до {n} = {num}")