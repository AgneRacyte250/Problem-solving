# Initilise empty dictionary
d = {}
diction = dict()

#initilias non-empty dictionary
phonebook =\
    {"Thomas":77546635345,
     "Aga":424534634634,
     "Md":34252454
    }
#print all phonebook
print(phonebook)

#Print/ access individual elemnts
name = input("Who you gonna call: ")
if name in phonebook:
    print(f"Calling...{phonebook[name]}")
else:
    print(f"No number for {name}")

#Zipping two lists together to compose adictionary
name = ["Garry", "Ian","Laura"]
age = [56,21,16]
people = dict(zip(name, age))
print(people)

#Traversing Dictionarys - accessing the values or keys
for thing in people:
    print(thing)    #Tranvirsing it only looks at keys
for thing in people.values(): #prints value
    print(thing)
for thing in people.keys(): #prints only keys
    print(thing)
for k, v in people.items: #prints both keys and values--both argumetns are provided
    print(f"Person {k} is tha {v} years old")


