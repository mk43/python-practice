import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.scatter(X, Y, s=50, c=T, alpha=.5)

plt.xlim(-2.5, 2.5)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())

plt.show()
