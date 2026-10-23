"""Exact finite acceptance for the elementary biform proof; no discovery import."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULTS = ROOT / 'results/elementary-biform-gap-2026-10-23'
BASE = '3008d704d1797da02f7bf3f29cc1dbd4c0e7fa93'
SOURCE_PATHS = (
    'research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md',
    'research/ai/2026-10-20-koszul/cyclic_finite_target.md',
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / 'sources.json').read_text())
    require(record['base_commit'] == BASE, 'Changed source baseline')
    require(record['field'] == 'characteristic zero'
            and record['imported_structural_theorems'] == []
            and record['independent_review'] is False
            and record['improves_omega'] is False, 'Changed scope')
    entries = record['source_references']
    require(len(entries) == 2 and {e['path'] for e in entries} == set(SOURCE_PATHS),
            'Changed local source inventory')
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest()
        require(actual == entry['sha256'], 'Changed local source bytes')
    external = record['external_references']
    require(len(external) == 1 and external[0]['doi'] == '10.1016/0001-8708(85)90121-5'
            and external[0]['sha256'] ==
            '42d26f70bf29bbd43d04e6f962f43bdbe5db1a4f59cb1075a7ccdbc32f7f25bf', 'Changed classical attribution pin')
    return len(entries)


def literal_matrix(a, b, coefficients):
    require(type(a) is int and type(b) is int and 2 <= a <= b, 'Invalid source size')
    require(all(type(i) is int and type(s) is int and 0 <= i < a and 0 <= s < b
                for i, s in coefficients), 'Coefficient outside the source')
    width = a+b-1
    return [[coefficients.get((h-j, ell-r), 0)
             for h in range(width) for r in range(a)]
            for j in range(b) for ell in range(width)]


def power_coefficients(e, alpha=1, beta=1):
    require(type(e) is int and e >= 1 and alpha != 0 and beta != 0, 'Invalid mixed power')
    return {(i, e-i): comb(e, i)*alpha**i*beta**(e-i) for i in range(e+1)}


def determinant(matrix):
    """Fraction-free integer Bareiss determinant, with exact division checked."""
    n = len(matrix)
    require(all(len(row) == n for row in matrix), 'Nonsquare minor')
    work = [list(row) for row in matrix]
    previous, sign = 1, 1
    for col in range(n-1):
        pivot = next((i for i in range(col, n) if work[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign = -sign
        value = work[col][col]
        for i in range(col+1, n):
            for j in range(col+1, n):
                numerator = value*work[i][j]-work[i][col]*work[col][j]
                require(numerator % previous == 0, 'Inexact Bareiss division')
                work[i][j] = numerator // previous
            work[i][col] = 0
        previous = value
    return sign*work[-1][-1] if n else 1


def power_case(a, b, e):
    require(2 <= a <= b and 1 <= e < a, 'Power outside the proved range')
    width = a+b-1
    blocks = []
    for d in range(1-a, b+e):
        r0, r1, j0 = max(0, -d), min(a-1, b+e-1-d), max(0, d-e)
        count = r1-r0+1
        rows = [(j0+u)*width+(j0+u+e-d) for u in range(count)]
        columns = [(d+r0+v)*a+r0+v for v in range(count)]
        k = d+r0-j0
        minor = [[comb(e, k+v-u) if 0 <= k+v-u <= e else 0
                  for v in range(count)] for u in range(count)]
        blocks.append({'d': d, 'rows': rows, 'columns': columns,
                       'determinant': determinant(minor)})
    return {'a': a, 'b': b, 'e': e, 'rank': a*(b+e), 'blocks': blocks}


def case_formats():
    return [(a, b, e) for a in range(2, 7) for b in range(a, a+3) for e in range(1, a)]


def make_certificate():
    return {'schema': 1, 'base_commit': BASE, 'field': 'characteristic zero',
            'cases': [power_case(*case) for case in case_formats()]}


def check_certificate(certificate):
    require(certificate['schema'] == 1 and certificate['base_commit'] == BASE
            and certificate['field'] == 'characteristic zero', 'Changed certificate scope')
    cases = certificate['cases']
    require([(c['a'], c['b'], c['e']) for c in cases] == case_formats(),
            'Incomplete or reordered power inventory')
    block_count = 0
    largest_determinant = 0
    for case in cases:
        a, b, e = case['a'], case['b'], case['e']
        require(case == power_case(a, b, e), 'Changed minor indices or determinants')
        matrix = literal_matrix(a, b, power_coefficients(e))
        width = a+b-1
        rows, columns = [], []
        for block in case['blocks']:
            rr, cc = block['rows'], block['columns']
            require(len(rr) == len(cc) and all(0 <= r < b*width for r in rr)
                    and all(0 <= c < a*width for c in cc), 'Unavailable minor indices')
            minor = [[matrix[r][c] for c in cc] for r in rr]
            require(determinant(minor) == block['determinant'] > 0,
                    'Literal minor is not positive')
            require(all((r//width-r % width)+e == block['d'] for r in rr)
                    and all(c//a-c % a == block['d'] for c in cc),
                    'Minor blocks have incompatible weights')
            rows.extend(rr)
            columns.extend(cc)
            block_count += 1
            largest_determinant = max(largest_determinant, block['determinant'])
        require(len(rows) == len(set(rows)) == case['rank'], 'Duplicated lower rows')
        require(len(columns) == len(set(columns)) == case['rank'], 'Duplicated lower columns')
        require(set(columns) == set(range(a*(b+e))), 'Incomplete active-column cover')
        require(all(value == 0 for row in matrix for value in row[a*(b+e):]),
                'Entry outside the upper cover')
        # Literal support equation prevents off-diagonal interactions among blocks.
        require(all(value == 0 or (r//width-r % width)+e == c//a-c % a
                    for r, row in enumerate(matrix) for c, value in enumerate(row)),
                'Nonzero entry couples different minor blocks')
    return {'power_cases': len(cases), 'positive_integer_minors': block_count,
            'largest_block_determinant': largest_determinant,
            'active_column_upper_covers': len(cases)}


def translation(n, value):
    return [[comb(k, i)*value**(k-i) if i <= k else 0 for k in range(n)] for i in range(n)]


def multiply(left, right):
    cols = list(zip(*right))
    return [[sum(x*y for x, y in zip(row, col)) for col in cols] for row in left]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def tensor(left, right):
    return [[x*y for x in row_a for y in row_b] for row_a in left for row_b in right]


def shift_coefficients(coefficients, c, d):
    result = {}
    for (i, s), value in coefficients.items():
        for u in range(i+1):
            for v in range(s+1):
                key = (u, v)
                result[key] = result.get(key, 0)+value*comb(i, u)*c**(i-u)*comb(s, v)*d**(s-v)
    return {key: value for key, value in result.items() if value}


def check_covariance():
    count = 0
    for a, b in [(2, 2), (2, 3), (3, 3), (3, 4)]:
        coefficients = {(i, s): (-1)**(i+s)*(1+2*i+3*s) for i in range(a) for s in range(b)}
        width = a+b-1
        matrix = literal_matrix(a, b, coefficients)
        for c, d in [(1, -2), (-2, 1), (0, 2)]:
            left = tensor(transpose(translation(b, -c)), translation(width, d))
            right = tensor(transpose(translation(width, c)), translation(a, -d))
            actual = literal_matrix(a, b, shift_coefficients(coefficients, c, d))
            require(multiply(multiply(left, matrix), right) == actual,
                    'Crossed affine covariance failed')
            count += 1
        for t in [Fraction(2), Fraction(-3, 2)]:
            actual = literal_matrix(a, b, {key: value*t**sum(key) for key, value in coefficients.items()})
            expected = [[t**(ell-j+h-r)*matrix[j*width+ell][h*a+r]
                         for h in range(width) for r in range(a)]
                        for j in range(b) for ell in range(width)]
            require(actual == expected, 'Crossed scaling covariance failed')
            count += 1
    return count


def verify(certificate=None):
    sources = check_sources()
    if certificate is None:
        certificate = json.loads((RESULTS / 'certificate.json').read_text())
    return {'source_pins': sources, **check_certificate(certificate),
            'affine_and_scaling_controls': check_covariance(),
            'status': 'finite exact controls for a written unreviewed all-size proof',
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--export-certificate', action='store_true')
    parser.add_argument('--write-report', action='store_true')
    args = parser.parse_args()
    if args.export_certificate:
        (RESULTS / 'certificate.json').write_text(json.dumps(make_certificate(), indent=2)+'\n')
    report = verify()
    if args.write_report:
        (RESULTS / 'verification.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
