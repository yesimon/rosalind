#!/usr/bin/env python
import sys
from Bio.Seq import Seq


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    n = len(ss[0])
    ss2 = [str(Seq(s).reverse_complement()) for s in ss]
    ss.extend(ss2)
    db = set([(s[:-1], s[1:]) for s in ss])
    for e in db:
        print('(%s, %s)' % e)
