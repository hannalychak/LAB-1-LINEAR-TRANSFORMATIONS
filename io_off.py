import numpy as np


def read_off(filename: str):
    with open(filename, 'r') as f:
        # check that the first line is OFF
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')

        # number of vertices and faces (the third value is usually ignored)
        n_verts, n_faces, _ = map(int, f.readline().strip().split())

        # vertex coordinates (x, y, z)
        verts = [list(map(float, f.readline().strip().split())) for _ in range(n_verts)]

        # faces: the first number is the vertex count of the face (ignored), then indices
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range(n_faces)]

    return np.array(verts), faces