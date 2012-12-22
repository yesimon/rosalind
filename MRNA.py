#!/usr/bin/env python
import sys
from Bio.Data import CodonTable
from werkzeug.datastructures import MultiDict


if __name__ == '__main__':
    prot = sys.stdin.read().strip()
    rev = MultiDict()
    st = CodonTable.unambiguous_dna_by_name['Standard']
    for codon, aa in st.forward_table.viewitems():
        rev.add(aa, codon)
    remain = len(st.stop_codons)
    for aa in prot:
        remain = remain * len(rev.getlist(aa)) % 1000000
    print(remain)
