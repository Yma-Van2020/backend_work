import random

class Character:

    def __init__(self, name):
        self.name = name

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nHealth: {self.health}\nEnergy: {self.energy}\n")

    def attack(self, other_character):
        self.energy_check()
        energy_cost = 20
        hit_chance = other_character.block()
        if self.energy < energy_cost:
            print(f'Not enough energy to perform this action.')
            return self
        if hit_chance == [1]:
            return self
        else:
            self.energy -= energy_cost
            damage_dealt = self.strength
            other_character.health -= damage_dealt
            print(f'{self.name} attacks {other_character.name} dealing {damage_dealt} damage. {other_character.name} loses {damage_dealt} health.')
            if other_character.health <= self.strength:
                print(f'---> {other_character.name} has been defeated!')
            moves = [0, 1]
            rng = random.choices(moves, weights=(50, 50))
            if rng == [0]:
                other_character.attack(other_character)
                print(f'{other_character.name} attacks!')
            elif rng == [1]:
                if other_character == Pirate("Jack Sparrow"):
                    other_character.drink_rum()
                    print(f'{other_character.name} drinks rum.')
                elif other_character == Ninja("Michelangelo"):
                    other_character.meditate()
                    print(f'{other_character.name} meditates.')
            return self

    def energy_check(self):
        if self.energy <= 30:
            print(f"Warning! {self.name}'s energy is low!")
    

class Ninja(Character):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.energy = 100
        self.strength = 20
        # self.type = "ninja"
    def meditate(self):
        self.energy += 20
        self.health += 10
    def block(self):
        prob = [0, 1]
        roll = random.choices(prob, weights=(30, 70))
        if roll == [1]:
            print(f'Attack dodged by {self.name}!')
        return roll

class Pirate(Character):
    def __init__(self , name):
        super().__init__(name)
        self.health = 150
        self.energy = 75
        self.strength = 25
        # self.type = "pirate"
    def drink_rum(self):
        self.energy += 25
        self.health -= 10
    def block(self):
        prob = [0, 1]
        roll = random.choices(prob, weights=(40, 60))
        if roll == [1]:
            print(f'Attack blocked by {self.name}!')
        return roll
    
