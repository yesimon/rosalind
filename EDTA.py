#!/usr/bin/env python
import sys
from itertools import product


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    m = {(0, 0): (0, None)}
    m.update({((i, 0), (i, (i-1, 0))) for i in range(1, sl+1)})
    m.update({((0, i), (i, (0, i-1))) for i in range(1, tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = 0 if s[i-1] == t[j-1] else 1
        d = m[(i-1, j-1)][0] + cost
        l = m[(i-1, j)][0] + 1
        u = m[(i, j-1)][0] + 1
        b = min(d, l, u)
        if d == b:
            m[(i, j)] = (b, (i-1, j-1))
        elif l == b:
            m[(i, j)] = (b, (i-1, j))
        elif u == b:
            m[(i, j)] = (b, (i, j-1))
    print(m[(i,j)][0])
    c = (i, j)
    sa = ''
    ta = ''
    while m[c][1] != None:
        i, j = c
        c = m[c][1]
        if i-1 == c[0] and j-1 == c[1]:
            sa += s[i-1]
            ta += t[j-1]
        elif i == c[0]:
            sa += '-'
            ta += t[j-1]
        elif j == c[1]:
            sa += s[i-1]
            ta += '-'
    print(''.join(reversed(sa)))
    print(''.join(reversed(ta)))
