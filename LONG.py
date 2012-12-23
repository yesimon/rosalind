#!/usr/bin/env python
import sys
from itertools import combinations


def overlap(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    if s2 in s1:
        return s1
    for i in range(1, len(s2)):
        if s1.endswith(s2[:len(s2)-i]):
            s = s1 + s2[len(s2)-i:]
            return s
        if s1.startswith(s2[i:]):
            s = s2 + s1[len(s2)-i:]
            return s
    return


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    while len(ss) != 1:
        best = {}
        best['len'] = 0
        for comb in combinations(ss, 2):
            joined = overlap(*comb)
            if joined:
                ol = len(comb[0]) + len(comb[1]) - len(joined)
                if ol > best['len']:
                    best['len'] = ol
                    best['joined'] = joined
                    best['comb'] = comb
        ss.pop(ss.index(best['comb'][0]))
        ss.pop(ss.index(best['comb'][1]))
        ss.append(best['joined'])
    print ss[0]
