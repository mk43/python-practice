import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 40)
y1 = 10 * x + 50
y2 = x**2

plt.figure()
plt.plot(x, y1, 'b-')
plt.plot(x, y2, 'b--')
plt.xlim((-20, 20))
plt.ylim((-60, 160))
plt.xlabel('I am x')
plt.ylabel('I am y')

plt.xticks(np.linspace(-20, 20, 5))
plt.yticks([0, 50, 100], [r'$bad$', r'$normal$', r'$good$'])

boderparameter = plt.gca()
boderparameter.spines['right'].set_color('none')
boderparameter.spines['top'].set_color('none')

boderparameter.xaxis.set_ticks_position('top')

boderparameter.spines['left'].set_position(('data',0))
boderparameter.spines['bottom'].set_position(('data',0))
boderparameter.xaxis.set_ticks_position('bottom')
boderparameter.set_xlabel('')
boderparameter.set_ylabel('')

plt.show()