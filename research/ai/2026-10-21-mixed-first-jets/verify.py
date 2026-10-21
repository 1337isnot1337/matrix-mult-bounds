"""Verify the complete sixteen-parameter mixed two-jet family over Q."""
import argparse
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
DEFAULT = ROOT / 'results/mixed-first-jets-2026-10-21/twojet-family.json'


def index(i, j, z):
    return (4*i+j)*7+z


A0 = [index(i, j, z) for i, j, z in product((1, 2), (1, 2), (0, 3, 6))]
KERNEL = set(range(112))-set(A0)
TERMS = [(index(i, s, 6-p-q), index(p, j, 6-r-s), index(r, q, 6-i-j))
         for i, j, p, q, r, s in product(range(4), repeat=6)]


def rows(encoded):
    return [{j: Fraction(num, den) for j, num, den in row} for row in encoded]


def pad_top(encoded, count):
    return rows(encoded)+[{} for _ in range(count-4)]


def add(*terms):
    result = defaultdict(Fraction)
    for scalar, tensor in terms:
        for key, value in tensor.items():
            result[key] += scalar*value
    return {key: value for key, value in result.items() if value}


def contract(left, right):
    by_left, by_right = defaultdict(list), defaultdict(list)
    for i, row in enumerate(left):
        for j, value in row.items():
            by_left[j].append((i, value))
    for i, row in enumerate(right):
        for j, value in row.items():
            by_right[j].append((i, value))
    result = defaultdict(Fraction)
    for a, b, c in TERMS:
        for j, x in by_left[b]:
            for k, y in by_right[c]:
                result[a, j, k] += x*y
    return {key: value for key, value in result.items() if value}


def correct(encoded, tensor):
    by_column = defaultdict(list)
    for i, j, numerator, denominator in encoded:
        if i not in KERNEL or j not in A0:
            raise ArithmeticError('Source row correction is outside the specified block')
        by_column[j].append((i, Fraction(numerator, denominator)))
    result = defaultdict(Fraction)
    for (a, b, c), value in tensor.items():
        for i, scale in by_column[a]:
            result[i, b, c] += scale*value
    return {key: value for key, value in result.items() if value}


def check_kernel(label, tensor):
    bad = [(key, value) for key, value in tensor.items() if key[0] in KERNEL and value]
    if bad:
        raise ArithmeticError(f'{label}: nonzero corrected coefficient {bad[0]}')


def covector_rank(covectors):
    matrix = sp.Matrix(len(covectors), 112, lambda i, j: covectors[i].get(j, 0))
    return len(matrix.to_DM().rref()[1])


def verify(certificate):
    if certificate['parameter_count'] != 16 or certificate['active_output_dimensions'] != [18, 10]:
        raise ArithmeticError('Unexpected family format')
    g = rows(certificate['leading_rows'])
    expected = [{index(0, 3, z): Fraction(1), index(3, 0, z): Fraction(-1)} for z in (1, 2, 4, 5)]
    if g != expected:
        raise ArithmeticError('Leading rows do not equal the canonical flag')
    p0, q0 = g+[{} for _ in range(14)], g+[{} for _ in range(6)]
    p_const = [{} for _ in range(4)]+rows(certificate['first_constant_B_new'])
    q_const = [{} for _ in range(4)]+rows(certificate['first_constant_C_new'])
    if len(p_const) != 18 or len(q_const) != 10:
        raise ArithmeticError('Wrong number of first new rows')
    if (covector_rank(g+p_const[4:]), covector_rank(g+q_const[4:])) != (18, 10):
        raise ArithmeticError('First quotient dimensions are not fourteen and six')
    zero = contract(p0, q0)
    first_constant = add((1, contract(p_const, q0)), (1, contract(p0, q_const)))
    second_constant = contract(p_const, q_const)
    check_kernel('leading coefficient', zero)
    check_kernel('constant first coefficient', first_constant)
    check_kernel('constant second coefficient', second_constant)
    ps, qs, firsts = [], [], []
    for i, encoded in enumerate(certificate['first_top_directions']):
        if len(encoded) != 8:
            raise ArithmeticError('A top direction must have eight rows')
        p, q = pad_top(encoded[:4], 18), pad_top(encoded[4:], 10)
        ps.append(p)
        qs.append(q)
        first = add((1, contract(p, q0)), (1, contract(p0, q)))
        firsts.append(first)
        correction = certificate['first_row_corrections'][i]
        check_kernel(f'first parameter {i}', add((1, first), (-1, correct(correction, zero))))
        p2 = [{} for _ in range(4)]+rows(certificate['second_linear_B_new'][i])
        q2 = [{} for _ in range(4)]+rows(certificate['second_linear_C_new'][i])
        second = add((1, contract(p2, q0)), (1, contract(p0, q2)),
                     (1, contract(p, q_const)), (1, contract(p_const, q)))
        check_kernel(f'second linear parameter {i}',
                     add((1, second), (-1, correct(correction, first_constant))))
    if len(ps) != 16:
        raise ArithmeticError('Missing parameter directions')
    direction_matrix = sp.Matrix(896, 16, lambda r, c:
                                 (ps[c] if r < 448 else qs[c])[(r//112) % 4].get(r % 112, 0))
    if len(direction_matrix.to_DM().rref()[1]) != 16:
        raise ArithmeticError('The parameter directions are dependent')
    monomials = list(combinations_with_replacement(range(16), 2))
    if [record['monomial'] for record in certificate['second_quadratic']] != [list(m) for m in monomials]:
        raise ArithmeticError('Incomplete quadratic monomial coverage')
    for record in certificate['second_quadratic']:
        i, j = record['monomial']
        p2, q2 = pad_top(record['B_top'], 18), pad_top(record['C_top'], 10)
        pieces = [(1, contract(p2, q0)), (1, contract(p0, q2)),
                  (1, contract(ps[i], qs[j])),
                  (-1, correct(certificate['first_row_corrections'][i], firsts[j])),
                  (-1, correct(record['first_row_correction'], zero))]
        if i != j:
            pieces.extend(((1, contract(ps[j], qs[i])),
                           (-1, correct(certificate['first_row_corrections'][j], firsts[i]))))
        check_kernel(f'second quadratic monomial {i},{j}', add(*pieces))
    return {'field': 'Q', 'parameters': 16, 'source_terms': 4096,
            'active_output_dimensions': [18, 10], 'first_quotient_ranks': [14, 6],
            'independent_leading_row_directions': 16,
            'quadratic_parameter_monomials': len(monomials),
            'complete_kernel_coefficient_identities': 171,
            'coefficient_cells_in_checked_universe': 171*100*18*10,
            'formal_order_verified': 2,
            'scope': 'Exact jets and regular first-row corrections through order two; no higher-order lift or matrix target.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=DEFAULT)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(verify(json.loads(args.certificate.read_text())), indent=2)+'\n')
