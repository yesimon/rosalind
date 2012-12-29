#!/usr/bin/env python
import sys
from itertools import product
from Bio.SubsMat.MatrixInfo import blosum62


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    f = {}
    g = {}
    h = {}
    m.update({((i, 0), (-11 - i, (i-1, 0))) for i in range(1, sl+1)})
    m.update({((0, i), (-11 - i, (0, i-1))) for i in range(1, tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = blosum62.get((s[i-1], t[j-1]))
        if cost == None:
            cost = blosum62.get((t[j-1], s[i-1]))
        f[(i, j)] = m[(i-1, j-1)][0] + cost
        gg = g.get((i-1, j))
        if gg != None:
            gg -= 1
        hh = h.get((i, j-1))
        if hh != None:
            hh -= 1
        g[(i, j)] = max(m[(i-1, j)][0] - 12, gg)
        h[(i, j)] = max(m[(i, j-1)][0] - 12, hh)
        v = max(f[(i, j)], g[(i, j)], h[(i, j)])
        if v == f[(i, j)]:
            m[(i, j)] = (v, (i-1, j-1))
        elif v == g[(i, j)]:
            m[(i, j)] = (v, (i-1, j))
        elif v == h[(i, j)]:
            m[(i, j)] = (v, (i, j-1))
    print(m[(i,j)][0])
