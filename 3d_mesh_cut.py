import numpy as np
from stl import mesh


def slice_mesh(file_path, layer_thickness):
    # Load the mesh
    model = mesh.Mesh.from_file(file_path)
    min_z, max_z = model.z.min(), model.z.max()  # No need for abs here
    
    slices = []

    # Generate slices
    for z in np.arange(min_z, max_z, layer_thickness):
        # Create a mask for triangles that intersect the current layer
        mask = np.any((model.z >= z) & (model.z < z + layer_thickness), axis=1)

        # Filter points using the mask
        slice_points = model.points[mask]

        # DEBUG PRINTS
        print("Min Z:", min_z, "Max Z:", max_z)
        print("Current Slice Z:", z, "-", z + layer_thickness)
        print("Mask:", mask)
        print("Points in Slice:", slice_points)

        slices.append(slice_points)

    return slices

def writeToFile(points):
    print("opening text file")
    with open("points.txt", 'w') as textFile:
        print("writing to textfile")
        textFile.writelines(str(points))
        textFile.close()


if __name__ == '__main__':
    startProg = input("Start Program? Y/N");
    print(startProg)

    if (startProg == 'y' or startProg == 'Y' or startProg == 'yes'):
        filePathInput = str(input("path to file: "))
        print(filePathInput)
        numOfSlices = int(input("number of slices: "))
        print(numOfSlices)

        points = slice_mesh(filePathInput, numOfSlices)
        writeToFile(points)

    else:
        print("ok bye")