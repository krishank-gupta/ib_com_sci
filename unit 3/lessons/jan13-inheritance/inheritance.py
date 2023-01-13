# Inheritance
class Pet:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def get_price_tax(self):
        # Assume 10% Tax
        return self.price * 1.1

# Inherit data from parent class using |class child(parent)|
class Goldfish(Pet):
    def __init__(self, name, price, brain):
        # Create a Pet class using |super()|
        super().__init__(name, price, type='Fish')
        self.brain = brain

    def swim(self):
        return "Swimming Straight" if self.brain else "Swimming upside down"


# Create pets

bob = Pet(name="bob", )