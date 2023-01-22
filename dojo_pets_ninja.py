import dojo_pets_pets

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def getPet(self, name, type, tricks, health, energy, sound):
        name = dojo_pets_pets.Pets(name, type, tricks, health, energy, sound)

    # def walk(self, pet):
        # dojo_pets_pets.Pets.play(pet)


kyle = Ninja('Kyle', 'Runge', 'Shadow', 'Hotdog', 'Purina')
kyle.getPet('Shadow', 'Dog', ['Be a good boy!', 'Shake', 'Fetch'], 100, 75, 'Chewbacca noises !!!!')

kyle.walk('Shadow')


