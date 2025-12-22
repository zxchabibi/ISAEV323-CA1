class Character:  
    def __init__(self, name):
        self.name = name  
    def move(self): 
        print(f"{self.name} идёт")
class Archer(Character):  
    def shoot(self):  
        print(f"{self.name} стреляет из лука")
class Knight(Character):  
    def attack_sword(self):  
        print(f"{self.name} бьёт мечом")
a = Archer("Serious sam")  
b = Knight("Doomslayer") 
a.move()  
a.shoot()  
b.move()  
b.attack_sword()  