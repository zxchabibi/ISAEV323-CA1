class Box:
    def __init__(self, volume):
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть числом.")
        if volume < 0:
            raise ValueError("Объем не может быть отрицательным.")
        self.volume = volume

    def __str__(self):
        return f"Коробка объемом: {self.volume}"

    def __add__(self, other):
        if not isinstance(other, Box):
            raise TypeError("Можно сложить только объект Box с другим объектом Box.")
        return Box(self.volume + other.volume)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Коробку можно умножить только на целое число.")
        if other < 0:
            raise ValueError("Множитель должен быть неотрицательным целым числом.")
        return Box(self.volume * other)

    def __eq__(self, other):
        if not isinstance(other, Box):
            return NotImplemented
        return self.volume == other.volume

box1 = Box(10)
box2 = Box(25)
box3 = Box(10)
box4 = Box(5)

print(box1)
print(box2)
print(box3)
print(box4)

sum_box = box1 + box2
print(sum_box)

multiplied_box = box4 * 3
print(multiplied_box)

print(box1 == box2)
print(box1 == box3)
print(box2 == box4)

try:
    Box(-5)
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    box1 + "не коробка"
except TypeError as e:
    print(f"Ошибка: {e}")

try:
    box1 * 2.5
except TypeError as e:
    print(f"Ошибка: {e}")
