
def open_file():
    file = open('test.txt')
    print(file.read())
def open_with():
    with open('test.txt') as file:
        data = file.read()
        lines = data.split('\n')
        print(data)
        print(lines)
def reading(): # read only a few characters by supplying an appropriate value to the method read
    with open('test.txt') as file:
        lines = file.read(10)
        print(lines)
def readLines(): # retrieve all the lines in a file as a list using the method readlines
    with open('test.txt') as file:
        lines = file.readlines()
        print(lines)
def readline():
    with open('test.txt') as file:
        line = file.readline().strip()
        print(line)
readLines()
