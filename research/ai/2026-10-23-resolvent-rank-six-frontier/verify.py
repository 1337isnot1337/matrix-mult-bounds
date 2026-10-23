"""Exact integer certificate replay; no discovery code is imported.

The polynomial product-dimension and compression arguments are written proofs.
This program checks their source normal form and finite sharpness controls.
"""

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULTS = ROOT / 'results/resolvent-rank-six-frontier-2026-10-23'


def zeros(n, m):
    return [[0] * m for _ in range(n)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    result = zeros(len(a), len(b[0]))
    sparse = [[(j, x) for j, x in enumerate(row) if x] for row in b]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in sparse[k]:
                    result[i][j] += x * y
    return result


def combine(basis, coefficients):
    return [[sum(c * b[i][j] for c, b in zip(coefficients, basis))
             for j in range(len(basis[0][0]))] for i in range(len(basis[0]))]


def inverse_integer(a):
    n = len(a)
    work = [[Fraction(x) for x in row + unit]
            for row, unit in zip(a, identity(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if work[i][j])
        work[j], work[pivot] = work[pivot], work[j]
        scale = work[j][j]
        work[j] = [x / scale for x in work[j]]
        for i in range(n):
            scale = work[i][j]
            if i != j and scale:
                work[i] = [x - scale * y for x, y in zip(work[i], work[j])]
    if any(x.denominator != 1 for row in work for x in row[n:]):
        raise ValueError('nonintegral source inverse')
    inverse = [[int(x) for x in row[n:]] for row in work]
    if multiply(a, inverse) != identity(n) or multiply(inverse, a) != identity(n):
        raise ValueError('incorrect two-sided inverse')
    return inverse


def source():
    rows = list(product(range(4), range(7)))
    columns = list(product(range(7), range(4)))
    raw = [[[int(H - j == i and L - r == s) for H, r in columns]
            for j, L in rows] for i, s in product(range(4), repeat=2)]
    unit = combine(raw, [int(i + s == 3) for i, s in product(range(4), repeat=2)])
    inverse = inverse_integer(unit)
    high = [multiply(raw[0], multiply(inverse, a)) for a in raw]
    labels = [['g', i, s] for i, s in product(range(4), repeat=2)]
    labels += [['f', i, s] for i, s in product(range(4), repeat=2) if (i, s) != (0, 3)]
    basis = raw + [a for i, a in enumerate(high) if i != 3]
    if combine(high, [int(i + s == 3) for i, s in product(range(4), repeat=2)]) != raw[0]:
        raise ValueError('incorrect gauge identity')
    return raw, unit, high, basis, labels


def normal_block(i):
    """Coefficient of x^i after the two fixed output row additions."""
    result = zeros(28, 28)
    for j in range(3):
        result[7 * j][4 * (i + j) + 3] = 1
        result[21 + j][4 * i + j] = 1
    return result


def shear(a):
    result = [row[:] for row in a]
    result[22] = [x + y for x, y in zip(a[22], a[14])]
    result[23] = [x + y for x, y in zip(a[23], a[7])]
    return result


def validate_certificate(certificate, basis, labels):
    if (certificate.get('size') != 7 or certificate.get('dimension') != 31
            or certificate.get('labels') != labels
            or certificate.get('remaining_dimension') != 5):
        raise ValueError('incorrect certificate format')
    if len(certificate.get('stages', [])) != 26:
        raise ValueError('exactly 26 stages are required')
    coordinates = identity(31)
    remaining_labels = labels[:]
    for number, stage in enumerate(certificate['stages']):
        form, pivot, minor = stage['form'], stage['pivot'], stage['minor']
        if (len(form) != len(basis) or any(type(x) is not int for x in form)
                or type(pivot) is not int or not 0 <= pivot < len(basis)
                or form[pivot] not in (-1, 1)):
            raise ValueError(f'nonunit elimination at stage {number}')
        if (len(minor) != 7 or any(len(pair) != 2 for pair in minor)
                or any(type(x) is not int or not 0 <= x < 28 for pair in minor for x in pair)
                or len({r for r, c in minor}) != 7 or len({c for r, c in minor}) != 7):
            raise ValueError(f'invalid minor at stage {number}')
        for k, (r, c) in enumerate(minor):
            diagonal = [a[r][c] for a in basis]
            factor = diagonal[pivot] // form[pivot]
            if factor not in (-1, 1) or diagonal != [factor * x for x in form]:
                raise ValueError(f'wrong diagonal at stage {number}')
            if any(a[r][later] for _, later in minor[k + 1:] for a in basis):
                raise ValueError(f'nontriangular minor at stage {number}')
        chosen = basis[pivot]
        old_coordinates = coordinates[pivot]
        coordinates = [[x - form[j] // form[pivot] * y
                        for x, y in zip(row, old_coordinates)]
                       for j, row in enumerate(coordinates) if j != pivot]
        basis = [combine([a, chosen], [1, -form[j] // form[pivot]])
                 for j, a in enumerate(basis) if j != pivot]
        remaining_labels.pop(pivot)
    expected_labels = [['f', i, 0] for i in range(4)] + [['f', 3, 1]]
    if remaining_labels != expected_labels or certificate.get('remaining_labels') != expected_labels:
        raise ValueError('incorrect remaining labels')
    expected_coordinates = []
    for i in range(4):
        expected_coordinates.append([int(label == ['f', i, 0]) for label in labels])
    expected_coordinates.append([
        -int(label == ['g', 1, 0])
        + int(label in [['f', 1, 3], ['f', 2, 2], ['f', 3, 1]]) for label in labels])
    if coordinates != expected_coordinates:
        raise ValueError('wrong original-coordinate elimination')
    for i, a in enumerate(basis):
        expected = normal_block(i)
        if i == 4:
            expected = [[-x for x in row] for row in expected]
        if shear(a) != expected:
            raise ValueError('incorrect polynomial normal form')
    return basis


def sparse_rank(vectors, prime=None):
    """Exact rank of sparse flattened matrices, over Q or a prime field."""
    pivots = {}
    for vector in vectors:
        row = {i: (x % prime if prime else Fraction(x)) for i, x in vector.items()}
        row = {i: x for i, x in row.items() if x}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                inverse = pow(row[pivot], -1, prime) if prime else 1 / row[pivot]
                pivots[pivot] = {i: (x * inverse % prime if prime else x * inverse)
                                 for i, x in row.items()}
                break
            scale = row[pivot]
            for i, x in pivots[pivot].items():
                value = row.get(i, 0) - scale * x
                if prime:
                    value %= prime
                if value:
                    row[i] = value
                else:
                    row.pop(i, None)
    return len(pivots)


def full_basis(raw, unit, high, mixed):
    """W after diag(K,K,K,RK), in middle-coordinate-first ordering."""
    def blocks(items):
        result = {}
        for br, bc, a in items:
            a = shear(a) if br == 3 else a
            for r, row in enumerate(a):
                for c, x in enumerate(row):
                    if x:
                        result[(28 * br + r) * 112 + 28 * bc + c] = x
        return result
    result = [blocks([(i, i, unit) for i in range(4)])]
    result += [blocks([(1, 0, a), (2, 1, a), (3, 2, a)]) for a in raw]
    result += [blocks([(2, 0, a), (3, 1, a)]) for a in raw]
    result += [blocks([(3, 0, a)]) for a in mixed]
    result += [blocks([(3, j, a)]) for j in range(1, 4) for a in high]
    return result


def compression_controls(basis):
    # P deletes these three output rows; C omits input columns 0,1,2.
    # One zero output row / input column pads each factor to size 110.
    aligned_rows = {84, 91, 98}
    unaligned_rows = {0, 1, 2}
    def compress(rows):
        return [{index: x for index, x in a.items()
                 if index // 112 not in rows and index % 112 not in {0, 1, 2}}
                for a in basis]
    reports = []
    for prime in [None, 2, 3, 1009]:
        ranks = [sparse_rank(vectors, prime) for vectors in
                 [basis, compress(aligned_rows), compress(unaligned_rows)]]
        if ranks != [112, 111, 112]:
            raise ValueError(f'compression control failed over {prime}: {ranks}')
        reports.append({'field': 'Q' if prime is None else f'F{prime}',
                        'source_dimension': ranks[0], 'aligned_dimension': ranks[1],
                        'unaligned_dimension': ranks[2]})
    return reports


def verify(certificate, check_sources=True):
    if check_sources:
        sources = json.loads((PACKAGE / 'sources.json').read_text())
        for record in sources['local_dependencies']:
            if hashlib.sha256((ROOT / record['path']).read_bytes()).hexdigest() != record['sha256']:
                raise ValueError('changed source pin: ' + record['path'])
    raw, unit, high, mixed, labels = source()
    validate_certificate(certificate, mixed, labels)
    for i in range(4):
        if shear(high[4 * i]) != normal_block(i):
            raise ValueError('pure Q normal form failed')
    basis = full_basis(raw, unit, high, mixed)
    return {
        'schema': 'resolvent-rank-six-locus-verification-v1',
        'integer_minor_identities': 26, 'minor_size': 7,
        'mixed_rank_at_most_six_dimension': 5,
        'pure_Q_rank_at_most_six_dimension': 4,
        'full_rank_at_most_six_dimension': 17,
        'normal_form_degree_bounds': [4, 3, 3, 3],
        'compression_controls': compression_controls(basis),
        'all_field_classification': 'written proof plus exact integer identities',
        'compression_dimension_bound': 'written polynomial product-dimension proof',
        'independent_review': False, 'improves_omega': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', nargs='?', type=Path, default=RESULTS / 'certificate.json')
    args = parser.parse_args()
    print(json.dumps(verify(json.loads(args.certificate.read_text())), indent=2))


if __name__ == '__main__':
    main()
