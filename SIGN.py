#!/usr/bin/env python
import sys
from itertools import permutations, repeat, product
from scipy.misc import factorial


if __name__ == '__main__':
    n = int(sys.stdin.read().strip())
    print(2 ** n * factorial(n, 1))
    for x in permutations(range(1, n+1)):
        signs = [i for i in product(*repeat([-1, 1], n))]
        for s in signs:
            print(' '.join([str(k) for k in (tuple(a * b for a, b in zip(x, s)))]))