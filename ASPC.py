#!/usr/bin/env python
import sys
from scipy.misc import comb


if __name__ == '__main__':
    n, m = [int(x) for x in sys.stdin.read().strip().split()]
    print(sum([comb(n, k, 1) for k in range(m, n+1)]) % 1000000)
