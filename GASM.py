#!/usr/bin/env python
import sys
from itertools import chain
from Bio.Seq import Seq


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    ss_rc = [str(Seq(s).reverse_complement()) for s in ss]
    n = len(ss)
    l = len(ss[0])
    for k in range(l-1, 1, -1):
        db = dict(flatten([[(s[i:i+k], s[i+1:i+k+1]) for i in range(l-k)] for s in ss]))
        db_rc = dict(flatten([[(s[i:i+k], s[i+1:i+k+1]) for i in range(l-k)] for s in ss_rc]))
        f = km = db.iterkeys().next()
        s = ''
        while True:
            if km in db:
                s += km[-1]
                km = db.pop(km)
                if km == f:
                    print s
                    sys.exit()
            elif km in db_rc:
                s += km[-1]
                km = db_rc.pop(km)
                if km == f:
                    print s
                    sys.exit()
            else:
                break
