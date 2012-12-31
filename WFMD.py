#!/usr/bin/env python
from __future__ import division
import sys
from scipy.misc import factorial


if __name__ == '__main__':
    N, m, g, k = [int(x) for x in sys.stdin.read().strip().split()]
    p = m / (2*N)
    q = 1 - p
    pr = 0
    for i in range(0, k):
        pr += factorial(2*N)/(factorial(i)*factorial(2*N-i)) * p ** i * q ** (2*N-i)
    print(pr)
