"""Exact characteristic-two algebra for the two evaluation-kernel charts."""
import hashlib
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def residue(expression):
    numerator, denominator = sp.fraction(sp.cancel(expression))
    def reduce(poly):
        symbols = sorted(poly.free_symbols, key=str)
        return sp.Poly(poly, *symbols, modulus=2).as_expr() if symbols else int(poly) % 2
    if reduce(denominator) == 0:
        raise ArithmeticError('denominator vanishes in characteristic two')
    return reduce(numerator)


def zero(expression, label):
    if residue(expression) != 0:
        raise ArithmeticError(label)


def matrix_zero(matrix, label):
    for entry in matrix:
        zero(entry, label)


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def binary_action(g):
    a, b, c, d = list(g)
    return sp.Matrix([[a*a, a*c, c*c], [0, a*d+b*c, 0], [b*b, b*d, d*d]])


def invariants(M):
    a, b, c, d, e, f, g, h, i = list(M)
    D = M.det()
    A = 2*a*i+2*c*g-b*h-d*f
    T = (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
         +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
         -c*d*e*h-c*d*f*g+c*e*e*g)
    return D, A, T


def chart_equations(t, b, c, f, h, i, ell, square):
    if square:
        return t*i+f*h+b*h+t*ell+ell*ell, t*i*i+b*h*i+c*h*h+(t*i+f*h)*ell
    return b*i+c*h+b*h+t*(f+ell)+ell*ell, b*f*h+c*t*(i+h)+(b*i+c*h)*ell


def square_divided_C(t, b, c, f, i, rho, mu):
    return i*i+rho*b*i+rho*rho*c*t+mu*t*(i+rho*f)


def square_checks():
    t, b, c, f, h, i, ell = sp.symbols('t b c f h i ell')
    alpha, kap, mu, lam, rho, I = sp.symbols('alpha kappa mu lambda rho I')
    Q, C = chart_equations(t, b, c, f, h, i, ell, True)
    beta = mu+mu*mu
    zero(square_divided_C(t, b, c, f, beta*t, 0, mu)-beta*mu*mu*t*t, 'square zero rho')
    for epsilon in (0, 1):
        ii = epsilon*rho*b+I*t
        ff = (epsilon+1)*b+(I+beta)*t/rho
        zero(Q.subs({h: rho*t, ell: mu*t, i: ii, f: ff}), 'square h-zero Q')
        expected = t*(rho*(I+mu)*b+rho*rho*c+(I*I+mu*I+mu*(I+beta))*t)
        zero(square_divided_C(t, b, c, ff, ii, rho, mu)-expected, 'square h-zero mixed term')
        zero(C.subs({h: rho*t, ell: mu*t, i: ii, f: ff})-t*expected, 'square h-zero source C')
    sub = {ell: lam*h+mu*t, f: b+lam*lam*h+kap*t, i: (kap+lam)*h+beta*t}
    expected = (h*h*(c+kap*b+lam**3*h+((kap+lam)**2+lam*lam*(mu+1))*t)
                +mu*mu*b*h*t+lam*mu*mu*h*t*t+beta*mu*mu*t**3)
    zero(Q.subs(sub), 'square main Q')
    zero(C.subs(sub)-expected, 'square main C')
    B, C0, z = sp.symbols('B C0 z')
    z_coefficient = sp.expand(expected.subs({b: B*z, c: C0*z})).coeff(z)
    zero(z_coefficient-h*((C0+kap*B)*h+mu*mu*B*t), 'square independent-coordinate coefficient')
    normal = {ell: lam*h, f: b+lam*lam*h+(alpha+lam)*t, i: alpha*h,
              c: (alpha+lam)*b+lam**3*h+(alpha*alpha+lam*lam)*t}
    zero(Q.subs(normal), 'square normal Q'); zero(C.subs(normal), 'square normal C')
    return {'h_zero_branches_checked': [0, 1], 'mixed_term_retained': 'rho*b*i',
            'square_main_residual': str(expected)}


def nonsingular_checks():
    t, b, c, f, h, i, ell = sp.symbols('t b c f h i ell')
    Q, C = chart_equations(t, b, c, f, h, i, ell, False)
    zero((C+ell*Q).subs(t, 0)-(b*h*(f+ell)+ell**3), 'nonsingular section combination')
    x, y, B, H, F, I, beta, eta = sp.symbols('x y B H F I beta eta')
    sub = {ell: x, b: beta*x+B*t, h: eta*x+H*t,
           f: (1+1/(beta*eta))*x+F*t, c: y,
           i: eta*y/beta+(eta+1/beta)*x+I*t}
    zero(sp.expand(Q.subs(sub)).coeff(t, 1).coeff(y, 1)-H-B*eta/beta, 'nonsingular Q ty')
    substituted = sp.expand(C.subs(sub).subs(H, B*eta/beta))
    zero(substituted.coeff(t, 1).coeff(y, 2)-eta/beta, 'nonsingular C ty2')
    L, C0 = sp.symbols('L C0')
    ff = B*i+(B+C0)*h+L*(1+L)*t
    zero(Q.subs({b: B*t, c: C0*t, ell: L*t, f: ff}), 'nonsingular b-zero Q')
    expected = B*ff*h+t*((C0+L*B)*i+C0*(1+L)*h)
    zero(C.subs({b: B*t, c: C0*t, ell: L*t, f: ff})-t*expected, 'nonsingular b-zero C')
    ff = B*i+H*c+(B*H+L+L*L)*t
    zero(Q.subs({b: B*t, h: H*t, ell: L*t, f: ff}), 'nonsingular both-zero Q')
    expected = c*i+t*(B*H*ff+H*c+L*B*i+L*H*c)
    zero(C.subs({b: B*t, h: H*t, ell: L*t, f: ff})-t*expected, 'nonsingular both-zero C')
    swap = {b: h, h: b, c: i, i: c, ell: ell+t}
    zero(Q.subs(swap, simultaneous=True)-Q, 'row reversal Q')
    zero(C.subs(swap, simultaneous=True)-C, 'row reversal C')
    j = sp.symbols('j')
    a, S = F+L, F+L+L*L
    sub = {i: j+h, f: F*t, ell: L*t}
    q = b*j+c*h+S*t*t
    zero(Q.subs(sub)-q, 'nonsingular reduced Q')
    zero(C.subs(sub)-t*(c*j+a*b*h+L*S*t*t)-L*t*q, 'nonsingular reduced C modulo Q')
    zero(c*(b*j+c*h)+b*(c*j+a*b*h)-h*(c*c+a*b*b), 'nonsingular elimination')
    normal = {ell: L*t, f: L*(1+L)*t, c: L*b, i: (L+1)*h}
    zero(Q.subs(normal), 'nonsingular normal Q'); zero(C.subs(normal), 'nonsingular normal C')
    return {'nonzero_ell_obstruction': 'eta/beta coefficient of t*y^2',
            'both_zero_obstruction': 'c*i on the two-dimensional section',
            'row_reversal_is_permitted': True}


def action_checks():
    t, x, y, b, h, alpha, lam, L, r = sp.symbols('t x y b h alpha lambda L r')
    N = sp.Matrix([[t, x, 0], [0, t, x], [0, y, 0]])
    square = sp.Matrix([[t, b, (alpha+lam)*b+lam**3*h+(alpha*alpha+lam*lam)*t],
                        [0, t, b+lam*lam*h+(alpha+lam)*t], [0, h, alpha*h]])
    image = binary_action(sp.Matrix([[1, 0], [lam, 1]]))*N*binary_action(sp.Matrix([[1, alpha], [0, 1]])).T
    matrix_zero(image-square.subs({b: x+lam*t+lam*lam*y, h: y}), 'square shear')
    normal = sp.Matrix([[0, b, L*b], [t, t, L*(1+L)*t], [0, h, (L+1)*h]])
    M0 = normal.subs(L, 0)
    matrix_zero(normal*binary_action(sp.Matrix([[1, L], [0, 1]])).T-M0, 'nonsingular shear')
    P = sp.Matrix([[b, b, 0], [0, t, 0], [0, h, h]])
    matrix_zero(P*binary_action(sp.Matrix([[1, 0], [1, 1]])).T-M0, 'previous-plane normalization')
    matrix_zero(binary_action(sp.Matrix([[0, 1], [1, 0]]))-sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), 'permitted row reversal')
    matrix_zero(binary_action(sp.Matrix([[1, 0], [r, 1]])).inv().T*sp.Matrix([1, r, r*r])-sp.Matrix([1, 0, 0]), 'evaluation kernel normalization')
    D, _, _ = invariants(square)
    zero(D-t*h*(b+lam*t+lam*lam*h), 'square normal determinant')
    D, _, _ = invariants(normal)
    zero(D-t*b*h, 'nonsingular normal determinant')


def report():
    check_pins()
    t, b, c, f, h, i, ell = sp.symbols('t b c f h i ell')
    for square in (True, False):
        M = sp.Matrix([[t, b, c], [0, t, f], [0, h, i]]) if square else sp.Matrix([[0, b, c], [t, t, f], [0, h, i]])
        D, A, T = invariants(M)
        Q, C = chart_equations(t, b, c, f, h, i, ell, square)
        zero(D-t*(A+t*ell+ell*ell)-t*Q, 'integral chart Q')
        zero(T-D*ell-t*C, 'integral chart C')
    square_result, nonsingular_result = square_checks(), nonsingular_checks()
    action_checks()
    return {'claim': 'AI-CHAR2-EVALUATION-KERNEL-ATTAINERS-001',
            'characteristic': 2, 'geometric_orbits_in_evaluation_kernel_locus': 2,
            'normalized_chart_classification_over_ground_field': True,
            'arbitrary_ground_field_descent_proved': False,
            'complete_char2_attainer_classification': False,
            'square_chart_representative': '[[t,x,0],[0,t,x],[0,y,0]]',
            'nonsingular_chart_representative': '[[x,x,0],[0,y,0],[0,z,z]]',
            **square_result, **nonsingular_result,
            'computer_certifies_geometric_exhaustion': False,
            'independent_review': False, 'lean_formalized': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
