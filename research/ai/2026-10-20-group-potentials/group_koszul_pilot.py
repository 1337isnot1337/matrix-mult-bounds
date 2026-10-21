"""Exact full-space Koszul necessary tests for two unconstructed group targets."""
from fractions import Fraction
import json
from math import comb
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '2026-10-20-paired-sources'))
from all_ranks import matrix_basic_rank


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def run():
    records = []
    for name, degrees, n in [('F8^2:C7', [1]*7+[7]*9, 19),
                             ('SL2(5)', [1,2,2,3,3,4,4,5,6], 10)]:
        ambient = sum(d*d for d in degrees)
        distinct = sorted(set(degrees))
        blocks = {d: [matrix_basic_rank(d,d,q) for q in range(d*d)]
                  for d in distinct}
        target = [matrix_basic_rank(n,n,q) for q in range(n*n)]
        rejected = []
        closest = None
        for p in range((ambient+1)//2):
            source = sum(degrees.count(d)*d*sum(choose(ambient-d*d,p-q)*rank
                         for q,rank in enumerate(blocks[d])) for d in distinct)
            dest = n*sum(choose(ambient-n*n,p-q)*rank for q,rank in enumerate(target))
            if dest > source:
                rejected.append(p)
            candidate = Fraction(source-dest,source),p,source,dest
            if closest is None or candidate[0] < closest[0]:
                closest = candidate
        records.append({'source':name, 'target':[n]*3,
                        'powers_checked':(ambient+1)//2,
                        'excluded_at_powers':rejected,
                        'closest_relative_gap':str(closest[0]),
                        'closest_power':closest[1],
                        'source_rank_at_closest':closest[2],
                        'target_rank_at_closest':closest[3],
                        'scope':'Necessary full-space Koszul test only; padded target '
                                'first leg and direct-sum source. No degeneration asserted.'})
    return records


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
