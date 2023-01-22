# import dojo_names_ninja

class Pets:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound

    def sleep(self, name):
        if self.name == name:
            self.health += 25
            print(f"{self.name} feels refreshed! Health increased by 25 points. {self.name}'s health is now {self.health}")
    
    def eat(self, name):
        if self.name == name:
            self.health += 5
            self.energy += 10
            print(f"{self.name} at some grub! Health increased by 5 points and energy up by 10. {self.name}'s health is now {self.health} and energy {self.energy}")

    def play(self, name):
        if self.name == name:
            self.health += 5
            print(f"{self.name} feels refreshed! Health increased by 5 points. {self.name}'s health is now {self.health}")

    def play(self, name):
        if self.name == name:
            self.health += 5
            print(f"{self.name} feels refreshed! Health increased by 5 points. {self.name}'s health is now {self.health}")


