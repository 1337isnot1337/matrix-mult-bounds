"""Replay the seventh-power source cover and next two-matrix screen."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from source_power5 import verify as verify_source_power5
from source_power6 import verify as verify_source_power6
from source_power7 import verify as verify_source_power7
from target_power import maximum_direct_sum_power_slice_rank, orientation_orbits


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RESULTS = ROOT/'results/nonsplit-two-matrix-targets-2026-10-23'
SOURCE_RESULTS = ROOT/'results/sl2-finite-slices-2026-10-21'
SOURCE_VERIFIER = ROOT/'research/ai/2026-10-21-sl2-finite-slices/verify_cover.py'
SOURCE_BOUND = 100_070_673_945_707
POWER5_BOUND = 9_874_344_844
POWER6_BOUND = 991_166_716_704


def verify_inputs():
    sources = json.loads((HERE/'SOURCES.json').read_text())
    for record in sources['local']:
        actual = hashlib.sha256((ROOT/record['path']).read_bytes()).hexdigest()
        if actual != record['sha256']:
            raise ValueError(f"source bytes changed: {record['path']}")
    return sources


def verify_dense_source(certificate):
    spec = importlib.util.spec_from_file_location('nonsplit_finite_source_verifier', SOURCE_VERIFIER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.verify(certificate)


def verify():
    sources = verify_inputs()
    source_certificate = json.loads((SOURCE_RESULTS/'cover-certificate.json').read_text())
    dense_report = verify_dense_source(source_certificate)
    if dense_report['original_group_coefficients_checked'] != 120**3:
        raise ValueError('incomplete dense replay of the actual nonsplit source')

    degrees = source_certificate['basis_degrees']
    p5_certificate = json.loads((RESULTS/'power5-source-cover.json').read_text())
    p5_source_report = verify_source_power5(p5_certificate, degrees)
    p6_certificate = json.loads((RESULTS/'power6-source-cover.json').read_text())
    p6_source_report = verify_source_power6(p6_certificate, degrees)
    p7_certificate = json.loads((RESULTS/'power7-source-cover.json').read_text())
    p7_source_report = verify_source_power7(p7_certificate, degrees)
    if (p5_source_report['slice_upper_bound'], p6_source_report['slice_upper_bound'],
            p7_source_report['slice_upper_bound']) != (POWER5_BOUND, POWER6_BOUND, SOURCE_BOUND):
        raise ValueError('one of the saved source-power bounds changed')

    p6_target = json.loads((RESULTS/'power6-target-census.json').read_text())
    if (p6_target['input_candidates_after_power5'], p6_target['power6_excluded_count'],
            p6_target['power6_not_excluded_count'], p6_target['source_power6_slice_upper_bound']) != (
            136, 10, 126, POWER6_BOUND):
        raise ValueError('sixth-power candidate frontier input changed')
    candidates = [row for row in p6_target['candidate_results'] if not row['power6_excluded']]
    if len(candidates) != 126 or len({row['index'] for row in candidates}) != 126:
        raise ValueError('seventh-power candidate list is incomplete or duplicated')

    rows = []
    for candidate in candidates:
        shapes = candidate['shapes']
        leg_dimensions = [sum(shape[permutation[0]]*shape[permutation[1]]
                              for shape in shapes)
                          for permutation in ((0, 1, 2), (1, 2, 0), (2, 0, 1))]
        if max(leg_dimensions) > 120:
            raise ValueError(f"candidate {candidate['index']} exceeds source dimension 120")
        power7 = maximum_direct_sum_power_slice_rank(shapes, 7)
        rows.append({'index': candidate['index'], 'shapes': shapes,
                     'one_copy_joint_leg_dimensions': leg_dimensions,
                     'power6_target_slice_rank': candidate['power6_target_slice_rank'],
                     'power7_target_slice_rank': power7['maximum_slice_rank'],
                     'power7_maximizing_orientation_multisets':
                         power7['maximizing_orientation_multisets'],
                     'power7_excluded': power7['maximum_slice_rank'] > SOURCE_BOUND})

    excluded = [row for row in rows if row['power7_excluded']]
    retained = [row for row in rows if not row['power7_excluded']]
    orbits = orientation_orbits(7)
    if len(orbits) != 132 or any(len(orbit) != 6 for orbit in orbits.values()):
        raise ArithmeticError('seventh-power orientation orbits are not 132 six-element orbits')
    orbit_sizes = {}
    for orbit in orbits.values():
        orbit_sizes[str(len(orbit))] = orbit_sizes.get(str(len(orbit)), 0)+1
    target_report = {'source_power7_slice_upper_bound': SOURCE_BOUND,
                     'full_orientation_multisets': 792,
                     'orientation_orbits_checked': len(orbits),
                     'orientation_orbit_size_counts': orbit_sizes,
                     'input_candidates_after_power6': len(candidates),
                     'power7_excluded_count': len(excluded),
                     'power7_not_excluded_count': len(retained),
                     'largest_power7_target_slice_rank': max(row['power7_target_slice_rank'] for row in rows),
                     'largest_power7_candidate': max(rows, key=lambda row: row['power7_target_slice_rank']),
                     'largest_not_excluded_power7_candidate': max(
                         retained, key=lambda row: row['power7_target_slice_rank']),
                     'excluded_candidates': excluded,
                     'candidate_results': rows,
                     'scope': 'Exact seventh-power check of the 126 candidates not excluded by the pinned '
                              'power-six ledger. The earlier pair enumeration and complex screens are not regenerated.',
                     'all_two_matrix_candidates_enumerated': False,
                     'all_targets_constructed': False,
                     'independent_mathematical_review': False,
                     'lean_formalized': False,
                     'improves_omega': False}
    return {'source_dense_replay': dense_report,
            'source_power5_replay': p5_source_report,
            'source_power6_replay': p6_source_report,
            'source_power7_replay': p7_source_report,
            'target_power7': target_report,
            'prior_frontier': sources['prior_frontier']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    (args.output.parent/'power7-target-census.json').write_text(
        json.dumps(report['target_power7'], indent=2)+'\n')
    print(json.dumps({key: report[key] for key in
                      ('source_dense_replay', 'source_power7_replay')}, indent=2))
    print(json.dumps({key: report['target_power7'][key] for key in
                      ('input_candidates_after_power6', 'power7_excluded_count',
                       'power7_not_excluded_count', 'largest_power7_target_slice_rank')}, indent=2))
