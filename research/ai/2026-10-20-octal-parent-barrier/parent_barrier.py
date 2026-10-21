"""Exact orbit-hole obstruction for coordinate potentials on one F8 parent.

Standard library only. The integer DP is independently comparable with a
complete 9^7 enumeration. This is not an obstruction to general degenerations.
"""
from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path
import sys

GROUP_PATH = Path(__file__).resolve().parents[1] / '2026-10-20-group-potentials'
sys.path.insert(0, str(GROUP_PATH))
from octal_group import cubic_group, cubic_parent, fm  # noqa: E402

# Entries are (scalar, free coordinate); rows index these three lists.
SEED = [[(1, 1), (3, 3)], [(3, 6), (5, 7)],
        [(3, 0), (3, 3), (5, 0), (5, 1)]]
ROWS = [(0, 0, 1, 1, 0, 1), (0, 0, 1, 0, 1, 1),
        (1, 1, 0, 2, 3, 0), (1, 1, 0, 3, 2, 0)]


def transformed_seed(parent, lam, shifts, rotation):
    sets = [None] * 3
    for family, seed in enumerate(SEED):
        indices = [(fm(lam, a) - 1) * 8 +
                   fm(fm(lam, lam), x ^ fm(a, shifts[family]))
                   for a, x in seed]
        dest = (family + rotation) % 3
        sets[dest] = [parent[dest][i] for i in indices]
    rows = []
    for row in ROWS:
        step = 2 * rotation
        rows.append(row[-step:] + row[:-step] if step else row)
    return sets, rows


def verify_circuit(group, sets, rows):
    """Recompute both group support and positive zero dependence directly."""
    shape = list(map(len, sets))
    total = [0] * sum(shape)
    mul, inv = group['mul'], group['inv']
    for s, t, tt, u, uu, ss in rows:
        if (s, t, u) == (ss, tt, uu):
            raise ValueError('an intended term is not a strict inequality')
        x = mul[inv[sets[0][s]]][sets[1][t]]
        y = mul[inv[sets[1][tt]]][sets[2][u]]
        z = mul[inv[sets[2][uu]]][sets[0][ss]]
        if mul[mul[x][y]][z] != group['identity']:
            raise ValueError('invalid group support relation')
        for index, sign in ((s, 1), (ss, -1),
                            (shape[0] + tt, 1), (shape[0] + t, -1),
                            (shape[0] + shape[1] + uu, 1),
                            (shape[0] + shape[1] + u, -1)):
            total[index] += sign
    if not rows or any(total):
        raise ValueError('positive circuit does not sum to zero')
    return len(rows)


def verify_orbit():
    group = cubic_group()
    parent = cubic_parent(group)
    circuits = relations = 0
    for lam in range(1, 8):
        for shifts in product(range(8), repeat=3):
            for rotation in range(3):
                sets, rows = transformed_seed(parent, lam, shifts, rotation)
                relations += verify_circuit(group, sets, rows)
                circuits += 1
    # Verify exactly the translation incidence used in the written count.
    # Every hole meets one translate for a two-point piece, and two for a
    # four-point piece, whenever its scalar is in that piece's scalar support.
    incidences = []
    for family, seed in enumerate(SEED):
        scalars = sorted({a for a, _ in seed})
        counts = []
        for a in scalars:
            for hole in range(8):
                hits = sum(any(aa == a and (x ^ fm(a, shift)) == hole
                               for aa, x in seed) for shift in range(8))
                counts.append(hits)
        expected = 2 if family == 2 else 1
        if set(counts) != {expected}:
            raise ArithmeticError('translation-incidence mismatch')
        incidences.append(expected)
    powers = [1]
    for _ in range(6):
        powers.append(fm(powers[-1], 3))
    if len(set(powers)) != 7 or fm(powers[-1], 3) != 1 or fm(3, 3) != 5:
        raise ArithmeticError('invalid scalar cycle')
    return {'circuits_checked': circuits, 'support_relations_checked': relations,
            'positive_weights_per_circuit': [1] * 4,
            'seed_family_sizes': list(map(len, SEED)),
            'hole_translation_incidences': incidences, 'scalar_cycle': powers}


def edge_score(a, b, low=4, high=8):
    return int(a + b >= low) + 2 * int(a + b >= high)


def cycle_maxima(length=7, cap=8, low=4, high=8):
    """Max-plus DP. Fix the first value, then store (total,last)->maximum.

    Prefixes with equal state have the same future options; retaining only
    the greatest prefix score is exact. Include the closing cycle edge last.
    """
    if length < 2 or cap < 0 or not 0 <= low <= high:
        raise ValueError('invalid cycle parameters')
    maxima = [-1] * (length * cap + 1)
    witnesses = [None] * len(maxima)
    for first in range(cap + 1):
        states = {(first, first): (0, (first,))}
        for _ in range(length - 1):
            following = {}
            for (total, last), (score, values) in states.items():
                for value in range(cap + 1):
                    key = total + value, value
                    candidate = score + edge_score(last, value, low, high)
                    if key not in following or candidate > following[key][0]:
                        following[key] = candidate, values + (value,)
            states = following
        for (total, last), (score, values) in states.items():
            score += edge_score(last, first, low, high)
            if score > maxima[total]:
                maxima[total], witnesses[total] = score, list(values)
    for total, values in enumerate(witnesses):
        if sum(values) != total or sum(edge_score(values[i - 1], values[i], low, high)
                                       for i in range(length)) != maxima[total]:
            raise ArithmeticError('invalid maximizing witness')
    return maxima, witnesses


def exhaustive_maxima(length=7, cap=8, low=4, high=8):
    """Independent full enumeration, without state compression."""
    maxima = [-1] * (length * cap + 1)
    edge_table = [[int(a + b >= low) + 2 * int(a + b >= high)
                   for b in range(cap + 1)] for a in range(cap + 1)]
    count = 0
    for values in product(range(cap + 1), repeat=length):
        score = edge_table[values[-1]][values[0]]
        for i in range(1, length):
            score += edge_table[values[i - 1]][values[i]]
        total = sum(values)
        if score > maxima[total]:
            maxima[total] = score
        count += 1
    return maxima, count


def volume_bound(maxima):
    maximum = -1
    holes = None
    checked = 0
    for hs, ht, hu in product(range(57), repeat=3):
        checked += 1
        if maxima[hs] + maxima[ht] + maxima[hu] < 21:
            continue
        volume = (56 - hs) * (56 - ht) * (56 - hu)
        if volume > maximum:
            maximum, holes = volume, [hs, ht, hu]
    return {'triples_checked': checked, 'max_volume': maximum,
            'maximizing_hole_totals': holes,
            'scope': 'Necessary aggregate hole-score condition; attainability not asserted.'}


def gate_certificate(volume):
    # V^(3/4) < 5500 < 7+73*7^(9/4). All decisions are integers.
    if not volume ** 3 < 5500 ** 4:
        raise ValueError('target exceeds the selected rational separator')
    if not 76 ** 4 < 7 ** 9 or not 5500 < 7 + 73 * 76:
        raise ArithmeticError('source lower bound failed')
    return {'volume_cubed': volume ** 3, 'separator_fourth_power': 5500 ** 4,
            'source_root_lower': 76, 'source_root_lower_fourth_power': 76 ** 4,
            'source_root_radicand': 7 ** 9, 'source_cost_lower': 7 + 73 * 76,
            'separator': 5500, 'target_exponent': '3/4', 'source_exponent': '9/4'}


def report(exhaustive=False):
    orbit = verify_orbit()
    maxima, witnesses = cycle_maxima()
    if max(maxima[:12]) != 6:
        raise ArithmeticError('small-hole analytic bound mismatch')
    bound = volume_bound(maxima)
    result = {'claim': 'AI-GROUP-PARENT-ORBIT-007', 'group': 'F8^3:C7',
              'parent_shape': [56] * 3, 'orbit': orbit, 'max_scores': maxima,
              'maximizing_cycle_witnesses': witnesses, 'volume_bound': bound,
              'degree_sum_gate': gate_certificate(bound['max_volume']),
              'status': 'proof-written-unreviewed', 'improves_omega': False,
              'scope': 'Single targets from vertex subsets of this fixed parent, '
                       'with strict coordinate potentials and the usual source degree-sum gate.'}
    if exhaustive:
        other, count = exhaustive_maxima()
        if other != maxima:
            raise ArithmeticError('independent exhaustive table mismatch')
        result['independent_enumeration'] = {'vectors_checked': count,
                                              'all_57_maxima_match': True}
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exhaustive', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = report(args.exhaustive)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in
                     ['claim', 'orbit', 'volume_bound', 'degree_sum_gate', 'improves_omega']},
                     indent=2))
