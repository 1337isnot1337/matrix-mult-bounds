"""Separate-mask Newton pruning when only selected legs have two-weight lifts.

The unselected legs are conservatively left unpruned.  A selected target
matrix-unit lift may use any one or two source weights: both components
are source-torus limits and obey the same homogeneous slice-rank bound.
"""

import argparse
from collections import defaultdict
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location('independent_newton_replay', HERE / 'parity_balancing_newton_pruning_audit.py')
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)
OUTPUT = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_mixed_grading.json'


def run(terms, selected_legs, target_dimensions=(778, 778, 778), maximum_slice_rank=27):
    if len(target_dimensions) != 3 or any(type(d) is not int or not 0 < d <= 960 for d in target_dimensions):
        raise ValueError('Exactly three positive target dimensions at most 960 are required')
    if any(type(leg) is not int or leg not in range(3) for leg in selected_legs):
        raise ValueError('A selected leg must be 0, 1, or 2')
    if type(maximum_slice_rank) is not int or maximum_slice_rank < 0:
        raise ValueError('The maximum target slice rank must be a nonnegative integer')
    masks = [set(range(960)) for _ in range(3)]
    selected = set(selected_legs)
    rounds = []
    while all(len(masks[i]) >= target_dimensions[i] for i in range(3)):
        sizes = [len(mask) for mask in masks]
        bounds = [maximum_slice_rank + sum(sizes[j] - target_dimensions[j] for j in range(3) if j != i) for i in range(3)]
        ranks = [[0] * 960 for _ in range(3)]
        active = 0
        for point in terms:
            if all(point[i] in masks[i] for i in range(3)):
                active += 1
                for i in range(3):
                    ranks[i][point[i]] += 1
        updated = [set(mask) for mask in masks]
        removals = []
        for leg in sorted(selected):
            grouped = defaultdict(list)
            for column in masks[leg]:
                i, k, s = CORE.coordinates(column)
                grouped[i + s - k].append(column)
            keep = set()
            for weight, columns in grouped.items():
                good = [c for c in columns if ranks[leg][c] <= bounds[leg]]
                polygon = CORE.hull((CORE.coordinates(c)[0], CORE.coordinates(c)[2]) for c in good)
                keep.update(c for c in columns if CORE.in_hull((CORE.coordinates(c)[0], CORE.coordinates(c)[2]), polygon))
            updated[leg] = keep
        for leg in range(3):
            removals.append(sorted(masks[leg] - updated[leg]))
        rounds.append({'available_dimensions': sizes, 'slice_rank_upper_bounds': bounds,
                       'retained_dimensions': [len(mask) for mask in updated],
                       'restricted_source_terms': active,
                       'removed_common_columns_by_leg': removals,
                       'output_coordinate_sha256_by_leg': [CORE.digest(mask) for mask in updated]})
        if updated == masks:
            break
        masks = updated
    return {'selected_legs_with_at_most_two_weights_per_matrix_unit': sorted(selected),
            'unselected_legs_left_unpruned': sorted(set(range(3)) - selected),
            'target_dimensions': list(target_dimensions),
            'maximum_target_matrix_unit_slice_rank': maximum_slice_rank,
            'rounds': rounds, 'final_available_dimensions': [len(mask) for mask in masks],
            'excluded': any(len(masks[i]) < target_dimensions[i] for i in range(3)),
            'failure_to_exclude_is_not_a_construction': True}


def replay():
    terms = CORE.source()
    for x, y, z in terms:
        xi, xk, xs = CORE.coordinates(x)
        yi, yk, ys = CORE.coordinates(y)
        zi, zk, zs = CORE.coordinates(z)
        if (xi + ys - zk, xk - yi - zs, xs - yk + zi) != (0, 0, 0):
            raise ArithmeticError('The full three-parameter source torus failed')
    cases = [run(terms, selected) for selected in ((0,), (0, 1), (0, 1, 2))]
    row_count_cases = [run(terms, (0, 1), (count, count, 778)) for count in (760, 759)]
    if not row_count_cases[0]['excluded'] or row_count_cases[1]['excluded']:
        raise ArithmeticError('The exact 760/759 row-count controls changed')
    return {'format': 'separate-mask-mixed-grading-pruning-v2',
            'source_terms_checked': len(terms), 'cases': cases,
            'all_three_full_source_torus_parameters_checked': True,
            'selected_row_count_cases': row_count_cases,
            'at_least_two_legs_each_require_this_many_three_or_more_weight_images': 19,
            'restricted_target_injectivity_is_inherited_from_the_full_maps': True,
            'all_row_counts_and_masks_recomputed': True,
            'arbitrary_ungraded_restrictions_excluded': False,
            'arbitrary_degenerations_excluded': False,
            'new_exponent_established': False,
            'proof_review': 'Checked by another agent in this generating session; no external independent review or formalization.',
            'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    report = replay()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'output': str(args.output), 'cases': [
        {'selected': c['selected_legs_with_at_most_two_weights_per_matrix_unit'],
         'rounds': [[r['available_dimensions'], r['slice_rank_upper_bounds'], r['retained_dimensions']] for r in c['rounds']],
         'target_dimensions': c['target_dimensions'],
         'excluded': c['excluded']} for c in report['cases'] + report['selected_row_count_cases']]}, indent=2))


if __name__ == '__main__':
    main()
