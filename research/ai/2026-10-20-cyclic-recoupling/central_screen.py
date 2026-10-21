"""A determinant certificate that the central multiplicity tensor is not M2."""
import argparse
import json
from pathlib import Path

import sympy as sp

from coefficients import read_json


def report(grouped):
    block = next(b for b in grouped['blocks'] if b['degrees'] == [6, 6, 6])
    assert block['multiplicity_dimensions'] == [4, 4, 4]
    x = sp.symbols('x0:4')
    matrix = sp.zeros(4)
    for i, j, k, coefficient in block['multiplicity_terms']:
        matrix[j, k] += sp.Rational(coefficient)*x[i]
    determinant = sp.factor(matrix.det())
    specialized = sp.Poly(determinant.subs({x[1]: 1, x[2]: 0, x[3]: 0}), x[0])
    _, primitive = specialized.clear_denoms(convert=True)[1].primitive()
    f = primitive.set_domain(sp.QQ)
    derivative = f.diff()
    u, v, divisor = sp.gcdex(f, derivative)
    assert divisor == sp.Poly(1, x[0], domain=sp.QQ)
    assert u*f+v*derivative == divisor
    assert f.degree() == 4
    return {'a': 4, 'representation_degrees': [6, 6, 6],
        'slice_determinant': str(determinant),
        'specialization': {'x1': 1, 'x2': 0, 'x3': 0},
        'primitive_quartic_coefficients_high_to_low': [int(c) for c in f.all_coeffs()],
        'bezout_u_high_to_low': [str(c) for c in u.all_coeffs()],
        'bezout_v_high_to_low': [str(c) for c in v.all_coeffs()],
        'bezout_identity': 'u*f+v*derivative(f)=1',
        'squarefree_quartic_verified': True,
        'ordinary_restriction_to_M2_excluded': True,
        'arbitrary_degeneration_to_M2_excluded': False,
        'new_exponent_established': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(report(read_json(args.input)), indent=2)+'\n')
    print('Squarefree quartic certificate passed; arbitrary degeneration is not excluded.')
