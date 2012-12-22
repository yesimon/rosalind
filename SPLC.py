#!/usr/bin/env python
import sys
import re
from Bio.Seq import Seq


if __name__ == '__main__':
    lines = sys.stdin.read().strip().split('\n')
    rna, introns = lines[0], lines[1:]
    for intron in introns:
        rna = re.sub(intron, '', rna)
    print(str(Seq(rna).translate()[:-1]))
