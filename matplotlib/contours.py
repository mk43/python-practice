import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

plt.contourf(X, Y, f(X, Y), 12, alpha=.9, cmap=plt.cm.coolwarm)

C = plt.contour(X, Y, f(X, Y), 12, colors='black')

plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())

plt.show()
