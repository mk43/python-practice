import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line0 = ax.plot(x, np.cos(x))
line, = ax.plot(x, np.sin(x))


def init():
    line.set_ydata(np.sin(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))
    return line,


animation = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)

animation.save('resetvalue.gif', writer='imagemagick')

plt.show()
