#spell cheker
words = set() # collection of values with no dublicates

def check(word):
    if word.lower() in word:
        return True
    else:
        return False
def load(dictionary):
    file = open(dictionary,"r")
    for line in file:
        word = line.rstrip()
        words.add(word)
    close(file)
    return True
def isze():
    return len(words)
def unload():
    return True

