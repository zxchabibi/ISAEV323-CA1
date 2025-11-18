students = [
    ("Мария", 20, 4.8),
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Иван", 19, 3.8),
    ("Елена", 23, 4.9)
]

print("Студенты старше 20 лет:")
older_students = [f"- {n} ({a}), средний балл: {s}" for n, a, s in students if a > 20]
print('\n'.join(older_students) if older_students else "Нет студентов старше 20 лет.")

best_student = max(students, key=lambda s: s[2])
print(f"\nЛучший студент: {best_student[0]}, средний балл: {best_student[2]}")

print("\nОтсортированный список студентов по имени:")
[print(f"- {n} (Возраст: {a}, Средний балл: {s})") for n, a, s in sorted(students, key=lambda s: s[0])]
