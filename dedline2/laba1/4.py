from random import randint
secret_number = randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадать!")
guessed = False
while not guessed:
    guess_str = input("Ваша догадка: ")
    guess = int(guess_str)
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print("Угадал!")
        guessed = True 