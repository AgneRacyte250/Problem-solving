from clothingsize import ClothingSize
class Clothing:
    def __init__(self, colour = "white", material = "cotton", size =ClothingSize.MEDIUM):
        self.colour = colour
        self.material = material
        self.size = size
    def __str__(self):
        return f"{self.colour}, piece of clothes of {self.size} made from {self.material}"
    def __repr(self):
        return f"Clothing(colour = self.colour, material = self.material, self.size = size)"

if __name__ == "__main__":
    t_shirt = Clothing("blue", "silk")
    sweatshirt = Clothing(size=ClothingSize.SMALL, colour="yellow")
    print(t_shirt)
    print(sweatshirt)
    print(repr(sweatshirt))
    print(repr(t_shirt))