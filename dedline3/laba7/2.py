class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.__salary = value
emp = Employee("John", 50000)
print(emp.salary) 
try:
    emp.salary = -100  
except ValueError as e:
    print(f"Ошибка: {e}")
emp.salary = 60000  
print(emp.salary)  