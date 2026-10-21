"""All-graph exclusion on a nonempty open set of the partner parameter."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('generic_partner_previous', HERE.parent / '2026-10-21-all-mixed-graphs-a1/verify.py')
previous = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(previous)
generic, graph = previous.generic, previous.graph
uniform, frames = generic.uniform, generic.frames
normal, point, pure = previous.normal, previous.point, previous.pure
A, B = generic.A, generic.B
FIELD = sp.QQ.frac_field(A)
REFERENCE = sp.Integer(2)
rank_guards = []
denominators = set()


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): sp.sympify(value, locals={'a': A})
        for i, j, value in record['entries']})


def zero(matrix):
    return matrix.to_DM().convert_to(FIELD).is_zero_matrix


def multiply(left, right):
    return (left.to_DM().convert_to(FIELD)*right.to_DM().convert_to(FIELD)).to_Matrix()


def reference(matrix):
    entries = {}
    for (i, j), value in matrix.todok().items():
        value = sp.cancel(value)
        numerator, denominator = sp.fraction(value)
        sp.Poly(numerator, A, domain=sp.QQ)
        polynomial = sp.Poly(denominator, A, domain=sp.QQ)
        if polynomial.eval(REFERENCE) == 0:
            raise ArithmeticError('A coefficient has a pole at the reference partner')
        if polynomial.degree() > 0:
            denominators.add(str(sp.factor(denominator)))
        entries[i, j] = sp.Rational(value.subs(A, REFERENCE))
    return sp.SparseMatrix(*matrix.shape, entries)


def guard(matrix, rank, label):
    numeric = reference(matrix)
    point_rank = len(numeric.to_DM().rref()[1])
    if point_rank != rank:
        raise ArithmeticError('A generic rank fails at the reference partner: '+label)
    rank_guards.append({'label': label, 'shape': list(matrix.shape),
                        'generic_rank': rank, 'reference_rank': point_rank})
    return numeric


def row_basis(matrix, label):
    reduced, pivots = matrix.to_DM().convert_to(FIELD).rref()
    pivots = list(pivots)
    reduced = reduced.to_Matrix()[:len(pivots), :]
    numeric = guard(matrix, len(pivots), label)
    numeric_reduced, numeric_pivots = point.row_basis(numeric)
    if (pivots != list(numeric_pivots) or reference(reduced) != numeric_reduced
            or not zero(matrix-multiply(matrix[:, pivots], reduced))
            or reduced[:, pivots] != sp.eye(len(pivots))):
        raise ArithmeticError('The rational rowspace certificate fails: '+label)
    return reduced, pivots


def kernel(matrix, label):
    result, free = normal.sparse_nullspace(matrix)
    guard(matrix, matrix.cols-result.cols, label)
    reference(result)
    if result[free, :] != sp.eye(len(free)) or not zero(multiply(matrix, result)):
        raise ArithmeticError('The rational kernel certificate fails: '+label)
    return result


def span(minors, targets, label):
    reduced, pivots = row_basis(minors, label)
    reference(targets)
    if not zero(targets-multiply(targets[:, pivots], reduced)):
        raise ArithmeticError('The cubic target is outside the actual minor span')


def clear_rows(matrix):
    output = matrix.copy()
    for i in range(matrix.rows):
        denominator = sp.lcm([sp.denom(sp.cancel(value)) for value in matrix[i, :].todok().values()])
        if denominator != 1:
            output[i, :] = matrix[i, :].applyfunc(lambda value: sp.cancel(denominator*value))
    reference(output)
    return output


def minor_cuts(matrix, rows, witnesses, size):
    cuts = []
    for witness in witnesses:
        if witness['size'] != size:
            raise ArithmeticError('Incorrect repeated minor size')
        pure.check_minor(matrix, rows, witness)
        cuts.append(sp.SparseMatrix(1, matrix.cols,
            {(0, j): sp.sympify(value, locals={'a': A}) for j, value in witness['form']}))
    if not cuts:
        raise ArithmeticError('Empty minor reduction')
    return sp.SparseMatrix.vstack(*cuts)


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def data():
    source = generic.source_data()
    base, plane = source['base'], source['plane']
    _, columns = plane.row_join(sp.eye(88)).to_DM().rref()
    quotient = sp.SparseMatrix.eye(88)[:, [j-4 for j in columns[4:]]]
    # The shared partition helper uses only this constant plane complement.
    if quotient != previous.data()['quotient']:
        raise ArithmeticError('The constant source complement changed')
    selected = generic.certificate()['selected_rows']
    obstruction = sp.SparseMatrix.vstack(*(base[[312*c+i for i in selected], :]*quotient for c in range(7)))
    basis, _, _ = uniform.polynomial_row_basis(point.joint(obstruction, 56))
    even = [168*j+k for j in range(3) for k in range(84)]
    odd = [168*j+84+k for j in range(3) for k in range(84)]
    projection = uniform.expand(basis[:, odd]-A**3*basis[:, even])
    combinations, _ = uniform.hyper.uniform_kernel(projection.T)
    stable = uniform.expand(combinations.T*basis)
    stable_kernel, _ = uniform.hyper.uniform_kernel(pure.flat3(stable[:, even], 84))
    projected_rows, _, _ = uniform.polynomial_row_basis(projection)
    projected = pure.flat3(projected_rows, 84)
    parameters = sp.SparseMatrix.eye(84)
    dimensions = [84]
    for record in certificate()['projection_square_rounds']:
        cuts = minor_cuts(uniform.expand(projected*parameters), projected_rows.rows, record['witnesses'], 2)
        reduced, _ = uniform.hyper.uniform_kernel(cuts)
        if record['before'] != parameters.cols or record['after'] != reduced.cols:
            raise ArithmeticError('Incorrect uniform projection reduction')
        parameters = uniform.expand(parameters*reduced)
        dimensions.append(parameters.cols)
    if (basis.rows, stable.rows, stable_kernel.cols, dimensions) != (56, 10, 54, [84, 64, 48]):
        raise ArithmeticError('Incorrect all-parameter initial enclosure')
    tensor = sp.SparseMatrix(uniform.data()['virtual']['third'].subs(B, 1))
    first, second = sp.SparseMatrix.eye(64), sp.SparseMatrix.eye(64)
    for k, source_index in enumerate(normal.KERNEL):
        i, q, z = source_index//28, (source_index//7) % 4, source_index % 7
        if i == 2:
            first[normal.KERNEL.index(28+7*q+z), k] -= A
        if q == 2:
            second[normal.KERNEL.index(28*i+7+z), k] += 1
    change = first*second
    if any(i >= j for i, j in (change-sp.eye(64)).todok()):
        raise ArithmeticError('The polynomial source change is not unitriangular')
    return {'obstruction': obstruction, 'third': graph.source_action(tensor*quotient, change),
            'families': [stable_kernel, parameters], 'projection_dimensions': dimensions}


def source_rows(parameters, selected, label):
    n = parameters.cols
    full = multiply(data()['third'], parameters)
    joint = sp.SparseMatrix(448, 7*n,
        {(i//7, n*(i % 7)+j): value for (i, j), value in full.todok().items()})
    known = sp.SparseMatrix.vstack(point.joint(multiply(data()['obstruction'], parameters), 56),
        *[joint[7*i:7*(i+1), :] for i in sorted(selected)])
    basis, pivots = row_basis(known, label)
    return basis, pivots, joint


def replay(parameters, selected, records, label):
    selected, dimensions = set(selected), [parameters.cols]
    for i, record in enumerate(records):
        n, stage = parameters.cols, label+'/'+str(i)
        basis, pivots, joint = source_rows(parameters, selected, stage+'/known')
        if record['kind'] == 'mixed_only':
            combinations = kernel(basis[:, :6*n].T, stage+'/boundary')
            cuts = multiply(combinations.T, basis[:, 6*n:])
        elif record['kind'] == 'cubic_minors':
            cuts = minor_cuts(point.flat(clear_rows(basis), n), basis.rows, record['witnesses'], 3)
        elif record['kind'] == 'low_sources':
            if record['parameters'] != n:
                raise ArithmeticError('Incorrect low-source parameter count')
            residual = joint-multiply(joint[:, pivots], basis)
            reference(residual)
            for item in record['sources']:
                source_index = item['source_position']
                if (not 0 <= source_index < 64 or source_index in selected
                        or item['source_index'] != normal.KERNEL[source_index]):
                    raise ArithmeticError('Invalid adapted source identity')
                block = residual[7*source_index:7*(source_index+1), :]
                bound = item['bound']
                if 'cover' in bound:
                    point.check_cover(block, n, bound['cover'])
                elif (len(block.to_DM().convert_to(FIELD).rref()[1]) != bound['joint_B_rank']
                      or bound['joint_B_rank'] > 2):
                    raise ArithmeticError('The source slice exceeds the target rank gap')
                selected.add(source_index)
            continue
        else:
            raise ArithmeticError('Unknown source reduction')
        reduced = kernel(cuts, stage+'/cuts')
        if record['before'] != n or record['after'] != reduced.cols or reduced.cols >= n:
            raise ArithmeticError('Incorrect source reduction dimension')
        parameters = multiply(parameters, reduced)
        dimensions.append(parameters.cols)
    return parameters, selected, dimensions


def linear_cubes(parameters, selected, records, label):
    if [r['group'] for r in records] != [0, 1]:
        raise ArithmeticError('Both cubic blocks must be covered')
    basis, _, _ = source_rows(parameters, selected, label+'/known')
    cuts, covered = [], []
    for record in records:
        columns, rows = previous.partition(parameters, basis, record)
        covered.extend(columns)
        minors = previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
        forms = decode(record['forms'])
        variables = sp.symbols('x0:'+str(len(columns)))
        targets = previous.polynomial_rows([f**3 for f in forms*sp.Matrix(variables)], variables)
        span(minors, targets, label+'/span'+str(record['group']))
        cuts.append(sp.SparseMatrix(forms.rows, parameters.cols,
            {(i, columns[j]): value for (i, j), value in forms.todok().items()}))
    if sorted(covered) != list(range(parameters.cols)):
        raise ArithmeticError('The cubic source partition omits parameters')
    return multiply(parameters, kernel(sp.SparseMatrix.vstack(*cuts), label+'/linear_forms'))


def stable_branches(parameters, selected):
    records = certificate()['stable_branch_certificates']
    if parameters.cols != 6 or [r['group'] for r in records] != [0, 1]:
        raise ArithmeticError('Incorrect stable branch coverage')
    basis, _, _ = source_rows(parameters, selected, 'branches/known')
    groups = []
    u, v, w = sp.symbols('u v w')
    for record in records:
        columns, rows = previous.partition(parameters, basis, record)
        plane, line = decode(record['plane']), decode(record['line'])
        if len(columns) != 3 or plane != sp.Matrix([[0, 1, -A**3]]) or line != sp.Matrix([[1, 1, 0], [-1, 0, 1]]):
            raise ArithmeticError('Incorrect parameter-dependent branch equations')
        minors = previous.cubic_coefficients(basis, columns, rows, record['witnesses'])
        ell = (plane*sp.Matrix([u, v, w]))[0]
        targets = previous.polynomial_rows([ell*f**2 for f in line*sp.Matrix([u, v, w])], (u, v, w))
        span(minors, targets, 'branches/span'+str(record['group']))
        groups.append(columns)
    output = []
    from itertools import product
    for modes in product(('A', 'B'), repeat=2):
        cuts = []
        for columns, mode in zip(groups, modes):
            matrix = sp.Matrix([[0, 1, -A**3]]) if mode == 'A' else sp.Matrix([[1, 1, 0], [-1, 0, 1]])
            cuts.append(sp.SparseMatrix(matrix.rows, 6,
                {(i, columns[j]): value for (i, j), value in matrix.todok().items()}))
        name = 'stable-'+''.join(modes)
        output.append((name, multiply(parameters, kernel(sp.SparseMatrix.vstack(*cuts), name+'/branch'))))
    return output


@lru_cache(None)
def report():
    rank_guards.clear()
    denominators.clear()
    cert, original = certificate(), data()
    if ([r['case'] for r in cert['initial_source_cases']] != ['stable', 'rank-one-projection']
            or [r['case'] for r in cert['after_linear_source_cases']] != ['stable', 'rank-one-projection']):
        raise ArithmeticError('Incomplete initial family coverage')
    traces, stable = [], None
    for family, record, later in zip(original['families'], cert['initial_source_cases'], cert['after_linear_source_cases']):
        name = record['case']
        parameters, selected, dimensions = replay(family, set(), record['records'], name+'/initial')
        if sorted(selected) != record['selected_sources']:
            raise ArithmeticError('Incorrect initial source set')
        cubes = [r for r in cert['linear_cube_cases'] if r['case'] == name]
        parameters = linear_cubes(parameters, selected, cubes, name+'/cubes')
        dimensions.append(parameters.cols)
        parameters, selected, rest = replay(parameters, selected, later['records'], name+'/later')
        if sorted(selected) != later['selected_sources']:
            raise ArithmeticError('Incorrect later source set')
        dimensions.extend(rest[1:])
        traces.append({'case': name, 'dimensions': dimensions})
        if name == 'stable':
            stable = (parameters, selected)
        elif parameters.cols:
            raise ArithmeticError('The rank-one family remains')
    branches, records = stable_branches(*stable), cert['stable_terminal_branches']
    if [r['case'] for r in records] != [name for name, _ in branches]:
        raise ArithmeticError('The four stable branches are not covered')
    terminal = []
    for (name, parameters), record in zip(branches, records):
        remaining, selected, dimensions = replay(parameters, stable[1], record['records'], name+'/terminal')
        if remaining.cols or sorted(selected) != record['selected_sources']:
            raise ArithmeticError('A stable branch remains')
        terminal.append({'case': name, 'dimensions': dimensions})
    generic.check_torus(generic.certificate()['torus_boundary_weights'], generic.certificate()['torus_mixed_weight'])
    return {'claim': 'AI-GENERIC-PARTNER-ALL-GRAPHS-098', 'partner_chart': 'b=1',
            'rational_function_field': 'Q(a)', 'good_partner_reference': 2,
            'all_graphs_for_every_good_partner': True, 'arbitrary_boundary_four_space': True,
            'good_set_definition': 'All recorded coefficient denominators are nonzero and every guarded matrix has its recorded generic rank',
            'good_set_nonempty_zariski_open': True, 'partner_complement_finite': True,
            'projection_reductions_all_a': original['projection_dimensions'],
            'initial_source_traces': traces, 'stable_terminal_traces': terminal,
            'coefficient_denominators': sorted(denominators), 'rank_guards': list(rank_guards),
            'plane_dimension': 4, 'final_nonplane_dimension': 0,
            'all_graph_targets_excluded_on_good_set': True, 'extends_by_ratio_a_over_b': True,
            'exceptional_partners_classified': False, 'independent_review': False, 'improves_omega': False}


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
