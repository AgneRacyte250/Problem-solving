from tech import Tech
class Laser(Tech):
    MAX_RANGE = 100
    def __init__(self):
        pass
    def __str__(self):
        return f"Laser object whit max_range whit 100 meters"
    def __repr__(self):
        return "Laser()"
    def fire(self,range):
        if range <= Laser.MAX_RANGE:
            print("pew pew enemy is in trouble!!!!")
        else:
            print("Enemy is safe")
    def activate(self):
        print("Laser ready to fire")
    def deactivate(self):
        print("Laser shuts down")

if __name__== "__main__":
    las = Laser()
    las.fire(80)
    las.fire(120)
