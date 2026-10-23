"""Construct complete degree-eight/degree-nine maps preserving PR107's two-jet."""
import argparse
import importlib.util
import json
from pathlib import Path

import sympy as s


ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('fixed_two_credited_cores',
    ROOT / 'research/ai/2026-10-23-conic-polynomial-curve/construct.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
a, b, d, t, x = prior.a, prior.b, prior.d, prior.t, prior.x


def product(left, right):
    result = [s.S.Zero]*(len(left)+len(right)-1)
    for i, u in enumerate(left):
        for j, v in enumerate(right):
            result[i+j] += u*v
    return [s.factor(z) for z in result]


def core_coefficients():
    u0, v0 = prior.cores()
    u = s.Matrix([a, a*d**3, 1, d**3])
    v = s.Matrix([-b, 1, -b*d**3, d**3])
    f, e = s.Matrix([0, 1, 0, 0]), s.Matrix([0, 0, 1, 0])
    delta = (a+d**3)*(b-d**3)
    u3 = u0.applyfunc(lambda z: s.Poly(z, x).nth(3))
    v3 = v0.applyfunc(lambda z: s.Poly(z, x).nth(3))
    avec, dvec = u3*v, v3*u
    h = s.Matrix([-delta**2*(b-2*d**3)/(3*d**2),
                  -d*delta**2*(b+d**3)/3,
                  delta**2*(b-d**3)/(3*d**2), 0, 0,
                  b*d*delta**2/3, 0])
    w = s.Matrix([delta**2*(b-d**3)/(3*d**2), 0,
                  b*d*delta**2/3, delta**2*(b-d**3)/(3*d**2)])
    evec = u3*w
    kappa = delta**2*(delta+b*d**3)/(3*d**2)
    if (u0.subs(x, d)*w+h+d*delta**2*avec/3).applyfunc(s.expand) != s.zeros(7, 1):
        raise ArithmeticError('second-order boundary identity failed')
    if s.expand((w.T*u)[0]-kappa) != 0:
        raise ArithmeticError('wrong varying-gauge pairing')
    left_root = [d, -2*delta/3, delta**2/(9*d)]
    right_root = [d, delta/3, delta**2/(9*d), -kappa]
    left_cube = product(product(left_root, left_root), left_root)
    right_cube = product(product(right_root, right_root), right_root)
    # The residuals Up(s(t))*v(t) and Vp(r(t))*u. Their first three
    # coefficients vanish; the polynomial projections therefore fix the jet.
    left_residual = [s.zeros(7, 1) for _ in range(9)]
    right_residual = [s.zeros(7, 1) for _ in range(10)]
    for order in range(1, len(left_cube)):
        left_residual[order] += left_cube[order]*avec
        left_residual[order+2] += left_cube[order]*evec
    left_residual[1] += 2*d*d*delta*avec
    left_residual[2] -= s.Rational(5, 3)*d*delta**2*avec
    left_residual[3] -= d*d*kappa*avec
    left_residual[4] += s.Rational(4, 3)*d*delta*kappa*avec
    for order in range(1, len(right_cube)):
        right_residual[order] = right_cube[order]*dvec
    right_residual[1] -= d*d*delta*dvec
    right_residual[2] -= s.Rational(2, 3)*d*delta**2*dvec
    for residual in (left_residual, right_residual):
        if any(z.applyfunc(s.expand) != s.zeros(7, 1) for z in residual[:3]):
            raise ArithmeticError('projection would change the prescribed two-jet')
    left = [-z*f.T for z in left_residual]
    right = [-z*e.T for z in right_residual]
    left[0] += u0
    left[1] += d*d*avec*(delta*f-u).T
    left[2] += h*f.T+s.Rational(4, 3)*d*delta*avec*u.T
    right[0] += v0
    right[1] += d*d*dvec*v.T
    right[2] += s.Rational(2, 3)*d*delta*dvec*v.T
    for root, matrices, vector, other in (
            (left_root, left, avec, evec),
            (right_root, right, v, w)):
        square = product(root, root)
        p = [square[k]+(root[k]*x if k < len(root) else 0)
             for k in range(len(square))]
        p[0] += x*x
        for order, value in enumerate(p):
            if matrices is left:
                matrices[order+1] += value*vector*u.T
                matrices[order+3] += value*other*u.T
            else:
                matrices[order+1] -= value*dvec*vector.T
                matrices[order+3] -= value*dvec*other.T
    return ([z.applyfunc(s.expand) for z in left],
            [z.applyfunc(s.expand) for z in right])


def construct():
    left, right = core_coefficients()
    return {
        'schema': 'conic-fixed-two-curve-v1',
        'status': 'explicit-witness',
        'claim_id': 'AI-CONIC-FIXED-TWO-CURVE-001',
        'base': 'c=-d^3',
        'chart': 'd != 0',
        'coefficient_ring': 'Q[a,b,d,d^-1]',
        'B': [prior.encode_core(matrix, 'B', 0)[0] for matrix in left],
        'C': [prior.encode_core(matrix, 'C', 0)[0] for matrix in right],
        'source_row_corrections_through_two': [
            {'shape': [100, 12], 'entries': []},
            {'shape': [100, 12], 'entries': []}],
        'fixed_source_kernel': True,
        'normal_class': '[1:d]',
        'prescribed_full_two_jet_preserved': True,
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
