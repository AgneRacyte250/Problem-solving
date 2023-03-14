def generate():
    name = input("Enter name of a student: ")
    mark = float(input((f"Enter mark for {name}: ")))
    return name, mark
def list_of_students(n):
    stud_list = []
    for i in range(n):
        stud_list.append(generate())
    return stud_list
print(list_of_students(2))
def average(lista = []):
    total = 0
    for tup in lista:
        total += tup[1]
        if len(lista) > 0:
            avrg = total/len(lista)
        else:
            avrg =0
def run():
    stud_list = list()
    while True:
        opt= int(input("Menu\n\n1.Populate List of Students\n2.Calculate Average Mark\n3.Change a Mark of a Student\n4.Exit\n"))
        if opt == 4:
            break
        elif opt == 1:
            n = int(input("Entre Number of Students: "))
            stud_list.extend(list_of_students(n))
        elif opt == 2:
            print(f"The avarage mark is {average(stud_list):.2f}")
        elif opt == 3:
            name = input("Whos Mark to Update?: ")
            for student in stud_list:
                if student[0].upper() == name.upper():
                    n_mark = float(input(f"Enter New Mark fo {name}: "))
                    stud_list.remove(student)
                    stud_list.append((name, n_mark))
        else:
            print("Somthing is wrong. You fool!!")

run()