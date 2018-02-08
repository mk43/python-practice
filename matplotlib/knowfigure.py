import matplotlib.pyplot as plt
import numpy as np

# example 1
# x = np.linspace(0, 10, 20)
# y = x + 1
#
# plt.plot(x, y)
# plt.show()

# example 2
# x = np.linspace(0, 10, 20)
# y1 = x + 1
# y2 = -x + 1
#
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()

# example 3
x = np.linspace(0, 10, 20)
y1 = x + 1
y2 = -x - 10
plt.figure()
plt.plot(x, y1)
plt.figure(figsize=(9, 6))
plt.plot(x, y2)
plt.show()

