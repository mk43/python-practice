import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y1 = x + 1
y2 = x + 2
y3 = x + 3
y4 = x + 4
y5 = x + 5
y6 = x + 6
y7 = x + 7

plt.figure()
plt.plot(x, y1, 'bo')
plt.plot(x, y2, 'r-')
plt.plot(x, y3, 'g--')
plt.plot(x, y4, 'y.-')
plt.plot(x, y5, 'm^', x, y6, 'm-')
plt.plot(x, y7, 'c-', linewidth=6)

plt.show()