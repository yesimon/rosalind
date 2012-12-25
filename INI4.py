#!/usr/bin/env python
import sys


if __name__ == '__main__':
    a, b = [int(x) for x in sys.stdin.read().strip().split()]
    print(sum([x for x in range(a, b+1) if x % 2 == 1]))
