temps = [15, 18, 12, 20, 16, 14, 19, 17, 13, 21, 15, 16, 18, 20]
print(f"Температуры: {temps}")

avg = sum(temps) / len(temps)

print(f"Максимальная: {max(temps)}°C")
print(f"Минимальная: {min(temps)}°C")
print(f"Средняя: {avg:.1f}°C")
print(f"Дней выше средней: {sum(1 for t in temps if t > avg)}")
print(f"Отсортированный список: {sorted(temps)}")
print(f"Температуры в Фаренгейтах: {[round((t * 9/5) + 32, 1) for t in temps]}")
