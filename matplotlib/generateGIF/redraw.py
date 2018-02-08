import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
ax.plot(x, np.cos(x))


def init():
    return ax.plot(x, np.sin(x))


def animate(i):
    try:
        ax.lines.pop(1)
    except Exception:
        pass
    line = ax.plot(x, np.sin(x + i / 10.0), 'r')
    return line,


animation = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=False)

animation.save('redraw.gif', writer='imagemagick')

plt.show()
