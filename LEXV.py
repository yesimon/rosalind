#!/usr/bin/env python
import sys
from itertools import product, repeat


if __name__ == '__main__':
    line1, line2 = sys.stdin.read().split('\n')[:2]
    alphabet, n = ''.join(line1.split(' ')), int(line2)
    for x in product(*repeat(' %s' % alphabet, n)):
        xs = ''.join(x).strip()
        if not x[0] == ' ' and not ' ' in xs:
            print xs
