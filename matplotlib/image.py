import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(2, 1, 16).reshape(4, 4)

plt.imshow(a, interpolation='nearest', cmap='coolwarm', origin='lower')

plt.colorbar(shrink=.98)

plt.xticks(())
plt.yticks(())
plt.show()
