"""Discovery only: exact modular algebra powers in characteristic five."""
import argparse
from itertools import product
import json
from math import comb
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
P = 5


def echelon(rows, target=None):
    A = np.array(rows, dtype=np.int64, copy=True) % P
    columns = A.shape[1]
    if target is not None:
        A = np.column_stack((A, np.array(target, dtype=np.int64)))
    pivots = []
    r = 0
    for c in range(columns):
        candidates = np.flatnonzero(A[r:, c])
        if not len(candidates):
            continue
        i = r+int(candidates[0])
        A[[r, i]] = A[[i, r]]
        A[r] = (A[r]*pow(int(A[r, c]), -1, P)) % P
        factors = A[:, c].copy()
        factors[r] = 0
        A = (A-factors[:, None]*A[r]) % P
        pivots.append(c)
        r += 1
        if r == len(A):
            break
    if target is not None and np.any(A[r:, -1]):
        raise ValueError('no linear preimage')
    return A[:r], pivots


def kernel(rows):
    A, pivots = echelon(rows)
    free = sorted(set(range(A.shape[1]))-set(pivots))
    basis = []
    for c in free:
        v = np.zeros(A.shape[1], dtype=np.int64)
        v[c] = 1
        v[pivots] = -A[:, c] % P
        basis.append(v)
    return np.array(basis), len(pivots)


def run():
    identity = (1, 0, 0, 1)
    matrices = [identity]+sorted(A for A in product(range(5), repeat=4)
                                 if (A[0]*A[3]-A[1]*A[2]) % 5 == 1 and A != identity)
    lookup = {A: i for i, A in enumerate(matrices)}

    def matrix_product(A, B):
        a, b, c, d = A
        e, f, g, h = B
        return ((a*e+b*g) % 5, (a*f+b*h) % 5, (c*e+d*g) % 5, (c*f+d*h) % 5)

    multiplication = np.array([[lookup[matrix_product(A, B)] for B in matrices] for A in matrices])
    inverse = np.array([list(row).index(0) for row in multiplication])
    inverse_rows = multiplication[inverse]

    def mul(a, b):
        return a @ b[inverse_rows] % P

    def power(a, exponent):
        out = np.eye(1, 120, dtype=np.int64)[0]
        while exponent:
            if exponent & 1:
                out = mul(out, a)
            a = mul(a, a)
            exponent //= 2
        return out

    def symmetric_representation(A, degree):
        a, b, c, d = A
        out = np.zeros((degree+1, degree+1), dtype=np.int64)
        for j in range(degree+1):
            for u in range(degree-j+1):
                for v in range(j+1):
                    out[u+v, j] += (comb(degree-j, u)*pow(a, degree-j-u)*pow(c, u)
                                    *comb(j, v)*pow(b, j-v)*pow(d, v))
        return out % P

    representations = [[symmetric_representation(A, degree) for A in matrices] for degree in range(5)]
    for module in representations:
        for a in range(120):
            for b in range(120):
                if not np.array_equal(module[a] @ module[b] % P, module[multiplication[a, b]]):
                    raise ArithmeticError('symmetric-power action is not multiplicative')
    images = np.array([np.concatenate([module[g].ravel() for module in representations]) for g in range(120)])
    J, image_rank = kernel(images.T)
    if image_rank != 55 or len(J) != 65:
        raise ArithmeticError('unexpected semisimple image dimension')
    bases = [np.eye(120, dtype=np.int64), J]
    for _ in range(1, 15):
        rows = np.concatenate([bases[-1] @ b[inverse_rows] % P for b in J])
        basis, _ = echelon(rows)
        bases.append(basis)
        print('power dimensions', [len(b) for b in bases], flush=True)
        if not len(basis):
            break
        if len(basis) == len(bases[-2]):
            raise ArithmeticError('proposed kernel is not shown nilpotent')
    if len(bases[-1]):
        raise ArithmeticError('nilpotency cutoff not reached')
    # Solve for the identity of the degree-four image factor, then lift it.
    target = np.zeros(55, dtype=np.int64)
    target[30:] = np.eye(5, dtype=np.int64).ravel()
    A, pivots = echelon(images.T, target)
    steinberg = np.zeros(120, dtype=np.int64)
    steinberg[pivots] = A[:, -1]
    steinberg = power(steinberg, 125)
    if not np.array_equal(mul(steinberg, steinberg), steinberg):
        raise ArithmeticError('projector lift is not idempotent')
    unit = np.eye(1, 120, dtype=np.int64)[0]
    z = np.zeros(120, dtype=np.int64)
    z[lookup[(4, 0, 0, 4)]] = 1
    projectors = [(3*(unit+z)-steinberg) % P, (3*(unit-z)) % P, steinberg]
    if not np.array_equal(sum(projectors) % P, unit):
        raise ArithmeticError('blocks do not sum to the identity')
    blocks = []
    for e in projectors:
        if not np.array_equal(mul(e, e), e):
            raise ArithmeticError('block is not idempotent')
        if any(not np.array_equal(mul(row, e), mul(e, row)) for row in np.eye(120, dtype=np.int64)):
            raise ArithmeticError('block is not central')
        block_bases = [echelon(B @ e[inverse_rows] % P)[0] if len(B) else B for B in bases]
        dimensions = [len(B) for B in block_bases]
        while len(dimensions) > 2 and dimensions[-2] == 0:
            dimensions.pop()
        layers = [a-b for a, b in zip(dimensions, dimensions[1:])]
        blocks.append({'projector': e.tolist(), 'dimensions': dimensions, 'layers': layers})
    return {'status': 'discovery-only', 'group': 'SL(2,F5)', 'coefficient_field': 'F5',
            'image_rank': image_rank, 'kernel_power_dimensions': [len(b) for b in bases],
            'blocks': blocks, 'exclusion_established': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report[key] for key in ('status', 'image_rank', 'kernel_power_dimensions')}))
    print('block layers', [block['layers'] for block in report['blocks']])
