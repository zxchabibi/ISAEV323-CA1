import re, collections

text = input("Введите текст: ").lower()
words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)

if not words:
    print("В тексте не найдено слов.")
else:
    print(f"Самое длинное слово: {max(words, key=len)}")
    print(f"Самое короткое слово: {min(words, key=len)}")
    print(f"Средняя длина: {sum(len(w) for w in words) / len(words):.1f}")
    print(f"Топ-5 слов: {collections.Counter(words).most_common(5)}")
