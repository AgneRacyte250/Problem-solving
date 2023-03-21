def interests():
    print("Enter all your interests one after another\"stop\" to stop ")
    s1 = set()
    interest = ""
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        s1.add(interest)
    return s1
def tinderDeSecond():
    print("Firs Person: ")
    p1 = interests()
    print("Second Person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
        print(f"You are a match made in heaven!!! you have {len(common)} interests in common!!!")
    else:
        print(f"OWWWW no its not gonna work, ypu have  only {len(common)} Find another Person!!")

tinderDeSecond()