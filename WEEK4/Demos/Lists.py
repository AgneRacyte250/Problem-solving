#Declare empty list
bleh = []
meh = list()
#declare non-empty list
yummy = ["chiken", "icream","chocalate","chips" ]
#print inter list
print(yummy)
#print a single item
print(yummy[2])
#print sum items
print(yummy[1:3])
# Add element to a list - adding the item to the end
print(bleh)
bleh.append("marmite")
bleh.append("Anchioves")
bleh.append("Carrots")
bleh.append("Tomatos ")
bleh.append("liver")
print(bleh)
# add miltiple items to a list
n = int(input("Enter how many food you wan to enter: "))
for i in range(n):
    bleh.append(input("Enter horible Food: "))
print(bleh)
bleh.extend(["Horse meat", "Pncakes"])
print(bleh)
#Inster items in a spesific possition
bleh.insert(1,"nothing")
print(bleh)
bleh.insert(4,"onions ")
print(bleh)
#remove
bleh.remove("Carrots")
bleh.remove("Tomatos")
print(bleh)