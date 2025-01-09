import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stl(file_path):
    return mesh.Mesh.from_file(file_path)

def slice_mesh(mesh_data, slices_x, slices_y):
    vertices = mesh_data.vectors.reshape(-1, 3)  # Get all vertices (N x 3)
    min_x, max_x = vertices[:, 0].min(), vertices[:, 0].max()
    min_y, max_y = vertices[:, 1].min(), vertices[:, 1].max()
    
    x_intervals = np.linspace(min_x, max_x, slices_x + 1)
    y_intervals = np.linspace(min_y, max_y, slices_y + 1)
    
    x_centers = []
    y_centers = []
    max_z_values = []
    
    for i in range(slices_x):
        row_x = []
        row_y = []
        row_z = []
        for j in range(slices_y):
            # Define the bounds for this slice
            x_min, x_max = x_intervals[i], x_intervals[i + 1]
            y_min, y_max = y_intervals[j], y_intervals[j + 1]
            
            # Find vertices within this slice
            mask = (
                (vertices[:, 0] >= x_min) & (vertices[:, 0] < x_max) &
                (vertices[:, 1] >= y_min) & (vertices[:, 1] < y_max)
            )
            slice_vertices = vertices[mask]
            
            if len(slice_vertices) > 0:
                # Compute the max Z value in this slice
                max_z = slice_vertices[:, 2].max()
            else:
                max_z = 0  # Default if no vertices are in the slice
            
            # Use the midpoint of the slice for x, y
            mid_x = (x_min + x_max) / 2
            mid_y = (y_min + y_max) / 2
            row_x.append(mid_x)
            row_y.append(mid_y)
            row_z.append(max_z)
        
        x_centers.append(row_x)
        y_centers.append(row_y)
        max_z_values.append(row_z)
    
    return np.array(x_centers), np.array(y_centers), np.array(max_z_values)

def plot_surface(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Max Z')
    plt.show()

if __name__ == "__main__":
    stl_file_path = "./data/file2.stl"
    slices_x = 4 # > number = more detail
    slices_y = 4 # ghost basin has a 4x4 array of electrodes

    # load and slice STL file
    stl_mesh = load_stl(stl_file_path)
    x, y, z = slice_mesh(stl_mesh, slices_x, slices_y)

    # print the results and plotting
    print("Sliced Points (x, y, max z):")
    print(f"X:\n{x}")
    print(f"Y:\n{y}")
    print(f"Z:\n{z}")
    plot_surface(x, y, z)
