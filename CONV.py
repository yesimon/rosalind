#!/usr/bin/env python
import sys
from collections import Counter
from decimal import Decimal


if __name__ == '__main__':
    s1, s2 = [[Decimal(x) for x in line.split()] for line in sys.stdin.read().strip().split('\n')]
    c = Counter()
    for i in s1:
        for j in s2:
            c[i - j] += 1
    x, count = c.most_common(1)[0]
    print(count)
    print(abs(x))
