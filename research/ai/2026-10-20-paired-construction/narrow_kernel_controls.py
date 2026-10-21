"""Exact local coefficient controls for the ordinary Q_(3,2) obstruction.

These checks verify the integer identities used in the written proof.
They do not replace its incidence, pencil, fibre, or projective lemmas,
and they do not exclude a singular Laurent degeneration.
"""

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path


def rank(matrix):
    if not matrix:
        return 0
    a = [[Q(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(a[0])):
        selected = next((i for i in range(pivot, len(a)) if a[i][column]), None)
        if selected is None:
            continue
        a[pivot], a[selected] = a[selected], a[pivot]
        value = a[pivot][column]
        a[pivot] = [x / value for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            multiplier = a[i][column]
            if multiplier:
                a[i] = [x - multiplier * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def determinant(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError('The determinant requires a square matrix.')
    value = Q(1)
    for column in range(n):
        selected = next((i for i in range(column, n) if a[i][column]), None)
        if selected is None:
            return Q(0)
        if selected != column:
            a[column], a[selected] = a[selected], a[column]
            value = -value
        pivot = a[column][column]
        value *= pivot
        for i in range(column + 1, n):
            multiplier = a[i][column] / pivot
            for j in range(column + 1, n):
                a[i][j] -= multiplier * a[column][j]
            a[i][column] = 0
    return value


def add_outer(matrix, left, right, coefficient=1):
    for i, x in enumerate(left):
        if x:
            for j, y in enumerate(right):
                if y:
                    matrix[i][j] += coefficient * x * y


def source_slices(n, bmap, cmap):
    """Expand every coefficient of A_pq B_y,q+v C_p+y,v independently."""
    bdim, cdim = len(bmap[0]), len(cmap[0])
    slices = []
    for p in range(n):
        for q in range(n):
            matrix = [[0] * cdim for _ in range(bdim)]
            for y in range(2):
                for v in range(2):
                    add_outer(matrix, bmap[y * (n + 1) + q + v],
                              cmap[2 * (p + y) + v])
            slices.append(matrix)
    return slices


def jet_control(n):
    if n < 3:
        raise ValueError('The offending A21 slice requires n >= 3.')
    bdim, cdim = 2 * n, 2 * n + 2
    # Quotient K_B = span(B00, B01+B10), retaining b_(2(j-1)+y)=B_yj.
    bmap = [[0] * bdim for _ in range(2 * (n + 1))]
    bmap[n + 1][0] = -1
    for y in range(2):
        for j in range(1, n + 1):
            bmap[y * (n + 1) + j][2 * (j - 1) + y] = 1

    # This is an invertible coordinate change on the FULL original C space.
    # Basis: c_p0=C_p1-C_(p+1),0, c_p1=C_(p+1),1, u=C00, v=C01.
    # The two free coordinates u,v are retained, not set to zero.
    cmap = [[0] * cdim for _ in range(cdim)]
    cmap[0][2 * n] = 1
    cmap[1][2 * n + 1] = 1
    cmap[2][2 * n + 1] = 1
    cmap[2][0] = -1
    for z in range(2, n + 1):
        cmap[2 * z][2 * (z - 2) + 1] = 1
        cmap[2 * z][2 * (z - 1)] = -1
    for z in range(1, n + 1):
        cmap[2 * z + 1][2 * (z - 1) + 1] = 1
    change_det = determinant(cmap)
    assert abs(change_det) == 1

    slices = source_slices(n, bmap, cmap)
    fibre_equalities = []
    for p in range(n):
        expected = [[0] * cdim for _ in range(bdim)]
        expected[0][2 * p] = 1
        expected[1][2 * p + 1] = 1
        equal = slices[p * n] == expected
        assert equal
        fibre_equalities.append(equal)

    offending = slices[2 * n + 1]
    expected = [[0] * cdim for _ in range(bdim)]
    # b0(c01-c10) + b2 c11 + b1(c11-c20) + b3 c21.
    for row, col, coefficient in [(0, 1, 1), (0, 2, -1), (2, 3, 1),
                                  (1, 3, 1), (1, 4, -1), (3, 5, 1)]:
        expected[row][col] = coefficient
    assert offending == expected
    block = [row[:2] for row in offending]
    assert rank(block) == 1
    free_columns_zero = all(row[-2:] == [0, 0] for row in offending)
    assert free_columns_zero
    result = {
        'n': n,
        'source_dimensions': [n * n, 2 * (n + 1), 2 * (n + 1)],
        'b_quotient_dimension': bdim,
        'c_coordinate_change_determinant': int(change_det),
        'source_monomials_expanded': 4 * n * n,
        'fibre_slice_equalities': fibre_equalities,
        'offending_slice_parameter': [2, 1],
        'offending_complete_identity_passes': True,
        'offending_free_coordinate_columns_zero': free_columns_zero,
        'paired_block_rank': rank(block),
        'paired_block': block,
    }
    if n == 3:
        result.update({'b_quotient_map': bmap, 'c_full_coordinate_map': cmap,
                       'offending_full_matrix': offending,
                       'fibre_full_matrices': [slices[p * n] for p in range(n)]})
    return result


def polynomial_product(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            answer[i + j] += x * y
    return answer


def quotient_map(kernel):
    """Return coordinate images in the quotient, using exact row reduction."""
    a = [[Q(x) for x in row] for row in kernel]
    ambient = len(a[0])
    pivots = []
    for column in range(ambient):
        selected = next((i for i in range(len(pivots), len(a)) if a[i][column]), None)
        if selected is None:
            continue
        p = len(pivots)
        a[p], a[selected] = a[selected], a[p]
        scale = a[p][column]
        a[p] = [x / scale for x in a[p]]
        for i in range(len(a)):
            if i != p and a[i][column]:
                multiplier = a[i][column]
                a[i] = [x - multiplier * y for x, y in zip(a[i], a[p])]
        pivots.append(column)
        if len(pivots) == len(a):
            break
    free = [i for i in range(ambient) if i not in pivots]
    images = [[Q(0)] * len(free) for _ in range(ambient)]
    for j, col in enumerate(free):
        images[col][j] = 1
    for row, pivot in enumerate(pivots):
        images[pivot] = [-a[row][col] for col in free]
    assert all(all(sum(v[i] * images[i][j] for i in range(ambient)) == 0
                   for j in range(len(free))) for v in kernel)
    return images


def uniform_control(g, ell):
    if len(g) != 3 or len(ell) != 2 or not any(g) or not any(ell):
        raise ValueError('A nonzero quadratic and a nonzero linear form are required.')
    h = polynomial_product(g, ell)
    kernel = [h + [0] * 4, [0] * 4 + h]
    bmap = quotient_map(kernel)
    cmap = [[int(i == j) for j in range(8)] for i in range(8)]
    raw = source_slices(3, bmap, cmap)
    fibre = []
    for p in range(3):
        matrix = [[sum(g[q] * raw[3 * p + q][i][j] for q in range(3))
                   for j in range(8)] for i in range(6)]
        fibre.append(matrix)
    # Horizontal concatenation: the combined B-image of the fibre.
    b_span = rank([[x for matrix in fibre for x in matrix[i]] for i in range(6)])
    # Vertical concatenation: the combined C-support of the fibre.
    c_span = rank([row for matrix in fibre for row in matrix])
    individual = [rank(matrix) for matrix in fibre]
    assert b_span == 2
    assert c_span <= 4
    assert individual == [2, 2, 2]
    return {'quadratic_g': g, 'linear_ell': ell, 'cubic_h': h,
            'kernel_dimension': rank(kernel), 'combined_b_span': b_span,
            'combined_c_span': c_span, 'individual_slice_ranks': individual,
            'c_quotient_applied': False}


def run():
    return {
        'scope': 'Exact local identities for the ordinary Q_(3,2) obstruction; no singular-degeneration exclusion.',
        'field': 'Q (integer jet maps and rational uniform-kernel quotients)',
        'improves_omega': False,
        'jets': [jet_control(n) for n in range(3, 9)],
        'uniforms': [uniform_control(g, ell) for g, ell in [
            ([1, 0, 0], [1, 0]), ([1, 2, 1], [2, 3]),
            ([1, 0, 1], [1, 1]), ([0, 0, 1], [0, 1]),
            ([0, 1, 0], [1, -1])]],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = run()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'jet_controls': len(report['jets']), 'uniform_controls': len(report['uniforms']),
                      'all_pass': True, 'improves_omega': False, 'output': str(args.output)}))
