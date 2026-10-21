"""Apply the maintained exact matrix-rank formula in all target orientations."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'2026-10-20-paired-sources'))
from all_ranks import matrix_basic_rank


def screen():
    degrees = [1, 2, 2, 3, 3, 4, 4, 5, 6]*2
    ambient = sum(d*d for d in degrees)
    choose = lambda n, k: comb(n, k) if 0 <= k <= n else 0
    blocks = {d: [matrix_basic_rank(d, d, q) for q in range(d*d)] for d in set(degrees)}
    source = [sum(degrees.count(d)*d*sum(choose(ambient-d*d, p-q)*rank
              for q, rank in enumerate(blocks[d])) for d in blocks)
              for p in range(ambient)]
    reports = []
    for l, b, r in ((13, 15, 13), (13, 13, 15), (15, 13, 13)):
        target = [matrix_basic_rank(l, r, q) for q in range(l*r)]
        rows = []
        for p, rank in enumerate(source):
            dest = b*sum(choose(ambient-l*r, p-q)*value for q, value in enumerate(target))
            rows.append((rank-dest, p, rank, dest))
        closest = min(rows, key=lambda row: Fraction(row[0], row[2]))
        reports.append({'matrix_dimensions_l_b_r': [l, b, r], 'powers_checked': ambient,
            'excluded_at_powers': [p for gap, p, _, _ in rows if gap < 0],
            'closest_power': closest[1], 'source_rank_at_closest': closest[2],
            'target_rank_at_closest': closest[3],
            'closest_relative_gap': str(Fraction(closest[0], closest[2]))})
    return {'group': 'SL(2,5) x C2', 'shape': [13, 13, 15], 'reports': reports,
            'scope': 'Necessary full-space Koszul ranks in all orientations only. '
                     'Passing is not a degeneration.'}


if __name__ == '__main__':
    print(json.dumps(screen(), indent=2))
