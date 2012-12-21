#!/usr/bin/env python
import sys
from Bio import SeqIO


if __name__ == '__main__':
    adj = []
    recs = SeqIO.to_dict(SeqIO.parse(sys.stdin, 'fasta'))
    for seq_id, rec in recs.viewitems():
        for seq2_id, rec2 in recs.viewitems():
            if str(rec.seq)[-3:] == str(rec2.seq)[:3] and seq_id != seq2_id:
                adj.append((seq_id, seq2_id))
    for pair in adj:
        print(' '.join(pair))
