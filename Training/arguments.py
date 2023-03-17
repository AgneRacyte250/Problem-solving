#Takes argumetns form comand line
def first():
 from sys import argv
 if len(argv) == 2:
    print(f"Hello, {argv[1]}")
 else:
    print("Hello World")
def second():
 from sys import argv
 for arg in argv[1:]:
     print( f"{arg }",end=" ")

second()
