import numpy as np

P = np.array([[0, 0, 0, -1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0]])
Q = np.array([[0, 0, 0, 1]]).T
R = np.array([[0, 0, 1, 0]])
lamdas = np.array([-1]*P.shape[0])

# P_stab= np.array([[1, 0, 0, -1], [0, 1, 1, -1], [1, -1, 0, 0], [1, 0, 0, 0]])
# Q_stab = np.array([[0, 0, 1, 0]])
P_stab = P
Q_stab = Q
lamdas_stab = np.array([-1]*P_stab.shape[0])
