def dimensions():
    w = float(input("Enter the width of the room:  "))
    l = float(input("Enter the lenght of the room: "))
    #area = l*w
    return l*w
def r_name():
    return input("Enter room name: ")


def price (name, area):
    if name.lower() == "Bathroom":
        return area *20
    elif name.lower() == "Bedroom":
        return area * 10
    elif name.lower()== "livinf room":
        return area * 12
    else:
        return area * 30
def run():
    t_price = 0
    num = int(input("Hoe many rooms to clean: "))
    for i in range(num):
        room = r_name()
        area = dimensions()
        p = price(room, area)
        t_price+= p
    print(f"The total price {t_price}")
run()
