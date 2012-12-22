#!/usr/bin/env python
from __future__ import division
import sys
from Bio import SeqIO


tt = {
    frozenset(['A', 'G']): 'transition',
    frozenset(['C', 'T']): 'transition',
    frozenset(['A', 'C']): 'transversion',
    frozenset(['G', 'T']): 'transversion',
    frozenset(['A', 'T']): 'transversion',
    frozenset(['C', 'G']): 'transversion',
}


if __name__ == '__main__':
    rec1, rec2 = [x for x in SeqIO.parse(sys.stdin, 'fasta')][:2]
    transitions, transversions = 0, 0
    for s1, s2 in zip(str(rec1.seq), str(rec2.seq)):
        diff = tt.get(frozenset([s1, s2]))
        if diff:
            if diff == 'transition':
                transitions += 1
            elif diff == 'transversion':
                transversions += 1
    print(transitions/transversions)
