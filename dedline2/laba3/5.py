text = ""
while True:
    line = input()
    if line == "":
        break
    text += line + " "
words = text.split()
stats = {}
for word in words:
    clean_word = word.lower().strip('.,!?;:')
    if clean_word in stats:
        stats[clean_word] += 1
    else:
        stats[clean_word] = 1
print(f"Статистика слов: {stats}")