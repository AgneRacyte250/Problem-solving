from inhabintant import inhabitant
from clothing import Clothing

class Human(inhabitant):
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0, energy=0):
        super().__init__(name,age, energy)
        self.Clothing = []

    def __str__(self):
        return f"{self.name} of age {self.age} has {self.energy} energy and wears {self.Clothing}"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy}, clothing = {self.Clothing})"
    def dress(self, clothing):
        self.Clothing.append(clothing)
    def undress(self, clothing):
        if clothing in self.Clothing:
            self.Clothing.remove(clothing)


if __name__ == "__main__":
    h = Human("Patric, 29")
    h.display()
    print(h)
    print(repr(h))
    h.move(55)
    h.eat(28)
    for i in range(4):
        h.grow()
    trousers = Clothing("Blue", "dennin ")
    h.dress(trousers)
    print(h.dress)