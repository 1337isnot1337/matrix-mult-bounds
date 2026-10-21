"""Exact four-point matching cuts from a central C2^2 slice bound."""
import argparse
from itertools import combinations, permutations
import json
from pathlib import Path
import random


def multiply(left, right):
    value = 0
    for a in range(4):
        for b in range(4):
            if left >> a & 1 and right >> b & 1:
                value ^= 1 << (a ^ b)
    return value


def slice_control():
    basis = [1, 3, 5, 15]  # 1, x-1, y-1, (x-1)(y-1), in F2[C2^2].
    for a in basis[1:]:
        for b in basis[1:]:
            for c in basis[1:]:
                if multiply(multiply(a, b), c):
                    raise ArithmeticError('the augmentation ideal does not have zero cube')
    checked = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                coefficient = multiply(multiply(basis[i], basis[j]), basis[k]) & 1
                if i and j and k and coefficient:
                    raise ArithmeticError('a tensor term escapes the three slices')
                checked += 1
    return {'field': 'F2', 'basis': basis, 'zero_cube_products': 27,
            'transformed_tensor_coefficients': checked, 'slice_rank_upper': 3}


def matched_color_control():
    """All normalized matched color bijections in the two groups of order4."""
    counts = {}
    for cyclic in (False, True):
        checked = accepted = 0
        for left in permutations((1, 2, 3)):
            for right in permutations((1, 2, 3)):
                T, U = (0,)+left, (0,)+right
                differences = [(u-t) % 4 if cyclic else u ^ t for t, u in zip(T, U)]
                checked += 1
                accepted += len(set(differences)) == 4
        counts['C4' if cyclic else 'C2^2'] = {'checked': checked, 'matched_bijections': accepted}
    if counts != {'C2^2': {'checked': 36, 'matched_bijections': 12},
                  'C4': {'checked': 36, 'matched_bijections': 0}}:
        raise ArithmeticError('incorrect normalized central matching control')
    return counts


def find_match(Q, sets):
    S, T, U = map(set, sets)
    M, inv = Q['mul'], Q['inv']
    for r in range(len(M)):
        common = sorted(s for s in S if M[s][r] in T)
        if len(common) < 4:
            continue
        # For arbitrary candidates, try each anchored four-subset. The local
        # caller already has pair capacity four, so common has exactly four.
        for points in combinations(common, 4):
            first = points[0]
            for u in sorted(U):
                t = M[inv[first]][u]
                if all(M[s][t] in U for s in points):
                    return {'type': 'exact-central-slice', 'points': list(points),
                            'right_shifts': [r, t],
                            'blocked_points': sorted([(0, s) for s in points]
                                +[(1, M[s][r]) for s in points]+[(2, M[s][t]) for s in points])}
    return None


def verify_match(Q, item):
    points, (r, t) = item['points'], item['right_shifts']
    n = len(Q['mul'])
    if len(points) != 4 or len(set(points)) != 4 or any(not 0 <= q < n for q in points+[r, t]):
        raise ValueError('four distinct projected points and valid shifts required')
    expected = sorted([(0, q) for q in points]+[(1, Q['mul'][q][r]) for q in points]
                      +[(2, Q['mul'][q][t]) for q in points])
    if expected != [tuple(p) for p in item['blocked_points']]:
        raise ValueError('incorrect conditional matching support')
    return True


def commuting_violations(G, sets):
    classes = [{min(G['mul'][g][G['inv'][h]], G['inv'][G['mul'][g][G['inv'][h]]])
                for g, h in combinations(S, 2)} for S in sets]
    count = 0
    for f, h, k in permutations(range(3)):
        for a in classes[h]:
            for b in classes[k]:
                for x in {a, G['inv'][a]}:
                    for y in {b, G['inv'][b]}:
                        z = G['mul'][x][y]
                        if z == G['mul'][y][x] and min(z, G['inv'][z]) in classes[f]:
                            count += 1
    return count


def control():
    from four_colors import data
    from group_exact import pair_map, extra_relations, verify_farkas
    from search import potential_or_circuit
    G, Q, _ = data()
    rng = random.Random(2026102132)
    for tried in range(1, 10001):
        points = [0]+sorted(rng.sample(range(1, 120), 3))
        if len({Q['pairs'][min(a,b), max(a,b)][0] for a, b in combinations(points, 2)}) != 6:
            continue
        times_omega = [0, 2, 3, 1]
        sets = [[4*q for q in points], [4*q+i for i, q in enumerate(points)],
                [4*q+times_omega[i] for i, q in enumerate(points)]]
        for f in range(3):
            pair_map(G, sets[f], sets[(f+1) % 3])
        if commuting_violations(G, sets):
            continue
        relations, _ = extra_relations(G, sets)
        answer = potential_or_circuit(relations, 12)
        if 'potentials' in answer or not verify_farkas(relations, answer['indices'], answer['weights']):
            raise ArithmeticError('central-slice control contradicts the exact potential test')
        support = set()
        for i in answer['indices']:
            s, t, tt, u, uu, ss = relations[i]['vertices']
            support.update(((0, sets[0][s]), (0, sets[0][ss]), (1, sets[1][t]),
                            (1, sets[1][tt]), (2, sets[2][u]), (2, sets[2][uu])))
        return {'slice_control': slice_control(), 'candidates_tested': tried,
                'projected_points': points, 'pair_injective': True, 'commuting_trade_violations': 0,
                'matching': find_match(Q, [points]*3),
                'farkas': {'type': 'exact-farkas', 'sets': sets, 'relation_vertices':
                    [relations[i]['vertices'] for i in answer['indices']], 'weights': answer['weights'],
                    'blocked_lift_points': sorted(support)}, 'exponent_improvement': False}
    raise RuntimeError('the bounded control search found no suitable projection')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = control()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'farkas'}))
