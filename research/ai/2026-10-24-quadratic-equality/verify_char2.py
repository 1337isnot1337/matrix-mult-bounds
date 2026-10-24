"""Polynomial characteristic-two equality certificates with literal source checks."""
import json

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def reduce_two(expression):
    variables = sorted(expression.free_symbols, key=str)
    if not variables:
        return sp.Integer(int(expression) % 2)
    return sp.Poly(expression, *variables, modulus=2).as_expr()


def require_zero(expression, label):
    if reduce_two(sp.expand(expression)) != 0:
        raise ArithmeticError(label)


def determinant_factors(M):
    a, b, c, d, e, f, g, h, i = list(M)
    D = M.det()
    A = b*h+d*f
    T = (a*a*i*i+a*b*h*i+a*d*f*i+a*c*h*h+a*f*f*g+b*b*g*i
         +b*c*g*h+b*d*f*h+b*e*f*g+c*c*g*g+c*d*d*i+c*d*e*h
         +c*d*f*g+c*e*e*g)
    G = D**3+e*e*D*T+e*T*T+e*A*D*D
    return D, T, reduce_two(D*D*G)


def literal_determinant(M):
    source = sp.Matrix([[M[H-j, L-r] if 0 <= H-j < 3 and 0 <= L-r < 3 else 0
                         for H in range(5) for r in range(3)]
                        for j in range(3) for L in range(5)])
    variables = sorted(M.free_symbols, key=str)
    domain = sp.GF(2).poly_ring(*variables) if variables else sp.GF(2)
    exact = DomainMatrix.from_Matrix(source).convert_to(domain)
    return domain.to_sympy(exact.det())


def top_quartic(a, c, d, f, g, i):
    return (a*i+c*g)**2+a*d*f*i+a*f*f*g+c*d*d*i+c*d*f*g


def symbolic_checks():
    a, c, d, f, g, h, i, t = sp.symbols('a c d f g h i t')
    cases = [
        ('row_column_extension', sp.Matrix([[0, 0, 1], [0, 1, f], [1, h, i]]), 1),
        ('kernel_first_coordinate', sp.Matrix([[a, 0, 0], [d, 1, 0], [g, 0, 1]]), a**6),
        ('kernel_last_coordinate', sp.Matrix([[a, 0, 1], [d, 1, 0], [g, 0, 0]]), g**6),
        ('kernel_middle_escape', sp.Matrix([[0, 1, 0], [d, 1, 0], [0, 0, 1]]), d**5),
        ('off_conic_escape', sp.Matrix([[t, t, 0], [d+1, 1, 0], [0, 0, 1]]),
         t**5*d*d*(d**3+d+t)),
    ]
    controls = []
    for label, matrix, expected in cases:
        expected = sp.sympify(expected)
        _, _, factored = determinant_factors(matrix)
        require_zero(factored-expected, label+' factor identity')
        actual = literal_determinant(matrix)
        require_zero(actual-expected, label+' literal source identity')
        controls.append({'label': label, 'source_size': 15,
                         'variables': sorted(map(str, matrix.free_symbols)),
                         'determinant_mod_two': str(reduce_two(expected)),
                         'literal_source_matches': True})
    M = sp.Matrix([[a, 0, c], [d, 1, f], [g, 0, i]])
    D, T, determinant = determinant_factors(M)
    top = top_quartic(a, c, d, f, g, i)
    require_zero(D-(a*i+c*g), 'middle-column coefficient determinant')
    require_zero(T-top-c*g, 'middle-column quartic including adfi')
    variables = (a, c, d, f, g, i)
    polynomial = sp.Poly(determinant, *variables, modulus=2)
    degree = polynomial.total_degree()
    highest = sum(coefficient*sp.prod(x**power for x, power in zip(variables, monomial))
                  for monomial, coefficient in polynomial.terms() if sum(monomial) == degree)
    if degree != 12:
        raise ArithmeticError('highest source degree')
    require_zero(highest-D*D*top*top, 'highest homogeneous part')
    left = sp.Poly(sp.expand(top), c, f, i)
    right = sp.Poly(sp.expand(top), a, d, g)
    for actual, expected in zip([left.coeff_monomial(i*i), left.coeff_monomial(c*c),
                                 left.coeff_monomial(c*i)], [a*a, g*g, d*d]):
        require_zero(actual-expected, 'left coefficient gcd certificate')
    for actual, expected in zip([right.coeff_monomial(a*a), right.coeff_monomial(g*g),
                                 right.coeff_monomial(a*g)], [i*i, c*c, f*f]):
        require_zero(actual-expected, 'right coefficient gcd certificate')
    alpha, beta, gamma, delta, s, r, lam = sp.symbols('alpha beta gamma delta s r lam')
    det = alpha*delta+beta*gamma
    A = sp.Matrix([[alpha**2, alpha*gamma, gamma**2], [0, det, 0],
                   [beta**2, beta*delta, delta**2]])
    eta = sp.Matrix([0, 1, 0])
    pair = (alpha*s+beta*r, gamma*s+delta*r)
    expected = sp.Matrix([pair[0]**2, pair[0]*pair[1], pair[1]**2])+lam*det*eta
    actual = A.T*(sp.Matrix([s*s, s*r, r*r])+lam*eta)
    for entry in actual-expected:
        require_zero(entry, 'kernel orbit action')
    for entry in eta.T*A-det*eta.T:
        require_zero(entry, 'middle coefficient scaling')
    return {'literal_symbolic_controls': controls, 'literal_control_count': len(controls),
            'middle_column_quartic_includes_adfi': True,
            'middle_column_highest_degree': degree,
            'highest_part': '(ai+cg)^2*T_top^2',
            'left_coefficient_gcd_certificate': ['a^2', 'g^2', 'd^2'],
            'right_coefficient_gcd_certificate': ['i^2', 'c^2', 'f^2'],
            'binary_action_and_middle_coefficient_identities': True,
            'scope': 'Polynomial identities over F2; no finite-point census or exhaustive family search',
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    print(json.dumps(symbolic_checks(), indent=2))
