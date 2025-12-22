text = input("Введите произвольный текст: ")
search_word = input("Введите слово для поиска: ")
if not search_word:
    print("Ошибка: слово для поиска не может быть пустым")
else:
    word_count = text.count(search_word)
    first_index = text.find(search_word)
    cleaned_text = text.replace(search_word, "")
    print(f"\nРезультаты поиска слова '{search_word}':")
    print(f"Количество встреченных слов: {word_count}")
    if first_index >= 0:
        print(f"Индекс первого встреченного слова: {first_index}")
    else:
        print("Слово не найдено в тексте")
    
    print("\nТекст без введенного слова:")
    print(cleaned_text)
