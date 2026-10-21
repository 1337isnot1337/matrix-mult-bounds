"""Exact modular certificates that cubic minors generate all quartics."""
from itertools import combinations_with_replacement, permutations

import sympy as sp


def field_value(value, prime):
    value = sp.Rational(value)
    if int(value.q) % prime == 0:
        raise ArithmeticError('Coefficient denominator is not a modular unit')
    return int(value.p)*pow(int(value.q), -1, prime) % prime


def insert(polynomial, pivots, prime):
    polynomial = dict(polynomial)
    while polynomial:
        lead = min(polynomial)
        if lead not in pivots:
            inverse = pow(polynomial[lead], -1, prime)
            pivots[lead] = {j: value*inverse % prime for j, value in polynomial.items()}
            return
        multiplier = polynomial[lead]
        for j, value in pivots[lead].items():
            updated = (polynomial.get(j, 0)-multiplier*value) % prime
            if updated:
                polynomial[j] = updated
            else:
                polynomial.pop(j, None)


def reduced_rows(pivots, prime):
    for lead in sorted(pivots, reverse=True):
        row = pivots[lead]
        for other in sorted(j for j in row if j != lead and j in pivots):
            multiplier = row.pop(other)
            for j, value in pivots[other].items():
                if j == other:
                    continue
                updated = (row.get(j, 0)-multiplier*value) % prime
                if updated:
                    row[j] = updated
                else:
                    row.pop(j, None)
    if any(j != lead and j in pivots for lead, row in pivots.items() for j in row):
        raise ArithmeticError('Cubic row reduction is incomplete')
    return list(pivots.values())


def span_report(parts, case, prime):
    """Multiply a verified basis of cubic forms by every normal variable."""
    if not sp.isprime(prime):
        raise ArithmeticError('The certificate modulus is not prime')
    parameters, rows = case['component']['parameters'], case['component']['rows']
    if len(parameters) != 14 or len(set(parameters)) != 14 or len(set(rows)) != len(rows):
        raise ArithmeticError('Incorrect normal block coordinates')
    cells = {(row, c): {j: field_value(parts[c][row, parameter], prime)
              for j, parameter in enumerate(parameters) if parts[c][row, parameter]}
              for row in rows for c in range(6)}
    monomials = list(combinations_with_replacement(range(14), 3))
    indices = {monomial: j for j, monomial in enumerate(monomials)}
    signed = [(p, (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)))
              for p in permutations(range(3))]
    pivots = {}
    for witness in case['witnesses']:
        rr, cc = witness['rows'], witness['columns']
        if (len(rr) != 3 or len(set(rr)) != 3 or not set(rr) <= set(rows)
                or len(cc) != 3 or len(set(cc)) != 3 or not set(cc) <= set(range(6))):
            raise ArithmeticError('Invalid cubic minor coordinates')
        polynomial = {}
        for permutation, sign in signed:
            first, second, third = [cells[rr[k], cc[permutation[k]]] for k in range(3)]
            for i, x in first.items():
                for j, y in second.items():
                    for k, z in third.items():
                        index = indices[tuple(sorted((i, j, k)))]
                        value = (polynomial.get(index, 0)+sign*x*y*z) % prime
                        if value:
                            polynomial[index] = value
                        else:
                            polynomial.pop(index, None)
        insert(polynomial, pivots, prime)
    cubic_rank = len(pivots)
    reduced = reduced_rows(pivots, prime)
    quartics = list(combinations_with_replacement(range(14), 4))
    quartic_indices = {monomial: j for j, monomial in enumerate(quartics)}
    quartic_pivots = {}
    for variable in range(14):
        for row in reduced:
            polynomial = {quartic_indices[tuple(sorted(monomials[j]+(variable,)))]: value
                          for j, value in row.items()}
            insert(polynomial, quartic_pivots, prime)
    if len(quartic_pivots) != len(quartics):
        raise ArithmeticError('Degree-four span is incomplete')
    return {'normal_variables': 14, 'cubic_witnesses': len(case['witnesses']),
            'cubic_rank_mod_prime': cubic_rank, 'quartic_monomials': len(quartics),
            'quartic_rank_mod_prime': len(quartic_pivots), 'prime': prime}
