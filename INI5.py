#!/usr/bin/env python
import sys


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    for i, s in enumerate(ss):
        if i % 2 == 1:
            print(s)
