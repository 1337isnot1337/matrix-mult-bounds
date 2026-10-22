"""Discovery only: split exact A5 corner idempotents over F4."""
import argparse
from functools import lru_cache
from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from pilot import PRIOR, radical, indices, xor

N = 60
MASK = (1 << N)-1


def scale(value, coefficient):
    a, b = value & MASK, value >> N
    if coefficient == 0:
        return 0
    if coefficient == 1:
        return value
    if coefficient == 2:
        return b | ((a ^ b) << N)
    if coefficient == 3:
        return (a ^ b) | (a << N)
    raise ValueError('not an F4 scalar')


def insert(value, basis):
    while value:
        a, b = value & MASK, value >> N
        pivot = (a | b).bit_length()-1
        coefficient = ((a >> pivot) & 1) | (((b >> pivot) & 1) << 1)
        if pivot not in basis:
            basis[pivot] = scale(value, {1: 1, 2: 3, 3: 2}[coefficient])
            return True
        value ^= scale(basis[pivot], coefficient)
    return False


def run(prior):
    original = radical.group()
    even = prior['original_even_indices']
    lookup = {g: i for i, g in enumerate(even)}
    M = [[lookup[original['mul'][g][h]] for h in even] for g in even]
    inverse = [row.index(0) for row in M]

    @lru_cache(maxsize=25000)
    def translate(g, value):
        return xor(1 << M[g][h] for h in indices(value))

    @lru_cache(maxsize=25000)
    def mul2(a, b):
        return xor(translate(g, b) for g in indices(a))

    def mul(a, b):
        a0, a1, b0, b1 = a & MASK, a >> N, b & MASK, b >> N
        cross = mul2(a1, b1)
        return (mul2(a0, b0) ^ cross) | ((mul2(a0, b1) ^ mul2(a1, b0) ^ cross) << N)

    old = [int(v, 16) for v in prior['idempotents']]
    idempotents, roots = [old[0]], []
    for i in (1, 2):
        corner = next(c for c in prior['corners'] if c['i'] == c['j'] == i)
        candidates = [0]
        for text in corner['bases'][0]:
            candidates += [v ^ int(text, 16) for v in candidates]
        root = min(a for a in candidates if mul2(a, a) ^ a ^ old[i] == 0)
        roots.append(root)
        idempotents += [(root ^ old[i]) | (old[i] << N), root | (old[i] << N)]
    idempotents += old[3:]
    if xor(idempotents) != 1:
        raise ArithmeticError('F4 idempotents do not sum to one')
    for i, e in enumerate(idempotents):
        for j, f in enumerate(idempotents):
            if mul(e, f) != (e if i == j else 0):
                raise ArithmeticError('F4 idempotent product is incorrect')
    raw = json.loads((PRIOR/'A5-radical.json').read_text())
    powers = [[1 << g for g in range(N)]]+[[int(v, 16) for v in row] for row in raw['bases']]
    corners, vectors, types = [], [], []
    for i, e in enumerate(idempotents[:5]):
        for j, f in enumerate(idempotents[:5]):
            bases = []
            for power in powers:
                span = {}
                for value in power:
                    insert(mul(mul(e, value), f), span)
                bases.append(list(span.values()))
            if not bases[0]:
                continue
            corners.append({'i': i, 'j': j, 'dimensions': list(map(len, bases)),
                            'bases': [[hex(v) for v in row] for row in bases]})
            span = {}
            for k in range(4, -1, -1):
                for value in bases[k]:
                    if insert(value, span):
                        vectors.append(value)
                        types.append((i, j, k))
    if len(vectors) != 44:
        raise ArithmeticError('wrong F4 principal dimension')
    keys = sorted(set(types))
    coefficients = np.array([types.count(key) for key in keys])
    coarse = set()
    for a, b, c in product(keys, repeat=3):
        if a[1] == b[0] and b[1] == c[0] and c[1] == a[0] and a[2]+b[2]+c[2] <= 4:
            coarse.add(tuple([a, b, c].count(key) for key in keys))
    inverted = [(xor(1 << inverse[g] for g in indices(v & MASK)),
                 xor(1 << inverse[g] for g in indices(v >> N))) for v in vectors]
    products = [[mul(a, b) for b in vectors] for a in vectors]
    support, exact = [], set()
    for i, j, k in product(range(44), repeat=3):
        a, b = products[i][j] & MASK, products[i][j] >> N
        c, d = inverted[k]
        value = (((a & c).bit_count() ^ (b & d).bit_count()) & 1) | (
            (((a & d).bit_count() ^ (b & c).bit_count() ^ (b & d).bit_count()) & 1) << 1)
        if value:
            row = tuple([types[i], types[j], types[k]].count(key) for key in keys)
            if row not in coarse:
                raise ArithmeticError('F4 support escapes the corner/Loewy majorant')
            support.append([i, j, k, value])
            exact.add(row)
    start = np.array([(key[2]-4/3)*np.log(.75) for key in keys])
    scores = {}
    for name, rows in (('coarse', coarse), ('actual_support', exact)):
        A = np.array(sorted(rows))
        fit = minimize(lambda w: coefficients @ np.exp(w), start,
                       jac=lambda w: coefficients*np.exp(w), method='SLSQP',
                       constraints={'type': 'ineq', 'fun': lambda w: A @ w, 'jac': lambda w: A},
                       bounds=[(-20, 20)]*len(keys), options={'ftol': 1e-10, 'maxiter': 1000})
        scores[name] = {'optimizer_success': bool(fit.success),
                        'minimum_constraint_value': float(min(A @ fit.x)),
                        'principal_score_estimate': float(fit.fun),
                        'split_score_estimate': float((fit.fun+16)*(27/4)**(1/3)),
                        'weights': fit.x.tolist(), 'constraints': A.tolist()}
    return {'status': 'numerical-discovery-only', 'field': 'F2[w]/(w^2+w+1)',
            'encoding': 'low60 coefficient bits plus high60 w-coefficient bits',
            'quadratic_roots_in_old_corners': [hex(v) for v in roots],
            'idempotents': [hex(v) for v in idempotents], 'corners': corners,
            'basis': [hex(v) for v in vectors], 'basis_types': types,
            'keys': keys, 'coefficients': coefficients.tolist(),
            'trace_support': support, 'scores': scores,
            'exact_exclusion_established': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({name: {k: v for k, v in score.items() if k not in ('weights', 'constraints')}
                      for name, score in result['scores'].items()}))
