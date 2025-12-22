class вектор:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"вектор({self.x}, {self.y})"
    def __add__(self, other):
        return вектор(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return вектор(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return вектор(self.x * other, self.y * other)
        elif isinstance(other, вектор):
            return self.x * other.x + self.y * other.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
v1 = вектор(2, 3)
v2 = вектор(4, 1)
print(v1 + v2)        
print(v1 - v2)         
print(v1 * 3)          
print(v1 * v2)          
print(v1 == вектор(2, 3))  