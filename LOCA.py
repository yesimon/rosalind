#!/usr/bin/env python
import sys
from itertools import product
from Bio.SubsMat.MatrixInfo import pam250


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    m.update({((i, 0), (0, (i-1, 0))) for i in range(1, sl+1)})
    m.update({((0, i), (0, (0, i-1))) for i in range(1, tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = pam250.get((s[i-1], t[j-1]))
        if cost == None:
            cost = pam250.get((t[j-1], s[i-1]))
        d = m[(i-1, j-1)][0] + cost
        l = m[(i-1, j)][0] - 5
        u = m[(i, j-1)][0] - 5
        z = 0
        b = max(d, l, u, z)
        if d == b:
            m[(i, j)] = (b, (i-1, j-1))
        elif l == b:
            m[(i, j)] = (b, (i-1, j))
        elif u == b:
            m[(i, j)] = (b, (i, j-1))
        elif z == b:
            m[(i, j)] = (b, None)
    c, v = max(m.iteritems(), key=lambda x: x[1][0])
    print(v[0])
    sa = ''
    ta = ''
    while m[c][1] != None:
        i, j = c
        c = m[c][1]
        if i-1 == c[0] and j-1 == c[1]:
            sa += s[i-1]
            ta += t[j-1]
        elif i == c[0]:
            ta += t[j-1]
        elif j == c[1]:
            sa += s[i-1]
    print(''.join(reversed(sa)))
    print(''.join(reversed(ta)))
