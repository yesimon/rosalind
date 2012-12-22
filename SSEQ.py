#!/usr/bin/env python
import sys


if __name__ == '__main__':
    s, t = sys.stdin.read().strip().split('\n')[:2]
    j = 0
    for i, ss in enumerate(s):
        if t[j] == ss:
            sys.stdout.write('%s ' % str(i + 1))
            j += 1
            if j == len(t):
                sys.stdout.write('\n')
                break
