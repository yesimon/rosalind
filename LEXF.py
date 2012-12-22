#!/usr/bin/env python
import sys
from itertools import product, repeat


if __name__ == '__main__':
    line1, line2 = sys.stdin.read().split('\n')[:2]
    alphabet, n = line1.split(' '), int(line2)
    for x in product(*repeat(alphabet, n)):
        print(''.join(x))
