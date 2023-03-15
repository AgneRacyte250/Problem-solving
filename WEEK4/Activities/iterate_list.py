def directions():
    directions =["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def menu():
    print("Please Select a Direction")
    dire = directions()
    for index in range(len(dire)):
        print("{}: {}\n".format(index, dire[index]))

def run():
    menu()

run()