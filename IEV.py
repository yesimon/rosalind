#!/usr/bin/env python
from __future__ import division
import sys


if __name__ == '__main__':
    a, b, c, d, e, _ = [int(x) for x in sys.stdin.read().split(' ')]
    print(2 * (a + b + c + 3/4 * d + 1/2 * e))
