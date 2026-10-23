"""Variable-initial-moment discovery pilot; exact finite scope only."""

import argparse
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    'additive_cost_source', ROOT/'research/ai/2026-10-23-hankel-annihilator-degree/verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def literal_matrix(sequence, a, b):
    coeff = v.source.coefficients(sequence, a, b)
    m = a+b-1
    rows = itertools.product(range(b), range(a), range(m))
    columns = list(itertools.product(range(m), range(b), range(a)))
    return [[int(coeff.get((H-j, p+q, L-t), 0)) for H, q, t in columns]
            for j, p, L in rows]


def modular_rank(matrix, prime):
    a = [[int(c) % prime for c in row] for row in matrix]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][column], -1, prime)
        a[rank] = [(c*inverse) % prime for c in a[rank]]
        for i in range(rank+1, len(a)):
            c = a[i][column]
            if c:
                a[i] = [(x-c*y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def report():
    x, z = v.X, v.Z
    cases = []
    for g0 in (0, 1):
        for cs in itertools.product((-1, 0, 1), repeat=4):
            if g0 == 0 and not any(cs):
                continue
            g1 = cs[0]+cs[1]*x+cs[2]*z+cs[3]*x*z
            f = [g0, g1, x*z*g0, x*z*g1, x**2*z**2*g0]
            if v.sp.expand(g0*g0*x*z-g1*g1) == 0:
                raise ArithmeticError('Declared deficient symbol rank is incorrect')
            rank = modular_rank(literal_matrix(f, 3, 3), 32003)
            row = {'g0': g0, 'g1_coefficients': list(cs), 'rank_mod_32003': rank}
            if rank < 24:
                row['rational_rank'] = v.source.exact_rank(literal_matrix(f, 3, 3))
            cases.append(row)
    return {'scope': '161 declared ternary initial-moment cases for A(3,3) and V^2-xz U^2',
            'cases': cases, 'declared_cases': 161, 'candidate_additive_bound': 24,
            'minimum_modular_rank': min(c['rank_mod_32003'] for c in cases),
            'rational_violations': sum(c.get('rational_rank', 24) < 24 for c in cases),
            'general_additive_inequality_proved': False,
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
