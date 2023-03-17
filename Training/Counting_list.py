def number_of_items():
# dictionary comprehensions
    ls = list()
    many=int(input("How many items do you have?: "))
    for i in range(many):
        items = input("Enter your item: ")
        ls.append(items)
    occurrence = {item: ls.count(item) for item in ls}
    print(ls)
# prints the number of occurrence letter
    item = input("Enter the item: ")
    print("You have ",occurrence.get(item),f"{ls}")
number_of_items()