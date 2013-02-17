#!/usr/bin/env python
import sys
from Bio import Entrez

if __name__ == '__main__':
    species, minlen, maxlen, date = sys.stdin.read().strip().split('\n')
    Entrez.email = 'test@example.com'
    term = ('srcdb_refseq[Properties] AND {}[Organism] AND {}:{}[Sequence Length] '
            'AND 0:{}[Publication Date]'.format(species, minlen, maxlen, date))
    record = Entrez.read(Entrez.esearch(db='nucleotide', term=term))
    print(record['Count'])
