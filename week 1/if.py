temp = float(input("what is your temp "))
if temp > 38.6:
    print("you have tempature. poor you")
elif temp < 36:
    print("you have low temp")
else:
    print("you dont have tempeture")
print("your temp is {}c".format(temp))