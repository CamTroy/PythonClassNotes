# Object Oriented Programming
class Vehicle:
    color = ""

class Plane(Vehicle):
    target = ""
    wing_span = 0

    def __str__(self):
        return f"This plane is a {self.color} plane with a wing span of {self.wing_span} and is flying toward {self.target}."

    def fly(self):
        print("OH NO WE'RE GONNA CRASH!!!")

airliner = Plane()

airliner.color = "white"
airliner.target = "the south tower"
airliner.wing_span = 100

print(airliner)