# https://www.geogebra.org/m/Da6WsuXk
# https://es.wikipedia.org/wiki/M%C3%A9todo_de_Euler


import numpy as np
import matplotlib.pyplot as plt

def fun(x):
 return np.array(-x[1], x[0]-x[1])

t1 = 0
t2 = 12
h = .01

t = np.arange(t1, t2, h)
np1 = len(t)

xx = np.zeros((np1, 2))

x1 = np.array([5, -3])
xx[0,:] = x1

for i in range(1,np1):
 x2 = x1 + h*fun(x1)
 xx[i,:] = x2
 x1 = x2


plt.plot(xx[:,0])
plt.show()


