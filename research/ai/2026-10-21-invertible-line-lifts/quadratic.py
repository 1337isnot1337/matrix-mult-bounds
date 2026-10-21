"""Complete quadratic compatibility equations for a specified 36-direction ansatz."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as sp

SPEC = importlib.util.spec_from_file_location('invertible_normal_filter', Path(__file__).with_name('normal_space.py'))
normal_filter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(normal_filter)
normal, extension, third = normal_filter.normal, normal_filter.extension, normal_filter.third


@lru_cache(None)
def data():
    seed = json.loads(normal_filter.SEED.read_text())
    left = third.verify.rows(seed['first_constant_B_new'])
    right = third.verify.rows(seed['first_constant_C_new'])
    filtered = normal_filter.data()
    directions = filtered['pure_B'].row_join(filtered['pure_C']).row_join(filtered['complement'])
    first, cb, cc, _, top, annihilator = extension.matrices()
    identity = [{i: 1} for i in range(112)]
    bg = extension.contract(identity, extension.G, extension.OUTSIDE)
    gc = extension.contract(extension.G, identity, extension.OUTSIDE)
    entries = defaultdict(int)
    for (x, column), value in bg.todok().items():
        u, c = divmod(column, 4)
        for b in range(4):
            entries[16*x+4*b+c, 112*b+u] += value
    for (x, column), value in gc.todok().items():
        b, u = divmod(column, 112)
        for c in range(4):
            entries[16*x+4*b+c, 448+112*c+u] += value
    derivative = sp.MutableSparseMatrix(1600, 896, dict(entries))
    recovery = sp.kronecker_product(sp.SparseMatrix.eye(100), normal.data()['recover'])
    source_correction = recovery*derivative
    quotients = [normal.sparse_nullspace(matrix.T)[0].T for matrix in (cb, cc)]
    linear, old_operators = [], []
    for side, rows, offset in (('B', left, 448), ('C', right, 0)):
        one = (extension.contract(rows, identity, extension.OUTSIDE) if side == 'B'
               else extension.contract(identity, rows, extension.OUTSIDE))
        old = (extension.contract(rows, extension.G, extension.A0) if side == 'B'
               else extension.contract(extension.G, rows, extension.A0))
        direct = sp.MutableSparseMatrix(400, 896,
            {(4*x+c, offset+112*c+u): value for (x, u), value in one.todok().items()
             for c in range(4)})
        old_operator = sp.kronecker_product(sp.SparseMatrix.eye(100), old.T)
        old_operators.append(old_operator)
        linear.append(direct-old_operator*source_correction)
    if any(top*directions) or any(linear[0]*directions) or any(linear[1]*directions):
        raise ArithmeticError('The selected first directions require nonzero second new rows')
    system = sp.MutableSparseMatrix.vstack(top, quotients[0]*linear[0], quotients[1]*linear[1])
    cokernel = normal.sparse_nullspace(system.T)[0].T
    forcing = sp.MutableSparseMatrix.vstack(
        sp.kronecker_product(sp.SparseMatrix.eye(100), annihilator),
        -quotients[0]*old_operators[0]*recovery,
        -quotients[1]*old_operators[1]*recovery)
    obstruction = cokernel*forcing
    rows = [[{j: directions[112*b+j, k] for j in range(112) if directions[112*b+j, k]}
             for b in range(8)] for k in range(36)]
    for row in rows:
        if (any(extension.contract(row[:4], right, extension.A0))
                or any(extension.contract(left, row[4:], extension.A0))
                or any(extension.contract(row[:4], extension.G, extension.A0)
                       + extension.contract(extension.G, row[4:], extension.A0))):
            raise ArithmeticError('A source-correction term omitted from the ansatz is nonzero')
    monomials = list(combinations_with_replacement(range(36), 2))
    columns = []
    for i, j in monomials:
        tensor = extension.contract(rows[i][:4], rows[j][4:], extension.OUTSIDE)
        if i != j:
            tensor += extension.contract(rows[j][:4], rows[i][4:], extension.OUTSIDE)
        columns.append(obstruction*sp.Matrix(list(tensor)))
    coefficients = normal.distinct_rows(sp.MutableSparseMatrix.hstack(*columns))
    reduced, pivots = coefficients.to_DM().rref()
    reduced = sp.MutableSparseMatrix(reduced.to_Matrix()[:len(pivots), :])
    return {'system': system, 'cokernel': cokernel, 'forcing': forcing, 'directions': directions,
            'monomials': monomials, 'raw_coefficients': coefficients, 'equations': reduced,
            'left': left, 'right': right}


def uncorrected_first_rank(parameters):
    d = data()
    vector = d['directions']*sp.Matrix(parameters)
    rows = [{j: vector[112*b+j] for j in range(112) if vector[112*b+j]} for b in range(8)]
    maps = []
    for offset, new in ((0, d['left']), (4, d['right'])):
        maps.append([{j: extension.G[b].get(j, 0)+rows[offset+b].get(j, 0)
                      for j in range(112) if extension.G[b].get(j, 0)+rows[offset+b].get(j, 0)}
                     for b in range(4)]+new)
    return third.matrix_rank(extension.contract(*maps, range(112)))


@lru_cache(None)
def report():
    d = data()
    if d['system'].shape != (1016, 896) or d['cokernel'].rows != 384 or d['equations'].rows != 16:
        raise ArithmeticError('Unexpected complete compatibility dimensions')
    if any(d['cokernel']*d['system']):
        raise ArithmeticError('Invalid compatibility cokernel')
    if any(d['equations'][i, j] for i in range(16) for j, (a, b) in enumerate(d['monomials'])
           if not (a < 16 <= b < 32)):
        raise ArithmeticError('A quadratic equation involves an unexpected parameter block')
    sample = [0]*36
    sample[0] = sample[22] = 1
    values = sp.Matrix([sample[i]*sample[j] for i, j in d['monomials']])
    if any(d['equations']*values) or uncorrected_first_rank(sample) != 13:
        raise ArithmeticError('The retained compatible, growing truncation control failed')
    return {'field': 'Q, with polynomial compatibility over C',
            'parameter_split': {'pure_B': 16, 'pure_C': 16, 'selected_coupled': 4},
            'second_top_and_third_cross_system_shape': [1016, 896],
            'system_rank': 632, 'cokernel_dimension': 384,
            'quadratic_monomials': [list(m) for m in d['monomials']],
            'independent_quadratic_equations': 16,
            'equation_coefficients': [[[j, str(d['equations'][i, j])]
                                       for j in range(d['equations'].cols) if d['equations'][i, j]]
                                      for i in range(16)],
            'only_pure_B_times_pure_C_parameters_occur': True,
            'compatible_control': {'nonzero_parameter_indices': [0, 22],
                                   'values': [1, 1], 'uncorrected_first_rank_at_t_one': 13},
            'scope': 'Specified zero-second-new-row ansatz only. These equations concern second leading rows and third new rows; third leading-row and later equations remain. This is not a target obstruction for arbitrary corrections.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(), indent=2)+'\n')
