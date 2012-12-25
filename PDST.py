#!/usr/bin/env python
from __future__ import division
import sys
from itertools import combinations
from Bio import SeqIO


if __name__ == '__main__':
    ss = [str(x.seq) for x in SeqIO.parse(sys.stdin, 'fasta')]
    D = [[0 for _ in ss] for _ in ss]
    n = len(ss[0])
    for i, j in combinations(range(len(ss)), 2):
        diff = sum([x != y for x, y in zip(ss[i], ss[j])]) / n
        D[i][j] = diff
        D[j][i] = diff
    for line in D:
        print ' '.join([str(x) for x in line])
