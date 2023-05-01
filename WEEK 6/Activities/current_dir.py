import os
def cwd():
    path = os.getcwd()
    print(f'Current working Directory: {path}')
    return path
def display():
    for file in os.listdir(cwd()):
        print(file)
display()