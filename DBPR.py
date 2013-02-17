#!/usr/bin/env python
import sys
from Bio import ExPASy
from Bio import SwissProt

if __name__ == '__main__':
    rec = SwissProt.read(ExPASy.get_sprot_raw(sys.stdin.read().strip()))
    gos = [r[2].split(':')[1] for r in rec.cross_references if
           r[0] == 'GO' and r[2].startswith('P')]
    print('\n'.join(gos))
