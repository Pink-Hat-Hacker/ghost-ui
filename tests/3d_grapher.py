import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data for the mesh
x = np.arange(-10, 10, 0.25)
y = np.arange(-2, 2, 1)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Plot the mesh
surf = ax.plot_surface(x, y, z, cmap='viridis')

# Add labels and a colorbar
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.colorbar(surf)

# Show the plot
plt.show()