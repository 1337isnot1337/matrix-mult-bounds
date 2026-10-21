"""Exact necessary tests on fixed Cartan blocks; no degeneration is constructed."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path
import gzip
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "paired_all_ranks", ROOT / "research/ai/2026-10-20-paired-sources/all_ranks.py")
paired = importlib.util.module_from_spec(spec)
spec.loader.exec_module(paired)


@lru_cache(None)
def wedges(m, p):
    return tuple(combinations(range(m), p))


def rank_mod2(dimensions, terms, p):
    """Rank over F2, hence a lower bound for the same integer matrix over Q."""
    a, b, c = dimensions
    rows = {w: i for i, w in enumerate(wedges(a, p+1))}
    by_input = defaultdict(list)
    for x, y, z in terms:
        by_input[y].append((x, z))
    pivots = {}
    for wedge in wedges(a, p):
        occupied = set(wedge)
        for y in range(b):
            vector = 0
            for x, z in by_input[y]:
                if x not in occupied:
                    vector ^= 1 << (c*rows[tuple(sorted(wedge+(x,)))]+z)
            while vector:
                pivot = vector.bit_length()-1
                if pivot in pivots:
                    vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    break
    return len(pivots)


@lru_cache(None)
def wedge_weights(vectors):
    counts = [defaultdict(int) for _ in range(len(vectors)+1)]
    counts[0][0, 0] = 1
    for j, (x, y) in enumerate(vectors):
        for p in range(j+1, 0, -1):
            for (u, v), multiplicity in counts[p-1].items():
                counts[p][u+x, v+y] += multiplicity
    return counts


def grading_upper(vectors, p):
    counts = wedge_weights(tuple(vectors[0]))
    columns, rows = defaultdict(int), defaultdict(int)
    for (x, y), multiplicity in counts[p].items():
        for u, v in vectors[1]:
            columns[x-u, y-v] += multiplicity
    for (x, y), multiplicity in counts[p+1].items():
        for u, v in vectors[2]:
            rows[x+u, y+v] += multiplicity
    return sum(min(n, rows[w]) for w, n in columns.items())


def source_blocks(a):
    m = 2*a-1
    coordinates = [list(product(range(a), range(m), range(a))),
                   list(product(range(a), range(a), range(m))),
                   list(product(range(m), range(a), range(a)))]
    weights = [[k-i-s for i, k, s in coordinates[0]],
               [k-j-p for j, p, k in coordinates[1]],
               [k-q-r for k, q, r in coordinates[2]]]
    grades = [[(i, k) for i, k, s in coordinates[0]],
              [(j, -p) for j, p, k in coordinates[1]],
              [(-k, -q) for k, q, r in coordinates[2]]]
    groups = [{w: [i for i, x in enumerate(vec) if x == w] for w in set(vec)}
              for vec in weights]
    positions = [{w: {x: i for i, x in enumerate(v)} for w, v in g.items()}
                 for g in groups]
    blocks = defaultdict(list)
    for i, j, p, q, r, s in product(range(a), repeat=6):
        term = ((i*m+p+q)*a+s, (j*a+p)*m+r+s, ((i+j)*a+q)*a+r)
        block_weights = tuple(weights[k][term[k]] for k in range(3))
        assert sum(block_weights) == 0
        assert all(sum(grades[k][term[k]][g] for k in range(3)) == 0 for g in range(2))
        blocks[block_weights].append(tuple(positions[k][block_weights[k]][term[k]] for k in range(3)))
    return blocks, groups, grades


def target_shapes(a, weights):
    u = [1, 1]+[2]*(2*a-5)+[1, 1]
    w = [1]+[2]*(a-2)+[1]+[2]*(a-2)+[1]
    shapes = []
    for i in range(len(u)):
        j, k = i+weights[0], i+weights[0]+weights[1]
        if 0 <= j < len(u) and 0 <= k < len(w):
            shapes.append((u[i], u[j], w[k]))
    return shapes


def modular_powers(dimensions):
    a, b, _ = dimensions
    maximum = min(2, a-1)
    if a >= 4 and comb(a, 3)*b <= 10000:
        maximum = 3
    if a <= 10:
        maximum = (a-1)//2
    return range(maximum+1)


def records_for(a):
    blocks, groups, grades = source_blocks(a)
    records = []
    for weights, terms in sorted(blocks.items()):
        shapes = target_shapes(a, weights)
        if not shapes:
            continue
        dimensions = tuple(len(groups[k][weights[k]]) for k in range(3))
        for axis in range(3):
            order = [axis, (axis+1)%3, (axis+2)%3]
            dims = tuple(dimensions[k] for k in order)
            tensor = [tuple(t[k] for k in order) for t in terms]
            vectors = [[grades[k][x] for x in groups[k][weights[k]]] for k in order]
            # paired.py uses first leg l*r, second l*b, third b*r.
            oriented = [(s[(axis+1)%3], s[(axis+2)%3], s[axis]) for s in shapes]
            selected = modular_powers(dims)
            for p in range(dims[0]):
                target = sum(paired.padded_matrix_rank(s, dims[0], p) for s in oriented)
                upper = grading_upper(vectors, p)
                assert upper >= target
                record = {'a': a, 'weights': weights, 'axis': axis, 'power': p,
                          'dimensions': dims, 'target_shapes': oriented,
                          'source_grading_rank_upper': upper, 'target_rank': target}
                if p in selected:
                    lower = rank_mod2(dims, tensor, p)
                    assert target <= lower <= upper
                    record['source_rank_mod2'] = lower
                records.append(record)
    return records


def report():
    records = sum((records_for(a) for a in (3, 4, 5)), [])
    summary = [{'a': a, 'grading_comparisons': sum(r['a'] == a for r in records),
                'modular_comparisons': sum(r['a'] == a and 'source_rank_mod2' in r for r in records)}
               for a in (3, 4, 5)]
    return {'summary': summary, 'records': records, 'constructed': False,
            'general_exclusion': False, 'new_exponent_established': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = report()
    payload = (json.dumps(result, separators=(',', ':'))+'\n').encode()
    args.output.write_bytes(gzip.compress(payload, mtime=0))
    print(json.dumps(result['summary'], indent=2))
