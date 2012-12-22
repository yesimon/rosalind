#!/usr/bin/env python
import sys
from Bio.Seq import Seq


if __name__ == '__main__':
    print(Seq.translate(Seq(sys.stdin.read()))[:-1])
