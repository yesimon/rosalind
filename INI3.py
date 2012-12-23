#!/usr/bin/env python
import sys


if __name__ == '__main__':
    s, line2 = sys.stdin.read().strip().split('\n')[:2]
    a, b, c, d = [int(x) for x in line2.split()]
    print(' '.join(s[a:b+1], s[c:d+1]))
