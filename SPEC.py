#!/usr/bin/env python
import sys
from operator import itemgetter


mass = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


if __name__ == '__main__':
    rm = [float(x) for x in sys.stdin.read().strip().split('\n')]
    m = [rm[i+1] - rm[i] for i in range(len(rm)-1)]
    rev = {b: a for a, b in mass.viewitems()}
    prot = []
    for mm in m:
        diffs = [(abs(mm - k), v) for k, v in rev.iteritems()]
        prot.append(min(diffs, key=itemgetter(0))[1])
    print(''.join(prot))
