"""Exact finite ingredients of the stated degree-13 pencil obstruction.

The universal conclusion also uses the written two-leg rank-chain theorem.
This program does not substitute finite examples for that theorem.
All arithmetic and polynomial identities use the Python standard library.
"""

from collections import Counter
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-degree13-pencils.json'
NEGATIVE = ((0, 13, 0), (0, 14, 1), (1, 14, 0))
POSITIVE = ((7, 1, 7), (7, 0, 6), (6, 0, 7))
MINUS_EXTREME = (0, 14, 0)
PLUS_EXTREME = (7, 0, 7)
NEGATIVE_GRID = (
    ((1, 7, 6), (0, 6, 6), (0, 7, 7)),
    ((0, 7, 7), None, None),
    ((1, 8, 7), (0, 7, 7), None),
)
POSITIVE_GRID = (
    ((6, 7, 1), (7, 8, 1), (7, 7, 0)),
    ((7, 7, 0), None, None),
    ((6, 6, 0), (7, 7, 0), None),
)


def source_matrix(point):
    """Sparse physical entries (row_i,row_q,column_p,column_s)."""
    i, k, s = point
    if not (0 <= i < 8 and 0 <= k < 15 and 0 <= s < 8):
        raise ValueError('Source coordinate is outside A(8,8)')
    return {(i, q, k - q, s): 1 for q in range(8) if 0 <= k - q < 8}


def trace_form(left, right):
    """Return every coefficient of F in tr(W(left) W(right) W(F))."""
    result = Counter()
    for (i, q, p, s), x in source_matrix(left).items():
        for (j, t, r, u), y in source_matrix(right).items():
            if (p, s) == (j, t):
                # The product entry is ((i,q),(r,u)); reverse it for trace.
                result[r, i + u, q] += x * y
    return {point: value for point, value in result.items() if value}


def unit_product(left, right):
    return (left[0], right[1]) if left[1] == right[0] else None


def target_trace_coordinate(left, right):
    value = unit_product(left, right)
    return None if value is None else (value[1], value[0])


def verify_product_grids(negative_grid=NEGATIVE_GRID, positive_grid=POSITIVE_GRID):
    source_points = tuple(product(range(8), range(15), range(8)))
    weight_sets = {
        w: {point for point in source_points if point[0] + point[2] - point[1] == w}
        for w in (-14, -13, 13, 14)
    }
    if weight_sets[-13] != set(NEGATIVE) or weight_sets[13] != set(POSITIVE):
        raise ArithmeticError('A degree-13 source basis is incomplete')
    if weight_sets[-14] != {MINUS_EXTREME} or weight_sets[14] != {PLUS_EXTREME}:
        raise ArithmeticError('An extreme source block is not the asserted line')
    checks = 0
    for left_basis, right_basis, expected in (
        (NEGATIVE, POSITIVE, negative_grid),
        (POSITIVE, NEGATIVE, positive_grid),
    ):
        for i, left in enumerate(left_basis):
            for j, right in enumerate(right_basis):
                actual = trace_form(left, right)
                wanted = {} if expected[i][j] is None else {expected[i][j]: 1}
                for point in source_points:
                    if actual.get(point, 0) != wanted.get(point, 0):
                        raise ArithmeticError('A universal product-grid coefficient is incorrect')
                    checks += 1
    if trace_form(MINUS_EXTREME, PLUS_EXTREME) != {(0, 7, 7): 1}:
        raise ArithmeticError('The negative-positive extreme product is incorrect')
    if trace_form(PLUS_EXTREME, MINUS_EXTREME) != {(7, 7, 0): 1}:
        raise ArithmeticError('The positive-negative extreme product is incorrect')
    return {
        'source_basis_coordinates': len(source_points),
        'degree_13_ordered_products': 18,
        'product_grid_coefficients_checked': checks,
        'extreme_products_checked': 2,
        'negative_grid': negative_grid,
        'positive_grid': positive_grid,
    }


def verify_endpoint_projections():
    """Check the four physical projections and the target covectors they contain."""
    v, u = (0, 7), (7, 0)

    def right_column(point, endpoint):
        return {(i, q): value for (i, q, p, s), value in source_matrix(point).items()
                if (p, s) == endpoint}

    def left_row(endpoint, point):
        return {(p, s): value for (i, q, p, s), value in source_matrix(point).items()
                if (i, q) == endpoint}

    cases = (
        ('A', [right_column(point, u) for point in NEGATIVE],
         [{(0, 6): 1}, {}, {(1, 7): 1}], (0, 1), 'p,r'),
        ('B', [left_row(v, point) for point in NEGATIVE],
         [{(6, 0): 1}, {(7, 1): 1}, {}], (1, 0), 'p,q'),
        ('C', [left_row(u, point) for point in POSITIVE],
         [{(1, 7): 1}, {(0, 6): 1}, {}], (0, 1), 's,t'),
        ('D', [right_column(point, v) for point in POSITIVE],
         [{(7, 1): 1}, {}, {(6, 0): 1}], (1, 0), 's,u'),
    )
    for _, actual, expected, _, _ in cases:
        if actual != expected:
            raise ArithmeticError('An endpoint projection has the wrong physical channels')
    n1, n2, p1, p2 = (0, 25), (1, 26), (25, 0), (26, 1)
    eplus, eminus = (26, 0), (0, 26)
    products = (
        (unit_product(n1, eplus), unit_product(n2, eplus)),
        (unit_product(eplus, n1), unit_product(eplus, n2)),
        (unit_product(eminus, p1), unit_product(eminus, p2)),
        (unit_product(p1, eminus), unit_product(p2, eminus)),
    )
    expected_products = ((None, (1, 0)), ((26, 25), None),
                         (None, (0, 1)), ((25, 26), None))
    if products != expected_products:
        raise ArithmeticError('An endpoint target covector is incorrect')
    return [{'type': name, 'projection_columns': columns,
             'target_covector_in_column_span': list(covector)}
            for name, _, _, covector, columns in cases]


# Small exact commutative polynomial operations; a monomial is a sorted tuple.
def variable(name):
    return {(name,): 1}


def add(*polynomials):
    result = Counter()
    for polynomial in polynomials:
        result.update(polynomial)
    return {monomial: value for monomial, value in result.items() if value}


def scale(polynomial, scalar):
    return {monomial: scalar * value for monomial, value in polynomial.items()
            if scalar * value}


def multiply(left, right):
    result = Counter()
    for ml, cl in left.items():
        for mr, cr in right.items():
            result[tuple(sorted(ml + mr))] += cl * cr
    return {monomial: value for monomial, value in result.items() if value}


def determinant(left, right):
    return add(multiply(left[0], right[1]), scale(multiply(left[1], right[0]), -1))


def outer(left, right):
    return [[multiply(x, y) for y in right] for x in left]


def matrix_add(*matrices):
    return [[add(*(matrix[i][j] for matrix in matrices)) for j in range(2)]
            for i in range(2)]


def annihilate(left_pivot, right_pivot, matrix):
    left = (scale(left_pivot[1], -1), left_pivot[0])
    right = (scale(right_pivot[1], -1), right_pivot[0])
    return add(*(multiply(multiply(left[i], matrix[i][j]), right[j])
                 for i, j in product(range(2), repeat=2)))


def verify_generic_identities():
    p, q, r, s, t, u = [tuple(variable(name + str(i)) for i in (1, 2))
                        for name in 'pqrstu']
    checked = 0
    for left, right, free_terms, boundary_terms, expected in (
        (p, s, (outer(p, s), outer(p, t), outer(r, s)),
         (outer(p, u), outer(q, s), outer(r, t)),
         multiply(determinant(p, r), determinant(s, t))),
        (s, p, (outer(s, p), outer(s, q), outer(u, p)),
         (outer(s, r), outer(t, p), outer(u, q)),
         multiply(determinant(s, u), determinant(p, q))),
    ):
        for term in free_terms:
            if annihilate(left, right, term):
                raise ArithmeticError('The missing-direction functional does not kill a free term')
            checked += 1
        if annihilate(left, right, matrix_add(*boundary_terms)) != expected:
            raise ArithmeticError('The boundary determinant identity is incorrect')
        checked += 1
        z0, z1 = variable('z0'), variable('z1')
        diagonal = [[z0, {}], [{}, z1]]
        wanted = add(multiply(multiply(left[1], right[1]), z0),
                     multiply(multiply(left[0], right[0]), z1))
        if annihilate(left, right, diagonal) != wanted:
            raise ArithmeticError('The target diagonal missing-direction identity is incorrect')
        checked += 1
    return {'formal_polynomial_identities_checked': checked,
            'extreme_scalar_values_normalized': False,
            'negative_pair_nonzero_coordinates': ['p2', 's2'],
            'negative_pair_zero_product': 'p1*s1',
            'positive_pair_nonzero_coordinates': ['s1', 'p1'],
            'positive_pair_zero_product': 's2*p2'}


def verify_cross_types():
    # The third source boundary functional is forced to the listed target
    # diagonal, up to a nonzero scalar. Different diagonals remain independent.
    cases = (
        ('A_then_C', NEGATIVE[1], POSITIVE[2], (0, 25), (25, 0), None),
        ('C_then_A', POSITIVE[2], NEGATIVE[1], (25, 0), (0, 25), (26, 26)),
        ('B_then_D', NEGATIVE[2], POSITIVE[1], (1, 26), (26, 1), (0, 0)),
        ('D_then_B', POSITIVE[1], NEGATIVE[2], (26, 1), (1, 26), None),
    )
    boundary = {(0, 7, 7): (0, 0), (7, 7, 0): (26, 26)}
    result = []
    for name, left, right, target_left, target_right, expected_boundary in cases:
        source = trace_form(left, right)
        if len(source) > 1 or any(value != 1 for value in source.values()):
            raise ArithmeticError('A mixed singular product is not zero or one boundary coordinate')
        source_target = None if not source else boundary[next(iter(source))]
        required = target_trace_coordinate(target_left, target_right)
        if source_target != expected_boundary or required is None or source_target == required:
            raise ArithmeticError('A cross-type target contradiction failed')
        result.append({'ordered_types': name, 'forced_target_diagonal': source_target,
                       'required_independent_target_diagonal': required})
    return result


def verify_double_singular():
    # These four complete rows of the product grids give the two direct proofs.
    if [trace_form(NEGATIVE[1], point) for point in POSITIVE] != [
            {(0, 7, 7): 1}, {}, {}]:
        raise ArithmeticError('The negative double-singular offdiagonal equation failed')
    if [trace_form(NEGATIVE[2], point) for point in POSITIVE] != [
            {(1, 8, 7): 1}, {(0, 7, 7): 1}, {}]:
        raise ArithmeticError('The negative double-singular diagonal equation failed')
    if [trace_form(POSITIVE[1], point) for point in NEGATIVE] != [
            {(7, 7, 0): 1}, {}, {}]:
        raise ArithmeticError('The positive double-singular offdiagonal equation failed')
    if [trace_form(POSITIVE[2], point) for point in NEGATIVE] != [
            {(6, 6, 0): 1}, {(7, 7, 0): 1}, {}]:
        raise ArithmeticError('The positive double-singular diagonal equation failed')
    return {
        'complete_product_rows_checked': 4,
        'A_and_B': {'offdiagonal_equation': 'q1*s2*a=0',
                    'forced_zero_coordinate': 's2',
                    'remaining_diagonal_equation': 'r2*t2*a=z11',
                    'a_is_nonzero_multiple_of': 'z00'},
        'C_and_D': {'offdiagonal_equation': 't2*p1*b=0',
                    'forced_zero_coordinate': 'p1',
                    'remaining_diagonal_equation': 'u1*q1*b=z25,25',
                    'b_is_nonzero_multiple_of': 'z26,26'},
    }


def cross_types_allowed(pattern):
    a, b, c, d = pattern
    return not ((a >= 0 and c >= 0 and a != c) or
                (b >= 0 and d >= 0 and b != d))


def generic_implications_allowed(pattern):
    a, b, c, d = pattern
    for i in range(3):
        j = (i + 1) % 3
        if (b == i or d == j) and not (a == i or c == j):
            return False
        if (c == i or a == j) and not (d == i or b == j):
            return False
    return True


def pattern_report():
    candidates = list(product(range(-1, 3), repeat=4))
    after_cross = [p for p in candidates if cross_types_allowed(p)]
    survivors = [p for p in after_cross if generic_implications_allowed(p)]
    expected = {(-1, -1, -1, -1)}
    for i in range(3):
        expected.update(((i, i, -1, -1), (-1, -1, i, i), (i, i, i, i)))
    if set(survivors) != expected:
        raise ArithmeticError('The cyclic singular-pattern classification changed')
    classified = []
    for pattern in survivors:
        a, b, c, d = pattern
        if pattern == (-1, -1, -1, -1):
            reason = 'all_generic_opposite_pair_contradiction'
        elif a == b and a >= 0:
            reason = 'negative_double_singular_contradiction'
        elif c == d and c >= 0:
            reason = 'positive_double_singular_contradiction'
        else:
            raise ArithmeticError('An unexcluded pattern survived')
        classified.append({'locations_A_B_C_D': list(pattern), 'contradiction': reason})
    return {
        'type_location_choices': len(candidates),
        'after_cross_type_exclusions': len(after_cross),
        'after_generic_pair_implications': len(survivors),
        'classified_survivors': classified,
        'patterns_after_all_contradictions': 0,
        'at_most_one_leg_per_type_dependency': 'parity_balancing_rankone_13_chain.md and symmetry addendum',
    }


def report():
    result = {
        'source': 'A(8,8)',
        'target': 'M27 direct_sum M7',
        'common_M27_charge_multiplicities': [1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1],
        'common_M7_charge_multiplicities': [1] * 7,
        'map_scope': 'ordinary maps preserving the specified integer grading on all three legs',
        'product_grids': verify_product_grids(),
        'endpoint_projections': verify_endpoint_projections(),
        'generic_pair_identities': verify_generic_identities(),
        'cross_type_contradictions': verify_cross_types(),
        'double_singular_contradictions': verify_double_singular(),
        'cyclic_pattern_enumeration': pattern_report(),
        'written_proof_excludes_specified_ordinary_torus_profile': True,
        'other_torus_profiles_excluded': False,
        'arbitrary_singular_limits_excluded': False,
        'new_exponent_established': False,
    }
    # Return the same list representation before and after JSON serialization.
    return json.loads(json.dumps(result))


if __name__ == '__main__':
    data = report()
    OUTPUT.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'output': str(OUTPUT),
                      'product_coefficients_checked': data['product_grids']['product_grid_coefficients_checked'],
                      'patterns': data['cyclic_pattern_enumeration'],
                      'new_exponent_established': False}, indent=2))
