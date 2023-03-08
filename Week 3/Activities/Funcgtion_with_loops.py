def cross_bridge(s):
    if s <= 5:
       for i in range(0, s):
           print("Cross step.")
       print("We must keep going !!!")
    elif s > 5:
        for i in range(0, s):
            print("Cross step.")
        print("The bridge is collapsing!!!!")

cross_bridge(3)
cross_bridge(6)