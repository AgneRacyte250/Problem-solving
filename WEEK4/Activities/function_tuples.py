def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return max(likelihoods), min(likelihoods)



print(f"Minimum likelihood of falling: {likelihood()[1]}%")
print(f"Maximum likelihood of falling {likelihood()[0]}%")
