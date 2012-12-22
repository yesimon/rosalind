#!/usr/bin/env python
import sys
from itertools import product


def ss_dp(*ss):
    """Find longest common substring of ss."""
    dp = {}
    for tups in product(*[[i for i in enumerate(s)] for s in ss]):
        co,  letters = zip(*tups)
        prev = tuple(x - 1 for x in co)
        if letters.count(letters[0]) == len(letters):
            dp[co] = dp.get(prev, 0) + 1
    co, length = max(dp.iteritems(), key=lambda x: x[1])
    return ss[0][co[0] + 1 - length:co[0] + 1]


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    print(reduce(ss_dp, ss))
