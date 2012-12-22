#!/usr/bin/env python
import sys
import re
from Bio.Seq import Seq


if __name__ == '__main__':
    s = Seq(sys.stdin.read().strip())
    sr = s.reverse_complement()
    ss = [s, s[1:-2], s[2:-1], sr, sr[1:-2], sr[2:-1]]
    prots = set()
    for s in ss:
        prots.update((mo.groups()[0][:-1] for mo in re.finditer(r'(?=(M\w*\*))',  str(s.translate())) if mo))
    print '\n'.join(prots)
