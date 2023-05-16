from tech import Tech
class Jetpack(Tech):
    def __init__(self):
        pass
    def __str__(self):
        return "This is the jetpack lets fly"
    def __repr__(self):
        return "Jetpack()"
    def activate(self):
        print("jetpack started")
    def deactivate(self):
        print("Jetpack is off")
    def fly(self, speed):
        print(f"Jetpack flies at {speed} meters per second")
if __name__ == "__main__":
    jetp = Jetpack()
    jetp.activate()
    jetp.deactivate()
    jetp.fly(34)
    jetp.fly(78)
