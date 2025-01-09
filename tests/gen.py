import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stl(file_path):
    """Load an STL file and return the mesh."""
    return mesh.Mesh.from_file(file_path)

def slice_mesh(mesh_data, slices_x, slices_y):
    """Slice the mesh along the x and y axes and find max z values."""
    vertices = mesh_data.vectors.reshape(-1, 3)  # Get all vertices (N x 3)
    min_x, max_x = vertices[:, 0].min(), vertices[:, 0].max()
    min_y, max_y = vertices[:, 1].min(), vertices[:, 1].max()
    
    # Define slicing intervals
    x_intervals = np.linspace(min_x, max_x, slices_x + 1)
    y_intervals = np.linspace(min_y, max_y, slices_y + 1)
    
    results = []  # To store (x, y, max_z)
    
    for i in range(slices_x):
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
                # Use the midpoint of the slice for x, y
                mid_x = (x_min + x_max) / 2
                mid_y = (y_min + y_max) / 2
                results.append((mid_x, mid_y, max_z))
    
    return np.array(results)

def plot_3d_points(points):
    """Plot the (x, y, max_z) points in 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Max Z')
    plt.show()

# Main program
if __name__ == "__main__":
    stl_file_path = "./data/file.stl"  # Replace with your STL file path
    slices_x = 4
    slices_y = 4

    # Load and process STL file
    stl_mesh = load_stl(stl_file_path)
    points = slice_mesh(stl_mesh, slices_x, slices_y)

    # Print the results and plot
    print("Sliced Points (x, y, max z):")
    print(points)
    plot_3d_points(points)
