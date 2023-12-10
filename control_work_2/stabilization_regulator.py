from itertools import accumulate
import operator
import numpy as np
from numpy.linalg import matrix_rank
np.set_printoptions(linewidth=np.inf, floatmode='maxprec', suppress=True)

def kalman_matrix(P, Q):
    n, r  = Q.shape
    K = np.zeros(shape=(n, n))
    ks = [0]
    while np.linalg.matrix_rank(K) < n:
        if len(ks) > r:
            print('System is not able to be stabilized')
            exit(1)
        q = Q[:, len(ks) - 1]
        next_col = np.linalg.matrix_power(P, ks[-1]) @ q
        Kupd = K.copy()
        Kupd[:, sum(ks)] = next_col
        # print(matrix_rank(K), matrix_rank(Kupd))

        if matrix_rank(K) == matrix_rank(Kupd):
            ks.append(0)
            continue
        
        K = Kupd
        ks[-1] += 1

    return K, ks


def construct_matrix_T(P0_block, lamdas):
    def sub_problem(p0, thetas):
        bettas = np.poly(thetas)[1:]
        alphas = np.poly(p0)[1:]
        c = alphas - bettas

        dim = p0.shape[0]
        t = np.eye(dim)
        for i in range(dim - 1):
            t[i, i + 1:] = alphas[:-(i + 1)]
        return t, c

    T = np.zeros((len(lamdas), len(lamdas)))
    C = np.zeros((P0_block.shape[0], len(lamdas)))
    ks = []
    for i in range(P0_block.shape[0]):
        p0 = P0_block[i, i]
        ks.append(p0.shape[0])
        rng0 = sum(ks[:-1])
        rng1 = sum(ks)
        t, c = sub_problem(p0, lamdas[rng0:rng1])
        T[rng0:rng1, rng0:rng1] = t
        C[i, rng0:rng1] = c

    return T, C


def splitxs(ks):
    splitxs = np.array(list(accumulate(ks, operator.add)))
    return splitxs

def split_into_blocks(P0, ks):
    splixs = splitxs(ks)[:-1]
    P0 = np.array(np.vsplit(P0, splixs))
    # print(P0, P0.shape)

    P0 = np.split(P0, splixs, axis=2)
    P0 = np.swapaxes(P0, 0, 1)
    # for i in range(len(splixs) + 1):
    #     for j in range(len(splixs) + 1):
            # print(f'P[{i}, {j}]: \n{P0[i, j]}\n')
    
    return P0

def regulator(P, Q, lamdas):    
    n, r = Q.shape

    # print(dim)
    # print(P)
    # print(Q)

    K, ks = kalman_matrix(P, Q) 

    P0  = (np.linalg.inv(K)) @ P @ K

    P0_block = split_into_blocks(P0, ks)
    T, C = construct_matrix_T(P0_block, lamdas)

    regulator = C @ np.linalg.inv(K @ T)

    return regulator    