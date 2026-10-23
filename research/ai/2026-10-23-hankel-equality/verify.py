"""Exact finite controls for deficient-symbol saturation; not a proof search."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

X, Z = sp.symbols('x z')


def exact_rank(rows, variables=()):
    domain = sp.QQ.frac_field(*variables) if variables else sp.QQ
    return DomainMatrix.from_Matrix(sp.Matrix(rows)).convert_to(domain).rank()


def coefficients(sequence, a, b):
    if len(sequence) != a+b-1:
        raise ValueError('Wrong long-coordinate length')
    result = {}
    for k, value in enumerate(sequence):
        for (i, s), c in sp.Poly(value, X, Z).terms():
            if i >= a or s >= b:
                raise ValueError('Coefficient outside the declared source')
            if c:
                result[i, k, s] = c
    return result


def full_slice_rank(coeff, a, b):
    """Build the literal source matrix, independently of archived helpers."""
    m = a+b-1
    n = a*b*m
    rows = {}
    for (i, k, s), value in coeff.items():
        for p in range(a):
            q = k-p
            if not 0 <= q < b:
                continue
            for j in range(b):
                for r in range(a):
                    row = (j*a+p)*m+s+r
                    column = ((i+j)*b+q)*a+r
                    rows.setdefault(row, {})[column] = value
    return DomainMatrix.from_dict_sympy(n, n, rows).convert_to(sp.QQ).rank()


def annihilator_system(coeff, a, b, r):
    """All coefficient recurrences, including homogeneous endpoint forms."""
    m = a+b-1
    rows = [[coeff.get((i, k+j, s), 0) for j in range(r+1)]
            for i in range(a) for s in range(b) for k in range(m-r)]
    return sp.Matrix(rows)


def control(name, sequence, a, b, expected_r, expected_full=None):
    coeff = coefficients(sequence, a, b)
    symbol = [[sequence[p+q] for q in range(b)] for p in range(a)]
    r = exact_rank(symbol, (X, Z))
    full = full_slice_rank(coeff, a, b)
    if r != expected_r or (expected_full is not None and full != expected_full):
        raise ArithmeticError('Unexpected exact control rank')
    if full < a*b*r:
        raise ArithmeticError('Polynomial slice lower bound failed')
    recurrence = annihilator_system(coeff, a, b, r)
    basis = recurrence.nullspace()
    q = None
    if len(basis) == 1:
        vector = list(basis[0])
        pivot = next(c for c in vector if c)
        q = [str(sp.cancel(c/pivot)) for c in vector]
    return {'name': name, 'a': a, 'b': b,
            'sequence': [str(sp.expand(f)) for f in sequence],
            'symbol_rank': r, 'full_slice_rank': full,
            'saturated': full == a*b*r,
            'deficient_symbol': r < min(a, b),
            'common_annihilator_nullity': len(basis),
            'normalized_common_annihilator': q}


def report():
    saturated = []
    # Origin jets and infinity jets protect the homogeneous endpoint cases,
    # at every rank through the actual A9 equality rank.
    for r in range(1, 9):
        a = b = r+1
        m = a+b-1
        for label, k in [('origin', r-1), ('infinity', m-r)]:
            f = [0]*m
            f[k] = X**(a-1)*Z**(b-1)
            saturated.append(control(f'{label}-rank-{r}', f, a, b, r, a*b*r))
    # A reduced scheme with independently varying short factors.
    a, b, r = 4, 5, 3
    f = [sum((1+t*X)*(1+(t+1)*Z)*t**k for t in (1, 2, 3))
         for k in range(a+b-1)]
    saturated.append(control('three-reduced-points', f, a, b, r, a*b*r))
    # A nonreduced scheme with both a moving weight and a derivative term.
    a = b = 4
    f = [(1+X)*(1+Z)*(2**k+k*2**(k-1) if k else 1)
         for k in range(2*a-1)]
    saturated.append(control('double-point-away-from-origin', f, a, b, 2, 32))
    near_equality = []
    for a in (3, 4, 5):
        f = [X*Z, 1]+[0]*(2*a-3)
        near_equality.append(control(f'fixed-double-point-excess-one-a{a}', f, a, a, 2, 2*a*a+1))
    nonsaturated = []
    for r in range(2, 9):
        a = b = r+1
        f = [X**(k//r) if k % r == 0 else 0 for k in range(2*a-1)]
        nonsaturated.append(control(f'variable-recurrence-rank-{r}', f, a, b, r))
    boundary = control('credited-PR76-full-rank-warning', [0, X, 0, 1], 2, 3, 2, 12)
    for row in saturated:
        if not row['saturated'] or not row['deficient_symbol'] or row['common_annihilator_nullity'] != 1:
            raise ArithmeticError('Saturated control has no unique constant annihilator')
    for row in nonsaturated:
        if (row['full_slice_rank'] != row['a']*row['b']*row['symbol_rank']+row['a']
                or row['common_annihilator_nullity'] != 0):
            raise ArithmeticError('Variable recurrence failed to protect saturation')
    for row in near_equality:
        if row['common_annihilator_nullity'] != 1:
            raise ArithmeticError('Near-equality strip control has no constant scheme')
    if boundary['common_annihilator_nullity'] != 0:
        raise ArithmeticError('Full-symbol boundary warning failed')
    return {'saturated_controls': saturated, 'near_equality_controls': near_equality,
            'nonsaturated_controls': nonsaturated,
            'full_symbol_boundary': boundary,
            'scope': 'Exact finite controls; the all-rank theorem rests on the written proof.',
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end='')
