def movements():
    path = ["Move Forward", 10,"Move Backward", 5,"Move Left", 3,"Move Right", 1]
    return path

def run():
    print("Movving....\n")
    moving = movements()
    print(f"{moving[0]} For {moving[1]}\n{moving[2]} For  {moving[3]}\n{moving[4]} For {moving[5]}\n{moving[6]} For {moving[7]}",end="" )


run()
