import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

plt.style.use("default")

def show(X_old, X_new, M, title, lim=1000):
    plt.figure(figsize=(5, 5))
    plt.fill(X_old[0], X_old[1], color="gray", alpha=0.4) # (2, N)
    plt.fill(X_new[0], X_new[1], color="green", alpha=0.4)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.gca().set_aspect("equal", adjustable="box")  # equal scale
    plt.axhline(0, color="black", linewidth=0.8)  # (y = 0)
    plt.axvline(0, color="black", linewidth=0.8)  # (x = 0)
    plt.grid(True, linestyle="--", color="gray", alpha=0.5)
    plt.title(title)
    plt.show()
    print(title)
    print(np.round(M, 3))

# X_old is the original figure (gray).
# X_new is a figure after conversion (green).
# M is a matrix, we only print it.
# Title is the title of the picture.

def plot_off(vertices, faces):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # polygon mesh from the faces
    mesh = Poly3DCollection([vertices[face] for face in faces],
                            alpha=0.3, edgecolor='k')
    ax.add_collection3d(mesh)

    # vertices as red points
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # scale the scene to the model
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    plt.show()


def visualize_off(vertices, faces):
    """Interactive viewer (rotate/zoom with the mouse). Only displays, does not transform."""
    import open3d as o3d

    mesh = o3d.geometry.TriangleMesh()                                   # triangle mesh
    mesh.vertices = o3d.utility.Vector3dVector(vertices)                 # load vertices
    mesh.triangles = o3d.utility.Vector3iVector(np.array(faces))         # load face indices
    mesh.compute_vertex_normals()                                        # normals for correct shading

    o3d.visualization.draw_geometries([mesh])                            # open the interactive window