def direction():

 d=input("Введите направление (left, right, straight, back):")

 if d=="left":print("Иду влево")
 elif d=="right":print("Иду вправо")
 elif d=="straight":print("Иду прямо")
 elif d=="back":print("Иду назад")
 else:print("Неправильное направление")
direction()