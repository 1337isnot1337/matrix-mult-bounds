"""Offline exact rational ranks of every Q_(3,2) and target Koszul map.

Both source and target ranks come from signed tensor coefficient matrices.
This is a finite necessary-condition check, not a degeneration certificate.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from collections import defaultdict
from math import comb
import json
from pathlib import Path
import argparse


def source(n, m):
    axes = [list(product(range(n), repeat=2)),
            list(product(range(m), range(n + m - 1))),
            list(product(range(n + m - 1), range(m)))]
    weights = [axes[0], [(y, -j) for y, j in axes[1]], [(-z, v) for z, v in axes[2]]]
    indices = [{c: i for i, c in enumerate(axis)} for axis in axes]
    terms = [(indices[0][p, q], indices[1][y, q + v], indices[2][p + y, v])
             for p, q, y, v in product(range(n), range(n), range(m), range(m))]
    return [len(axis) for axis in axes], weights, terms


def target(n, m, leg, ambient):
    axes = [list(product(range(n), repeat=2)), list(product(range(n), range(m))),
            list(product(range(m), range(n)))]
    weights = [[(i, 0, k) for i, k in axes[0]],
               [(-i, j, 0) for i, j in axes[1]],
               [(0, -j, -k) for j, k in axes[2]]]
    indices = [{c: i for i, c in enumerate(axis)} for axis in axes]
    terms = [(indices[0][i, k], indices[1][i, j], indices[2][j, k])
             for i, j, k in product(range(n), range(m), range(n))]
    dims = [len(axis) for axis in axes]
    padding = ambient - dims[leg]
    if padding < 0:
        raise ValueError('Target first factor exceeds the ambient dimension.')
    # Unused first-factor coordinates can be assigned arbitrary weights.
    for p in range(padding):
        weights[leg].append((100 + p, 1000 + p, 10000 + p))
    dims[leg] = ambient
    return dims, weights, terms


def rank_q(matrix):
    if not matrix:
        return 0
    a = [[Q(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(a[0])):
        selected = next((i for i in range(pivot, len(a)) if a[i][column]), None)
        if selected is None:
            continue
        a[pivot], a[selected] = a[selected], a[pivot]
        value = a[pivot][column]
        for j in range(column, len(a[0])):
            a[pivot][j] /= value
        for i in range(pivot + 1, len(a)):
            multiplier = a[i][column]
            if multiplier:
                for j in range(column, len(a[0])):
                    a[i][j] -= multiplier * a[pivot][j]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def rank_mod2(matrix):
    pivots = {}
    for row in matrix:
        bits = sum((int(value) & 1) << j for j, value in enumerate(row))
        while bits:
            p = bits.bit_length() - 1
            if p in pivots:
                bits ^= pivots[p]
            else:
                pivots[p] = bits
                break
    return len(pivots)


def tensor_rank(dims, weights, terms, leg, power):
    weight_dimension = len(weights[0][0])
    assert all(sum(weights[side][term[side]][k] for side in range(3)) == 0
               for term in terms for k in range(weight_dimension))
    other = [i for i in range(3) if i != leg]
    first, second, third = dims[leg], dims[other[0]], dims[other[1]]
    by_input = defaultdict(list)
    for term in terms:
        by_input[term[other[0]]].append((term[leg], term[other[1]]))
    columns = defaultdict(list)
    for subset in combinations(range(first), power):
        mask = sum(1 << i for i in subset)
        weight = tuple(sum(weights[leg][i][k] for i in subset) for k in range(len(weights[leg][0])))
        for j in range(second):
            key = tuple(x - y for x, y in zip(weight, weights[other[0]][j]))
            columns[key].append((mask, j))
    blocks = []
    for weight, col_keys in sorted(columns.items()):
        entries = []
        row_ids = {}
        for col, (mask, j) in enumerate(col_keys):
            for x, z in by_input[j]:
                if mask >> x & 1:
                    continue
                row = (mask | 1 << x, z)
                if row not in row_ids:
                    row_ids[row] = len(row_ids)
                sign = -1 if (mask >> (x + 1)).bit_count() & 1 else 1
                entries.append((row_ids[row], col, sign))
        matrix = [[0] * len(col_keys) for _ in row_ids]
        for row, col, value in entries:
            matrix[row][col] += value
        r2 = rank_mod2(matrix)
        rational = rank_q(matrix)
        assert rational >= r2
        blocks.append({'weight': list(weight), 'rows': len(row_ids), 'columns': len(col_keys),
                       'rank_q': rational, 'rank_mod2': r2})
    return {'dimensions': dims, 'domain': second * comb(first, power), 'codomain': third * comb(first, power + 1),
            'rank_q': sum(block['rank_q'] for block in blocks),
            'rank_mod2': sum(block['rank_mod2'] for block in blocks),
            'blocks': blocks}


def rank(n, m, leg, power):
    source_data = source(n, m)
    ambient = source_data[0][leg]
    src = tensor_rank(*source_data, leg, power)
    dst = tensor_rank(*target(n, m, leg, ambient), leg, power)
    return {'n': n, 'm': m, 'leg': leg, 'power': power,
            'source_rank_q': src['rank_q'], 'source_rank_mod2': src['rank_mod2'],
            'target_rank_q': dst['rank_q'], 'target_rank_mod2': dst['rank_mod2'],
            'passes': src['rank_q'] >= dst['rank_q'], 'source': src, 'target': dst}


def run(n=3, m=2):
    if n < 1 or m < 1:
        raise ValueError('Source dimensions must be positive.')
    results = []
    dims = source(n, m)[0]
    for leg in range(3):
        for p in range(dims[leg]):
            result = rank(n, m, leg, p)
            results.append(result)
    return {'scope': f'All three legs and all potentially nonzero exterior degrees of Q_({n},{m}) versus M({n},{m},{n}).',
            'field': 'Q, with independent GF(2) lower-rank controls',
            'method': 'Source and target signed coefficient matrices, blocked by exact additive torus weights.',
            'source_dimensions': dims, 'target_dimensions': [n*n, n*m, n*m],
            'comparison_count': len(results), 'all_pass': all(result['passes'] for result in results),
            'improves_omega': False, 'records': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--n', type=int, default=3)
    parser.add_argument('--m', type=int, default=2)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run(args.n, args.m)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'output': str(args.output), 'comparisons': report['comparison_count'],
                      'all_pass': report['all_pass'], 'improves_omega': False}))
