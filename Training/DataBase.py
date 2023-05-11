from person import person

class Database: #saving classes and creating the data base

    def __init__(self, name):
        self.name = name + "'s database" # stores name attributes
        self.people =[]
        self.n_ppl = len(self.people)
    def add_person(self, p):
        self.people.append(p)
        self.n_ppl += 1
    def remove_perosn(self, p):
        if p in self.people:
            self.people.remove(p)
        else:
            print('Person does not exist in the database')
    def display_all(self):
        for person in self.people:
            print(person)
if __name__ == "__main__":
    p1 = person("Tad", 67, 'Truck Driver', 78)
    p2 = person('Jam', 45, 'Teacher', 56)
    p3 = person('ur', 23, 'uniployd', 55)
    db = Database('Piotr')
    db.add_person(p2)
    db.display_all()
    db.add_person(p3)
    db.remove_perosn(p3)
    db.remove_perosn(p2)
    db.display_all()