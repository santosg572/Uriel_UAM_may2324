import numpy as np
import matplotlib.pyplot as plt

x1 = (5 + np.sqrt(17))/4
x2 = (5 - np.sqrt(17))/4

f2 = np.exp(3*x2)
f1 = np.exp(3*x1)

c2 = (6*x1 -1)/(f2 * (x2-x1))
c1 = (-1 - c2*x2*f2) / (x1*f1)

x = np.arange(3,6,.1)
y = c1*np.exp(x1*x) + c2*np.exp(x2*x)

plt.plot(x,y)
plt.show()






