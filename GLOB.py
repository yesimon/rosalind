#!/usr/bin/env python
import sys
from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    m.update({((i, 0), (i * -5, (i-1, 0))) for i in range(1, sl+1)})
    m.update({((0, i), (i * -5, (0, i-1))) for i in range(1, tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = blosum62.get((s[i-1], t[j-1]))
        if cost == None:
            cost = blosum62.get((t[j-1], s[i-1]))
        d = m[(i-1, j-1)][0] + cost
        l = m[(i-1, j)][0] - 5
        u = m[(i, j-1)][0] - 5
        b = max(d, l, u)
        if d == b:
            m[(i, j)] = (b, (i-1, j-1))
        elif l == b:
            m[(i, j)] = (b, (i-1, j))
        elif u == b:
            m[(i, j)] = (b, (i, j-1))
    print(m[(i,j)][0])
