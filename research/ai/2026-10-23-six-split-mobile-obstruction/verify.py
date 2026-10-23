"""Exact saturation obstruction for the six-split seed's mobile W spaces."""
from math import comb
from pathlib import Path
import argparse
import importlib.util
import json
import shutil
import subprocess
import tempfile


PACKAGE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    'six_split_fixed_cover', PACKAGE.parent / '2026-10-23-six-split-grid/verify.py')
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)
CLAIM = 'AI-EXTERNAL-SIX-SPLIT-MOBILE-009'
MOBILE_PAIRS = ((8, 17), (58, 43))
MOBILE_COMPONENTS = ((8, 17), (43, 58, 59))


def check_small_entries(vectors, mobile):
    if len(vectors) != 47 or len(mobile) != 4:
        raise ArithmeticError('Unexpected fixed or mobile input count.')
    if any(len(row) != 20 or any(type(x) is not int or x not in (-1, 0, 1) for x in row)
           for row in list(vectors) + list(mobile)):
        raise ArithmeticError('The bounded-minor proof requires original entries in {0,1,-1}.')


def configuration():
    components, bases, fixed, vectors, checks = S.geometry()
    factors = S.seed()
    mobile = [factors[2][i] for pair in MOBILE_PAIRS for i in pair]
    check_small_entries(vectors, mobile)
    positive_rank = S.C.W.rank([row for row, weight in zip(vectors, S.WEIGHTS) if weight], 101)
    if positive_rank != 20:
        raise ArithmeticError('Positive-weight directions must span dimension twenty.')
    for component, pair in zip(MOBILE_COMPONENTS, MOBILE_PAIRS):
        if list(component) not in components or not set(pair) <= set(component):
            raise ArithmeticError('The required isolated mobile component changed.')
        products = [[u * v for u in factors[0][i] for v in factors[1][i]] for i in component]
        w_rows = [factors[2][i] for i in component]
        if (S.C.W.rank(products, 101) != len(component) or S.C.W.rank(w_rows, 101) != 2
                or S.C.W.rank([factors[2][i] for i in pair], 101) != 2):
            raise ArithmeticError('A mobile W-flattening must have rank two with the stated basis.')
    return vectors, mobile, checks, positive_rank


def check_report(report, vectors, mobile):
    expected = (101, 1009, 47, 20, comb(47, 4), 177997, 16, 21649)
    fields = ('fixed_prime', 'intersection_prime', 'fixed_vectors', 'dimension',
              'four_subsets', 'independent_four_subsets', 'maximum_fixed_weight',
              'unique_saturated_flats')
    if tuple(report[key] for key in fields) != expected:
        raise ArithmeticError('Unexpected saturated-flat coverage or parameters.')
    prior_report = json.loads((S.PACKAGE / 'enumeration.json').read_text())
    S.check_enumeration(prior_report, vectors)
    if report['fixed_weight_histogram'] != prior_report['flat_weight_histogram']:
        raise ArithmeticError('The complete fixed-weight histogram differs from the accepted cover.')
    saturated = report['saturated_basis_count']
    if saturated != report['fixed_weight_histogram']['16']:
        raise ArithmeticError('The saturation counters disagree.')
    if len(report['mobile_pairs']) != 2:
        raise ArithmeticError('Both mobile pairs must be checked.')
    for index, (record, hit_count) in enumerate(zip(report['mobile_pairs'], (25, 26))):
        if record['rank_increment_failures'] != 0 or record['unique_nonzero_intersections'] != hit_count:
            raise ArithmeticError('A mobile space has an uncertified extra intersection.')
        histogram = record['rank_pair_histogram']
        if (len(histogram) != 2 or [row[:2] for row in histogram] != [[4, 5], [5, 6]]
                or any(type(row[2]) is not int or row[2] <= 0 for row in histogram)
                or sum(row[2] for row in histogram) != saturated):
            raise ArithmeticError('Every saturated basis must pass the rank-increment test.')
        ids = record['allowed_line_witness_basis']
        if (len(ids) != 4 or len(set(ids)) != 4
                or any(type(i) is not int or not 0 <= i < 47 for i in ids)):
            raise ArithmeticError('Invalid saturated equality-witness basis.')
        basis = [vectors[i] for i in ids]
        x, y = mobile[2 * index:2 * index + 2]
        if (S.C.W.rank(basis) != 4 or S.C.W.rank(basis + [x]) != 4
                or S.C.W.rank(basis + [x, y]) != 5):
            raise ArithmeticError('The exact allowed-line witness changed.')
        members = [i for i, row in enumerate(vectors) if S.C.W.rank(basis + [row], 101) == 4]
        if sum(S.WEIGHTS[i] for i in members) != 16:
            raise ArithmeticError('The allowed-line witness must be saturated.')


def enumerate_saturated(vectors, mobile):
    check_small_entries(vectors, mobile)
    compiler = shutil.which('cc') or shutil.which('gcc') or shutil.which('clang')
    if compiler is None:
        raise RuntimeError('A C99 compiler is required for the full saturated-flat replay.')
    with tempfile.TemporaryDirectory(prefix='six-split-saturation-') as temporary:
        directory = Path(temporary)
        source = directory / 'input.txt'
        source.write_text(''.join(' '.join(map(str, (weight, *row))) + '\n'
                                  for weight, row in zip(S.WEIGHTS, vectors))
                          + ''.join(' '.join(map(str, row)) + '\n' for row in mobile))
        executable = directory / 'saturated-flats'
        subprocess.run([compiler, '-O3', '-std=c99', '-Wall', '-Wextra',
                        str(PACKAGE / 'saturated_flats.c'), '-o', str(executable)], check=True)
        completed = subprocess.run([str(executable), str(source)], check=True,
                                   capture_output=True, text=True)
        return json.loads(completed.stdout)


def verify(full=False):
    vectors, mobile, checks, positive_rank = configuration()
    report = json.loads((PACKAGE / 'enumeration.json').read_text())
    check_report(report, vectors, mobile)
    if full:
        actual = enumerate_saturated(vectors, mobile)
        check_report(actual, vectors, mobile)
        if actual != report:
            raise ArithmeticError('The complete saturated-flat replay differs from the retained run.')
    return {
        'claim_id': CLAIM,
        'source_sha256': S.C.W.SOURCE_HASH,
        'replacements': [list(row) for row in S.REPLACEMENTS],
        'cross_component_disjointness_checks': checks,
        'positive_weight_fixed_span_rank': positive_rank,
        'saturated_fixed_sets_have_rank_four': True,
        'fixed_weight_total': sum(S.WEIGHTS),
        'fixed_weight_cap': 16,
        'all_saturated_rational_four_flats': report['unique_saturated_flats'],
        'mobile_components': [list(component) for component in MOBILE_COMPONENTS],
        'mobile_W_flattening_ranks': [2, 2],
        'allowed_intersection_lines': [{'spanning_term': pair[0], 'missing_basis_term': pair[1]}
                                       for pair in MOBILE_PAIRS],
        'possible_intersection_span_dimensions': [1, 1],
        'all_finite_standard_flips_full_W_nine_cover_excluded': True,
        'full_W_nine_cover_after_minimum_term_component_refactorizations_excluded': True,
        'termwise_Q64_grid_excluded_in_specified_alignment': True,
        'fixed_47_direction_cover_remains_valid': True,
        'stored_four_subsets': report['four_subsets'],
        'exhaustive_enumeration_rerun_by_this_command': full,
        'field': 'any characteristic-zero extension of the rational numbers',
        'grid_alignment': 'the 25-dimensional target leg maps to the first source leg; W is on a long leg',
        'general_Q64_maps_excluded': False,
        'further_singular_degenerations_excluded': False,
        'other_split_seeds_excluded': False,
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
