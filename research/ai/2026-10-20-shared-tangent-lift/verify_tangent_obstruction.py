"""Exact finite checks for the first and second order shared-map obstruction."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def multiply(left, right):
    out = [0]*(len(left)+len(right)-1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i+j] += a*b
    return out


def root_polynomial(nodes):
    out = [1]
    for node in nodes:
        out = multiply(out, [-node, 1])
    return out


def evaluate(poly, node):
    value = 0
    for coefficient in reversed(poly):
        value = value*node+coefficient
    return value


def rank_rational(matrix):
    work = [[Fraction(v) for v in row] for row in matrix]
    if not work:
        return 0
    row = 0
    for column in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        leading = work[row][column]
        work[row] = [v/leading for v in work[row]]
        for i in range(row+1, len(work)):
            coefficient = work[i][column]
            if coefficient:
                work[i] = [v-coefficient*w for v, w in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def central_block(s, degree, nodes):
    d = 2*s-1
    return [[sum(node**(r+a+t+c) for node in nodes)
             for t in range(s+1) for c in range(d-degree+1)]
            for r in range(s) for a in range(degree+1)]


def row_times_matrix(row, matrix):
    return [sum(row[i]*matrix[i][j] for i in range(len(row)))
            for j in range(len(matrix[0]))]


def matrix_times_column(matrix, column):
    return [sum(v*w for v, w in zip(row, column)) for row in matrix]


def verify(s):
    assert s >= 2
    m, d = 2*s, 2*s-1
    n = m*(m+1)//2
    retained = list(range(s+1))
    dropped = list(range(s+1, m))
    a = root_polynomial(range(s-1))
    c = root_polynomial([s-1, s])
    g = multiply(a, c)
    assert g == root_polynomial(retained)
    ap = a+[0]*(s-len(a))
    cp = c+[0]*(s+1-len(c))
    left = [ar*ca for ar in ap for ca in cp]
    right = [ct*az for ct in cp for az in ap]
    m0 = central_block(s, s, retained)
    m1 = central_block(s, s, dropped)
    assert not any(row_times_matrix(left, m0))
    assert not any(matrix_times_column(m0, right))
    # These coefficients multiply arbitrary entries of the tensor perturbation.
    annihilation = [sum(ap[r]*cp[t]*sum(node**(r+t+i) for node in retained)
                        for r in range(s) for t in range(s+1))
                    for i in range(m)]
    assert not any(annihilation)
    forcing = sum(x*y for x, y in zip(left, matrix_times_column(m1, right)))
    assert forcing == sum(evaluate(g, node)**2 for node in dropped)
    assert forcing > 0
    ranks = [rank_rational(central_block(s, degree, retained))
             for degree in range(m)]
    assert sum(ranks) == n+s-1
    assert all(ranks[degree] == min(s+1, s+degree, 3*s-degree)
               for degree in range(m))
    return {'m': m, 's': s, 'N': n, 'retained_nodes': retained,
            'dropped_nodes': dropped, 'a_coefficients': a, 'c_coefficients': c,
            'g_coefficients': g, 'block_ranks': ranks,
            'total_target_rank': sum(ranks), 'source_rank_allowance': n+s-1,
            'left_kernel_verified': True, 'right_kernel_verified': True,
            'all_perturbation_coefficients_annihilated': True,
            'nonzero_normal_forcing': forcing}


def report(max_s=5):
    return {'status': 'exact finite controls for the written obstruction',
            'cases': [verify(s) for s in range(2, max_s+1)],
            'scope': 'excludes the specified simple-pole and quadratic-ramified families',
            'second_order_zero_correction': 'proved by the image-intersection argument in README',
            'higher_ramification_excluded': False,
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-s', type=int, default=5)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = report(args.max_s)
    data = json.dumps(result, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
