import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 23/38
c = 5/19
x = np.linspace(-4, 10, 256, endpoint = True)
y = (b * x) + c

plt.plot(x, y, '-g', label=r'$y = 23x/38 + 5/19$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve')
plt.legend(loc='upper left')

plt.scatter(1,1)

plt.scatter(-2, -1)

plt.scatter(3,2)

plt.scatter(2,2)

plt.xlim([-4, 4])
plt.ylim([-4, 4])

plt.show()
