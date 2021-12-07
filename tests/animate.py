from matplotlib import animation
from matplotlib import pyplot as plt
import random
import time

class Animate(object):
    def __init__(self) -> None:
        super().__init__()
        self.fig = plt.figure()
        self.ax = plt.axes()
        self.line, = self.ax.plot([], [], lw=2)
        self.index = 1

    def initialize(self):
        self.line.set_data([], [])
        return self.line,

    def animate(self, i):
        x = self.index
        y = random.randrange(0,100)
        self.index+=1
        self.ax.scatter(x,y,color='black',marker="x")
        time.sleep(0.5)
        return self.line,
  
    def run(self):
        anim = animation.FuncAnimation(self.fig, self.animate, 
        init_func=self.initialize, frames=200, interval=20, blit=True)
        plt.show()


if __name__=="__main__":
    a = Animate()
    a.run()


