"""Record exact nineteen-test addition and unchanged prior acceptance bytes."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/dev/shm/matrix-consolidation-5e4a124ebf61')
DISK = Path('/workspace/scratch/5e4a124ebf61/consolidation')
sys.path.insert(0, str(DISK))
import run_full_validation as evidence

BASE = '6b57043164f7d534b858507a37f64fdfda38f29f'
BASE_INVENTORY_SHA256 = '5de9f93be205961d6fbdbef3827c58b2c21a7d224d6ad1ab8f4171b9a4f7f172'
REVISED_IDS = {'AI-A4-TWOSIDED-LOWRANK-003', 'AI-A4-TWOSIDED-RANKLOSS-001'}
SHARED = {'PROVENANCE.md', 'STATUS.md', 'docs/research_directions.md', 'research/ACTIVE.md', 'research/claims.json'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def entries(repo, sha):
    result = {}
    for item in git(repo, 'ls-tree', '-r', '-z', sha).split(b'\0'):
        if item:
            meta, name = item.split(b'\t', 1)
            result[name.decode()] = meta.decode()
    return result


def claims(repo, sha):
    rows = json.loads(git(repo, 'show', sha + ':research/claims.json'))['claims']
    assert len({row['id'] for row in rows}) == len(rows)
    return {row['id']: row for row in rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-head', required=True)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--log-dir', type=Path, default=ROOT / 'test_logs_concurrent_wave')
    args = parser.parse_args()
    repo, logs = args.repo.resolve(), args.log_dir.resolve()
    assert not sys.flags.optimize
    summary_path = logs / 'summary.json'
    summary = json.loads(summary_path.read_text())
    if not summary['passed'] or summary['head'] != args.expected_head or summary['tests_run'] != 21:
        parser.error('Require21 passing focused checks at the exact frozen revision')
    if (logs / 'coverage_union.json').exists() or (logs / 'discovery.json').exists():
        parser.error('Existing evidence is immutable')
    plan_path = ROOT / 'concurrent_wave_validation_plan.json'
    audit_path = ROOT / 'concurrent_wave_code_audit.json'
    scope_path = ROOT / 'concurrent_wave_scope.json'
    prior_path = ROOT / 'concurrent_wave_previous_validation_hashes.json'
    plan, audit, scope, prior = [json.loads(path.read_text()) for path in (plan_path, audit_path, scope_path, prior_path)]
    assert plan['expected_tests'] == 21 and plan['baseline_head'] == BASE
    assert all(Path(path).is_file() and digest(Path(path)) == sha for path, sha in prior.items())
    inventory_path = ROOT / 'test_logs_balanced_followup/discovery.json'
    baseline_coverage_path = ROOT / 'test_logs_balanced_followup/coverage_union.json'
    equivalence_path = ROOT / 'main_a510_publication_equivalence.json'
    assert digest(inventory_path) == BASE_INVENTORY_SHA256
    previous_inventory = json.loads(inventory_path.read_text())
    assert json.loads(baseline_coverage_path.read_text())['passed']
    evidence.REPO = repo
    before = evidence.snapshot()
    if before['head'] != args.expected_head or before['status']:
        parser.error('The tested repository must remain clean at the frozen head')
    evidence.write_json(logs / 'inventory_tree_before.json', before)
    env = os.environ.copy()
    env.update(PYTHONOPTIMIZE='0', PYTHONDONTWRITEBYTECODE='1', PYTHONHASHSEED='0',
               OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
    command = [sys.executable, 'tools/test_shard.py', '--list']
    started = time.monotonic()
    print('Listing the frozen concurrent-wave inventory', flush=True)
    with (logs / 'discovery.log').open('w') as out, (logs / 'discovery.stderr.log').open('w') as err:
        result = subprocess.run(command, cwd=repo, env=env, stdout=out, stderr=err, timeout=180)
    if result.returncode:
        raise RuntimeError('Inventory failed; inspect discovery.stderr.log')
    inventory = json.loads((logs / 'discovery.log').read_text())
    evidence.write_json(logs / 'discovery.json', inventory)
    after = evidence.snapshot()
    evidence.write_json(logs / 'inventory_tree_after.json', after)
    baseline_entries, final_entries = entries(repo, BASE), entries(repo, args.expected_head)
    changes = sorted(path for path in baseline_entries.keys() | final_entries.keys()
                     if baseline_entries.get(path) != final_entries.get(path))
    novel = [{'source_commit': head['sha'], **row} for head in scope['heads']
             for row in head['changed_paths'] if not row['already_identical']]
    allowed = SHARED | {row['path'] for row in novel}
    unexpected = [path for path in changes if path not in allowed and not path.startswith('docs/consolidation/')]
    source_checks = []
    for row in novel:
        path = row['path']
        if path in SHARED or path.endswith(('.md', '.log')):
            continue
        source_checks.append({'path': path, 'source_commit': row['source_commit'],
                              'expected_sha256': row['source_sha256'],
                              'actual_sha256': digest(repo / path),
                              'matches': digest(repo / path) == row['source_sha256']})
    old_tests = [path for path in baseline_entries if path.startswith('tests/')]
    existing_tests_exact = all(final_entries.get(path) == baseline_entries[path] for path in old_tests)
    executable_suffixes = {'.py', '.cpp', '.sh', '.yaml', '.yml', '.toml', '.cfg', '.ini'}
    old_executable = [path for path in baseline_entries if not path.startswith('docs/consolidation/')
                      and (Path(path).suffix in executable_suffixes or Path(path).name.startswith('requirements'))]
    existing_executable_exact = all(final_entries.get(path) == baseline_entries[path] for path in old_executable)
    pin_checks = []
    for pin in audit['a4_dependency_pin_checks']:
        actual = digest(repo / pin['path'])
        pin_checks.append({'manifest': pin['manifest'], 'path': pin['path'],
                           'expected_sha256': pin['expected_sha256'], 'actual_sha256': actual,
                           'matches': actual == pin['expected_sha256']})
    old_claims, new_claims = claims(repo, BASE), claims(repo, args.expected_head)
    source_claims = {head['sha']: claims(repo, head['sha']) for head in scope['heads']}
    added_claims = sorted(new_claims.keys() - old_claims.keys())
    removed_claims = sorted(old_claims.keys() - new_claims.keys())
    changed_claims = sorted(key for key in old_claims.keys() & new_claims.keys() if old_claims[key] != new_claims[key])
    expected_added = {}
    for sha, rows in source_claims.items():
        for key in rows.keys() - old_claims.keys():
            if key in expected_added:
                assert expected_added[key]['record'] == rows[key]
            expected_added[key] = {'source_commit': sha, 'record': rows[key]}
    added_exact = set(added_claims) == set(expected_added) and all(new_claims[key] == row['record'] for key, row in expected_added.items())
    a4_sha = 'beb14b693fc7c3283d33a87ac93e4e35afe4e6b9'
    changed_fields = {key: sorted(field for field in old_claims[key].keys() | new_claims[key].keys()
                                 if old_claims[key].get(field) != new_claims[key].get(field)) for key in changed_claims}
    revisions_exact = set(changed_claims) == REVISED_IDS and all(new_claims[key] == source_claims[a4_sha][key] for key in REVISED_IDS)
    flags = ('status', 'independent_review', 'lean_formalized', 'improves_omega')
    old_flags_exact = all(key in new_claims and all(old_claims[key].get(flag) == new_claims[key].get(flag) for flag in flags) for key in old_claims)
    previous, current = set(previous_inventory['test_ids']), set(inventory['test_ids'])
    selected = {test for row in summary['jobs'] for test in row['printed_test_ids']}
    expected_new = set(plan['new_test_ids'])
    tracked_changes = sorted(path for path in before['file_sha256'].keys() | after['file_sha256'].keys()
                             if before['file_sha256'].get(path) != after['file_sha256'].get(path))
    changed_prior = [path for path, sha in prior.items() if not Path(path).is_file() or digest(Path(path)) != sha]
    archive_exact_to_baseline = all(path in baseline_entries and final_entries.get(path) == baseline_entries[path]
                                    for path in before['archive_sha256'])
    source_receipts = [summary_path, plan_path, audit_path, scope_path, prior_path, inventory_path,
                       baseline_coverage_path, equivalence_path, ROOT / 'concurrent_wave_aggregation_static_review.json']
    receipt = {
        'schema': 'matrix-mult-bounds-concurrent-wave-coverage-v1', 'recorded_at': evidence.utc_now(),
        'head': before['head'], 'head_tree': before['head_tree'], 'passing_comparison_head': BASE,
        'source_heads': plan['source_heads'], 'discovery_command': command,
        'discovery_elapsed_seconds': round(time.monotonic() - started, 3),
        'previous_inventory': {'tests': len(previous), 'modules': previous_inventory['total_modules']},
        'final_inventory': {'tests': len(current), 'modules': inventory['total_modules']},
        'tests_added': sorted(current - previous), 'tests_removed': sorted(previous - current),
        'new_tests_without_focused_coverage': sorted((current - previous) - selected),
        'focused_tests_passed': len(selected), 'focused_ids_outside_final_inventory': sorted(selected - current),
        'composite_exactly_covers_final_inventory': previous | selected == current,
        'all_original_test_files_byte_exact': existing_tests_exact, 'existing_test_files_checked': len(old_tests),
        'all_existing_executable_dependency_files_byte_exact': existing_executable_exact,
        'existing_executable_dependency_files_checked': len(old_executable),
        'source_exact_new_code_and_data_checks': source_checks,
        'strict_a4_transitive_dependency_pin_checks': pin_checks,
        'changed_paths_since_passing_tree': changes, 'unexpected_changes': unexpected,
        'claims_count': len(new_claims), 'claim_ids_added': added_claims, 'claim_ids_removed': removed_claims,
        'changed_existing_claim_fields': changed_fields, 'all_five_new_records_exact_to_source': added_exact,
        'two_authored_claim_revisions_exact_to_source': revisions_exact, 'all_existing_claim_status_flags_unchanged': old_flags_exact,
        'tracked_files_changed_during_inventory': tracked_changes, 'frozen_head_unchanged': before['head'] == after['head'],
        'clean_tracked_status_after': not after['status'], 'archive_unchanged': before['archive_sha256'] == after['archive_sha256'],
        'archives_byte_exact_to_passing_baseline': archive_exact_to_baseline, 'archive_files_hashed': len(before['archive_sha256']),
        'previous_evidence_files_checked': len(prior), 'changed_previous_evidence_files': changed_prior,
        'source_receipts': [{'path': str(path), 'sha256': digest(path)} for path in source_receipts],
        'scope_caveat': 'All19 newly added acceptance/rejection tests and the two ledger/link checks passed on this frozen tree. The prior1961-test composite plus these new tests covers the final1980-ID inventory, and every old test/executable/dependency file remains byte-exact. The complete final local suite was listed, not rerun in one uninterrupted execution. Final-head hosted Python matrix, archive replay and Lean CI remain required. Mathematical review/status flags are unchanged.',
    }
    receipt['passed'] = (
        len(previous) == previous_inventory['total_tests'] == 1961 and previous_inventory['total_modules'] == 438
        and len(current) == inventory['total_tests'] == len(inventory['test_ids']) == 1980 and inventory['total_modules'] == 441
        and current - previous == expected_new and len(expected_new) == 19 and not previous - current
        and len(selected) == 21 and not selected - current and previous | selected == current
        and existing_tests_exact and existing_executable_exact and not unexpected
        and all(row['matches'] for row in source_checks) and len(pin_checks) == 19 and all(row['matches'] for row in pin_checks)
        and len(old_claims) == 614 and len(new_claims) == 619 and len(added_claims) == 5 and not removed_claims
        and added_exact and revisions_exact and all(fields == ['limitations'] for fields in changed_fields.values()) and old_flags_exact
        and not tracked_changes and not changed_prior and receipt['frozen_head_unchanged']
        and receipt['clean_tracked_status_after'] and receipt['archive_unchanged'] and archive_exact_to_baseline)
    evidence.write_json(logs / 'coverage_union.json', receipt)
    print(json.dumps({key: receipt[key] for key in ['passed', 'head', 'final_inventory', 'tests_added', 'tests_removed',
          'focused_tests_passed', 'unexpected_changes', 'changed_existing_claim_fields', 'changed_previous_evidence_files']}), flush=True)
    return 0 if receipt['passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
