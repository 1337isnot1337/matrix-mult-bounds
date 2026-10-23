"""Construct an exact cubic curve preserving PR107's full first jet."""
import argparse
import importlib.util
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[3]
PRIOR = ROOT / 'research/ai/2026-10-23-conic-polynomial-curve/construct.py'
spec = importlib.util.spec_from_file_location('fixed_first_credited_cores', PRIOR)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
a, b, d, t, x = prior.a, prior.b, prior.d, prior.t, prior.x


def polynomial_cores():
    u0, v0 = prior.cores()
    u = s.Matrix([a, a*d**3, 1, d**3])
    v = s.Matrix([-b, 1, -b*d**3, d**3])
    f = s.Matrix([0, 1, 0, 0])
    delta = (a+d**3)*(b-d**3)
    left_vector = u0.applyfunc(lambda z: s.Poly(z, x).nth(3))*v
    right_vector = v0.applyfunc(lambda z: s.Poly(z, x).nth(3))*u
    left_coefficients = [
        u0,
        (x*x+d*x)*left_vector*u.T+d*d*delta*left_vector*f.T,
        -s.Rational(2, 3)*delta*(x+d)*left_vector*u.T
        -s.Rational(2, 3)*d*delta**2*left_vector*f.T,
        s.Rational(8, 27)*delta**2*left_vector*u.T
        +s.Rational(4, 27)*delta**3*left_vector*f.T,
    ]
    right_coefficients = [
        v0,
        -(x*x+d*x)*right_vector*v.T,
        -s.Rational(1, 3)*delta*(x+d)*right_vector*v.T,
        -s.Rational(2, 27)*delta**2*right_vector*v.T,
    ]
    left = sum((t**k*z for k, z in enumerate(left_coefficients)), s.zeros(7, 4))
    right = sum((t**k*z for k, z in enumerate(right_coefficients)), s.zeros(7, 4))
    # Separate short formula explains the complete identity; acceptance will
    # instead contract the exported full maps against the literal source.
    root_left = d-s.Rational(2, 3)*delta*t
    root_right = d+s.Rational(1, 3)*delta*t
    alpha = d*d*t-s.Rational(2, 3)*d*delta*t*t+s.Rational(4, 27)*delta**2*t**3
    beta = d*d*t+s.Rational(1, 3)*d*delta*t*t+s.Rational(1, 27)*delta**2*t**3
    left_base = u0+alpha*left_vector*(delta*f-u).T
    right_base = v0+beta*right_vector*v.T
    identities = [
        left_base*v-(x**3-root_left**3)*left_vector,
        right_base*u-(x**3-root_right**3)*right_vector,
        left*right.T-left_base*right_base.T,
    ]
    if any(matrix.applyfunc(s.expand) != s.zeros(*matrix.shape) for matrix in identities):
        raise ArithmeticError('moving-root polynomial identity failed')
    return left.applyfunc(s.expand), right.applyfunc(s.expand)


def construct():
    left, right = polynomial_cores()
    return {
        'schema': 'conic-fixed-first-curve-v1',
        'status': 'explicit-witness',
        'claim_id': 'AI-CONIC-FIXED-FIRST-CURVE-001',
        'base': 'c=-d^3',
        'coefficient_ring': 'Q[a,b,d]',
        'scope': 'Every complex a,b,d',
        'B': prior.encode_core(left, 'B', 3),
        'C': prior.encode_core(right, 'C', 3),
        'fixed_source_kernel': True,
        'normal_class': '[1:d]',
        'full_first_jet_preserved': True,
        'prescribed_second_jet_preserved': False,
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
    args.output.write_text(json.dumps(construct(), indent=2)+'\n')
