class SmartLight:
    def __init__(self):
        self.brightness = 50
        self.color = "white"
        self.__is_on = False
    def turn_on(self):
        self.__is_on = True
        print("Лампочка включена")
    def turn_off(self):
        self.__is_on = False
        print("Лампочка выключена")
    def set_color(self, new_color):
        self.color = new_color
        if self.__is_on:
            print(f"Цвет изменён на {new_color}")
        return self.color
    def status(self):
        s = "включена" if self.__is_on else "выключена"
        return f"Яркость: {self.brightness}, Цвет: {self.color}, Статус: {s}"
a = SmartLight()
print(a.status())
a.turn_on()
a.set_color("красный")
print(a.status())
a.turn_off()