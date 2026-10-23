#!/usr/bin/env python3
"""Independent literal-source finite-field check of the top-coefficient biform rank theorem.

Uses only the Python standard library. The rank oracle builds the complete
coefficient matrix, including its zero rows, rather than using the syzygy proof.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def coefficient_matrix(a: int, b: int, e: int, c: tuple[int, ...], w: tuple[int, ...], p: int):
    """The literal R_(a,b) rows (j,L), columns (H,r)."""
    assert a >= 2 and b > e >= 1 and len(c) == e and len(w) == a
    m = a + b - 1
    M = [[0] * (a * m) for _ in range(b * m)]
    # Build from source coefficients directly, never from the recurrence.
    for r in range(a):
        for j in range(b):
            for s, coefficient in enumerate(c):
                row = j * m + (r + s)
                col = j * a + r  # column index is actually H*a+r; H=j.
                M[row][col] = (M[row][col] + coefficient) % p
            for k, coefficient in enumerate(w):
                if coefficient:
                    row = j * m + (r + e)
                    col = (j + k) * a + r
                    M[row][col] = (M[row][col] + coefficient) % p
    return M


def exact_rank_modp(M: list[list[int]], p: int) -> int:
    A = [row[:] for row in M]
    nrows = len(A)
    ncols = len(A[0])
    rank = 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, nrows) if A[i][col] % p), None)
        if pivot is None:
            continue
        A[rank], A[pivot] = A[pivot], A[rank]
        inv = pow(A[rank][col] % p, -1, p)
        A[rank][col:] = [(x * inv) % p for x in A[rank][col:]]
        for i in range(rank + 1, nrows):
            multiplier = A[i][col] % p
            if multiplier:
                A[i][col:] = [(x - multiplier * y) % p for x, y in zip(A[i][col:], A[rank][col:])]
        rank += 1
        if rank == nrows:
            break
    return rank


def predicted_rank(a: int, b: int, e: int, w: tuple[int, ...], p: int) -> int:
    deg = max(k for k, coeff in enumerate(w) if coeff % p)
    return a * b + sum(min(b, deg * ((a + j) // e)) for j in range(e))


def verify(a, b, e, c, w, p):
    expected = predicted_rank(a, b, e, w, p)
    got = exact_rank_modp(coefficient_matrix(a, b, e, c, w, p), p)
    if expected != got:
        raise AssertionError(f"R({a},{b}) e={e}, c={c}, w={w} over F_{p}: expected {expected}, got {got}")
    return expected


def xorshift32(x):
    x ^= (x << 13) & 0xFFFFFFFF
    x ^= x >> 17
    x ^= (x << 5) & 0xFFFFFFFF
    return x & 0xFFFFFFFF


def run():
    counts = Counter()
    shapes = set()
    observed = set()
    # All lower coefficients and all nonzero top polynomials, over F_2.
    for a in (2, 3, 4):
        for b in range(3, 7):
            for e in range(2, min(4, b - 1) + 1):
                for lower in itertools.product(range(2), repeat=e - 1):
                    c = (1,) + lower
                    for w in itertools.product(range(2), repeat=a):
                        if not any(w):
                            continue
                        got = verify(a, b, e, c, w, 2)
                        shapes.add((a, b, e))
                        observed.add(got)
                        counts['GF2_exhaustive'] += 1
    # Exhaustive F_3 controls for smaller shapes.
    for a in (2, 3):
        for b in range(3, 6):
            for e in range(2, min(3, b - 1) + 1):
                for c0 in (1, 2):
                    for lower in itertools.product(range(3), repeat=e - 1):
                        c = (c0,) + lower
                        for w in itertools.product(range(3), repeat=a):
                            if not any(w):
                                continue
                            verify(a, b, e, c, w, 3)
                            counts['GF3_exhaustive'] += 1
    # Fixed-seed, broad rectangular spectrum; coefficients are unrestricted.
    rng = 0xB1F0A26E
    for p in (5, 7, 101):
        for a in range(2, 8):
            for e in range(2, 6):
                for b in (e + 1, e + 3, e + 7):
                    c = []
                    for i in range(e):
                        rng = xorshift32(rng)
                        c.append((rng % (p - 1)) + 1 if i == 0 else rng % p)
                    w = []
                    for i in range(a):
                        rng = xorshift32(rng)
                        w.append(rng % p)
                    if not any(w):
                        w[0] = 1
                    verify(a, b, e, tuple(c), tuple(w), p)
                    counts['seeded'] += 1
    # Each possible degree: factor through neither a diagonal nor binomial restriction.
    for p in (2, 3, 5, 101):
        for a in range(2, 9):
            for d in range(0, a):
                for e in (2, 3, 4):
                    b = max(e + 1, a * d + 1)
                    c = (1,) + (1,) + (0,) * (e - 2)
                    w = (1,) + (0,) * (d - 1) + (1,) if d else (1,)
                    w = w + (0,) * (a - len(w))
                    verify(a, b, e, c, w, p)
                    counts['degree_witnesses'] += 1
    return {'result':'PASS','checks':dict(counts), 'total':sum(counts.values()),
            'exhaustive_GF2_shapes':len(shapes), 'exhaustive_GF2_distinct_ranks':len(observed),
            'seed':'0xB1F0A26E', 'fields':[2,3,5,7,101],
            'formula':'rank = ab + sum_{j=0}^{e-1} min(b, d*floor((a+j)/e))'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--receipt', type=Path)
    args = ap.parse_args()
    receipt = run()
    s = json.dumps(receipt, indent=2, sort_keys=True) + '\n'
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(s)
    print(s, end='')
