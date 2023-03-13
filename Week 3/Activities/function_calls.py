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

word="This is sparta"
print(word[3:8:1])
