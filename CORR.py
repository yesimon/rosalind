#!/usr/bin/env python
import sys
from collections import Counter
from Bio.Seq import Seq


def hamm(s1, s2):
    return sum([int(a != b) for a, b in zip(s1, s2)])


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    c = Counter()
    for s in ss:
        src = str(Seq(s).reverse_complement())
        if src in c:
            c[src] += 1
        else:
            c[s] += 1
    good, bad = [], []
    for k, v in c.viewitems():
        if v >= 2:
            good.append(k)
        else:
            bad.append(k)
    for b in bad:
        try:
            gi = [hamm(g, b) for g in good].index(1)
            print('%s->%s' % (b, good[gi]))
        except ValueError:
            brc = str(Seq(b).reverse_complement())
            grci = [hamm(g, brc) for g in good].index(1)
            print('%s->%s' % (b, str(Seq(good[grci]).reverse_complement())))
