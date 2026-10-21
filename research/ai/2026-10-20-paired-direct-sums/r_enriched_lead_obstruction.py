"""Exact source checks for an enriched reduced-corner leading-point gate.

This checks the fixed R leading maps and the universal first-edge support
identities used in the accompanying proof.  It does not exclude arbitrary
degenerations from R plus two scalar summands.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

from q64_m1_leading_exact import rref
from reduced_corner_replay import SOURCE, contraction, source_terms


def zeros(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def leading_maps():
    """Return target-by-source maps with only outer indices zero and one active."""
    inverse = zeros(4, 7)
    for row, column, value in [(0, 0, 1), (1, 5, -1), (2, 2, 1),
                               (2, 5, 1), (3, 4, 1)]:
        inverse[row][column] = value
    a, b, c = [zeros(16, width) for width in [16, 18, 18]]
    native_old = [0, 2]
    for i, k in product(range(2), repeat=2):
        a[4*i+k][4*native_old[k]+native_old[i]] = 1
    for i, y, v, s in product(range(2), range(2), range(2), range(7)):
        b[4*i+2*y+v][7*y+s] = inverse[2*i+v][s]
    for k, y, v, s in product(range(2), range(2), range(2), range(7)):
        c[4*(2*y+v)+k][2*s+v] = inverse[2*k+y][s]
    # Interior native coordinates: b_(y,output), c_(output,v), offset14.
    b[0][14] = b[4][15] = 1
    c[0][14] = c[1][16] = 1
    # The interior adds a second copy of old middle channel zero.
    for row in [0, 4]:
        b[row] = [Fraction(x, 2) for x in b[row]]
    return [a, b, c]


def report():
    terms = source_terms()
    if len(terms) != 90:
        raise ArithmeticError('The maintained reduced-corner source changed.')
    maps = leading_maps()
    wanted = [0]*4096
    for i, j, k in product(range(2), range(4), range(2)):
        wanted[((4*i+k)*16+4*i+j)*16+4*j+k] = 1
    if contraction(maps) != wanted:
        raise ArithmeticError('The enriched leading M(2,4,2) did not reconstruct.')
    old_b = maps[1][:8]
    old_c = [maps[2][4*j+k] for j, k in product(range(4), range(2))]
    h0 = zeros(16, 64)
    for a, b, c, coefficient in terms:
        for i, j in product(range(8), repeat=2):
            h0[a][8*i+j] += coefficient*old_b[i][b]*old_c[j][c]
    active = [index for index, row in enumerate(h0) if any(row)]
    kernel_indices = [index for index, row in enumerate(h0) if not any(row)]
    if active != [0, 2, 8, 10] or len(rref(h0)[1]) != 4:
        raise ArithmeticError('The native leading image is not the stated four-dimensional space.')
    # Each active source slice is exactly its matrix unit tensored with I4.
    for p, q in product([0, 2], repeat=2):
        block = [0]*64
        i, k = q//2, p//2
        for j in range(4):
            block[8*(4*i+j)+2*j+k] = 1
        if h0[4*p+q] != block:
            raise ArithmeticError('The exact leading matrix-unit identity failed.')
    position = {a: i for i, a in enumerate(kernel_indices)}
    endpoint_b, endpoint_c = [zeros(18, 12*8) for _ in range(2)]
    interior_b, interior_c = [zeros(18, 12*8) for _ in range(2)]
    for a, b, c, coefficient in terms:
        if a not in position:
            continue
        u = position[a]
        eb = endpoint_b if b < 14 else interior_b
        ec = endpoint_c if c < 14 else interior_c
        for j in range(8):
            eb[b][8*u+j] += coefficient*old_c[j][c]
            ec[c][8*u+j] += coefficient*old_b[j][b]
    supports = [[index for index, row in enumerate(matrix) if any(row)]
                for matrix in [endpoint_b, endpoint_c, interior_b, interior_c]]
    if supports != [[1, 3, 6, 8, 10, 13], [2, 3, 6, 7, 12, 13], [16, 17], [15, 17]]:
        raise ArithmeticError('A first-edge native support changed.')
    opposite_supports = [sorted({column % 8 for row in matrix
                                for column, value in enumerate(row) if value})
                         for matrix in [interior_b, interior_c]]
    if opposite_supports != [[1], [4]]:
        raise ArithmeticError('An interior first-edge opposite support is not a line.')
    # The target first-edge slice for a B-functional X is a direct sum of
    # two copies of the 2x4 matrix X, after fixed row/column permutations.
    edge_basis = []
    for i, j in product(range(2), range(4)):
        matrix = zeros(4, 8)
        for k in range(2):
            matrix[2*i+k][2*j+k] = 1
        reordered = [[matrix[2*i0+k0][2*j0+k1]
                      for k1, j0 in product(range(2), range(4))]
                     for k0, i0 in product(range(2), range(2))]
        expected = zeros(4, 8)
        for k in range(2):
            expected[2*k+i][4*k+j] = 1
        if reordered != expected:
            raise ArithmeticError('The target functional slice is not diag(X,X).')
        edge_basis.append(matrix)
    if any(len(rref(matrix)[1]) != 2 for matrix in edge_basis):
        raise ArithmeticError('A target edge matrix-unit functional has the wrong rank.')
    return {'source': 'R16x18x18 direct sum D2',
            'target_sought': 'M(4,4,4)',
            'fixed_leading_target': 'M(2,4,2)',
            'coefficient_field': 'Q, and the support proof over C',
            'source_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
            'native_R_terms_checked': 90,
            'leading_integer_rational_positions_checked': 4096,
            'leading_target_nonzero_positions': 16,
            'native_old_outer_indices': [0, 2],
            'native_leading_rank': 4,
            'native_K0_basis_indices': kernel_indices,
            'native_leading_image_minimum_nonzero_matrix_rank': 4,
            'endpoint_first_edge_native_B_support': supports[0],
            'endpoint_first_edge_native_C_support': supports[1],
            'interior_first_edge_native_B_support': supports[2],
            'interior_first_edge_native_C_support': supports[3],
            'interior_first_edge_old_C_support': opposite_supports[0],
            'interior_first_edge_old_B_support': opposite_supports[1],
            'target_first_edge_B_C_dimensions': [8, 8],
            'target_functional_slice_identity_checked_on_all_basis_coefficients': True,
            'target_first_edge_minimum_nonzero_functional_slice_rank': 2,
            'scalar_first_cross_vectors_required_on_each_side': 2,
            'scalar_old_product_span_dimensions_covered_in_proof': [0, 1, 2],
            'fixed_leading_maps_excluded_with_all_two_scalar_leading_placements': True,
            'free_edge_and_corner_A_subspaces_covered': True,
            'higher_coefficients_respecting_stated_lower_row_powers_covered': True,
            'arbitrary_border_D2_repair_excluded': False,
            'any_new_search_run': False,
            'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = report()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
