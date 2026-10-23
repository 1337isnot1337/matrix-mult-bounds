"""Exact finite census of two-equal-leg monotone S5 degree covers."""

import argparse
from hashlib import sha256
from itertools import accumulate, combinations_with_replacement
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT/'results/s5-finite-covers-2026-10-23/certificate.json'


def principal_counts(j):
    coefficients = [1]
    for _ in range(j):
        output = [0]*(len(coefficients)+6)
        for i, x in enumerate(coefficients):
            for d, y in enumerate((17, 9, 9, 18, 9, 9, 17)):
                output[i+d] += x*y
        coefficients = output
    return coefficients


def third_leg(first, maximum):
    k = len(first)-1
    return [max([-1] + [maximum-2-first[a]-first[b]
                        for a in range(k-c+1) for b in range(k-c-a+1)
                        if first[a] < maximum and first[b] < maximum])
            for c in range(k+1)]


def optimize(coefficients, central_counts):
    maximum, k = len(coefficients)-1, len(central_counts)-1
    prefix = [0] + list(accumulate(coefficients))
    best = prefix[-1]*sum(central_counts)
    witness = [[-1]*(k+1), [-1]*(k+1), [maximum]*(k+1)]
    cases = 0
    for ascending in combinations_with_replacement(range(-1, maximum+1), k+1):
        first = list(reversed(ascending))
        cases += 1
        initial = 2*sum(c*prefix[f+1] for c, f in zip(central_counts, first))
        if initial >= best:
            continue
        third = third_leg(first, maximum)
        cost = initial + sum(c*prefix[f+1] for c, f in zip(central_counts, third))
        if cost < best:
            best, witness = cost, [first, first[:], third]
    return {'cost': best, 'cutoffs': witness, 'first_staircases_checked': cases}


def export():
    prior = json.loads(INPUT.read_text())
    rows = []
    for source in prior['sources']:
        r = source['central_rank']
        for j in range(4):
            k = 3*(r+1)-j
            row = optimize(principal_counts(j), [comb(k, e)*16**(3-j) for e in range(k+1)])
            row.update(central_rank=r, principal_factors=j, central_factors=k,
                       prior_weighted_cost=source['rows'][j]['selected_slices'])
            rows.append(row)
    return {'schema': 's5-two-equal-staircase-v1',
            'source_pin': {'path': str(INPUT.relative_to(ROOT)), 'sha256': sha256(INPUT.read_bytes()).hexdigest()},
            'scope': 'Cube block-word bidegree majorants; monotone thresholds; two equal legs.',
            'rows': rows, 'total_first_staircases_checked': sum(row['first_staircases_checked'] for row in rows),
            'improved_word_count': sum(row['cost'] < row['prior_weighted_cost'] for row in rows),
            'arbitrary_cover_optimality_claimed': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(export(), indent=2)+'\n')
