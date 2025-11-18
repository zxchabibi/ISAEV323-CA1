fruits = {
    "яблоко": 5,
    "банан": 3,
    "апельсин": 10,
    "арбуз": 33
}
for fruit, count in fruits.items():
    print(f"за прилавком есть {count} {fruit}")

fruits["яблоко"] -= 2

fruits["арбуз"] = 0

print("\n--- Итого ---")
for fruit, count in fruits.items():
    print(f"За прилавком осталось {count} {fruit}")
