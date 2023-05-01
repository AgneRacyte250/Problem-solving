import os
with open('Loacation.txt', 'w') as file:
    file.write('The Law Section ')
    file.write('The Art Section ')
    file.write('The Technology Section ')
    file.write('The History Section ')
def search(file_name):
    print("Searching...")
    with open(file_name, "r") as file:
        for location in file:
            print(f"Looked in {location.strip()}")
    print("...Done!")
def run():
    #if the file is the other directory file_path = 'C:/Users/username/Desktop/data/files/txt/Location.txt'
    search('Loacation.txt') # file_path
run()