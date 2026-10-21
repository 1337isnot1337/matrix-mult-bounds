"""Exact rank strata and exceptional-point closure on a two-coordinate graph."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('two_coordinate_graph', HERE.parent / '2026-10-21-mixed-five-space-graphs/verify.py')
graph = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(graph)
pure, point, normal, third = graph.pure, graph.point, graph.normal, graph.third
T, H = sp.symbols('t h')
LOCALS = {'t': T, 'h': H}
encode = graph.encode


def expression(value):
    return sp.sympify(value, locals=LOCALS)


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): expression(value) for i, j, value in record['entries']})


def determinant(matrix):
    domain_matrix = matrix.to_DM(extension=True)
    return domain_matrix.domain.to_sympy(domain_matrix.det())


def zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix.todok().values())


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def source_data():
    psi, tensor, sources, plane, change = graph.source_data()
    low = graph.source_action(tensor, sources)
    rows = 312
    entries = {(rows*(i//200)+i % 200, j): value for (i, j), value in psi.todok().items()}
    for source in range(16):
        for (i, j), value in low[49*source:49*(source+1), :].todok().items():
            b, c = divmod(i, 7)
            entries[rows*c+200+7*source+b, j] = value
    base = sp.SparseMatrix(7*rows, 88, entries)
    mixed = base[6*rows:, :]+T*base[:rows, :]+H*base[rows:2*rows, :]
    return {'base': base, 'mixed': mixed, 'plane': plane, 'tensor': tensor, 'change': change}


def check_kernel(matrix, kernel):
    if kernel.shape != (88, 32):
        raise ArithmeticError('Incorrect polynomial normal-frame size')
    for value in kernel.todok().values():
        sp.Poly(value, T, H, domain=sp.QQ)
    left, right = matrix.to_DM().unify(kernel.to_DM())
    if not (left*right).is_zero_matrix:
        raise ArithmeticError('Polynomial normal-kernel identity failed')
    if len(kernel.subs({T: 1, H: 2}).to_DM().rref()[1]) != 32:
        raise ArithmeticError('Polynomial normal frame is generically dependent')


def check_root_cover(polynomial, parameter, controls):
    roots = sp.roots(polynomial, parameter)
    if sum(roots.values()) != sp.degree(polynomial, parameter):
        raise ArithmeticError('Univariate exceptional roots are incomplete')
    given = [expression(c['value']) for c in controls]
    if len(given) != len(roots) or set(given) != set(roots):
        raise ArithmeticError('Exceptional root controls are incomplete')
    product = sp.Poly(polynomial, parameter).LC()*sp.prod((parameter-r)**m for r, m in roots.items())
    if sp.expand(polynomial-product) != 0:
        raise ArithmeticError('Incorrect complete root factorization')


@lru_cache(None)
def rank_data():
    data, cert = source_data(), certificate()
    matrix, kernel = data['mixed'], decode(cert['polynomial_kernel'])
    check_kernel(matrix, kernel)
    if kernel*decode(cert['plane_embedding']) != data['plane']:
        raise ArithmeticError('Incorrect constant plane embedding')
    generic = cert['generic_minor']
    if len(set(generic['rows'])) != 56 or len(set(generic['columns'])) != 56:
        raise ArithmeticError('Expected a rank56 generic minor')
    value = determinant(matrix[generic['rows'], generic['columns']])
    expected = T**10*(H-1)**2*(H+T)**4*(T-H**2)**4
    if sp.expand(value-expected) != 0 or sp.expand(expression(generic['determinant'])-expected) != 0:
        raise ArithmeticError('Incorrect generic normal-rank minor')
    matched = cert['generic_kernel_minor']
    kernel_det = determinant(kernel[matched['rows'], :])
    if (not expression(matched['ratio']).is_Rational or not expression(matched['ratio'])
            or sp.expand(kernel_det-expression(matched['determinant'])) != 0
            or sp.expand(value-expression(matched['ratio'])*kernel_det) != 0):
        raise ArithmeticError('Incorrect matched generic kernel minor')
    expected_loci = [{'h': '1'}, {'h': '-t'}, {'t': 'h**2'}, {'t': '0'}]
    if ([c['substitution'] for c in cert['rank_cover']] != expected_loci
            or len(cert['curve_kernel_minors']) != 4):
        raise ArithmeticError('The generic exceptional curves are not covered')
    controls = []
    for curve, matched in zip(cert['rank_cover'], cert['curve_kernel_minors']):
        substitution = {expression(k): expression(v) for k, v in curve['substitution'].items()}
        parameter = expression(curve['parameter'])
        if len(set(curve['rows'])) != 56 or len(set(curve['columns'])) != 56:
            raise ArithmeticError('Expected a rank56 curve minor')
        restricted, frame = matrix.subs(substitution), kernel.subs(substitution)
        value = determinant(restricted[curve['rows'], curve['columns']])
        if sp.expand(value-expression(curve['determinant'])) != 0:
            raise ArithmeticError('Incorrect curve rank minor')
        kernel_det = determinant(frame[matched['rows'], :])
        if (matched['locus'] != curve['locus'] or not expression(matched['ratio']).is_Rational
                or not expression(matched['ratio']) or sp.expand(kernel_det-expression(matched['determinant'])) != 0
                or sp.expand(value-expression(matched['ratio'])*kernel_det) != 0):
            raise ArithmeticError('Incorrect matched curve kernel minor')
        check_root_cover(value, parameter, curve['exception_controls'])
        for control in curve['exception_controls']:
            root = expression(control['value'])
            special = restricted.subs(parameter, root)
            actual = determinant(special[control['rows'], control['columns']])
            if actual == 0 or sp.simplify(actual-expression(control['determinant'])) != 0:
                raise ArithmeticError('Incorrect exceptional-point rank minor')
            rank = control['rank']
            if len(control['rows']) != rank or len(control['columns']) != rank:
                raise ArithmeticError('Incorrect exceptional-point minor size')
            frame_rank = len(frame.subs(parameter, root).to_DM(extension=True).rref()[1])
            if rank == 56:
                if frame_rank != 32:
                    raise ArithmeticError('Polynomial frame misses a regular exceptional-chart point')
            elif len(special.to_DM(extension=True).rref()[1]) != rank:
                raise ArithmeticError('Incorrect complete exceptional-point rank')
            tv, hv = [sp.sympify(substitution.get(x, x)).subs(parameter, root) for x in (T, H)]
            if rank != (52 if (tv, hv) == (0, 0) else 54 if (tv, hv) == (1, 1) else 56):
                raise ArithmeticError('An unrecorded rank stratum remains')
            controls.append({'t': str(tv), 'h': str(hv), 'rank': rank, 'frame_rank': frame_rank})
    return {'kernel': kernel, 'point_controls': controls}


def cuts_from_witnesses(matrix, rows, witnesses, size):
    forms = []
    for witness in witnesses:
        if witness['size'] != size:
            raise ArithmeticError('Incorrect minor size for the rank bound')
        pure.check_minor(matrix, rows, witness)
        forms.append(sp.SparseMatrix(1, matrix.cols, {(0, j): expression(value) for j, value in witness['form']}))
    return sp.SparseMatrix.vstack(*forms)


@lru_cache(None)
def exceptional_data():
    data = source_data()
    kernel, free = normal.sparse_nullspace(data['mixed'].subs({T: 1, H: 1}))
    if kernel.cols != 34 or kernel*data['plane'][free, :] != data['plane']:
        raise ArithmeticError('Incorrect exceptional normal kernel')
    _, columns = data['plane'][free, :].row_join(sp.eye(34)).to_DM().rref()
    quotient = kernel[:, [j-4 for j in columns[4:]]]
    obstruction = data['base']*quotient
    actual_mixed = obstruction[1872:, :]+obstruction[:312, :]+obstruction[312:624, :]
    if actual_mixed.todok():
        raise ArithmeticError('Exceptional actual mixed row is not annihilated')
    obstruction[1872:, :] = sp.zeros(312, 30)
    basis, _ = point.row_basis(point.joint(obstruction, 312))
    even = [60*j+k for j in range(3) for k in range(30)]
    odd = [60*j+30+k for j in range(3) for k in range(30)]
    projection = basis[:, odd]-basis[:, even]
    stable_combinations, _ = normal.sparse_nullspace(projection.T)
    stable = stable_combinations.T*basis
    stable_kernel, _ = normal.sparse_nullspace(pure.flat3(stable[:, even], 30))
    q_rows, _ = point.row_basis(projection)
    q = pure.flat3(q_rows, 30)
    parameters = sp.SparseMatrix.eye(30)
    for record in certificate()['square_rounds']:
        if parameters.cols != record['before']:
            raise ArithmeticError('Incorrect square-round dimension')
        cuts = cuts_from_witnesses(q*parameters, q_rows.rows, record['witnesses'], 2)
        reduced, _ = normal.sparse_nullspace(cuts)
        if reduced.cols != record['after']:
            raise ArithmeticError('Incorrect square-round kernel')
        parameters = parameters*reduced
    if (basis.rows, stable.rows, stable_kernel.cols, parameters.cols) != (56, 10, 16, 6):
        raise ArithmeticError('Incorrect exceptional case dimensions')
    tensor = data['tensor'].copy()
    for (i, j), value in data['tensor'].todok().items():
        if i % 7 in (0, 1):
            tensor[7*(i//7)+6, j] += value
    adapted = graph.source_action(tensor*quotient, data['change'])
    return {'basis': basis, 'third': adapted, 'families': [stable_kernel, parameters]}


def replay_case(data, parameters, records):
    selected, dimensions = set(), [parameters.cols]
    base = point.flat(data['basis'], 30)
    for record in records:
        xp, jp = base*parameters, data['third']*parameters
        rows = 56+7*len(selected)
        entries = {(rows*(i//56)+i % 56, j): value for (i, j), value in xp.todok().items()}
        for k, source in enumerate(sorted(selected)):
            for (i, j), value in jp[49*source:49*(source+1), :].todok().items():
                b, c = divmod(i, 7)
                entries[rows*c+56+7*k+b, j] = value
        obstruction = sp.SparseMatrix(7*rows, parameters.cols, entries)
        mixed = obstruction[6*rows:, :]
        if record['kind'] == 'mixed_row':
            cuts = mixed
        else:
            if mixed.todok():
                raise ArithmeticError('Mixed-row constraints were not imposed')
            reduced, pivots = point.row_basis(point.joint(obstruction, rows))
            if record['kind'] == 'cubic_minors':
                cuts = cuts_from_witnesses(point.flat(reduced, parameters.cols), reduced.rows, record['witnesses'], 3)
            elif record['kind'] == 'low_sources':
                if record['parameters'] != parameters.cols:
                    raise ArithmeticError('Incorrect low-source parameter dimension')
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
                        raise ArithmeticError('Source slice exceeds the target rank gap')
                    selected.add(source)
                continue
            else:
                raise ArithmeticError('Unknown terminal reduction')
        reduced, _ = normal.sparse_nullspace(cuts)
        if record['before'] != parameters.cols or record['after'] != reduced.cols or reduced.cols >= parameters.cols:
            raise ArithmeticError('Incorrect terminal kernel dimension')
        parameters = parameters*reduced
        dimensions.append(parameters.cols)
    if parameters.cols:
        raise ArithmeticError('Exceptional normal family remains')
    return dimensions


@lru_cache(None)
def report():
    ranks, exceptional = rank_data(), exceptional_data()
    cases = certificate()['exception_cases']
    if len(cases) != 2 or not all(c['closed'] for c in cases):
        raise ArithmeticError('Both exceptional families must be covered')
    dimensions = [replay_case(exceptional, parameters, case['result'])
                  for parameters, case in zip(exceptional['families'], cases)]
    return {'claim': 'AI-MIXED-TWO-COORDINATE-STRATA-093', 'partner': {'a': 1, 'b': 1},
            'mixed_row': 'm+t*d0+h*d1', 'field': 'complex numbers',
            'normal_dimension': {'generic_and_all_other_points': 32, 't=0,h=0': 36, 't=1,h=1': 34},
            'polynomial_frame': {'shape': [88, 32], 'degree': 4, 'complete_away_from': [[0, 0], [1, 1]]},
            'point_controls': ranks['point_controls'], 'exceptional_quotient_dimension': 30,
            'square_dimensions': [30]+[r['after'] for r in certificate()['square_rounds']],
            'exceptional_case_dimensions': dimensions, 'exceptional_target_excluded': True,
            'general_chart_target_excluded': False, 'independent_review': False, 'improves_omega': False}


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
