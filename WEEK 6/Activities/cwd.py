import os
def Cwd():
    path = os.getcwd()
    print(f'The current working Directory is: {path}')
    print('The Directory Contains the following:')
    print(os.listdir(path))
def run():
    print('Processing....')
    Cwd()
run()
