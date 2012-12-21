#!/usr/bin/env python
import sys
from Bio import SeqIO
from Bio.SeqUtils import GC


if __name__ == '__main__':
    max_gc = max(SeqIO.parse(sys.stdin, 'fasta'), key=lambda rec: GC(rec.seq))
    print(max_gc.id)
    print('%s%%' % GC(max_gc.seq))
