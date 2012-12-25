#!/usr/bin/env python
import sys
import pickle
from itertools import combinations, permutations


def p_mul(x, y):
    return tuple([x[yy - 1] for yy in y])


def p_inv(x):
    return tuple([x.index(i + 1) + 1 for i in range(len(x))])


def p_rev(p, x, y):
    if x == 0:
        return p[y::-1] + p[y+1:]
    if y == len(p) - 1:
        return p[:x] + p[:x-1:-1]
    return p[:x] + p[y:x-1:-1] + p[y+1:]


def n_table(n):
    i = tuple(range(1, n+1))
    table = {i: (0, None)}
    ring = set([i])
    new_ring = set()
    perms = set([x for x in permutations(range(1, n+1))])
    n_fac = len(perms)
    while len(table) < n_fac:
        for p in ring:
            dep, _ = table[p]
            for i, j in combinations(range(n), 2):
                pr = p_rev(p, i, j)
                if not pr in table:
                    new_ring.add(pr)
                    table[pr] = (dep + 1, (i, j))
        ring, new_ring = new_ring, set()
    return table


if __name__ == '__main__':
    pair = [tuple([int(x) for x in l.split()]) for l in sys.stdin.read().strip().split('\n')]
    n = len(pair[0])
    try:
        with open('SORT_table.pkl', 'rb') as f:
            table = pickle.load(f)
    except IOError, pickle.UnpicklingError:
        table = n_table(n)
        with open('SORT_table.pkl', 'wb') as f:
            pickle.dump(table, f)
    pi = p_mul(p_inv(pair[1]), pair[0])
    print(table[pi][0]) # Reversal distance
    while pi != tuple(range(1, n+1)):
        i, j = table[pi][1]
        print('%s %s' % (i+1, j+1))
        pi = p_rev(pi, i, j)
