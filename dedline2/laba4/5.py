text = input("Введите текст: ")
words = text.split()
clean_words = []
for word in words:
    clean_word = word.lower().strip('.,!?;:')
    if clean_word:
        clean_words.append(clean_word)
longest = max(clean_words, key=len)
shortest = min(clean_words, key=len)
total_length = 0
for word in clean_words:
    total_length += len(word)
avg_length = total_length / len(clean_words)
word_count = {}
for word in clean_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
top_5 = sorted_words[:5]
print(f"Самое длинное слово: {longest}")
print(f"Самое короткое слово: {shortest}")
print(f"Средняя длина: {avg_length}")
print(f"Топ-5 слов: {top_5}")