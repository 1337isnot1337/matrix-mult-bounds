#!/usr/bin/env python3
"""Exact finite replay for the diagonal-shift correction flattening."""

import argparse
from collections import defaultdict
import json
from pathlib import Path


def correction(n):
    """Build M(n,4,n) minus the literal image of Q(n,4) under (1)."""
    out = defaultdict(int)
    for p in range(n):
        for q in range(n):
            for y in range(4):
                for v in range(4):
                    s, z = q + v, p + y
                    if s >= n or z >= n:
                        continue
                    for t in range(4):
                        i, h = q + t, p + t
                        if i < n and h < n:
                            # A_(p,q) -> a_(q+t,p+t),
                            # B_(y,s) -> b_(s,y), C_(z,v) -> c_(v,z).
                            out[(i * n + h, s * 4 + y, v * n + z)] -= 1

    for i in range(n):
        for h in range(n):
            for j in range(4):
                out[(i * n + h, i * 4 + j, j * n + h)] += 1
    return {key: value for key, value in out.items() if value}


def projected_matrix(n, tensor):
    """Sum the (0,0) and (1,1) inner-coordinate blocks."""
    matrix = [[0] * (n * n) for _ in range(n * n)]
    for (a, b, c), value in tensor.items():
        s, y = divmod(b, 4)
        v, z = divmod(c, n)
        if (y, v) in ((0, 0), (1, 1)):
            matrix[s * n + z][a] += value
    return matrix


def diagonal_formula(n):
    """Build the direct sum of the integer blocks T_(n-|delta|)."""
    matrix = [[0] * (n * n) for _ in range(n * n)]
    for delta in range(-(n - 1), n):
        length = n - abs(delta)
        s0, z0 = max(delta, 0), max(-delta, 0)
        for k in range(length):
            row = (s0 + k) * n + z0 + k
            if k == 0:
                matrix[row][(s0 + k) * n + z0 + k] += 1
                for offset in range(1, 4):
                    if k + offset < length:
                        col = (s0 + k + offset) * n + z0 + k + offset
                        matrix[row][col] -= 1
            else:
                for offset, value in ((-1, -1), (1, -2), (2, -2), (3, -1)):
                    if 0 <= k + offset < length:
                        col = (s0 + k + offset) * n + z0 + k + offset
                        matrix[row][col] += value
    return matrix


def rank_mod_two(matrix):
    work = [[value & 1 for value in row] for row in matrix]
    rows = len(work)
    rank = 0
    for col in range(len(work[0]) if work else 0):
        pivot = next((r for r in range(rank, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for r in range(rows):
            if r != rank and work[r][col]:
                work[r] = [left ^ right for left, right in zip(work[r], work[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def verify(max_n):
    if type(max_n) is not int or max_n < 1:
        raise ValueError('max_n must be a positive integer')
    sizes = []
    for n in range(1, max_n + 1):
        tensor = correction(n)
        direct = projected_matrix(n, tensor)
        formula = diagonal_formula(n)
        if direct != formula:
            raise ValueError(f'diagonal block formula disagrees at n={n}')
        rank = rank_mod_two(direct)
        if rank != n * n:
            raise ValueError(f'projected rank is {rank}, expected {n*n}, at n={n}')
        sizes.append({
            'n': n,
            'correction_nonzero_coefficients': len(tensor),
            'projected_first_flattening_rank_mod_2': rank,
            'first_leg_dimension': n * n,
            'diagonal_block_count': 2 * n - 1,
            'diagonal_block_length_sum': n * n,
        })
    return {
        'claim': 'AI-Q64-DIAGONAL-SHIFT-CORRECTION-001',
        'exact_integer_replay': True,
        'projection': 'sum of inner-coordinate blocks (0,0) and (1,1)',
        'sizes': sizes,
        'all_size_argument': 'proof.md, via the kernel recurrence modulo 2',
        'general_q_maps_excluded': False,
        'exponent_improvement': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=12)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(args.max_n)
    serialized = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized, end='')
