#!/usr/bin/env python
import sys
import string


if __name__ == '__main__':
    dna = sys.stdin.read()
    trans = string.maketrans('ACGT', 'TGCA')
    print(string.translate(dna[::-1], trans))
