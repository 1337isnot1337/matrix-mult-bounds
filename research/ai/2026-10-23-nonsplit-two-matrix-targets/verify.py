"""Replay the nonsplit source power-five and two-matrix candidate checks."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from source_power5 import export as export_source_power5, verify as verify_source_power5
from target_power import maximum_direct_sum_power_slice_rank


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULTS = ROOT/'results/nonsplit-two-matrix-targets-2026-10-23'
SOURCE_RESULTS = ROOT/'results/sl2-finite-slices-2026-10-21'
SOURCE_VERIFIER = ROOT/'research/ai/2026-10-21-sl2-finite-slices/verify_cover.py'
SOURCE_BOUND = 9_874_344_844


def load_source_verifier():
    spec = importlib.util.spec_from_file_location('nonsplit_finite_source_verifier', SOURCE_VERIFIER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_inputs():
    sources = json.loads((HERE/'SOURCES.json').read_text())
    for record in sources['local']:
        actual = hashlib.sha256((ROOT/record['path']).read_bytes()).hexdigest()
        if actual != record['sha256']:
            raise ValueError(f"source bytes changed: {record['path']}")
    return sources


def verify():
    sources = verify_inputs()
    source_certificate = json.loads((SOURCE_RESULTS/'cover-certificate.json').read_text())
    source_report = load_source_verifier().verify(source_certificate)
    if source_report['original_group_coefficients_checked'] != 120**3:
        raise ValueError('full original SL(2,F5) coefficient replay changed')

    degrees = source_certificate['basis_degrees']
    expected_source_power5 = export_source_power5(degrees)
    source_power5_path = RESULTS/'power5-source-cover.json'
    stored_source_power5 = json.loads(source_power5_path.read_text())
    source_power5_report = verify_source_power5(stored_source_power5, degrees)
    if stored_source_power5 != expected_source_power5:
        raise ValueError('saved source power-five cover is not the reconstructed cover')
    if source_power5_report['slice_upper_bound'] != SOURCE_BOUND:
        raise ValueError('wrong source power-five slice bound')

    pilot = json.loads((RESULTS/'pilot.json').read_text())
    profile = json.loads((RESULTS/'profile-pilot.json').read_text())
    if pilot['counts'] != {
            'pair_orientation_cases': 1_576_960,
            'dimension_and_slice': 707_476,
            'strict_gate': 1_165,
            'joint_koszul': 344,
            'joint_cube': 313}:
        raise ValueError('pinned earlier pair-screen counts changed')
    if (profile['before_profile'], profile['profile_excluded'], profile['after_profile']) != (313, 151, 162):
        raise ValueError('pinned earlier profile-screen counts changed')
    cube = json.loads((RESULTS/'permutation-cube-pilot.json').read_text())
    if (cube['unique_after_profile'], cube['permutation_cube_excluded'],
            cube['survivor_count']) != (145, 1, 144):
        raise ValueError('saved earlier-screen frontier counts changed')
    candidates = cube['survivors']
    if len(candidates) != 144 or len({json.dumps(row['shapes']) for row in candidates}) != 144:
        raise ValueError('two-matrix candidate list is incomplete or duplicated')

    rows = []
    for index, candidate in enumerate(candidates):
        shapes = candidate['shapes']
        leg_dimensions = [sum(shape[permutation[0]]*shape[permutation[1]]
                              for shape in shapes)
                          for permutation in ((0, 1, 2), (1, 2, 0), (2, 0, 1))]
        if max(leg_dimensions) > 120:
            raise ValueError(f'candidate {index} exceeds source dimension 120')
        one_copy_cube = maximum_direct_sum_power_slice_rank(shapes, 3)
        if one_copy_cube['maximum_slice_rank'] != candidate['maximum_permuted_cube_target_slice_rank']:
            raise ValueError(f'prior target cube value changed for candidate {index}')
        power5 = maximum_direct_sum_power_slice_rank(shapes, 5)
        rows.append({'index': index, 'shapes': shapes,
                     'one_copy_joint_leg_dimensions': leg_dimensions,
                     'power3_target_slice_rank': one_copy_cube['maximum_slice_rank'],
                     'power5_target_slice_rank': power5['maximum_slice_rank'],
                     'power5_maximizing_orientation_multisets':
                         power5['maximizing_orientation_multisets'],
                     'power5_excluded': power5['maximum_slice_rank'] > SOURCE_BOUND})

    excluded = [row for row in rows if row['power5_excluded']]
    retained = [row for row in rows if not row['power5_excluded']]
    target_report = {'source_power5_slice_upper_bound': SOURCE_BOUND,
                     'orientation_multisets_checked_per_candidate':
                         maximum_direct_sum_power_slice_rank(candidates[0]['shapes'], 5)['full_orientation_multisets'],
                     'orientation_orbits_checked_per_candidate':
                         maximum_direct_sum_power_slice_rank(candidates[0]['shapes'], 5)['orientation_multisets_checked'],
                     'candidate_count_from_pinned_prior_ledger': len(rows),
                     'prior_power3_values_replayed': len(rows),
                     'power5_excluded_count': len(excluded),
                     'power5_not_excluded_count': len(retained),
                     'largest_power5_target_slice_rank': max(row['power5_target_slice_rank'] for row in rows),
                     'largest_power5_candidate': max(rows, key=lambda row: row['power5_target_slice_rank']),
                     'excluded_candidates': excluded,
                     'candidate_results': rows,
                     'scope': 'Exact power-five check of the 144 candidates in the pinned prior frontier. '
                              'The earlier pair enumeration, rank-profile, and Koszul screens are not regenerated here.',
                     'all_two_matrix_candidates_enumerated': False,
                     'all_targets_constructed': False,
                     'independent_mathematical_review': False,
                     'lean_formalized': False,
                     'improves_omega': False}
    return {'source_dense_replay': source_report,
            'source_power5_replay': source_power5_report,
            'target_power5': target_report,
            'prior_frontier': sources['prior_frontier']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    target_path = args.output.parent/'power5-target-census.json'
    target_path.write_text(json.dumps(report['target_power5'], indent=2)+'\n')
    print(json.dumps({key: report[key] for key in ('source_dense_replay', 'source_power5_replay')}, indent=2))
    print(json.dumps({key: report['target_power5'][key] for key in
                      ('candidate_count_from_pinned_prior_ledger', 'power5_excluded_count',
                       'power5_not_excluded_count', 'largest_power5_target_slice_rank')}, indent=2))
