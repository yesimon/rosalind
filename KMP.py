#!/usr/bin/env python
import sys


if __name__ == '__main__':
    s = sys.stdin.read().strip()
    T = [0 for _ in s]
    T[:2] = -1, 0
    k, cnd = 2, 0
    while k < len(s):
        if s[k-1] == s[cnd]:
            cnd += 1
            T[k] = cnd
            k += 1
        elif cnd > 0:
            cnd = T[cnd]
        else:
            T[k] = 0
            k += 1
    T.append(0)
    print(' '.join([str(x) for x in T[1:]]))
