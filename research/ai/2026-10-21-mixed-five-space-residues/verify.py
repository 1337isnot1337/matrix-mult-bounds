"""Exact five-space normal closure at the rank-one partner u=v=e3.

The C corrections are virtual on the maximal seven-frame.  Their residual
factors through Psi; they become actual only on a subspace annihilating Psi.
"""
import argparse
from collections import defaultdict
from functools import lru_cache
import importlib.util
from itertools import combinations
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('five_space_hyperplanes', HERE.parent / '2026-10-21-rankone-mixed-hyperplanes/verify.py')
hyper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(hyper)
frames, normal, third = hyper.frames, hyper.normal, hyper.third
extension, minors = frames.extension, hyper.minors
encode = hyper.encode


def joint(matrix, rows):
    """Column-major evaluations -> rows by (C coordinate, parameter)."""
    return sp.MutableSparseMatrix(rows, 7*matrix.cols,
        {(i % rows, matrix.cols*(i//rows)+j): value
         for (i, j), value in matrix.todok().items()})


def flat(matrix, parameters):
    return sp.MutableSparseMatrix(7*matrix.rows, parameters,
        {(matrix.rows*(j//parameters)+i, j % parameters): value
         for (i, j), value in matrix.todok().items()})


def row_basis(matrix):
    reduced, pivots = matrix.to_DM().rref()
    return reduced.to_Matrix()[:len(pivots), :], list(pivots)


@lru_cache(None)
def source_data():
    data = normal.data()
    left, right = (m.subs({frames.A: 0, frames.B: 0}) for m in frames.chart_frames())
    b_rows = frames.covectors(left, data['E_B_complement'])
    c_rows = frames.covectors(right, data['E_C_complement'])
    parameters = normal.sparse_nullspace(frames.constraints(left, sp.zeros(16, 0)))[0]
    if parameters.cols != 88:
        raise ArithmeticError('Unexpected full B-frame normal dimension')
    normal_values = data['first_kernel']*parameters
    leading = sp.MutableSparseMatrix(896, 88,
        {(normal.NORMAL[i], j): value for (i, j), value in normal_values.todok().items()})
    source_correction = sp.kronecker_product(sp.SparseMatrix.eye(64), data['recover'])*data['operator']*leading
    psi = frames.constraints(sp.zeros(16, 0), right)*parameters
    psi_joint, pivots = row_basis(joint(psi, 200))
    identity = [{i: 1} for i in range(112)]
    solutions, c_residuals = [], []
    for side, rows, key in (('B', b_rows, 'left_constraints'), ('C', c_rows, 'right_constraints')):
        base = data[key]
        _, cc = base.to_DM().rref()
        cc = list(cc)
        _, rr = base[:, cc].T.to_DM().rref()
        rr = list(rr)
        inverse = base[rr, cc].inv()
        answers = []
        for row in rows:
            one = extension.contract([row], identity, normal.KERNEL) if side == 'B' else extension.contract(identity, [row], normal.KERNEL)
            core = extension.contract([row], extension.G, extension.A0) if side == 'B' else extension.contract(extension.G, [row], extension.A0)
            offset = 448 if side == 'B' else 0
            direct = sp.MutableSparseMatrix(256, 896,
                {(4*x+c, offset+112*c+u): value for (x, u), value in one.todok().items() for c in range(4)})
            rhs = direct*leading-sp.kronecker_product(sp.SparseMatrix.eye(64), core.T)*source_correction
            values = -inverse*rhs[rr, :]
            answer = sp.MutableSparseMatrix.zeros(112, 88)
            for i, j in enumerate(cc):
                answer[j, :] = values[i, :]
            residual = base*answer+rhs
            if side == 'B' and residual.todok():
                raise ArithmeticError('B correction does not solve its equations')
            if side == 'C':
                c_residuals.append(residual)
            answers.append(answer)
        solutions.append(answers)
    residual_joint = joint(sp.MutableSparseMatrix.vstack(*c_residuals), 256)
    residual_factor = residual_joint[:, pivots]
    if residual_joint != residual_factor*psi_joint:
        raise ArithmeticError('Virtual C residual does not factor through Psi')
    third_map = sp.MutableSparseMatrix.zeros(64*49, 88)
    pair = extension.contract(b_rows, c_rows, extension.A0)
    for k in range(88):
        b2, c2 = [[{j: row[j, k] for j in range(112) if row[j, k]} for row in answers] for answers in solutions]
        y = sp.Matrix(64, 12, lambda i, j: source_correction[12*i+j, k])
        value = extension.contract(b2, c_rows, normal.KERNEL)+extension.contract(b_rows, c2, normal.KERNEL)-y*pair
        third_map[:, k] = sp.Matrix(list(value))
    return {'parameters': parameters, 'psi': psi, 'third': third_map,
            'residual_factor': residual_factor, 'psi_joint_basis': psi_joint}


def cover(support):
    """A cover of at most two row/column vertices certifies matrix rank <=2."""
    if not support:
        return []
    for size in (1, 2):
        for vertices in combinations(range(14), size):
            if all(i in vertices or 7+j in vertices for i, j in support):
                return list(vertices)
    return None


def check_cover(block, parameters, vertices):
    if len(vertices) > 2 or len(set(vertices)) != len(vertices) or any(v not in range(14) for v in vertices):
        raise ArithmeticError('Invalid rank-two cover')
    if any(i not in vertices and 7+j//parameters not in vertices for i, j in block.todok()):
        raise ArithmeticError('Uncovered nonzero coefficient')


def check_minor(matrix, rows, record):
    positions = record['positions']
    if len(positions) != 3 or len({r for r, _ in positions}) != 3 or len({c for _, c in positions}) != 3:
        raise ArithmeticError('Invalid three-by-three minor')
    form = sp.MutableSparseMatrix(1, matrix.cols,
        {(0, j): sp.Rational(value) for j, value in record['form']})
    scales = [sp.Rational(value) for value in record['scales']]
    for k, (r, c) in enumerate(positions):
        if not scales[k] or matrix[rows*c+r, :] != scales[k]*form:
            raise ArithmeticError('Incorrect repeated diagonal form')
        for _, future in positions[k+1:]:
            if matrix[rows*future+r, :].todok():
                raise ArithmeticError('Incorrect triangular zero')
    if sp.prod(scales) != sp.Rational(record['determinant_ratio']):
        raise ArithmeticError('Incorrect determinant ratio')


def forced_forms(matrix, rows):
    forms, indices, positions = [], {}, defaultdict(list)
    by_row, scales = defaultdict(dict), {}
    table = [[0]*7 for _ in range(rows)]
    for (i, j), value in matrix.todok().items():
        by_row[i][j] = value
    for index, row in sorted(by_row.items()):
        form = minors.primitive_form(row)
        if form not in indices:
            indices[form] = len(forms)+1
            forms.append(form)
        number = indices[form]
        c, r = divmod(index, rows)
        table[r][c] = number
        positions[number].append((r, c))
        j, value = form[0]
        scales[r, c] = row[j]/value
    chosen, records = [], []
    for number, form in enumerate(forms, 1):
        witness = minors.triangular_witness(table, positions[number], size=3)
        if witness is None:
            continue
        diagonal = [scales[position] for position in witness]
        record = {'positions': [list(p) for p in witness], 'form': [[j, str(v)] for j, v in form],
                  'scales': [str(v) for v in diagonal], 'determinant_ratio': str(sp.prod(diagonal))}
        check_minor(matrix, rows, record)
        chosen.append(form)
        records.append(record)
    return sp.MutableSparseMatrix(len(chosen), matrix.cols,
        {(i, j): value for i, form in enumerate(chosen) for j, value in form}), records


@lru_cache(None)
def reduction():
    data = source_data()
    parameters = sp.SparseMatrix.eye(88)
    selected, records, checks = set(), [], []
    while True:
        psi, third_map = data['psi']*parameters, data['third']*parameters
        rows = 200+7*len(selected)
        entries = {(rows*(i//200)+i % 200, j): value for (i, j), value in psi.todok().items()}
        for k, a in enumerate(sorted(selected)):
            for (i, j), value in third_map[49*a:49*(a+1), :].todok().items():
                b, c = divmod(i, 7)
                entries[rows*c+200+7*k+b, j] = value
        z = sp.MutableSparseMatrix(7*rows, parameters.cols, entries)
        reduced_z, pivots = row_basis(joint(z, rows))
        third_joint = sp.MutableSparseMatrix(448, 7*parameters.cols,
            {(i//7, parameters.cols*(i % 7)+j): value for (i, j), value in third_map.todok().items()})
        residual = third_joint-third_joint[:, pivots]*reduced_z
        additions = []
        for a in range(64):
            block = residual[7*a:7*(a+1), :]
            vertices = cover({(i, j//parameters.cols) for i, j in block.todok()})
            if vertices and a not in selected:
                check_cover(block, parameters.cols, vertices)
                additions.append({'source_position': a, 'source_index': normal.KERNEL[a], 'cover': vertices})
                checks.append(('cover', block, parameters.cols, vertices))
        if additions:
            selected.update(r['source_position'] for r in additions)
            records.append({'kind': 'low_rank_sources', 'parameters': parameters.cols, 'sources': additions})
            continue
        cut_blocks, minor_records = [], []
        for label, matrix, count in (('original', z, rows), ('joint_row_basis', flat(reduced_z, parameters.cols), reduced_z.rows)):
            cuts, witnesses = forced_forms(matrix, count)
            if cuts.rows:
                cut_blocks.append(cuts)
            minor_records.append({'matrix': label, 'minors': witnesses})
            checks.extend(('minor', matrix, count, witness) for witness in witnesses)
        mixed_rows = [i for i in range(reduced_z.rows) if not any(reduced_z.row(i)[:6*parameters.cols])]
        if mixed_rows:
            cut_blocks.append(reduced_z[mixed_rows, 6*parameters.cols:])
        if not cut_blocks:
            break
        cuts = sp.MutableSparseMatrix.vstack(*cut_blocks)
        kernel, _ = normal.sparse_nullspace(cuts)
        if cuts*kernel != sp.zeros(cuts.rows, kernel.cols) or kernel.cols >= parameters.cols:
            raise ArithmeticError('Invalid forced normal reduction')
        records.append({'kind': 'forced_forms', 'before': parameters.cols, 'after': kernel.cols,
                        'minor_groups': minor_records, 'mixed_only_rows': mixed_rows,
                        'joint_row_basis': encode(reduced_z), 'kernel': encode(kernel)})
        parameters = parameters*kernel
    final = data['parameters']*parameters
    plane = frames.plane_parameters()
    if final.cols != 4 or third.matrix_rank(final) != 4 or third.matrix_rank(sp.Matrix.hstack(final, plane)) != 4:
        raise ArithmeticError('Remaining normals are not exactly the plane motions')
    if z.todok() or residual.todok():
        raise ArithmeticError('The final constraint or third residue is nonzero')
    return {'rounds': records, 'parameters': parameters, 'checks': checks, 'final': final,
            'selected_sources': [normal.KERNEL[a] for a in sorted(selected)]}


@lru_cache(None)
def report():
    data, result = source_data(), reduction()
    return {'claim': 'AI-MIXED-FIVE-SPACE-POINT-087', 'partner': [0, 0, 0, 1],
            'first_dimensions': [7, 5], 'mixed_projection_required': True,
            'normal_dimensions': [88]+[r['after'] for r in result['rounds'] if r['kind'] == 'forced_forms'],
            'virtual_c_residual_factor': encode(data['residual_factor']),
            'conditioned_psi_joint_basis': encode(data['psi_joint_basis']),
            'virtual_third_coefficients': encode(data['third']),
            'rounds': result['rounds'], 'selected_sources': result['selected_sources'],
            'final_parameter_basis': encode(result['parameters']),
            'final_normal_basis': encode(result['final']), 'final_is_plane_kernel': True,
            'scope': 'Exact normal closure at this partner point for every complex mixed five-space; no assertion for all partner lines or for the matrix exponent.'}


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
