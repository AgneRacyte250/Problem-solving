#The class person which is a blueprint for my objects to store information about humans/people.
class person:
    #Initialiser or constructor a function that is automatically called when an object is instantiated (magic method)
    #Initialiser of any class has the same name
    #Define 'DUNDER' -Double underscore
    #Class attribute or a feature  accsecible/applied to everyone
    #MAX_WEIGHT
    MAX_W = 200
    def __init__(self,name , age = 0, job = '', w= 100):
        #Below are the instance attributes (feature)
        self.name = name
        self.age = age
        self.job = job
        if w > person.MAX_W:
            self.weight = person.MAX_W
        else:
            self.weight = w

p1 = person('Luke', 23, 'clerk', 22)
p2 = person('lil', 24, 'barista', 34)
print(f'Person 1 is called {p1.name} and A Person 2 is called {p2.name}')
print(f"Their total weight is {p1.weight + p2.weight}")
print(p1, '\n', p2)