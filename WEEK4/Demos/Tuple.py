#Declare a Tuple. cant expand or change data
x = ("Piotr", 68, True)
y = tuple(["Garry", 32, False]) #Casted
#print Tuples
print(x)
print(y)
print(x[1])
# Cannot change individual items
#x[1] = 69 #type error

#Concatinate Tuples
z = x + y
print(z)
print(x)
print(y)
#Using min and max function
h = (74, 68, 45, 35, 15,1, 82)
print(max(h))
# swaping values inside in an tuple
lista = list(h)
temp = lista[0]
lista[0] = lista[1]
lista[1]= temp
h1 = tuple(lista)
print(h1)
#Deleting the item of from a tuple
del h1[0]