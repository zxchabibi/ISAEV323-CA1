temperatures = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures) / len(temperatures)
days_above = 0
for temp in temperatures:
    if temp > avg_temp:
        days_above += 1
sorted_temps = sorted(temperatures)
fahrenheit = []
for temp in temperatures:
    f = temp * 9/5 + 32
    fahrenheit.append(f)
print(f"Температуры: {temperatures}")
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")
print(f"Средняя: {avg_temp}°C")
print(f"Дней выше средней: {days_above}")
print(f"Отсортированные: {sorted_temps}")
print(f"Фаренгейты: {fahrenheit}")