import os

def search(file_name):
    print('Searching....')
    section = []
    books = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith("Section"):
                section_name = line.split(":")[1].strip()
                section.append(section_name)
            else:
                books.append(line.strip())
    print('Done!!!')
    return (section, books)

def save(file_name, data):
    section = data[0]
    books  = data[1]
    print('Saving...')
    with open(file_name, 'w') as file:
        file.write(f"Section: {section}\n")
        file.write(f"Books: {books}\n")
    print('Done!!!')

def run():
    data = search('C:/Users/agnes/Desktop/Folders/cs year 1/PS phyton/PycharmProjects/Problem-solving/WEEK 6/Tasks/data/txt/books.txt')
    save('C:/Users/agnes/Desktop/Folders/cs year 1/PS phyton/PycharmProjects/Problem-solving/WEEK 6/Tasks/data/txt/section-books.txt', data)

run()

