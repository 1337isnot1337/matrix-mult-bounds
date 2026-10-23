#!/usr/bin/env python3
"""Exact finite controls for diagonal-biform rank formulas; stdlib only.

Written all-size proofs are in proof.md. These checks cover finite sizes.
"""
import argparse
import json
from pathlib import Path


def rank_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    if not a:
        return 0
    rows, cols = len(a), len(a[0])
    pivot = 0
    for col in range(cols):
        if pivot == rows:
            break
        k = next((k for k in range(pivot, rows) if a[k][col]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        inv = pow(a[pivot][col], -1, p)
        a[pivot] = [v * inv % p for v in a[pivot]]
        for k in range(pivot + 1, rows):
            factor = a[k][col]
            if factor:
                a[k] = [(a[k][j] - factor * a[pivot][j]) % p
                        for j in range(cols)]
        pivot += 1
    return pivot


def full_matrix(a, coeff):
    """Literal R_a with rows (j,L) and columns (H,r)."""
    n = a * (2*a-1)
    mat = [[0] * n for _ in range(n)]
    for j in range(a):
        for ell in range(2*a-1):
            row = mat[j * (2*a-1) + ell]
            for k, value in enumerate(coeff):
                h, r = j+k, ell-k
                if h < 2*a-1 and 0 <= r < a:
                    row[h*a+r] = value
    return mat


def block(a, coeff, s):
    indices = range(max(0, s-2*a+2), min(a-1, s)+1)
    return [[coeff[k] if 0 <= (k := s-i-j) < len(coeff)
             else 0 for j in indices] for i in indices]


def toeplitz(a, coeff, h):
    return [[coeff[k] if 0 <= (k := h+1+v-u) < len(coeff)
             else 0 for v in range(a)] for u in range(a)]


def determinant(a, c0, c1, c2, p):
    d0, d1 = 1, c1 % p
    for _ in range(2, a+1):
        d0, d1 = d1, (c1*d1-c0*c2*d0) % p
    return d1 if a else d0


def verify():
    primes = (2, 3, 5, 7, 101)
    polys = ((1,), (1,1), (2,1), (1,1,1), (1,0,1),
             (1,2,3), (2,3,2), (1,2,0,1), (2,0,1,3))
    block_cases = full_cases = quadratic_cases = tail_cases = 0
    for p in primes:
        for a in range(3, 11):
            for coeff in polys:
                d = len(coeff)-1
                if d >= a or coeff[0] % p == 0 or coeff[-1] % p == 0:
                    continue
                blocks = [block(a, coeff, s) for s in range(3*a-2)]
                got = sum(rank_mod(b, p) for b in blocks)
                expected = a*a + sum(rank_mod(toeplitz(a, coeff, h), p)
                                     for h in range(d))
                assert got == expected, (p,a,coeff,got,expected)
                block_cases += 1
                if d == 2:
                    det = determinant(a, *coeff, p)
                    predicted = a*a+2*a-(det == 0)
                    assert got == predicted, (p,a,coeff,got,predicted)
                    quadratic_cases += 1
                for s, b in enumerate(blocks):
                    if s < a:
                        rank_expected = s+1
                    elif s >= a+d:
                        rank_expected = max(0, 2*a+d-1-s)
                    else:
                        continue
                    assert rank_mod(b,p) == rank_expected, (p,a,coeff,s)
                    tail_cases += 1
                if a <= 5:
                    full_rank = rank_mod(full_matrix(a,coeff), p)
                    assert full_rank == got, (p,a,coeff,full_rank,got)
                    full_cases += 1
    periodic = 0
    for p in primes:
        for a in range(3, 61):
            assert (determinant(a,1,1,1,p) == 0) == (a % 3 == 2)
            periodic += 1
    return {
        'result': 'pass', 'primes': list(primes),
        'block_rank_cases': block_cases,
        'full_literal_matrix_cases': full_cases,
        'quadratic_closed_rank_cases': quadratic_cases,
        'triangular_block_cases': tail_cases,
        'cyclotomic_recurrence_cases': periodic,
        'scope': 'finite controls; all-field claims require the written proofs'
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(verify(), indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding='utf-8')
    print(result, end='')


if __name__ == '__main__':
    main()
