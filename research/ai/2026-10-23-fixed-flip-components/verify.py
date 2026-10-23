"""Exact component and fixed-direction certificates for two split seeds.

Finite standard flips cannot connect the displayed blocks. Fifty fixed
third-factor directions already fail the nine-group necessary grid test.
"""
from collections import Counter
from itertools import combinations
from math import comb, gcd
from pathlib import Path
import argparse
import importlib.util
import json

PACKAGE = Path(__file__).resolve().parent
WEIGHTED = PACKAGE.parent / '2026-10-23-grid-escape'
SPEC = importlib.util.spec_from_file_location('fixed_component_weighted', WEIGHTED / 'verify.py')
W = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(W)
SCENARIOS = {
    'four': {
        'replacements': ((0, 18, -1), (17, 8, 1), (48, 2, -1), (56, 22, -1)),
        'component_sizes': {1: 36, 2: 15, 3: 2, 4: 1},
        'weights': (2,4,2,3,4,4,4,4,2,4,4,4,4,4,4,4,4,4,4,4,
                    4,3,4,4,3,2,0,4,0,0,4,4,4,4,1,3,1,1,0,2,
                    4,2,2,4,4,4,2,2,1,2),
        'cap': 16, 'total': 148, 'independent_four_subsets': 229716,
    },
    'five': {
        'replacements': ((16, 57, 1), (47, 52, -1), (31, 48, -1),
                         (26, 32, 1), (54, 60, -1)),
        'component_sizes': {1: 36, 2: 15, 5: 2},
        'weights': (2,1,1,2,2,2,2,2,1,2,2,1,1,2,2,2,2,1,2,2,
                    2,1,2,2,2,2,2,1,0,2,1,0,2,2,1,2,1,1,1,2,
                    1,1,1,1,2,0,2,1,1,1),
        'cap': 8, 'total': 74, 'independent_four_subsets': 229803,
    },
}


def canonical(row):
    content = gcd(*row)
    if not content:
        raise ArithmeticError('Every displayed term factor must be nonzero.')
    if next(x for x in row if x) < 0:
        content = -content
    return tuple(x // content for x in row)


def seed(name):
    original = W.load_factors()
    factors = [[row[:] for row in original[key]] for key in ('u', 'v', 'w')]
    for i, j, scalar in SCENARIOS[name]['replacements']:
        factors[0][i] = [scalar * x for x in original['u'][j]]
    return factors


def sharing_components(factors):
    parent = list(range(76))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for leg in factors:
        seen = {}
        for i, row in enumerate(leg):
            point = canonical(row)
            if point in seen:
                parent[root(i)] = root(seen[point])
            seen[point] = i
    components = {}
    for i in range(76):
        components.setdefault(root(i), []).append(i)
    return sorted(components.values(), key=lambda group: group[0])


def independent_rows(rows):
    chosen = []
    for row in rows:
        if W.rank(chosen + [row]) > len(chosen):
            chosen.append(row)
    return chosen


def certify_disjoint_spans(bases):
    """Certify pairwise trivial intersections, separately on all three legs."""
    checks = 0
    for leg in bases:
        for left, right in combinations(leg, 2):
            if W.rank(left + right, 101) != len(left) + len(right):
                raise ArithmeticError('Different component leg spans are not certified disjoint.')
            checks += 1
    return checks


def analyze_components(factors):
    components = sharing_components(factors)
    bases = [[independent_rows([leg[i] for i in group]) for group in components]
             for leg in factors]
    checks = certify_disjoint_spans(bases)
    # Both sides of the V-flattening have independent component columns.
    # Its rank is the number of displayed terms, hence no term can become zero.
    for group in components:
        products = [[u * w for u in factors[0][i] for w in factors[2][i]] for i in group]
        if (W.rank([factors[1][i] for i in group], 101) != len(group)
                or W.rank(products, 101) != len(group)):
            raise ArithmeticError('A component V-flattening lacks the full term-count rank.')
    fixed = [group for i, group in enumerate(components) if len(bases[2][i]) == 1]
    vectors = [canonical(factors[2][group[0]]) for group in fixed]
    if len(set(vectors)) != len(vectors):
        raise ArithmeticError('The fixed component directions must be distinct.')
    if W.rank(vectors, 101) != 20:
        raise ArithmeticError('The fixed third-factor span should have dimension twenty.')
    return components, bases, fixed, vectors, checks


def check_flat_report(report, vectors, scenario):
    if (report['prime'], report['vectors'], report['dimension'], report['four_subsets']) != (
            101, 50, 20, comb(50, 4)):
        raise ArithmeticError('Unexpected fixed-direction enumeration parameters.')
    if report['independent_four_subsets'] != scenario['independent_four_subsets']:
        raise ArithmeticError('The independent-subset count changed.')
    weights, cap = scenario['weights'], scenario['cap']
    if len(weights) != 50 or min(weights) < 0 or sum(weights) != scenario['total']:
        raise ArithmeticError('Invalid fixed-direction integer weights.')
    histogram = {int(k): v for k, v in report['flat_weight_histogram'].items()}
    if (not histogram or min(histogram) < 0 or max(histogram) != cap
            or any(type(n) is not int or n <= 0 for n in histogram.values())
            or sum(histogram.values()) != report['independent_four_subsets']
            or report['maximum_flat_weight'] != cap):
        raise ArithmeticError('The fixed-direction weight counters disagree.')
    ids = report['weighted_witness_basis']
    if len(ids) != 4 or len(set(ids)) != 4 or any(type(i) is not int or not 0 <= i < 50 for i in ids):
        raise ArithmeticError('Invalid fixed-direction equality basis.')
    basis = [vectors[i] for i in ids]
    if W.rank(basis, 101) != 4 or W.rank(basis) != 4:
        raise ArithmeticError('The equality basis must have rank four.')
    members = [i for i, row in enumerate(vectors) if W.rank(basis + [row], 101) == 4]
    if (members != report['weighted_witness_members'] or sum(weights[i] for i in members) != cap
            or W.rank([vectors[i] for i in members]) != 4):
        raise ArithmeticError('The rational equality witness changed.')


def verify(full=False):
    results = {}
    for name, scenario in SCENARIOS.items():
        factors = seed(name)
        components, bases, fixed, vectors, checks = analyze_components(factors)
        if dict(Counter(map(len, components))) != scenario['component_sizes'] or len(fixed) != 50:
            raise ArithmeticError('Unexpected component partition or fixed-direction count.')
        report = json.loads((PACKAGE / (name + '_enumeration.json')).read_text())
        check_flat_report(report, vectors, scenario)
        if full:
            actual = W.enumerate_flats(vectors, scenario['weights'])
            check_flat_report(actual, vectors, scenario)
            if actual != report:
                raise ArithmeticError('The complete fixed-direction enumeration changed.')
        results[name] = {
            'replacements': [list(replacement) for replacement in scenario['replacements']],
            'components': components,
            'component_leg_dimensions': [[len(leg[i]) for leg in bases] for i in range(len(components))],
            'cross_component_disjointness_checks': checks,
            'component_V_flattening_rank_equals_term_count': True,
            'fixed_W_representatives': [group[0] for group in fixed],
            'fixed_W_weights': list(scenario['weights']),
            'fixed_W_total_weight': scenario['total'],
            'rank_four_flat_weight_cap': scenario['cap'],
            'nine_group_capacity': 9 * scenario['cap'],
            'minimum_rank_four_groups_by_weight': (scenario['total'] + scenario['cap'] - 1) // scenario['cap'],
            'all_finite_standard_flips_termwise_grid_excluded': scenario['total'] > 9 * scenario['cap'],
            'stored_four_subsets': report['four_subsets'],
            'exhaustive_enumeration_rerun_by_this_command': full,
        }
    return {'claim_id': 'AI-EXTERNAL-FIXED-FLIP-GRID-004',
            'source_sha256': W.SOURCE_HASH, 'scenarios': results,
            'scope': {
                'field': 'any characteristic-zero extension of the rational numbers',
                'moves': 'finite shared-factor standard flips, factor gauges whose three scalars have product one, and permutations',
                'grid_alignment': 'the 25-dimensional target leg maps to the first source leg; W is on a long leg',
                'application': 'termwise assignment of the full generic family to the 9-by-9 evaluation grid',
            },
            'arbitrary_algorithms_excluded': False, 'general_Q64_maps_excluded': False,
            'further_stabilizer_degenerations_excluded': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enumerate', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(verify(args.enumerate), indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
