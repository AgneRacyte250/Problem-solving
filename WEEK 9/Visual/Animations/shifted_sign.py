import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplot()

def animate(f):
    ax.cla()
    ax.set_xlim(0, 720) # values on x axes
    ax.set_ylim(-1, 1) # values on y lines
    angles = np.arange(0,720) #array of numbres from 0 to 720.
    ang_rads = angles * np.pi / 180  #convirting deggres to radians
    y = np.sin(ang_rads - f/50)
    ax.plot(angles, y, 'bo') #ploting the sgin itself

def run():
    larry = a.FuncAnimation(fig, animate, interval=100, frames=720)
    plt.show()

run()

