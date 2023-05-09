import matplotlib.pyplot as pl
import matplotlib.animation as a
import matplotlib.pyplot as plt

boxes = []
fig, ax = plt.subplots()
format = ['bo--', 'r-', 'y-.', 'gx--', 'p--']
def init():
    boxes.append({'x': [2,10, 10, 2, 2], 'y':[10, 10, 2, 2, 10]}) # dict that contain a key of x and y that has a list of corrdinates
    boxes.append({'x': [4, 8, 8, 4, 4], 'y': [8, 8, 4, 4, 8]}) # fifth numbers needs for finishing the square
    boxes.append({'x': [5, 7, 7, 5, 5], 'y': [7, 7, 5, 5, 7]})

def animate(f):

    ax.cla()
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.plot(boxes[f%3]['x'], boxes[f%3]['y'], format[f%5]) # f%3 will produce the numbers between 0 and 2 taking the key values provide in second list

def run():
    garry = a.FuncAnimation(fig, animate, frames=100, interval=1000, init_func=init)
    plt.show()

run()