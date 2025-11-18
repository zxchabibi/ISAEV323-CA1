tasks = []
while True:
    print("\n--- Меню To-Do списка ---\n1 - Показать все задачи\n2 - Добавить задачу\n3 - Отметить задачу как выполненную (удалить)\n4 - Выйти")
    c = input("Выберите опцию: ")

    if c == '1':
        print("\nВаши задачи:")
        print("Список задач пуст." if not tasks else '\n'.join(f"{i+1}. {t}" for i, t in enumerate(tasks)))
    elif c == '2':
        t = input("Введите описание новой задачи: ")
        tasks.append(t)
        print(f'Задача "{t}" добавлена.')
    elif c == '3':
        if not tasks: print("Нет задач для удаления."); continue
        print("\nВаши задачи:\n" + '\n'.join(f"{i+1}. {t}" for i, t in enumerate(tasks)))
        try:
            n = int(input("Какую задачу выполнили? "))
            if 1 <= n <= len(tasks): print(f'задача "{tasks.pop(n-1)}" удалена!')
            else: print("Неверный номер задачи.")
        except ValueError: print("Некорректный ввод.")
    elif c == '4': print("Выход из программы."); break
    else: print("Неверный выбор.")
