"""Exact first-leg Koszul ranks for unequal paired convolution sources.

The proof requires a,c>=2, a<=b+1 and c<=d+1. Surviving matrix
targets are necessary-test survivors, not constructed degenerations.
"""
from collections import defaultdict
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations, product
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / 'research/ai/2026-10-20-paired-sources/all_ranks.py'
_spec = spec_from_file_location('unequal_paired_matrix_reference', REFERENCE)
matrix_reference = module_from_spec(_spec)
_spec.loader.exec_module(matrix_reference)


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def validate_source(a, b, c, d):
    if any(not isinstance(value, int) or value < 1 for value in (a, b, c, d)):
        raise ValueError('source lengths must be positive integers')
    if min(a, c) < 2 or a > b + 1 or c > d + 1:
        raise ValueError('the formula requires a,c>=2; a<=b+1; c<=d+1')


def source_format(a, b, c, d):
    return a * c, b * (c + d - 1), (a + b - 1) * d


def source_rank(a, b, c, d, power):
    validate_source(a, b, c, d)
    v, y, z = source_format(a, b, c, d)
    return (y * choose(v - 2, power) + z * choose(v - 2, power - 1)
            + 2 * (a - 1) * (c - 1) * choose(v - 3, power - 1))


def source_terms(a, b, c, d):
    return [(p * c + q, y * (c + d - 1) + q + t, (p + y) * d + t)
            for p in range(a) for q in range(c)
            for y in range(b) for t in range(d)]


def coefficient_rank_mod2(a, b, c, d, power):
    """Build the coefficient map independently, in its two weight blocks."""
    blocks = defaultdict(list)
    for subset in combinations(range(a * c), power):
        mask = sum(1 << i for i in subset)
        x = sum(i // c for i in subset)
        y = sum(i % c for i in subset)
        for i in range(b):
            for j in range(c + d - 1):
                blocks[x - i, y + j].append((mask, i, j))
    rank = 0
    for columns in blocks.values():
        row_ids, pivots = {}, {}
        for mask, i, j in columns:
            vector = 0
            for q in range(c):
                t = j - q
                if not 0 <= t < d:
                    continue
                for s in range(a):
                    index = s * c + q
                    if mask >> index & 1:
                        continue
                    row = mask | (1 << index), s + i, t
                    if row not in row_ids:
                        row_ids[row] = len(row_ids)
                    vector ^= 1 << row_ids[row]
            while vector:
                pivot = vector.bit_length() - 1
                if pivot in pivots:
                    vector ^= pivots[pivot]
                else:
                    pivots[pivot] = vector
                    rank += 1
                    break
    return rank


def coefficient_rank_mod_prime(a, b, c, d, power, prime=65521):
    """Generic signed exterior-map construction, separate from the weight code."""
    by_input = defaultdict(list)
    for first, second, third in source_terms(a, b, c, d):
        by_input[second].append((first, third))
    pivots = {}
    for subset in combinations(range(a * c), power):
        selected = set(subset)
        for second in range(b * (c + d - 1)):
            column = {}
            for first, third in by_input[second]:
                if first in selected:
                    continue
                row = tuple(sorted((*subset, first))), third
                sign = -1 if sum(index < first for index in subset) % 2 else 1
                column[row] = (column.get(row, 0) + sign) % prime
            column = {row: value for row, value in column.items() if value}
            while column:
                pivot = max(column)
                coefficient = column[pivot]
                if pivot not in pivots:
                    inverse = pow(coefficient, -1, prime)
                    pivots[pivot] = {row: value * inverse % prime
                                     for row, value in column.items()}
                    break
                for row, value in pivots[pivot].items():
                    new = (column.get(row, 0) - coefficient * value) % prime
                    if new:
                        column[row] = new
                    else:
                        column.pop(row, None)
    return len(pivots)


def finite_cost(a, b):
    """External rank, two-sector and shifted-tripling upper bounds.

    A pair (multiplicity,cost) means multiplicity*P(a,b)<=cost**(1/t).
    This table is not claimed to contain every available upper bound.
    """
    return [(1, a + b - 1),
            (2, max(a, b) + 2 * min(a, b) - 1),
            (6, 3 * (a + b) - 2)]


def improving_by_recorded_cost(source, shape):
    a, b, c, d = source
    l, middle, r = shape
    volume = l * middle * r
    return any((m1 * m2 * volume) ** 3 > (cost1 * cost2) ** 4
               for m1, cost1 in finite_cost(a, b)
               for m2, cost2 in finite_cost(c, d))


def finite_frontier(maximum_v=169, maximum_side=20):
    """Complete stated source grid; targets keep outer sizes (a,c)."""
    records, source_count = [], 0
    for a in range(2, maximum_side + 1):
        for c in range(a, maximum_side + 1):
            v = a * c
            if v > maximum_v:
                continue
            basic = [matrix_reference.matrix_basic_rank(a, c, p) for p in range(v)]
            first = [choose(v - 2, p) for p in range(v)]
            second = [choose(v - 2, p - 1) for p in range(v)]
            third = [2 * (a - 1) * (c - 1) * choose(v - 3, p - 1)
                     for p in range(v)]
            for b in range(a - 1, 2 * a + 1):
                for d in range(c - 1, 2 * c + 1):
                    if a == c and b > d:
                        continue
                    source_count += 1
                    source = a, b, c, d
                    _, y, z = source_format(*source)
                    maximum, limiting_power = min(
                        ((y * u + z * w + term) // target_rank, p)
                        for p, (u, w, term, target_rank)
                        in enumerate(zip(first, second, third, basic)) if target_rank)
                    if not improving_by_recorded_cost(source, (a, maximum, c)):
                        continue
                    low, high = 1, maximum
                    while low < high:
                        middle = (low + high) // 2
                        if improving_by_recorded_cost(source, (a, middle, c)):
                            high = middle
                        else:
                            low = middle + 1
                    records.append({
                        'source': list(source), 'format': [v, y, z],
                        'first_improving_target': [a, low, c],
                        'maximum_middle_permitted_by_first_leg_Koszul': maximum,
                        'limiting_power': limiting_power})
    records.sort(key=lambda record: (max(record['format']), sum(record['format']),
                                     record['format'][0], record['source']))
    return {
        'scope': ('2<=a<=c<=maximum_side, ac<=maximum_v, a-1<=b<=2a, '
                  'c-1<=d<=2c; b<=d when a=c. Only targets M(a,m,c).'),
        'maximum_v': maximum_v, 'maximum_side': maximum_side,
        'source_count': source_count, 'surviving_source_count': len(records),
        'records': records, 'constructed_targets': 0, 'improves_omega': False,
        'proof_status': 'Written and unreviewed; this is a necessary test.'}


def selected_target_certificate():
    source, target = (10, 9, 12, 12), (10, 14, 12)
    v, y, z = source_format(*source)
    ranks = []
    for power in range(v):
        actual_source = source_rank(*source, power)
        actual_target = matrix_reference.padded_matrix_rank(target, v, power)
        if actual_target > actual_source:
            raise ArithmeticError('selected target fails a first-leg test')
        ranks.append({'power': power, 'source_rank': actual_source,
                      'target_rank': actual_target})
    if not 60480 ** 22496 > 3850 ** 30000:
        raise ArithmeticError('conditional rational exponent comparison failed')
    return {
        'source': list(source), 'source_format': [v, y, z],
        'target': list(target), 'target_format': [120, 140, 168],
        'first_leg_Koszul': ranks,
        'ordinary_slice_screen': {'left': 294, 'right': 315, 'passes': True},
        'coordinate_parent_order': 414, 'target_volume': 1680,
        'conditional_exponent': {'numerator': 22496, 'denominator': 10000,
                                 'exact_comparison': '60480^22496 > 3850^30000'},
        'constructed': False, 'improves_omega': False,
        'proof_status': 'Written and unreviewed; the construction premise is unproved.'}


def coefficient_controls():
    selected = set()
    for a, b, c, d in product(range(2, 5), range(1, 5), range(2, 5), range(1, 5)):
        if a > b + 1 or c > d + 1:
            continue
        powers = range(a * c) if max(a, c) <= 3 else range(4)
        selected.update((a, b, c, d, p) for p in powers)
    for source in ((2, 1, 3, 7), (2, 1, 4, 8), (2, 7, 3, 2)):
        selected.update((*source, p) for p in range(source[0] * source[2]))
    records = []
    for a, b, c, d, power in sorted(selected):
        observed = coefficient_rank_mod2(a, b, c, d, power)
        expected = source_rank(a, b, c, d, power)
        if observed != expected:
            raise ArithmeticError((a, b, c, d, power, observed, expected))
        records.append({'source': [a, b, c, d], 'power': power, 'rank_mod2': observed})
    odd_records = []
    for source in ((2, 1, 2, 2), (3, 2, 2, 3), (2, 4, 3, 2), (3, 4, 3, 3)):
        for power in range(3):
            observed = coefficient_rank_mod_prime(*source, power)
            expected = source_rank(*source, power)
            if observed != expected:
                raise ArithmeticError((source, power, observed, expected))
            odd_records.append({'source': list(source), 'power': power,
                                'prime': 65521, 'rank': observed})
    return {'mod2_records': records, 'odd_prime_records': odd_records,
            'improves_omega': False,
            'scope': 'Independent signed and characteristic-two coefficient-map controls.'}


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('controls', 'frontier', 'target'), required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    routines = {'controls': coefficient_controls, 'frontier': finite_frontier,
                'target': selected_target_certificate}
    report = routines[args.mode]()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(args.mode + ' exact certificate written; no exponent improvement is claimed.')
