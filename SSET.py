#!/usr/bin/env python
import sys


if __name__ == '__main__':
    n = int(sys.stdin.read().strip())
    print(2 ** n % 1000000)
