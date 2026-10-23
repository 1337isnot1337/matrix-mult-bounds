"""Independent literal factorization and finite controls of the chart minimum."""

import argparse
import importlib.util
import itertools
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('binomial_chart_pilot', PACKAGE/'pilot.py')
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)
x, z = pilot.v.X, pilot.v.Z


def feasible_seeds(a, b, r):
    if not 2 <= r < min(a, b):
        raise ValueError('The deficient binomial chart requires 2<=r<min(a,b)')
    return [j for j in range(r) if (a+b-2-j)//r < min(a, b)]


def basis_sequence(a, b, r, seed):
    if seed not in feasible_seeds(a, b, r):
        raise ValueError('Infeasible source seed')
    return [(x*z)**((k-seed)//r) if k % r == seed else 0
            for k in range(a+b-1)]


def residue_counts(length, r):
    return [(length-1-s)//r+1 for s in range(r)]


def rank_formula(a, b, r, seed):
    if seed not in feasible_seeds(a, b, r):
        raise ValueError('Infeasible source seed')
    u, v = residue_counts(a, r), residue_counts(b, r)
    return sum((b+u[s]-1)*(a+v[(seed-s) % r]-1) for s in range(r))


def balanced_minimum(n, r):
    if not 2 <= r < n:
        raise ValueError('Invalid balanced chart')
    q, t = divmod(n, r)
    return r*n*n+2*n*(n-r)+r*(q-1)**2+2*(q-1)*t+max(0, 2*t-r)


def keys(a, b, r, seed):
    m = a+b-1
    row_keys = []
    for short_j, p, L in itertools.product(range(b), range(a), range(m)):
        s, P = p % r, p//r
        row_keys.append((s, short_j+P, L-P))
    column_keys = []
    for H, q, short_t in itertools.product(range(m), range(b), range(a)):
        t, Q = q % r, q//r
        s = (seed-t) % r
        h = (s+t-seed)//r
        column_keys.append((s, H-Q-h, short_t+Q+h))
    return row_keys, column_keys


def check_key_rectangles(a, b, r, seed):
    rows, columns = keys(a, b, r, seed)
    shared = set(rows) & set(columns)
    u, v = residue_counts(a, r), residue_counts(b, r)
    expected = set()
    for s in range(r):
        t = (seed-s) % r
        h = (s+t-seed)//r
        expected.update((s, A, B) for A in range(b+u[s]-1)
                        for B in range(h, h+a+v[t]-1))
    if shared != expected or len(shared) != rank_formula(a, b, r, seed):
        raise ArithmeticError('Exact key-rectangle identity failed')
    return rows, columns, shared


def literal_certificate(a, b, r, seed):
    rows, columns, shared = check_key_rectangles(a, b, r, seed)
    matrix = pilot.literal_matrix(basis_sequence(a, b, r, seed), a, b)
    for i, row in enumerate(matrix):
        if any(value != int(rows[i] == columns[j]) for j, value in enumerate(row)):
            raise ArithmeticError('Key factorization differs from a literal source coefficient')
    row_first, column_first = {}, {}
    for i, key in enumerate(rows):
        row_first.setdefault(key, i)
    for j, key in enumerate(columns):
        column_first.setdefault(key, j)
    ordered = sorted(shared)
    chosen_rows = [row_first[key] for key in ordered]
    chosen_columns = [column_first[key] for key in ordered]
    for i, row in enumerate(chosen_rows):
        for j, column in enumerate(chosen_columns):
            if matrix[row][column] != int(i == j):
                raise ArithmeticError('Literal identity minor failed')
    return {'a': a, 'b': b, 'r': r, 'seed': seed,
            'source_dimension': len(rows), 'exact_rank': len(shared),
            'all_source_coefficients_checked': len(rows)**2,
            'identity_minor_rows': chosen_rows, 'identity_minor_columns': chosen_columns}


def torus_control():
    a = b = 4
    r = 2
    initial = [1, 1+x+z+x*z]
    f = [pilot.v.sp.expand((x*z)**(k//r)*initial[k % r]) for k in range(a+b-1)]
    supports = []
    for j, g in enumerate(initial):
        for (i, s), coefficient in pilot.v.sp.Poly(g, x, z).terms():
            if coefficient:
                supports.append((i, s, j, coefficient))
    second = [j-r*s for i, s, j, _ in supports]
    alpha = max(second)-min(second)+1
    beta, gamma = -alpha-r, 1
    weighted = [(i*alpha+s*beta+j*gamma, i, s, j, c) for i, s, j, c in supports]
    weighted.sort()
    if len({row[0] for row in weighted}) != len(weighted):
        raise ArithmeticError('Torus weights failed to separate initial monomials')
    lowest, i, s, seed, coefficient = weighted[0]
    coeff = pilot.v.source.coefficients(f, a, b)
    limit = {key: c for key, c in coeff.items()
             if key[0]*alpha+key[1]*gamma+key[2]*beta == lowest}
    expected = pilot.v.source.coefficients(
        [coefficient*x**i*z**s*t for t in basis_sequence(a, b, r, seed)], a, b)
    if limit != expected or any(I*alpha+k*gamma+S*beta < lowest for I, k, S in coeff):
        raise ArithmeticError('Coefficientwise monomial limit failed')
    rank_mod = pilot.modular_rank(pilot.literal_matrix(f, a, b), 32003)
    lower = rank_formula(a, b, r, seed)
    if rank_mod < lower:
        raise ArithmeticError('Literal finite rank violates the proposed weight-limit bound')
    return {'a': a, 'b': b, 'r': r, 'initial_moments': [str(g) for g in initial],
            'weights_alpha_gamma_beta': [alpha, gamma, beta],
            'normalizing_weight': lowest,
            'limit_seed': seed, 'limit_monomial_x_z': [i, s],
            'limit_exact_rank': lower, 'original_rank_mod_32003': rank_mod}


def report():
    formats, seed_cases = [], 0
    for a in range(3, 10):
        for b in range(3, 10):
            for r in range(2, min(a, b)):
                seeds = feasible_seeds(a, b, r)
                ranks = []
                for seed in seeds:
                    check_key_rectangles(a, b, r, seed)
                    ranks.append(rank_formula(a, b, r, seed))
                    seed_cases += 1
                formats.append({'a': a, 'b': b, 'r': r, 'feasible_seeds': seeds,
                                'basis_ranks': ranks, 'chart_minimum': min(ranks) if ranks else None})
    closed_cases = 0
    for n in range(3, 61):
        for r in range(2, n):
            if balanced_minimum(n, r) != min(rank_formula(n, n, r, j) for j in range(r)):
                raise ArithmeticError('Balanced closed formula differs from the cyclic convolution')
            closed_cases += 1
    chosen = [(3, 3, 2, 0), (3, 3, 2, 1), (4, 4, 2, 0), (4, 4, 2, 1),
              (4, 4, 3, 0), (4, 4, 3, 2), (5, 5, 2, 0), (5, 5, 2, 1),
              (5, 5, 4, 0), (5, 5, 4, 3), (3, 5, 2, 1), (5, 3, 2, 1),
              (4, 6, 3, 0), (4, 6, 3, 1), (4, 6, 3, 2), (6, 4, 3, 1),
              (5, 7, 3, 0), (5, 7, 3, 2), (7, 5, 3, 1)]
    certificates = [literal_certificate(*parameters) for parameters in chosen]
    return {'format_range': {'a': [3, 9], 'b': [3, 9], 'r': '2<=r<min(a,b)'},
            'source_formats_checked': len(formats), 'feasible_seed_cases_checked': seed_cases,
            'formats': formats, 'balanced_closed_cases_checked': closed_cases,
            'balanced_closed_range': {'n': [3, 60], 'r': '2<=r<n'},
            'literal_certificates': certificates,
            'literal_coefficients_checked': sum(c['all_source_coefficients_checked'] for c in certificates),
            'torus_control': torus_control(), 'field_scope_of_written_theorem': 'Every field',
            'general_degree_one_additive_conjecture_proved': False,
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
