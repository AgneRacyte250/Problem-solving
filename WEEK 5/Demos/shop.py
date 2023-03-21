def shop():
    items = {"Bread": 1.99, "Eggs": 3.49, "Milk": 1.99, "Chiking": 7.99, "Cheese": 2.49, "Ham": 3.99}
    return items
def view_all(products = {}):
    for i, j in products.items():
        print(f"{i}----------£{j}")

def playing():
    d = shop()
    d["Cheese"] = 3
    d["Milk"] = 1.69
    del d["Eggs"]
    prod = input("Enter new Prod: ")
    price = float(input("Enter The price: "))
    d[prod] = price
    view_all(d)
def basket():
    b = []
    while True:
        product = input("Enter an item or \"stop\": ")
        if product.upper() == "STOP":
            break
        q = int(input(f"Enter the quantity of {product}:  "))
        for i in range(q):
            b.append(product)
    return b
def till(basket = []):
    all_items = shop()
    total = 0
    for product in basket:
        if product.lower() in all_items:
            total+=all_items[product]
    else:
        print(f"No luck.The {product} is not sold her, Go to Lidl")
    return total


def run():
    print("Welcome tto my Shop.Please look around. We are watching you")
    view_all(shop())
    b = basket()
    while True:
        response = input("Are you ready to pay[y/n]")
        if response[0].lower == "y":
            to_pay = till(b)
            print(f"Pay £{to_pay:.2f} or i will come after you")
            break
        else:
            b2 = basket()
            b2.extend(b2)
run()
