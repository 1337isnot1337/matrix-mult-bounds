"""Separate exact replay of iterative homogeneous-slice Newton pruning.

This audit independently builds all source terms, checks every coordinate
slice is a partial permutation, and uses a monotone-chain convex hull.
It does not import the primary pruning implementation.
"""

import argparse
from collections import defaultdict
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_newton_pruning_audit.json'


def index(i, k, s):
    return (15 * i + k) * 8 + s


def coordinates(column):
    i, rem = divmod(column, 120)
    k, s = divmod(rem, 8)
    return i, k, s


def source():
    terms = []
    row_seen = [[0] * 960 for _ in range(3)]
    column_seen = [[0] * 960 for _ in range(3)]
    for i, p, r, j, q, s in product(range(8), repeat=6):
        triple = (index(i, p + q, s), index(p, r + s, j), index(r, i + j, q))
        if sum(coordinates(c)[0] + coordinates(c)[2] - coordinates(c)[1] for c in triple):
            raise ArithmeticError('The original source grading failed')
        terms.append(triple)
        for leg in range(3):
            c, row, column = triple[leg], triple[(leg + 1) % 3], triple[(leg + 2) % 3]
            row_bit, column_bit = 1 << row, 1 << column
            if row_seen[leg][c] & row_bit or column_seen[leg][c] & column_bit:
                raise ArithmeticError('A coordinate slice is not a partial permutation')
            row_seen[leg][c] |= row_bit
            column_seen[leg][c] |= column_bit
    return terms


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) < 2:
        return points
    lower, upper = [], []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def in_hull(point, vertices):
    if not vertices:
        return False
    if len(vertices) == 1:
        return point == vertices[0]
    if len(vertices) == 2:
        a, b = vertices
        return cross(a, b, point) == 0 and all(min(a[t], b[t]) <= point[t] <= max(a[t], b[t]) for t in range(2))
    return all(cross(vertices[j], vertices[(j + 1) % len(vertices)], point) >= 0 for j in range(len(vertices)))


def digest(columns):
    return hashlib.sha256(json.dumps(sorted(columns), separators=(',', ':')).encode()).hexdigest()


def replay(target_dimension=778, maximum_matrix_unit_slice_rank=27):
    terms = source()
    available = set(range(960))
    rounds = []
    while len(available) >= target_dimension:
        before = len(available)
        bound = maximum_matrix_unit_slice_rank + 2 * (before - target_dimension)
        ranks = [[0] * 960 for _ in range(3)]
        active_terms = 0
        for triple in terms:
            if all(c in available for c in triple):
                active_terms += 1
                for leg in range(3):
                    ranks[leg][triple[leg]] += 1
        if ranks[0] != ranks[1] or ranks[0] != ranks[2]:
            raise ArithmeticError('The three actual coordinate-slice rank arrays differ')
        by_weight = defaultdict(list)
        for c in sorted(available):
            i, k, s = coordinates(c)
            by_weight[i + s - k].append(c)
        retained = set()
        weight_reports = []
        for weight, columns in sorted(by_weight.items()):
            good = [c for c in columns if ranks[0][c] <= bound]
            vertices = hull((coordinates(c)[0], coordinates(c)[2]) for c in good)
            kept = [c for c in columns if in_hull((coordinates(c)[0], coordinates(c)[2]), vertices)]
            retained.update(kept)
            weight_reports.append({'weight': weight, 'before': len(columns),
                                   'good_coordinate_slices': len(good),
                                   'good_point_hull': vertices, 'after': len(kept),
                                   'removed_common_columns': sorted(set(columns) - set(kept))})
        rounds.append({'available_dimension': before,
                       'matrix_unit_lift_rank_upper_bound': bound,
                       'retained_dimension': len(retained),
                       'restricted_source_nonzero_terms': active_terms,
                       'three_coordinate_rank_arrays_equal': True,
                       'input_coordinate_sha256': digest(available),
                       'output_coordinate_sha256': digest(retained),
                       'weight_blocks': weight_reports})
        if retained == available:
            break
        available = retained
    return {'format': 'independent-iterative-newton-pruning-replay-v1',
            'source': 'A(8,8)', 'source_dimension': 960,
            'source_nonzero_terms_enumerated': len(terms),
            'all_three_legs_all_coordinate_slices_partial_permutations': True,
            'target_dimension_per_leg': target_dimension,
            'maximum_matrix_unit_target_slice_rank': maximum_matrix_unit_slice_rank,
            'rank_upper_bound_formula': 'r_max + 2*(available_dimension-target_dimension)',
            'rounds': rounds, 'final_allowed_dimension': len(available),
            'ordinary_homogeneous_matrix_unit_restriction_excluded': len(available) < target_dimension,
            'arbitrary_ungraded_restrictions_excluded': False,
            'arbitrary_degenerations_excluded': False,
            'new_exponent_established': False,
            'review_scope': 'Separate implementation by a second agent in the generating session; no external independent review or formalization.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = replay()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'output': str(args.output),
                      'rounds': [[r['available_dimension'], r['matrix_unit_lift_rank_upper_bound'], r['retained_dimension']] for r in result['rounds']],
                      'final_allowed_dimension': result['final_allowed_dimension'],
                      'excluded': result['ordinary_homogeneous_matrix_unit_restriction_excluded']}, indent=2))


if __name__ == '__main__':
    main()
