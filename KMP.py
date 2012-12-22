#!/usr/bin/env python
import sys


if __name__ == '__main__':
    s = sys.stdin.read().strip()
    sys.stdout.write('0 ')
    for k in range(1, len(s)):
        match = 0
        for i in range(1, k):
            if s[k+1-i:k+1] == s[:i]:
                match += 1
            else:
                break
        sys.stdout.write('%s ' % match)
    sys.stdout.write('\n')
