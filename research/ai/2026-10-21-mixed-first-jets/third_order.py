"""Exact normal and third-coefficient constraints for the fixed mixed seed."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


verify = load('mixed_third_family', HERE / 'verify.py')
normal = load('mixed_third_normal', HERE.parent / '2026-10-21-moving-boundary-flags/normal_directions.py')
extension = normal.extension
STAGES = ((36, 37, 39, 40, 43, 44, 46, 47), (64, 65, 71, 72))


def matrix_rank(matrix):
    return len(matrix.to_DM().rref()[1])


def rank_certificate(matrix):
    if any(value.q != 1 for value in matrix.todok().values()):
        raise ArithmeticError('The modular certificate requires integral entries')
    return extension.rank_certificate(matrix)


def top_directions(certificate):
    columns = []
    for encoded in certificate['first_top_directions']:
        rows = verify.rows(encoded)
        columns.append(sp.Matrix([row.get(j, 0) for row in rows for j in range(112)]))
    return sp.Matrix.hstack(*columns)


def first_constraints(certificate):
    """Impose both off-diagonal equations, eliminating arbitrary corrections."""
    data = normal.data()
    cuts = []
    for side in ('B', 'C'):
        basis = normal.row_matrix(extension.G+data[f'E_{side}_complement']).T
        vectors = normal.row_matrix(verify.rows(certificate[f'first_constant_{side}_new'])).T
        coordinates = basis.gauss_jordan_solve(vectors)[0]
        obstruction = data['left_obstruction' if side == 'B' else 'right_obstruction']
        for k in range(vectors.cols):
            cut = sp.MutableSparseMatrix.zeros(200, 228)
            for j in range(16):
                cut += coordinates[4+j, k]*obstruction[200*j:200*(j+1), :]
            cuts.append(cut)
    return normal.distinct_rows(sp.MutableSparseMatrix.vstack(*cuts))


def third_coefficients(certificate):
    """The new-by-new block on the 64-dimensional polynomial annihilator."""
    left = verify.rows(certificate['first_constant_B_new'])
    right = verify.rows(certificate['first_constant_C_new'])
    second_constant = verify.contract(left, right)
    maps = {a: sp.MutableSparseMatrix.zeros(84, 16) for a in normal.KERNEL}
    for k in range(16):
        left_second = verify.rows(certificate['second_linear_B_new'][k])
        right_second = verify.rows(certificate['second_linear_C_new'][k])
        tensor = verify.add(
            (1, verify.contract(left_second, right)),
            (1, verify.contract(left, right_second)),
            (-1, verify.correct(certificate['first_row_corrections'][k], second_constant)))
        for (a, b, c), value in tensor.items():
            if a in maps:
                maps[a][6*b+c, k] = value
    return maps


def force_stage(maps, parameter_basis, sources, row_bound):
    """A fixed row cover proves rank <= row_bound for all complex parameters."""
    matrices, covers = [], []
    for a in sources:
        coefficients = maps[a]*parameter_basis
        occupied = sorted({r//6 for r, c in coefficients.todok()})
        if len(occupied) > row_bound:
            raise ArithmeticError(f'Source {a} exceeds its universal row cover')
        covers.append({'source_index': a, 'output_rows': occupied})
        matrices.append(coefficients)
    constraints = sp.MutableSparseMatrix.vstack(*matrices)
    kernel, _ = normal.sparse_nullspace(constraints)
    return parameter_basis*kernel, {
        'source_row_covers': covers,
        'universal_matrix_rank_bound': row_bound,
        'rank_certificate': rank_certificate(constraints),
        'remaining_parameter_dimension': kernel.cols,
    }


@lru_cache(None)
def report():
    certificate = json.loads(verify.DEFAULT.read_text())
    verify.verify(certificate)
    data = normal.data()
    directions = top_directions(certificate)
    normals = directions[normal.NORMAL, :]
    parameters = normals[data['free'], :]
    constraints = first_constraints(certificate)
    if data['first_kernel']*parameters != normals or matrix_rank(parameters) != 16:
        raise ArithmeticError('The frozen seed does not span sixteen first-normal solutions')
    if constraints*parameters != sp.zeros(constraints.rows, 16):
        raise ArithmeticError('The seed violates a first cross equation')
    first_rank = rank_certificate(constraints)
    if first_rank['rational_rank'] != 212:
        raise ArithmeticError('Unexpected dimension of the compatible normal space')
    maps = third_coefficients(certificate)
    first_basis, first_stage = force_stage(maps, sp.SparseMatrix.eye(16), STAGES[0], 1)
    final_basis, second_stage = force_stage(maps, first_basis, STAGES[1], 2)
    if (first_basis.cols, final_basis.cols) != (10, 4):
        raise ArithmeticError('Unexpected third-order constraint ranks')
    plane = sp.Matrix.hstack(*(sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
                              for rows in normal.plane_directions()))
    final_normals = directions*final_basis
    if matrix_rank(final_normals.row_join(plane)) != 4:
        raise ArithmeticError('Remaining directions are not the common-plane tangent space')
    if any(any(matrix*final_basis) for matrix in maps.values()):
        raise ArithmeticError('Common-plane directions have a projected third obstruction')
    return {
        'field': 'Q, with polynomial identities valid over C',
        'first_normal_dimension': 228,
        'mixed_cross_distinct_rows': constraints.rows,
        'mixed_cross_rank_certificate': first_rank,
        'compatible_normal_dimension': 16,
        'third_coefficient_source_dimension': 64,
        'third_coefficient_matrix_shape': [14, 6],
        'stages': [first_stage, second_stage],
        'remaining_parameter_vectors': [[str(x) for x in final_basis[:, k]]
                                        for k in range(final_basis.cols)],
        'remaining_normal_dimension': 4,
        'remaining_space_equals_common_plane_tangents': True,
        'scope': 'Exact finite lemma for the fixed mixed 14-by-6 first spaces; all-order consequence requires third_order.md.',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
