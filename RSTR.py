#!/usr/bin/env python
import sys
from collections import Counter
from math import log, exp


if __name__ == '__main__':
    line1, s = sys.stdin.read().strip().split('\n')
    line1 = line1.split()
    N, x = int(line1[0]), float(line1[1])
    c = Counter(s)
    log_p = (c['A'] + c['T']) * log((1 - x)/2) + (c['C'] + c['G']) * log(x/2)
    p = exp(log_p)
    print(1 - (1-p) ** N)
