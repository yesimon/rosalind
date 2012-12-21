#!/usr/bin/env python
import sys
from collections import Counter

if __name__ == '__main__':
    dna = sys.stdin.read()
    counts = Counter(dna)
    print('%i %i %i %i' % (counts['A'], counts['C'], counts['G'], counts['T']))
