products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}
max_sold = 0
best_sold_name = ""
for name, info in products.items():
    if info["sold"] > max_sold:
        max_sold = info["sold"]
        best_sold_name = name
print(f"Самый продаваемый: {best_sold_name}")
total = 0
for name, info in products.items():
    total += info["price"] * info["sold"]
print(f"Общая выручка: {total}")
max_revenue = 0
best_revenue_name = ""
for name, info in products.items():
    revenue = info["price"] * info["sold"]
    if revenue > max_revenue:
        max_revenue = revenue
        best_revenue_name = name
print(f"Самый прибыльный: {best_revenue_name}")