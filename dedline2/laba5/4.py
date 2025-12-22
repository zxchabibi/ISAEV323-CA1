text = input("Введите текст: ")
words = text.lower().split()
unique_words = set(words)
long_words = set()
for word in unique_words:
    if len(word) > 5:
        long_words.add(word)
has_keywords = "python" in unique_words or "programming" in unique_words
print(f"Уникальные слова: {len(unique_words)}")
print(f"Длинные слова: {long_words}")
print(f"Найдены ключевые слова: {has_keywords}")