tasks = []
while True:
    print("\n1 - Показать все задачи")
    print("2 - Добавить задачу") 
    print("3 - Удалить задачу")
    print("4 - Выйти")
    choice = input("Выбери: ")
    if choice == '1':
        if not tasks:
            print("Нет задач!")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")            
    elif choice == '2':
        new_task = input("Введи задачу: ")
        tasks.append(new_task)
        print("Задача добавлена!")      
    elif choice == '3':
        if not tasks:
            print("Нет задач для удаления!")
        else:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Какую задачу выполнили? ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                print(f'Задача "{removed}" удалена!')
            else:
                print("Неправильный номер!")           
    elif choice == '4':
        print("Пока!")
        break
    else:
        print("Неправильный выбор!")