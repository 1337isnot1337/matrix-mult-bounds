"""Replay integer minor identities for the complete resolvent rank-six locus.

The discovery search and predecessor verifier are not runtime dependencies.
The determinant-pencil argument over algebraically closed fields is written
mathematics, not a machine-formalized consequence of this finite replay.
"""

import argparse
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def combine(basis, coefficients):
    return [[sum(c * b[i][j] for c, b in zip(coefficients, basis))
             for j in range(len(basis[0][0]))] for i in range(len(basis[0]))]


def multiply(a, b):
    out = [[0] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(b[k]):
                    out[i][j] += x * y
    return out


def integer_inverse(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row + unit]
         for row, unit in zip(matrix, identity(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        scale = a[j][j]
        a[j] = [x / scale for x in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                scale = a[i][j]
                a[i] = [x - scale * y for x, y in zip(a[i], a[j])]
    inverse = [row[n:] for row in a]
    if any(x.denominator != 1 for row in inverse for x in row):
        raise ValueError('source unit inverse is not integral')
    inverse = [[int(x) for x in row] for row in inverse]
    if multiply(matrix, inverse) != identity(n) or multiply(inverse, matrix) != identity(n):
        raise ValueError('two-sided integer inverse failed')
    return inverse


def source():
    rows = list(product(range(4), range(7)))
    columns = list(product(range(7), range(4)))
    labels = list(product(range(4), repeat=2))
    raw = [[[int(h - j == i and ell - r == s) for h, r in columns]
            for j, ell in rows] for i, s in labels]
    unit = combine(raw, [int(i + s == 3) for i, s in labels])
    inverse = integer_inverse(unit)
    high = [multiply(raw[0], multiply(inverse, b)) for b in raw]
    if combine(high, [int(i + s == 3) for i, s in labels]) != raw[0]:
        raise ValueError('mixed-block gauge relation failed')
    mixed = raw + [b for i, b in enumerate(high) if i != 3]
    names = [['g', i, s] for i, s in labels]
    names += [['f', i, s] for i, s in labels if (i, s) != (0, 3)]
    terminal = [high[4 * i] for i in range(4)]
    terminal.append(combine([raw[4], high[7], high[10], high[13]], [-1, 1, 1, 1]))
    return raw, unit, inverse, high, mixed, names, terminal


def eliminate(basis, stages, size):
    """Check polynomial triangular minors and unit substitutions over Z."""
    transforms = identity(len(basis))
    for number, stage in enumerate(stages):
        form, pivot, minor = stage['form'], stage['pivot'], stage['minor']
        if (len(form) != len(basis) or any(type(x) is not int for x in form)
                or type(pivot) is not int or not 0 <= pivot < len(basis)
                or form[pivot] not in (-1, 1)):
            raise ValueError(f'invalid unit substitution at stage {number}')
        if (len(minor) != size or any(len(pair) != 2 for pair in minor)
                or any(type(x) is not int or not 0 <= x < 28 for pair in minor for x in pair)
                or len({r for r, c in minor}) != size or len({c for r, c in minor}) != size):
            raise ValueError(f'invalid minor at stage {number}')
        for k, (r, c) in enumerate(minor):
            entries = [b[r][c] for b in basis]
            sign = entries[pivot] * form[pivot]
            if sign not in (-1, 1) or entries != [sign * x for x in form]:
                raise ValueError(f'incorrect diagonal at stage {number}')
            if any(b[r][cc] for rr, cc in minor[k + 1:] for b in basis):
                raise ValueError(f'nonzero upper triangle at stage {number}')
        chosen, change = basis[pivot], transforms[pivot]
        basis = [combine([b, chosen], [1, -form[j] * form[pivot]])
                 for j, b in enumerate(basis) if j != pivot]
        transforms = [[x - form[j] * form[pivot] * y for x, y in zip(t, change)]
                      for j, t in enumerate(transforms) if j != pivot]
    return basis, transforms


def validate_certificate(certificate):
    raw, unit, inverse, high, mixed, labels, expected = source()
    if (certificate.get('dimension') != 31 or certificate.get('size') != 7
            or certificate.get('remaining_dimension') != 5 or certificate.get('labels') != labels
            or len(certificate.get('stages', [])) != 26
            or len(certificate.get('terminal_six_minor_stages', [])) != 5):
        raise ValueError('incorrect certificate dimensions, labels, or stage counts')
    terminal, transforms = eliminate(mixed, certificate['stages'], 7)
    if terminal != expected or transforms != certificate.get('remaining_basis_coefficients'):
        raise ValueError('terminal space or recorded parameter transformation is incorrect')
    image_rows = [0, 7, 14, 21, 22, 23]
    if any(x for b in terminal for r, row in enumerate(b) if r not in image_rows for x in row):
        raise ValueError('terminal space leaves the six-row image')
    remainder, _ = eliminate(terminal, certificate['terminal_six_minor_stages'], 6)
    if remainder:
        raise ValueError('terminal six-minor certificate is incomplete')
    return {'seven_minor_stages': 26, 'six_minor_stages': 5,
            'mixed_dimension': 31, 'mixed_rank_at_most_six_dimension': 5,
            'transformed_common_image_rows': image_rows}


def sparse_rank(vectors):
    """Exact rational rank of sparse coefficient vectors, for a finite control."""
    pivots = {}
    for vector in vectors:
        row = {k: Fraction(v) for k, v in vector.items() if v}
        while row:
            pivot = min(row)
            scale = row[pivot]
            if pivot not in pivots:
                pivots[pivot] = {k: v / scale for k, v in row.items()}
                break
            for k, v in pivots[pivot].items():
                value = row.get(k, 0) - scale * v
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
    return len(pivots)


def full_transformed_basis():
    """Basis of (I_4 tensor K) W, with middle coordinate ordered first."""
    raw, unit, inverse, high, mixed, labels, terminal = source()

    def blocks(matrix, positions):
        return {(28 * u + i, 28 * v + j): x
                for u, v in positions for i, row in enumerate(matrix)
                for j, x in enumerate(row) if x}

    basis = [blocks(unit, [(i, i) for i in range(4)])]
    basis += [blocks(b, [(2, 0), (3, 1)]) for b in raw]
    basis += [blocks(b, [(1, 0), (2, 1), (3, 2)]) for b in raw]
    basis += [blocks(b, [(3, 0)]) for b in mixed]
    basis += [blocks(b, [(3, j)]) for j in (1, 2, 3) for b in high]
    return basis


def verify(certificate):
    report = validate_certificate(certificate)
    basis = full_transformed_basis()
    deleted_rows = [105, 106, 107]
    deleted_columns = [31, 35, 39]
    compressed = [{(r, c): x for (r, c), x in b.items()
                   if r not in deleted_rows and c not in deleted_columns} for b in basis]
    if len(basis) != 112 or sparse_rank(basis) != 112:
        raise ValueError('full source-space basis has the wrong dimension')
    if compressed[64] or sparse_rank(compressed) != 111:
        raise ValueError('explicit rank109/rank109 compression is not sharp')
    return {**report, 'full_limit_space_dimension': 112,
            'full_rank_at_most_six_dimension': 17,
            'explicit_compression': {'field_checked': 'Q', 'left_rank': 109,
                'right_rank': 109, 'deleted_transformed_output_rows': deleted_rows,
                'deleted_input_columns': deleted_columns, 'image_dimension': 111,
                'kernel_witness_basis_index': 64},
            'rank_locus_field_scope': 'every field; integer minor identities',
            'written_compression_bound': 'kernel dimension at most one over algebraically closed fields',
            'independent_review': False, 'formalized': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
