import re
text = input("Введите текст: ").lower()
words = re.findall(r'[a-zA-Z]+', text)
unique_words = set(words)
print(f"Уникальные слова: {len(unique_words)}")
long_words = {w for w in unique_words if len(w) > 5}
print(f"Длинные слова: {long_words}")
has_keywords = "python" in unique_words or "programming" in unique_words
print(f"Найдены ключевые слова: {has_keywords}")
