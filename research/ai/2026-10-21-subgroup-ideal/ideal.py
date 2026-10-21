"""Exact two-sided subgroup-averaging ideals and coordinate obstruction cuts."""
import argparse
from functools import reduce
from math import gcd, lcm
import importlib.util
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
NATIVE = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-five-native-parity'
sys.path.insert(0, str(NATIVE))
from data import data
from split_source import split_data


def sources():
    G, _, _ = data()
    split, _, _ = split_data()
    path = Path(__file__).resolve().parents[1]/'2026-10-20-sl2-five-c2/source_data.py'
    spec = importlib.util.spec_from_file_location('subgroup_ideal_product_source', path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    return G, split, helper.group()


def cyclic_subgroup(G, order=5):
    for g in range(1, len(G['mul'])):
        points, x = [], 0
        for _ in range(order):
            points.append(x)
            x = G['mul'][x][g]
        if x == 0 and len(set(points)) == order:
            return sorted(points)
    raise ValueError('no cyclic subgroup of the requested order')


def ideal_cosets(G, H):
    n, M, inv = len(G['mul']), G['mul'], G['inv']
    if not H or len(set(H)) != len(H) or 0 not in H or any(
            M[g][h] not in H for g in H for h in H):
        raise ValueError('a subgroup is required')
    conjugates = {tuple(sorted(M[M[g][h]][inv[g]] for h in H)) for g in range(n)}
    cosets = {tuple(sorted(M[g][h] for h in K)) for K in conjugates for g in range(n)}
    return sorted(conjugates), sorted(cosets)


def modular_rank(rows, prime=1000003):
    basis = {}
    for row in rows:
        row = [v % prime for v in row]
        for i in range(len(row)):
            value = row[i]
            if not value:
                continue
            if i not in basis:
                inverse = pow(value, -1, prime)
                basis[i] = [v*inverse % prime for v in row]
                break
            old = basis[i]
            row = [(v-value*w) % prime for v, w in zip(row, old)]
    return len(basis)


def derive(G, H):
    n = len(G['mul'])
    conjugates, cosets = ideal_cosets(G, H)
    rows = [[int(g in C) for g in range(n)] for C in map(set, cosets)]
    reduced, pivots = sp.Matrix(rows).rref()
    free = sorted(set(range(n))-set(pivots))
    annihilators = []
    for f in free:
        vector = [sp.Integer(0)]*n
        vector[f] = sp.Integer(1)
        for i, p in enumerate(pivots):
            vector[p] = -reduced[i, f]
        denominator = lcm(*(int(v.q) for v in vector))
        integers = [int(v*denominator) for v in vector]
        common = reduce(gcd, integers)
        annihilators.append([v//common for v in integers])
    return {'group': G['name'], 'order': n, 'subgroup': H,
            'conjugate_subgroups': conjugates, 'cosets': cosets,
            'ideal_dimension': len(pivots), 'free_coordinates': free,
            'integer_annihilators': annihilators, 'rank_control_prime': 1000003,
            'scope': 'A full coset in one target vertex set forces the product '
                     'of the other two sizes to be at most this ideal dimension.',
            'exponent_improvement': False}


def verify(G, record):
    n = len(G['mul'])
    if record['group'] != G['name'] or record['order'] != n:
        raise ValueError('wrong group')
    conjugates, cosets = ideal_cosets(G, record['subgroup'])
    if record['conjugate_subgroups'] != [list(row) for row in conjugates] or record['cosets'] != [list(row) for row in cosets]:
        raise ValueError('wrong subgroup conjugates or coset span')
    D, free, vectors = record['ideal_dimension'], record['free_coordinates'], record['integer_annihilators']
    if (not 0 <= D <= n or free != sorted(set(free)) or len(free) != n-D
            or any(not 0 <= f < n for f in free) or len(vectors) != n-D):
        raise ValueError('wrong claimed ideal codimension')
    for f, vector in zip(free, vectors):
        if (len(vector) != n or any(type(v) is not int for v in vector)
                or vector[f] <= 0 or any(vector[q] for q in free if q != f)):
            raise ValueError('annihilator independence certificate failed')
        if any(sum(vector[g] for g in C) for C in cosets):
            raise ValueError('not an annihilator of the entire ideal')
    rows = [[int(g in C) for g in range(n)] for C in map(set, cosets)]
    if record['rank_control_prime'] != 1000003 or modular_rank(rows) != D:
        raise ValueError('modular lower rank does not match exact upper rank')
    return {'group': G['name'], 'ideal_dimension': D, 'annihilators': n-D,
            'conjugate_subgroups': len(conjugates), 'cosets': len(cosets)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    records = [derive(G, cyclic_subgroup(G)) for G in sources()]
    # JSON normalization matches the separate verifier's input contract.
    records = json.loads(json.dumps(records))
    receipts = [verify(G, r) for G, r in zip(sources(), records)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({'records': records, 'verification': receipts,
                                      'exponent_improvement': False}, indent=2)+'\n')
    print(json.dumps(receipts))
