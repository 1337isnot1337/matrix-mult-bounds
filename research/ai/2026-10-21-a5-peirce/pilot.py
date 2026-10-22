"""Discovery only: exact A5 corners and numerical Loewy weight candidates."""
import argparse
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PRIOR = HERE.parent/'2026-10-21-s5-block-filtration/discovery'
sys.path.insert(0, str(PRIOR))
from peirce import indices, xor, solver, radical


def run():
    original = radical.group()
    reps = radical.representations(original)[:2]
    even = [g for g, p in enumerate(original['matrices'])
            if sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
    lookup = {g: i for i, g in enumerate(even)}
    M = [[lookup[original['mul'][g][h]] for h in even] for g in even]
    image_dimensions = []
    for representation in reps:
        span = {}
        for g in even:
            radical.insert(representation[g], span)
        image_dimensions.append(len(span))
    if image_dimensions == [16, 8]:
        reps = list(reversed(reps))
    elif image_dimensions != [8, 16]:
        raise ArithmeticError('unexpected restricted image dimensions')
    images = [1 | (reps[0][g] << 1) | (reps[1][g] << 17) for g in even]
    preimage = solver(images)
    for a, g in enumerate(even):
        for b, h in enumerate(even):
            for representation in reps:
                if radical.matrix_product(representation[g], representation[h]) != representation[even[M[a][b]]]:
                    raise ArithmeticError('restricted representation is not multiplicative')

    @lru_cache(maxsize=25000)
    def translate(g, value):
        return xor(1 << M[g][h] for h in indices(value))

    def mul(a, b):
        return xor(translate(g, b) for g in indices(a))

    def image(a):
        return xor(images[g] for g in indices(a))

    other_rows = [sum(1 << g for g in range(60) if images[g] >> bit & 1)
                  for bit in [0]+list(range(17, 33))]
    natural = {}
    for value in radical.kernel(other_rows, 60):
        radical.insert((image(value) >> 1) & 65535, natural)
    if len(natural) != 8:
        raise ArithmeticError('natural block image must have dimension eight')
    matrices = [0]
    for value in natural.values():
        matrices += [old ^ value for old in matrices]

    def rank(A):
        rows = {}
        for i in range(4):
            radical.insert((A >> (4*i)) & 15, rows)
        return len(rows)

    first = min(A for A in matrices if rank(A) == 2 and radical.matrix_product(A, A) == A)
    identity = sum(1 << i for i in (0, 5, 10, 15))
    slots = [1, first << 1, (identity ^ first) << 1]+[1 << (17+i) for i in (0, 5, 10, 15)]
    idempotents, remaining = [], 1
    for slot in slots:
        value = mul(mul(remaining, preimage(slot)), remaining)
        for _ in range(3):
            value = mul(value, value)
        if mul(value, value) != value or image(value) != slot:
            raise ArithmeticError('idempotent lift failed')
        if any(mul(e, value) or mul(value, e) for e in idempotents):
            raise ArithmeticError('idempotents are not mutually orthogonal')
        idempotents.append(value)
        remaining ^= value
    if remaining:
        raise ArithmeticError('idempotents do not sum to one')
    principal = xor(idempotents[:3])
    if any(mul(principal, 1 << g) != mul(1 << g, principal) for g in range(60)):
        raise ArithmeticError('principal block projector is not central')
    prior = json.loads((PRIOR/'A5-radical.json').read_text())
    powers = [[1 << g for g in range(60)]]+[[int(v, 16) for v in row] for row in prior['bases']]
    corners, coefficients = [], {}
    for i, e in enumerate(idempotents):
        for j, f in enumerate(idempotents):
            bases = []
            for power in powers:
                basis = {}
                for value in power:
                    radical.insert(mul(mul(e, value), f), basis)
                bases.append(list(basis.values()))
            if not bases[0]:
                continue
            corners.append({'i': i, 'j': j, 'dimensions': list(map(len, bases)),
                            'bases': [[hex(v) for v in row] for row in bases]})
            if i < 3 and j < 3:
                for k, (a, b) in enumerate(zip(bases, bases[1:])):
                    if len(a) > len(b):
                        coefficients[i, j, k] = len(a)-len(b)
    keys = sorted(coefficients)
    constraints = set()
    for a, b, c in product(keys, repeat=3):
        if a[1] == b[0] and b[1] == c[0] and c[1] == a[0] and a[2]+b[2]+c[2] <= 4:
            constraints.add(tuple([a, b, c].count(key) for key in keys))
    A = np.array(sorted(constraints))
    sizes = np.array([coefficients[key] for key in keys])
    start = np.array([(key[2]-4/3)*np.log(.75) for key in keys])
    optimum = minimize(lambda w: sizes @ np.exp(w), start,
                       jac=lambda w: sizes*np.exp(w), method='SLSQP',
                       constraints={'type': 'ineq', 'fun': lambda w: A @ w, 'jac': lambda w: A},
                       bounds=[(-20, 20)]*len(keys), options={'ftol': 1e-10, 'maxiter': 1000})
    return {'status': 'numerical-discovery-only', 'group': 'A5',
            'original_even_indices': even, 'natural_image_dimension': len(natural),
            'idempotents': [hex(v) for v in idempotents], 'principal_projector': hex(principal),
            'corners': corners, 'keys': keys, 'coefficients': sizes.tolist(),
            'constraints': A.tolist(), 'weights': optimum.x.tolist(),
            'optimizer_success': bool(optimum.success), 'optimizer_message': str(optimum.message),
            'minimum_constraint_value': float(min(A @ optimum.x)),
            'principal_score_estimate': float(optimum.fun),
            'A5_score_estimate': float(optimum.fun+16),
            'split_score_estimate': float((optimum.fun+16)*(27/4)**(1/3)),
            'exponent_improvement': False, 'exact_exclusion_established': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ('status', 'optimizer_success',
                     'principal_score_estimate', 'A5_score_estimate', 'split_score_estimate',
                     'minimum_constraint_value')}))
