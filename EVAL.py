#!/usr/bin/env python
import sys
from collections import Counter
from numpy import log, exp


if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\n')
    N = int(lines[0])
    s = lines[1]
    cgs = [float(x) for x in lines[2].split()]
    c = Counter(s)
    for cg in cgs:
        log_p = (c['A'] + c['T']) * log((1 - cg)/2) + (c['C'] + c['G']) * log(cg/2)
        sys.stdout.write('%s ' % str(exp(log_p) * (N-1)))
    sys.stdout.write('\n')