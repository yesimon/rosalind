#!/usr/bin/env python
import sys
from Bio import Entrez
from Bio import SeqIO

if __name__ == '__main__':
    ids = sys.stdin.read().strip().split()
    Entrez.email = 'test@example.com'
    recs = SeqIO.parse(Entrez.efetch(db='nucleotide', id=ids, rettype='fasta'), 'fasta')
    print(min(recs, key=lambda x: len(x.seq)).format('fasta'))
