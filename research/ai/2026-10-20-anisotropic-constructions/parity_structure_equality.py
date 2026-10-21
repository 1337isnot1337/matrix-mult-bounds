"""Exact controls for the two-variable slice-rank equality argument.

The proof is in parity_structure_equality.md.  These finite examples check
indexing, the two intermediate ranks, and constant-shear normalization.
They establish no restriction or improved exponent.
"""

from __future__ import annotations

import argparse
from itertools import product
import json
from math import comb
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

from slice_rank_gap import full_matrix


X, Z = sp.symbols('x z')


def rational_rank(matrix, variables=()):
    domain = sp.QQ.frac_field(*variables) if variables else sp.QQ
    return DomainMatrix.from_list_sympy(
        len(matrix), len(matrix[0]), matrix).convert_to(domain).rank()


def coefficient_vector(sequence, a, b):
    m = a+b-1
    assert len(sequence) == m
    result = [0]*(a*b*m)
    for k, polynomial in enumerate(sequence):
        for (i, s), coefficient in sp.Poly(polynomial, X, Z).terms():
            assert i < a and s < b and coefficient.q == 1
            result[(i*m+k)*b+s] = int(coefficient)
    return result


def intermediate_matrices(f, a, b):
    m = a+b-1

    def entry(i, k, s):
        return f[(i*m+k)*b+s] if 0 <= i < a and 0 <= s < b else 0

    # K is the transpose of the inner z coefficient map over Q(x).
    k_matrix = [[sum(entry(i, p+q, long_index-r)*X**i
                     for i in range(a))
                 for p, long_index in product(range(a), range(m))]
                for q, r in product(range(b), range(a))]
    # J is the transpose of the inner x coefficient map over Q(z).
    j_matrix = [[sum(entry(long_index-j, p+q, s)*Z**s
                     for s in range(b))
                 for long_index, q in product(range(m), range(b))]
                for j, p in product(range(b), range(a))]
    return k_matrix, j_matrix


def shear(sequence, value):
    d = len(sequence)-1
    return [sp.expand(sum(comb(d-k, j-k)*value**(j-k)*sequence[j]
                          for j in range(k, d+1)))
            for k in range(d+1)]


def shear_matrix(n, value):
    return sp.Matrix([[comb(n-1-p, j-p)*value**(j-p) if j >= p else 0
                       for j in range(n)] for p in range(n)])


def recurrence(sequence):
    leading = sp.Matrix([[sequence[0], sequence[1]],
                         [sequence[1], sequence[2]]])
    assert sp.expand(leading.det()) != 0
    coefficients = [sp.cancel(value) for value in
                    leading.inv()*sp.Matrix(sequence[2:4])]
    assert all(sp.expand(sequence[k+2]-coefficients[0]*sequence[k]
                         -coefficients[1]*sequence[k+1]) == 0
               for k in range(len(sequence)-2))
    return coefficients


def example_report(name, sequence, a, b, expected_full, shear_value=None):
    f = coefficient_vector(sequence, a, b)
    symbol = [[sequence[p+q] for q in range(b)] for p in range(a)]
    full_rank = rational_rank(full_matrix(f, a, b))
    symbol_rank = rational_rank(symbol, (X, Z))
    k_matrix, j_matrix = intermediate_matrices(f, a, b)
    rho = rational_rank(k_matrix, (X,))
    sigma = rational_rank(j_matrix, (Z,))
    assert full_rank == expected_full
    assert symbol_rank == 2
    assert full_rank >= b*rho >= a*b*symbol_rank
    assert full_rank >= a*sigma >= a*b*symbol_rank
    report = {'name': name, 'source_lengths': [a, b],
              'sequence': [str(sp.expand(value)) for value in sequence],
              'full_rational_slice_rank': full_rank,
              'rational_function_hankel_rank': symbol_rank,
              'inner_z_rank_over_Qx': rho, 'inner_x_rank_over_Qz': sigma,
              'rank_bound_forward': [full_rank, b*rho, a*b*symbol_rank],
              'rank_bound_reverse': [full_rank, a*sigma, a*b*symbol_rank],
              'both_inner_equalities': rho == 2*a and sigma == 2*b}
    checked = sequence
    if shear_value is not None:
        checked = shear(sequence, shear_value)
        expected = shear_matrix(a, shear_value)*sp.Matrix(symbol)*shear_matrix(b, shear_value).T
        actual = sp.Matrix([[checked[p+q] for q in range(b)] for p in range(a)])
        assert all(sp.expand(value) == 0 for value in actual-expected)
        checked_f = coefficient_vector(checked, a, b)
        transformed_rank = rational_rank(full_matrix(checked_f, a, b))
        assert transformed_rank == full_rank
        report.update({'constant_shear': shear_value,
                       'hankel_shear_identity_exact': True,
                       'full_rank_after_shear': transformed_rank})
    coefficients = recurrence(checked)
    report['recurrence_coefficients_c0_c1'] = [str(value) for value in coefficients]
    report['recurrence_is_constant'] = all(not value.free_symbols for value in coefficients)
    if full_rank == 2*a*b:
        assert report['both_inner_equalities'] and report['recurrence_is_constant']
    return report


def report():
    a, b = 5, 6
    d = a+b-2
    g0 = (1+X)*(1+Z)
    g1 = (1+2*X**2)*(1-Z**3)
    tangent_g = (1+X**2)*(1+Z**3)
    records = [
        example_report('distinct finite points',
                       [g0+g1*2**k for k in range(d+1)], a, b, 60),
        example_report('tangent at two',
                       [0]+[tangent_g*k*2**(k-1) for k in range(1, d+1)],
                       a, b, 60),
        example_report('both endpoints before normalization',
                       [g0]+[0]*(d-1)+[g1], a, b, 60, shear_value=1),
        example_report('variable x recurrence',
                       [X**(k//2) if k % 2 == 0 else 0 for k in range(d+1)],
                       a, b, 75),
        example_report('variable z recurrence',
                       [Z**(k//2) if k % 2 == 0 else 0 for k in range(d+1)],
                       a, b, 84),
    ]
    assert records[3]['recurrence_coefficients_c0_c1'] == ['x', '0']
    assert records[4]['recurrence_coefficients_c0_c1'] == ['z', '0']
    assert not records[3]['both_inner_equalities']
    assert not records[4]['both_inner_equalities']
    return {'scope': 'exact finite controls for the written equality proof',
            'examples': records, 'number_of_examples': len(records),
            'all_arithmetic_exact': True, 'new_exponent_established': False,
            'target_restriction_constructed': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = report()
    payload = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.write_text(payload)
    else:
        print(payload, end='')
