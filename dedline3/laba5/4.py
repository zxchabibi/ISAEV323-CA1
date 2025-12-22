class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def strike(self, target):
        target.health -= self.attack_power
knight = Hero("арт", 100, 20)
rogue = Hero("шалун", 80, 15)
knight.strike(rogue) 
rogue.strike(knight)  
print(f"{knight.name}: {knight.health}")  
print(f"{rogue.name}: {rogue.health}")    