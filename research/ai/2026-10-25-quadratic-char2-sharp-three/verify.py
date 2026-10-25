"""Exact algebra supporting the sharp characteristic-two three-space bound."""
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
SPEC = importlib.util.spec_from_file_location(
    'sharp_three_cap_four_dependency',
    ROOT / 'research/ai/2026-10-25-quadratic-char2-cap-four/verify.py')
cap_four = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cap_four)
invariants = cap_four.invariants


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def mod2(expression):
    expression = sp.expand(expression)
    variables = sorted(expression.free_symbols, key=str)
    if not variables:
        return sp.Integer(expression) % 2
    return sp.Poly(expression, *variables, modulus=2).as_expr()


def require_zero(expression, label):
    if mod2(expression) != 0:
        raise ArithmeticError(label)


def adjugate_form(N):
    return N[1, 1]**2+N[1, 0]*N[1, 2]+N[0, 1]*N[2, 1]+N[0, 0]*N[2, 2]


def conic(vector):
    return vector[1]**2+vector[0]*vector[2]


def middle_rank_one_residuals(b0, c0, f0, h0, i0):
    return [i0+f0*h0, b0*i0+c0*h0+f0, b0*f0+c0]


def report():
    check_pins()
    a, b, c, d, e, f, g, h, i = sp.symbols('a b c d e f g h i')
    M = sp.Matrix([[a, b, c], [d, e, f], [g, h, i]])
    D, A, T = invariants(M)
    require_zero(adjugate_form(M.adjugate())-T-e*D, 'full adjugate identity')
    u = sp.Matrix(sp.symbols('u0:3'))
    v = sp.Matrix(sp.symbols('v0:3'))
    require_zero(adjugate_form(u*v.T)-conic(u)*conic(v), 'rank-one adjugate factor')
    x, y, z = sp.symbols('x y z')
    Alt = sp.Matrix([[0, z, y], [z, 0, x], [y, x, 0]])
    for entry in Alt.adjugate()-sp.Matrix([x, y, z])*sp.Matrix([[x, y, z]]):
        require_zero(entry, 'alternating adjugate')

    aa, bb, cc, dd, ff, gg, hh, jj = sp.symbols('aa bb cc dd ff gg hh jj')
    P = sp.Matrix([[aa*x+bb*y, cc*x+dd*y], [ff*x+gg*y, hh*x+jj*y]])
    cubic = (sp.Matrix([[y, x]])*P.adjugate()*sp.Matrix([x, y]))[0]
    expected_cubic = ff*x**3+dd*y**3+(hh+gg+aa)*x*x*y+(jj+cc+bb)*x*y*y
    require_zero(cubic-expected_cubic, 'primitive section cubic')
    P1 = sp.Matrix([[0, cc*x], [gg*y, gg*x+cc*y]])
    for entry in P1+sp.Matrix([x, y])*sp.Matrix([[gg, cc]])-gg*x*sp.eye(2):
        require_zero(entry, 'primitive section shear')

    # Both middle-kernel branches are required for a three-dimensional section.
    p, q0, r, s0, uu, vv, t = sp.symbols('p q0 r s0 uu vv t')
    eta = sp.Matrix([[1+p*t, 0, q0*t], [r*t, 0, 1+s0*t], [uu*t, 0, vv*t]])
    eta_T = invariants(eta)[2]
    for j, expected in enumerate(cap_four.eta_coefficients(p, q0, r, s0, uu, vv), 1):
        require_zero(sp.expand(eta_T).coeff(t, j)-expected, 'middle rank-two Taylor coefficient')
    h0, b0, c0, f0, g0, i0 = sp.symbols('h0 b0 c0 f0 g0 i0')
    polar = sp.hessian(h0*(a*f+c*d)+d*f, (a, c, d, f)).det()
    require_zero(polar-h0**4, 'middle rank-two polar determinant')
    N = sp.Matrix([[a, b0*t, c], [d, t, f0*t], [g0*t, 0, i0*t]])
    ND, NA, _ = invariants(N)
    q_two = t*(a*i0+b0*d*i0+c*g0)+b0*f0*g0*t*t
    require_zero(ND-t*q_two, 'middle rank-two determinant')
    require_zero(NA-d*f0*t, 'middle rank-two A2')
    require_zero(ND.subs({i0: 0, g0: 0}), 'middle rank-two contradiction')

    N = sp.Matrix([[a, b0*t, c0*t], [d, t, f0*t], [g, h0*t, i0*t]])
    ND, NA, _ = invariants(N)
    L = a*(i0+f0*h0)+d*(b0*i0+c0*h0)+g*(b0*f0+c0)
    require_zero(ND-t*t*L, 'middle rank-one determinant')
    require_zero(NA-d*f0*t-b0*h0*t*t, 'middle rank-one A2')
    residuals = middle_rank_one_residuals(b0, c0, f0, h0, i0)
    obstruction = sp.Poly(L-d*f0, a, d, g)
    for monomial, residual in zip((a, d, g), residuals):
        require_zero(obstruction.coeff_monomial(monomial)-residual,
                     'middle rank-one coefficient comparison')
    require_zero(residuals[1].subs({i0: f0*h0, c0: b0*f0})-f0,
                 'middle rank-one scalar contradiction')
    require_zero(ND.subs({f0: 0, c0: 0, i0: 0}), 'middle rank-one zero determinant')

    # Evaluation-kernel orbit, complement middle entry nonzero.
    d0 = sp.Symbol('d0')
    N = sp.Matrix([[0, b, c], [d0*t, t, f], [0, h, i]])
    ND, NA, _ = invariants(N)
    require_zero(ND-d0*t*(b*i+c*h), 'evaluation nonsquare determinant')
    require_zero(NA-b*h-d0*t*f, 'evaluation nonsquare A2')
    evaluation_polar = sp.hessian(d0*(b*i+c*h)+b*h, (b, c, h, i)).det()
    require_zero(evaluation_polar-d0**4, 'evaluation polar minor')
    # Square first column: the free-c coefficient is essential.
    N = sp.Matrix([[t, b, c], [0, t, f], [0, h, i]])
    ND, NA, NT = invariants(N)
    require_zero(ND-t*(t*i+f*h), 'evaluation square determinant')
    require_zero(NA-b*h, 'evaluation square A2')
    require_zero(NT-t*t*i*i-t*b*h*i-t*c*h*h, 'evaluation square quartic')
    require_zero(sp.expand(NT).coeff(c)-t*h*h, 'evaluation free-c forcing')
    lam, delta = sp.symbols('lambda delta')
    require_zero((delta+lam+lam*lam).subs(delta, lam)-lam*lam,
                 'evaluation final scalar contradiction')

    # Mixed kernel orbit, with the complement reduction h0=g0.
    N = sp.Matrix([[a, a+b0*t, c], [d0*t, t, f], [g0*t, h0*t, i0*t]])
    ND, NA, _ = invariants(N)
    require_zero(sp.expand(ND).coeff(t, 1)-a*f*(h0+g0), 'mixed section quotient')
    require_zero(NA.subs(t, 0), 'mixed section A2')
    mixed_q = t*(a*i0*(1+d0)+b0*f*g0+c*g0*(1+d0))+b0*d0*i0*t*t
    require_zero(ND.subs(h0, g0)-t*mixed_q, 'mixed full determinant')
    require_zero(NA.subs(h0, g0)-t*(a*g0+d0*f)-b0*g0*t*t, 'mixed full A2')
    require_zero(ND.subs({h0: 0, g0: 0, d0: 0, i0: 0}), 'mixed zero-g contradiction')
    require_zero((i0*(1+d0)+g0).subs(d0, 1)-g0, 'mixed nonzero-g contradiction')
    if sp.hessian(a*i+c*g, (a, i, c, g)).det() != 1:
        raise ArithmeticError('mixed f-zero nondegenerate quadric')

    # The remaining compression sections reduce to kernel containers.
    require_zero(T.subs({e: 0, f: 0, h: 0, i: 0})-c*c*g*g,
                 'compression inside middle section')
    require_zero(T.subs({a: 0, c: 0, e: 0, g: 0, i: 0})-b*d*f*h,
                 'transverse compression section')
    return {
        'claim': 'AI-CHAR2-QUADRATIC-SHARP-THREE-001',
        'scope': 'exact algebraic corroboration; the geometric proof is separate',
        'characteristic': 2,
        'adjugate_identity': 'S(adj M)=T4+eD',
        'rank_one_adjugate_factor': 'S(u v^t)=Q(u)Q(v)',
        'primitive_section_cubic': str(mod2(expected_cubic)),
        'primitive_shear_checked': True,
        'middle_rank_two_polar_determinant': str(polar),
        'middle_rank_two_q': str(sp.expand(q_two)),
        'middle_rank_one_residuals': [str(mod2(value)) for value in residuals],
        'middle_rank_one_case_checked': True,
        'evaluation_kernel_polar_minor': str(evaluation_polar),
        'evaluation_kernel_free_c_coefficient': str(t*h*h),
        'mixed_kernel_full_q': str(sp.expand(mixed_q)),
        'compression_sections_checked': True,
        'upper_bound_characteristic_two': 3,
        'lower_bound_from_pinned_construction': 3,
        'sharpness_from_pinned_construction': True,
        'classifies_attaining_three_spaces': False,
        'computer_certifies_geometric_proof': False,
        'independent_review': False, 'lean_formalized': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
