#!/usr/bin/env python
import sys
from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62
import numpy as np


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    T = np.zeros((sl+1, tl+1), dtype=np.character)
    V = np.zeros((sl+1, tl+1))
    F = np.zeros((sl+1, tl+1))
    G = np.zeros((sl+1, tl+1))
    H = np.zeros((sl+1, tl+1))
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        if (s[i-1], t[j-1]) in blosum62:
            cost = blosum62[(s[i-1], t[j-1])]
        else:
            cost = blosum62[(t[j-1], s[i-1])]
        F[i, j] = V[i-1, j-1] + cost
        G[i, j] = max(V[i-1, j] - 12, G[i-1, j] - 1)
        H[i, j] = max(V[i, j-1] - 12, H[i, j-1] - 1)
        V[i, j] = v = max(F[i, j], G[i, j], H[i, j], 0)
        if v == F[i, j]:
            T[i, j] = 'D'
        elif v == G[i, j]:
            T[i, j] = 'L'
        elif v == H[i, j]:
            T[i, j] = 'U'
        elif v == 0:
            T[i, j] = ''
    i, j = np.unravel_index(np.argmax(V), V.shape)
    print(int(V[i, j]))
    sa = ''
    ta = ''
    while T[i, j]:
        dir = T[i, j]
        if dir == 'D':
            sa += s[i-1]
            ta += t[j-1]
            i, j = i - 1, j - 1
        elif dir == 'L':
            ta += t[j-1]
            i = i - 1
        elif dir == 'U':
            sa += s[i-1]
            j = j - 1
    print(''.join(reversed(sa)))
    print(''.join(reversed(ta)))
