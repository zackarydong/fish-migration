import numpy as np
import matplotlib.pyplot as plt


# setup the figure and axes
fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(111, projection='3d')

# fake data
_x = np.arange(7)
_y = np.arange(10)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = x + y
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Temperature Distribution')
ax1.set_xlabel

plt.show()


