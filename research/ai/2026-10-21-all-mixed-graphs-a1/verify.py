"""Exact source-stage closure of every mixed graph at a=b=1."""
import argparse
from functools import lru_cache
import importlib.util
from itertools import combinations_with_replacement, permutations, product
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('all_graph_dichotomy', HERE.parent / '2026-10-21-global-mixed-normal-dichotomy/verify.py')
dichotomy = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dichotomy)
generic, graph = dichotomy.generic, dichotomy.graph
point, pure, normal = dichotomy.point, dichotomy.pure, dichotomy.normal
decode = dichotomy.decode


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def data():
    original = dichotomy.data()
    base, quotient = original['base'], original['quotient']
    selected = generic.certificate()['selected_rows']
    obstruction = sp.SparseMatrix.vstack(*(base[[312*c+i for i in selected], :]*quotient for c in range(7)))
    tensor = sp.SparseMatrix(generic.uniform.data()['virtual']['third'].subs({generic.A: 1, generic.B: 1}))
    first, second = sp.SparseMatrix.eye(64), sp.SparseMatrix.eye(64)
    for k, source in enumerate(normal.KERNEL):
        i, q, z = source//28, (source//7) % 4, source % 7
        if i == 2:
            first[normal.KERNEL.index(28+7*q+z), k] -= 1
        if q == 2:
            second[normal.KERNEL.index(28*i+7+z), k] += 1
    change = first*second
    if any(i >= j for i, j in (change-sp.eye(64)).todok()):
        raise ArithmeticError('The adapted source change is not unitriangular')
    return {'obstruction': obstruction, 'third': graph.source_action(tensor*quotient, change),
            'quotient': quotient, 'families': [original['stable_kernel'], original['zero_projection_kernel']]}


def source_rows(parameters, selected):
    n = parameters.cols
    full = data()['third']*parameters
    joint = sp.SparseMatrix(448, 7*n,
        {(i//7, n*(i % 7)+j): value for (i, j), value in full.todok().items()})
    known = sp.SparseMatrix.vstack(point.joint(data()['obstruction']*parameters, 56),
        *[joint[7*i:7*(i+1), :] for i in sorted(selected)])
    basis, pivots = point.row_basis(known)
    return basis, pivots, joint


def replay(parameters, selected, records):
    selected, dimensions = set(selected), [parameters.cols]
    for record in records:
        n = parameters.cols
        basis, pivots, joint = source_rows(parameters, selected)
        if record['kind'] == 'mixed_only':
            combinations, _ = normal.sparse_nullspace(basis[:, :6*n].T)
            cuts = combinations.T*basis[:, 6*n:]
        elif record['kind'] == 'cubic_minors':
            cuts = dichotomy.affine.cuts_from_witnesses(point.flat(basis, n), basis.rows, record['witnesses'], 3)
        elif record['kind'] == 'low_sources':
            if record['parameters'] != n:
                raise ArithmeticError('Incorrect low-source parameter count')
            residual = joint-joint[:, pivots]*basis
            for item in record['sources']:
                source = item['source_position']
                if (not 0 <= source < 64 or source in selected
                        or item['source_index'] != normal.KERNEL[source]):
                    raise ArithmeticError('Invalid adapted source identity')
                block = residual[7*source:7*(source+1), :]
                bound = item['bound']
                if 'cover' in bound:
                    point.check_cover(block, n, bound['cover'])
                elif (graph.third.matrix_rank(block) != bound['joint_B_rank']
                      or bound['joint_B_rank'] > 2):
                    raise ArithmeticError('The slice exceeds the target rank gap')
                selected.add(source)
            continue
        else:
            raise ArithmeticError('Unknown source-stage reduction')
        kernel, _ = normal.sparse_nullspace(cuts)
        if record['before'] != n or record['after'] != kernel.cols or kernel.cols >= n:
            raise ArithmeticError('Incorrect complete source-stage kernel')
        parameters = parameters*kernel
        dimensions.append(parameters.cols)
    return parameters, selected, dimensions


def partition(parameters, basis, record):
    embedding = data()['quotient']*parameters
    groups = {i: k for k, group in enumerate(generic.certificate()['normal_components']) for i in group}
    column_groups = []
    for j in range(parameters.cols):
        supported = {groups[i] for i in range(88) if embedding[i, j]}
        if len(supported) != 1:
            raise ArithmeticError('A terminal parameter mixes source blocks')
        column_groups.append(supported.pop())
    group = record['group']
    columns = [j for j, k in enumerate(column_groups) if k == group]
    rows = []
    for i in range(basis.rows):
        supported = {column_groups[j % parameters.cols] for (_, j), value in basis[i:i+1, :].todok().items()}
        if len(supported) != 1:
            raise ArithmeticError('A terminal source row mixes blocks')
        if supported == {group}:
            rows.append(i)
    if columns != record['normal_parameters'] or rows != record['source_rows']:
        raise ArithmeticError('Incorrect terminal block partition')
    return columns, rows


def cubic_coefficients(basis, columns, rows, witnesses):
    n = len(columns)
    monomials = list(combinations_with_replacement(range(n), 3))
    indices = {m: k for k, m in enumerate(monomials)}
    full_n = basis.cols//7
    cells = {(i, c): {j: basis[old, full_n*c+column] for j, column in enumerate(columns)
                     if basis[old, full_n*c+column]} for i, old in enumerate(rows) for c in range(7)}
    signed = [(p, (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)))
              for p in permutations(range(3))]
    entries = {}
    for k, witness in enumerate(witnesses):
        rr, cc = witness['rows'], witness['columns']
        if (len(rr) != 3 or len(set(rr)) != 3 or not set(rr) <= set(range(len(rows)))
                or len(cc) != 3 or len(set(cc)) != 3 or not set(cc) <= set(range(7))):
            raise ArithmeticError('Invalid terminal cubic minor')
        for permutation, sign in signed:
            first, second, third = [cells[rr[i], cc[permutation[i]]] for i in range(3)]
            for u, x in first.items():
                for v, y in second.items():
                    for w, z in third.items():
                        key = (k, indices[tuple(sorted((u, v, w)))])
                        entries[key] = entries.get(key, 0)+sign*x*y*z
    return sp.SparseMatrix(len(witnesses), len(monomials), entries)


def polynomial_rows(polynomials, variables):
    monomials = [sp.prod(variables[i] for i in indices)
                 for indices in combinations_with_replacement(range(len(variables)), 3)]
    return sp.Matrix([[sp.Poly(sp.expand(f), *variables).coeff_monomial(m) for m in monomials]
                      for f in polynomials])


def check_span(coefficients, minors, targets):
    if coefficients.rows != targets.rows or coefficients.cols != minors.rows or coefficients*minors != targets:
        raise ArithmeticError('The exact cubic span identity fails')


def linear_cubes(parameters, selected, records):
    if [r['group'] for r in records] != [0, 1] or not all(r['all_cubes_proved'] for r in records):
        raise ArithmeticError('Incomplete linear-cube source coverage')
    basis, _, _ = source_rows(parameters, selected)
    cuts, covered = [], []
    for record in records:
        columns, rows = partition(parameters, basis, record)
        covered.extend(columns)
        minors = cubic_coefficients(basis, columns, rows, record['witnesses'])
        forms, coefficients = decode(record['forms']), decode(record['cube_coefficients'])
        variables = sp.symbols('x0:'+str(len(columns)))
        polynomials = list(forms*sp.Matrix(variables))
        check_span(coefficients, minors, polynomial_rows([f**3 for f in polynomials], variables))
        if len(forms.to_DM().rref()[1]) != forms.rows:
            raise ArithmeticError('The forced linear forms are dependent')
        cuts.append(sp.SparseMatrix(forms.rows, parameters.cols,
            {(i, columns[j]): value for (i, j), value in forms.todok().items()}))
    if sorted(covered) != list(range(parameters.cols)):
        raise ArithmeticError('The terminal source partition omits parameters')
    kernel, _ = normal.sparse_nullspace(sp.SparseMatrix.vstack(*cuts))
    return parameters*kernel


def stable_branches(parameters, selected):
    records = certificate()['stable_branch_certificates']
    if parameters.cols != 6 or [r['group'] for r in records] != [0, 1]:
        raise ArithmeticError('Incorrect stable branch coverage')
    basis, _, _ = source_rows(parameters, selected)
    groups = []
    u, v, w = sp.symbols('u v w')
    for record in records:
        columns, rows = partition(parameters, basis, record)
        if len(columns) != 3:
            raise ArithmeticError('Expected three variables in each stable block')
        minors = cubic_coefficients(basis, columns, rows, record['witnesses'])
        targets = polynomial_rows([(v-w)**2*(v+w), (v-w)**2*(u-w)], (u, v, w))
        check_span(decode(record['coefficients']), minors, targets)
        groups.append(columns)
    branches = []
    for modes in product(('A', 'B'), repeat=2):
        cuts = []
        for columns, mode in zip(groups, modes):
            i, j, k = columns
            forms = [{j: 1, k: -1}] if mode == 'A' else [{j: 1, k: 1}, {i: 1, k: -1}]
            cuts.extend(sp.SparseMatrix(1, 6, {(0, j): value for j, value in form.items()}) for form in forms)
        kernel, _ = normal.sparse_nullspace(sp.SparseMatrix.vstack(*cuts))
        branches.append(('stable-'+''.join(modes), parameters*kernel))
    return branches


@lru_cache(None)
def report():
    dichotomy.report()
    generic.check_torus(generic.certificate()['torus_boundary_weights'], generic.certificate()['torus_mixed_weight'])
    cert = certificate()
    if ([r['case'] for r in cert['initial_source_cases']] != ['stable', 'projection-zero']
            or [r['case'] for r in cert['after_linear_source_cases']] != ['stable', 'projection-zero']):
        raise ArithmeticError('Both initial families must be covered')
    stable = None
    traces = []
    for family, record, after in zip(data()['families'], cert['initial_source_cases'], cert['after_linear_source_cases']):
        parameters, selected, dimensions = replay(family, set(), record['records'])
        if sorted(selected) != record['selected_sources']:
            raise ArithmeticError('Incorrect first-stage source set')
        cubes = [r for r in cert['linear_cube_cases'] if r['case'] == record['case']]
        parameters = linear_cubes(parameters, selected, cubes)
        dimensions.append(parameters.cols)
        parameters, selected, later = replay(parameters, selected, after['records'])
        if sorted(selected) != after['selected_sources']:
            raise ArithmeticError('Incorrect second-stage source set')
        dimensions.extend(later[1:])
        traces.append({'case': record['case'], 'dimensions': dimensions})
        if record['case'] == 'stable':
            stable = (parameters, selected)
        elif parameters.cols:
            raise ArithmeticError('The zero-projection family remains')
    terminals = cert['stable_terminal_branches']
    branches = stable_branches(*stable)
    if [r['case'] for r in terminals] != [name for name, _ in branches]:
        raise ArithmeticError('Incomplete four-branch coverage')
    terminal_traces = []
    for (name, parameters), record in zip(branches, terminals):
        remaining, selected, dimensions = replay(parameters, stable[1], record['records'])
        if remaining.cols or sorted(selected) != record['selected_sources']:
            raise ArithmeticError('A stable branch remains')
        terminal_traces.append({'case': name, 'dimensions': dimensions})
    return {'claim': 'AI-ALL-MIXED-GRAPHS-A1-097', 'partner': {'a': 1, 'b': 1},
            'all_six_graph_parameters_covered': True, 'arbitrary_boundary_four_space': True,
            'initial_source_traces': traces, 'stable_terminal_traces': terminal_traces,
            'final_nonplane_dimension': 0, 'plane_dimension': 4,
            'all_graph_targets_excluded_at_partner': True,
            'extends_to_a_equals_b_nonzero': True,
            'all_partners_classified': False, 'independent_review': False, 'improves_omega': False}


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
