"""Exact one-matrix-plus-scalars frontier; no target is constructed."""
import argparse
from fractions import Fraction as Q
from itertools import permutations
import json
from math import comb, isqrt, prod
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT/'research/ai/2026-10-21-semisimple-koszul'))
from semisimple_koszul import padded_basic_ranks, source_ranks
from rank_locus_obstruction import profile, screen
from fourier_certificate import power_interval
from cube_cover import joint_target_cube

DEGREES = [1, 2, 2, 3, 3, 4, 4, 5, 6]
N = 120
SLICE_BOUND = 98
CUBE_BOUND = 1012332
SCALE = 10**12


def joint_ranks(shape, scalars, ambient=N):
    a, b, c = shape
    return [c*rank+scalars*comb(ambient-1, p)
            for p, rank in enumerate(padded_basic_ranks(a, b, ambient))]


def target_profile(shape, scalars, rank_budget):
    a, b, c = shape
    return max(k*(a+b-k)+min(scalars, rank_budget-c*k)
               for k in range(min(a, b)+1) if c*k <= rank_budget)


def profile_checks(shape, scalars, source_profile):
    checks = []
    for ordered in sorted(set(permutations(shape))):
        a, b, c = ordered
        margins = [target_profile(ordered, scalars, t)
                   -(source_profile[t]['dimension']+a*b+scalars-N)
                   for t in range(N+1)]
        checks.append({'ordered_shape': ordered,
                       'rank_budgets_checked': N+1,
                       'minimum_dimension_margin': min(margins)})
    return checks


def conditional_gate(scalars, exponent):
    if scalars not in (11, 12, 13):
        raise ValueError('conditional gate covers scalar counts 11, 12 and 13')
    numerator, denominator = exponent.numerator, exponent.denominator
    source_upper = sum(power_interval(d, numerator, denominator, SCALE)[1]
                       for d in DEGREES)
    target_lower = power_interval(891, numerator, 3*denominator, SCALE)[0]+scalars
    if target_lower <= source_upper:
        raise ValueError('conditional exponent comparison is not strict')
    if not 9**81 > 6**94:
        raise ArithmeticError('exact logarithmic monotonicity comparison failed')
    return {'scalar_outputs': scalars, 'conditional_exponent_upper_bound': str(exponent),
            'source_cost_upper': str(source_upper), 'target_cost_lower': str(target_lower),
            'strict_margin_lower': str(target_lower-source_upper),
            'prerequisite': 'An exact degeneration to M(9,9,11) plus these scalar outputs; unconstructed.',
            'actual_improvement_established': False}


def frontier():
    source_r = source_ranks(DEGREES)
    source_p = profile(DEGREES)
    costs = [power_interval(d, 9, 4, SCALE) for d in DEGREES]
    source_lo = sum(pair[0] for pair in costs)
    source_hi = sum(pair[1] for pair in costs)
    shape_count, family_count = 0, 0
    survivors = []
    before_cube = []
    cube_exclusions = []
    caps = []
    for b in range(1, isqrt(N)+1):
        for c in range(b, N//b+1):
            for a in range(1, b+1):
                shape = (a, b, c)
                shape_count += 1
                family_count += N-b*c+1
                if screen(DEGREES, shape, source_p)['excluded']:
                    continue
                cap = min(N-b*c, SLICE_BOUND-a*b)
                witness = {'type': 'dimension or finite slice rank'}
                for ordered in sorted(set(permutations(shape))):
                    x, y, z = ordered
                    for p, rank in enumerate(padded_basic_ranks(x, y, N)):
                        bound = (source_r[p]-z*rank)//comb(N-1, p)
                        if bound < cap:
                            cap = bound
                            witness = {'type': 'Koszul', 'ordered_shape': ordered,
                                       'power': p, 'source_rank': source_r[p],
                                       'matrix_target_rank': z*rank,
                                       'per_scalar_rank': comb(N-1, p)}
                if cap < 0:
                    continue
                caps.append({'shape': shape, 'maximum_scalar_outputs': cap,
                             'active_cap_witness': witness})
                lower, upper = power_interval(prod(shape), 3, 4, SCALE)
                for r in range(cap+1):
                    if upper+r <= source_lo:
                        continue
                    if lower+r <= source_hi:
                        raise ArithmeticError('refine improvement-gate precision')
                    checks = profile_checks(shape, r, source_p)
                    if any(check['minimum_dimension_margin'] < 0 for check in checks):
                        continue
                    record = {'shape': shape, 'scalar_outputs': r,
                                      'leg_dimensions': [a*b+r, b*c+r, c*a+r],
                                      'finite_slice_rank': a*b+r,
                                      'strict_9_fourths_margin_lower': str(lower+r-source_hi),
                                      'maximum_scalar_outputs_from_Koszul': cap,
                                      'active_cap_witness': witness,
                                      'rank_profile_checks': checks,
                                      'status': 'passes the earlier necessary screens'}
                    before_cube.append(record)
                    target_cube = joint_target_cube(shape, r)
                    if target_cube > CUBE_BOUND:
                        cube_exclusions.append({'shape': shape, 'scalar_outputs': r,
                                                'target_cube_slice_rank': target_cube,
                                                'source_cube_slice_upper_bound': CUBE_BOUND,
                                                'strict_gap': target_cube-CUBE_BOUND})
                    else:
                        survivors.append(record)
    bounds = {11: Q(1121, 500), 12: Q(2233, 1000), 13: Q(2223, 1000)}
    return {'source_degrees': DEGREES, 'source_dimension': N,
            'finite_characteristic_two_slice_bound': SLICE_BOUND,
            'source_cost_at_9_fourths': [str(source_lo), str(source_hi)],
            'sorted_shapes_checked': shape_count, 'dimension_compatible_family_members': family_count,
            'scalar_caps': caps, 'improving_survivors_before_cube': before_cube,
            'cube_exclusions': cube_exclusions, 'improving_survivors': survivors,
            'source_cube_slice_upper_bound': CUBE_BOUND,
            'conditional_gates': [conditional_gate(r, bound) for r, bound in bounds.items()],
            'scope': 'Complete one-copy family M(a,b,c) plus scalar outputs, including sides one, '
                     'under the stated good-reduction hypothesis; general target sums remain open.',
            'all_targets_constructed': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = frontier()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'scalar_caps'}, indent=2))
