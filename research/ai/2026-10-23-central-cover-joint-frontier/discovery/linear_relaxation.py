"""Optional numerical joint-sum relaxation; no acceptance or construction."""
import argparse
from itertools import permutations
import json
from math import isqrt, prod
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT/'research/ai/2026-10-21-semisimple-koszul'))
from semisimple_koszul import padded_basic_ranks, source_ranks
from rank_locus_obstruction import profile, screen


def run(tails):
    degrees = [1, 2, 2, 3, 3, 4, 4, 5, 6]
    dimension = 120
    source = source_ranks(degrees)
    source_profile = profile(degrees)
    items, columns = [], []
    for b in range(1, isqrt(dimension)+1):
        for c in range(b, dimension//b+1):
            for a in range(1, b+1):
                shape = (a, b, c)
                if a*b > 98 or screen(degrees, shape, source_profile)['excluded']:
                    continue
                ranksets = [(z, padded_basic_ranks(x, y, dimension))
                            for x, y, z in set(permutations(shape))]
                if any(z*r[p] > source[p] for z, r in ranksets for p in range(len(source))):
                    continue
                averaged = [sum(z*r[p] for z, r in ranksets)/len(ranksets)
                            for p in range(len(source))]
                column = [a*b/98]+[r/s for r, s in zip(averaged, source)]
                if tails:
                    for t in range(1, dimension+1):
                        target = sum(x*y*(z >= t) for x, y, z in set(permutations(shape)))/len(ranksets)
                        column.append(target/(dimension-source_profile[t-1]['dimension']))
                items.append(shape)
                columns.append(column)
    matrix = np.array(columns).T
    costs = np.array([prod(shape)**.75 for shape in items])
    result = linprog(-costs, A_ub=matrix, b_ub=np.ones(matrix.shape[0]),
                     bounds=(0, None), method='highs')
    if not result.success:
        raise RuntimeError(result.message)
    return {'items': items, 'lp_upper_float': float(-result.fun),
            'weights_float': list(-result.ineqlin.marginals),
            'primal_float': list(result.x), 'source_degrees': degrees,
            'acceptance_status': 'numerical discovery only', 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile-tails', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run(args.profile_tails)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(report['lp_upper_float'])
