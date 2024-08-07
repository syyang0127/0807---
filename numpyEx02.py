import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

axis = plt.axes(projection='3d')
plt.show()

Z = np.linspace(0,1,100)
X = Z * np.sin(30*Z)
Y = Z * np.cos(30*Z)

axis.plot3D(X,Y,Z)