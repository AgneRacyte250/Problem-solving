import os
def search(file_name):
    print('Searching...')
    data = ()
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('Section'):
                print('hello')

                