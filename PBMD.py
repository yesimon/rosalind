#!/usr/bin/env python
import sys
from Bio import Entrez

if __name__ == '__main__':
    author, year = sys.stdin.read().strip().split('\n')
    Entrez.email = 'test@example.com'
    term = '"{}"[Date - Publication] : "{}"[Date - Publication] AND {}[Author]'.format(
        year, int(year) + 1, author)
    record = Entrez.read(Entrez.esearch(db='pubmed', term=term))
    print(record['IdList'][-1])
