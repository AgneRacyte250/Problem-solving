def observed():
    observations = list()
    for i in range(3):
        observations.append(input("Please Enter an observation: "))
    return observations
def remove_observations ():
    observations = observed()
    opt = input(("Do you wish to remove an observation? y/n: "))
    if opt == "y":
        obse = input("Enter a string representing observation: ")
        observations.remove(obse)
        print(f"Done {obse} was removed...")
    elif opt == "n":
        pass
    else:
        print("Invalid character")


def run():
    print("Counting Observations......")
    observation = observed()
    remove_observations()
