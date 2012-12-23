#!/usr/bin/env python
import sys
from itertools import product, repeat
from collections import Counter
from Bio import SeqIO


def kmers(n):
    return [''.join(x) for x in product(*repeat('ACGT', n))]


if __name__ == '__main__':
    s = str(SeqIO.read(sys.stdin, 'fasta').seq)
    c = Counter([s[i:i+4] for i in range(len(s) - 3)])
    print(' '.join(str(c[kmer]) for kmer in kmers(4)))
