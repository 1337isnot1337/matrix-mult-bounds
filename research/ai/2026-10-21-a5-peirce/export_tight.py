"""Export an exact witness from the A5 discovery data; no numerical weights."""
import argparse
from functools import lru_cache
import gzip
from itertools import permutations
import json
from math import lcm
from pathlib import Path
import random
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RESULTS = ROOT/'results/a5-peirce-2026-10-21'
N = 60
MASK = (1 << N)-1


def indices(value):
    while value:
        bit = value & -value
        yield bit.bit_length()-1
        value ^= bit


def xor(values):
    result = 0
    for value in values:
        result ^= value
    return result


def scale(value, coefficient):
    a, b = value & MASK, value >> N
    return (value, b | ((a ^ b) << N), (a ^ b) | (a << N))[coefficient-1]


def export():
    def discovery(name):
        path = RESULTS/name
        raw = path.read_bytes() if path.exists() else gzip.decompress(Path(str(path)+'.gz').read_bytes())
        return json.loads(raw)

    prior = discovery('pilot.json')
    split = discovery('f4-pilot.json')
    basis = [int(v, 16) for v in split['basis']]
    if split['basis_types'][1][2] != 2 or split['basis_types'][2][2] != 2:
        raise ValueError('unexpected degree-two loop indices')
    first, second = basis[1:3]
    basis[1], basis[2] = first ^ scale(second, 2), first ^ scale(second, 3)
    for i in range(3, 7):
        for j in range(3, 7):
            corner = next(c for c in prior['corners'] if c['i'] == i and c['j'] == j)
            if len(corner['bases'][0]) != 1:
                raise ValueError('defect-zero corner is not one-dimensional')
            basis.append(int(corner['bases'][0][0], 16))
    weights = [4-3*t[2] for t in split['basis_types']]+[0]*16
    points = [p for p in permutations(range(5))
              if sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0]
    lookup = {p: i for i, p in enumerate(points)}
    M = [[lookup[tuple(p[q[k]] for k in range(5))] for q in points] for p in points]
    inverse = [row.index(0) for row in M]

    @lru_cache(maxsize=25000)
    def translate(g, value):
        return xor(1 << M[g][h] for h in indices(value))

    @lru_cache(maxsize=25000)
    def binary_mul(a, b):
        return xor(translate(g, b) for g in indices(a))

    def mul(a, b):
        a0, a1, b0, b1 = a & MASK, a >> N, b & MASK, b >> N
        cross = binary_mul(a1, b1)
        return (binary_mul(a0, b0) ^ cross) | (
            (binary_mul(a0, b1) ^ binary_mul(a1, b0) ^ cross) << N)

    inverted = [(xor(1 << inverse[g] for g in indices(v & MASK)),
                 xor(1 << inverse[g] for g in indices(v >> N))) for v in basis]
    leading = []
    for a in range(N):
        for b in range(N):
            value = mul(basis[a], basis[b])
            low, high = value & MASK, value >> N
            for c, (x, y) in enumerate(inverted):
                coefficient = (((low & x).bit_count() ^ (high & y).bit_count()) & 1) | (
                    (((low & y).bit_count() ^ (high & x).bit_count() ^ (high & y).bit_count()) & 1) << 1)
                if coefficient:
                    exponent = weights[a]+weights[b]+weights[c]
                    if exponent < 0:
                        raise ValueError('discovered basis has a negative coefficient exponent')
                    if exponent == 0:
                        leading.append([a, b, c, coefficient])
    equations = []
    for a, b, c, _ in leading:
        row = [0]*(3*N)
        for leg, i in enumerate((a, b, c)):
            row[leg*N+i] = 1
        equations.append(row)
    kernel = sp.Matrix(equations).nullspace()
    integer_kernel = []
    for vector in kernel:
        denominator = lcm(*(int(v.q) for v in vector))
        integer_kernel.append([int(v*denominator) for v in vector])
    rng = random.Random(20261021)
    tight = None
    for attempt in range(100):
        multipliers = [rng.randrange(-1000000, 1000001) for _ in integer_kernel]
        flat = [sum(c*v[i] for c, v in zip(multipliers, integer_kernel)) for i in range(3*N)]
        candidate = [flat[leg*N:(leg+1)*N] for leg in range(3)]
        if all(len(set(row)) == N for row in candidate):
            tight = candidate
            break
    if tight is None:
        raise ValueError('no injective integer tightness witness found')
    margins = [[0]*120 for _ in range(3)]
    for a, b, c, _ in leading:
        atom = 128 if a < 44 else 213
        for digits in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            for leg, (i, d) in enumerate(zip((a, b, c), digits)):
                margins[leg][2*i+d] += atom
    sys.path.insert(0, str(HERE.parent/'2026-10-20-sl2-five-native-parity'))
    from data import data
    sys.path.insert(0, str(HERE.parent/'2026-10-21-s5-split'))
    from s5_source import control
    G, Q, _ = data()
    embedding = control()['quotient_action_image']
    even_lookup = {g: i for i, g in enumerate(prior['original_even_indices'])}
    projection = [{'matrix': list(matrix),
                   'image': even_lookup[embedding[Q['projection'][g]]]}
                  for g, matrix in enumerate(G['matrices'])]
    return {'source_base_commit': 'ef76802bcbe47adf3076ddcba6a34e8ff221089c',
            'coefficient_field': 'F2[w]/(w^2+w+1)',
            'group_elements': points, 'basis': [hex(v) for v in basis],
            'degeneration_weights': [weights]*3, 'leading_tensor': leading,
            'tight_weights': tight, 'tight_kernel_dimension': len(kernel),
            'tightness_search_seed': 20261021, 'tightness_search_attempts': attempt+1,
            'probability_denominator': 122688, 'marginal_counts': margins,
            'cover_projection': projection,
            'external_sources': ['CVZ19 Theorem1.1.31', 'AVZ20 Section1.4.3 equation11'],
            'scope': 'Asymptotic characteristic-two global source-slice-rank cost barrier; '
                     'no target construction or finite-power exclusion.',
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    certificate = export()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps({'basis': len(certificate['basis']),
                      'leading_terms': len(certificate['leading_tensor']),
                      'tightness_attempts': certificate['tightness_search_attempts']}))
