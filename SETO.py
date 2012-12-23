#!/usr/bin/env python
import sys


if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    A = set([int(x) for x in lines[1][1:-1].split(',')])
    B = set([int(x) for x in lines[2][1:-1].split(',')])
    print('{%s}' % ', '.join([str(x) for x in A | B]))
    print('{%s}' % ', '.join([str(x) for x in A & B]))
    print('{%s}' % ', '.join([str(x) for x in A - B]))
    print('{%s}' % ', '.join([str(x) for x in B - A]))
    print('{%s}' % ', '.join([str(x) for x in set(range(1, n+1)) - A]))
    print('{%s}' % ', '.join([str(x) for x in set(range(1, n+1)) - B]))
