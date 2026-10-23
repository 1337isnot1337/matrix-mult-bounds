"""Collect the frozen regression, including the disclosed scratch-link retries."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import platform
import shutil
import subprocess

ROOT = Path.cwd()
HERE = ROOT / 'results/local/conjugation-limit'
DEST = ROOT / 'results/conjugation-limit-2026-10-23/validation'
TEST = 'test_research.RepositoryTests.test_relative_markdown_links'

plan = json.loads((HERE / 'plan.json').read_text())
shards = [json.loads((HERE / f'shard-{i}.json').read_text()) for i in range(3)]
expected = set(plan['expected_ids'])
prefix = plan['prefix_passed_ids']
completed = prefix + [identifier for shard in shards for identifier in shard['completed_ids']]
passed = prefix + [identifier for shard in shards for identifier in shard['passed_ids']]
skipped = [identifier for shard in shards for identifier in shard['skipped_ids']]
counts = collections.Counter(completed)
initial_failed = sorted(expected - set(passed) - set(skipped))
current = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True).splitlines()
identity = current == [plan['checkpoint'], plan['tree']]
exact = set(completed) == expected and all(value == 1 for value in counts.values())
assert identity and exact
assert initial_failed == [TEST]
assert [shard['failures'] for shard in shards] == [0, 1, 0]
assert all(shard['errors'] == 0 and shard['exact_expected_coverage'] for shard in shards)

retry_names = ['link-test-retry.log', 'link-test-retry-2.log', 'link-test-retry-3.log']
retry_logs = [(HERE / name).read_text() for name in retry_names]
assert all('Ran 1 test' in log for log in retry_logs)
assert all('FAILED (failures=1)' in log for log in retry_logs[:2])
assert retry_logs[-1].rstrip().endswith('OK') and f'({TEST}) ... ok' in retry_logs[-1]
assert all('EXPLORATION.md: proof.md' in log for log in retry_logs[:2])
replay_lines = (HERE / 'replay.log').read_text().splitlines()
assert len(replay_lines) == 5 and all(': passed (' in line for line in replay_lines)
DEST.mkdir(parents=True, exist_ok=True)
files = ['full-tests.log', 'shard-0.log', 'shard-1.log', 'shard-2.log', 'replay.log',
         'plan.json', 'shard-0.json', 'shard-1.json', 'shard-2.json',
         'remaining_tests.py', 'collect_validation.py', 'finalize_validation.py',
         'initial-validation.json'] + retry_names
for name in files:
    shutil.copyfile(HERE / name, DEST / name)
report = {
    'schema': 'a4-conjugation-validation-v2',
    'completed_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'python': platform.python_version(),
    'tested_local_commit': plan['checkpoint'],
    'tested_tree': plan['tree'],
    'tree_and_head_unchanged_during_validation': identity,
    'full_regression': {
        'discovered_tests': len(expected), 'unique_completed_tests': len(completed),
        'initial_passed_tests': len(passed), 'initial_failed_test_ids': initial_failed,
        'skipped_tests': len(skipped), 'initial_all_passed': False,
        'missing_test_ids': sorted(expected-set(completed)),
        'unexpected_test_ids': sorted(set(completed)-expected),
        'duplicate_completed_test_ids': sorted(key for key,value in counts.items() if value > 1),
        'exact_initial_union_coverage': exact,
        'final_passed_tests_after_scratch_correction': len(set(passed) | {TEST}),
        'final_unresolved_failed_test_ids': [],
        'all_passed_after_scratch_correction': set(passed) | {TEST} == expected,
        'monolithic_run_completed': False,
        'prefix_command': plan['prefix_command'], 'prefix_exit_code': 130,
        'prefix_passed_tests': len(prefix),
        'interruption_reason': plan['interruption_reason'],
        'interrupted_test_resumed': plan['interrupted_uncompleted_id'],
        'shard_test_counts': [shard['tests_run'] for shard in shards],
        'shard_exit_codes': [0, 1, 0],
        'shard_commands': [f'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python results/local/conjugation-limit/remaining_tests.py --shard {i}' for i in range(3)],
        'scratch_document_correction': {
            'failed_test_id': TEST,
            'cause': 'The Markdown-link test scans untracked files. A draft EXPLORATION.md under results/local had links intended for its eventual package location, including a nonexistent proof.md sibling.',
            'correction': 'Preserved the draft outside the repository and changed its remaining transient scratch copy to plain-text references. No tracked source, test, or validation gate was changed.',
            'intermediate_retries': [
                {'log': retry_names[0], 'exit_code': 1, 'reason': 'A transient scratch copy still contained the same invalid link.'},
                {'log': retry_names[1], 'exit_code': 1, 'reason': 'The original scratch copy had reappeared with the same invalid link.'}],
            'final_retry': {'log': retry_names[2], 'exit_code': 0, 'tests_passed': 1},
            'retry_command': 'python -m unittest discover -s tests -p test_research.py -k test_relative_markdown_links -v'
        }
    },
    'archive_replay': {'command': 'python tools/replay.py', 'exit_code': 0,
                       'all_five_passed': True, 'reports': replay_lines},
    'focused_verification': {'command': "python -m unittest discover -s tests -p 'test_conjugation_limit.py' -v",
                             'tests_passed': 8, 'seconds': 13.283,
                             'counted_again_as_new_coverage': False},
    'certificate_replay': {'command': 'python research/ai/2026-10-23-conjugation-limit/verify.py',
                           'exit_code': 0, 'regenerated_discovery_equals_retained_certificate': True},
    'artifact_sha256': {name: hashlib.sha256((DEST/name).read_bytes()).hexdigest() for name in files},
    'all_validation_passed_after_scratch_correction': True,
    'scope': 'The frozen code tree is covered by a retained 288-test successful prefix and three disjoint remaining-test shards. One scratch-document link failed and was corrected, then only that test was rerun. All failed receipts and logs are retained. The interrupted monolithic run is not represented as completed. Same-session checking does not change mathematical review status.'
}
(DEST.parent / 'validation.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({key: report[key] for key in ['tested_tree', 'all_validation_passed_after_scratch_correction']}))
print(json.dumps(report['full_regression'], indent=2))
