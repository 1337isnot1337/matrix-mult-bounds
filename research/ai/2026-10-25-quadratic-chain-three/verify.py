"""Integer source certificates and section invariants for a second three-plane."""
import hashlib
import json
from pathlib import Path

import sympy as sp

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]


def zero(value, label):
    if sp.expand(value) != 0:
        raise ArithmeticError(label)


def check_pins():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for item in sources['local_dependencies']:
        if hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ArithmeticError('source pin: ' + item['path'])
    return sources


def family(t, x, y):
    return sp.Matrix([[t, x, 0], [0, t, x], [0, y, 0]])


def literal_source(M):
    return sp.Matrix([
        [M[H-j, L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
         for H in range(5) for r in range(3)]
        for j in range(3) for L in range(5)])


def kernel(t, x, y):
    return sp.Matrix([0, 0, -y*y, 0, y*y, 0, 0, 0, 0, -t*y, -x*y, 0, t*t, 2*t*x, x*x])


def invariants(M):
    a, b, c, d, e, f, g, h, i = list(M)
    D = sp.expand(M.det())
    A = 2*a*i+2*c*g-b*h-d*f
    T = (a*a*i*i-a*b*h*i-2*a*c*g*i+a*c*h*h-a*d*f*i+a*f*f*g
         +b*b*g*i-b*c*g*h+b*d*f*h-b*e*f*g+c*c*g*g+c*d*d*i
         -c*d*e*h-c*d*f*g+c*e*e*g)
    return D, sp.expand(A), sp.expand(T)


def section_checks():
    B = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
    H = sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 1, 0]])
    P = sp.Matrix([[1, 1, 0], [0, 0, 0], [0, 0, 0]])
    Q = sp.Matrix([[0, 0, 0], [0, 0, 0], [0, 1, 1]])
    nr, nl = sp.Matrix.vstack(B, H), sp.Matrix.vstack(B.T, H.T)
    pr, pl = sp.Matrix.vstack(P, Q), sp.Matrix.vstack(P.T, Q.T)
    if nr[:, 0] != sp.zeros(6, 1) or pl[:, 1] != sp.zeros(6, 1):
        raise ArithmeticError('section zero columns')
    for value in pr*sp.Matrix([1, -1, 1]):
        zero(value, 'earlier section kernel')
    # Unit minors prove the ranks uniformly; rational ranks alone would not.
    minors = [nr.extract([0, 1], [1, 2]).det(), nl.extract([1, 2, 4], [0, 1, 2]).det(),
              pr.extract([0, 5], [0, 2]).det(), pl.extract([0, 4], [0, 2]).det()]
    if minors != [1, 1, 1, 1]:
        raise ArithmeticError('section unit minors')
    return {'new_right_left_kernel_dimensions': [1, 0],
            'earlier_right_left_kernel_dimensions': [1, 1], 'section_unit_minors': [int(value) for value in minors]}


def report():
    check_pins()
    t, x, y = sp.symbols('t x y')
    M = family(t, x, y)
    if [M[0, 0], M[0, 1], M[2, 1]] != [t, x, y]:
        raise ArithmeticError('three independent directions')
    D, A, T = invariants(M)
    for value, label in ((D+t*x*y, 'coefficient determinant'), (A+x*y, 'integer A2'), (T, 'integer T4')):
        zero(value, label)
    e = M[1, 1]
    P12 = D**4+(e*D+2*T)*(e*D*T+T*T-A*D*D)
    zero(P12, 'integer P12')
    R, v = literal_source(M), kernel(t, x, y)
    if v[2] != -y*y:
        raise ArithmeticError('primitive kernel coordinate')
    for entry in R*v:
        zero(entry, 'integer source kernel')
    minor = R.minor_submatrix(0, 2)
    determinant = sp.factor(minor.det(method='domain-ge'))
    zero(determinant+t*t*x**7*y**5, 'literal generic minor')
    zero(R.det(method='domain-ge'), 'literal source determinant')
    unit = minor.subs({t: 1, x: 1, y: 1})
    if unit.det(method='bareiss') != -1:
        raise ArithmeticError('unit basepoint minor')
    obstruction = sp.expand(e**3-16*D)
    if sp.Poly(obstruction, t, x, y).coeff_monomial(t**3) != 1:
        raise ArithmeticError('odd extension obstruction')
    return {'claim': 'AI-QUADRATIC-CHAIN-THREE-001', 'scope': 'geometric family over every field',
            'dimension': 3, 'coefficient_matrix': [[str(v) for v in row] for row in M.tolist()],
            'coefficient_determinant': str(D), 'integer_A2': str(A), 'integer_T4': str(T),
            'integer_P12': 0, 'literal_source_determinant': 0,
            'polynomial_right_kernel': [str(entry) for entry in v],
            'deleted_row_pair': [0, 0], 'deleted_column_pair': [0, 2],
            'generic_minor': str(determinant), 'basepoint': [1, 1, 1],
            'base_minor_determinant': -1, 'base_minor_matrix': [[int(v) for v in row] for row in unit.tolist()],
            **section_checks(), 'odd_extension_obstruction': str(obstruction),
            'maximality_dependencies': ['characteristic-two sharp cap three', 'odd attainer identity 16D=m^3'],
            'finite_pilot_is_classification': False, 'complete_char2_classification': False,
            'independent_review': False, 'lean_formalized': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2))
