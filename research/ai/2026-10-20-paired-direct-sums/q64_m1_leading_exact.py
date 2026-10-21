"""Exact checks for two leading M(1,4,1) points in Q(6,4).

Only the sparse fixed point is excluded.  No result here excludes moving
leading maps, other valuations, or the endpoint product-injection point.
This verification module uses only the Python standard library.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]


def zeros(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def source_terms(n=6):
    return [(n*p+q, (n+3)*y+q+v, 4*(p+y)+v)
            for p, q, y, v in product(range(n), range(n), range(4), range(4))]


def powers():
    return [[-int(i > 0)-int(k > 0) for i in range(5) for k in range(5)],
            [int(i > 0) for i in range(5) for _ in range(4)],
            [int(k > 0) for _ in range(4) for k in range(5)]]


def sparse_maps(n=6):
    """Return only the four old B and C rows of the sparse leading point."""
    b, c = zeros(4, 4*(n+3)), zeros(4, 4*(n+3))
    for y, v in product(range(2), repeat=2):
        b[2*y+v][(n+3)*y+v] = 1
        c[2*y+v][4*y+v] = 1
    return b, c


def embedded_product_maps():
    """Embed the previously certified exact Q54 -> M4 maps in Q64 -> M5."""
    certificate = REPO/'research/ai/2026-10-20-paired-construction/q54-exact.json'
    a0, b0, c0 = json.loads(certificate.read_text())['maps_target_by_source']
    a, b, c = [zeros(rows, 36) for rows in [25, 20, 20]]
    for i, k, p, q in product(range(4), range(4), range(5), range(5)):
        a[5*i+k][6*p+q] = a0[4*i+k][5*p+q]
    for i, j, y, s in product(range(4), range(4), range(4), range(8)):
        b[4*i+j][9*y+s] = b0[4*i+j][8*y+s]
    for j, k, z, v in product(range(4), range(4), range(8), range(4)):
        c[5*j+k][4*z+v] = c0[4*j+k][4*z+v]
    return a, b, c


def rref(matrix):
    """Rational row reduction, returning the full matrix and pivot columns."""
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return a, []
    row, pivots = 0, []
    for column in range(len(a[0])):
        found = next((i for i in range(row, len(a)) if a[i][column]), None)
        if found is None:
            continue
        a[row], a[found] = a[found], a[row]
        pivot = a[row][column]
        a[row] = [x/pivot for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][column]:
                scale = a[i][column]
                a[i] = [x-scale*y for x, y in zip(a[i], a[row])]
        pivots.append(column)
        row += 1
        if row == len(a):
            break
    return a, pivots


def leading_data(b, c, n=6):
    """Compute H0 and the exact source spans of both first-edge tensors."""
    h = zeros(16, n*n)
    for a_index, b_index, c_index in source_terms(n):
        for j, k in product(range(4), repeat=2):
            h[4*j+k][a_index] += b[j][b_index]*c[k][c_index]
    reduced, pivots = rref(h)
    free = [i for i in range(n*n) if i not in pivots]
    kernel = []
    for f in free:
        vector = [Fraction(0) for _ in range(n*n)]
        vector[f] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][f]
        kernel.append(vector)
    bf = zeros(4*(n+3), 4*len(kernel))
    cf = zeros(4*(n+3), 4*len(kernel))
    for a_index, b_index, c_index in source_terms(n):
        for u, vector in enumerate(kernel):
            value = vector[a_index]
            if not value:
                continue
            for j in range(4):
                bf[b_index][4*u+j] += value*c[j][c_index]
                cf[c_index][4*u+j] += value*b[j][b_index]
    return {'pre_A_rank': len(pivots), 'pre_A_kernel_dimension': len(free),
            'first_edge_source_ranks': [len(rref(bf)[1]), len(rref(cf)[1])],
            'B_first_edge_nonzero_source_columns': [i for i, row in enumerate(bf) if any(row)],
            'C_first_edge_nonzero_source_columns': [i for i, row in enumerate(cf) if any(row)]}


def inherited_jet_data():
    """Check the first jet of the three inherited non-old M4 outer rows."""
    a, b, c = embedded_product_maps()
    old_b, old_c = b[:4], [c[5*j] for j in range(4)]
    h0, h1 = zeros(16, 36), zeros(128, 36)
    for aa, bb, cc in source_terms():
        for j, k in product(range(4), repeat=2):
            h0[4*j+k][aa] += old_b[j][bb]*old_c[k][cc]
        for new, j in product(range(16), range(4)):
            h1[4*new+j][aa] += b[4+new][bb]*old_c[j][cc]
            outer, middle = divmod(new, 4)
            h1[64+4*new+j][aa] += old_b[j][bb]*c[5*middle+outer+1][cc]
    rank0, rank01 = len(rref(h0)[1]), len(rref(h0+h1)[1])
    p = zeros(4, 6)
    for row, column in enumerate([0, 2, 3, 5]):
        p[row][column] = 1
    p[0][4] = -1
    corner = [[u[i]*v[j] for i, j in product(range(6), repeat=2)]
              for u, v in product(p, repeat=2)]
    if len(rref(corner)[1]) != 16:
        raise ArithmeticError('The proposed corner vectors are dependent.')
    if any(sum(x*y for x, y in zip(row, v)) for row in h0+h1 for v in corner):
        raise ArithmeticError('The proposed corner does not annihilate the first jet.')
    for outer in range(1, 4):
        for side, a_row in [(0, 5*outer), (1, outer)]:
            actual = [sum(x*y for x, y in zip(row, a[a_row])) for row in h1]
            wanted = [0]*128
            for j in range(4):
                wanted[64*side+4*(4*(outer-1)+j)+j] = 1
            if actual != wanted:
                raise ArithmeticError('An inherited target edge did not reconstruct.')
    if (rank0, rank01) != (4, 20):
        raise ArithmeticError('The inherited first-jet ranks changed.')
    return {'H0_rank': rank0, 'H1_on_kernel_H0_rank': rank01-rank0,
            'stacked_H0_H1_rank': rank01,
            'remaining_kernel_dimension': 36-rank01,
            'remaining_kernel_is_P_tensor_P': True,
            'P_basis_coefficients': p,
            'inherited_target_edge_slices_checked': 6,
            'fourth_outer_row_constructed': False}


def exact_report():
    from q64_experiment_replay import contraction, degrees

    sparse = leading_data(*sparse_maps())
    expected_b = [9*y+s for y in range(2) for s in range(2, 7)]
    if sparse['pre_A_rank'] != 4 or sparse['first_edge_source_ranks'] != [10, 10]:
        raise ArithmeticError('The sparse leading-point ranks changed.')
    if sparse['B_first_edge_nonzero_source_columns'] != expected_b:
        raise ArithmeticError('The sparse first-edge support formula failed.')

    maps = embedded_product_maps()
    actual, _ = contraction(maps, 0)
    target = [0]*10000
    for i, j, k in product(range(4), repeat=3):
        target[((5*i+k)*20+4*i+j)*20+5*j+k] = 1
    if actual != target:
        raise ArithmeticError('The exact embedded M4 coefficient identity failed.')
    degree = degrees(powers())
    if any(a for a, d in zip(actual, degree) if d != 0):
        raise ArithmeticError('The M1 powers do not preserve the embedded M4.')
    b, c = maps[1][:4], [maps[2][5*j] for j in range(4)]
    endpoint = leading_data(b, c)
    if endpoint['pre_A_rank'] != 4 or endpoint['first_edge_source_ranks'] != [32, 32]:
        raise ArithmeticError('The endpoint leading-point ranks changed.')
    return {'source': 'Q(6,4)', 'target_sought': 'M(5,4,5)',
            'coefficient_ring': 'Q', 'auxiliary_rank': 0,
            'source_terms_checked': 576,
            'embedded_M4_target_positions_checked': 10000,
            'embedded_M4_nonzero_positions': 64,
            'map_row_powers': powers(), 'sparse_fixed_point': sparse,
            'sparse_fixed_point_target_edge_rank_required': 16,
            'sparse_fixed_point_excluded_in_stated_chart': True,
            'endpoint_product_point': endpoint,
            'endpoint_passes_first_edge_flattening_test': True,
            'inherited_first_jet': inherited_jet_data(),
            'moving_leading_maps_excluded': False,
            'full_target_degeneration_proved': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(exact_report(), indent=2))
