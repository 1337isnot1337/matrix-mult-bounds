"""Uniform normal-rank certificate for all maximal rank-one mixed pairs."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('rankone_seven_both', HERE.parent / '2026-10-21-both-mixed-first-spaces/verify.py')
both = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(both)
normal, extension, third = both.normal, both.extension, both.third
A, B = sp.symbols('a b')


def zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix.todok().values())


def chart_frames():
    left, right = sp.zeros(16, 7), sp.zeros(16, 7)
    for j in range(6):
        left[2*j, j], left[2*j+1, j] = -B, 1
        right[2*j, j], right[2*j+1, j] = A, 1
    left[12:, 6] = sp.Matrix([A*B, -A, -B, 1])
    right[12:, 6] = sp.Matrix([A*B, B, A, 1])
    return left, right


def covectors(coordinates, basis):
    return [{j: sp.expand(sum(coordinates[k, col]*basis[k].get(j, 0) for k in range(16)))
             for j in range(112)
             if sum(coordinates[k, col]*basis[k].get(j, 0) for k in range(16))}
            for col in range(coordinates.cols)]


def constraints(left, right):
    data = normal.data()
    blocks = []
    for side, coordinates in (('left', left), ('right', right)):
        obstruction = data[f'{side}_obstruction']
        for col in range(coordinates.cols):
            block = sp.MutableSparseMatrix.zeros(200, 228)
            for j in range(16):
                if coordinates[j, col]:
                    block += coordinates[j, col]*obstruction[200*j:200*(j+1), :]
            blocks.append(block)
    return sp.MutableSparseMatrix.vstack(*blocks)


def plane_parameters():
    data = normal.data()
    plane = sp.Matrix.hstack(*(sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
                              for rows in normal.plane_directions()))
    return sp.MutableSparseMatrix(plane[normal.NORMAL, :][data['free'], :])


def triangular_order(matrix):
    adjacency = [set() for _ in range(matrix.rows)]
    degrees = [0]*matrix.rows
    for i, j in matrix.todok():
        adjacency[i].add(j)
        degrees[j] += 1
    queue = [i for i, degree in enumerate(degrees) if not degree]
    order = []
    while queue:
        i = queue.pop()
        order.append(i)
        for j in sorted(adjacency[i]):
            degrees[j] -= 1
            if not degrees[j]:
                queue.append(j)
    verify_triangular_order(matrix, order)
    return order


def verify_triangular_order(matrix, order):
    if sorted(order) != list(range(matrix.rows)):
        raise ArithmeticError('The polynomial support is not acyclic')
    position = {i: j for j, i in enumerate(order)}
    if any(position[i] >= position[j] for i, j in matrix.todok()):
        raise ArithmeticError('An asserted strictly triangular entry is not above the diagonal')


@lru_cache(None)
def chart_data():
    left, right = chart_frames()
    data = normal.data()
    unit_rows = [1, 3, 5, 7, 9, 11, 15]
    if left[unit_rows, :] != sp.eye(7) or right[unit_rows, :] != sp.eye(7):
        raise ArithmeticError('The chart frame loses rank at a parameter value')
    rows_b = covectors(left, data['E_B_complement'])
    rows_c = covectors(right, data['E_C_complement'])
    if not zero(extension.contract(rows_b, rows_c, extension.OUTSIDE)):
        raise ArithmeticError('The polynomial first-space pair is incompatible')
    matrix = constraints(left, right)
    base = matrix.subs({A: 0, B: 0})
    certificate = third.rank_certificate(base)
    if certificate['rational_rank'] != 224:
        raise ArithmeticError('Unexpected chart base rank')
    rr, cc = certificate['minor_rows'], certificate['minor_columns']
    normalized = (base[rr, cc].inv()*matrix[rr, cc]-sp.eye(224)).applyfunc(sp.expand)
    order = triangular_order(normalized)
    plane = plane_parameters()
    if third.matrix_rank(plane) != 4 or not zero(matrix*plane):
        raise ArithmeticError('The common-plane parameters are not the full four-kernel')
    return {'matrix': matrix, 'base_certificate': certificate, 'normalized': normalized,
            'order': order, 'left_rows': rows_b, 'right_rows': rows_c}


def endpoint_frames():
    data = normal.data()
    eb, ec = data['E_B_complement'], data['E_C_complement']
    u, v = sp.Matrix([0, 0, -1, 0]), sp.Matrix([0, 1, 0, 0])
    left, right = sp.zeros(16, 7), sp.zeros(16, 7)
    left[12:, 6], right[12:, 6] = u, v
    ub, vc = covectors(left[:, 6:], eb), covectors(right[:, 6:], ec)
    hb = extension.contract(eb[:12], vc, extension.OUTSIDE)
    hc = extension.contract(ub, ec[:12], extension.OUTSIDE)
    left[:12, :6] = normal.sparse_nullspace(hb)[0]
    right[:12, :6] = normal.sparse_nullspace(hc)[0]
    if not zero(extension.contract(covectors(left, eb), covectors(right, ec), extension.OUTSIDE)):
        raise ArithmeticError('The exceptional endpoint pair is incompatible')
    return left, right


@lru_cache(None)
def report():
    data = chart_data()
    endpoint = constraints(*endpoint_frames())
    endpoint_certificate = third.rank_certificate(endpoint)
    if endpoint_certificate['rational_rank'] != 224 or not zero(endpoint*plane_parameters()):
        raise ArithmeticError('The exceptional endpoint normal kernel changed')
    both.pencil.check_orbit_identities()
    return {'field': 'Polynomial identities over Q[a,b], valid for every a,b in C',
            'chart': 'v=(a*b,b,a,1), u=(a*b,-a,-b,1)',
            'first_quotient_dimensions': [7, 7], 'normal_constraint_shape': [2800, 228],
            'chart_base_rank_certificate': data['base_certificate'],
            'normalized_minor_size': 224, 'normalized_minor_is_identity_plus_strictly_triangular': True,
            'normalized_nonzero_polynomial_entries': [[i, j, str(value)]
                                                      for (i, j), value in data['normalized'].todok().items()],
            'triangular_order': data['order'], 'minor_prime': extension.PRIME,
            'exceptional_endpoint': {'v': [0, 1, 0, 0], 'rank_certificate': endpoint_certificate},
            'uniform_normal_rank': 224, 'kernel_dimension': 4,
            'kernel_is_common_plane_directions': True,
            'coverage': 'v3 nonzero chart, its source-reversed v0 nonzero chart, and the two reversed endpoints with v0=v3=0.',
            'scope': 'Exact all-parameter normal lemma. The all-order target exclusion uses the written moving-plane induction, not a finite numerical rank inference.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
