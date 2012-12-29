#!/usr/bin/env python
import sys
from itertools import product


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')
    sl, tl = len(s), len(t)
    m = {}
    m.update({((i, 0), i) for i in range(sl+1)})
    m.update({((0, i), i) for i in range(tl+1)})
    for i, j in product(range(1, sl+1), range(1, tl+1)):
        cost = 0 if s[i-1] == t[j-1] else 1
        m[(i, j)] = min(m[(i-1, j-1)] + cost, m[(i-1, j)] + 1, m[(i, j-1)] + 1)
    print m[(i, j)]
