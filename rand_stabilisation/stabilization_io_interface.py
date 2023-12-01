import numpy as np
from h5py import File
from scipy.io import savemat
from stabilization_regulator import regulator

P = np.array([[0, 0, 0, 1],[0, -1, 1, 0],[ 1, -1, 0, 0],[ 1, 0, 0, 0]])
Q = np.transpose(np.array([[0, 0, 1, 0], [1, 0, 0, 0]]))
lamdas = np.array([-1, -1, -1, -1])

regulator = regulator(P, Q, lamdas)
mdicU = {'C': regulator,
         'P' : P,
         'Q' : Q,
         'lamdas': lamdas}
savemat('./stabilization.mat', mdicU)
print(regulator)