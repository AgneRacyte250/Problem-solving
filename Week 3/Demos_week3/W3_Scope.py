def ing_a(a):
    a= a+1
    return a
def dec_a(a):
    a=a-1
    return a
def run():
    a =7
    a = dec_a(ing_a (a+2))
    for i in range (2):
        a =ing_a(a)
    print(f"The value of a is {a}")
run()