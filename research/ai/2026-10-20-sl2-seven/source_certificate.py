"""Exact rational center calculation for C[SL(2,7)].

SymPy supplies rational matrix and polynomial arithmetic. The result uses no
floating character values and imports no character table.
"""
import argparse
from fractions import Fraction
import json
from math import isqrt
from pathlib import Path
import sys

import sympy as sp

sys.path.insert(0, str(Path(__file__).with_name('imported')))
from group_exact import group


def derive():
    G = group(7)
    n = len(G['mul'])
    unseen, classes = set(range(n)), []
    while unseen:
        x = min(unseen)
        orbit = sorted({G['mul'][G['mul'][g][x]][G['inv'][g]]
                        for g in range(n)})
        classes.append(orbit)
        unseen.difference_update(orbit)
    labels = {g: i for i, c in enumerate(classes) for g in c}
    r = len(classes)
    constants = [[[0]*r for _ in classes] for _ in classes]
    for i, ci in enumerate(classes):
        for j, cj in enumerate(classes):
            counts = [0]*r
            for x in ci:
                for y in cj:
                    counts[labels[G['mul'][x][y]]] += 1
            for k, ck in enumerate(classes):
                if counts[k] % len(ck):
                    raise ArithmeticError('nonintegral class product')
                constants[i][j][k] = counts[k]//len(ck)

    z = list(range(r))
    M = sp.Matrix(r, r, lambda k, j:
                  sum(z[i]*constants[i][j][k] for i in range(r)))
    unit = sp.eye(r)[:, 0]
    powers = [unit]
    for _ in range(1, r+1):
        powers.append(M*powers[-1])
    cyclic = sp.Matrix.hstack(*powers[:r])
    determinant = cyclic.det()
    if not determinant:
        raise ArithmeticError('chosen center generator is not cyclic')
    x = sp.Symbol('x')
    P = M.charpoly(x).as_poly()
    if sum((c*powers[int(mon[0])] for mon, c in P.terms()),
           sp.zeros(r, 1)) != sp.zeros(r, 1):
        raise ArithmeticError('central polynomial identity failed')
    factors = sp.factor_list(P)[1]
    projectors, records, degrees = [], [], []
    for f, multiplicity in factors:
        if multiplicity != 1 or not f.is_irreducible:
            raise ArithmeticError('irreducible squarefree factor required')
        h = P.exquo(f)
        E = (h*sp.invert(h, f)).rem(P)
        e = sum((c*powers[int(mon[0])] for mon, c in E.terms()),
                sp.zeros(r, 1))
        Ematrix = sum((c*(M**int(mon[0])) for mon, c in E.terms()),
                     sp.zeros(r))
        if Ematrix*e != e or any(Ematrix*v != sp.zeros(r, 1)
                                for _, v in projectors):
            raise ArithmeticError('central idempotent identities failed')
        projectors.append((Ematrix, e))
        d2 = n*e[0]/f.degree()
        if d2.q != 1 or isqrt(int(d2))**2 != d2:
            raise ArithmeticError('non-square complex block dimension')
        degree = isqrt(int(d2))
        degrees.extend([degree]*f.degree())
        records.append({'irreducible_factor': list(map(int, f.all_coeffs())),
                        'central_idempotent': list(map(str, e)),
                        'regular_rank': int(n*e[0]),
                        'number_of_complex_blocks': f.degree(),
                        'complex_matrix_degree': degree})
    if sum((e for _, e in projectors), sp.zeros(r, 1)) != unit:
        raise ArithmeticError('central projectors do not sum to identity')
    degrees.sort()
    if sum(d*d for d in degrees) != n:
        raise ArithmeticError('Wedderburn dimensions do not exhaust group')
    return {'group': G['name'], 'order': n, 'class_sizes': list(map(len, classes)),
            'class_representatives': [list(G['matrices'][c[0]]) for c in classes],
            'center_generator_coefficients': z,
            'cyclic_basis_determinant': str(determinant),
            'minimal_polynomial': list(map(int, P.all_coeffs())),
            'rational_central_blocks': records, 'complex_degrees': degrees,
            'arithmetic': 'exact integers and rationals',
            'sympy_version': sp.__version__}


def root_floor(a, n):
    """Floor(a**(1/n)), with a final integer comparison."""
    if a < 0 or n < 1:
        raise ValueError('nonnegative integer and positive root index required')
    if a < 2:
        return a
    upper = 1 << ((a.bit_length()+n-1)//n)
    value = upper >> 1
    while upper-value > 1:
        middle = (upper+value)//2
        if pow(middle, n) <= a:
            value = middle
        else:
            upper = middle
    if not pow(value, n) <= a < pow(value+1, n):
        raise ArithmeticError('root interval failed')
    return value


def exponent_gate(degrees, shape=(16, 16, 17), tau=Fraction(2247, 1000)):
    """A conditional source/target comparison, not a tensor witness."""
    if len(shape) != 3 or min(shape) <= 0:
        raise ValueError('positive matrix dimensions required')
    volume = shape[0]*shape[1]*shape[2]
    scale = 10**10
    m, q = tau.numerator, tau.denominator
    upper = [root_floor(pow(d, m)*pow(scale, q), q)+1 for d in degrees]
    lower = root_floor(pow(volume, m)*pow(scale, 3*q), 3*q)
    if sum(upper) >= lower:
        raise ArithmeticError('strict exponent gate does not pass')
    return {'shape': list(shape), 'tau': str(tau), 'scale': scale,
            'source_term_upper_numerators': upper,
            'source_upper_numerator': sum(upper),
            'target_lower_numerator': lower,
            'strict_positive_margin_numerator': lower-sum(upper),
            'meaning': 'Conditional comparison only. No degeneration supplied.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = derive()
    report['conditional_exponent_gate'] = exponent_gate(report['complex_degrees'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'degrees': report['complex_degrees'],
                      'conditional_gate': report['conditional_exponent_gate']}))


if __name__ == '__main__':
    main()
