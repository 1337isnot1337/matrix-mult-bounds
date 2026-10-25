"""Exact algebraic corroboration of the odd-characteristic attainer proof."""
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


def zero(value, label):
    if sp.expand(value) != 0:
        raise ArithmeticError(label)


def matrix_zero(M, label):
    for value in M:
        zero(value, label)


def invariants(M):
    a, b, c, d, e, f, g, h, i = list(M)
    A2 = 2*a*i+2*c*g-b*h-d*f
    T4 = (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
          +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
          -c*d*e*h-c*d*f*g+c*e*e*g)
    return sp.expand(M.det()), sp.expand(A2), sp.expand(T4)


def binary_action(g):
    a, b, c, d = list(g)
    return sp.Matrix([[a*a, a*c, c*c], [2*a*b, a*d+b*c, 2*c*d],
                      [b*b, b*d, d*d]])


def kernel_normalizer(r):
    return sp.Matrix([[1, 0], [r, 1]])


def adjugate_form(N):
    return N[1, 1]**2-N[1, 0]*N[1, 2]-N[0, 1]*N[2, 1]+N[0, 0]*N[2, 2]


def compression_checks():
    a, b, c, d, e, f, g, h = sp.symbols('a b c d e f g h')
    cases = [
        (sp.Matrix([[a, b, c], [d, 0, 0], [g, 0, 0]]), c*c*g*g),
        (sp.Matrix([[a, b, c], [0, e, 0], [0, h, 0]]), a*c*h*h),
        (sp.Matrix([[a, 0, 0], [d, e, f], [g, 0, 0]]), a*g*f*f),
        (sp.Matrix([[0, b, 0], [d, e, f], [0, h, 0]]), b*d*f*h),
    ]
    for M, expected in cases:
        D, _, T = invariants(M)
        zero(D, 'compression determinant')
        zero(T-expected, 'compression quartic')
    return [str(T) for _, T in cases]


def singular_three_checks():
    x, y, lam, a, b, c, d, f, g, h, j = sp.symbols('x y lambda a b c d f g h j')
    u = sp.Matrix([x, y])
    v = sp.Matrix([-y, x])
    P = sp.Matrix([[a*x+b*y, c*x+d*y], [f*x+g*y, h*x+j*y]])
    cubic = (v.T*P.adjugate()*u)[0]
    zero(cubic-(-f*x**3+(a-h-g)*x*x*y+(b-j+c)*x*y*y+d*y**3), 'signed singular cubic')
    P0 = sp.Matrix([[0, c*x], [g*y, -g*x+c*y]])
    matrix_zero(P0+u*sp.Matrix([[-g, -c]])+g*x*sp.eye(2), 'section shear')
    N = sp.Matrix([[lam, 0, x], [0, lam, y], [-y, x, 0]])
    L = sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    alternating = L*N
    matrix_zero(alternating+alternating.T, 'alternating normalized space')
    t, p, q, r, s, aa, bb, cc, dd = sp.symbols('t p q r s aa bb cc dd')
    block = sp.Matrix([[1+p*t, q*t, aa*t], [r*t, 1+s*t, bb*t], [cc*t, dd*t, 0]])
    expected = -t*t*(aa*cc+bb*dd)-t**3*(sp.Matrix([[cc, dd]])*sp.Matrix([[s, -q], [-r, p]])*sp.Matrix([aa, bb]))[0]
    zero(block.det()-expected, 'rank-two block determinant')
    return str(sp.expand(cubic))


def rank_one_eta_checks():
    a, b, c, d, e, f, g, h, i, t = sp.symbols('a b c d e f g h i t')
    a0, b0, c0, d0, e0, f0, g0, h0, i0 = sp.symbols('a0 b0 c0 d0 e0 f0 g0 h0 i0')
    M = sp.Matrix([[a, b0*t, c0*t], [d, e0*t, f0*t], [g, h0*t, i0*t]])
    D, _, T = invariants(M)
    lead = sp.expand(T).coeff(t, 2)
    zero(sp.Poly(lead, a, d, g).coeff_monomial(a*a)-i0*i0, 'rank-one square a coefficient')
    zero(sp.Poly(lead, a, d, g).coeff_monomial(g*g)-c0*c0, 'rank-one square g coefficient')
    zero(lead.subs({i0: 0, c0: 0})-a*f0*f0*g, 'rank-one surviving f obstruction')
    zero(D.subs({i0: 0, c0: 0, f0: 0}), 'rank-one singular conclusion')
    M = sp.Matrix([[a0*t, b, c0*t], [d0*t, e, f0*t], [g0*t, h, i0*t]])
    D, _, T = invariants(M)
    linear = sp.expand(D).coeff(t, 2)
    zero(D-t*t*linear, 'nonsquare rank-one determinant')
    zero(sp.expand(T).coeff(t, 3), 'nonsquare quartic parity')
    zero(sp.expand(D*(t-e)/2).coeff(t, 3)-linear/2, 'nonsquare rank-one obstruction')
    p, q, r, s, u, v = sp.symbols('p q r s u v')
    M = sp.Matrix([[1+p*t, 0, q*t], [r*t, 0, 1+s*t], [u*t, 0, v*t]])
    T = invariants(M)[2]
    zero(T.coeff(t, 1)-u, 'eta first coefficient')
    zero(T.coeff(t, 2)-(v*v-r*v+(p+2*s)*u), 'eta second coefficient')
    zero(T.coeff(t, 3).subs({u: 0, r: v})-(p-s)*v*v, 'eta cubic')
    zero(T.coeff(t, 4).subs({u: 0, r: v, p: s})-q*v**3, 'eta quartic')
    obstruction = h0*(a*f-c*d)-d*f
    zero(sp.hessian(obstruction, (a, c, d, f)).det()-h0**4, 'eta polar minor')
    M = sp.Matrix([[a, b0*t, c], [d, e0*t, f0*t], [g0*t, 0, i0*t]])
    D, _, T = invariants(M)
    zero(sp.Poly(T, c).coeff_monomial(c*c)-g0*g0*t*t, 'eta free c square')
    zero(sp.Poly(T.subs(g0, 0), c, d, t).coeff_monomial(c*d*d*t)-i0, 'eta free c cubic')
    zero(D.subs({g0: 0, i0: 0}), 'eta singular conclusion')
    return True


def section_checks():
    t, b, c, e, f, h, i, k, beta, iota, e0, h0 = sp.symbols('t b c e f h i k beta iota e0 h0')
    M = sp.Matrix([[t, b, c], [0, e, f], [0, h, i]])
    D, A, T = invariants(M)
    ell = (t-e)/2
    Q = e*i-f*h+b*h-e*e/4-2*t*i+t*t/4
    C = t*i*i-b*h*i+c*h*h-(e*i-f*h)*(t-e)/2
    zero(D-t*(A-e*ell-ell*ell)-t*Q, 'full conic determinant identity')
    zero(T-D*ell-t*C, 'full conic quartic identity')
    Q0, C0 = Q.subs(t, 0), C.subs(t, 0)
    zero(8*C0-4*e*Q0-(8*c*h*h-4*b*h*(2*i+e)+e**3), 'conic section combination')
    zero(Q0.subs({e: k*h, f: b+k*i-k*k*h/4}, simultaneous=True), 'conic f relation')
    reduced = 8*c*h-8*b*i-4*k*b*h+k**3*h*h
    zero(reduced.subs({b: beta*h, c: beta*i+(beta*k/2-k**3/8)*h}, simultaneous=True), 'conic b branch')
    zero(reduced.subs({i: iota*h, c: (iota+k/2)*b-k**3*h/8}, simultaneous=True), 'conic i branch')
    linear = (e0-2)*i+h0*(b-f)+(1-e0*e0)*t/4
    quadratic = i*i-h0*b*i+h0*h0*c*t-t*(1-e0)*(e0*i-h0*f)/2
    zero(Q.subs({e: e0*t, h: h0*t}, simultaneous=True)-t*linear, 'full linear remainder')
    zero(C.subs({e: e0*t, h: h0*t}, simultaneous=True)-t*quadratic, 'full quadratic remainder')
    final = sp.factor(linear.subs({h0: 0, i: e0*(1-e0)*t/2}, simultaneous=True))
    zero(final+t*(e0-1)**2*(2*e0-1)/4, 'final diagonal equation')
    # Clear only powers of two before the explicit characteristic-three check.
    mod3 = sp.Poly(sp.expand(4*final), e0, t, modulus=3).as_expr()
    zero(sp.Poly(mod3.subs(e0, 2), t, modulus=3).as_expr(), 'characteristic-three surviving root')
    d = sp.symbols('d')
    M = sp.Matrix([[0, b, c], [d*t, e, f], [0, h, i]])
    D, A, _ = invariants(M)
    nonconic = d*(c*h-b*i)+b*h-e*e/4+d*t*f+t*t/4
    zero(D-t*(A-e*ell-ell*ell)-t*nonconic, 'nonsingular first-column identity')
    section = nonconic.subs(t, 0)
    zero(sp.hessian(section, (b, c, e, h, i)).det()+d**4/2, 'rank-five polar minor')
    if sp.diff(section, f) != 0:
        raise ArithmeticError('rank-five radical direction')
    zero(sp.diff(nonconic, f)-d*t, 'rank-five complement obstruction')
    return {'final_diagonal_equation': str(final), 'rank_five_polar_minor': '-d**4/2',
            'characteristic_three_cleared_equation': str(mod3)}


def report():
    check_pins()
    D, e, A, T, ell = sp.symbols('D e A T ell')
    P12 = D**4+(e*D+2*T)*(e*D*T+T*T-A*D*D)
    zero(P12.subs(T, D*ell)-D**3*(D+(e+2*ell)*(e*ell+ell*ell-A)), 'integral linear-form identity')
    xs = sp.symbols('a b c d e f g h i')
    M = sp.Matrix(3, 3, xs)
    D, A, T = invariants(M)
    e = M[1, 1]
    J = sp.Matrix([[0, 0, -2], [0, 1, 0], [-2, 0, 0]])
    H = M.T*J*M*J
    zero(sp.trace(H)-e*e-4*A, 'trace identity')
    zero((sp.trace(H)**2-sp.trace(H*H))/2-16*T-8*e*D, 'intrinsic m identity')
    Dt, At, Tt = invariants(M.T)
    for value in (Dt-D, At-A, Tt-T):
        zero(value, 'transpose identity')
    zero(adjugate_form(M.adjugate())-T-e*D, 'integer adjugate identity')
    u, v = sp.Matrix(sp.symbols('u0:3')), sp.Matrix(sp.symbols('v0:3'))
    zero(adjugate_form(u*v.T)-(u[1]**2-u[0]*u[2])*(v[1]**2-v[0]*v[2]), 'primitive conic factors')
    x, y, z = sp.symbols('x y z')
    alt = sp.Matrix([[0, z, -y], [-z, 0, x], [y, -x, 0]])
    matrix_zero(alt.adjugate()-sp.Matrix([x, y, z])*sp.Matrix([[x, y, z]]), 'alternating adjugate')
    al, be, ga, de = sp.symbols('alpha beta gamma delta')
    action = binary_action(sp.Matrix([[al, be], [ga, de]]))
    matrix_zero(action.T*J*action-(al*de-be*ga)**2*J, 'binary discriminant covariance')
    zero(action.det()-(al*de-be*ga)**3, 'binary determinant covariance')
    r = sp.symbols('r')
    e0 = sp.Matrix([1, 0, 0])
    matrix_zero(binary_action(kernel_normalizer(r)).inv().T*sp.Matrix([1, r, r*r])-e0, 'kernel normalizer orientation')
    matrix_zero(binary_action(sp.Matrix([[1, -r], [0, 1]]))*sp.Matrix([1, 2*r, r*r])-e0, 'ordinary column normalizer')
    cubic = singular_three_checks()
    compression = compression_checks()
    rank_one_eta_checks()
    section = section_checks()
    t, b, c, f = sp.symbols('t b c f')
    normal = sp.Matrix([[8*t, b, c], [0, 4*t, f], [0, 0, t]])
    D, A, T = invariants(normal)
    m = sp.cancel(normal[1, 1]+2*T/D)
    zero(16*D-m**3, 'intrinsic cubic consequence')
    zero(4*(normal[1, 1]**2+4*A)-5*m*m, 'intrinsic trace consequence')
    return {'claim': 'AI-ODD-QUADRATIC-ATTAINERS-001',
            'scope': 'dimension-four geometric families with nonzero coefficient determinant over every field of characteristic different from two',
            'normal_form': '[[8t,b,c],[0,4t,f],[0,0,t]]',
            'equivalence': 'binary coefficient actions over K and optional transposition',
            'signed_singular_three_cubic': cubic, 'compression_quartics': compression,
            'integral_and_covariance_identities_checked': True,
            'adjugate_and_rank_one_exclusions_checked': True,
            'eta_coefficients_and_polar_minor_checked': True,
            'normalization_orientation_checked': True, **section,
            'intrinsic_consequences': ['16D=m^3', '4(e^2+4A2)=5m^2'],
            'intrinsic_consequence_verification': 'normal-form identities and binary-action identities; transport follows written algebra',
            'computer_certifies_geometric_classification': False,
            'independent_review': False, 'lean_formalized': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
