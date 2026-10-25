"""Integer kernel and minor certificates for a universal quadratic three-plane."""
import hashlib
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def require_zero(expression, label):
    if sp.expand(expression) != 0:
        raise ArithmeticError(label)


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        actual = hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def family(x, y, z):
    return sp.Matrix([[x, x, 0], [0, y, 0], [0, z, z]])


def literal_source(M):
    return sp.Matrix([
        [M[H-j, L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
         for H in range(5) for r in range(3)]
        for j in range(3) for L in range(5)])


def kernel_vector(x, y, z):
    v = sp.zeros(15, 1)
    v[2] = -y*z*z
    v[4] = v[5] = x*z*z
    v[9] = v[10] = -x*x*z
    v[12] = x*x*y
    return v


def invariant_coordinates(M):
    a, b, c, d, e, f, g, h, i = list(M)
    D = M.det()
    A2 = 2*a*i+2*c*g-b*h-d*f
    T4 = (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
          +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
          -c*d*e*h-c*d*f*g+c*e*e*g)
    return sp.expand(D), sp.expand(A2), sp.expand(T4)


def integer_invariants(M):
    D, A2, T4 = invariant_coordinates(M)
    e = M[1, 1]
    P12 = D**4+(e*D+2*T4)*(e*D*T4+T4*T4-A2*D*D)
    return D, A2, T4, sp.expand(P12)



def extension_checks():
    x, y, z, t = sp.symbols('x y z t')
    a, b, c, d, e0, f, g, h, i = sp.symbols('a b c d e0 f g h i')
    B = sp.Matrix([[a, b, c], [d, e0, f], [g, h, i]])
    D, A, T = invariant_coordinates(family(x, y, z)+t*B)
    dotD, dotA, dotT = [sp.diff(q, t).subs(t, 0) for q in (D, A, T)]
    expected_dotD = y*z*a-x*z*d+x*z*e0-x*z*f+x*y*i
    require_zero(dotD-expected_dotD, 'complete determinant differential')
    C = sp.expand(x*y*z*(dotD-x*z*e0-y*dotA)+(y*y-2*x*z)*dotT)
    expected_C = (c*x*y*y*z*z-(d+f)*x*x*y*z*z+g*x*x*y*y*z
                  -2*(a-b+c)*x*x*z**3-2*(i-h+g)*x**3*z*z)
    require_zero(C-expected_C, 'first-order extension condition')
    # Check the abstract derivative simplification without dropping any entry.
    dd, ee, aa, tt = sp.symbols('D e A T')
    dp, ep, ap, tp = sp.symbols('dotD dote dotA dotT')
    F = dd*(dd**4+(ee*dd+2*tt)*(ee*dd*tt+tt*tt-aa*dd*dd))
    derivative = sum(sp.diff(F, v)*dv for v, dv in zip((dd, ee, aa, tt), (dp, ep, ap, tp)))
    derivative = derivative.subs({tt: 0, dd: ee*aa})
    chain = (ee*aa)**3*((ee*aa)*(dp-aa*ep-ee*ap)+(ee*ee-2*aa)*tp)
    require_zero(derivative-chain, 'integral determinant chain rule')
    u, v, w = sp.symbols('u v w')
    candidate = sp.Matrix([[x, x+u*t, 0], [w*t, y, -w*t], [0, z, z+v*t]])
    D, A, T, P = integer_invariants(candidate)
    odd = sp.factor((D*P).subs({u: 0, v: 0}))
    require_zero(odd+t*t*w*w*x**4*y**5*z**4, 'odd extension obstruction')
    G9 = D**3+y*y*D*T+y*T*T+y*A*D*D
    second = sp.Poly(sp.expand(G9), t).coeff_monomial(t*t)
    second = sp.Poly(second, x, y, z, u, v, w, modulus=2).as_expr()
    expected_second = x*x*y*z*z*(u*u*z*z+u*w*y*z+v*v*x*x+v*w*x*y+w*w*y*y)
    if not sp.Poly(second-expected_second, x, y, z, u, v, w, modulus=2).is_zero:
        raise ArithmeticError('characteristic-two extension obstruction')
    coeff = sp.Poly(second, x, y, z)
    forcing = [coeff.coeff_monomial(m) for m in (x*x*y*z**4, x**4*y*z*z, x*x*y**3*z*z)]
    if forcing != [u*u, v*v, w*w]:
        raise ArithmeticError('three forcing square coefficients')
    return {'scope': 'no strictly larger geometric rank-at-most14 linear space contains this three-plane',
            'first_order_C': str(C), 'dotD': str(dotD),
            'odd_candidate_source_determinant': str(odd),
            'characteristic_two_G9_t2': str(second),
            'characteristic_two_forcing_coefficients': [str(q) for q in forcing],
            'global_dimension_four_excluded': False}


def report():
    check_pins()
    x, y, z = sp.symbols('x y z')
    M = family(x, y, z)
    # These three coefficient entries are an identity coordinate projection.
    if [M[0, 0], M[1, 1], M[2, 2]] != [x, y, z]:
        raise ArithmeticError('three independent directions')
    D, A2, T4, P12 = integer_invariants(M)
    for value, label in ((D-x*y*z, 'coefficient determinant'),
                         (A2-x*z, 'integer A2'), (T4, 'integer T4'),
                         (P12, 'integer residual determinant')):
        require_zero(value, label)
    R = literal_source(M)
    v = kernel_vector(x, y, z)
    if v[12] != x*x*y:
        raise ArithmeticError('nonzero kernel coefficient')
    for value in R*v:
        require_zero(value, 'polynomial source kernel')
    minor = R.minor_submatrix(14, 12)
    determinant = sp.factor(minor.det(method='domain-ge'))
    require_zero(determinant+x**6*y**3*z**5, 'generic minor')
    base = {x: 1, y: 1, z: 1}
    certificate = minor.subs(base)
    if certificate.det(method='bareiss') != -1:
        raise ArithmeticError('unit basepoint minor')
    # Direct symbolic source computation corroborates the kernel proof.
    require_zero(R.det(method='domain-ge'), 'literal source determinant')
    return {
        'claim': 'AI-QUADRATIC-UNIVERSAL-THREE-PLANE-001',
        'scope': 'geometric family over every field, including characteristics two and zero',
        'dimension': 3, 'coefficient_matrix': [[str(v) for v in row] for row in M.tolist()],
        'coefficient_determinant': str(D), 'integer_A2': str(A2),
        'integer_T4': str(T4), 'integer_P12': str(P12),
        'literal_source_determinant': 0,
        'polynomial_right_kernel': [str(value) for value in v],
        'generic_minor': str(determinant),
        'deleted_row_pair': [2, 4], 'deleted_column_pair': [4, 0],
        'basepoint': [1, 1, 1], 'base_minor_matrix': [[int(v) for v in row] for row in certificate.tolist()],
        'base_minor_determinant': -1,
        'source_rank_at_every_invertible_coefficient_point': 14,
        'lower_bound_all_fields': 3, 'upper_bound_characteristic_not_two': 4,
        'upper_bound_characteristic_two': 5,
        'nonextension': extension_checks(),
        'sharpness_supplied': False, 'independent_review': False,
        'lean_formalized': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
