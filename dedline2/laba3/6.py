from random import randint
name = input("Введите имя ларька: ")
print(f"CRM система Ларька {name}")
counter = {'Яблоко': {'max': 50, 'current': 20}, 'Банан': {'max': 30, 'current': 15}}
store = {'Яблоко': {'max': 200, 'current': 100}, 'Банан': {'max': 150, 'current': 80}}
price = {'Яблоко': {'sale_price': 50, 'purchase_price': 30}, 'Банан': {'sale_price': 40, 'purchase_price': 25}}
money = 1000
day = 1
while day <= 10 and money > 0:
    print(f"\n--- День {day} ---")
    print(f"Деньги: {money}")
    if randint(1, 100) <= 20:
        if counter:
            stolen_fruit = list(counter.keys())[randint(0, len(counter)-1)]
            stolen_percent = randint(50, 100) / 100
            stolen_amount = int(counter[stolen_fruit]['current'] * stolen_percent)
            counter[stolen_fruit]['current'] -= stolen_amount
            print(f"Ашот украл {stolen_amount} {stolen_fruit}!")
    for fruit in list(counter.keys()):
        if counter[fruit]['current'] > 0:
            if randint(1, 100) <= 60:
                sold = randint(1, min(5, counter[fruit]['current']))
                counter[fruit]['current'] -= sold
                money += sold * price[fruit]['sale_price']
                print(f"Продано {sold} {fruit}")
    for fruit in price:
        change = randint(-5, 5)
        price[fruit]['sale_price'] += change
        price[fruit]['purchase_price'] += change
        print(f"Цена на {fruit} изменилась на {change}")
    if input("Переместить фрукты? (да/нет): ") == 'да':
        fruit = input("Какой фрукт: ")
        if fruit in store:
            amount = int(input("Сколько: "))
            if store[fruit]['current'] >= amount:
                if counter[fruit]['current'] + amount <= counter[fruit]['max']:
                    store[fruit]['current'] -= amount
                    counter[fruit]['current'] += amount
                    print(f"Перемещено {amount} {fruit}")
                else:
                    print("Не поместится на прилавке!")
            else:
                print("Не хватает фруктов за прилавком!")
        else:
            print("Нет такого фрукта!")
    if input("Купить фрукты? (да/нет): ") == 'да':
        fruit = input("Какой фрукт: ")
        if fruit in price:
            amount = int(input("Сколько: "))
            cost = amount * price[fruit]['purchase_price']
            if money >= cost:
                money -= cost
                if fruit in store:
                    store[fruit]['current'] += amount
                else: 
                    store[fruit] = {'max': 200, 'current': amount}
                    counter[fruit] = {'max': 50, 'current': 0}
                    price[fruit] = {'sale_price': 60, 'purchase_price': 40}
                print(f"Куплено {amount} {fruit}")
            else:
                print("Не хватает денег!")
        else:
            print("Не продаем такой фрукт!")
    day += 1
if money <= 0:
    print("Банкрот! На арбузные плантации...")
else:
    print("Поздравляем! Ашот пойман!")