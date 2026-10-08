import numpy as np


def rotate_xy_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]])


def rotate_yz_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[1, 0,  0],
                     [0, c, -s],
                     [0, s,  c]])


def rotate_xz_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, 0, -s],
                     [0, 1,  0],
                     [s, 0,  c]])


def _apply(M, X):
    return (M @ X.copy().T).T      # X is (N, 3): transpose, multiply, transpose back


def rotate_xy(X, theta):
    return _apply(rotate_xy_matrix(theta), X)


def rotate_yz(X, theta):
    return _apply(rotate_yz_matrix(theta), X)


def rotate_xz(X, theta):
    return _apply(rotate_xz_matrix(theta), X)