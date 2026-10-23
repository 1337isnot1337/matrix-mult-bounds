"""Exact finite screens for ordinary restrictions from EPR(k) C(c,d).

The gcd and product-space obstructions apply to ordinary linear restrictions.
They do not exclude singular degenerations. See edge_ordinary.md.
"""
from functools import lru_cache
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path

_spec = spec_from_file_location('edge_ordinary_unequal_reference',
                               Path(__file__).with_name('unequal_paired.py'))
reference = module_from_spec(_spec)
_spec.loader.exec_module(reference)
choose = reference.choose


def ceil_div(a, b):
    return (a + b - 1) // b


@lru_cache(None)
def upper(k, c, d, power):
    return reference.source_rank_upper(k, 1, c, d, power)


@lru_cache(None)
def target_rank(l, middle, r, ambient, power):
    return reference.matrix_reference.padded_matrix_rank(
        (l, middle, r), ambient, power)


def improving(k, c, d, l, middle, r):
    volume = l * middle * r
    return any((multiplicity * volume) ** 3 > k ** 3 * cost ** 4
               for multiplicity, cost in reference.finite_cost(c, d))


def koszul_witness(k, c, d, l, middle, r):
    for other in (False, True):
        cc, dd, ll, mm = ((d, c, middle, l) if other else (c, d, l, middle))
        ambient, high, output = k * cc, cc + dd - 1, k * dd
        pivot = min(ambient - 1,
                    (output * ambient - high) // (high + output))
        for power in sorted(range(ambient), key=lambda p: (abs(p - pivot), p)):
            bound = upper(k, cc, dd, power)
            if min(ll * mm * choose(ambient, power),
                   mm * r * choose(ambient, power + 1)) <= bound:
                continue
            matrix_rank = target_rank(ll, mm, r, ambient, power)
            if matrix_rank > bound:
                return {'source_leg': 'third' if other else 'first',
                        'power': power, 'source_rank_upper_bound': bound,
                        'target_rank': matrix_rank,
                        'scope': 'arbitrary tensor degeneration'}
    return None


def factor_possibilities(k, c, d, l, middle, r):
    """Necessary common-factor parameter types for one input map.

    The source input consists of k binary forms of degree c-1, multiplied
    by forms of degree d-1. The rank limit is supplied by the two quotient
    codimensions. None means the pairwise image bound does not force a gcd.
    """
    high = c + d - 1
    rank_limit = middle + (high - l * middle) + (k * d - middle * r)
    if rank_limit >= 2 * d:
        return None
    degree = max(0, high - rank_limit)
    types = []
    if l * r <= k * (c - degree):
        types.append('fixed')
    if l * r <= c:
        types.append('full_bilinear')
    outer_low, outer_high = max(degree, l - 1), c - ceil_div(r, k)
    if outer_low <= outer_high:
        types.append('outer')
    shared_low = max(degree, r - 1)
    shared_high = min(c - ceil_div(l, k), high - l * middle)
    if shared_low <= shared_high:
        types.append('shared')
    return {'slice_rank_limit': rank_limit, 'gcd_degree_at_least': degree,
            'possible_parameter_types': types,
            'outer_degree_interval': [outer_low, outer_high],
            'shared_degree_interval': [shared_low, shared_high]}


def ordinary_witness(k, c, d, l, middle, r):
    high = c + d - 1
    if middle * (l + r - 1) > high + (k - 1) * d:
        return {'kind': 'minimum slice', 'source_leg': 'first',
                'left': middle * (l + r - 1),
                'right': high + (k - 1) * d, 'scope': 'ordinary restriction'}
    if l * (middle + r - 1) > high + (k - 1) * c:
        return {'kind': 'minimum slice', 'source_leg': 'third',
                'left': l * (middle + r - 1),
                'right': high + (k - 1) * c, 'scope': 'ordinary restriction'}
    first = factor_possibilities(k, c, d, l, middle, r)
    third = factor_possibilities(k, d, c, middle, l, r)
    result = {'first_input': first, 'third_input': third,
              'scope': 'ordinary restriction'}
    for leg, factors in [('first', first), ('third', third)]:
        if factors is not None and not factors['possible_parameter_types']:
            return dict(result, kind='gcd factor dimensions', source_leg=leg)
    if (first is not None and third is not None
            and set(first['possible_parameter_types']) <= {'outer', 'shared'}
            and set(third['possible_parameter_types']) <= {'outer', 'shared'}
            and 2 * l * middle > high and r > k):
        return dict(result, kind='factor product space',
                    target_high_dimension=l * middle,
                    high_projection_kernel_dimension=high - l * middle,
                    source_pairing_dimension=k, target_pairing_dimension=r)
    return None


def positive_controls():
    """Replay actual coefficient restrictions, independently of the screens.

    EPR(k) C((l-1)m+1,m) restricts to M(l,m,k) by retaining first
    polynomial indices i*m. All source coefficients are expanded and compared
    with the matrix tensor before testing that neither screen rejects it.
    """
    records = []
    for l, middle, k in product(range(2, 5), repeat=3):
        c, d = (l - 1) * middle + 1, middle
        first_map = {s * c + i * middle: i * k + s
                     for i in range(l) for s in range(k)}
        third_map = {s * d + j: j * k + s
                     for j in range(middle) for s in range(k)}
        observed = Counter()
        for x, y, z in reference.source_terms(k, 1, c, d):
            if x in first_map:
                observed[first_map[x], y, third_map[z]] += 1
        expected = Counter({(i * k + s, i * middle + j, j * k + s): 1
                            for i in range(l) for j in range(middle)
                            for s in range(k)})
        if observed != expected:
            raise ArithmeticError(('positive coefficient restriction',
                                   l, middle, k, observed, expected))
        witnesses = (koszul_witness(k, c, d, l, middle, k),
                     ordinary_witness(k, c, d, l, middle, k))
        if any(witness is not None for witness in witnesses):
            raise ArithmeticError(('false exclusion of actual restriction',
                                   l, middle, k, witnesses))
        records.append({'source': [k, 1, c, d],
                        'target': [l, middle, k],
                        'coefficient_count': len(expected),
                        'coefficient_identity_verified': True,
                        'all_screen_checks_pass': True})
    return {'field': 'all fields; integer coefficients',
            'fixture_count': len(records), 'records': records}


def finite_ordinary_frontier(maximum_dimension=100):
    records, survivors = [], []
    source_count = improving_target_count = 0
    witness_counts = {}
    for k in range(2, maximum_dimension // 2 + 1):
        for c in range(2, maximum_dimension // k + 1):
            last_d = min(maximum_dimension // k, maximum_dimension - c + 1)
            for d in range(c, last_d + 1):
                source_count += 1
                first, high, third = k * c, c + d - 1, k * d
                for l in range(1, min(first, high) + 1):
                    for r in range(1, min(first // l, third) + 1):
                        maximum_middle = min(high // l, third // r)
                        if not improving(k, c, d, l, maximum_middle, r):
                            continue
                        low, upper_middle = 1, maximum_middle
                        while low < upper_middle:
                            middle = (low + upper_middle) // 2
                            if improving(k, c, d, l, middle, r):
                                upper_middle = middle
                            else:
                                low = middle + 1
                        middle = low
                        count = maximum_middle - middle + 1
                        improving_target_count += count
                        record = {'source': [k, 1, c, d],
                                  'source_format': [first, high, third],
                                  'first_improving_target': [l, middle, r],
                                  'through_middle': maximum_middle,
                                  'covered_target_count': count}
                        witness = koszul_witness(k, c, d, l, middle, r)
                        if witness:
                            witness['kind'] = 'Koszul upper bound'
                        else:
                            witness = ordinary_witness(k, c, d, l, middle, r)
                        if witness:
                            record['witness'] = witness
                            key = witness['kind']
                            witness_counts[key] = witness_counts.get(key, 0) + count
                            records.append(record)
                        else:
                            survivors.append(record)
    return {
        'maximum_source_dimension': maximum_dimension,
        'scope': ('k,c,d>=2, c<=d, max(k*c,c+d-1,k*d)<=maximum; '
                  'all dimension-feasible positive matrix shapes; '
                  'improving means one of the three recorded profile costs.'),
        'source_count': source_count,
        'improving_target_count': improving_target_count,
        'excluded_target_counts_by_witness': witness_counts,
        'surviving_parameter_group_count': len(survivors),
        'survivors': survivors, 'exclusion_records': records,
        'overall_exclusion_scope': 'ordinary linear restriction only',
        'improves_omega': False,
        'proof_status': 'Written, exact finite replay, and unreviewed.'}


if __name__ == '__main__':
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('frontier', 'controls'),
                        default='frontier')
    parser.add_argument('--maximum-dimension', type=int, default=100)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = (positive_controls() if args.mode == 'controls'
              else finite_ordinary_frontier(args.maximum_dimension))
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('exclusion_records', 'survivors')}))
