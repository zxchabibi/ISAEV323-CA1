user_string = input("Введите строку для проверки на палиндром: ")

cleaned_string = ""
index_clean = 0
while index_clean < len(user_string):
    char = user_string[index_clean]
    if char != ' ':
        cleaned_string = cleaned_string + char.lower()
    index_clean = index_clean + 1

left_index = 0
right_index = len(cleaned_string) - 1
is_palindrome = True
while left_index < right_index:
    if cleaned_string[left_index] != cleaned_string[right_index]:
        is_palindrome = False
        break 
    left_index = left_index + 1
    right_index = right_index - 1
if is_palindrome:
    print("да, это палиндром")
else:
    print("нет, это не палиндром")