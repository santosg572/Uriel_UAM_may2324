import numpy as np
import matplotlib.pyplot as plt

del1 = .1
t1 = 3
t2 = 6


np1 = round((t2-t1)/del1)
xx1 = np.zeros(np1)
xx2 = np.zeros(np1)

xx1[0] = 6
xx2[0] = -1
x1 = 6
x2 = -1

print(len(xx1))

for i in range(np1-1):
 x1 = xx1[i] + del1*xx2[i]
 x2 = xx2[i] + del1*(5*xx2[i] - xx1[i])/2
 xx1[i+1] = x1
 xx2[i+1] = x2

print(xx1)
print(xx2)

plt.figure(figsize=(3, 9))
plt.subplot(211)
plt.plot(xx1)
plt.subplot(212)
plt.plot(xx2)
plt.show()




