fruits = {'яблок': 5,
		'бананы': 3,
        'апельсины': 10,
		'арбузы': 33}
print("Начальное количество фруктов и арбузов: ")
for fruit, count in fruits.items():
    print(f"За прилавком есть {count} {fruit}")
print()
fruits['яблок'] -= 2
print("Вы продали два яблока")
fruits['арбузы'] = 0
print("Поганый Ашот Похититель Арбузов украл как не странно все ваши арбузы!")
print()
print("Конечное количество фруктов и арбузов: ")
for fruit, count in fruits.items():
    print(f"За прилавком осталось {count} {fruit}")