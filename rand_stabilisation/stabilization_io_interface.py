import numpy as np
from h5py import File
from scipy.io import savemat
from stabilization_regulator import regulator

with File('./rand_stabilisation.mat', 'r') as rs:
    P = np.array(rs.get('P')).transpose()
    Q = np.array(rs.get('Q')).transpose()
    lamdas = np.array(rs.get('lamdas'))[:, 0].transpose()

regulator = regulator(P, Q, lamdas)
mdicU = {'C': regulator}
savemat('./regulator.mat', mdicU)
print(regulator)