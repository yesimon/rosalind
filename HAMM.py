#!/usr/bin/env python
import sys


if __name__ == '__main__':
    str1, str2 = sys.stdin.read().split('\n')[:2]
    print(sum([int(a != b) for a, b in zip(str1, str2)]))
