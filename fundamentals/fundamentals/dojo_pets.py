class Pet:
    def __init__(self, name, type, tricks, health = 100, energy = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        
    def sleep(self, energy):
        self.energy += 25
        print(f"{self.name} is sleeping")
        return self
    
    def eat(self, food):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is having some petfood")
        return self
    
    def play(self):
        self.health += 5
        print(f"{self.name} is playing happily")
        return self 
    
    def noise(self):
        print("meow~")
        print(f"{self.name} is making some happy noises")
        return self
    
    def Snake(Pet):
        def __init__(self, name, type, tricks, health = 80, energy = 70):
            super().__init__(name, type, tricks, health, energy)
        
    
    def Mouse(Pet):
        def __init__(self, name, type, tricks, health = 180, energy = 50):
            super().__init__(name, type, tricks, health, energy)
        
    def Spider(Pet):
        def __init__(self, name, type, tricks, health = 280, energy = 370):
            super().__init__(name, type, tricks, health, energy)

