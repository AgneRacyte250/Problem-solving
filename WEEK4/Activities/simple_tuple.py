def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods
def run():
    print(f"Minimume likelihood of falling: {min(likelihood())}%")

run()
