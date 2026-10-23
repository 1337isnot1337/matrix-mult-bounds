"""Exact nine-group cover of the six-split seed's 47 permanent W directions.

This is a necessary-condition checkpoint, not a cover of all factors or
a construction of maps from Q(6,4).
"""
from collections import Counter
from math import comb
from pathlib import Path
import argparse
import importlib.util
import json


PACKAGE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    'six_split_component_geometry', PACKAGE.parent / '2026-10-23-fixed-flip-components/verify.py')
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
CLAIM = 'AI-EXTERNAL-SIX-SPLIT-FIXED-COVER-007'
REPLACEMENTS = ((0, 18, -1), (17, 8, 1), (48, 2, -1), (56, 22, -1),
                (43, 59, -1), (47, 73, 1))
WEIGHTS = (4, 2, 1, 4, 2, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4,
           4, 4, 4, 4, 4, 3, 4, 4, 3, 2, 0, 4, 0, 0, 4, 4,
           4, 0, 3, 3, 4, 2, 2, 4, 4, 4, 4, 2, 2, 1, 2)


def seed():
    original = C.W.load_factors()
    factors = [[row[:] for row in original[key]] for key in ('u', 'v', 'w')]
    for i, j, scalar in REPLACEMENTS:
        factors[0][i] = [scalar * x for x in original['u'][j]]
    return factors


def geometry():
    components, bases, fixed, vectors, checks = C.analyze_components(seed())
    if (dict(Counter(map(len, components))) != {1: 35, 2: 13, 3: 2, 4: 1, 5: 1}
            or checks != 3978 or len(fixed) != 47):
        raise ArithmeticError('The six-split component geometry changed.')
    return components, bases, fixed, vectors, checks


def check_cover(cover, fixed, vectors):
    if (cover['schema'] != 'six-split-fixed-cover-v1' or cover['claim_id'] != CLAIM
            or cover['source_sha256'] != C.W.SOURCE_HASH
            or cover['replacements'] != [list(row) for row in REPLACEMENTS]
            or cover['fixed_W_representatives'] != [group[0] for group in fixed]
            or cover['weights'] != list(WEIGHTS)):
        raise ArithmeticError('The cover data differ from the pinned six-split configuration.')
    groups = cover['groups']
    if len(groups) != 9:
        raise ArithmeticError('The witness must contain exactly nine groups.')
    ranks = []
    covered = set()
    for group in groups:
        if (not group or len(set(group)) != len(group)
                or any(type(i) is not int or not 0 <= i < 47 for i in group)):
            raise ArithmeticError('Invalid fixed-direction group indices.')
        rank = C.W.rank([vectors[i] for i in group])
        if rank != 4 or sum(WEIGHTS[i] for i in group) != 16:
            raise ArithmeticError('Each retained group must have rational rank four and weight sixteen.')
        ranks.append(rank)
        covered.update(group)
    if covered != set(range(47)):
        raise ArithmeticError('The nine groups do not cover all 47 fixed directions.')
    return ranks


def check_enumeration(report, vectors):
    if (report['prime'], report['vectors'], report['dimension'], report['four_subsets'],
            report['independent_four_subsets']) != (101, 47, 20, comb(47, 4), 177997):
        raise ArithmeticError('Unexpected enumeration parameters or coverage.')
    if len(WEIGHTS) != 47 or min(WEIGHTS) < 0 or sum(WEIGHTS) != 144:
        raise ArithmeticError('Invalid nonnegative integer weights.')
    histogram = {int(k): value for k, value in report['flat_weight_histogram'].items()}
    if (not histogram or min(histogram) < 0 or max(histogram) != 16
            or any(type(count) is not int or count <= 0 for count in histogram.values())
            or sum(histogram.values()) != 177997 or report['maximum_flat_weight'] != 16):
        raise ArithmeticError('The exact weight-cap counters disagree.')
    ids = report['weighted_witness_basis']
    if (len(ids) != 4 or len(set(ids)) != 4
            or any(type(i) is not int or not 0 <= i < 47 for i in ids)):
        raise ArithmeticError('Invalid equality-witness basis.')
    basis = [vectors[i] for i in ids]
    if C.W.rank(basis) != 4 or C.W.rank(basis, 101) != 4:
        raise ArithmeticError('The equality basis must have rank four.')
    members = [i for i, row in enumerate(vectors) if C.W.rank(basis + [row], 101) == 4]
    if (members != report['weighted_witness_members']
            or sum(WEIGHTS[i] for i in members) != 16
            or C.W.rank([vectors[i] for i in members]) != 4):
        raise ArithmeticError('The rational equality witness differs.')


def verify(full=False):
    components, bases, fixed, vectors, checks = geometry()
    cover = json.loads((PACKAGE / 'cover.json').read_text())
    report = json.loads((PACKAGE / 'enumeration.json').read_text())
    ranks = check_cover(cover, fixed, vectors)
    check_enumeration(report, vectors)
    if full:
        actual = C.W.enumerate_flats(vectors, WEIGHTS)
        check_enumeration(actual, vectors)
        if actual != report:
            raise ArithmeticError('The complete enumeration differs from the retained run.')
    return {
        'claim_id': CLAIM,
        'source_sha256': C.W.SOURCE_HASH,
        'replacements': [list(row) for row in REPLACEMENTS],
        'components': components,
        'component_leg_dimensions': [[len(leg[i]) for leg in bases] for i in range(len(components))],
        'cross_component_disjointness_checks': checks,
        'component_V_flattening_rank_equals_term_count': True,
        'fixed_W_representatives': [group[0] for group in fixed],
        'fixed_W_directions_permanent_under_finite_standard_flips': True,
        'fixed_W_total_weight': sum(WEIGHTS),
        'rank_four_flat_weight_cap': 16,
        'minimum_groups_from_weight': 9,
        'groups': cover['groups'],
        'group_rational_ranks': ranks,
        'all_47_fixed_directions_covered': True,
        'exact_minimum_rank_at_most_four_groups': 9,
        'stored_four_subsets': report['four_subsets'],
        'exhaustive_enumeration_rerun_by_this_command': full,
        'field': 'any characteristic-zero extension of the rational numbers',
        'full_factor_cover_constructed': False,
        'Q64_grid_constructed': False,
        'new_matrix_multiplication_algorithm': False,
        'improves_omega': False,
        'proof_status': 'written-unreviewed',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enumerate', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(verify(args.enumerate), indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
