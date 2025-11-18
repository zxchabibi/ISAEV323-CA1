def find_word():
 t=input("Введите текст:")
 w=input("Введите слово:")
 if w in t:print(f"Слово есть в тексте. Количество: {t.count(w)}")
 else:print("Слова нет в тексте")

find_word()