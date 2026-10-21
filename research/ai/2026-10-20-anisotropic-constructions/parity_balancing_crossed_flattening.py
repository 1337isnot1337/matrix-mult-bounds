"""Exact controls for the crossed-module four-factor flattening.

The identity/product branch has rank45 per source copy; the transpose
branch has rank32. The arbitrary-first-map exclusion uses the separate
rank-one slice normalization and is asserted only for ordinary maps.
"""

import argparse
from itertools import product
import json
from pathlib import Path


def source_terms(copies):
    return [(2 * i + u, 40 * e + 8 * (a + u) + j, 36 * e + 9 * a + j + i, 1)
            for e, i, u, a, j in product(range(copies), range(2), range(2), range(4), range(8))]


def flatten(terms, ny, nz, transpose=False):
    matrix = [[0] * (2 * nz) for _ in range(2 * ny)]
    for x, y, z, value in terms:
        i, u = divmod(x, 2)
        if transpose:
            i, u = u, i
        matrix[i * ny + y][u * nz + z] += value
    return matrix


def rank_modulo(matrix, prime=65521):
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((row for row in range(rank, len(rows)) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [value * inverse % prime for value in rows[rank]]
        for row in range(rank + 1, len(rows)):
            if rows[row][column]:
                factor = rows[row][column]
                rows[row] = [(a - factor * b) % prime for a, b in zip(rows[row], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def verify_factorization(terms, copies, transpose=False):
    matrix = flatten(terms, 40 * copies, 36 * copies, transpose)
    entries = 0
    for row, values in enumerate(matrix):
        first, y = divmod(row, 40 * copies)
        ey, y = divmod(y, 40)
        ell, j = divmod(y, 8)
        for column, actual in enumerate(values):
            second, z = divmod(column, 36 * copies)
            ez, z = divmod(z, 36)
            a, h = divmod(z, 9)
            i, u = (second, first) if transpose else (first, second)
            expected = int(ey == ez and ell == a + u and h == j + i)
            if actual != expected:
                raise ArithmeticError('The actual flattening does not have the claimed tensor-product factors')
            entries += 1
    expected_rank = copies * (32 if transpose else 45)
    if rank_modulo(matrix) != expected_rank:
        raise ArithmeticError('The exact factor ranks and modular rank disagree')
    return {'copies': copies, 'transpose_first_leg': transpose,
            'matrix_shape': [len(matrix), len(matrix[0])],
            'all_factor_coefficients_checked': entries, 'rank': expected_rank}


def verify_target(r):
    terms = [(2 * i + u, u * r + alpha, i * r + alpha, 1)
             for i, u, alpha in product(range(2), range(2), range(r))]
    matrix = flatten(terms, 2 * r, 2 * r)
    if any(sum(row) != 1 for row in matrix) or any(sum(row[column] for row in matrix) != 1 for column in range(4 * r)):
        raise ArithmeticError('The target flattening is not a permutation matrix')
    return {'middle_dimension': r, 'permutation_matrix_size': 4 * r, 'rank': 4 * r}


def full_source_fixed_first_control():
    """Enumerate original A88 terms, then compare the compact flattening."""
    first = {(i, 2 * p + t, 2 * u): (2 * i + t, 2 * p + u)
             for i, t, p, u in product(range(2), repeat=4)}
    actual = {}
    original_terms = 0
    for i, p_source, rr, j, q_source, s in product(range(8), repeat=6):
        original_terms += 1
        labels = first.get((i, p_source + q_source, s))
        if labels is None:
            continue
        left, right = labels
        long_y, long_z = rr + s, i + j
        if not (p_source < 4 and q_source < 4 and long_y < 10 and long_z < 9):
            raise ArithmeticError('A contributing full-source coordinate escaped the compact support')
        ey, ell = long_y % 2, long_y // 2
        ez, aa = rr % 2, rr // 2
        compact_y = 80 * p_source + 40 * ey + 8 * ell + j
        compact_z = 72 * q_source + 36 * ez + 9 * aa + long_z
        point = (left * 320 + compact_y, right * 288 + compact_z)
        actual[point] = actual.get(point, 0) + 1
    expected = {}
    j4_terms = [(2 * t + p, a, b, 1)
                for t, p, a, b in product(range(2), range(2), range(4), range(4))
                if a + b == 2 * p + t]
    for first_j, source_p, source_q, coefficient_j in j4_terms:
        t, p = divmod(first_j, 2)
        for first_r, source_y, source_z, coefficient_r in source_terms(2):
            i, u = divmod(first_r, 2)
            row = (2 * i + t) * 320 + 80 * source_p + source_y
            column = (2 * p + u) * 288 + 72 * source_q + source_z
            point = row, column
            expected[point] = expected.get(point, 0) + coefficient_j * coefficient_r
    if actual != expected:
        raise ArithmeticError('The original full-source flattening is not J4 tensor the matched module')
    j4_matrix = flatten(j4_terms, 4, 4)
    if rank_modulo(j4_matrix) != 4:
        raise ArithmeticError('The small J4 factor rank changed')
    # The four independent rows have the indicated identity minor. All
    # other rows are zero or repeated rows, so this also proves the rank
    # directly over the integers.
    rows, columns = (0, 1, 2, 4), (0, 5, 4, 1)
    minor = [[j4_matrix[row][column] for column in columns] for row in rows]
    if minor != [[int(i == j) for j in range(4)] for i in range(4)]:
        raise ArithmeticError('The J4 integer identity minor changed')
    if any(row != [0] * 8 and row not in [j4_matrix[i] for i in rows] for row in j4_matrix):
        raise ArithmeticError('An extra independent J4 row appeared')
    return {'original_A88_terms_checked': original_terms,
            'contributing_original_terms': sum(actual.values()),
            'compact_source_format': [16, 320, 288],
            'full_flattening_shape': [1280, 1152], 'J4_factor_rank': 4,
            'matched_factor_rank': 90, 'full_flattening_rank': 360,
            'target_M4_4_r_flattening_rank': '16*r',
            'fixed_first_images_middle_bound': 22,
            'other_two_maps_arbitrary': True,
            'fixed_first_images': 'E_(i,t),(p,u) maps to F(i,2*p+t,2*u)',
            'unrestricted_first_map_exclusion_claimed': False}


def verify():
    records = [verify_factorization(source_terms(copies), copies, transpose)
               for copies, transpose in product((1, 2), (False, True))]
    targets = [verify_target(r) for r in (11, 14, 22, 27)]
    slice_controls = []
    for copies in (1, 2):
        for active in ({0}, {0, 3}):
            matrix = [[0] * (36 * copies) for _ in range(40 * copies)]
            for x, y, z, value in source_terms(copies):
                if x in active:
                    matrix[y][z] += value
            expected_rank = copies * (32 if len(active) == 1 else 36)
            if rank_modulo(matrix) != expected_rank:
                raise ArithmeticError('The slice normal-form rank changed')
            slice_controls.append({'copies': copies, 'active_first_coefficients': sorted(active),
                                   'rank': expected_rank})
    sheared = source_terms(1)
    sheared += [(0, y, z, value) for x, y, z, value in source_terms(1) if x == 3]
    shear_rank = rank_modulo(flatten(sheared, 40, 36))
    if shear_rank <= 45:
        raise ArithmeticError('The non-product first-map scope control changed')
    return {'claim_id': 'AI-CROSSED-FLAT-104', 'arithmetic': 'integer factor identities and exact prime-field ranks',
            'source_flattenings': records, 'target_flattenings': targets,
            'slice_normal_forms': slice_controls,
            'full_source_fixed_first_control': full_source_fixed_first_control(),
            'product_branch_middle_bounds': {'one_copy': 11, 'two_copies': 22},
            'transpose_branch_middle_bounds': {'one_copy': 8, 'two_copies': 16},
            'ordinary_first_map_normalization': [
                {'copies': 1, 'middle_dimension': 14, 'rank_one_lift_budget': 34,
                 'rank_two_source_slice': 36, 'product_bound': 11, 'transpose_bound': 8},
                {'copies': 2, 'middle_dimension': 27, 'rank_one_lift_budget': 71,
                 'rank_two_source_slice': 72, 'product_bound': 22, 'transpose_bound': 16}],
            'non_product_first_map_scope_control_rank': shear_rank,
            'arbitrary_ordinary_two_copy_M2_2_27_excluded': True,
            'arbitrary_singular_first_map_exclusion_claimed': False,
            'full_source_A88_M27_plus_M7_excluded': False,
            'new_exponent_established': False, 'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = verify()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
