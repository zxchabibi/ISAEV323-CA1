grades = []
grades.append(5)
grades.append(4)
grades.append(3)
grades.append(5)
grades.append(2)

print(f"Текущие оценки: {grades}")

if grades:
    grades.pop(0)
if grades:
    grades.pop()

if grades:
    average_grade = sum(grades) / len(grades)
    print(f"Средний балл: {average_grade}")
else:
    print("Список оценок пуст, невозможно посчитать средний балл.")

print(f"Итоговые оценки: {grades}")
