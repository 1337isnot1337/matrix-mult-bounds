"""Exact mixed-partner identities and compatible first-space witnesses."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS = ROOT / 'results/both-mixed-first-spaces-2026-10-21'
SPEC = importlib.util.spec_from_file_location('both_mixed_pencil', HERE.parent / '2026-10-21-mixed-first-jets/pencil_frontier.py')
pencil = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(pencil)
third = pencil.third
normal = third.normal
extension = third.extension


def zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix)


@lru_cache(None)
def data():
    canonical = normal.data()
    eb, ec = canonical['E_B_complement'], canonical['E_C_complement']
    left = extension.contract(eb[:12], ec[12:], extension.OUTSIDE)
    right = extension.contract(eb[12:], ec[:12], extension.OUTSIDE)
    rows_left = sorted({i for i, j in left.todok()})
    rows_right = sorted({i for i, j in right.todok()})
    if len(rows_left) != 12 or len(rows_right) != 12 or set(rows_left) & set(rows_right):
        raise ArithmeticError('The two mixed-boundary source supports are not disjoint twelve-frames')
    center = extension.OUTSIDE.index(extension.index(0, 0, 6))
    if center in rows_left+rows_right or any(extension.contract(eb[:12], ec[:12], extension.OUTSIDE)):
        raise ArithmeticError('Invalid central coordinate or nonzero boundary-by-boundary block')
    blocks_left = [left[rows_left, [4*b+k for b in range(12)]] for k in range(4)]
    blocks_right = [right[rows_right, 12*k:12*(k+1)] for k in range(4)]
    representations = []
    labels = ((1, 1), (0, 1), (1, 0), (0, 0))
    for blocks in (blocks_left, blocks_right):
        inverse = (blocks[0]+blocks[3]).inv()
        matrices = [block*inverse for block in blocks]
        for i, (a, b) in enumerate(labels):
            for j, (c, d) in enumerate(labels):
                expected = matrices[labels.index((a, d))] if b == c else sp.zeros(12)
                if matrices[i]*matrices[j] != expected:
                    raise ArithmeticError('The mixed boundary blocks are not the specified matrix units')
        representations.append(matrices)
    return {'B': eb, 'C': ec, 'L': rows_left, 'M': rows_right,
            'FL': representations[0], 'FM': representations[1],
            'mixed': extension.contract(eb[12:], ec[12:], extension.OUTSIDE),
            'center': center}


def adjugate_action(coefficients, representation):
    return ((coefficients[0]+coefficients[3])*sp.eye(12)
            - sum((coefficients[k]*representation[k] for k in range(4)), sp.zeros(12)))


def mixed_product(left, right):
    matrix = data()['mixed']
    return sp.Matrix(100, 1, lambda i, j:
        sum(matrix[i, 4*k+l]*left[k]*right[l] for k in range(4) for l in range(4)))


def verify_partner_identities():
    d = data()
    a, b, x, y = sp.symbols('a b x y')
    u = sp.Matrix(sp.symbols('u0:4'))
    v = sp.Matrix([a*b, b, a, 1])
    product = mixed_product(u, v)
    residual = adjugate_action(v, d['FL'])*product[d['L'], :]
    # These two equations force u=(-b*x,x,-b*y,y), uniformly in a,b.
    if sp.expand(residual[7]-(u[2]+b*u[3])) != 0:
        raise ArithmeticError('Incorrect first generic partner equation')
    if sp.expand(product[d['center']]-a*residual[7]-(u[0]+b*u[1])) != 0:
        raise ArithmeticError('Incorrect second generic partner equation')
    u = sp.Matrix([-b*x, x, -b*y, y])
    residual = adjugate_action(u, d['FM'])*mixed_product(u, v)[d['M'], :]
    if sp.expand(residual[1]+x*(x+a*y)) or sp.expand(residual[4]-y*(x+a*y)):
        raise ArithmeticError('Incorrect generic quadratic partner equations')
    # The remaining chart is v=e1; reversal also handles v=e2.
    v = sp.Matrix([0, 1, 0, 0])
    u = sp.Matrix(sp.symbols('u0:4'))
    product = mixed_product(u, v)
    residual = adjugate_action(v, d['FL'])*product[d['L'], :]
    if product[d['center']] != u[1] or residual[1] != -u[3]:
        raise ArithmeticError('Incorrect endpoint linear equations')
    u = sp.Matrix([x, 0, y, 0])
    residual = adjugate_action(u, d['FM'])*mixed_product(u, v)[d['M'], :]
    if sp.expand(residual[2]-x*x):
        raise ArithmeticError('Incorrect endpoint square equation')
    # This source automorphism takes v0 != 0 to the v3 != 0 chart.
    pencil.check_orbit_identities()
    for basis in (d['B'], d['C']):
        for k, row in enumerate(basis[12:]):
            flipped = {extension.index(3-j//28, 3-(j//7) % 4, 6-j % 7): value
                       for j, value in row.items()}
            if flipped != basis[15-k]:
                raise ArithmeticError('Source reversal does not reverse the four mixed coordinates')
    return {'generic_chart': 'v=(a*b,b,a,1)',
            'forced_partner': 'u is proportional to (v0,-v2,-v1,v3)',
            'generic_linear_equations': ['u2+b*u3=0', 'u0+b*u1=0'],
            'generic_quadratic_equations': ['x*(x+a*y)=0', 'y*(x+a*y)=0'],
            'endpoint': {'v': [0, 1, 0, 0], 'linear': ['u1=0', 'u3=0'], 'quadratic': 'u0^2=0'},
            'coverage': 'All nonzero complex rank-one v: v3 chart, reversed v0 chart, and two reversed coordinate endpoints.'}


def check_seed(path, expected_dimensions):
    seed = json.loads(path.read_text())
    encoded_b = seed.get('B_rows', seed.get('first_constant_B_new'))
    encoded_c = seed.get('C_rows', seed.get('first_constant_C_new'))
    left, right = third.verify.rows(encoded_b), third.verify.rows(encoded_c)
    if (len(left), len(right)) != expected_dimensions:
        raise ArithmeticError('Wrong first-space dimensions')
    mixed_ranks = []
    for side, rows in (('B', left), ('C', right)):
        expected = 4+len(rows)
        if third.verify.covector_rank(extension.G+rows) != expected:
            raise ArithmeticError('The first quotient rows are dependent')
        if third.verify.covector_rank(extension.G+data()[side]+rows) != 20:
            raise ArithmeticError('A first row lies outside the canonical extension')
        basis = normal.row_matrix(extension.G+data()[side]).T
        coordinates = basis.gauss_jordan_solve(normal.row_matrix(rows).T)[0][16:, :]
        if third.matrix_rank(coordinates) != 1:
            raise ArithmeticError('The example does not have a nonzero mixed line')
        vector = next(coordinates[:, i] for i in range(coordinates.cols) if any(coordinates[:, i]))
        mixed_rank = 1 if vector[0]*vector[3] == vector[1]*vector[2] else 2
        if mixed_rank != (1 if expected_dimensions == (7, 7) else 2):
            raise ArithmeticError('Wrong mixed matrix-rank stratum')
        mixed_ranks.append(mixed_rank)
    if any(extension.contract(left, right, extension.OUTSIDE)):
        raise ArithmeticError('The corrected mixed first spaces do not annihilate H')
    p0, q0 = extension.G+[{} for _ in left], extension.G+[{} for _ in right]
    p1, q1 = [{} for _ in range(4)]+left, [{} for _ in range(4)]+right
    coefficients = [third.verify.contract(p0, q0),
                    third.verify.add((1, third.verify.contract(p1, q0)),
                                     (1, third.verify.contract(p0, q1))),
                    third.verify.contract(p1, q1)]
    for i, tensor in enumerate(coefficients):
        third.verify.check_kernel(f'exact first-space polynomial coefficient {i}', tensor)
    cross = third.first_constraints({'first_constant_B_new': encoded_b,
                                     'first_constant_C_new': encoded_c})
    return {'first_quotient_dimensions': list(expected_dimensions),
            'mixed_projection_dimensions': [1, 1],
            'mixed_matrix_ranks': mixed_ranks,
            'active_output_dimensions': [4+len(left), 4+len(right)],
            'complete_polynomial_coefficients_checked': 3,
            'normal_dimension_after_off_diagonal_equations': 228-third.matrix_rank(cross),
            'scope': 'Compatible first spaces and an exact polynomial identity with first rank twelve; not a matrix target.'}


@lru_cache(None)
def report():
    return {'field': 'Q polynomial identities, valid over C',
            'matrix_unit_products_checked': 32,
            'partner_identities': verify_partner_identities(),
            'seven_by_seven_control': check_seed(RESULTS / 'seven-seven-seed.json', (7, 7)),
            'invertible_line_control': check_seed(RESULTS / 'invertible-lines-seed.json', (1, 1)),
            'consequence': 'With both mixed projections nonzero, both are lines: either rank-one partners with quotient ranks <=7 each, or invertible lines with quotient ranks exactly1 each.',
            'independent_review': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
