#!/usr/bin/env python
import sys
from Bio import Entrez

if __name__ == '__main__':
    genus, start, end = sys.stdin.read().strip().split('\n')
    Entrez.email = 'test@example.com'
    term = '({}[Organism]) AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(
        genus, start, end)
    record = Entrez.read(Entrez.esearch(db='nucleotide', term=term))
    print(record['Count'])
