from human import Human
from robot import Robot

class Planet:
    def __init__(self):
        self.humans = []
        self.robots = []
    def __str__(self):
        return f"This planet contains \nhumans: {self.humans}\n Robots: {self.robots}"
    def __repr__(self):
        return f"Planet(Humans = {self.humans}, Robots ={self.robots})"
    def add_human(self, hum):
        self.humans.append(hum)
    def remove_human(self, hum):
        if hum in self.humans:
            self.humans.remove(hum)

    def add_robot(self, rob):
        self.robots.append(rob)

    def remove_robot(self, rob):
        if rob in self.robots:
            self.robots.remove(rob)
if __name__ == "__main__":
    h1 = Human()
    h2 = Human()
    r1 = Robot()
    r2 = Robot()
    r3 = Robot()
    earth = Planet()
    earth.add_human(h1)
    earth.add_robot(r1)
    print(earth)
    print("-"*28)
    earth.add_robot(r1)
    earth.add_human(h2)
    print(earth)
    print("-" * 28)
    earth.remove_human(h2)
    print(earth)



