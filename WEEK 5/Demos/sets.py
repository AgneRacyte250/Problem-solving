#Initialise empty set s = {} (the class will be dict}
s = set()

#Initialise non-empty set
colours = {"blue", "red", "yellow","purple","red"}
print(len(colours)) #contains 4 uniq elements doesnt show the repeated values
print(colours) #will print in different order

#Adding elemnts into a set
colours.add("green")
colours.add("navy blue")
print(colours)

#Adding multiple elements
colours = colours.union({"black","magent","crimson","brown"})
print(colours)

#Removing items form a set
if "yellow" in colours:
    colours.remove("yellow")
print(colours)

#Set are hterogeneos and diplicates are not allowed
colours.add(99)
colours.add(True)
print(colours)

#Check membership
if "yellow" in colours:
    print("yay - I like yellow")
else:
    print("Sad days")

c = {"brown", "turquise","cyan","coquwlicot","pink","red"}

#Union - join 2 sets together, not keeping dublicates (each element appears one time)
c2 = colours.union(c)
print(f"c is {c}")
print(f"c2 is {c2}")
print(f"colours is {colours}")

# Intersection - looking at common values of 2 collections
c3 = c.intersection(colours)
print(f"c3 is {c3}")

#Difference - keep elements of one set that are Not part of
c4 = colours.difference(c)
c5 = c.difference(colours)
print(f"c4 is {c4}")
print(f"c5 is {c5}")



