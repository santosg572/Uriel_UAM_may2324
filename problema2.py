import numpy as np
import matplotlib.pyplot as plt
import numpy as np

del1 = .01
t1 = 0
t2 = 6


np1 = round((t2-t1)/del1)
xx1 = np.zeros(np1)
xx2 = np.zeros(np1)

xx1[0] = 1
xx2[0] = 1
x1 = 1
x2 = 1

tt = [0]

print(len(xx1))

for i in range(np1-1):
 x1 = xx1[i] + del1*xx2[i]
 x2 = xx2[i] + del1*(-2*xx2[i] - 5*xx1[i])
 xx1[i+1] = x1
 xx2[i+1] = x2
 t1 = t1 + del1
 tt.append(t1)

plt.figure(figsize=(9, 9))
plt.subplot(221)
plt.plot(tt, xx1)
plt.subplot(222)
plt.plot(tt, xx2)

tt = np.array(tt)
print(tt)
yy = np.exp(-tt) * (np.sin(2*tt) + np.cos(2*tt))

plt.subplot(223)
plt.plot(tt, yy) 

plt.subplot(224)
plt.plot(tt, yy)
plt.plot(tt, xx1, 'r')

plt.show()




