#!/usr/bin/env python
import sys
from itertools import product
from collections import defaultdict


if __name__ == '__main__':
    s1, s2 = sys.stdin.read().strip().split('\n')[:2]

    dp = defaultdict(str)
    for x, y in product(range(len(s1)), range(len(s2))):
        if s1[x] == s2[y]:
            dp[(x, y)] = dp[(x-1, y-1)] + s1[x]
        else:
            dp[(x, y)] = max(dp[(x-1, y)], dp[(x, y-1)], key=len)
    print(dp[len(s1)-1, len(s2)-1])
