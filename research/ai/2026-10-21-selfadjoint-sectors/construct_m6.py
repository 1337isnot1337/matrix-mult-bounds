#!/usr/bin/env python3
"""Exact finite m6 moment-core experiment; no exponent improvement claimed.

This adapts the self-adjoint m5 construction of the literature lane to a
prescribed moment core.  It is a constructive search, not a theorem until
all coefficient assertions return successfully.
"""
import argparse
import json
import random
from functools import reduce
from math import gcd
from pathlib import Path

import sympy as s

t = s.symbols('t')


def primitive(v):
    den = s.ilcm(*[x.q for x in v])
    ints = [int(x*den) for x in v]
    divisor = reduce(gcd, ints, 0)
    return s.Matrix([x//divisor for x in ints])


def solve_columns(matrix, target):
    pivots = matrix.rref()[1]
    chosen = matrix[:, pivots]
    coefficients = chosen.gauss_jordan_solve(target)[0]
    result = s.zeros(matrix.cols, target.cols)
    for i, p in enumerate(pivots):
        result[p, :] = coefficients[i, :]
    assert matrix*result == target
    return result


def attempt(seed, trials=12):
    rng = random.Random(seed)
    m, B, N, H, R = 6, 28, 21, 22, 34
    exponents = [0, 1, 3, 4, 5, 6]
    shared = s.Matrix([[int(i == d) for i in range(7)] for d in exponents])
    low_factors = s.Matrix([[rng.choice([-1, 0, 1]) for _ in range(6)]
                           for _ in range(3)])
    if low_factors.rank() != 3 or low_factors[0, 5] == 0:
        return None, 'low factors'
    moments = [s.S.Zero]*(2*B+m-1)
    for j in range(11, 22):
        moments[j] = s.Integer(rng.choice([-1, 0, 1]))
    moments[43] = s.S.One
    forms = [s.Matrix([[moments[j+k+d] for k in range(B)]
                       for j in range(B)]) for d in exponents]
    low = s.zeros(3, B)
    low[:, H:H+6] = low_factors
    product_low = s.Matrix.vstack(*[low*form for form in forms])
    if product_low.rank() != 12:
        return None, ('low product rank', product_low.rank())
    lower = s.Matrix([[int(j == i) for j in range(B)] for i in range(3)])
    upper = s.Matrix([[int(j == 6+i) for j in range(B)] for i in range(4)])
    core = lower.col_join(upper)
    assert product_low*core.T == s.zeros(18, 7)
    assert all(lower*form*lower.T == s.zeros(3, 3) for form in forms)
    central = [lower*form*upper.T for form in forms]
    central_shared = s.Matrix([[block[0, 0], block[0, 1], block[0, 2],
                               block[0, 3], block[1, 3], block[2, 3]]
                              for block in central])
    if central_shared.det() == 0:
        return None, 'central shared rank'
    assert all(block[i, j] == central_shared[x, i+j]
               for x, block in enumerate(central)
               for i in range(3) for j in range(4))
    first_product = s.Matrix.vstack(*[low[0, :]*form for form in forms])
    if first_product.rank() != 6:
        return None, 'first product rank'
    # Quotient of the first annihilator by the full three-row annihilator.
    span = s.Matrix.vstack(*[primitive(v).T for v in product_low.nullspace()])
    assert span.rows == B-12
    representatives = []
    for v in first_product.nullspace():
        row = primitive(v).T
        if span.col_join(row).rank() > span.rows:
            span = span.col_join(row)
            representatives.append(list(row))
    assert len(representatives) == 6
    representatives = s.Matrix(representatives)
    accepted = None
    for _ in range(trials):
        mixing = s.Matrix([[rng.choice([-1, 0, 1]) for _ in range(6)]
                           for _ in range(5)])
        high = mixing*representatives
        pencil0 = s.Matrix.hstack(*[high*form*low[1, :].T for form in forms])
        pencil1 = s.Matrix.hstack(*[high*form*low[2, :].T for form in forms])
        pencil = pencil1-t*pencil0
        kernel = [s.expand((-1)**i*pencil[:, [j for j in range(6) if j != i]].det())
                  for i in range(6)]
        if all(v == 0 for v in kernel):
            continue
        divisor = s.gcd_list(kernel)
        kernel = [s.cancel(v/divisor) for v in kernel]
        if max(s.degree(v, t) for v in kernel if v) != 5:
            continue
        change = s.Matrix([[s.expand(v).coeff(t, j) for j in range(6)]
                           for v in kernel])
        if change.det() == 0:
            continue
        change = s.Matrix(6, 6, list(primitive(list(change))))
        left = pencil0*change[:, :5]
        if left.det() == 0:
            continue
        assert pencil0*change == left.row_join(s.zeros(5, 1))
        assert pencil1*change == s.zeros(5, 1).row_join(left)
        accepted = left.inv()*high, change.inv().T
        break
    if accepted is None:
        return None, 'outer pencil'
    high, pair_shared = accepted
    top = solve_columns(first_product, s.eye(6)).T
    y = low.col_join(lower).col_join(upper).col_join(high).col_join(top)
    if y.rank() != N:
        return None, 'full Y rank'
    z = s.Matrix([[sum(y[row, j]*moments[j+k] for j in range(B))
                   for k in range(R)] for row in range(N)])
    if z.rank() != N:
        return None, 'full Z rank'
    blocks = [s.eye(6), pair_shared, central_shared, central_shared,
              pair_shared, s.eye(6)]
    labels = [(a, p-a) for p in range(m) for a in range(p+1)]
    count = 0
    for x, form in enumerate(forms):
        tensor_slice = y*form*y.T
        for j, (a, b) in enumerate(labels):
            for k, (c, d) in enumerate(labels):
                exponent = a+b+c+d-(m-1)
                if exponent <= 0:
                    expected = blocks[a+b][x, a+c] if exponent == 0 else 0
                    assert tensor_slice[j, k] == expected, (
                        seed, x, j, k, tensor_slice[j, k], expected)
                    count += 1
    return dict(status='exact rational independent-sector finite degeneration',
                source=[7, B], target_m=m, seed=seed,
                a_map=[[str(v) for v in shared.row(i)] for i in range(m)],
                y=[[str(v) for v in y.row(i)] for i in range(N)],
                z=[[str(v) for v in z.row(i)] for i in range(N)],
                shared_sector_maps=[[[str(v) for v in block.row(i)]
                                      for i in range(m)] for block in blocks],
                y_weights=[sum(v) for v in labels],
                z_weights=[sum(v)-(m-1) for v in labels],
                moment_sequence=[str(v) for v in moments],
                low_factors=[[str(v) for v in low_factors.row(i)] for i in range(3)],
                nonpositive_coefficients_checked=count,
                shared_sector_determinants=[str(block.det()) for block in blocks],
                new_exponent_established=False), None


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=7)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result,error=attempt(args.seed)
    if result is None:
        raise RuntimeError(f'Seed {args.seed} rejected: {error}')
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in
                     ['a_map','y','z','shared_sector_maps','moment_sequence','low_factors']}))
