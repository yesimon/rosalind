#!/usr/bin/env python
import sys
from Bio.Seq import Seq


if __name__ == '__main__':
    s = Seq(sys.stdin.read())
    sites = []
    for i in range(len(s) - 4):
        for j in range(4, min(13, len(s) - i + 1)):
            ss = s[i:i+j]
            if str(ss) == str(ss.reverse_complement()):
                print(' '.join([str(i + 1), str(j)]))
