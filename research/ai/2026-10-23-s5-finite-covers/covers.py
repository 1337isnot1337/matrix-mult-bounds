"""Export finite integer-weight slice covers of the certified S5 blocks."""

import argparse
from hashlib import sha256
from itertools import accumulate
import json
from math import comb, gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LAYERS = [17, 9, 9, 18, 9, 9, 17]
INPUTS = [
    'research/ai/2026-10-21-s5-block-filtration/blocks.py',
    'results/s5-block-filtration-2026-10-21/certificate.json',
    'research/ai/2026-10-21-s5-split/verify_radical.py',
    'results/s5-split-2026-10-21/radical-pilot.json',
    'results/s5-block-filtration-2026-10-21/frontier.json',
    'research/ai/2026-10-21-central-cover-finite-slices/proof.md',
]
SCOPE = ('One-copy characteristic-two degenerations to a single matrix tensor; '
         'over C only the maintained coefficient-one coordinate/potential class.')


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def degree_counts(j, k, s, h):
    principal = [0] * (6*s+1)
    principal[::s] = LAYERS
    central = [0] * (h+1)
    central[0] = central[h] = 1
    result = [1]
    for _ in range(j):
        result = multiply(result, principal)
    for _ in range(k):
        result = multiply(result, central)
    return result


def choose_cutoffs(counts):
    maximum = len(counts)-1
    prefix = [0] + list(accumulate(counts))
    # End of each constant-prefix interval, including the empty prefix.
    endpoints = [d-1 for d, count in enumerate(counts) if count] + [maximum]
    best = (sum(counts), None)
    for a in endpoints:
        for b in endpoints:
            c = maximum-2-a-b
            if c < -1:
                continue
            cost = prefix[a+1] + prefix[b+1] + prefix[min(c+1, len(counts))]
            if cost < best[0]:
                best = cost, [a, b, c]
    return best


def export():
    old = json.loads((ROOT/INPUTS[4]).read_text())
    sources = []
    for r, prior in zip((1, 2), old['sources']):
        rows = []
        for j in range(4):
            k = 3*(r+1)-j
            candidates = []
            for s in range(1, 13):
                for h in range(1, 13):
                    if gcd(s, h) != 1:
                        continue
                    counts = degree_counts(j, k, s, h)
                    cost, cuts = choose_cutoffs(counts)
                    candidates.append((cost, s, h, cuts, counts))
            cost, s, h, cuts, counts = min(candidates, key=lambda row: row[:3])
            rows.append({
                'principal_factors': j, 'central_factors': k,
                'word_multiplicity': comb(3, j), 'matrix_multiplicity': 16**(3-j),
                'weights': [s, h], 'cutoffs': cuts,
                'degree_counts_without_matrix': counts,
                'whole_leg_slices': 88**j * 16**(3-j) * 2**k,
                'selected_slices': cost * 16**(3-j),
                'primitive_weight_pairs_tested': len(candidates),
            })
        bound = sum(row['word_multiplicity'] * row['selected_slices'] for row in rows)
        survivors = [row for row in prior['records'] if not row['complex_koszul_excluded']]
        new = [row['shape'] for row in survivors if row['volume']**2 > bound
               and not row['coordinate_modular_excluded']]
        sources.append({
            'central_rank': r, 'source_dimension': 120*2**r, 'power': 3,
            'rows': rows, 'slice_upper_bound': bound,
            'single_target_volume_upper_bound': isqrt(bound),
            'previous_complex_test_survivor_count': len(survivors),
            'new_coordinate_exclusions': new,
            'remaining_shapes': [row['shape'] for row in survivors if row['volume']**2 <= bound],
        })
    return {
        'schema': 's5-finite-covers-v1', 'base_commit': 'dcd209a82e3bf97a64f8e747dd29f3a3242d8e0b',
        'source_pins': {path: sha256((ROOT/path).read_bytes()).hexdigest() for path in INPUTS},
        'scope': SCOPE, 'proof_status': 'written proof; unreviewed; not formalized',
        'weight_search_limit': 12, 'sources': sources,
        'optimal_cover_claimed': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(export(), indent=2)+'\n')
