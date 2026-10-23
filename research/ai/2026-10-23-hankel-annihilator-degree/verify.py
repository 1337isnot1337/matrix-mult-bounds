"""Literal finite checks for the annihilator-degree coefficient ranks."""

import argparse
import importlib.util
import json
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'degree_source_controls', ROOT/'research/ai/2026-10-23-hankel-equality/verify.py')
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)
X, Z = source.X, source.Z


def primitive_degree(vector, variable, other):
    domain = sp.QQ.frac_field(other)
    fractions = [sp.fraction(sp.cancel(c)) for c in vector if c]
    denominator = sp.Poly(1, variable, domain=domain)
    for _, d in fractions:
        denominator = sp.lcm(denominator, sp.Poly(d, variable, domain=domain))
    polys = [sp.Poly(sp.cancel(n*denominator.as_expr()/d), variable, domain=domain)
             for n, d in fractions]
    gcd = polys[0]
    for polynomial in polys[1:]:
        gcd = sp.gcd(gcd, polynomial)
    return int(max(f.degree() for f in polys)-gcd.degree())


def annihilator_degrees(sequence, r):
    recurrence = sp.Matrix([sequence[k:k+r+1] for k in range(len(sequence)-r)])
    kernel = DomainMatrix.from_Matrix(recurrence).convert_to(
        sp.QQ.frac_field(X, Z)).nullspace().to_Matrix()
    if kernel.rows != 1:
        raise ArithmeticError('Supporting form is not unique in the declared rank')
    vector = list(kernel)
    return primitive_degree(vector, X, Z), primitive_degree(vector, Z, X)


def inner_ranks(sequence, a, b):
    m = a+b-1
    z_coeff = [sp.Poly(f, Z) for f in sequence]
    x_coeff = [sp.Poly(f, X) for f in sequence]
    forward = [[z_coeff[p+q].nth(k-j) if k >= j else 0
                for q in range(b) for j in range(a)]
               for p in range(a) for k in range(m)]
    reverse = [[x_coeff[p+q].nth(k-j) if k >= j else 0
                for p in range(a) for j in range(b)]
               for q in range(b) for k in range(m)]
    return source.exact_rank(forward, (X,)), source.exact_rank(reverse, (Z,))


def control(name, sequence, a, b, r, degree_x, degree_z, expected_full=None):
    if annihilator_degrees(sequence, r) != (degree_x, degree_z):
        raise ArithmeticError('Declared primitive annihilator degrees are incorrect')
    rho, sigma = inner_ranks(sequence, a, b)
    predicted = (a*r+(b-r)*min(degree_z, a),
                 b*r+(a-r)*min(degree_x, b))
    if (rho, sigma) != predicted:
        raise ArithmeticError('Primitive-degree coefficient-rank formula failed')
    row = source.control(name, sequence, a, b, r, expected_full)
    lower = a*b*r+max(b*(b-r)*min(degree_z, a),
                        a*(a-r)*min(degree_x, b))
    if row['full_slice_rank'] < lower:
        raise ArithmeticError('Degree-dependent source-rank lower bound failed')
    row.update({'primitive_degrees': [degree_x, degree_z],
                'literal_inner_ranks': [rho, sigma],
                'predicted_inner_ranks': list(predicted),
                'degree_lower_bound': lower,
                'constant_scheme_strip_width': min(a*(a-r), b*(b-r))})
    return row


def monomial_sequence(a, b, r, variable, degree):
    f = [variable**(degree*(k//r)) if k % r == 0 else 0
         for k in range(a+b-1)]
    source.coefficients(f, a, b)  # Check source bounds before a rank calculation.
    return f


def report():
    balanced = []
    for n in range(3, 8):
        for r in range(2, n):
            f = monomial_sequence(n, n, r, X, 1)
            balanced.append(control(f'balanced-n{n}-r{r}', f, n, n, r, 1, 0,
                                    n*n*r+n*(n-r)))
    other = []
    for a, b, r in [(4, 6, 3), (6, 4, 3)]:
        for variable, degrees in [(X, (1, 0)), (Z, (0, 1))]:
            f = monomial_sequence(a, b, r, variable, 1)
            full = a*b*r+(a*(a-r) if variable == X else b*(b-r))
            other.append(control(f'rectangular-{a}-{b}-{variable}', f, a, b, r,
                                 *degrees, expected_full=full))
    for n, r, e in [(5, 4, 2), (6, 5, 2), (7, 6, 3)]:
        f = monomial_sequence(n, n, r, X, e)
        other.append(control(f'higher-degree-n{n}-r{r}-e{e}', f, n, n, r, e, 0,
                             n*n*r+n*(n-r)*e))
    both = [control('both-variables', [1, 0, X*Z, 0, X**2*Z**2],
                    3, 3, 2, 1, 1),
            control('rational-moving-support', [(1+X)**2, 0, (1+X)*(1+Z),
                                               0, (1+Z)**2],
                    3, 3, 2, 1, 1)]
    return {'balanced_sharpness_controls': balanced,
            'unbalanced_and_higher_degree_controls': other,
            'two_variable_controls': both,
            'scope': 'Exact finite controls of a written unreviewed general argument.',
            'independent_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    data = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end='')
