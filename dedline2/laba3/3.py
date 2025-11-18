phone_book = {"Александр": "123-45-67", "Мария": "987-65-43", "Иван": "555-11-22", "Елена": "777-88-99"}
while True:
    print("\n1-Показать\n2-Добавить\n3-Удалить\n4-Выйти")
    c = input("Действие: ")
    if c == '1': print('\n'.join([f"Имя: {n}, Телефон: {p}" for n,p in phone_book.items()]) if phone_book else "Пусто.")
    elif c == '2':
        n = input("Имя: ")
        print(f"'{n}' уже есть.") if n in phone_book else (phone_book.update({n: input("Телефон: ")}), print(f"'{n}' добавлен."))
    elif c == '3':
        n = input("Имя: ")
        print(f"'{n}' удален." if phone_book.pop(n, None) else f"'{n}' не найден.")
    elif c == '4': print("Выход."); exit()
    else: print("Ошибка.")
