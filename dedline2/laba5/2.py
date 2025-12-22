students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Иван", 20, 4.1),
    ("Ольга", 23, 4.3)
]
print("Студенты старше 20 лет:")
for name, age, score in students:
    if age > 20:
        print(f"- {name} ({age}), средний балл: {score}")
best_student = max(students, key=lambda x: x[2])
print(f"\nЛучший студент: {best_student[0]}, средний балл: {best_student[2]}")
sorted_students = sorted(students, key=lambda x: x[0])
print("\nОтсортированные студенты:")
for name, age, score in sorted_students:
    print(f"- {name} ({age}), средний балл: {score}")