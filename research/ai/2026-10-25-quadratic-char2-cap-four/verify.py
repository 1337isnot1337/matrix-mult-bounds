"""Exact algebraic corroboration of the characteristic-two cap-four proof."""
import hashlib
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def mod2(expression, variables):
    return sp.Poly(sp.expand(expression), *variables, modulus=2).as_expr()


def require_zero(expression, variables, label):
    if mod2(expression, variables) != 0:
        raise ArithmeticError(label)


def invariants(M):
    """Keep the integer representatives until each explicit reduction."""
    a, b, c, d, e, f, g, h, i = list(M)
    A2 = 2*a*i+2*c*g-b*h-d*f
    T4 = (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
          +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
          -c*d*e*h-c*d*f*g+c*e*e*g)
    return sp.expand(M.det()), sp.expand(A2), sp.expand(T4)


def eta_coefficients(p, q, r, s, u, v):
    return [u, v*v+r*v+p*u, (p+s)*r*v+(s*s+q*r)*u,
            (p*v+q*u)**2+(p*s+q*r)*(r*v+s*u)]


def report():
    check_pins()
    D, e, A, T, qD, ell = sp.symbols('D e A T qD ell')
    vs = (D, e, A, T, qD, ell)
    P = D**4+(e*D+2*T)*(e*D*T+T*T-A*D*D)
    G = D**3+e*e*D*T+e*T*T+e*A*D*D
    require_zero(D*P-D*D*G, vs, 'integer factor reduced before division')
    require_zero(G.subs(e, 0)-D**3, vs, 'middle section forces e divides D')
    # Algebra behind integrality; integral closedness remains a written argument.
    require_zero(G.subs({T: e*qD*ell, D: e*qD}, simultaneous=True)
                 -e**3*qD**2*(qD+e*ell+ell*ell+A), vs, 'monic linear-form equation')
    candidate = e*(A+e*ell+ell*ell)
    require_zero(G.subs({D: candidate, T: candidate*ell}, simultaneous=True), vs,
                 'linear-form converse')

    a, b, c, d, e, f, g, h, i = sp.symbols('a b c d e f g h i')
    xs = (a, b, c, d, e, f, g, h, i)
    M = sp.Matrix(3, 3, xs)
    D, A2, T4 = invariants(M)
    _, At, Tt = invariants(M.T)
    require_zero(At-A2, xs, 'A2 transpose')
    require_zero(Tt-T4, xs, 'T4 transpose')
    cases = {
        'e0_plus_eta': (T4.subs({d: 0, e: 0, b: a, h: g}), (a*i+c*g)**2+a*g*f*f),
        'compression_in_middle_section': (T4.subs({e: 0, f: 0, h: 0, i: 0}), c*c*g*g),
        'transverse_compression': (T4.subs({a: 0, c: 0, e: 0, g: 0, i: 0}), b*d*f*h),
        'eta_minors': (T4.subs({b: 0, e: 0, h: 0}),
                       (a*i+c*g)**2+(a*f+c*d)*(d*i+f*g)),
    }
    for label, (actual, expected) in cases.items():
        require_zero(actual-expected, xs, label)

    aa, dd, gg, t = sp.symbols('A D0 G t')
    N = sp.Matrix([[aa*t, b, c], [dd*t, t, f], [gg*t, h, i]])
    nd, na, _ = invariants(N)
    Q = aa*f*h+dd*(c*h+b*i)+gg*b*f+b*h
    require_zero(sp.expand(nd).coeff(t, 1)+na.subs(t, 0)-Q,
                 xs+(aa, dd, gg, t), 'e0 section quadratic')
    polar_minor = sp.hessian(Q, (b, c, h, i)).det()
    require_zero(polar_minor-dd**4, (aa, dd, gg), 'e0 polar minor')
    require_zero((nd/t).subs(dd, 0)-f*(aa*h+gg*b)-t*(aa*i+gg*c),
                 xs+(aa, gg, t), 'e0 full determinant quotient')

    p, q, r, s, u, v = sp.symbols('p q r s u v')
    eta = sp.Matrix([[1+p*t, 0, q*t], [r*t, 0, 1+s*t], [u*t, 0, v*t]])
    et = invariants(eta)[2]
    coefficients = eta_coefficients(p, q, r, s, u, v)
    for j, expected in enumerate(coefficients, 1):
        require_zero(sp.expand(et).coeff(t, j)-expected, (p, q, r, s, u, v),
                     'eta Taylor coefficient ' + str(j))
    require_zero(coefficients[3].subs({u: 0, r: v, s: p})-q*v**3,
                 (p, q, v), 'eta surviving quartic')
    b0, g0, h0, i0 = sp.symbols('b0 g0 h0 i0')
    complement = sp.Matrix([[a, b0*t, c], [d, t, f], [g0*t, h0*t, i0*t]])
    cd, ca, _ = invariants(complement)
    obstruction = mod2(sp.expand(cd).coeff(t, 1)+ca.subs(t, 0), (a, c, d, f, h0))
    require_zero(obstruction-h0*(a*f+c*d)-d*f, (a, c, d, f, h0), 'eta complement')
    if sp.Poly(obstruction, a, c, d, f).coeff_monomial(d*f) != 1:
        raise ArithmeticError('eta nonsquare polar coefficient')

    # The singular-space classification uses this exact block determinant.
    block = sp.Matrix([[1+p*t, q*t, a*t], [r*t, 1+s*t, b*t], [c*t, d*t, 0]])
    adj = sp.Matrix([[s, -q], [-r, p]])
    expected = -t*t*(a*c+b*d)-t**3*(sp.Matrix([[c, d]])*adj*sp.Matrix([a, b]))[0]
    if sp.expand(block.det()-expected) != 0:
        raise ArithmeticError('integer rank-two block determinant')
    return {
        'claim': 'AI-CHAR2-QUADRATIC-INVERTIBLE-CAP-001',
        'scope': 'exact polynomial corroboration; geometric proof is written separately',
        'characteristic': 2,
        'integral_linear_form_identities_checked': True,
        'orbit_and_compression_T4': {label: str(mod2(expected, xs))
                                     for label, (_, expected) in cases.items()},
        'e0_polar_minor': str(polar_minor),
        'eta_taylor_coefficients': [str(mod2(x, (p, q, r, s, u, v))) for x in coefficients],
        'eta_complement_obstruction': str(obstruction),
        'integer_rank_two_block_identity_checked': True,
        'lower_bound_all_fields_from_pinned_construction': 3,
        'upper_bound_all_fields_with_pinned_odd_proof': 4,
        'computer_certifies_geometric_classification': False,
        'sharpness_supplied': False, 'independent_review': False,
        'lean_formalized': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
