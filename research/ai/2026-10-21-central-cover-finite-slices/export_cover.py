"""Export integer slice covers from the previously certified A5 basis."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT/'results/a5-peirce-2026-10-21/tight-certificate.json'


def multiply(a, b):
    result = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def export():
    raw = INPUT.read_bytes()
    prior = json.loads(raw)
    degrees = [(4-w)//3 for w in prior['degeneration_weights'][0][:44]]+[0]*16
    histogram = Counter(degrees[:44])
    polynomial = [histogram[i] for i in range(max(histogram)+1)]
    covers = []
    for n in (1, 2, 3):
        rows = []
        for j in range(n+1):
            coefficients = [1]
            for _ in range(j):
                coefficients = multiply(coefficients, polynomial)
            for _ in range(n):
                coefficients = multiply(coefficients, [1, 1])
            maximum = 4*j+n
            quotient, remainder = divmod(maximum, 3)
            cutoffs = [quotient]*(remainder+1)+[quotient-1]*(2-remainder)
            slices = sum(sum(coefficients[:cut+1]) for cut in cutoffs)*16**(n-j)
            leg_dimension = 44**j*16**(n-j)*2**n
            rows.append({'principal_factors': j, 'word_multiplicity': comb(n, j),
                         'degree_counts_without_matrix': coefficients,
                         'cutoffs': cutoffs, 'degree_cover_slices': slices,
                         'whole_leg_slices': leg_dimension,
                         'selected_slices': min(slices, leg_dimension)})
        covers.append({'power': n, 'rows': rows,
                       'slice_upper_bound': sum(row['word_multiplicity']*row['selected_slices']
                                                for row in rows),
                       'M10_power_slice_rank': 100**n})
    return {'schema': 'central-cover-finite-slices-v1', 'group': 'A5 x C2',
            'coefficient_field': prior['coefficient_field'],
            'basis': prior['basis'], 'degrees': degrees,
            'basis_source': {'path': str(INPUT.relative_to(ROOT)), 'sha256': sha256(raw).hexdigest()},
            'covers': covers, 'rectangular_volume_upper_bound': 986,
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(export(), indent=2)+'\n')
