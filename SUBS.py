#!/usr/bin/env python
import re
import sys


if __name__ == '__main__':
    s, subs = sys.stdin.read().split('\n')[:2]
    print(' '.join([str(mo.start(0) + 1) for mo in re.finditer(r'(?=(%s))' % subs, s)]))
