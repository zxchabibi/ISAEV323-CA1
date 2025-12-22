class Student:
    def __init__(self, name, average_score):
        self.name = name
        self.average_score = average_score
    def is_excellent(self):
        return self.average_score == 5
student1 = Student("Vasya", 4.5)
student2 = Student("Petya", 5)
print(student1.is_excellent())  
print(student2.is_excellent())  