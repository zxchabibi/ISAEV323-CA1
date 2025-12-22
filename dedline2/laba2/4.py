n = int(input("Введите высоту пирамиды: "))
for i in range(1, n + 1):
    left = ''.join(str(j) for j in range(1, i + 1))
    right = ''.join(str(j) for j in range(i - 1, 0, -1))
    full = left + right
    total = n * 2 - 1
    spaces = ' ' * (n - i)
    print(spaces + full)
