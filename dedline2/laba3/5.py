import string

word_counts = {}
full_text = []

while True:
    line = input()
    if not line:
        break
    full_text.append(line)

text = " ".join(full_text)
cleaned_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
words = cleaned_text.split()

for word in words:
    if word:
        word_counts[word] = word_counts.get(word, 0) + 1

print("Вывод:")
print(f"Статистика слов: {word_counts}")
