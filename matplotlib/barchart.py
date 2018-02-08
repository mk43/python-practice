import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = np.random.uniform(0.1, 1.0, n)
Y2 = np.random.uniform(0.1, 1.0, n)

plt.bar(X, +Y1)
plt.bar(X, -Y2)

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

for x, y in zip(X, Y1):
    plt.text(x, y + 0.02, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x, -y - 0.02, '%.2f' % y, ha='center', va='top')

plt.show()
