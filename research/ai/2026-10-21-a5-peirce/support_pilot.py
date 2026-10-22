"""Discovery only: actual trace support in an adapted A5 principal basis."""
import argparse
from itertools import product
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from pilot import HERE, radical, indices, xor


def run(report):
    original = radical.group()
    even = report['original_even_indices']
    lookup = {g: i for i, g in enumerate(even)}
    M = [[lookup[original['mul'][g][h]] for h in even] for g in even]
    inverse = [row.index(0) for row in M]

    def mul(a, b):
        return xor(xor(1 << M[g][h] for h in indices(b)) for g in indices(a))

    vectors, types = [], []
    for corner in report['corners']:
        i, j = corner['i'], corner['j']
        if i >= 3 or j >= 3:
            continue
        span = {}
        for k in range(4, -1, -1):
            for text in corner['bases'][k]:
                value = int(text, 16)
                if radical.insert(value, span):
                    vectors.append(value)
                    types.append((i, j, k))
    if len(vectors) != 44:
        raise ArithmeticError('wrong principal basis dimension')
    keys = sorted(set(types))
    coefficients = np.array([types.count(key) for key in keys])
    inverted = [xor(1 << inverse[g] for g in indices(v)) for v in vectors]
    products = [[mul(a, b) for b in vectors] for a in vectors]
    support, constraints = [], set()
    for i, j, k in product(range(44), repeat=3):
        if (products[i][j] & inverted[k]).bit_count() % 2:
            a, b, c = types[i], types[j], types[k]
            if (a[1] != b[0] or b[1] != c[0] or c[1] != a[0]
                    or a[2]+b[2]+c[2] > 4):
                raise ArithmeticError('trace support escapes the corner/Loewy majorant')
            support.append([i, j, k])
            constraints.add(tuple([a, b, c].count(key) for key in keys))
    A = np.array(sorted(constraints))
    start = np.array([(key[2]-4/3)*np.log(.75) for key in keys])
    result = minimize(lambda w: coefficients @ np.exp(w), start,
                      jac=lambda w: coefficients*np.exp(w), method='SLSQP',
                      constraints={'type': 'ineq', 'fun': lambda w: A @ w, 'jac': lambda w: A},
                      bounds=[(-20, 20)]*len(keys), options={'ftol': 1e-10, 'maxiter': 1000})
    return {'status': 'numerical-discovery-only', 'basis': [hex(v) for v in vectors],
            'basis_types': types, 'trace_support': support, 'keys': keys,
            'coefficients': coefficients.tolist(), 'constraints': A.tolist(),
            'weights': result.x.tolist(), 'optimizer_success': bool(result.success),
            'minimum_constraint_value': float(min(A @ result.x)),
            'principal_score_estimate': float(result.fun),
            'split_score_estimate': float((result.fun+16)*(27/4)**(1/3)),
            'exact_exclusion_established': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ('status', 'optimizer_success',
                     'principal_score_estimate', 'split_score_estimate', 'minimum_constraint_value')}))
