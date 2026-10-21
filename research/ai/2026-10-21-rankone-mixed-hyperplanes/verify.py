"""Uniform conditioned obstruction for mixed hyperplanes of a rank-one frame."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('mixed_hyperplane_frames', HERE.parent / '2026-10-21-rankone-seven-frames/verify.py')
frames = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(frames)
normal, third = frames.normal, frames.third
minors = third.load('mixed_hyperplane_minor_search', HERE.parent / '2026-10-21-moving-boundary-flags/minimum_rank.py')
A, B = frames.A, frames.B


def encode(matrix):
    return {'shape': list(matrix.shape),
            'entries': [[i, j, str(value)] for (i, j), value in sorted(matrix.todok().items())]}


def uniform_kernel(matrix):
    """A fixed invertible minor and a full polynomial kernel certify every point."""
    base = matrix.subs({A: 0, B: 0})
    certificate = third.rank_certificate(base)
    rr, cc = certificate['minor_rows'], certificate['minor_columns']
    free = [j for j in range(matrix.cols) if j not in cc]
    inverse = base[rr, cc].inv()
    normalized = (inverse*matrix[rr, cc]-sp.eye(len(cc))).applyfunc(sp.expand)
    order = frames.triangular_order(normalized)
    values = sp.MutableSparseMatrix((-inverse*matrix[rr, free]).applyfunc(sp.expand))
    adjacency = defaultdict(list)
    for (i, j), value in normalized.todok().items():
        adjacency[i].append((j, value))
    for i in reversed(order):
        for j, value in adjacency[i]:
            values[i, :] -= value*values[j, :]
        values[i, :] = values[i, :].applyfunc(sp.expand)
    kernel = sp.MutableSparseMatrix(matrix.cols, len(free), {(j, k): 1 for k, j in enumerate(free)})
    for i, j in enumerate(cc):
        kernel[j, :] = values[i, :]
    if not frames.zero(matrix*kernel) or kernel[free, :] != sp.eye(len(free)):
        raise ArithmeticError('Invalid uniform polynomial kernel')
    return kernel, {'base_rank_certificate': certificate,
                    'normalized_minor_minus_identity': encode(normalized),
                    'triangular_order': order, 'free_coordinates': free,
                    'polynomial_kernel': encode(kernel)}


def check_minor(matrix, record):
    form = {j: sp.sympify(value, locals={'a': A, 'b': B}) for j, value in record['linear_form']}
    vector = sp.MutableSparseMatrix(1, matrix.cols, {(0, j): value for j, value in form.items()})
    scales = [sp.Rational(value) for value in record['diagonal_scales']]
    positions = record['positions']
    for k, (row, col) in enumerate(positions):
        if not scales[k] or not frames.zero(matrix[200*col+row, :]-scales[k]*vector):
            raise ArithmeticError('Incorrect repeated diagonal form')
        for _, future in positions[k+1:]:
            if matrix[200*future+row, :].todok():
                raise ArithmeticError('Incorrect triangular zero')
    if sp.prod(scales) != sp.Rational(record['determinant_ratio']):
        raise ArithmeticError('Incorrect determinant ratio')


def force_round(matrix):
    forms, indices, positions = [], {}, defaultdict(list)
    rows, scales = defaultdict(dict), {}
    table = [[0]*7 for _ in range(200)]
    for (i, j), value in matrix.todok().items():
        rows[i][j] = value
    for flat, row in sorted(rows.items()):
        scale = sp.Poly(row[min(row)], A, B).LC()
        form = tuple((j, sp.expand(value/scale)) for j, value in sorted(row.items()))
        if form not in indices:
            indices[form] = len(forms)+1
            forms.append(form)
        index = indices[form]
        col, source = divmod(flat, 200)
        table[source][col] = index
        positions[index].append((source, col))
        scales[source, col] = scale
    chosen, records = [], []
    for index, form in enumerate(forms, 1):
        witness = minors.triangular_witness(table, positions[index], size=2)
        if witness is None:
            continue
        diagonal = [scales[position] for position in witness]
        record = {'positions': [list(position) for position in witness],
                  'linear_form': [[j, str(value)] for j, value in form],
                  'diagonal_scales': [str(value) for value in diagonal],
                  'determinant_ratio': str(sp.prod(diagonal))}
        check_minor(matrix, record)
        chosen.append(form)
        records.append(record)
    if not chosen:
        return None
    constraints = sp.MutableSparseMatrix(len(chosen), matrix.cols,
        {(i, j): value for i, form in enumerate(chosen) for j, value in form})
    kernel, certificate = uniform_kernel(constraints)
    return kernel, {'before': matrix.cols, 'forced_rank': matrix.cols-kernel.cols,
                    'after': kernel.cols, 'minors': records, 'constraint_kernel': certificate}


def conditioned_case(left, right):
    left_system = frames.constraints(left, sp.zeros(16, 0))
    right_system = frames.constraints(sp.zeros(16, 0), right)
    kernel, certificate = uniform_kernel(left_system)
    if kernel.cols != 88:
        raise ArithmeticError('Unexpected conditioned normal dimension')
    matrix = (right_system*kernel).applyfunc(sp.expand)
    rounds, matrices = [], []
    total = kernel
    while matrix.todok():
        result = force_round(matrix)
        if result is None:
            break
        next_kernel, record = result
        matrices.append(matrix)
        rounds.append(record)
        total = total*next_kernel
        matrix = (matrix*next_kernel).applyfunc(sp.expand)
    support = sorted({i//200 for i, j in matrix.todok()})
    if total.cols != 16 or support != [6]:
        raise ArithmeticError('Rank-one obstruction is not confined to the mixed column')
    base = matrix.subs({A: 0, B: 0})
    if third.matrix_rank(base) != 12:
        raise ArithmeticError('The boundary-only control lost its twelve non-plane parameters')
    parameter = next(j for j in range(base.cols) if base[:, j].todok())
    control = sp.Matrix(200, 7, lambda i, j: base[200*j+i, parameter])
    if third.matrix_rank(control) != 1:
        raise ArithmeticError('The nonzero rank-one control failed')
    return {'report': {'left_normal_dimension': 88, 'left_kernel': certificate,
                       'rounds': rounds, 'remaining_parameter_dimension': 16,
                       'remaining_obstruction_columns': support,
                       'remaining_obstruction': encode(matrix),
                       'rank_one_boundary_control': {'parameter': parameter, 'matrix': encode(control)},
                       'boundary_only_normal_dimension': 16},
            'round_matrices': matrices}


@lru_cache(None)
def data():
    return {'chart': conditioned_case(*frames.chart_frames()),
            'endpoint': conditioned_case(*frames.endpoint_frames())}


@lru_cache(None)
def report():
    d = data()
    left, right = frames.chart_frames()
    five = frames.constraints(left, right[:, [1, 3, 4, 5, 6]]).subs({A: 0, B: 0})
    if third.matrix_rank(five) != 216:
        raise ArithmeticError('The smaller mixed five-space control changed')
    return {'field': 'Polynomial identities over Q[a,b], valid over C',
            'chart': d['chart']['report'], 'endpoint': d['endpoint']['report'],
            'matrix_shape': [200, 7], 'rank_assumption_for_minor_implication': 1,
            'conclusion': 'Under the full opposite seven-frame, rank at most one forces the obstruction to vanish on all six boundary directions. A mixed hyperplane then forces its remaining column to vanish too.',
            'seven_by_five_control': {'parameters': [0, 0], 'C_columns_kept': [1, 3, 4, 5, 6],
                                      'normal_dimension': 12, 'target_or_higher_lift_claimed': False},
            'scope': 'All mixed hyperplanes in the maximal rank-one frame, using the preceding chart/reversal coverage. Boundary-only hyperplanes and five-dimensional mixed spaces are outside the exclusion.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
