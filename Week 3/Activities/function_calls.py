def box(word):
    lenght=len(word)
    print("#"*(lenght+4))
    print("#"+ word +"#")
    print("#"*(lenght +4))

def low(word):
    print(word.lower())
def upper(word):
    print(word.upper())

# slicing - and act of accsesing of individual items of a list . works on a charecter of a string . slosing using
# [start:end:steps ] spesifing
#word="This is sparta"
#print(word[3:8:1])
def mirro(word):
    print(word,"|", word[::-1])

def repeat(word):
    number=int(input("How many times to repeat: "))
    for i in range(number):
        if i % 2 == 0:
            word.upper()
        else:
            word.lower()
def run():
    w= input("Enter a word: ")
    print("Choose an opptoin:\n1.Box\n2.Lower case\n3.upper case\n4.Mirror\n5.Repeat")
    opt= int(input())
    if opt==1:
        box(w)
    elif opt==2:
        low(w)
    elif opt == 3:
        upper(w)
    elif opt ==4:
         mirro(w)
    elif opt ==5:
        repeat(w)
    else:
        print("No such option!!!")


run()