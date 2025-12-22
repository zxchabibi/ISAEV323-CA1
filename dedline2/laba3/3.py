phone_book = {'Мама': '123456', 'Папа': '654321', 'Друг': '111222'}
while True:
    print("\n1 - показать все контакты")
    print("2 - добавить контакт") 
    print("3 - удалить контакт")
    print("4 - выйти")   
    choice = input("Выбери действие: ")
    if choice == '1':
        print("\nТелефонная книга:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")         
    elif choice == '2':
        name = input("Введи имя: ")
        if name in phone_book:
            print("Такой контакт уже есть!")
        else:
            phone = input("Введи телефон: ")
            phone_book[name] = phone
            print("Контакт добавлен!")         
    elif choice == '3':
        name = input("Введи имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт удален!")
        else:
            print("Такого контакта нет!")  
    elif choice == '4':
        print("Пока!")
        exit()
    else:
        print("Неправильный выбор!")