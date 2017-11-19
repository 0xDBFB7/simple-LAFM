import matplotlib.pyplot as plt
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x, y, z = np.loadtxt('test.csv', delimiter=',', unpack=True)

for idx,val in enumerate(z):
	if val > 0.004:
		z[idx] = 0.004
for idx,val in enumerate(z):
	if val < 0.0:
		z[idx] = 0.0

ax1.scatter(x,y,z,c=z)
plt.show()
