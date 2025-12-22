import math

route = [(0, 0), (2, 4), (5, 8), (10, 8), (12, 5)]

print(f"Анализ GPS-трека:")
print(f"Маршрут: {route}")

total_length = 0.0
max_segment_length = -1.0
longest_segment_start = None
longest_segment_end = None

if len(route) >= 2:
    for i in range(1, len(route)):
        p1 = route[i-1]
        p2 = route[i]

        x1, y1 = p1
        x2, y2 = p2

        segment_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        total_length += segment_length

        if segment_length > max_segment_length:
            max_segment_length = segment_length
            longest_segment_start = p1
            longest_segment_end = p2
else:
    print("\nМаршрут слишком короткий для расчета длины и перегонов (требуется как минимум 2 точки).")

is_closed = False
if len(route) > 0:
    is_closed = (route[0] == route[-1])

print(f"\n1. Общая длина маршрута: {total_length:.2f}")

print(f"\n2. Самый длинный перегон:")
if longest_segment_start is not None:
    print(f"   Начало: {longest_segment_start}")
    print(f"   Конец: {longest_segment_end}")
    print(f"   Длина: {max_segment_length:.2f}")
else:
    print("   Не удалось определить перегоны (маршрут состоит менее чем из двух точек).")

print(f"\n3. Маршрут {'замкнут' if is_closed else 'не замкнут'}.")
