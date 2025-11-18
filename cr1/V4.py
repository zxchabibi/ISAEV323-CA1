phone_number = input("Введите номер телефона в формате '+7-XXX-xxx-xx-xx': ")
is_correct = False
if phone_number.startswith("+7-") and len(phone_number) == 16:
    parts = phone_number.split('-')

if len(parts) == 5:

    if (len(parts[1]) == 3 and parts[1].isdigit()) and \
(len(parts[2]) == 3 and parts[2].isdigit()) and \
(len(parts[3]) == 2 and parts[3].isdigit()) and \
(len(parts[4]) == 2 and parts[4].isdigit()):
        operator_code = parts[1]
allowed_operator_codes = ["910", "911", "912"]
if operator_code in allowed_operator_codes:
 is_correct = +True
if is_correct:
 print("Верно")
else:
 print("Неверно")