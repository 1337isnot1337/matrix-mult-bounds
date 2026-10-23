"""Export the selected Peirce-basis finite covers using integer polynomials."""

import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
import json
from math import comb, isqrt, prod
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
SOURCE = ROOT/'results/s5-peirce-covers-2026-10-23/source.json'
PRIOR = ROOT/'results/s5-finite-covers-2026-10-23/certificate.json'
FRONTIER = ROOT/'results/s5-block-filtration-2026-10-21/frontier.json'


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def export():
    spec = importlib.util.spec_from_file_location('s5_peirce_weight_source', PACKAGE/'source.py')
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    basis = json.loads(SOURCE.read_text())
    receipt = source.replay(basis)
    prior = json.loads(PRIOR.read_text())
    frontier = json.loads(FRONTIER.read_text())
    parameters = {
        1: [(-1, 1, [1, 1, 2]), (-1, 5, [9, 13, 13]),
            (-1, 5, [14, 14, 14]), (1, 6, [17, 17, 18])],
        2: [(-1, 1, [2, 2, 3]), (-1, 5, [14, 18, 18]),
            (-1, 5, [19, 19, 19]), (1, 6, [23, 23, 24])],
    }
    sources = []
    for r in (1, 2):
        rows = []
        for j, (v, h, cuts) in enumerate(parameters[r]):
            degrees = source.degree_family(1, v)
            histogram = Counter(degrees[t] for t in basis['principal_labels'])
            principal = [histogram[d] for d in range(max(histogram)+1)]
            central = [0]*(h+1)
            central[0] = central[h] = 1
            k = 3*(r+1)-j
            polynomial = [1]
            for _ in range(j):
                polynomial = multiply(polynomial, principal)
            for _ in range(k):
                polynomial = multiply(polynomial, central)
            cost = 16**(3-j)*sum(sum(polynomial[:cut+1]) for cut in cuts)
            rows.append({'principal_factors': j, 'principal_degrees': degrees,
                         'central_weight': h, 'source_degree_bound': 12,
                         'cutoffs': cuts, 'selected_slices': cost})
        bound = sum(comb(3, j)*row['selected_slices'] for j, row in enumerate(rows))
        old_bound = prior['sources'][r-1]['slice_upper_bound']
        previous_shapes = [row['shape'] for row in frontier['sources'][r-1]['records']
                           if not row['complex_koszul_excluded'] and row['volume']**2 <= old_bound]
        sources.append({'central_rank': r, 'power': 3, 'rows': rows,
                        'slice_upper_bound': bound, 'single_target_volume_upper_bound': isqrt(bound),
                        'additional_coordinate_exclusions': [s for s in previous_shapes if prod(s)**2 > bound],
                        'remaining_shapes': [s for s in previous_shapes if prod(s)**2 <= bound]})
    return {'schema': 's5-peirce-finite-covers-v1',
            'source_sha256': sha256(json.dumps(basis, sort_keys=True).encode()).hexdigest(),
            'prior_pins': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                           for p in (PRIOR, FRONTIER)},
            'sources': sources, 'source_coefficients_checked': receipt['original_coefficients_checked'],
            'improves_omega': False, 'arbitrary_complex_exclusion': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(export(), indent=2)+'\n')
