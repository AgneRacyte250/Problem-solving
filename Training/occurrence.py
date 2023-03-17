#Using loop
def using_loop():
    mylist = [10,23,22,12,12,34,22,12,10]
    x = int(input("Enter a Number:"))
    count= 0
    for ele in mylist:
        if ele == x:
            count=count+1
    print("{} has occurred {} times".format(x,count))

#using count
def using_count():
    mylist = [10, 23, 22, 12, 12, 34, 22, 12, 10]
    x = int(input("Enter a Number:"))
    print("{} Has occurred {} Time".format(x,mylist.count(x)))

#Using counter
def using_counter():
    from collections import Counter
    mylist = [10, 23, 22, 12, 12, 34, 22, 12, 10]
    x = int(input("Enter a Number:"))
    dic = Counter(mylist)
    print("{} Has occurred {} Time".format(x,dic[x]))
using_counter()