"""Exact controls and an exhaustive C replay for a weighted termwise grid bound.

The quick mode checks the stored run and exact witnesses. Only --enumerate
repeats all 1,282,975 U and 424,270 W four-subsets; the report distinguishes them.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import argparse
import json
import shutil
import subprocess
import tempfile

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
SOURCE = ROOT / 'research/ai/2026-10-21-external-grid-seed/factors.json'
SOURCE_HASH = 'bc4bc0eb93b6074ec57aa420322b506a39f7958bd88f2b9897995006c4bc00c3'
EXCEPTIONAL = frozenset((17, 20, 26, 29, 30, 34, 35, 38, 39, 40, 41,
                        44, 46, 51, 55, 59, 61, 64, 67, 70, 72, 74, 75))
WEIGHTS = tuple(3 + (i in EXCEPTIONAL) for i in range(76))
REPORT = PACKAGE / 'enumeration.json'
W_REPORT = PACKAGE / 'w_enumeration.json'
W_WEIGHTS = (4, 3, 3, 2, 3, 3, 2, 2, 4, 1, 2, 1, 4, 4, 4, 4, 4, 4,
             0, 4, 4, 4, 0, 4, 4, 4, 2, 4, 4, 4, 4, 2, 0, 4, 0, 0,
             4, 4, 1, 4, 0, 2, 2, 1, 2, 2, 2, 3, 2, 2, 1, 3, 2, 1,
             4, 3, 0, 2)
SPLIT_REPLACEMENTS = ((0, 18, -1), (17, 8, 1), (48, 2, -1), (56, 22, -1))


def rank(rows, prime=None):
    if not rows:
        return 0
    a = [[x % prime if prime else Fraction(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = pow(a[pivot][col], -1, prime) if prime else 1 / a[pivot][col]
        a[pivot] = [(x * scale) % prime if prime else x * scale for x in a[pivot]]
        for i in range(pivot + 1, len(a)):
            value = a[i][col]
            if value:
                updated = [x - value * y for x, y in zip(a[i], a[pivot])]
                a[i] = [x % prime for x in updated] if prime else updated
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def load_factors():
    raw = SOURCE.read_bytes()
    if sha256(raw).hexdigest() != SOURCE_HASH:
        raise ArithmeticError('External factor arrays differ from the pinned extraction.')
    return json.loads(raw)


def load_vectors():
    data = load_factors()
    vectors = data['u']
    if len(vectors) != 76 or any(len(row) != 20 for row in vectors):
        raise ArithmeticError('Unexpected first-factor dimensions.')
    if any(type(x) is not int for row in vectors for x in row):
        raise ArithmeticError('Expected integer factor coefficients.')
    if any(rank([u, v], 101) != 2 for u, v in combinations(vectors, 2)):
        raise ArithmeticError('The 76 original first factors must be projectively distinct.')
    if rank(vectors, 101) != 20:
        raise ArithmeticError('The finite-field span must extend every smaller flat to rank four.')
    return vectors


def load_w_vectors():
    """Canonical projective classes, in first-occurrence order in the source."""
    data = load_factors()
    classes = {}
    for i, row in enumerate(data['w']):
        if len(row) != 20 or any(type(x) is not int for x in row):
            raise ArithmeticError('Unexpected integer third-factor dimensions.')
        scale = next((x for x in row if x), None)
        if scale is None:
            raise ArithmeticError('The original third factors must be nonzero.')
        canonical = tuple(Fraction(x, scale) for x in row)
        if any(x.denominator != 1 for x in canonical):
            raise ArithmeticError('The pinned third-factor normalization should be integral.')
        canonical = tuple(int(x) for x in canonical)
        classes.setdefault(canonical, []).append(i)
    vectors = list(classes)
    if len(vectors) != 58 or rank(vectors, 101) != 20:
        raise ArithmeticError('Unexpected third-factor projective configuration.')
    if any(rank([u, v], 101) != 2 for u, v in combinations(vectors, 2)):
        raise ArithmeticError('Distinct rational third-factor directions collide modulo 101.')
    return vectors, list(classes.values())


def write_input(path, vectors, weights=WEIGHTS):
    if len(weights) != len(vectors):
        raise ValueError('Each vector needs one weight.')
    path.write_text(''.join(' '.join(map(str, (weight, *row))) + '\n'
                            for weight, row in zip(weights, vectors)))


def check_report(report, vectors):
    if (report['prime'], report['vectors'], report['dimension']) != (101, 76, 20):
        raise ArithmeticError('Unexpected finite enumeration parameters.')
    if report['four_subsets'] != comb(76, 4):
        raise ArithmeticError('The stored run does not cover every four-subset.')
    histogram = {int(k): value for k, value in report['basis_weighted_histogram'].items()}
    pairs = report['size_exceptional_histogram']
    if any(type(k) is not int or type(e) is not int or type(count) is not int
           or not 4 <= k <= 8 or not 0 <= e <= min(k, 23) or count <= 0
           for k, e, count in pairs):
        raise ArithmeticError('Invalid weighted-flat histogram.')
    if len(set((k, e) for k, e, _ in pairs)) != len(pairs):
        raise ArithmeticError('Duplicate weighted-flat histogram cell.')
    marginal = Counter()
    for k, e, count in pairs:
        marginal[k] += count
    if dict(marginal) != histogram or sum(histogram.values()) != report['independent_four_subsets']:
        raise ArithmeticError('The enumeration counters disagree.')
    if report['independent_four_subsets'] != 1280087 or max(histogram) != 8:
        raise ArithmeticError('The source enumeration differs from its retained exact run.')
    if max(3 * k + e for k, e, _ in pairs) != 24 or report['maximum_flat_weight'] != 24:
        raise ArithmeticError('The weighted cap is not 24.')
    weight_histogram = Counter()
    for k, e, count in pairs:
        weight_histogram[3 * k + e] += count
    if dict(weight_histogram) != {int(k): v for k, v in report['flat_weight_histogram'].items()}:
        raise ArithmeticError('The first-factor weight counters disagree.')
    ids = report['weighted_witness_basis']
    if len(ids) != 4 or len(set(ids)) != 4 or any(type(i) is not int or not 0 <= i < 76 for i in ids):
        raise ArithmeticError('Invalid weighted-flat basis.')
    basis = [vectors[i] for i in ids]
    if rank(basis) != 4 or rank(basis, 101) != 4:
        raise ArithmeticError('The weighted-flat witness has the wrong rank.')
    members = [i for i, row in enumerate(vectors) if rank(basis + [row], 101) == 4]
    if members != report['weighted_witness_members']:
        raise ArithmeticError('The weighted witness membership differs from the source.')
    if sum(WEIGHTS[i] for i in members) != 24 or rank([vectors[i] for i in members]) != 4:
        raise ArithmeticError('The cap must be attained by a rational rank-four flat.')


def deletion_screen(deleted, groups=9):
    """Necessary screen when surviving directions are a subset of the original 76.

    Passing this weight inequality does not assert that a grid cover exists.
    """
    if type(groups) is not int or groups <= 0:
        raise ValueError('The number of groups must be a positive integer.')
    deleted = tuple(deleted)
    if len(set(deleted)) != len(deleted) or any(type(i) is not int or not 0 <= i < 76 for i in deleted):
        raise ValueError('Deleted directions must be distinct indices from 0 through 75.')
    removed_weight = sum(WEIGHTS[i] for i in deleted)
    remaining_weight = sum(WEIGHTS) - removed_weight
    return {
        'deleted_distinct_directions': len(deleted),
        'deleted_exceptional_directions': sum(i in EXCEPTIONAL for i in deleted),
        'removed_weight': removed_weight,
        'remaining_distinct_directions': 76 - len(deleted),
        'remaining_weight': remaining_weight,
        'group_capacity': 24 * groups,
        'excluded_by_weight': remaining_weight > 24 * groups,
        'grid_constructed': False,
    }


def check_w_report(report, vectors):
    if (report['prime'], report['vectors'], report['dimension']) != (101, 58, 20):
        raise ArithmeticError('Unexpected third-factor enumeration parameters.')
    if report['four_subsets'] != comb(58, 4) or report['independent_four_subsets'] != 423231:
        raise ArithmeticError('Incorrect complete third-factor coverage.')
    histogram = {int(k): v for k, v in report['basis_weighted_histogram'].items()}
    if histogram != {4: 344182, 5: 67780, 6: 10443, 7: 826}:
        raise ArithmeticError('The third-factor flat histogram changed.')
    if report['maximum_flat_weight'] != 16 or report['maximum_flat_cardinality'] != 7:
        raise ArithmeticError('The third-factor caps changed.')
    weighted = {int(k): v for k, v in report['flat_weight_histogram'].items()}
    if (max(weighted) != 16 or min(weighted) < 0
            or any(type(v) is not int or v <= 0 for v in weighted.values())
            or sum(weighted.values()) != 423231):
        raise ArithmeticError('The third-factor weight counters disagree.')
    ids = report['weighted_witness_basis']
    if len(ids) != 4 or len(set(ids)) != 4 or any(type(i) is not int or not 0 <= i < 58 for i in ids):
        raise ArithmeticError('Invalid third-factor witness basis.')
    basis = [vectors[i] for i in ids]
    if rank(basis, 101) != 4 or rank(basis) != 4:
        raise ArithmeticError('The third-factor witness must have rank four.')
    members = [i for i, row in enumerate(vectors) if rank(basis + [row], 101) == 4]
    if members != report['weighted_witness_members']:
        raise ArithmeticError('The third-factor witness membership changed.')
    if sum(W_WEIGHTS[i] for i in members) != 16 or rank([vectors[i] for i in members]) != 4:
        raise ArithmeticError('The third-factor cap must have a rational equality witness.')


def enumerate_flats(vectors, weights=WEIGHTS):
    compiler = shutil.which('cc') or shutil.which('gcc') or shutil.which('clang')
    if compiler is None:
        raise RuntimeError('A C99 compiler is needed for the exhaustive replay.')
    with tempfile.TemporaryDirectory(prefix='weighted-grid-') as name:
        work = Path(name)
        inp, exe = work / 'input.txt', work / 'weighted-flats'
        write_input(inp, vectors, weights)
        subprocess.run([compiler, '-O3', '-std=c99', f'-DN={len(vectors)}',
                        str(PACKAGE / 'weighted_flats.c'), '-o', str(exe)],
                       check=True, capture_output=True, text=True)
        proc = subprocess.run([str(exe), str(inp)], check=True, capture_output=True, text=True)
        return json.loads(proc.stdout)


def verify(full=False):
    vectors = load_vectors()
    report = json.loads(REPORT.read_text())
    check_report(report, vectors)
    w_vectors, w_classes = load_w_vectors()
    w_report = json.loads(W_REPORT.read_text())
    check_w_report(w_report, w_vectors)
    if full:
        actual = enumerate_flats(vectors)
        check_report(actual, vectors)
        if actual != report:
            raise ArithmeticError('The complete enumeration differs from the retained result.')
        actual_w = enumerate_flats(w_vectors, W_WEIGHTS)
        check_w_report(actual_w, w_vectors)
        if actual_w != w_report:
            raise ArithmeticError('The complete third-factor enumeration differs from the retained result.')
    deleted = [i for i, _, _ in SPLIT_REPLACEMENTS]
    if any(j in deleted or c not in (-1, 1) for _, j, c in SPLIT_REPLACEMENTS):
        raise ArithmeticError('The displayed replacements must retain their target directions.')
    split = deletion_screen(deleted)
    if split['remaining_weight'] != 238 or not split['excluded_by_weight']:
        raise ArithmeticError('The four-split seed control changed.')
    return {
        'source_sha256': SOURCE_HASH,
        'prime': 101,
        'original_projective_directions': 76,
        'exceptional_directions': sorted(EXCEPTIONAL),
        'original_weight': sum(WEIGHTS),
        'rank_four_flat_weight_cap': 24,
        'nine_group_capacity': 216,
        'required_deleted_weight': 35,
        'minimum_number_deleted_by_this_bound': 9,
        'four_split_seed': split,
        'unchanged_third_factor': {
            'projective_directions': 58,
            'projective_class_representatives': [group[0] for group in w_classes],
            'weights': list(W_WEIGHTS),
            'total_weight': sum(W_WEIGHTS),
            'rank_four_flat_weight_cap': 16,
            'nine_group_capacity': 144,
            'minimum_rank_four_groups_by_weight': (sum(W_WEIGHTS) + 15) // 16,
            'stored_four_subsets': w_report['four_subsets'],
            'all_direction_preserving_termwise_candidates_excluded': sum(W_WEIGHTS) > 144,
        },
        'stored_four_subsets': report['four_subsets'],
        'exhaustive_enumeration_rerun_by_this_command': full,
        'arbitrary_replacement_vectors_excluded': False,
        'general_Q64_maps_excluded': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enumerate', action='store_true', help='Rerun every four-subset in C99.')
    parser.add_argument('--write-input', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.write_input:
        write_input(args.write_input, load_vectors())
    result = verify(args.enumerate)
    text = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')
