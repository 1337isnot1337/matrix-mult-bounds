"""Exact coefficient controls for the written paired-long-leg proof.

Finite-field source ranks are lower bounds over C. Only a matching
dimension bound or the exported integer kernel makes one an exact rank.
The all-size injectivity assertion is a written proof, not formalized here.
"""
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import comb, gcd, lcm
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
PREDECESSOR = ROOT / 'research/ai/2026-10-20-paired-sources/paired.py'


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def hankel_rank(a, p):
    if a < 2:
        raise ValueError('a>=2 required')
    return a * min(choose(2*a-1, p), choose(2*a-1, p+1))


def injectivity_endpoint(a):
    if a < 2:
        raise ValueError('a>=2 required')
    return a*(a-1)


def long_terms(a):
    """First coordinate is B, second is A, third is C."""
    h = 2*a-1
    return [(y*h+q+v, u*a+q, (u+y)*a+v)
            for u, q, y, v in product(range(a), repeat=4)]


def source_column(a, mask, u, q):
    h = 2*a-1
    for y, v in product(range(a), repeat=2):
        b = y*h+q+v
        if mask >> b & 1:
            continue
        sign = -1 if (mask & ((1 << b)-1)).bit_count() % 2 else 1
        yield (mask | (1 << b), u+y, v), sign


def bit_rank(vectors):
    pivots = {}
    for vector in vectors:
        while vector:
            pivot = vector.bit_length()-1
            if pivot in pivots:
                vector ^= pivots[pivot]
            else:
                pivots[pivot] = vector
                break
    return len(pivots)


def source_rank_mod2(a, p):
    """Independent coefficient lower bound, separated by the two weights."""
    N, h = a*(2*a-1), 2*a-1
    if not 0 <= p <= N:
        raise ValueError('exterior degree out of range')
    blocks = defaultdict(list)
    row_grades = {}
    for subset in combinations(range(N), p+1):
        mask = sum(1 << b for b in subset)
        row_grades[mask] = (sum(b//h for b in subset),
                            sum(b % h for b in subset))
    for subset in combinations(range(N), p):
        mask = sum(1 << b for b in subset)
        sy, sj = sum(b//h for b in subset), sum(b % h for b in subset)
        for u, q in product(range(a), repeat=2):
            blocks[sy-u, sj+q].append((mask, u, q))
    total = 0
    for weight, columns in blocks.items():
        row_ids = {}

        def vectors():
            for mask, u, q in columns:
                vector = 0
                for (rowmask, z, v), _ in source_column(a, mask, u, q):
                    sy, sj = row_grades[rowmask]
                    if (sy-z, sj-v) != weight:
                        raise ValueError('a coefficient crosses the claimed weight block')
                    row = (rowmask, z, v)
                    if row not in row_ids:
                        row_ids[row] = len(row_ids)
                    vector ^= 1 << row_ids[row]
                yield vector

        total += bit_rank(vectors())
    return total


def generic_koszul_columns(dimensions, terms, p):
    """Full coefficient builder, independent of the paired-source grading."""
    n, m, _ = dimensions
    by_input = defaultdict(list)
    for b, u, v in terms:
        by_input[u].append((b, v))
    columns = []
    for subset in combinations(range(n), p):
        mask = sum(1 << b for b in subset)
        for u in range(m):
            column = defaultdict(int)
            for b, v in by_input[u]:
                if mask >> b & 1:
                    continue
                sign = -1 if (mask & ((1 << b)-1)).bit_count() % 2 else 1
                column[mask | (1 << b), v] += sign
            columns.append({r: x for r, x in column.items() if x})
    return columns


def generic_rank_mod2(columns):
    row_ids = {}

    def vectors():
        for column in columns:
            vector = 0
            for row, value in column.items():
                if value % 2:
                    if row not in row_ids:
                        row_ids[row] = len(row_ids)
                    vector ^= 1 << row_ids[row]
            yield vector

    return bit_rank(vectors())


def hankel_rank_mod2(a, p):
    h = 2*a-1
    terms = [(q+v, q, v) for q, v in product(range(a), repeat=2)]
    return generic_rank_mod2(generic_koszul_columns((h, a, a), terms, p))


def integer_kernel(columns):
    """Small exact rational elimination; export primitive integer vectors."""
    rows = defaultdict(dict)
    for j, column in enumerate(columns):
        for row, value in column.items():
            rows[row][j] = Fraction(value)
    basis = {}
    for row in rows.values():
        vector = dict(row)
        while vector:
            pivot = min(vector)
            if pivot not in basis:
                scale = vector[pivot]
                basis[pivot] = {j: x/scale for j, x in vector.items()}
                break
            factor = vector[pivot]
            for j, value in basis[pivot].items():
                result = vector.get(j, 0)-factor*value
                if result:
                    vector[j] = result
                else:
                    vector.pop(j, None)
    free = sorted(set(range(len(columns)))-set(basis))
    witnesses = []
    for f in free:
        vector = {f: Fraction(1)}
        for pivot in sorted(basis, reverse=True):
            value = -sum(x*vector.get(j, 0) for j, x in basis[pivot].items()
                         if j != pivot)
            if value:
                vector[pivot] = value
        denominator = lcm(*(x.denominator for x in vector.values()))
        integer = {j: int(x*denominator) for j, x in vector.items()}
        divisor = reduce(gcd, map(abs, integer.values()))
        witnesses.append([[j, x//divisor] for j, x in sorted(integer.items())])
    return free, witnesses


def verify_integer_kernel(columns, free, witnesses):
    if len(set(free)) != len(free) or len(free) != len(witnesses):
        raise ValueError('bad free-coordinate count')
    for own_free, pairs in zip(free, witnesses):
        vector = dict(pairs)
        if len(vector) != len(pairs) or not vector.get(own_free):
            raise ValueError('kernel coordinates repeat or lack the independent pivot')
        if any(vector.get(f, 0) for f in free if f != own_free):
            raise ValueError('kernel vectors have no diagonal independent-coordinate minor')
        image = defaultdict(int)
        for j, value in vector.items():
            if not 0 <= j < len(columns) or type(value) is not int:
                raise ValueError('invalid integer kernel entry')
            for row, coefficient in columns[j].items():
                image[row] += value*coefficient
        if any(image.values()):
            raise ValueError('integer kernel vector has nonzero image')
    return len(witnesses)


def source_identity_controls():
    spec = importlib.util.spec_from_file_location('paired_original_source', PREDECESSOR)
    predecessor = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(predecessor)
    counts = []
    for a in range(2, 7):
        dimensions, original = predecessor.source(a)
        actual = long_terms(a)
        if actual != [(b, u, c) for u, b, c in original]:
            raise ValueError('source convention differs from the maintained source')
        # Exchange B,C and transpose A, including the two long-index reorderings.
        h = 2*a-1
        exchanged = [(u % a * a + u//a, (c % a)*h+c//a,
                      (b % h)*a+b//h) for u, b, c in original]
        if sorted(exchanged) != sorted(original):
            raise ValueError('claimed long-leg symmetry is not a tensor identity')
        counts.append({'a': a, 'format': list(dimensions), 'source_terms': len(actual)})
    return counts


def build_report():
    hankel = []
    for a in range(2, 7):
        h = 2*a-1
        ranks = [hankel_rank_mod2(a, p) for p in range(h+1)]
        if ranks != [hankel_rank(a, p) for p in range(h+1)]:
            raise ValueError('Hankel rank does not match the dimension upper bound')
        hankel.append({'a': a, 'ranks': ranks, 'exact_over_C_by_dimension_bound': True})
    paired = []
    degrees = {2: range(3), 3: range(7), 4: range(4), 5: range(2), 6: range(2)}
    for a, powers in degrees.items():
        for p in powers:
            rank = source_rank_mod2(a, p)
            columns = a*a*comb(a*(2*a-1), p)
            if rank != columns:
                raise ValueError('finite injectivity control fails')
            paired.append({'a': a, 'power': p, 'columns': columns, 'mod2_rank': rank,
                           'exact_over_C_by_dimension_bound': True})
    columns = generic_koszul_columns((6, 4, 6), long_terms(2), 3)
    free, witnesses = integer_kernel(columns)
    lower = generic_rank_mod2(columns)
    nullity = verify_integer_kernel(columns, free, witnesses)
    if len(columns)-nullity != lower or lower != 70:
        raise ValueError('beyond-interval rank bounds do not match')
    return {
        'schema': 'paired-long-leg-injectivity-v1',
        'proof_status': 'proof-written-unreviewed',
        'written_theorem': {'fields': 'every field', 'sizes': 'every integer a>=2',
                           'interval': '0<=p<=a*(a-1)',
                           'long_legs': ['B with input A*', 'C with input A*'],
                           'rank': 'a^2*binom(a*(2*a-1),p)'},
        'source_identity_controls': source_identity_controls(),
        'hankel_coefficient_controls': hankel,
        'paired_coefficient_controls': paired,
        'beyond_interval_countercontrol': {
            'a': 2, 'power': 3, 'columns': len(columns), 'mod2_rank': lower,
            'free_columns': free, 'integer_kernel_vectors': witnesses,
            'exact_rank_over_C': lower,
        },
        'no_new_target_exclusion_in_proved_interval': True,
        'higher_degrees_decided': False,
        'independent_review': False,
        'lean_formalized': False,
        'improves_omega': False,
    }


def verify_report(report):
    scope = {'schema': 'paired-long-leg-injectivity-v1',
             'proof_status': 'proof-written-unreviewed',
             'no_new_target_exclusion_in_proved_interval': True,
             'higher_degrees_decided': False, 'independent_review': False,
             'lean_formalized': False, 'improves_omega': False}
    if any(report.get(key) != value for key, value in scope.items()):
        raise ValueError('proof status or unresolved scope was changed')
    pins = json.loads((PACKAGE/'sources.json').read_text())
    for pin in pins['local_sources']:
        if hashlib.sha256((ROOT/pin['path']).read_bytes()).hexdigest() != pin['sha256']:
            raise ValueError('adopted source differs from its inspected byte pin')
    counter = report['beyond_interval_countercontrol']
    columns = generic_koszul_columns((6, 4, 6), long_terms(2), 3)
    verify_integer_kernel(columns, counter['free_columns'], counter['integer_kernel_vectors'])
    if report != build_report():
        raise ValueError('coefficient report or proof scope differs from exact regeneration')
    return {'verified': True, 'paired_full_column_controls': len(report['paired_coefficient_controls']),
            'hankel_all_degree_controls': sum(len(c['ranks']) for c in report['hankel_coefficient_controls']),
            'beyond_interval_exact_complex_rank': 70,
            'formalized_all_size_theorem': False, 'new_target_exclusions': 0,
            'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', type=Path)
    args = parser.parse_args()
    report = (verify_report(json.loads(args.verify.read_text())) if args.verify else build_report())
    text = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end='')
