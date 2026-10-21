"""Independent physical-matrix controls for the affine slice builder.

The non-square A(3,4) control uses a complete exact M3 and denominator
three.  Every normalized affine coefficient is reconstructed by exact
physical matrix traces, separately from the builder's six-index source
loop.  No numerical library is required.
"""

from copy import deepcopy
from itertools import product
import json
from math import gcd
from pathlib import Path

import torus_affine_slices as affine


HERE = Path(__file__).resolve().parent
A, B, LONG, DIM = 3, 4, 6, 72


def encode(leg, i, middle, s):
    return ((i * LONG + middle) * B + s,
            (s * A + i) * LONG + middle,
            (middle * B + s) * A + i)[leg]


def decode(leg, column):
    if leg == 0:
        im, s = divmod(column, B)
        i, middle = divmod(im, LONG)
    elif leg == 1:
        si, middle = divmod(column, LONG)
        s, i = divmod(si, A)
    else:
        ms, i = divmod(column, A)
        middle, s = divmod(ms, B)
    return i, middle, s


def common(leg, column):
    return encode(0, *decode(leg, column))


def build_control():
    vertices = [(0, 3), (1, 2), (2, 0)]
    maps = [[], [], []]
    for row, (u, v) in enumerate(product(range(3), repeat=2)):
        i, q = vertices[u]
        p, s = vertices[v]
        for leg in range(3):
            maps[leg].append([row, encode(leg, i, q + p, s), 3])
    boundary = [column for column in range(DIM)
                if sum((decode(0, column)[0], decode(0, column)[2])) != decode(0, column)[1]]
    return {'source_lengths': [A, B], 'target_blocks': [3],
            'target_vertex_charges': [[0, 2, 5]], 'map_denominator': 3,
            'maps': maps, 'fixed_boundary_source_columns_common_order': boundary}


def basis_matrix(leg, column, value=1):
    i, middle, s = decode(leg, column)
    return {(i * B + q, p * B + s): value
            for p, q in product(range(A), range(B)) if p + q == middle}


def physical_maps(data, boundary_only=False):
    boundary = set(data['fixed_boundary_source_columns_common_order'])
    result = [[{} for _ in range(9)] for _ in range(3)]
    for leg, entries in enumerate(data['maps']):
        for row, column, value in entries:
            if boundary_only and common(leg, column) not in boundary:
                continue
            for key, entry in basis_matrix(leg, column, value).items():
                result[leg][row][key] = result[leg][row].get(key, 0) + entry
    return result


def trace_three(left, middle, right):
    middle_rows = {}
    for (row, column), value in middle.items():
        middle_rows.setdefault(row, []).append((column, value))
    value = 0
    for (row, inside), first in left.items():
        for last, second in middle_rows.get(inside, []):
            value += first * second * right.get((last, row), 0)
    return value


def image(maps):
    result = {}
    for x, y, z in product(range(9), repeat=3):
        value = trace_three(maps[0][x], maps[1][y], maps[2][z])
        if value:
            result[x, y, z] = value
    return result


def add_variable(maps, variable, value):
    leg, row, common_column = variable
    point = decode(0, common_column)
    for key, entry in basis_matrix(leg, encode(leg, *point), value).items():
        maps[leg][row][key] = maps[leg][row].get(key, 0) + entry


def normalize(row, rhs):
    row = {key: value for key, value in row.items() if value}
    factor = abs(rhs)
    for value in row.values():
        factor = gcd(factor, abs(value))
    if not factor:
        return {}, 0
    if row and row[min(row)] < 0:
        factor = -factor
    return {key: value // factor for key, value in row.items()}, rhs // factor


def verify():
    data = build_control()
    wanted = {(i * 3 + j, j * 3 + k, k * 3 + i): 27
              for i, j, k in product(range(3), repeat=3)}
    if image(physical_maps(data)) != wanted:
        raise ArithmeticError('The complete non-square M3 positive control failed')
    for leg in range(3):
        for column in range(DIM):
            if affine.common_column(A, B, leg, column) != common(leg, column):
                raise ArithmeticError('A non-square original/common column permutation failed')
            if affine.original_column(A, B, leg, common(leg, column)) != column:
                raise ArithmeticError('A non-square common/original inverse permutation failed')

    system = affine.build_system(data, weights=(2, -2))
    base = physical_maps(data, boundary_only=True)
    constant = image(base)
    derivatives = []
    for variable in system['variables']:
        changed = deepcopy(base)
        add_variable(changed, variable, 1)
        changed_image = image(changed)
        derivatives.append({point: changed_image.get(point, 0) - constant.get(point, 0)
                            for point in changed_image.keys() | constant.keys()
                            if changed_image.get(point, 0) != constant.get(point, 0)})
    expected = {}
    for leg, selected, left, right in product(range(3), system['selected_target_rows'], range(9), range(9)):
        point = [0, 0, 0]
        point[leg], point[(leg + 1) % 3], point[(leg + 2) % 3] = selected, left, right
        point = tuple(point)
        row = {variable: derivative[point] for variable, derivative in enumerate(derivatives)
               if point in derivative}
        rhs = wanted.get(point, 0) - constant.get(point, 0)
        row, rhs = normalize(row, rhs)
        if row or rhs:
            expected[leg, selected, left, right] = row, rhs
    actual = {tuple(record['key']): (record['row'], record['rhs']) for record in system['equations']}
    if expected != actual:
        raise ArithmeticError('The affine equations disagree with exact physical matrix derivatives')

    # Check the entire affine prediction at a nonsymmetric integer point.
    values = {index: ((7 * index + 3) % 11) - 5 for index in range(len(system['variables']))}
    changed = deepcopy(base)
    for index, variable in enumerate(system['variables']):
        add_variable(changed, variable, values[index])
    changed_image = image(changed)
    selected_set = set(system['selected_target_rows'])
    for point in product(range(9), repeat=3):
        if not any(row in selected_set for row in point):
            continue
        predicted = constant.get(point, 0) + sum(values[index] * derivative.get(point, 0)
                                                for index, derivative in enumerate(derivatives))
        if predicted != changed_image.get(point, 0):
            raise ArithmeticError('A complete physical slice has an omitted nonlinear term')
    solved = affine.exact_eliminate(system['equations'], system['current_values'])
    if not solved['feasible']:
        raise ArithmeticError('The positive control was incorrectly declared infeasible')
    solution = deepcopy(base)
    for index, value in solved['solution'].items():
        add_variable(solution, system['variables'][index], value)
    solved_image = image(solution)
    for point in product(range(9), repeat=3):
        if any(row in selected_set for row in point) and solved_image.get(point, 0) != wanted.get(point, 0):
            raise ArithmeticError('The solved affine point failed a physical target slice')

    # Fix the zero-weight slices instead; their free-by-free block is nonzero.
    nonlinear = deepcopy(data)
    old_boundary = set(data['fixed_boundary_source_columns_common_order'])
    nonlinear['fixed_boundary_source_columns_common_order'] = [c for c in range(DIM) if c not in old_boundary]
    try:
        affine.build_system(nonlinear, weights=(0,))
    except ValueError as error:
        if 'free-by-free' not in str(error):
            raise
    else:
        raise ArithmeticError('A nonlinear selected slice was incorrectly accepted as affine')
    return {'source': 'A(3,4)', 'positive_target': 'M3',
            'source_leg_dimension': DIM, 'physical_matrix_dimension': A * B,
            'common_original_permutation_checks': 3 * DIM,
            'complete_positive_target_coefficients_checked': 9 ** 3,
            'positive_target_terms': len(wanted), 'map_denominator': 3,
            'affine_builder_source_terms_checked': system['source_terms_checked'],
            'affine_variables': len(system['variables']),
            'normalized_equations_reconstructed_by_physical_traces': len(actual),
            'all_three_cyclic_leg_orientations_checked': True,
            'independent_integer_affine_point_checked': True,
            'feasible_solution_verified_by_physical_traces': True,
            'nonlinear_free_by_free_slice_rejected': True,
            'standard_library_only': True,
            'review_scope': 'checked by a second agent in this generating session; no external independent review',
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    (HERE / 'parity_structure_affine_audit.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
