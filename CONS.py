#!/usr/bin/env python
import sys
from collections import Counter


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    ss_T = zip(*ss)
    profile = [Counter(line) for line in ss_T]
    print(''.join([p.most_common(1)[0][0] for p in profile]))
    for nuc in 'ACGT':
        print('%s: %s' % (nuc, ' '.join([str(p[nuc]) for p in profile])))
