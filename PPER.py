#!/usr/bin/env python
import sys
from scipy.misc import comb, factorial


if __name__ == '__main__':
    n, k = [int(x) for x in sys.stdin.read().strip().split(' ')]
    print(comb(n, k, 1) * factorial(k, 1) % 1000000)
