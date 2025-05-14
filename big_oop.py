# OOP

pets = []

class Pet:
    name = ""
    age = 0
    species = ""

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        return f"Hi, my name is {self.name}, you should watch Neon Genesis Evangelion."

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.species}!!"

class Cat(Pet):
    color = ""

    def __init__(self, name, age, species, color):
        super().__init__(name, age, species)
        self.color = color

    def speak(self):
        return f"Meow"

class Dog(Pet):
    breed = ""

    def __init__(self, name, age, species, breed):
        super().__init__(name, age, species)
        self.breed = breed

    def speak(self):
        return "Woof"

class Dragon(Pet):
    wealth = 0

    def __init__(self, name, age, species, wealth):
        super().__init__(name, age, species)
        self.wealth = wealth

    def speak(self):
        return "Rawr"

    def breath_fire(self):
        print("All your pets are cooked!")
        return self

def print_pets(pets):

    for pet in pets:
        print(pet)

cat = Cat("Brooklyn", 4, "Cat", "Orange")
dog = Dog("Joe", 5, "Dog", "Golden Retriever")
dragon = Dragon("Joseph", 1000, "Dragon", 10000)

pets.append(cat)
pets.append(dog)
pets.append(dragon)

print(cat.speak())
print(dog.speak())
print(dragon.speak())
print()

print(f"Your pets are: ")
print_pets(pets)
print()

pets = [dragon.breath_fire()]

print(f"Your pets are now: ")
print_pets(pets)