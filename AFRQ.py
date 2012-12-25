#!/usr/bin/env python
import sys
from numpy import roots


if __name__ == '__main__':
    faas = [float(x) for x in sys.stdin.read().strip().split()]
    for faa in faas:
        q = faa ** 0.5
        p = max(roots([1, 2*q, q ** 2 - 1]))
        sys.stdout.write('%s ' % (2 * p * q + q ** 2))
    sys.stdout.write('\n')
