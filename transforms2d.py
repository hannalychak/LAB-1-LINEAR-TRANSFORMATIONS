import numpy as np

# Functions of Linear Transformations

def stretch_matrix(a, b):
    """Stretches or compresses the vector along each axis. The matrix
representation is diagonal"""
    return np.array([[a, 0],
                     [0, b]], dtype=float)

def shear_matrix(a, b):
    """Slants the vector by a scalar factor horizontally or vertically (or both
simultaneously)"""
    return np.array([[1, a],
                     [b, 1]], dtype=float)

def reflection_matrix(a, b):
    """Reflects the vector about a line that passes through the origin"""
    n = a * a + b * b
    if n == 0:
        raise ValueError("(a, b) must not be the zero vector")
    return np.array([[a * a - b * b, 2 * a * b],
                     [2 * a * b,     b * b - a * a]]) / n

def rotation_matrix(theta): # Theta θ - radians
    """Rotates the vector around the origin. (In theta θ - radians)"""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s],
                     [s,  c]])

# AL = L'

def _apply(M, X):
    return M @ X.copy() # @ - numpy multiplicator + make sure to copy the array before transforming it


def stretch(X, a, b):
    return _apply(stretch_matrix(a, b), X)


def shear(X, a, b):
    return _apply(shear_matrix(a, b), X)


def reflection(X, a, b):
    return _apply(reflection_matrix(a, b), X)


def rotation(X, theta):
    return _apply(rotation_matrix(theta), X)