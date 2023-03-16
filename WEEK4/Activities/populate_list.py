def directions():
    directions = ["Move Forward", "Move Backwards", "Turn Left", "Turn Right"]
    return directions
def menu ():
    print("Please Select a Direction:")
    dir = directions()
    for index in range(len(dir)):
        print("{}: {}".format(index, dir[index]), end="\n")
    index=int(input())
    return dir[index]
def run():
    rout = []
    print("Working Out The Escape Rout....")
    for i in range(5):
     rout.append(menu())

    print(f"Escape rout is: {rout}")
run()


