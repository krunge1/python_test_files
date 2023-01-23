import dojo_pets_pets

class Ninja:
    def __init__(self, first_name, pet, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def getPet(self, name, type, tricks, health, energy, sound):
        self.pet = dojo_pets_pets.Pets(name, type, tricks, health, energy, sound)
        return self
        
    def walk(self, pet):
        dojo_pets_pets.Pets.play(self.pet, pet)
        return self
    # walk() - walks the ninja's pet invoking the pet play() method

    def feed(self, pet):
        dojo_pets_pets.Pets.eat(self.pet, pet)
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method

    def bathe(self, pet):
        dojo_pets_pets.Pets.noise(self.pet, pet)
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method



