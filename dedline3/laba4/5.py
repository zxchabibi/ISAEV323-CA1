class Product:
    def __init__(self, a, b):
        self.name = a
        self.price = b
class Order:
    def __init__(self):
        self.items = []  
        self.status = "новый"
        self.delivery = None  
    def add(self, i):
        self.items.append(i)
class DeliveryPerson:
    def __init__(self, s):
        self.speed = s
class Courier(DeliveryPerson):  
    def call(self):
        print("Звоню")
p = Product("Товар", 100)
o = Order()
o.add(p)  
c = Courier(5)
o.delivery = c 
print(f"Статус: {o.status}")
print(f"Скорость: {o.delivery.speed}")
o.delivery.call()  