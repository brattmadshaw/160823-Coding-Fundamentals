class Avatar:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"Age: Your {self.name} has an age of {self.age} years old")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"

class Pet(Avatar):
    def __init__(self, name, age, rare=True):
        super().__init__(name, age)
        self.rare = rare

    def rarity(self):
        print(f"{self.name} is a rare pet")

    def __str__(self):
        return super().__str__() + f" - rare: {self.rare}"
    
class friend_pet(Avatar):
    def __init__(self, name, age, rarity=False):
        super().__init__(name, age)
        self.rarity = rarity

    def __str__(self):
        return super().__str__() + f" - rare: {self.rarity}"
    
avatar1 = Avatar("Avatar", 20)
Pet1 = Pet("Avatar's Pet", 2)
friend_pet1 = Pet("Friends's Pet", 5)

avatar1.description()
print(avatar1)

Pet1.description() 
Pet1.rarity()
print(Pet1)

friend_pet1.description()
print(friend_pet1)


