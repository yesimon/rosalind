#!/usr/bin/env python
import sys
from itertools import permutations


if __name__ == '__main__':
    n = int(sys.stdin.read())
    perms = [x for x in permutations([str(x) for x in range(1, n+1)])]
    print(len(perms))
    for p in perms:
        print(' '.join(p))
