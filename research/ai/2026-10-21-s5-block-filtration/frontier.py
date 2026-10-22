"""Compare the new modular bound with the credited complex necessary tests."""

import argparse
from fractions import Fraction
from math import isqrt, prod
import json
from pathlib import Path
import sys

from blocks import comparisons, PACKAGE

sys.path.insert(0, str(PACKAGE.parent/'2026-10-21-semisimple-koszul'))
from semisimple_koszul import source_ranks, target_screen
from rank_locus_obstruction import profile, screen, gate_9_fourths


def frontier(central_rank):
    if central_rank not in (1, 2):
        raise ValueError('this finite comparison covers one or two central C2 factors')
    degrees = [1, 1, 4, 4, 5, 5, 6] * (2**central_rank)
    ambient = sum(d*d for d in degrees)
    locus = profile(degrees)
    koszul = source_ranks(degrees)
    upper = Fraction(comparisons()['central_factor_upper_bounds'][central_rank])
    records = []
    checked = improving = 0
    for b in range(2, isqrt(ambient)+1):
        for c in range(b, ambient//b+1):
            for a in range(2, b+1):
                checked += 1
                shape = [a, b, c]
                if not gate_9_fourths(degrees, shape):
                    continue
                improving += 1
                if screen(degrees, shape, locus)['excluded']:
                    continue
                prior = target_screen(degrees, shape, koszul)
                records.append({
                    'shape': shape,
                    'volume': prod(shape),
                    'complex_koszul_excluded': prior['excluded'],
                    'complex_koszul_witness': prior.get('witness'),
                    'coordinate_modular_excluded': prod(shape)**2 > upper**3,
                })
    new = [r['shape'] for r in records
           if r['coordinate_modular_excluded'] and not r['complex_koszul_excluded']]
    return {
        'source': 'S5 x C2^'+str(central_rank),
        'source_dimension': ambient,
        'complex_degrees': degrees,
        'sorted_shapes_checked': checked,
        'strict_9_fourths_degree_gate_count': improving,
        'rank_locus_survivor_count': len(records),
        'full_complex_koszul_survivor_count': sum(not r['complex_koszul_excluded'] for r in records),
        'modular_exclusion_count_after_rank_locus': sum(r['coordinate_modular_excluded'] for r in records),
        'additional_coordinate_exclusions_after_koszul': new,
        'modular_source_strict_upper_bound': str(upper),
        'records': records,
        'scope': 'Every sorted integer shape with minimum side at least two and largest leg at most the source dimension. General complex gates retain their original scope; the new modular exclusions concern coordinate/potential maps only.',
    }


def report():
    return {'sources': [frontier(r) for r in (1, 2)],
            'improves_omega': False,
            'proof_status': 'written proof; unreviewed; no construction'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    value = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(value, indent=2)+'\n')
    print(json.dumps([{k: v for k, v in row.items() if k != 'records'}
                      for row in value['sources']], indent=2))
