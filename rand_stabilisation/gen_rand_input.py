import numpy as np
from h5py import File
from scipy.io import savemat
from stabilization_contol import stabilization

with File('./rand_stabilisation.mat', 'r') as rs:
    P = np.array(rs.get('randP')).transpose()
    Q = np.array(rs.get('Q')).transpose()
    lamdas = np.array(rs.get('lamdas'))[:, 0].transpose()

regulator = stabilization(P, Q, lamdas)
mdicU = {'u': regulator}
savemat('./stabilizating_control.mat', mdicU)
# print(regulator)