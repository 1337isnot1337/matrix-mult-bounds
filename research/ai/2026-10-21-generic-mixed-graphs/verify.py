"""Source-level certificate for an open set of all mixed graph parameters."""
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


graph = load('generic_graph_source', HERE.parent / '2026-10-21-mixed-five-space-graphs/verify.py')
macaulay = load('generic_graph_macaulay', HERE / 'macaulay.py')
uniform, frames, normal = graph.uniform, graph.frames, graph.normal
A, B = frames.A, frames.B
LAMBDA = sp.Symbol('lam', nonzero=True)
encode = uniform.encode


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): sp.Rational(value) for i, j, value in record['entries']})


def zero(matrix):
    return all(sp.expand(value) == 0 for value in matrix.todok().values())


def determinant(matrix):
    dm = matrix.to_DM()
    return dm.domain.to_sympy(dm.det())


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


def check_source_blocks(base, components, row_groups):
    if (len(components) != 2 or any(len(c) != 44 for c in components)
            or sorted(j for c in components for j in c) != list(range(88))
            or len(row_groups) != 312):
        raise ArithmeticError('Incorrect symbolic source partition')
    groups = {j: k for k, component in enumerate(components) for j in component}
    for (i, j), value in base.todok().items():
        if row_groups[i % 312] != groups[j]:
            raise ArithmeticError('Nonzero cross-block source coefficient')
        sp.Poly(value, A, domain=sp.QQ)
    return groups


@lru_cache(None)
def source_data():
    full, cert = uniform.data(), certificate()
    psi = sp.SparseMatrix(full['virtual']['psi'].subs(B, 1))
    tensor = sp.SparseMatrix(full['virtual']['third'].subs(B, 1))
    sources = sp.SparseMatrix(full['sources'].subs(B, 1))
    low = graph.source_action(tensor, sources)
    entries = {(312*(i//200)+i % 200, j): value for (i, j), value in psi.todok().items()}
    for source in range(16):
        for (i, j), value in low[49*source:49*(source+1), :].todok().items():
            b, c = divmod(i, 7)
            entries[312*c+200+7*source+b, j] = sp.expand(value)
    base = sp.SparseMatrix(2184, 88, entries)
    groups = check_source_blocks(base, cert['normal_components'], cert['source_row_groups'])
    plane = frames.plane_parameters()[full['normal_certificate']['free_coordinates'], :]
    if (any(value.free_symbols for value in plane.todok().values())
            or not zero(base*plane) or not zero(tensor*plane)):
        raise ArithmeticError('The four constant planes are not annihilated symbolically')
    plane_groups = []
    for j in range(4):
        supported = {groups[i] for i in range(88) if plane[i, j]}
        if len(supported) != 1:
            raise ArithmeticError('Plane coordinates mix the two source blocks')
        plane_groups.append(supported.pop())
    if sorted(plane_groups) != [0, 0, 1, 1]:
        raise ArithmeticError('Incorrect plane count in each block')
    return {'base': base, 'plane': plane, 'groups': groups}


@lru_cache(None)
def point_data():
    data, cert = source_data(), certificate()
    point = cert['point']
    if point != {'a': 1, 'b': 1, 'graph': [1, 2, 0, 0, 0, 0]}:
        raise ArithmeticError('Unexpected rational witness point')
    base = data['base'].subs(A, 1)
    mixed = base[1872:, :]+sum((h*base[312*j:312*(j+1), :]
        for j, h in enumerate(point['graph'])), sp.zeros(312, 88))
    minor = cert['normal_minor']
    rows, columns = minor['rows'], minor['columns']
    if (len(rows) != 56 or len(set(rows)) != 56 or not set(rows) <= set(range(312))
            or len(columns) != 56 or len(set(columns)) != 56 or not set(columns) <= set(range(88))):
        raise ArithmeticError('Expected a fixed rank56 normal minor')
    free = sorted(set(range(88))-set(columns))
    groups, row_groups = data['groups'], cert['source_row_groups']
    for group in range(2):
        if (sum(row_groups[i] == group for i in rows) != 28
                or sum(groups[j] == group for j in columns) != 28
                or sum(groups[j] == group for j in free) != 16):
            raise ArithmeticError('The fixed normal minor does not preserve the blocks')
    pivot = mixed[rows, columns]
    det = determinant(pivot)
    if det != sp.Rational(minor['point_determinant']) or not macaulay.field_value(det, cert['prime']):
        raise ArithmeticError('The point normal minor is not a modular unit')
    reduced = -(pivot.to_DM().convert_to(sp.QQ).inv()*mixed[rows, free].to_DM().convert_to(sp.QQ)).to_Matrix()
    kernel = sp.MutableSparseMatrix.zeros(88, 32)
    for j, column in enumerate(free):
        kernel[column, j] = 1
        for i, old in enumerate(columns):
            kernel[old, j] = reduced[i, j]
    plane_free = data['plane'][free, :]
    if kernel*plane_free != data['plane']:
        raise ArithmeticError('Incorrect plane lift in the fixed normal chart')
    constant = decode(cert['constant_free_frame'])
    if constant.shape != (32, 28):
        raise ArithmeticError('Incorrect constant quotient frame')
    basis_det = determinant(plane_free.row_join(constant))
    if not macaulay.field_value(basis_det, cert['prime']):
        raise ArithmeticError('The constant plane complement is not a modular unit')
    quotient_groups = []
    for j in range(28):
        supported = {groups[free[i]] for i in range(32) if constant[i, j]}
        if len(supported) != 1:
            raise ArithmeticError('A constant quotient coordinate mixes source blocks')
        quotient_groups.append(supported.pop())
    quotient = kernel*constant
    if not zero(mixed*quotient):
        raise ArithmeticError('The rational witness point misses mixed-row equations')
    selected = cert['selected_rows']
    if len(selected) != 56 or len(set(selected)) != 56 or not set(selected) <= set(range(312)):
        raise ArithmeticError('Incorrect selected obstruction rows')
    parts = [base[[312*c+i for i in selected], :]*quotient for c in range(6)]
    cases = cert['span_cases']
    if (len(cases) != 2 or sorted(j for c in cases for j in c['component']['parameters']) != list(range(28))
            or sorted(i for c in cases for i in c['component']['rows']) != list(range(56))):
        raise ArithmeticError('The two minor blocks do not cover all quotient coordinates')
    for case in cases:
        component = case['component']
        source_groups = {row_groups[selected[i]] for i in component['rows']}
        normal_groups = {quotient_groups[j] for j in component['parameters']}
        if len(source_groups) != 1 or source_groups != normal_groups:
            raise ArithmeticError('The symbolic and minor block coordinates disagree')
        outside = sorted(set(range(28))-set(component['parameters']))
        if any(part[component['rows'], outside].todok() for part in parts):
            raise ArithmeticError('The point obstruction has nonzero cross-block entries')
    return {'parts': parts, 'normal_minor': str(det), 'basis_determinant': str(basis_det),
            'constant_free_frame': constant}


def check_torus(boundary_weights, mixed_weight=7):
    if len(boundary_weights) != 6:
        raise ArithmeticError('Incorrect torus weight count')
    weights = list(boundary_weights)+[mixed_weight]
    left, right = frames.chart_frames()
    original = normal.data()
    for coordinates, basis in ((left, original['E_B_complement']), (right, original['E_C_complement'])):
        covectors = frames.covectors(coordinates, basis)
        for j, covector in enumerate(covectors):
            for index, value in covector.items():
                i, q, z = index//28, (index//7) % 4, index % 7
                transformed = LAMBDA**(i+q+z)*value
                expected = LAMBDA**weights[j]*value.subs({A: A/LAMBDA, B: B/LAMBDA})
                if sp.expand(transformed-expected) != 0:
                    raise ArithmeticError('Incorrect graph-frame torus covariance')


@lru_cache(None)
def report():
    point, cert = point_data(), certificate()
    spans = [macaulay.span_report(point['parts'], case, cert['prime']) for case in cert['span_cases']]
    check_torus(cert['torus_boundary_weights'], cert['torus_mixed_weight'])
    return {'claim': 'AI-GENERIC-MIXED-GRAPHS-094', 'rational_witness': cert['point'],
            'normal_minor_at_point': point['normal_minor'], 'constant_basis_determinant': point['basis_determinant'],
            'normal_variables': 88, 'fixed_necessary_equations': 56, 'plane_directions': 4,
            'quotient_dimensions': [14, 14], 'spans': spans,
            'open_parameter_space_at_b_one': ['a', 'h0', 'h1', 'h2', 'h3', 'h4', 'h5'],
            'open_set_definition': 'Fixed normal determinant nonzero and both degree-four Macaulay matrices have column rank2380',
            'nonempty_open_set_proved': True, 'point_target_excluded': True,
            'extends_to_b_nonzero_by_torus': True,
            'normalized_graph': ['h0/b**5', 'h1/b**2', 'h2/b**2', 'b*h3', 'b*h4', 'b**4*h5'],
            'all_graphs_classified': False, 'independent_review': False, 'improves_omega': False}


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
