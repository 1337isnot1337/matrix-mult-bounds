"""Necessary exact C2-color equations above the projected involutions.

These equations ignore all four-color inverse classes. Consistency is only
a necessary condition, while a contradictory circuit is an exact rejection.
"""
from collections import Counter
from itertools import combinations
import sys

from source_data import SEVEN
sys.path.insert(0, str(SEVEN))
from central_lift import eliminate


def pair_classes(G, Q):
    narrow = {c for c, lifts in Q['inverse_class_lifts'].items() if len(lifts) == 2}
    # Verify that the two classes are distinguished by the direct C2 bit.
    for c in narrow:
        colors = {}
        for g, image in enumerate(Q['projection']):
            if min(image, Q['inverse'][image]) == c:
                colors.setdefault(g & 1, set()).add(min(g, G['inv'][g]))
        if (set(colors) != {0, 1} or any(len(v) != 1 for v in colors.values())
                or colors[0] == colors[1]):
            raise ArithmeticError('narrow inverse classes are not C2 colors')
    pairs = {}
    for p, q in combinations(range(len(Q['representatives'])), 2):
        g = G['mul'][Q['representatives'][p]][G['inv'][Q['representatives'][q]]]
        image = Q['projection'][g]
        c = min(image, Q['inverse'][image])
        if c in narrow:
            pairs[p, q] = c
    return pairs


def necessary_system(pairs, sets):
    if len(sets) != 3 or any(not row or len(set(row)) != len(row) or
            any(type(p) is not int or not 0 <= p < 60 for p in row) for row in sets):
        raise ValueError('three nonempty sets of distinct projected points required')
    variables, lookup, rows = [], {}, []

    def variable(label):
        if label not in lookup:
            lookup[label] = len(variables)
            variables.append(label)
        return lookup[label]

    def add(labels, rhs, support):
        mask = 0
        for label in labels:
            mask ^= 1 << variable(label)
        rows.append({'mask': mask, 'rhs': rhs, 'support': sorted(set(support))})

    used = {}
    for f, points in enumerate(sets):
        for p, q in combinations(sorted(points), 2):
            if (p, q) in pairs:
                used.setdefault(pairs[p, q], {}).setdefault(f, []).append((p, q))
    for c, users in sorted(used.items()):
        if len(users) == 3:
            return {'capacity_core': [(f, p) for f in range(3) for p in users[f][0]]}
        if len(users) != 2:
            continue
        first, second = sorted(users)
        witnesses = {f: [(f, p) for p in users[f][0]] for f in users}
        add([('owner', first, c), ('owner', second, c)], 1,
            witnesses[first]+witnesses[second])
        for f, other in ((first, second), (second, first)):
            for p, q in users[f]:
                add([('bit', f, p), ('bit', f, q), ('owner', f, c)], 0,
                    [(f, p), (f, q)]+witnesses[other])
    return {'variables': variables, 'rows': rows}


def reject(pairs, sets):
    system = necessary_system(pairs, sets)
    if 'capacity_core' in system:
        return {'type': 'exact-capacity', 'sets': sets,
                'blocked_points': sorted(system['capacity_core'])}
    answer = eliminate(system)
    if answer['consistent']:
        return None
    rows = [system['rows'][i] for i in answer['circuit']]
    return {'type': 'exact-parity', 'sets': sets, 'variables': system['variables'],
            'rows': rows, 'blocked_points': sorted({p for row in rows for p in row['support']})}


def verify_rejection(pairs, record):
    system = necessary_system(pairs, record['sets'])
    if record['type'] == 'exact-capacity':
        if ('capacity_core' not in system or
                sorted(system['capacity_core']) != list(map(tuple, record['blocked_points']))):
            raise ValueError('wrong inverse-class capacity support')
        return True
    if 'capacity_core' in system:
        raise ValueError('wrong rejection type')
    return verify_parity_record(system, record)


def verify_parity_record(system, record):
    if record['type'] != 'exact-parity':
        raise ValueError('wrong rejection type')
    if [tuple(v) for v in record['variables']] != system['variables']:
        raise ValueError('wrong variable order')
    key = lambda r: (r['mask'], r['rhs'], tuple(map(tuple, r['support'])))
    expected, actual = Counter(map(key, system['rows'])), Counter(map(key, record['rows']))
    if not actual or any(n > expected[k] for k, n in actual.items()):
        raise ValueError('row not induced by these projected points')
    mask, rhs = 0, 0
    for row in record['rows']:
        mask ^= row['mask']
        rhs ^= row['rhs']
    points = sorted({tuple(p) for row in record['rows'] for p in row['support']})
    if mask or rhs != 1 or points != list(map(tuple, record['blocked_points'])):
        raise ValueError('not a contradictory circuit with the stated support')
    return True
