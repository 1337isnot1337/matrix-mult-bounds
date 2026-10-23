"""Finite exact controls for the written higher-Hankel/Segre argument.

All arithmetic is integral modulo the displayed prime. These controls
check concrete examples; they do not certify the universal geometric
theorem or construct a tensor restriction.
"""

from __future__ import annotations

import argparse
import itertools
import json
from math import comb
from pathlib import Path

PRIME = 101


def rank_mod(rows, prime=PRIME):
    rows = [[x % prime for x in row] for row in rows]
    if not rows:
        return 0
    pivot_row = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][col], -1, prime)
        rows[pivot_row] = [(v*inverse) % prime for v in rows[pivot_row]]
        for i in range(pivot_row+1, len(rows)):
            if rows[i][col]:
                multiple = rows[i][col]
                rows[i] = [(v-multiple*w) % prime
                           for v, w in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def jet_vector(degree, point, order):
    if point is None:
        return [int(j == degree-order) for j in range(degree+1)]
    return [comb(j, order)*point**(j-order) if j >= order else 0
            for j in range(degree+1)]


def span_vectors(degree, divisor, points=(0, 1, 2, None)):
    return [jet_vector(degree, point, order)
            for point, multiplicity in zip(points, divisor)
            for order in range(multiplicity)]


def divisors(length, point_count=4):
    return [multiplicities for multiplicities in itertools.product(range(length+1), repeat=point_count)
            if sum(multiplicities) <= length]


def hermite_intersections(maximum_length=3, degree=8):
    supports = divisors(maximum_length)
    checks = 0
    for left in supports:
        left_vectors = span_vectors(degree, left)
        assert rank_mod(left_vectors) == sum(left)
        for right in supports:
            union = tuple(max(x, y) for x, y in zip(left, right))
            intersection = tuple(min(x, y) for x, y in zip(left, right))
            assert sum(union) <= degree+1
            right_vectors = span_vectors(degree, right)
            intersection_dimension = (rank_mod(left_vectors)+rank_mod(right_vectors)
                                      -rank_mod(left_vectors+right_vectors))
            assert intersection_dimension == sum(intersection)
            checks += 1
    return {'degree': degree, 'maximum_divisor_length': maximum_length,
            'points': [0, 1, 2, 'infinity'], 'divisor_count': len(supports),
            'ordered_intersection_checks': checks}


def hankel(sequence, a, b):
    assert len(sequence) == a+b-1
    return [[sequence[p+q] for q in range(b)] for p in range(a)]


def support_union_controls(a, b, rank_limit):
    degree = a+b-2
    assert degree >= 3*rank_limit-1 and rank_limit < min(a, b)
    supports = divisors(rank_limit)
    supports = [s for s in supports if sum(s) == rank_limit]
    checks = 0
    for left in supports:
        lv = span_vectors(degree, left)
        f = [sum(v[k] for v in lv) for k in range(degree+1)]
        assert rank_mod(hankel(f, a, b)) == rank_limit
        for right in supports:
            union = tuple(max(x, y) for x, y in zip(left, right))
            if sum(union) <= rank_limit:
                continue
            rv = span_vectors(degree, right)
            g = [sum(v[k] for v in rv) for k in range(degree+1)]
            # t=2 never cancels the chosen highest jet coefficients 1 or 3.
            mixed = [x+2*y for x, y in zip(f, g)]
            assert rank_mod(hankel(mixed, a, b)) > rank_limit
            checks += 1
    return {'a': a, 'b': b, 'rank_limit': rank_limit,
            'support_pairs_forced_above_rank_limit': checks}


def source_slice_rows(a, b, coefficients):
    m = a+b-1
    rows = []
    for j in range(b):
        for p in range(a):
            for ell in range(m):
                rows.append([coefficients.get((hh-j, p+q, ell-r), 0)
                             for hh in range(m) for q in range(b) for r in range(a)])
    return rows


def coherent_source_control(a, b, divisor):
    degree = a+b-2
    vectors = span_vectors(degree, divisor)
    sequence = [sum(v[k] for v in vectors) for k in range(degree+1)]
    # A single monomial in the two outer variables; all divisor jets
    # occur with nonzero top coefficient.
    coefficients = {(0, k, 0): h for k, h in enumerate(sequence) if h}
    symbol_rank = rank_mod(hankel(sequence, a, b))
    source_rank = rank_mod(source_slice_rows(a, b, coefficients))
    assert symbol_rank == sum(divisor)
    assert source_rank == a*b*symbol_rank
    return {'a': a, 'b': b, 'divisor': divisor,
            'symbol_rank': symbol_rank, 'source_slice_rank': source_rank,
            'ab_times_symbol_rank': a*b*symbol_rank}


def report():
    return {'scope': 'finite exact arithmetic controls only; written proof is separate',
            'prime': PRIME,
            'hermite_intersections': hermite_intersections(),
            'support_union_controls': [support_union_controls(3, 4, 2),
                                       support_union_controls(4, 6, 3)],
            'coherent_source_controls': [coherent_source_control(3, 4, (1, 1, 0, 0)),
                                         coherent_source_control(3, 4, (0, 2, 0, 0)),
                                         coherent_source_control(3, 4, (0, 1, 0, 1)),
                                         coherent_source_control(4, 6, (0, 3, 0, 0))],
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
