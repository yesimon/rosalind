#!/usr/bin/env python
import sys
import math


if __name__ == '__main__':
    s, line2= sys.stdin.read().split('\n')[:2]
    cgs = [float(x) for x in line2.split()]
    for cg in cgs:
        log_p = 0
        for c in s:
            if c in 'CG':
                log_p += math.log10(cg/2)
            else:
                log_p += math.log10((1-cg)/2)
        sys.stdout.write('%s ' % log_p)
    sys.stdout.write('\n')