"""Uniform reduction of all mixed graphs at the partner a=b=1."""
import argparse
from functools import lru_cache
import importlib.util
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('dichotomy_affine', HERE.parent / '2026-10-21-mixed-exceptional-affine/verify.py')
affine = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(affine)
generic, graph = affine.generic, affine.graph
pure, point, normal = affine.pure, affine.point, affine.normal
H = sp.symbols('h0:6')
LOCALS = dict(zip(map(str, H), H))


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): sp.sympify(value, locals=LOCALS)
        for i, j, value in record['entries']})


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def data():
    source = affine.source_data()
    plane, base = source['plane'], source['base']
    _, columns = plane.row_join(sp.eye(88)).to_DM().rref()
    quotient = sp.SparseMatrix.eye(88)[:, [j-4 for j in columns[4:]]]
    if len(plane.row_join(quotient).to_DM().rref()[1]) != 88:
        raise ArithmeticError('Incorrect complement to the four planes')
    selected = generic.certificate()['selected_rows']
    parts = [base[[312*c+i for i in selected], :]*quotient for c in range(7)]
    obstruction = sp.SparseMatrix.vstack(*parts)
    basis, _ = point.row_basis(point.joint(obstruction, 56))
    if basis.rows != 56 or quotient.cols != 84:
        raise ArithmeticError('Incorrect global quotient or source row count')
    even = [168*j+k for j in range(3) for k in range(84)]
    odd = [168*j+84+k for j in range(3) for k in range(84)]
    projection = basis[:, odd]-basis[:, even]
    combinations, _ = normal.sparse_nullspace(projection.T)
    stable = combinations.T*basis
    stable_kernel, _ = normal.sparse_nullspace(pure.flat3(stable[:, even], 84))
    projected_rows, _ = point.row_basis(projection)
    projected = pure.flat3(projected_rows, 84)
    zero_kernel, _ = normal.sparse_nullspace(projected)
    if (stable.rows, stable_kernel.cols, projected_rows.rows, zero_kernel.cols) != (10, 54, 46, 36):
        raise ArithmeticError('Incorrect global stable/projection dimensions')
    return {'base': base, 'quotient': quotient, 'projection': projected,
            'projection_rows': projected_rows.rows, 'stable_kernel': stable_kernel,
            'zero_projection_kernel': zero_kernel}


def quadratic_coefficients(matrix, rows, witnesses):
    if matrix.cols != 12 or matrix.rows != 3*rows:
        raise ArithmeticError('Incorrect active projection matrix')
    monomials = list(combinations_with_replacement(range(12), 2))
    indices = {pair: k for k, pair in enumerate(monomials)}
    cells = [[{} for _ in range(3)] for _ in range(rows)]
    for (i, j), value in matrix.todok().items():
        cells[i % rows][i//rows][j] = sp.Rational(value)
    entries = {}
    for k, witness in enumerate(witnesses):
        i, j, c, d = witness
        if not (0 <= i < j < rows and 0 <= c < d < 3):
            raise ArithmeticError('Invalid quadratic minor witness')
        for left, right, sign in ((c, d, 1), (d, c, -1)):
            for u, x in cells[i][left].items():
                for v, y in cells[j][right].items():
                    key = (k, indices[tuple(sorted((u, v)))])
                    entries[key] = entries.get(key, 0)+sign*x*y
    return sp.SparseMatrix(len(witnesses), len(monomials), entries)


def check_square_identities(matrix, forms, coefficients):
    if forms.shape != (8, 12) or coefficients.shape != (8, matrix.rows):
        raise ArithmeticError('Incorrect quadratic-span certificate shape')
    monomials = list(combinations_with_replacement(range(12), 2))
    squares = sp.SparseMatrix(8, len(monomials), {(i, k): forms[i, u]*forms[i, v]*(1 if u == v else 2)
        for i in range(8) for k, (u, v) in enumerate(monomials) if forms[i, u] and forms[i, v]})
    if coefficients*matrix != squares or len(forms.to_DM().rref()[1]) != 8:
        raise ArithmeticError('The eight exact square identities fail')


@lru_cache(None)
def rank_one_data():
    original, cert = data(), certificate()
    projected, rows = original['projection'], original['projection_rows']
    parameters, dimensions = sp.SparseMatrix.eye(84), [84]
    for record in cert['projection_square_rounds']:
        cuts = affine.cuts_from_witnesses(projected*parameters, rows, record['witnesses'], 2)
        kernel, _ = normal.sparse_nullspace(cuts)
        if record['before'] != parameters.cols or record['after'] != kernel.cols or kernel.cols >= parameters.cols:
            raise ArithmeticError('Incorrect initial projection-square reduction')
        parameters = parameters*kernel
        dimensions.append(parameters.cols)
    full = projected*parameters
    _, active = full.to_DM().rref()
    active = list(active)
    if dimensions != [84, 52, 48] or len(active) != 12:
        raise ArithmeticError('Incorrect active projection dimension')
    small = full[:, active]
    _, selected_rows = small.T.to_DM().rref()
    selected_rows = list(selected_rows)
    coordinates = small[selected_rows, :].inv()*full[selected_rows, :]
    if small*coordinates != full:
        raise ArithmeticError('The active projection coordinates are incomplete')
    coefficients = quadratic_coefficients(small, rows, cert['quadratic_witnesses'])
    forms, identities = decode(cert['forced_linear_forms']), decode(cert['square_coefficients'])
    check_square_identities(coefficients, forms, identities)
    kernel, _ = normal.sparse_nullspace(forms*coordinates)
    parameters = parameters*kernel
    if parameters.cols != 40:
        raise ArithmeticError('Incorrect post-quadratic family dimension')
    return {'parameters': parameters, 'dimensions': dimensions+[40],
            'projection': projected*parameters, 'quadratic_coefficients': coefficients,
            'forms': forms, 'square_coefficients': identities}


def check_mixed_identity(matrix, target, record):
    identity = decode(record['row_identity'])
    if identity.shape != (2, 25) or target.shape != (2, 20) or matrix.shape != (25, 20):
        raise ArithmeticError('Incorrect polynomial row-identity shape')
    for value in identity.todok().values():
        if sp.Poly(value, *H, domain=sp.QQ).total_degree() > 1:
            raise ArithmeticError('Incorrect row-identity degree')
    if not generic.zero(identity*matrix-target):
        raise ArithmeticError('The mixed equations do not imply zero projection')


@lru_cache(None)
def report():
    original, reduced, cert = data(), rank_one_data(), certificate()
    parameters = reduced['parameters']
    embedding = original['quotient']*parameters
    base = original['base']
    mixed = base[1872:, :]*embedding+sum((h*base[312*j:312*(j+1), :]*embedding
        for j, h in enumerate(H)), sp.zeros(312, 40))
    normal_groups = {i: k for k, group in enumerate(generic.certificate()['normal_components']) for i in group}
    records = cert['mixed_projection_identities']
    if [r['group'] for r in records] != [0, 1]:
        raise ArithmeticError('Both source groups must be covered')
    covered = []
    for record in records:
        group, columns, selected = record['group'], record['normal_columns'], record['source_rows']
        expected = [j for j in range(40) if {normal_groups[i] for i in range(88) if embedding[i, j]} == {group}]
        if columns != expected or len(columns) != 20 or len(set(selected)) != 25 or not set(selected) <= set(range(312)):
            raise ArithmeticError('Incorrect mixed-identity source partition')
        covered.extend(columns)
        target, _ = point.row_basis(reduced['projection'][:, columns])
        check_mixed_identity(mixed[selected, columns], target, record)
    if sorted(covered) != list(range(40)):
        raise ArithmeticError('The mixed identities omit normal coordinates')
    final, _ = normal.sparse_nullspace(reduced['projection'])
    if final.cols != 36 or len((parameters*final).row_join(original['zero_projection_kernel']).to_DM().rref()[1]) != 36:
        raise ArithmeticError('The zero-projection family is incomplete')
    return {'claim': 'AI-GLOBAL-MIXED-NORMAL-DICHOTOMY-096', 'partner': {'a': 1, 'b': 1},
            'graph_parameters': [str(h) for h in H], 'all_six_graph_parameters_covered': True,
            'raw_normal_dimension': 88, 'plane_dimension': 4, 'normal_quotient_dimension': 84,
            'stable_boundary_rows': 10, 'stable_zero_quotient_dimension': 54,
            'projection_zero_quotient_dimension': 36, 'rank_one_reductions': reduced['dimensions'],
            'active_projection_variables': 12, 'quadratic_witnesses': len(cert['quadratic_witnesses']),
            'exact_square_identities': 8, 'polynomial_mixed_identity_rows': 4,
            'rank_one_projection_forced_zero': True, 'remaining_linear_families': [54, 36],
            'target_excluded': False, 'independent_review': False, 'improves_omega': False}


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
