#!/usr/bin/env python
import sys


if __name__ == '__main__':
    ss = sys.stdin.read().strip().split('\n')
    n = len(ss)
    db = dict([(s[:-1], s[1:]) for s in ss])
    k = db.iterkeys().next()
    s = ''
    while len(s) < n:
        s += db[k][-1]
        k = db[k]
    print(s)
