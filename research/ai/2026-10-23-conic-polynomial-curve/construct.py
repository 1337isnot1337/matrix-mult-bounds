"""Export a polynomial conic curve from a rank-one rational gauge.

The construction is separate from acceptance: verify.py checks the literal
source equations without importing this file or using the gauge identity.
"""
import argparse
from itertools import product
import json
from pathlib import Path

import sympy as s


a, b, d, t, x = s.symbols('a b d t x')


def cores():
    """The credited constant paired-row maps, grouped as seven 4-vectors."""
    u0 = s.Matrix([
        [0, -x**3, 0, 1],
        [-x**3, 0, 1, 0],
        [0, d**3, 0, -1],
        [-1, -b-d**3, 0, 1],
        [0, b*d**3+d**6, 1, -x**3],
        [0, -b*d**3, -1, 0],
        [0, b*d**6, x**3, 0],
    ])
    v0 = s.Matrix([
        [0, 0, x**3, -1],
        [x**3, -1, 0, 0],
        [1, 0, -a+d**3, -1],
        [0, -1, a*d**3, 0],
        [0, 0, -d**3, 1],
        [0, 1, -a*d**3+d**6, -x**3],
        [0, -x**3, a*d**6, 0],
    ])
    return u0, v0


def polynomial_cores():
    u0, v0 = cores()
    u = s.Matrix([a, a*d**3, 1, d**3])
    v = s.Matrix([-b, 1, -b*d**3, d**3])
    e = s.Matrix([0, 0, 1, 0])
    delta = (a+d**3)*(b-d**3)
    r = d+delta*t
    u3 = u0.applyfunc(lambda z: s.Poly(z, x).nth(3))
    v3 = v0.applyfunc(lambda z: s.Poly(z, x).nth(3))
    if ((u0.subs(x, d)*v).applyfunc(s.expand) != s.zeros(7, 1)
            or (v0.subs(x, d)*u).applyfunc(s.expand) != s.zeros(7, 1)
            or s.expand((v.T*u)[0]+delta) != 0 or (u.T*e)[0] != 1):
        raise ArithmeticError('wrong gauge data')
    left = u0+t*(x**2+d*x+d**2)*(u3*v)*u.T
    adjusted = v0-(r**3-d**3)*(v3*u)*e.T
    right = adjusted-t*(x**2+r*x+r**2)*(v3*u)*v.T
    if (left*right.T-u0*adjusted.T).applyfunc(s.expand) != s.zeros(7, 7):
        raise ArithmeticError('gauge pairing identity failed')
    return left.applyfunc(s.expand), right.applyfunc(s.expand)


def encode_core(matrix, side, degree):
    coefficients = [dict() for _ in range(degree+1)]
    for row, component in product(range(7), range(4)):
        j, r = divmod(component, 2)
        poly = s.Poly(matrix[row, component], t, x)
        if poly.degree(t) > degree or poly.degree(x) > 3:
            raise ArithmeticError('unexpected core degree')
        for order, power, parity in product(range(degree+1), range(4), range(2)):
            value = poly.coeff_monomial(t**order*x**power)
            if not value:
                continue
            column = (28*power+7*(3*j)+4-3*r+parity if side == 'B'
                      else 28*(3*r)+7*power+4-3*j+parity)
            coefficients[order][2*row+parity, column] = value
    return [{'shape': [14, 112],
             'entries': [[i, j, str(s.expand(z))] for (i, j), z in sorted(matrix.items())]}
            for matrix in coefficients]


def construct():
    left, right = polynomial_cores()
    return {
        'schema': 'conic-polynomial-curve-v1',
        'status': 'explicit-witness',
        'claim_id': 'AI-CONIC-POLYNOMIAL-CURVE-001',
        'base': 'c=-d^3',
        'coefficient_ring': 'Q[a,b,d]',
        'scope': 'Every complex a,b,d',
        'B': encode_core(left, 'B', 1),
        'C': encode_core(right, 'C', 3),
        'fixed_source_kernel': True,
        'normal_class': '[1:d]',
        'full_first_jet_preserved': False,
        'all_order_lift_established': True,
        'matrix_target_constructed': False,
        'exponent_improvement': False,
        'independent_mathematical_review': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(construct(), indent=2) + '\n')
