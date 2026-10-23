"""Discovery only: full nonsplit F4 trace after exact Peirce lifting."""
import argparse
from collections import Counter
from functools import lru_cache
import gzip
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = 120
MASK = (1 << N)-1


def indices(value):
    while value:
        bit = value & -value
        yield bit.bit_length()-1
        value ^= bit


def xor(values):
    out = 0
    for value in values:
        out ^= value
    return out


def scale(value, a):
    lo, hi = value & MASK, value >> N
    return [0, value, hi | ((lo ^ hi) << N), (lo ^ hi) | (lo << N)][a]


def insert(value, span):
    while value:
        lo, hi = value & MASK, value >> N
        pivot = (lo | hi).bit_length()-1
        a = ((lo >> pivot) & 1) | (((hi >> pivot) & 1) << 1)
        if pivot not in span:
            span[pivot] = scale(value, {1: 1, 2: 3, 3: 2}[a])
            return True
        value ^= scale(span[pivot], a)
    return False


def run():
    prior = json.loads((ROOT/'results/a5-peirce-2026-10-21/tight-certificate.json').read_text())
    discovery = json.loads(gzip.decompress((ROOT/'results/a5-peirce-2026-10-21/f4-pilot.json.gz').read_bytes()))
    identity = (1, 0, 0, 1)
    matrices = [identity]+sorted(tuple(row['matrix']) for row in prior['cover_projection']
                                 if tuple(row['matrix']) != identity)
    lookup = {A: i for i, A in enumerate(matrices)}

    def matrix_product(A, B):
        a, b, c, d = A
        e, f, g, h = B
        return ((a*e+b*g) % 5, (a*f+b*h) % 5, (c*e+d*g) % 5, (c*f+d*h) % 5)

    M = [[lookup[matrix_product(A, B)] for B in matrices] for A in matrices]
    inv = [row.index(0) for row in M]
    projection = {tuple(row['matrix']): row['image'] for row in prior['cover_projection']}
    reps = [next(i for i, A in enumerate(matrices) if projection[A] == q) for q in range(60)]
    z = lookup[(4, 0, 0, 4)]

    def lift(value):
        return xor(1 << (reps[i]+leg*N) for leg in range(2)
                   for i in indices((value >> (leg*60)) & ((1 << 60)-1)))

    @lru_cache(maxsize=50000)
    def translate(g, value):
        return xor(1 << M[g][h] for h in indices(value))

    @lru_cache(maxsize=50000)
    def binary_mul(a, b):
        return xor(translate(g, b) for g in indices(a))

    def mul(a, b):
        a0, a1, b0, b1 = a & MASK, a >> N, b & MASK, b >> N
        aa, bb = binary_mul(a0, b0), binary_mul(a1, b1)
        return (aa ^ bb) | ((binary_mul(a0, b1) ^ binary_mul(a1, b0) ^ bb) << N)

    ids, remaining = [], 1
    for encoded in discovery['idempotents']:
        value = mul(mul(remaining, lift(int(encoded, 16))), remaining)
        value = mul(value, value)
        if mul(value, value) != value or any(mul(value, e) or mul(e, value) for e in ids):
            raise ArithmeticError('nonorthogonal idempotent lift')
        ids.append(value)
        remaining ^= value
    if remaining:
        raise ArithmeticError('lifted idempotents do not sum to the identity')
    basis, types = [], []
    old_types = discovery['basis_types']+[[5+i, 5+j, 0] for i in range(4) for j in range(4)]
    for text, (i, j, degree) in zip(prior['basis'], old_types):
        value = mul(mul(ids[i], lift(int(text, 16))), ids[j])
        basis += [value, mul(value, 1 ^ (1 << z))]
        types += [[i, j, degree, 0], [i, j, degree, 1]]
    span = {}
    for value in basis:
        insert(value, span)
    if len(basis) != 120 or len(span) != 120:
        raise ArithmeticError('singular full nonsplit basis')
    inverted = []
    for value in basis:
        inverted.append(tuple(xor(1 << inv[g] for g in indices((value >> (leg*N)) & MASK))
                              for leg in range(2)))
    support, degrees = [], Counter()
    for a in range(N):
        for b in range(N):
            value = mul(basis[a], basis[b])
            lo, hi = value & MASK, value >> N
            for c, (c0, c1) in enumerate(inverted):
                low = ((lo & c0).bit_count() ^ (hi & c1).bit_count()) & 1
                high = ((lo & c1).bit_count() ^ (hi & c0).bit_count() ^ (hi & c1).bit_count()) & 1
                coefficient = low | (high << 1)
                if coefficient:
                    block = 'P' if max(a, b, c) < 88 else ('M' if min(a, b, c) >= 88 else 'mixed')
                    d = sum(types[v][2] for v in (a, b, c))
                    central_degree = sum(types[v][3] for v in (a, b, c))
                    degrees[block, d, central_degree] += 1
                    support.append([a, b, c, coefficient])
    return {'status': 'discovery-only', 'group': 'SL(2,F5)',
            'basis': [hex(value) for value in basis], 'basis_types': types,
            'idempotents': [hex(e) for e in ids], 'basis_rank': len(span),
            'support': support,
            'degree_counts': [[*key, count] for key, count in sorted(degrees.items())],
            'exponent_improvement': False, 'exclusion_established': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'basis_rank', 'degree_counts')}))
