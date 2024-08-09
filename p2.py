import numpy as np
import matplotlib.pyplot as plt

h = .1
t1 = 3
t2 = 10

t =np.arange(t1, t2, h)
np1 = len(t)

x11 = 6
x21 = -1

x1 = np.zeros((np1,1))
x2 = np.zeros((np1,1))

def f(t, x1, x2):
  return x2

def g(t, x1, x2):
  return (5*x2-x1)/2

x1[0] = x11
x2[0] = x21

tt=0
for i in range(2,np1):
 K1 = f(tt, x11, x21)
 L1 = g(tt, x11, x21)
 K2 = f(tt+h/2, x11+h*K1/2, x21+h*L1/2)
 L2 = g(tt+h/2, x11+h*K1/2, x21+h*L1/2)
 K3 = f(tt+h/2, x11+h*K2/2, x21+h*L2/2)
 L3 = g(tt+h/2, x11+h*K2/2, x21+h*L2/2)
 K4 = f(tt+h, x11+h*K3, x21+h*L3)
 L4 = f(tt+h, x11+h*K3, x21+h*L3)
 x12 = x11 + h*(K1 + 2*K2 + 2*K3 + K4)
 x22 = x21 + h*(L1 + 2*L2 + 2*L3 + L4)
# print((x12, x22))
 x1[i] = x12
 x2[i] = x22
 tt = tt + h
 x11 = x12
 x21 = x22

print(x1)
plt.plot(x1)

plt.show()

 

