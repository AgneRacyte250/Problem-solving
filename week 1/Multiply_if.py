age= int(input("Enter your age "))
ch= int(input("Enter the number of children "))
if age > 25 and ch > 0 and age <=55: # AND -> When hen its connected all need to be true
    print("You are a parent")
    print(f"Next year you will be {age+1} yay")
elif age > 55 and ch > 0:
    print("Hoppefuly you will get support")
elif age < 18 or ch == 0: # OR -> At least 1 needs to be true to go inside the elif block code
    print("Plenty of time to get kids")
else:
    print("You are old")
    print("Dont worry we will live for long")