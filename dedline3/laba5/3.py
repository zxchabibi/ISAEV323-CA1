class A:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Животное издает звук")
class Dog(A):
    def make_sound(self):
        print("Гав!")
class Cat(A):
    def make_sound(self):
        print("Мяу!")
def animal_chorus(animals):
    for a in animals:
        a.make_sound()
animals = [Dog("кто"), Cat("зачем кот")]
animal_chorus(animals)