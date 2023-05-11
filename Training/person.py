#The class person which is a blueprint for my objects to store information about humans/people.
class person:
    #Initialiser or constructor a function that is automatically called when an object is instantiated (magic method)
    #Initialiser of any class has the same name
    #Define 'DUNDER' -Double underscore
    #Class attribute or a feature  accsecible/applied to everyone
    #MAX_WEIGHT
    MAX_W = 200

    #Static method -> Utility function, that does not requer any object
    def is_mature(age):
        if age >= 25:
            return 'Person is mature'
        else:
            return 'Person is immature'
    def __init__(self,name , age = 0, job = '', w= 100):
        #Below are the instance attributes (feature)
        self.name = name
        self.age = age
        self.job = job
        if w > person.MAX_W:
            self.weight = person.MAX_W
        else:
            self.weight = w
        #magic method str provides 'informal' representation of object via strinf
        # it is invoked automatically when object  when it goes to print
    #def __str__(self):

    def eat(self, food):
        print(f'{self.name} have eaten {food}')
        self.weight += w
        print(f'{self.name} now weights ')

    #p1 = person('Luke', 23, 'clerk', 22)
    #p2 = person('lil', 24, 'barista', 34)
    #print(f'Person 1 is called {p1.name} and A Person 2 is called {p2.name}')
    #print(f"Their total weight is {p1.weight + p2.weight}")
    #print(p1, '\n', p2)
print(person.is_mature(18))
