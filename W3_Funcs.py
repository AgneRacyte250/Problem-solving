#Deffinition of function.
#parameters - data given and injected in to the function.
# Default parameters -  assumed that there nothing provided.

#def t_area():
   # h = float(input("Enter the hight: "))
   # b = float(input("Enter the base: "))
    #area= h*b*0.5
   # print("The area of this triangle is {}".format(area))
#t_area()


#def t_area(hight=1,base=3): # takes in the parameters in step when calling a function
    #area= hight*base*0.5
    #rint("The area of this triangle is {}".format(area))

#t_area(10,7) # calling a function with arguments.

#h = float(input("Enter the height:"))
#b = float(input("Enter the base: "))
#t_area( h, b) # taking input and passing them to a function.
def t_area(hight=1,base=3): # takes in the parameters in step when calling a function
    area= hight*base*0.5
    return area

area = t_area()
print("The area of this triangle is {}".format(area))
print(t_area(10,10))     #replaces the funciton call and returns the value