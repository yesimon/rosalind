#!/usr/bin/env python
import sys
import string


if __name__ == '__main__':
    dna = sys.stdin.read()
    trans = string.maketrans('T', 'U')
    print(string.translate(dna, trans))
