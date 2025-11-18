products = {
    "Ноутбук": {"price": 50000, "sold": 15},
    "Мышь": {"price": 1000, "sold": 45},
    "Клавиатура": {"price": 2500, "sold": 30},
    "Монитор": {"price": 30000, "sold": 8}
}

best_selling_item_name = max(products, key=lambda item: products[item]['sold'])
print(f"Самый продаваемый товар (по количеству): {best_selling_item_name}")

total_revenue = sum(data['price'] * data['sold'] for data in products.values())
print(f"Общая выручка магазина: {total_revenue} рублей")

highest_revenue_item_name = max(products, key=lambda item: products[item]['price'] * products[item]['sold'])
print(f"Товар, принесший наибольшую выручку: {highest_revenue_item_name}")
