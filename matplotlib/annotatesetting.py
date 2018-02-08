import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y = x + 5

plt.figure()
plt.plot(x, y, 'b-')

plt.xticks(np.linspace(-10, 10, 6))
plt.yticks(np.linspace(-6, 14, 6))

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position('zero')

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position('zero')

x0 = 4
y0 = x0 + 5
plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)
plt.scatter([x0], [y0], color='k')

plt.annotate(r'$(%s,\ %s)$' % (x0, y0), xy=(x0, y0),
             xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.1"))

plt.text(2, 14, r'$y\ =\ x\ +\ 5$', fontdict={'size': 16, 'color': 'r'})

plt.show()