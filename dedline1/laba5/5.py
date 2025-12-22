import random

import string

def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation + ' '

    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
random_chars = generate_random_string(5)
print(random_chars)
msg = input("Введите сообщение для кодирования: ")
n = int(input("Введите число: "))
letters = list(msg)

print(letters)
final_text = f"{generate_random_string(n)}" .join(letters)
print(final_text)