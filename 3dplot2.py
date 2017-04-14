import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Z = [2, 2, 3, 4, 1, 2, 6, 7, 9, 5]

ax.scatter(X, Y, Z, c='r', marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
