"""Exact rank-seven gap certificate and six-loss compression controls."""

import argparse
import importlib.util
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
spec = importlib.util.spec_from_file_location('rank_six_locus_base', PACKAGE / 'verify.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def verify(certificate, rank_six_certificate):
    base.validate_certificate(rank_six_certificate)
    raw, unit, inverse, high, mixed, labels, expected = base.source()
    if (certificate.get('dimension') != 31 or certificate.get('size') != 8
            or certificate.get('remaining_dimension') != 5 or certificate.get('labels') != labels
            or len(certificate.get('stages', [])) != 26):
        raise ValueError('incorrect rank-seven certificate dimensions or stages')
    terminal, transforms = base.eliminate(mixed, certificate['stages'], 8)
    if terminal != expected or transforms != certificate.get('remaining_basis_coefficients'):
        raise ValueError('incorrect rank-seven terminal space')
    witness = high[1]
    witness_rows = [0, 1, 7, 8, 14, 15, 22, 23]
    if [i for i, row in enumerate(witness) if any(row)] != witness_rows:
        raise ValueError('rank-eight witness support changed')
    # An explicit triangular minor certifies rank eight in every characteristic.
    pairs = certificate['rank_eight_witness_minor']
    if (len(pairs) != 8 or any(len(pair) != 2 for pair in pairs)
            or any(type(x) is not int or not 0 <= x < 28 for pair in pairs for x in pair)
            or sorted(r for r, c in pairs) != witness_rows
            or len({c for r, c in pairs}) != 8):
        raise ValueError('invalid rank-eight witness minor')
    minor = [[witness[r][c] for rr, c in pairs] for r, cc in pairs]
    if any(minor[i][j] for i in range(8) for j in range(i + 1, 8)):
        raise ValueError('rank-eight witness minor is not triangular')
    if any(minor[i][i] not in (-1, 1) for i in range(8)):
        raise ValueError('rank-eight witness minor has nonunit diagonal')
    basis = base.full_transformed_basis()
    image_rows = [0, 7, 14, 21, 22, 23]
    columns = [[0, 1, 2, 3, 7, 11], [0, 1, 3, 7, 11], [0, 3, 7, 11],
               [3, 7, 11], [3, 7], [3], []]
    controls = []
    for a in range(7):
        rows = [84 + i for i in (image_rows[-a:] if a else [])]
        cols = [28 + j for j in columns[a]]
        compressed = [{(r, c): x for (r, c), x in b.items()
                       if r not in rows and c not in cols} for b in basis]
        dimension = base.sparse_rank(compressed)
        if compressed[64] or dimension != (111 if a < 6 else 95):
            raise ValueError(f'sharp boundary control failed at output corank {a}')
        controls.append({'output_corank': a, 'input_corank': 6 - a,
                         'deleted_output_rows': rows, 'deleted_input_columns': cols,
                         'compressed_dimension_over_Q': dimension})
    return {'eight_minor_stages': 26, 'full_rank_at_most_seven_locus_dimension': 17,
            'rank_seven_absent': True, 'next_attained_rank': 8,
            'rank_locus_and_written_boundary_field_scope': 'every field',
            'compression_controls': controls, 'independent_review': False,
            'formalized': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    original = ROOT / 'results/resolvent-rank-six-locus-2026-10-23/certificate.json'
    report = verify(json.loads(args.certificate.read_text()), json.loads(original.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
