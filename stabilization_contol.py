import numpy as np
from sympy import Symbol, solve, symbols, Matrix, factor

np.set_printoptions(linewidth=np.inf)


P = np.array([[-1, 0, 1, 0],
              [1, 0, 0, 1],
              [1, 0, 0, 0],
              [0, -1, 0, 0]])

Q = np.array([[0],
              [0],
              [1],
              [0]])

lamdas = np.array([-1, -1, -1,-1 ])


# P = np.array([[1, -2, 2],
#               [-1, 2, -1],
#               [1, 1, 0]])

# Q = np.array([[0], [0] , [1]])

# lamdas = np.array([-1, -2, -3])

dim = Q.size

K = np.zeros(shape=(dim, dim))
for i in range(dim):
    next_col = np.linalg.matrix_power(P, i) @ Q
    K[:, i] = next_col[:, 0]

charpoly_P = np.poly(P)

P0  = (np.linalg.inv(K)) @ P @ K

T = np.eye(dim)
for i in range(dim - 1):
    T[i, i + 1:] = charpoly_P[1:-(i + 1)]

caPbar = (np.linalg.inv(T)) @ P0 @ T
caPbar = np.where(np.abs(caPbar) > 1e-6, caPbar, 0)
QpBar = (np.linalg.inv(T)) @ (np.linalg.inv(K)) @ Q
QpBar = np.where(np.abs(QpBar) > 1e-6, QpBar, 0)

betta = np.poly(lamdas)[1:]
alpha = charpoly_P[1:]
c = alpha - betta

u = c @ (np.linalg.inv(K @ T))

print(u)