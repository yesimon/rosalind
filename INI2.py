#!/usr/bin/env python
import sys


if __name__ == '__main__':
    print(sum([int(x) for x in sys.stdin.read().strip().split()]))
