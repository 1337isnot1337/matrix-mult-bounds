"""Assemble exact combined coverage after both frozen remainder shards finish."""
import hashlib
import itertools
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path.cwd()
HERE = ROOT / 'results/local/aggregation-search'
DEST = ROOT / 'research/ai/2026-10-23-aggregation-families/validation'
CHECKPOINT = 'f802c00d04c3f64c7436b4c9d4da67b81a1834b8'
TREE = 'ca5f7ce98a9f306e71bb5f0270cfd5b39581a695'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


head = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True).splitlines()
assert head == [CHECKPOINT, TREE], head
assert not subprocess.check_output(['git', 'status', '--porcelain'], text=True)
plan = json.loads((HERE / 'plan.json').read_text())
records = [json.loads((HERE / f'shard-{i}.json').read_text()) for i in range(2)]
assert digest(HERE / 'full-tests-prefix.log') == plan['prefix_log_sha256']
assert digest(HERE / 'focused-tests-frozen.log') == plan['focused_log_sha256']
for number, record in enumerate(records):
    assert (record['checkpoint'], record['tree']) == (CHECKPOINT, TREE)
    assert record['successful'] and record['exact_expected_coverage']
    assert record['failures'] == record['errors'] == record['unexpected_successes'] == 0
    assert not record['skipped_ids']
    expected = set(plan['shards'][number])
    assert len(record['passed_ids']) == len(expected) == record['tests_run']
    assert set(record['passed_ids']) == set(record['completed_ids']) == expected
parts = [plan['prefix_passed_ids'], plan['final_focused_ids'], *(r['passed_ids'] for r in records)]
assert all(len(part) == len(set(part)) for part in parts)
assert all(set(a).isdisjoint(b) for a, b in itertools.combinations(parts, 2))
combined = [identifier for part in parts for identifier in part]
assert len(combined) == len(set(combined)) == len(plan['expected_ids'])
assert set(combined) == set(plan['expected_ids'])
assert set(plan['discarded_old_aggregation_ids']) <= set(plan['final_focused_ids'])
assert plan['changed_ledger_reader_in_remaining_ids'] in set(records[0]['passed_ids']) | set(records[1]['passed_ids'])

# The immutable baseline commit predates the new aggregation test module.
# Compare it directly as an additional check on the preserved prefix.
changed_from_baseline = subprocess.check_output(['git', 'diff', '--name-only', 'bd03b9d', CHECKPOINT], text=True).splitlines()
package = 'research/ai/2026-10-23-aggregation-families/'
allowed = {'tests/test_aggregation_families.py', 'STATUS.md', 'PROVENANCE.md', 'research/claims.json'}
assert all(path.startswith(package) or path in allowed for path in changed_from_baseline)

DEST.mkdir()
filenames = ['remaining_tests.py', 'finalize_validation.py', 'plan.json',
             'full-tests-prefix.log', 'focused-tests-frozen.log',
             'shard-0.log', 'shard-0.json', 'shard-1.log', 'shard-1.json',
             'replay-preserved.log']
for name in filenames:
    shutil.copyfile(HERE / name, DEST / name)
report = {
    'status': 'passed_combined_exact_coverage',
    'code_checkpoint': CHECKPOINT, 'code_tree': TREE,
    'expected_tests': len(plan['expected_ids']),
    'covered_tests': len(combined),
    'retained_baseline_prefix_tests': len(parts[0]),
    'superseded_old_aggregation_tests': len(plan['discarded_old_aggregation_ids']),
    'final_focused_aggregation_tests': len(parts[1]),
    'remaining_shard_tests': [r['tests_run'] for r in records],
    'remaining_shard_seconds': [r['seconds'] for r in records],
    'failures': 0, 'errors': 0, 'skipped_tests': 0,
    'coverage_sets_pairwise_disjoint': True,
    'coverage_union_equals_final_discovery': True,
    'full_monolithic_run_claimed': False,
    'prefix_command': plan['prefix_command'], 'prefix_exit_code': 130,
    'prefix_total_successes_before_replacement': len(parts[0]) + len(plan['discarded_old_aggregation_ids']),
    'interrupted_case_completed_in_shards': plan['interrupted_uncompleted_id'],
    'prefix_successes_with_interleaved_stdout': plan['multiline_prefix_success_ids'],
    'source_comparison': {
        'launch_code_matches_commit': plan['source_comparison']['launch_code_matches_commit'],
        'unchanged_baseline_test_files': plan['source_comparison']['unchanged_baseline_test_files'],
        'unchanged_baseline_implementation_and_test_sources': plan['source_comparison']['unchanged_baseline_implementation_and_test_sources'],
        'unchanged_tracked_paths': plan['source_comparison']['unchanged_tracked_paths'],
        'direct_comparison_to_baseline_bd03b9d_passed': True,
        'full_git_object_difference_receipt': 'plan.json',
        'changed_claim_ledger_checked_on_frozen_checkpoint': plan['changed_ledger_reader_in_remaining_ids']
    },
    'scope': 'Combined exact coverage, not one monolithic frozen run. The six old aggregation cases are discarded; the final eleven-case focused pass replaces them. Every other test and implementation source is unchanged from the launch baseline. Both remainder shards ran on frozen f802c00, with HEAD/tree and clean-worktree checks before and after. The three changed files outside the aggregation package/module are documentation and the claim ledger; its reader passed on the frozen checkpoint.',
    'archived_replay': {'passed_reports': 5, 'implementation_unchanged_from_launch': True, 'log': 'replay-preserved.log'},
    'file_sha256': {name: digest(DEST / name) for name in filenames},
    'independent_mathematical_review': False
}
(DEST / 'combined_report.json').write_text(json.dumps(report, indent=2) + '\n')
validation_path = DEST.parent / 'validation.json'
validation = json.loads(validation_path.read_text())
validation['full_regression_suite'] = {
    'status': report['status'], 'code_checkpoint': CHECKPOINT, 'code_tree': TREE,
    'command': 'python -m unittest discover -s tests -v, followed by two recorded remainder shards',
    'expected_tests': report['expected_tests'], 'covered_tests': report['covered_tests'],
    'retained_baseline_prefix_tests': report['retained_baseline_prefix_tests'],
    'superseded_old_aggregation_tests': report['superseded_old_aggregation_tests'],
    'final_focused_aggregation_tests': report['final_focused_aggregation_tests'],
    'remaining_shard_tests': report['remaining_shard_tests'],
    'failures': 0, 'errors': 0, 'skipped_tests': 0,
    'receipt': 'validation/combined_report.json',
    'scope': report['scope']
}
validation_path.write_text(json.dumps(validation, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ['status', 'covered_tests', 'retained_baseline_prefix_tests', 'final_focused_aggregation_tests', 'remaining_shard_tests', 'code_tree']}, indent=2))
