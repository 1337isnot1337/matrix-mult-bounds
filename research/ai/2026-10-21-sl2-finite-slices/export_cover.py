"""Export finite witnesses from discovery; acceptance is verify_cover.py."""
import argparse
from collections import Counter
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT/'results/sl2-finite-slices-2026-10-21'


def export():
    discovery = json.loads((RESULTS/'lift-pilot.json').read_text())
    basis = discovery['basis']
    degrees = [degree+4*epsilon if i < 88 else epsilon
               for i, (_, _, degree, epsilon) in enumerate(discovery['basis_types'])]
    covers = []
    for extra in (False, True):
        suffix = '-c2' if extra else ''
        files = [RESULTS/f'{component}{suffix}-cover-pilot.json'
                 for component in ('principal', 'matrix')]
        if not all(path.exists() for path in files):
            continue
        records = [json.loads(path.read_text()) for path in files]
        if any(record['selected_coordinates'] is None for record in records):
            continue
        selected = [sorted(a+b) for a, b in zip(*(record['selected_coordinates'] for record in records))]
        covers.append({'extra_C2': extra, 'selected_coordinates': selected,
                       'slice_upper_bound': sum(map(len, selected))})
    weighted = json.loads((RESULTS/'c2-cube-weights-pilot.json').read_text())
    rows = []
    for row in weighted['rows']:
        j = row['principal_factors']
        weights = row['best']['weights']
        factors = []
        for ds, scale, times in (
                (degrees[:88], weights['principal_scale'], j),
                (degrees[88:], weights['matrix_central'], 3-j)):
            hist = Counter(ds)
            factor = [hist.get(k//scale, 0) if k % scale == 0 else 0
                      for k in range(max(ds)*scale+1)]
            factors += [factor]*times
        factor = [1]+[0]*(weights['extra_C2']-1)+[1]
        factors += [factor]*3
        coefficients = [1]
        for factor in factors:
            out = [0]*(len(coefficients)+len(factor)-1)
            for a, x in enumerate(coefficients):
                for b, y in enumerate(factor):
                    out[a+b] += x*y
            coefficients = out
        cuts = row['best']['cutoffs']
        rows.append({'principal_factors': j, 'word_multiplicity': comb(3, j),
                     'weights': weights, 'cutoffs': cuts, 'degree_counts': coefficients,
                     'per_word_slices': sum(sum(coefficients[:c+1]) for c in cuts)})
    cube = {'power': 3, 'extra_C2': True, 'rows': rows,
            'slice_upper_bound': sum(row['word_multiplicity']*row['per_word_slices'] for row in rows),
            'rectangular_volume_upper_bound': 2481}
    return {'schema': 'nonsplit-coordinate-slice-cover-v1',
            'coefficient_field': 'F2[w]/(w^2+w+1)', 'group': 'SL(2,F5)',
            'group_ordering': 'identity followed by lexicographic determinant-one matrices',
            'basis': basis, 'basis_degrees': degrees, 'covers': covers,
            'cube': cube, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(export(), indent=2)+'\n')
