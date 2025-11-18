def search_and_replace():
    text = input("Введите произвольный текст: ")
    word = input("Введите слово для поиска: ")
    count = text.lower().split().count(word.lower())  
    try:
        index = text.lower().split().index(word.lower())
    except ValueError:
        index = -1 
    new_text = text.replace(word, "**")
    print(f"Количество встреченных слов: {count}")
    if index != -1:
        print(f"Индекс первого встреченного слова: {index}")
    else:
        print(f"Слово не найдено")
    print(f"Текст без слова: {new_text}")

search_and_replace()

