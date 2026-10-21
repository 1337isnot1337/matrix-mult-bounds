"""Uniform pure-mixed five-space closure for b=1 and every complex a."""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('pure_mixed_uniform', HERE.parent / '2026-10-21-mixed-five-space-uniform/verify.py')
uniform = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(uniform)
point, frames, normal, third, hyper = uniform.point, uniform.frames, uniform.normal, uniform.third, uniform.hyper
A, B = frames.A, frames.B
encode, expand = uniform.encode, uniform.expand


def flat3(matrix, parameters=32):
    return sp.MutableSparseMatrix(3*matrix.rows, parameters,
        {(matrix.rows*(j//parameters)+i, j % parameters): sp.expand(value)
         for (i, j), value in matrix.todok().items()})


def check_minor(matrix, rows, record):
    positions = record['positions']
    size = record['size']
    if size not in (2, 3) or len(positions) != size or len({r for r, _ in positions}) != size or len({c for _, c in positions}) != size:
        raise ArithmeticError('Invalid repeated minor')
    form = sp.MutableSparseMatrix(1, matrix.cols,
        {(0, j): sp.sympify(value, locals={'a': A}) for j, value in record['form']})
    scales = [sp.Rational(value) for value in record['scales']]
    for k, (row, col) in enumerate(positions):
        if not scales[k] or not frames.zero(matrix[rows*col+row, :]-scales[k]*form):
            raise ArithmeticError('Incorrect repeated diagonal form')
        for _, future in positions[k+1:]:
            if matrix[rows*future+row, :].todok():
                raise ArithmeticError('Incorrect triangular zero')
    if sp.prod(scales) != sp.Rational(record['determinant_ratio']):
        raise ArithmeticError('Incorrect determinant ratio')


def forced_forms(matrix, rows, columns, size):
    forms, indices, positions = [], {}, defaultdict(list)
    by_row, scales = defaultdict(dict), {}
    table = [[0]*columns for _ in range(rows)]
    for (i, j), value in matrix.todok().items():
        by_row[i][j] = value
    for index, row in sorted(by_row.items()):
        scale = sp.Poly(row[min(row)], A).LC()
        form = tuple((j, sp.expand(value/scale)) for j, value in sorted(row.items()))
        if form not in indices:
            indices[form] = len(forms)+1
            forms.append(form)
        number = indices[form]
        col, source = divmod(index, rows)
        table[source][col] = number
        positions[number].append((source, col))
        scales[source, col] = scale
    chosen, records = [], []
    for number, form in enumerate(forms, 1):
        witness = point.minors.triangular_witness(table, positions[number], size=size)
        if witness is None:
            continue
        diagonal = [scales[position] for position in witness]
        record = {'size': size, 'positions': [list(p) for p in witness],
                  'form': [[j, str(value)] for j, value in form],
                  'scales': [str(value) for value in diagonal],
                  'determinant_ratio': str(sp.prod(diagonal))}
        check_minor(matrix, rows, record)
        chosen.append(form)
        records.append(record)
    return sp.MutableSparseMatrix(len(chosen), matrix.cols,
        {(i, j): value for i, form in enumerate(chosen) for j, value in form}), records


@lru_cache(None)
def initial_data():
    full = uniform.data()
    psi = expand(full['virtual']['psi'].subs({B: 1}))
    j_full = expand(full['virtual']['third'].subs({B: 1}))
    sources = full['sources']
    low = expand(sp.kronecker_product(sources.T, sp.SparseMatrix.eye(49))*j_full)
    mixed_rows = [49*i+7*j+6 for i in range(16) for j in range(7)]
    mixed = expand(sp.MutableSparseMatrix.vstack(psi[1200:1400, :], low[mixed_rows, :]))
    kernel, certificate = hyper.uniform_kernel(mixed)
    if kernel.cols != 36:
        raise ArithmeticError('Unexpected pure-mixed normal dimension')
    plane88 = frames.plane_parameters()[full['normal_certificate']['free_coordinates'], :]
    plane36 = plane88[certificate['free_coordinates'], :]
    if not frames.zero(kernel*plane36-plane88) or third.matrix_rank(plane36) != 4:
        raise ArithmeticError('Plane directions are not in the complete mixed kernel')
    if not frames.zero(psi*plane88) or not frames.zero(j_full*plane88):
        raise ArithmeticError('A plane direction has a nonzero obstruction or third slice')
    basis = sp.Matrix.hstack(plane36, sp.eye(36))
    _, columns = basis.to_DM().rref()
    columns = list(columns)
    if columns[:4] != [0, 1, 2, 3] or len(columns) != 36:
        raise ArithmeticError('Invalid plane complement')
    complement = [j-4 for j in columns[4:]]
    quotient = kernel[:, complement]
    p, l = expand(psi*quotient), expand(low*quotient)
    rows = 312
    entries = {(rows*(i//200)+i % 200, j): value for (i, j), value in p.todok().items()}
    for source in range(16):
        for (i, j), value in l[49*source:49*(source+1), :].todok().items():
            b_row, c_col = divmod(i, 7)
            entries[rows*c_col+200+7*source+b_row, j] = value
    obstruction = sp.MutableSparseMatrix(7*rows, 32, entries)
    if obstruction[6*rows:, :].todok():
        raise ArithmeticError('The pure mixed column does not vanish')
    row_basis, _, row_certificate = uniform.polynomial_row_basis(point.joint(obstruction, rows))
    if row_basis.rows != 44:
        raise ArithmeticError('Unexpected uniform obstruction row count')
    source_change, second = sp.SparseMatrix.eye(64), sp.SparseMatrix.eye(64)
    for k, source in enumerate(normal.KERNEL):
        i, s, z = source//28, (source//7) % 4, source % 7
        if i == 2:
            source_change[normal.KERNEL.index(28+7*s+z), k] -= A
        if s == 2:
            second[normal.KERNEL.index(28*i+7+z), k] += 1
    source_change = source_change*second
    if any(i >= j for i, j in (source_change-sp.eye(64)).todok()):
        raise ArithmeticError('Source change is not unitriangular')
    third_map = expand(sp.kronecker_product(source_change.T, sp.SparseMatrix.eye(49))*j_full*quotient)
    return {'mixed_certificate': certificate, 'kernel': kernel, 'plane36': plane36,
            'complement': complement, 'quotient': quotient, 'rows': row_basis,
            'row_certificate': row_certificate, 'source_change': source_change,
            'third': third_map}


@lru_cache(None)
def split_data():
    data = initial_data()
    rows = data['rows'][:, :192]
    even = [64*j+k for j in range(3) for k in range(32)]
    odd = [64*j+32+k for j in range(3) for k in range(32)]
    projection = expand(rows[:, odd]-A**3*rows[:, even])
    stable_kernel, stable_certificate = hyper.uniform_kernel(projection.T)
    stable = expand(stable_kernel.T*rows)
    if stable.rows != 14 or not frames.zero(stable[:, odd]-A**3*stable[:, even]):
        raise ArithmeticError('Invalid stable row subspace')
    stable_coefficients = flat3(stable[:, even])
    w_kernel, w_certificate = hyper.uniform_kernel(stable_coefficients)
    if w_kernel.cols != 6:
        raise ArithmeticError('Unexpected stable-core kernel')
    q_rows, _, q_certificate = uniform.polynomial_row_basis(projection)
    q = flat3(q_rows)
    parameters, records, checks = sp.SparseMatrix.eye(32), [], []
    while True:
        matrix = expand(q*parameters)
        if not matrix.todok():
            break
        cuts, witnesses = forced_forms(matrix, q_rows.rows, 3, 2)
        if not cuts.rows:
            raise ArithmeticError('Rank-one projection elimination stalled')
        kernel, certificate = hyper.uniform_kernel(cuts)
        checks.extend((matrix, q_rows.rows, witness) for witness in witnesses)
        records.append({'before': parameters.cols, 'after': kernel.cols,
                        'minors': witnesses, 'kernel_certificate': certificate})
        parameters = expand(parameters*kernel)
    if parameters.cols != 14:
        raise ArithmeticError('Unexpected zero-projection kernel')
    return {'stable_kernel_certificate': stable_certificate, 'stable_rows': stable,
            'stable_coefficients': stable_coefficients, 'w_kernel': w_kernel,
            'w_kernel_certificate': w_certificate, 'q_rows_certificate': q_certificate,
            'q_coefficients': q, 'q_kernel': parameters, 'q_rounds': records, 'minor_checks': checks}


def eliminate_case(parameters):
    data = initial_data()
    base = point.flat(data['rows'], 32)
    selected, records = set(), []
    while parameters.cols:
        xp, jp = expand(base*parameters), expand(data['third']*parameters)
        rows = 44+7*len(selected)
        entries = {(rows*(i//44)+i % 44, j): value for (i, j), value in xp.todok().items()}
        for k, source in enumerate(sorted(selected)):
            for (i, j), value in jp[49*source:49*(source+1), :].todok().items():
                b_row, c_col = divmod(i, 7)
                entries[rows*c_col+44+7*k+b_row, j] = value
        obstruction = sp.MutableSparseMatrix(7*rows, parameters.cols, entries)
        mixed = obstruction[6*rows:, :]
        if mixed.todok():
            kernel, certificate = hyper.uniform_kernel(mixed)
            if kernel.cols >= parameters.cols:
                raise ArithmeticError('Mixed-column reduction did not decrease dimension')
            records.append({'kind': 'mixed_column', 'before': parameters.cols,
                            'after': kernel.cols, 'kernel_certificate': certificate})
            parameters = expand(parameters*kernel)
            continue
        reduced, pivots, certificate = uniform.polynomial_row_basis(point.joint(obstruction, rows))
        j_joint = sp.MutableSparseMatrix(448, 7*parameters.cols,
            {(i//7, parameters.cols*(i % 7)+j): value for (i, j), value in jp.todok().items()})
        residual = expand(j_joint-j_joint[:, pivots]*reduced)
        additions = []
        for source in range(64):
            if source in selected:
                continue
            block = residual[7*source:7*(source+1), :]
            if not block.todok():
                continue
            cover = point.cover({(i, j//parameters.cols) for i, j in block.todok()})
            bound = {'cover': cover} if cover else None
            if cover:
                point.check_cover(block, parameters.cols, cover)
            else:
                rank = len(block.to_DM().rref()[1])
                if rank <= 2:
                    bound = {'joint_B_rank_over_Qa': rank}
            if bound is not None:
                additions.append({'source_position': source, 'source_index': normal.KERNEL[source],
                                  'bound': bound, 'joint_coefficients': encode(block)})
        if additions:
            selected.update(item['source_position'] for item in additions)
            records.append({'kind': 'low_sources', 'parameters': parameters.cols,
                            'sources': additions, 'rowspace_certificate': certificate})
            continue
        cuts, witnesses = forced_forms(point.flat(reduced, parameters.cols), reduced.rows, 7, 3)
        if not cuts.rows:
            raise ArithmeticError('Terminal mode elimination stalled')
        kernel, certificate = hyper.uniform_kernel(cuts)
        records.append({'kind': 'cubic_minors', 'before': parameters.cols, 'after': kernel.cols,
                        'minors': witnesses, 'kernel_certificate': certificate})
        parameters = expand(parameters*kernel)
    return records


@lru_cache(None)
def report():
    initial, split = initial_data(), split_data()
    return {'claim': 'AI-PURE-MIXED-FIVE-SPACES-089', 'chart': {'a': 'any complex number', 'b': 1},
            'C_first_space_contains_pure_mixed_vector': True,
            'normal_dimensions': {'full_B': 88, 'mixed_and_low_sources': 36, 'plane': 4, 'quotient': 32},
            'mixed_normal_certificate': initial['mixed_certificate'], 'plane_coordinates': encode(initial['plane36']),
            'quotient_columns': initial['complement'], 'quotient_basis': encode(initial['quotient']),
            'obstruction_row_certificate': initial['row_certificate'], 'source_change': encode(initial['source_change']),
            'stable_row_certificate': split['stable_kernel_certificate'], 'stable_rows': encode(split['stable_rows']),
            'stable_core_kernel_certificate': split['w_kernel_certificate'],
            'projection_row_certificate': split['q_rows_certificate'], 'projection_minrank_rounds': split['q_rounds'],
            'zero_projection_kernel': encode(split['q_kernel']),
            'case_dimensions': [6, 14], 'cases': [eliminate_case(split['w_kernel']), eliminate_case(split['q_kernel'])],
            'final_nonplane_dimension': 0,
            'scope': 'Uniform pure-mixed-row local exclusion for b=1, extended by the source torus to b nonzero. Arbitrary mixed-row graphs and the remaining partner strata are not covered; no exponent improvement.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(value)
    else:
        print(value, end='')
