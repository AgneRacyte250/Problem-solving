while True:
            print("Please choose from the menu: \n1.Nice message\n2.Area rectinmgal\n3.Area of triangle\n4.Times table\n5.Exit")
            opt = int(input())
            if opt == 1:
                print("You smell nice")
            elif opt == 2:
                h = float(input("Enter height: "))
                b = float(input("Enter the base: "))
                print(f"The are of this rectangle {h*b} cm^2")
            elif opt == 3:
                h = float(input("Enter height: "))
                b = float(input("Enter the base: "))
                print(f"The are of this triamgle {h * b * 0.5} cm^2")
            elif opt == 4:
                n = int(input("Enter whole number: "))
                for i in range(1, 11):
                    print(f"{n}*{i}= {n*i}")
            elif opt == 5:
                break
            else:
                print("No such option, please choose again")