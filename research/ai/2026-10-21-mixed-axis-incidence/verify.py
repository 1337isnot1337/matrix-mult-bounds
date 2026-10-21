"""Exact auxiliary-projection certificate closing the mixed-row axis."""
import argparse
from functools import lru_cache
import importlib.util
import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('incidence_axis', HERE.parent / '2026-10-21-mixed-axis-family/verify.py')
axis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(axis)
A, T = axis.A, axis.T
U, ELL = sp.symbols('u ell')
canonical, encode = axis.canonical, axis.encode
LOCALS = {'a': A, 't': T, 'u': U, 'ell': ELL}


def expression(value):
    return sp.sympify(value, locals=LOCALS)


def decode(record):
    return sp.SparseMatrix(*record['shape'], {(i, j): expression(value) for i, j, value in record['entries']})


@lru_cache(None)
def certificate():
    return json.loads((HERE / 'certificate.json').read_text())


@lru_cache(None)
def block_data():
    selected, kernel = axis.initial_data()['selected'], axis.split_data()['w_kernel']
    parts = [canonical(selected[:, 28*j:28*(j+1)]*kernel) for j in range(6)]
    components = certificate()['components']
    if len(components) != 2 or sorted(j for c in components for j in c['parameters']) != list(range(10)):
        raise ArithmeticError('The two blocks do not partition the normal parameters')
    all_rows = [i for c in components for i in c['rows']]
    if len(all_rows) != 50 or len(set(all_rows)) != 50 or not set(all_rows) <= set(range(56)):
        raise ArithmeticError('Invalid block row partition')
    for comp in components:
        if len(comp['parameters']) != 5 or len(comp['rows']) != 25:
            raise ArithmeticError('Incorrect block size')
        outside = sorted(set(range(10))-set(comp['parameters']))
        if any(part[comp['rows'], outside].todok() for part in parts):
            raise ArithmeticError('Nonzero cross-block coefficient')
    extra = sorted(set(range(56))-set(all_rows))
    if any(part[extra, :].todok() for part in parts):
        raise ArithmeticError('Unaccounted obstruction rows')
    first, second = components
    blocks = [part[first['rows'], first['parameters']] for part in parts]
    permutation = certificate()['component_permutation']
    if sorted(permutation) != list(range(25)):
        raise ArithmeticError('Invalid component row permutation')
    for part, block in zip(parts, blocks):
        if canonical(part[second['rows'], second['parameters']]-block[permutation, :]).todok():
            raise ArithmeticError('The two blocks are not identical')
    pencil = canonical(T**3*sp.SparseMatrix.hstack(*(blocks[2*j+1]-ELL*blocks[2*j] for j in range(3))))
    entries = {}
    for position, value in pencil.todok().items():
        polynomial = sp.Poly(value, A, T, ELL, domain=sp.QQ)
        if any(m[0] % 3 for m in polynomial.monoms()):
            raise ArithmeticError('Pencil coefficient is not polynomial in a cubed')
        entries[position] = sum(c*U**(m[0]//3)*T**m[1]*ELL**m[2] for m, c in polynomial.terms())
    reduced = sp.SparseMatrix(*pencil.shape, entries)
    if canonical(reduced.subs(U, A**3)-pencil).todok():
        raise ArithmeticError('Incorrect a-cubed substitution')
    return {'parts': parts, 'pencil': reduced, 'extra_rows': extra}


def check_exception_factor(factor):
    polynomial = sp.Poly(factor, ELL)
    if polynomial.degree() != 2:
        raise ArithmeticError('Exceptional factor must be quadratic in ell')
    high, middle = polynomial.nth(2), polynomial.nth(1)
    if (sp.expand((U-1)*middle-(-2*U**2+3*U-2)*high-U) != 0
            or sp.expand(high.subs(U, 0)+T) != 0):
        raise ArithmeticError('Exceptional-factor coefficient certificate failed')


def check_rank_minor(pencil, record, exception):
    rows, columns = record['rows'], record['columns']
    if len(rows) != 13 or len(set(rows)) != 13 or len(columns) != 13 or len(set(columns)) != 13:
        raise ArithmeticError('Expected a thirteen-by-thirteen minor')
    scalar = expression(record['coefficient'])
    if not scalar.is_Rational or not scalar:
        raise ArithmeticError('Invalid determinant scalar')
    factors = [(expression(value), power) for value, power in record['factors']]
    for factor, power in factors:
        if not isinstance(power, int) or power <= 0:
            raise ArithmeticError('Invalid factor multiplicity')
        sp.Poly(factor, U, T, ELL, domain=sp.QQ)
        if sp.expand(factor-exception) == 0 or sp.expand(factor+exception) == 0:
            check_exception_factor(exception)
        elif not axis.linear.laurent(sp.Poly(factor, ELL).LC(), U, T, True):
            raise ArithmeticError('A determinant factor may vanish identically in ell')
    expected = scalar*sp.prod(factor**power for factor, power in factors)
    actual = pencil[rows, columns].to_DM().det().as_expr()
    if sp.expand(actual-expected) != 0:
        raise ArithmeticError('Incorrect polynomial rank determinant')
    return expected


def check_lower_minor_pair(h1, pair):
    if len(pair) != 2:
        raise ArithmeticError('Expected two lower-block minors')
    minors = []
    for item in pair:
        rows, columns = item['rows'], item['columns']
        if (len(rows) != 2 or len(set(rows)) != 2 or not set(rows) <= set(range(1, 5))
                or len(columns) != 2 or len(set(columns)) != 2 or not set(columns) <= set(range(3))):
            raise ArithmeticError('Invalid lower-block minor positions')
        minors.append(h1[rows, columns].det())
    if sp.expand(sum(minors).subs(ELL, U)-T**3) != 0:
        raise ArithmeticError('Lower-block minor sum is not t cubed')
    return minors


@lru_cache(None)
def incidence_data():
    pencil, cert = block_data()['pencil'], certificate()
    kernel = decode(cert['joint_kernel'])
    if kernel.shape != (15, 2):
        raise ArithmeticError('Incorrect joint-kernel dimensions')
    for value in kernel.todok().values():
        sp.Poly(value, U, T, ELL, domain=sp.QQ)
    if canonical(pencil*kernel).todok():
        raise ArithmeticError('Polynomial joint-kernel identity failed')
    h0 = sp.Matrix(5, 3, lambda i, j: kernel[5*j+i, 0])
    h1 = sp.Matrix(5, 3, lambda i, j: kernel[5*j+i, 1])
    expected = sp.zeros(5, 3)
    expected[0, :] = sp.Matrix([[U-ELL-1, 1, 0]])
    exception = expression(cert['exception_factor'])
    if h0 != expected or h1[0, 1] != 0 or sp.expand(h1[4, 2]+exception) != 0:
        raise ArithmeticError('Incorrect kernel normalization')
    check_exception_factor(exception)
    determinant = check_rank_minor(pencil, cert['rank_minor'], exception)
    minors = check_lower_minor_pair(h1, cert['lower_minor_pair'])
    return {'kernel': kernel, 'h1': h1, 'determinant': determinant, 'lower_minors': minors}


def check_cube(parts, witness):
    positions = witness['positions']
    if (len(positions) != 3 or len({r for r, c in positions}) != 3
            or len({c for r, c in positions}) != 3):
        raise ArithmeticError('Invalid cubic minor positions')
    form = sp.SparseMatrix(1, parts[0].cols, {(0, j): expression(value) for j, value in witness['form']})
    scales = [expression(value) for value in witness['scales']]
    if len(scales) != 3 or any(not axis.linear.laurent(value, A, T, True) for value in scales):
        raise ArithmeticError('Cubic minor scale is not a Laurent unit')
    for i, ((row, column), scale) in enumerate(zip(positions, scales)):
        if not 0 <= row < 56 or not 0 <= column < 6:
            raise ArithmeticError('Cubic position outside the boundary block')
        if canonical(parts[column][row, :]-scale*form).todok():
            raise ArithmeticError('Incorrect cubic minor diagonal')
        if any(parts[c][row, :].todok() for r, c in positions[i+1:]):
            raise ArithmeticError('Cubic minor triangular zero is missing')
    if sp.expand(sp.prod(scales)-expression(witness['scale'])) != 0:
        raise ArithmeticError('Incorrect cubic minor product')
    return form


@lru_cache(None)
def terminal_data():
    incidence_data()
    cert = certificate()
    residual = [c['parameters'][0] for c in cert['components']]
    parts = [part[:, residual] for part in block_data()['parts']]
    parameters, checks = sp.SparseMatrix.eye(2), []
    for record in cert['residual_cubes']:
        if parameters.cols != record['before']:
            raise ArithmeticError('Incorrect cubic-round starting dimension')
        restricted = [canonical(part*parameters) for part in parts]
        cuts = sp.SparseMatrix.vstack(*(check_cube(restricted, w) for w in record['witnesses']))
        kernel = axis.linear.replay(cuts, record['kernel_steps'], A, T)
        if kernel.cols != record['after']:
            raise ArithmeticError('Incorrect cubic-round ending dimension')
        checks.extend((restricted, witness) for witness in record['witnesses'])
        parameters = canonical(parameters*kernel)
    if parameters.cols:
        raise ArithmeticError('Axis normals remain unresolved')
    return {'residual_coordinates': residual, 'cube_checks': checks}


@lru_cache(None)
def report():
    terminal = terminal_data()
    return {'claim': 'AI-MIXED-AXIS-CLOSURE-092',
            'parameters': {'a': 'any complex number', 'b': 1, 't': 'any nonzero complex number'},
            'mixed_row': 'm+t*d0', 'components': certificate()['components'],
            'joint_pencil': encode(block_data()['pencil']), 'joint_kernel': encode(incidence_data()['kernel']),
            'joint_rank': 13, 'kernel_dimension': 2, 'lower_minor_sum_at_ell_u': 't**3',
            'residual_coordinates': terminal['residual_coordinates'], 'normal_dimensions': [32, 14, 6, 4],
            'quotient_dimensions': [28, 10, 2, 0], 'plane_dimension': 4,
            'target_excluded_on_this_axis': True, 'all_graphs_classified': False,
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    value = json.dumps(report(), indent=2, default=int)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(value)
    else:
        print(value, end='')
