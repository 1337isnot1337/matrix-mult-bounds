"""Exact characteristic-three identities and an odd-characteristic two-plane."""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def require_zero(expression, label):
    if sp.cancel(expression) != 0:
        raise ArithmeticError(label)


def zero_mod_three(expression, variables, label):
    """Reduce a rational identity only when its denominator survives mod 3."""
    numerator, denominator = sp.cancel(expression).as_numer_denom()

    def reduce_polynomial(value):
        multiplier, polynomial = sp.Poly(value, *variables, domain=sp.QQ).clear_denoms()
        if int(multiplier) % 3 == 0:
            raise ValueError('coefficient denominator divisible by three')
        return sp.Poly(polynomial.as_expr(), *variables, modulus=3)

    if reduce_polynomial(denominator).is_zero:
        raise ValueError('denominator vanishes in characteristic three')
    if not reduce_polynomial(numerator).is_zero:
        raise ArithmeticError(label)


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        actual = hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def load_parent():
    path = ROOT / 'research/ai/2026-10-24-quadratic-equality/verify.py'
    spec = importlib.util.spec_from_file_location('char3_tangent_parent', path)
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    return parent


def radical_checks(parent):
    forms, _, _ = parent.symbolic_checks()
    B, Q, C = (forms[k] for k in ('B', 'Q', 'C'))
    mu, d = forms['mu'], forms['d']
    u, v, w = (forms[k] for k in ('u', 'v', 'w'))
    a, b, c, e = C
    variables = (u, v, w, a, b, c, e)
    factor = (b-c)*(v*(a-e)-u*b+w*c)
    zero_mod_three(forms['qc']-factor, variables, 'C-block factorization')
    F = sp.diag(sp.trace(B*B)/mu, 1, 1)
    F[1:3, 1:3] = B
    for entry in F-(Q*Q+d*sp.eye(3))/mu:
        zero_mod_three(entry, (u, v, w), 'extra radical direction')
    K = (3*mu**2-d)*B-2*mu*d*sp.eye(2)
    zero_mod_three(K.det()-d**3, (u, v, w), 'nondegenerate four-block')

    # Right perturbation V=NQ^2 gives H'=2Q, then Q'=-2Q^3.
    H = Q.inv()
    derivative_H = Q**2*H+H*Q**2
    derivative_Q = -Q*derivative_H*Q
    for entry in derivative_Q-Q**3:
        zero_mod_three(entry, (u, v, w), 'inverse-Gram derivative')
    derivative_mu = sp.trace(derivative_Q)/2
    zero_mod_three(derivative_mu-mu**3, (u, v, w), 'invariant mu derivative')
    p = sp.Symbol('p')
    derivative_p = p*sp.trace(Q**2)
    zero_mod_three(mu*derivative_p+p*derivative_mu-p*mu*d,
                   (u, v, w, p), 'linear-form derivative')
    t = sp.Symbol('t')
    expected = (1+(2*mu**2+d)*t+(mu**4+mu**2*d+d**2)*t**2
                +mu**2*d**2*t**3)
    zero_mod_three((sp.eye(3)+t*Q**2).det()-expected,
                   (u, v, w, t), 'literal determinant curve')
    zero_mod_three(sp.trace(2*t*Q+t*t*Q**3)-mu*t-2*mu**3*t*t,
                   (u, v, w, t), 'literal norm curve')

    controls = []
    for values in ((1, 0, 1), (1, 1, 0)):
        sub = dict(zip((u, v, w), values))
        # Multiply away symbolic denominators before using integer reduction.
        c_matrix = sp.hessian(mu*forms['qc'], tuple(C)).applyfunc(sp.cancel).subs(sub)
        off_matrix = sp.hessian(d*forms['q4'], tuple(forms['p'])+tuple(forms['q'])).applyfunc(sp.cancel).subs(sub)
        c_rank, off_rank = parent.rank_mod(c_matrix, 3), parent.rank_mod(off_matrix, 3)
        controls.append({'B_entries': list(values), 'C_rank': c_rank,
                         'four_block_rank': off_rank, 'tangent_rank': c_rank+off_rank})
    if [(row['C_rank'], row['four_block_rank']) for row in controls] != [(1, 4), (2, 4)]:
        raise ArithmeticError('scalar/nonscalar tangent controls')
    return controls


def line_invariants():
    p, mu, d, t, q = sp.symbols('p mu d t q')
    h = p*mu
    return {
        'p': p, 'mu': mu, 'd': d, 't': t, 'q': q,
        'qcurve': q+mu*t+2*mu**3*t*t,
        'hcurve': h*(1+d*t),
        'pcurve': p*(1+(2*mu**2+d)*t+(mu**4+mu**2*d+d*d)*t*t+mu**2*d*d*t**3),
    }


def cubic_line_check():
    data = line_invariants()
    p, mu, d, t, q = (data[k] for k in ('p', 'mu', 'd', 't', 'q'))
    difference = data['pcurve']-data['qcurve']*data['hcurve']+data['hcurve']**3
    actual = sp.Poly(difference, t).nth(3)
    expected = 2*p*mu**2*d*(d-mu**2)
    remainder = sp.rem(sp.Poly(actual-expected, p),
                       sp.Poly(p*p*mu*d-1, p)).as_expr()
    zero_mod_three(remainder, (p, mu, d, q), 'cubic coefficient contradiction')
    return '2*p*mu^2*d*(d-mu^2), modulo p^2*mu*d=1'


def plane_matrix(x, y):
    return sp.Matrix([[0, x+sp.I*y, x-y],
                      [-x-sp.I*y, -2*x, x-sp.I*y],
                      [x+y, -x+sp.I*y, 0]])


def literal_source(M):
    return sp.Matrix(15, 15, lambda row, col:
                     M[col//3-row//5, row % 5-col % 3]
                     if 0 <= col//3-row//5 <= 2 and 0 <= row % 5-col % 3 <= 2
                     else 0)


def two_plane_checks():
    x, y = sp.symbols('x y')
    M = plane_matrix(x, y)
    require_zero(M.det()-4*x**3, 'coefficient determinant')
    J = sp.Matrix([[0, 0, -2], [0, 1, 0], [-2, 0, 0]])
    H = M.T*J*M*J
    adj = H.adjugate()
    require_zero((2*adj-sp.trace(adj)*sp.eye(3)).det(), 'plane residual identity')
    base = M.subs({x: 1, y: 0})
    R = literal_source(base)
    minor = R.extract([i for i in range(15) if i != 1],
                      [i for i in range(15) if i != 3])
    determinant = minor.det()
    if determinant != 16:
        raise ArithmeticError('basepoint minor16 certificate')
    return {'coefficient_ring': 'Z[i,x,y]/(i^2+1)',
            'coefficient_determinant': '4*x^3', 'Delta_zero': True,
            'base_coefficient_matrix': [list(map(int, row)) for row in base.tolist()],
            'deleted_row_pair': [0, 1], 'deleted_column_pair': [1, 0],
            'base_minor_matrix': [list(map(int, row)) for row in minor.tolist()],
            'base_minor_determinant': int(determinant),
            'field_requires_sqrt_minus_one': True}


def report():
    check_pins()
    parent = load_parent()
    return {
        'status': 'Exact corroboration of written unreviewed proofs',
        'claims': ['AI-CHAR3-QUADRATIC-INVERTIBLE-001',
                   'AI-QUADRATIC-INVERTIBLE-TWO-PLANE-002'],
        'proof_sha256': hashlib.sha256((PACKAGE / 'proof.md').read_bytes()).hexdigest(),
        'two_plane_sha256': hashlib.sha256((PACKAGE / 'two-plane.md').read_bytes()).hexdigest(),
        'sources_sha256': hashlib.sha256((PACKAGE / 'sources.json').read_bytes()).hexdigest(),
        'radical_and_directional_identities_mod3': True,
        'characteristic_three_tangent_controls': radical_checks(parent),
        'cubic_line_coefficient': cubic_line_check(),
        'two_plane': two_plane_checks(),
        'odd_characteristic_upper_bound': 4,
        'algebraically_closed_odd_characteristic_lower_bound': 2,
        'characteristic_two_resolved': False, 'sharpness_supplied': False,
        'independent_review': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
