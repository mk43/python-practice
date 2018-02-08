import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y1 = 10 * x + 50
y2 = x**2

plt.figure()
l1, = plt.plot(x, y1, 'b-')
l2, = plt.plot(x, y2, 'b--')

plt.legend(handles=[l1, l2], labels=[r'$line\ 1$', r'$line\ 2$'],  loc='best')

plt.show()