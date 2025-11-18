math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}

print(f"Все три курса: {math_students & physics_students & cs_students}")
print(f"Только один курс: {(math_students - (physics_students | cs_students)) | (physics_students - (math_students | cs_students)) | (cs_students - (math_students | physics_students))}")
print(f"Математика но не физика: {math_students - physics_students}")
print(f"Всего студентов: {len(math_students | physics_students | cs_students)}")
    