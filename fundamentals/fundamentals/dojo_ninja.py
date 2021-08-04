import dojo_pets

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
    def walk(self):
       self.pet.play()
       print(f"{self.first_name} is walking {self.pet.name}")
       return self
   
    def feed(self):
        self.pet.eat(self.pet_food)
        print(f"{self.first_name} is Feeding {self.pet.name} with {self.pet_food}")
        return self 
         
    def bathe(self):    
        self.pet.noise()
        print(f"{self.first_name} is bathing {self.pet.name} and it makes noise")
        return self


Ninja1s_pet = Pet("Lucky", "dog", ["shake hands", "stand"])   
Ninja1 = Ninja("Katelyn", "Ma", "icecream", "can foods", Ninja1s_pet)
     

Ninja1.feed().walk().bathe()       