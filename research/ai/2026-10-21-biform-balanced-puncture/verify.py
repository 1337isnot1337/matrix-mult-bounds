"""Exact balanced-puncture identities and a complete affine core incidence chart."""
from functools import lru_cache
import argparse
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
X, Y, A, B, C, D, E = sp.symbols('x y a b c d e')
U_MONOMIALS = [1, X, Y, X*Y, Y**2, X*Y**2]
V_MONOMIALS = [1, X, X**2, Y, X*Y, X**2*Y]
H_MONOMIALS = [1, X, Y, X*Y]


def rational_matrix(record):
    return sp.MutableSparseMatrix(*record['shape'], {
        (i, j): sp.Rational(n, q) for i, j, n, q in record['entries']})


def encode(matrix):
    return {'shape': list(matrix.shape), 'entries': [
        [i, j, str(sp.expand(value))]
        for (i, j), value in sorted(matrix.todok().items()) if value]}


def decode(record):
    symbols = {str(z): z for z in (X, Y, A, B, C, D, E)}
    return sp.MutableSparseMatrix(*record['shape'], {
        (i, j): sp.sympify(value, locals=symbols)
        for i, j, value in record['entries']})


def coefficient_vector(polynomial, monomials):
    polynomial = sp.Poly(polynomial, X, Y)
    return sp.Matrix([polynomial.coeff_monomial(m) for m in monomials])


def flat(matrix):
    return sp.Matrix(matrix.rows*matrix.cols, 1, list(matrix))


def syzygies(g, lx, ly, h_basis=H_MONOMIALS):
    u = coefficient_vector(g*ly, U_MONOMIALS)
    v = coefficient_vector(g*lx, V_MONOMIALS)
    matrices = [coefficient_vector(ly*h, U_MONOMIALS)*v.T
                - u*coefficient_vector(lx*h, V_MONOMIALS).T
                for h in h_basis]
    return u, v, matrices


def quotient(vector):
    """Rows annihilate exactly the supplied nonzero rational column."""
    if not any(vector):
        raise ValueError('quotient kernel must be nonzero')
    return vector.T.to_DM().nullspace().to_Matrix()


def rank(matrix):
    return len(matrix.to_DM().rref()[1])


@lru_cache(None)
def core_data():
    source = ROOT/'results/biform-third-core-2026-10-21/structure.json'
    report = json.loads(source.read_text())
    raw = rational_matrix(report['core'])
    pivots = list(raw.to_DM().rref()[1])
    au = rational_matrix(report['U_basis_change'])
    bv = rational_matrix(report['V_basis_change'])
    change = sp.kronecker_product(au.T, bv.T)
    core = sp.Matrix.vstack(*(
        change*raw[36*k:36*(k+1), pivots] for k in range(4)))
    first = sorted({j for _, j in core[:36, :].todok()})
    second = sorted({j for _, j in core[36:72, :].todok()})
    paired = []
    for j in first:
        column = core[:36, j].col_join(core[72:108, j])
        matches = [k for k in second if column ==
                   core[36:72, k].col_join(core[108:144, k])]
        if len(matches) != 1:
            raise ArithmeticError('two source-pair copies no longer agree')
        paired.append(matches[0])
    if len(first) != 12 or sorted(paired) != second or rank(core) != 24:
        raise ArithmeticError('core parameter decomposition changed')
    pair = core[:36, first].col_join(core[72:108, first])
    annihilator = pair.T.to_DM().nullspace().to_Matrix()
    if annihilator.shape != (60, 72) or annihilator*pair != sp.zeros(60, 12):
        raise ArithmeticError('pair coefficient cokernel changed')
    return {'raw': raw, 'pivots': pivots, 'core': core,
            'first': first, 'second': paired, 'pair': pair,
            'annihilator': annihilator}


@lru_cache(None)
def affine_chart():
    """All points with g00=lx0=ly0=1, with no generic-point exceptions."""
    data = core_data()
    g = 1+C*X+D*Y+E*X*Y
    u, v, matrices = syzygies(g, 1+A*X, 1+B*Y, H_MONOMIALS[1:])
    generators = sp.Matrix.hstack(*(flat(m) for m in matrices))
    system = data['annihilator']*sp.diag(generators, generators)
    rows, columns = [1, 2, 25, 27, 28], [0, 1, 2, 3, 5]
    minor = system.extract(rows, columns)
    if sp.expand(minor.det()) != 1:
        raise ArithmeticError('unguarded unit minor changed')
    direction = sp.zeros(6, 1)
    direction[4] = 1
    solution = -minor.inv()*system[rows, 4]
    for j, value in zip(columns, solution):
        direction[j] = sp.expand(value)
    residual = (system*direction).applyfunc(sp.expand)
    f1, f2 = C+D, D**2+E
    gb = sp.groebner([f1, f2], C, D, E, A, B)
    for value in residual:
        if gb.reduce(value)[1] != 0:
            raise ArithmeticError('residual is outside the claimed ideal')
    # Two explicit row identities prove the reverse ideal containment.
    first_row = next(i for i, value in enumerate(residual) if value == -f1)
    second_row = next(i for i, value in enumerate(residual)
                      if sp.expand(value+f2+(A+2*C-D)*f1) == 0)
    if sp.expand(-residual[first_row]-f1) != 0:
        raise ArithmeticError('first reverse ideal identity failed')
    if sp.expand(-residual[second_row]
                 +(A+2*C-D)*residual[first_row]-f2) != 0:
        raise ArithmeticError('second reverse ideal identity failed')
    # The constant coefficient of g is one, so h mod Cg has the unique
    # representative supported on x,y,xy. There is no lost syzygy class.
    specialized = {D: -C, E: -C**2}
    image = (sp.diag(generators, generators)*direction).subs(specialized)
    pair = data['pair']
    pivot_rows = list(pair.T.to_DM().rref()[1])
    normal = pair[pivot_rows, :].inv()*image[pivot_rows, :]
    normal = normal.applyfunc(sp.expand)
    if any(sp.expand(z) for z in pair*normal-image):
        raise ArithmeticError('normal family leaves the actual core')
    full = sp.zeros(24, 2)
    for j, k, value in zip(data['first'], data['second'], normal):
        full[j, 0] = value
        full[k, 1] = value
    return {'u': u, 'v': v, 'generators': generators, 'system': system,
            'rows': rows, 'columns': columns, 'direction': direction,
            'residual': residual, 'reverse_rows': [first_row, second_row],
            'normal': full, 'specialized_image': image,
            'specialized_u': u.subs(specialized),
            'specialized_v': v.subs(specialized)}


def multiplication():
    return sp.Matrix.hstack(*(
        coefficient_vector(u*v, [X**i*Y**j for i in range(4) for j in range(4)])
        for u in U_MONOMIALS for v in V_MONOMIALS))


def controls():
    mu = multiplication()
    g = 1+X+Y+2*X*Y
    u, v, matrices = syzygies(g, 1+3*X, 2-Y)
    span = sp.Matrix.hstack(*(flat(m) for m in matrices))
    if rank(span) != 3 or mu*span != sp.zeros(16, 4):
        raise ArithmeticError('three-dimensional polynomial control failed')
    left, right = quotient(u), quotient(v)
    units = [sp.eye(2)[:, i]*sp.eye(2)[j, :] for i in range(2) for j in range(2)]
    for m in matrices:
        for unit in units:
            projected = sp.kronecker_product(left, sp.eye(2))*sp.kronecker_product(m, unit)*sp.kronecker_product(right.T, sp.eye(2))
            if projected != sp.zeros(10):
                raise ArithmeticError('product-kernel cancellation failed')
    data = core_data()
    coordinate = []
    for i in range(6):
        for j in range(6):
            rows = [36*k+6*p+q for k in range(4)
                    for p in range(6) for q in range(6) if p != i and q != j]
            system = data['core'][rows, :]
            kernel = system.to_DM().nullspace().to_Matrix().T
            coordinate.append({'u_index': i, 'v_index': j,
                               'nonplane_dimension': kernel.cols,
                               'kernel': encode(kernel)})
    if sum(c['nonplane_dimension'] != 0 for c in coordinate) != 8:
        raise ArithmeticError('coordinate discovery coverage changed')
    return {'three_dimensional_syzygy_control': {
        'g': str(g), 'lx': '1 + 3*x', 'ly': '2 - y',
        'u': encode(u), 'v': encode(v), 'matrices': [encode(m) for m in matrices],
        'dimension': 3, 'all_sixteen_auxiliary_products_cancel': True},
        'coordinate_charts': coordinate,
        'scope': 'Exact controls; only the written proof classifies arbitrary kernels.'}


def reports():
    chart = affine_chart()
    data = core_data()
    return {'affine_chart': {
        'scope': 'g00=lx0=ly0=1; all five remaining complex parameters, including special values',
        'independent_parameter_pivots': data['pivots'],
        'source_pair_columns': [data['first'], data['second']],
        'pair_coefficient_map': encode(data['pair']),
        'pair_annihilator': encode(data['annihilator']),
        'syzygy_generators': encode(chart['generators']),
        'incidence_system': encode(chart['system']),
        'unit_minor_rows': chart['rows'], 'unit_minor_columns': chart['columns'],
        'unit_minor_determinant': 1, 'kernel_direction': encode(chart['direction']),
        'residual': encode(chart['residual']),
        'residual_ideal': ['c + d', 'd**2 + e'],
        'reverse_ideal_rows': chart['reverse_rows'],
        'normal_family': encode(chart['normal']),
        'nonplane_normal_dimension_on_incidence': 2,
        'two_slice_unit_minor_columns': [6, 18],
        'two_slice_unit_minor_determinant': -1,
        'shared_factor_on_incidence': '(1 + c*x)*(1 - c*y)',
        'all_later_tensor_coefficients_verified': False,
        'improves_omega': False}, 'controls': controls()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, report in reports().items():
        (args.output_dir/(name+'.json')).write_text(json.dumps(report, indent=2)+'\n')
        print(name, 'written', flush=True)
