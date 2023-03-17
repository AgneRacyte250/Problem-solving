def first():
    scores = [32, 37, 66]
    avarege = sum(scores) / len(scores)
    print(avarege)
def second():
    score = []
    for i in range(3):
        s = int(input("Scores: "))
        score.append(s) #score+=[s]
    avarege = sum(score) / len(score)
    print(f"{avarege}")
def uppercase():
    before = input("Before: ")
    after = before.upper()
    print(f"After: {after}")
uppercase()