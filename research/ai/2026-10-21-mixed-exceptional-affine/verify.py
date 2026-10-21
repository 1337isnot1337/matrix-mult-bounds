"""Affine rank-jump family and complete closure of its base graph."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('affine_generic_graph', HERE.parent / '2026-10-21-generic-mixed-graphs/verify.py')
generic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generic)
graph = generic.graph
pure, point, normal, third = graph.pure, graph.point, graph.normal, graph.third
X, Y, Z = sp.symbols('x y z')
PARAMETERS = (X, Y, Z)
LOCALS = dict(zip(('x', 'y', 'z'), PARAMETERS))
GRAPH = (X-Y, 1-X-Z, 1-X, X, Y, Z)


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): sp.sympify(value, locals=LOCALS)
        for i, j, value in record['entries']})


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


def check_left(matrix, record):
    left = decode(record['left'])
    if left.shape != (3, 28):
        raise ArithmeticError('Expected three polynomial left relations')
    for value in left.todok().values():
        if sp.Poly(value, *PARAMETERS, domain=sp.QQ).total_degree() > 2:
            raise ArithmeticError('Incorrect left-relation degree')
    if not generic.zero(left*matrix):
        raise ArithmeticError('The polynomial left relations fail')
    columns = record['point_columns']
    if len(columns) != 3 or len(set(columns)) != 3 or not set(columns) <= set(range(28)):
        raise ArithmeticError('Invalid left independence minor')
    value = generic.determinant(left[:, columns].subs(dict.fromkeys(PARAMETERS, 0)))
    if value != 4 or value != sp.Rational(record['point_determinant']):
        raise ArithmeticError('The left relations are not independent at the base point')
    return left


@lru_cache(None)
def source_data():
    data = generic.source_data()
    return {'base': sp.SparseMatrix(data['base'].subs(generic.A, 1)), 'plane': data['plane']}


@lru_cache(None)
def affine_data():
    base, cert = source_data()['base'], generic.certificate()
    records = certificate()['left_certificates']
    if ([sp.sympify(v, locals=LOCALS) for v in certificate()['graph']] != list(GRAPH)
            or [r['block'] for r in records] != [0, 1]):
        raise ArithmeticError('Incorrect affine graph or block coverage')
    reports = []
    for block, record in enumerate(records):
        columns = cert['normal_components'][block]
        selected = [i for i in cert['normal_minor']['rows'] if cert['source_row_groups'][i] == block]
        if selected != record['selected_rows'] or len(selected) != 28:
            raise ArithmeticError('Incorrect selected source rows')
        all_rows = [i for i, group in enumerate(cert['source_row_groups']) if group == block]
        parts = [base[[312*c+i for i in selected], columns] for c in range(7)]
        joint = sp.SparseMatrix.hstack(*parts)
        full = sp.SparseMatrix.hstack(*(base[[312*c+i for i in all_rows], columns] for c in range(7)))
        _, pivots = joint.to_DM().rref()
        pivots = list(pivots)
        if len(pivots) != 28:
            raise ArithmeticError('The selected global row chart is dependent')
        reconstruction = full[:, pivots]*joint[:, pivots].inv()
        if reconstruction*joint != full:
            raise ArithmeticError('The selected rows do not span all seven source blocks')
        mixed = parts[6]+sum((value*part for value, part in zip(GRAPH, parts[:6])), sp.zeros(28, 44))
        left = check_left(mixed, record)
        point_rank = len(mixed.subs(dict.fromkeys(PARAMETERS, 0)).to_DM().rref()[1])
        if point_rank != 25:
            raise ArithmeticError('Incorrect base-point component rank')
        reports.append({'block': block, 'global_row_chart': [28, 44],
                        'left_relations': left.rows, 'left_minor_at_base': '4',
                        'rank_upper_bound_everywhere': 25, 'rank_at_base': point_rank})
    return reports


def cuts_from_witnesses(matrix, rows, witnesses, size):
    cuts = []
    for witness in witnesses:
        if witness['size'] != size:
            raise ArithmeticError('Incorrect repeated minor size')
        pure.check_minor(matrix, rows, witness)
        cuts.append(sp.SparseMatrix(1, matrix.cols,
            {(0, j): sp.Rational(value) for j, value in witness['form']}))
    if not cuts:
        raise ArithmeticError('Empty repeated-minor reduction')
    return sp.SparseMatrix.vstack(*cuts)


@lru_cache(None)
def point_data():
    data = source_data()
    base, plane = data['base'], data['plane']
    mixed = base[1872:, :]+base[312:624, :]+base[624:936, :]
    kernel, free = normal.sparse_nullspace(mixed)
    if kernel.cols != 38 or kernel*plane[free, :] != plane:
        raise ArithmeticError('Incorrect complete 38-dimensional normal kernel')
    _, columns = plane[free, :].row_join(sp.eye(38)).to_DM().rref()
    quotient = kernel[:, [j-4 for j in columns[4:]]]
    obstruction = base*quotient
    if (obstruction[1872:, :]+obstruction[312:624, :]+obstruction[624:936, :]).todok():
        raise ArithmeticError('The actual mixed row is not annihilated')
    obstruction[1872:, :] = sp.zeros(312, 34)
    basis, _ = point.row_basis(point.joint(obstruction, 312))
    even = [68*j+k for j in range(3) for k in range(34)]
    odd = [68*j+34+k for j in range(3) for k in range(34)]
    projection = basis[:, odd]-basis[:, even]
    combinations, _ = normal.sparse_nullspace(projection.T)
    stable = combinations.T*basis
    stable_kernel, _ = normal.sparse_nullspace(pure.flat3(stable[:, even], 34))
    projected_rows, _ = point.row_basis(projection)
    projected = pure.flat3(projected_rows, 34)
    parameters, dimensions = sp.SparseMatrix.eye(34), [34]
    for record in certificate()['square_rounds']:
        cuts = cuts_from_witnesses(projected*parameters, projected_rows.rows, record['witnesses'], 2)
        reduced, _ = normal.sparse_nullspace(cuts)
        if record['before'] != parameters.cols or record['after'] != reduced.cols or reduced.cols >= parameters.cols:
            raise ArithmeticError('Incorrect square-minor reduction')
        parameters = parameters*reduced
        dimensions.append(parameters.cols)
    if ((basis.rows, stable.rows, stable_kernel.cols, parameters.cols) != (44, 14, 6, 14)
            or (projected*parameters).todok()):
        raise ArithmeticError('Incorrect stable/projection families')
    full = generic.uniform.data()
    tensor = sp.SparseMatrix(full['virtual']['third'].subs({generic.A: 1, generic.B: 1}))
    original = tensor.copy()
    for (i, j), value in original.todok().items():
        if i % 7 in (1, 2):
            tensor[7*(i//7)+6, j] += value
    first, second = sp.SparseMatrix.eye(64), sp.SparseMatrix.eye(64)
    for k, source in enumerate(normal.KERNEL):
        i, q, z = source//28, (source//7) % 4, source % 7
        if i == 2:
            first[normal.KERNEL.index(28+7*q+z), k] -= 1
        if q == 2:
            second[normal.KERNEL.index(28*i+7+z), k] += 1
    change = first*second
    if any(i >= j for i, j in (change-sp.eye(64)).todok()):
        raise ArithmeticError('The source change is not unitriangular')
    return {'basis': basis, 'third': graph.source_action(tensor*quotient, change),
            'families': [stable_kernel, parameters], 'square_dimensions': dimensions}


def replay_case(data, parameters, records):
    count = data['basis'].rows
    selected, dimensions = set(), [parameters.cols]
    base = point.flat(data['basis'], 34)
    for record in records:
        xp, jp = base*parameters, data['third']*parameters
        rows = count+7*len(selected)
        entries = {(rows*(i//count)+i % count, j): value for (i, j), value in xp.todok().items()}
        for k, source in enumerate(sorted(selected)):
            for (i, j), value in jp[49*source:49*(source+1), :].todok().items():
                b, c = divmod(i, 7)
                entries[rows*c+count+7*k+b, j] = value
        obstruction = sp.SparseMatrix(7*rows, parameters.cols, entries)
        mixed = obstruction[6*rows:, :]
        if record['kind'] == 'mixed_row':
            cuts = mixed
        else:
            if mixed.todok():
                raise ArithmeticError('The mixed equations were not imposed')
            reduced, pivots = point.row_basis(point.joint(obstruction, rows))
            if record['kind'] == 'cubic_minors':
                cuts = cuts_from_witnesses(point.flat(reduced, parameters.cols), reduced.rows, record['witnesses'], 3)
            elif record['kind'] == 'low_sources':
                if record['parameters'] != parameters.cols:
                    raise ArithmeticError('Incorrect low-source parameter count')
                joint = sp.SparseMatrix(448, 7*parameters.cols,
                    {(i//7, parameters.cols*(i % 7)+j): value for (i, j), value in jp.todok().items()})
                residual = joint-joint[:, pivots]*reduced
                for item in record['sources']:
                    source = item['source_position']
                    if source in selected or item['source_index'] != normal.KERNEL[source]:
                        raise ArithmeticError('Incorrect adapted source identity')
                    block = residual[7*source:7*(source+1), :]
                    bound = item['bound']
                    if 'cover' in bound:
                        point.check_cover(block, parameters.cols, bound['cover'])
                    elif third.matrix_rank(block) != bound['joint_B_rank'] or bound['joint_B_rank'] > 2:
                        raise ArithmeticError('The slice exceeds the target rank gap')
                    selected.add(source)
                continue
            else:
                raise ArithmeticError('Unknown terminal reduction')
        reduced, _ = normal.sparse_nullspace(cuts)
        if record['before'] != parameters.cols or record['after'] != reduced.cols or reduced.cols >= parameters.cols:
            raise ArithmeticError('Incorrect terminal reduction dimension')
        parameters = parameters*reduced
        dimensions.append(parameters.cols)
    if parameters.cols:
        raise ArithmeticError('A non-plane family remains')
    return dimensions


@lru_cache(None)
def report():
    affine, data = affine_data(), point_data()
    cases = certificate()['terminal_cases']
    if [c['case'] for c in cases] != ['stable', 'projection-rank-one'] or not all(c['closed'] for c in cases):
        raise ArithmeticError('Incomplete case coverage')
    dimensions = [replay_case(data, family, case['result']) for family, case in zip(data['families'], cases)]
    return {'claim': 'AI-MIXED-EXCEPTIONAL-AFFINE-095', 'partner': {'a': 1, 'b': 1},
            'affine_graph': [str(value) for value in GRAPH], 'affine_blocks': affine,
            'normal_dimension_at_least_everywhere': 38, 'generic_normal_dimension': 38,
            'base_graph': [0, 1, 1, 0, 0, 0], 'base_normal_dimension': 38,
            'plane_dimension': 4, 'base_quotient_dimension': 34, 'base_joint_rows': 44,
            'base_stable_rows': 14, 'square_dimensions': data['square_dimensions'],
            'terminal_dimensions': dimensions, 'base_target_excluded': True,
            'whole_affine_family_target_excluded': False, 'independent_review': False, 'improves_omega': False}


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
