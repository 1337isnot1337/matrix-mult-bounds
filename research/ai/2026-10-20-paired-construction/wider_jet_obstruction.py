"""Exact coefficient certificate excluding one ordinary boundary-jet ansatz.

For n >= m+1, the regular-nilpotent B quotient of Q(n,m) cannot yield
M(n,m,n), regardless of the C quotient. This does not classify other B
kernels and does not exclude singular Laurent families.
"""

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    answer = Q(1)
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            answer = -answer
        value = a[col][col]
        answer *= value
        for i in range(col + 1, n):
            if a[i][col]:
                multiplier = a[i][col] / value
                for j in range(col + 1, n):
                    a[i][j] -= multiplier * a[col][j]
                a[i][col] = 0
    return answer


def maps(n, m):
    if m < 2 or n < m + 1:
        raise ValueError('The certified obstruction requires m >= 2 and n >= m+1.')
    long = n + m - 1
    bdim, cdim = n * m, m * long
    bmap = [[0] * bdim for _ in range(m * long)]
    for y in range(m):
        for j in range(long):
            if j < m:
                power = m - 1 - j
                if y >= power:
                    bmap[y * long + j][y - power] = (-1) ** power
            else:
                bmap[y * long + j][m + (j - m) * m + y] = 1

    # Full C coordinates are c_(p,alpha), followed by the free original
    # C_(z,v) with z < m-1. No free coordinate is discarded.
    cmap = [[0] * cdim for _ in range(cdim)]
    for z in range(m - 1):
        for v in range(m):
            cmap[z * m + v][n * m + z * m + v] = 1
    for z in range(m - 1, long):
        p = z - m + 1
        for alpha in range(m):
            row = cmap[z * m + alpha]
            row[p * m + alpha] = (-1) ** (m - 1 - alpha)
            for v in range(alpha + 1, m):
                factor = -(-1) ** (v - alpha)
                earlier = cmap[(z + alpha - v) * m + v]
                for col, value in enumerate(earlier):
                    row[col] += factor * value
    return bmap, cmap


def slice_matrix(n, m, bmap, cmap, p, q):
    long = n + m - 1
    matrix = [[0] * len(cmap[0]) for _ in range(len(bmap[0]))]
    for y in range(m):
        for v in range(m):
            b = bmap[y * long + q + v]
            c = cmap[(p + y) * m + v]
            for i, x in enumerate(b):
                if x:
                    for j, value in enumerate(c):
                        if value:
                            matrix[i][j] += x * value
    return matrix


def control(n, m):
    bmap, cmap = maps(n, m)
    bdim, cdim = len(bmap[0]), len(cmap[0])
    det = determinant(cmap)
    assert abs(det) == 1
    # Expand every A-slice, not only the support of the expected identities.
    slices = [[slice_matrix(n, m, bmap, cmap, p, q) for q in range(n)]
              for p in range(n)]
    for p in range(n):
        expected = [[0] * cdim for _ in range(bdim)]
        for alpha in range(m):
            expected[alpha][p * m + alpha] = 1
        assert slices[p][0] == expected

    offending = slices[m][1]
    expected = [[0] * cdim for _ in range(bdim)]
    for y in range(m):
        for v in range(max(0, m - 2 - y), m - 1):
            alpha = y - m + 2 + v
            expected[alpha][y * m + v + 1] += 1
            expected[alpha][(y + 1) * m + v] -= 1
        expected[m + y][(y + 1) * m + m - 1] += 1
    assert offending == expected
    block = [row[:m] for row in offending]
    block_expected = [[0] * m for _ in range(bdim)]
    block_expected[0][m - 1] = 1
    assert block == block_expected
    assert all(not any(row[n * m:]) for row in offending)
    result = {
        'n': n, 'm': m,
        'source_dimensions': [n * n, cdim, cdim],
        'target_dimensions': [n * n, bdim, bdim],
        'b_kernel_dimension': m * (m - 1),
        'c_coordinate_change_determinant': int(det),
        'all_source_monomials_expanded': n * n * m * m,
        'fixed_q_zero_fibre_identities': n,
        'full_offending_identity_passes': True,
        'offending_parameter': [m, 1],
        'offending_has_no_free_c_coordinates': True,
        'first_paired_block_nonzeros': [[0, m - 1, 1]],
        'first_paired_block_rank': 1,
    }
    if (n, m) == (5, 4):
        result.update({'b_quotient_map': bmap, 'c_full_coordinate_map': cmap,
                       'offending_full_matrix': offending, 'first_paired_block': block})
    return result


def run():
    return {
        'scope': 'One specified regular-nilpotent B quotient, with arbitrary ordinary C quotient; no full-kernel classification or border exclusion.',
        'field': 'Q; the symbolic argument applies over C',
        'improves_omega': False,
        'records': [control(n, m) for n, m in [(3, 2), (4, 3), (5, 4), (13, 4)]],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'controls': len(report['records']), 'all_pass': True,
                      'improves_omega': False, 'output': str(args.output)}))
