#!/usr/bin/env python
from __future__ import division
import sys


if __name__ == '__main__':
    k, m, n = [int(x) for x in sys.stdin.read().split(' ')[:3]]
    T = k + m + n
    mf = m/T * (1/4 * (m-1)/(T-1) + 1/2 * n/(T-1)) # P(recessive | first parent = Dd)
    nf = n/T * (1/2 * m/(T-1) + (n-1)/(T-1)) # P(recessive | first parent = dd)
    print(1 - mf - nf)
