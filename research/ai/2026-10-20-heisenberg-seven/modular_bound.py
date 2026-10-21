"""Exact Petrov-filtration application to coordinate Heisenberg targets.

The filtration is external, not a new result of this repository. The note
states the characteristic-transfer and cyclic-symmetrization hypotheses.
All acceptance comparisons below are rational/integer comparisons.
"""
import argparse
from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path
import sys

FIVE = Path(__file__).resolve().parents[1]/'2026-10-20-heisenberg-five'
sys.path.insert(0, str(FIVE))
from source import require_odd_prime

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)


def root_floor(value, degree):
    lo, hi = 0, 1 << ((value.bit_length()+degree-1)//degree)
    while lo+1 < hi:
        middle = (lo+hi)//2
        if middle**degree <= value:
            lo = middle
        else:
            hi = middle
    return lo


def bound(p, t):
    require_odd_prime(p)
    t = Fraction(t)
    if not 0 < t < 1:
        raise ValueError('a rational parameter strictly between zero and one is required')
    D = 4*(p-1)
    polynomial = sum(t**a for a in range(p))**2*sum(t**(2*c) for c in range(p))
    Q = polynomial**3/t**D  # Cubed asymptotic slice-rank upper bound.
    scale = 10**6
    lower_root = root_floor(p**9*scale**4, 4)
    if not lower_root**4 <= p**9*scale**4 < (lower_root+1)**4:
        raise ArithmeticError('incorrect certified fourth root')
    L = p*p+(p-1)*Fraction(lower_root, scale)
    return {'prime': p, 'parameter': str(t), 'top_weight': D,
            'weight_polynomial': str(polynomial), 'slice_bound_cubed': str(Q),
            'source_cost_lower': str(L), 'root_scale': scale,
            'fourth_root_lower_numerator': lower_root,
            'strict_gate_exclusion': Q**3 < L**8,
            'scope': 'Coordinate/potential degenerations, including joint powers and '
                     'finite rectangular direct sums; usual character-degree gate only.',
            'general_complex_degeneration_excluded': False,
            'exponent_improvement': False}


def finite_filtration(p):
    """Check the PBW change of basis and all right-generator products over Fp."""
    require_odd_prime(p)
    points = list(product(range(p), repeat=3))
    index = {v: i for i, v in enumerate(points)}
    n = p**3

    def normal_coordinates(vector):
        # g(a,b,c)=z^c y^b x^a, and g=(1+Z)^c(1+Y)^b(1+X)^a.
        for axis in range(3):
            output = [0]*n
            for (a, b, c), coefficient in zip(points, vector):
                if not coefficient:
                    continue
                point = [a, b, c]
                upper = point[axis]
                for exponent in range(upper+1):
                    point[axis] = exponent
                    output[index[tuple(point)]] += coefficient*comb(upper, exponent)
            vector = [v % p for v in output]
        return vector

    generators = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    checked = 0
    for a, b, c in points:
        basis = [0]*n
        for i, j, k in product(range(a+1), range(b+1), range(c+1)):
            basis[index[i, j, k]] = (comb(a, i)*comb(b, j)*comb(c, k)
                                    *(-1)**(a+b+c-i-j-k)) % p
        expected = [0]*n
        expected[index[a, b, c]] = 1
        if normal_coordinates(basis) != expected:
            raise ArithmeticError('PBW basis transform failed')
        weight = a+b+2*c
        for (x, y, z), delta in zip(generators, (1, 1, 2)):
            multiplied = [-v for v in basis]
            for (i, j, k), coefficient in zip(points, basis):
                multiplied[index[(i+x) % p, (j+y) % p, (k+z+i*y) % p]] += coefficient
            result = normal_coordinates([v % p for v in multiplied])
            if any(value and i+j+2*k < weight+delta
                   for (i, j, k), value in zip(points, result)):
                raise ArithmeticError('right multiplication decreased the PBW weight')
            checked += 1
    return {'prime': p, 'pbw_basis_vectors': n, 'right_generator_products': checked,
            'coefficient_field': f'F_{p}', 'filtration_verified': True}


def generate():
    rows = []
    for p in PRIMES+(53,):
        # Fixed finite grid; it need not find the true optimum.
        candidates = [bound(p, 1-Fraction(k, 20*p))
                      for k in range(1, min(60, 20*p))]
        rows.append(min(candidates, key=lambda row: Fraction(row['slice_bound_cubed'])))
    return {'external_filtration': 'Petrov arXiv:1606.03256v4 Section 7',
            'proved_exclusion_primes': list(PRIMES), 'bounds': rows,
            'filtration_controls': [finite_filtration(p) for p in (3, 5, 7)],
            'proof_review_status': 'written-unreviewed', 'exponent_improvement': False}


def verify_report(report):
    if report['proved_exclusion_primes'] != list(PRIMES):
        raise ValueError('wrong exclusion-prime list')
    rows = report['bounds']
    if [row['prime'] for row in rows] != list(PRIMES)+[53]:
        raise ValueError('wrong certificate prime coverage')
    for row in rows:
        if row != bound(row['prime'], row['parameter']):
            raise ValueError('changed rational gate certificate')
        if row['strict_gate_exclusion'] != (row['prime'] in PRIMES):
            raise ValueError('wrong gate-exclusion scope')
    controls = [finite_filtration(p) for p in (3, 5, 7)]
    if report['filtration_controls'] != controls:
        raise ValueError('changed finite filtration controls')
    if report['exponent_improvement'] is not False:
        raise ValueError('no exponent improvement was established')
    return {'prime_certificates': len(rows), 'excluded_primes': len(PRIMES),
            'basis_vectors': sum(row['pbw_basis_vectors'] for row in controls),
            'generator_products': sum(row['right_generator_products'] for row in controls)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = generate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'exclusion_primes': report['proved_exclusion_primes'],
                      'filtration_controls': report['filtration_controls']}))
