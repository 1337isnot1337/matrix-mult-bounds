"""Exact normal filter for the retained invertible mixed first lines."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location('invertible_both_source', HERE.parent / '2026-10-21-both-mixed-first-spaces/verify.py')
both = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(both)
third, normal, extension = both.third, both.normal, both.extension
constructor = third.load('invertible_row_solver', HERE.parent / '2026-10-21-mixed-first-jets/construct.py')
SEED = ROOT / 'results/both-mixed-first-spaces-2026-10-21/invertible-lines-seed.json'


def sparse_columns(matrix):
    return [[[i, int(sp.Rational(value).p), int(sp.Rational(value).q)]
             for i, value in enumerate(matrix[:, k]) if value]
            for k in range(matrix.cols)]


@lru_cache(None)
def data():
    seed = json.loads(SEED.read_text())
    left = third.verify.rows(seed['first_constant_B_new'])
    right = third.verify.rows(seed['first_constant_C_new'])
    canonical = normal.data()
    cross = third.first_constraints(seed)
    parameters, _ = normal.sparse_nullspace(cross)
    normals = canonical['first_kernel']*parameters
    directions = sp.MutableSparseMatrix(896, parameters.cols,
        {(normal.NORMAL[r], k): value for (r, k), value in normals.todok().items()})
    recovery = sp.kronecker_product(sp.SparseMatrix.eye(64), canonical['recover'])
    y = recovery*canonical['operator']*directions
    identity = [{i: 1} for i in range(112)]
    corrections = []
    for side, rows, key in (('B', left, 'left_constraints'), ('C', right, 'right_constraints')):
        one = (extension.contract(rows, identity, normal.KERNEL) if side == 'B'
               else extension.contract(identity, rows, normal.KERNEL))
        old = (extension.contract(rows, extension.G, extension.A0) if side == 'B'
               else extension.contract(extension.G, rows, extension.A0))
        offset = 448 if side == 'B' else 0
        direct = sp.MutableSparseMatrix(256, 896,
            {(4*x+c, offset+112*c+u): value for (x, u), value in one.todok().items()
             for c in range(4)})
        residual = direct*directions-sp.kronecker_product(sp.SparseMatrix.eye(64), old.T)*y
        corrections.append(constructor.solver(canonical[key])(-residual))
    third_map = sp.MutableSparseMatrix.zeros(64, directions.cols)
    old_pair = extension.contract(left, right, extension.A0)
    for k in range(directions.cols):
        b2 = [{j: corrections[0][j, k] for j in range(112) if corrections[0][j, k]}]
        c2 = [{j: corrections[1][j, k] for j in range(112) if corrections[1][j, k]}]
        source_correction = sp.Matrix(64, 12, lambda i, j: y[12*i+j, k])
        third_map[:, k] = (extension.contract(b2, right, normal.KERNEL)
                           + extension.contract(left, c2, normal.KERNEL)
                           - source_correction*old_pair)
    kernel, _ = normal.sparse_nullspace(third_map)
    remaining = directions*kernel
    pure_b = remaining*normal.sparse_nullspace(remaining[448:, :])[0]
    pure_c = remaining*normal.sparse_nullspace(remaining[:448, :])[0]
    plane = sp.Matrix.hstack(*(sp.Matrix([row.get(j, 0) for row in rows for j in range(112)])
                              for rows in normal.plane_directions()))
    base = pure_b.row_join(pure_c).row_join(plane)
    _, pivots = base.row_join(remaining).to_DM().rref()
    selected = [j-base.cols for j in pivots if j >= base.cols]
    return {'cross': cross, 'directions': directions, 'third': third_map,
            'remaining': remaining, 'pure_B': pure_b, 'pure_C': pure_c,
            'plane': plane, 'base': base, 'complement': remaining[:, selected]}


@lru_cache(None)
def report():
    d = data()
    cross_rank = third.rank_certificate(d['cross'])
    third_rank = third.rank_certificate(d['third'])
    if (cross_rank['rational_rank'], third_rank['rational_rank']) != (156, 32):
        raise ArithmeticError('Unexpected normal-filter ranks')
    dimensions = [d[key].cols for key in ('directions', 'remaining', 'pure_B', 'pure_C', 'complement')]
    if dimensions != [72, 40, 16, 16, 4] or third.matrix_rank(d['base']) != 36:
        raise ArithmeticError('Unexpected normal-space decomposition')
    if third.matrix_rank(d['remaining'].row_join(d['plane'])) != 40:
        raise ArithmeticError('Plane motion is not contained in the retained normal space')
    return {'field': 'Q, with linear identities valid over C',
            'first_quotient_dimensions': [1, 1],
            'cross_rank_certificate': cross_rank,
            'normal_dimension_before_third': 72,
            'projected_third_rank_certificate': third_rank,
            'normal_dimension_after_zero_third': 40,
            'pure_B_dimension': 16, 'pure_C_dimension': 16,
            'pure_and_plane_span_dimension': 36,
            'selected_coupled_complement_dimension': 4,
            'remaining_normal_directions': sparse_columns(d['remaining']),
            'pure_B_directions': sparse_columns(d['pure_B']),
            'pure_C_directions': sparse_columns(d['pure_C']),
            'selected_coupled_directions': sparse_columns(d['complement']),
            'scope': 'Necessary linear normal filter for this first seed. The vector-space decomposition is not a nonlinear gauge reduction or an assertion that all directions lift.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
