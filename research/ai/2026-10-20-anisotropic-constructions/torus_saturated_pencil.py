"""Exact cube determinant in the saturated degree-13 source pencil.

This is a finite replay of torus_saturated_pencil.md, not a search result.
"""

import importlib.util
from itertools import permutations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUTPUT = ROOT / 'results/anisotropic-constructions-2026-10-20/torus-saturated-pencil.json'
SPEC = importlib.util.spec_from_file_location('degree13_pencil_controls', HERE / 'torus_degree13_pencils.py')
POLY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(POLY)


def determinant(matrix):
    result = {}
    for permutation in permutations(range(3)):
        sign = (-1) ** sum(permutation[i] > permutation[j]
                           for i in range(3) for j in range(i + 1, 3))
        term = {(): sign}
        for i in range(3):
            term = POLY.multiply(term, matrix[i][permutation[i]])
        result = POLY.add(result, term)
    return result


def report():
    a, h, v, w = (POLY.variable(name) for name in ('a', 'h', 'v', 'w'))
    matrix = [[v, h, a], [a, {}, {}], [w, a, {}]]
    expected = {('a', 'a', 'a'): 1}
    if determinant(matrix) != expected:
        raise ArithmeticError('The universal source determinant is not a cubed boundary coefficient')
    coordinate_checks = 0
    for left_basis, right_basis, grid in (
        (POLY.NEGATIVE, POLY.POSITIVE, POLY.NEGATIVE_GRID),
        (POLY.POSITIVE, POLY.NEGATIVE, POLY.POSITIVE_GRID),
    ):
        for i, j in product(range(3), repeat=2):
            actual = POLY.trace_form(left_basis[i], right_basis[j])
            wanted = {} if grid[i][j] is None else {grid[i][j]: 1}
            if actual != wanted:
                raise ArithmeticError('A source product table changed')
            coordinate_checks += 1
    # Use distinct bases of the three vertex spaces. Low endpoints have
    # dimension one; the intermediate charge-13 space has two vertices.
    negative = ((0, 13), (0, 14), (1, 15))
    positive = ((13, 0), (14, 0), (15, 1))
    target = [[int(POLY.target_trace_coordinate(left, right) == (0, 0))
               for right in positive] for left in negative]
    if target != [[1, 0, 0], [0, 1, 0], [0, 0, 0]]:
        raise ArithmeticError('The intermediate two-channel target slice is incorrect')
    # Exercise arbitrary nonzero scalar values and other source coefficients.
    exact_specializations = 0
    for av, hv, vv, wv in product((-3, -1, 1, 2), (-2, 0, 3), (0, 4), (-5, 1)):
        numbers = [[vv, hv, av], [av, 0, 0], [wv, av, 0]]
        actual_det = sum(((-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)))
                         * numbers[0][p[0]] * numbers[1][p[1]] * numbers[2][p[2]]
                         for p in permutations(range(3)))
        if actual_det != av ** 3 or actual_det == 0:
            raise ArithmeticError('An arbitrary-scalar source slice failed the rank-three check')
        exact_specializations += 1
    return {
        'source': 'A(8,8)',
        'map_scope': 'ordinary grading-preserving restrictions with the stated saturated adjacent blocks',
        'ordered_source_products_checked': coordinate_checks,
        'formal_source_determinant': 'a^3 (negative then positive), b^3 (positive then negative)',
        'arbitrary_nonzero_scalar_specializations_checked': exact_specializations,
        'required_target_test_slice': target,
        'source_test_slice_rank': 3,
        'target_test_slice_rank': 2,
        'extreme_scalars_normalized': False,
        'all_nonempty_neighbor_corollary': 'If every vertex list has positive multiplicities at 0,1,13,14 and no outside charges, all four multiplicities must equal one.',
        'neighbor_holes_excluded': False,
        'singular_limits_excluded': False,
        'new_exponent_established': False,
    }


if __name__ == '__main__':
    data = report()
    OUTPUT.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'output': str(OUTPUT), **data}, indent=2))
