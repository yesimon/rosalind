#!/usr/bin/env python
import sys
from scipy.misc import comb


if __name__ == '__main__':
    k, N = [int(x) for x in sys.stdin.read().split(' ')]
    T = k ** 2
    print(sum([comb(T, i, 1) * 0.25**i * 0.75**(T-i) for i in range(N, T+1)]))
