#!/usr/bin/env python
import sys
import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, connected_components


if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    m = np.zeros((n, n))
    adj = [[int(x) for x in line.split(' ')] for line in lines[1:]]
    for edge in adj:
        m[edge[0]-1, edge[1]-1] = 1
    g = csgraph_from_dense(m)
    print(connected_components(g, False)[0] - 1)
