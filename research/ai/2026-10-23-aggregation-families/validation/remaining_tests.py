"""Resume only uncompleted baseline tests on the frozen aggregation checkpoint."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time
import unittest

ROOT = Path.cwd()
HERE = ROOT / 'results/local/aggregation-search'
PACKAGE = 'research/ai/2026-10-23-aggregation-families/'
CHECKPOINT = 'f802c00d04c3f64c7436b4c9d4da67b81a1834b8'
TREE = 'ca5f7ce98a9f306e71bb5f0270cfd5b39581a695'
LAUNCH = 'c40d4b5'
MODULE = 'test_aggregation_families.'
HEADER = re.compile(r'^\S+ \(([^)]+)\) \.\.\.', re.M)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def frozen():
    actual = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True).splitlines()
    if actual != [CHECKPOINT, TREE]:
        raise RuntimeError('the validation checkpoint changed')
    if subprocess.check_output(['git', 'status', '--porcelain'], text=True):
        raise RuntimeError('the tracked validation worktree is not clean')


def discover():
    tests = list(flatten(unittest.TestLoader().discover('tests')))
    identifiers = [test.id() for test in tests]
    if len(identifiers) != len(set(identifiers)) or any('_FailedTest' in i for i in identifiers):
        raise RuntimeError('duplicate identifiers or a test import failure')
    return tests, identifiers


def manifest(revision):
    data = subprocess.check_output(['git', 'ls-tree', '-r', '-z', revision])
    result = {}
    for entry in data.split(b'\0'):
        if not entry:
            continue
        metadata, path = entry.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        result[path.decode()] = {'mode': mode, 'type': kind, 'git_object': oid}
    return result


def source_comparison():
    before, after = manifest(LAUNCH), manifest(CHECKPOINT)
    changed = {path: {'before': before.get(path), 'after': after.get(path)}
               for path in sorted(set(before) | set(after)) if before.get(path) != after.get(path)}
    other_allowed = {'tests/test_aggregation_families.py', 'STATUS.md', 'PROVENANCE.md', 'research/claims.json'}
    unexpected = [path for path in changed if not path.startswith(PACKAGE) and path not in other_allowed]
    if unexpected:
        raise RuntimeError(f'other launch inputs changed: {unexpected}')
    tests = [path for path in before if path.startswith('tests/') and path.endswith('.py')
             and Path(path).name.startswith('test') and path != 'tests/test_aggregation_families.py']
    sources = [path for path in before if Path(path).suffix in {'.py', '.cpp', '.sh', '.js', '.ts'}
               and not path.startswith(PACKAGE) and path != 'tests/test_aggregation_families.py']
    if any(before[path] != after.get(path) for path in tests + sources):
        raise RuntimeError('baseline test or implementation source changed')
    return {'launch_code_matches_commit': subprocess.check_output(['git', 'rev-parse', LAUNCH], text=True).strip(),
            'checkpoint': CHECKPOINT, 'tree': TREE,
            'unchanged_baseline_test_files': len(tests),
            'unchanged_baseline_implementation_and_test_sources': len(sources),
            'unchanged_tracked_paths': sum(before.get(path) == after.get(path) for path in set(before) | set(after)),
            'changed_paths': changed,
            'scope': 'Every tracked difference is listed. All baseline tests and implementation sources outside the replaced aggregation package/module are byte-identical Git objects. STATUS.md and PROVENANCE.md are documentation; the changed claim ledger is read by a remaining test on the frozen checkpoint.'}


def prefix_results():
    path = HERE / 'full-tests-prefix.log'
    log = path.read_text()
    headers = list(HEADER.finditer(log))
    passed, unfinished, multiline = [], [], []
    for index, header in enumerate(headers):
        end = headers[index + 1].start() if index + 1 < len(headers) else len(log)
        tail = log[header.end():end].strip()
        identifier = header.group(1)
        if tail == 'ok' or tail.startswith('ok\n') or tail.endswith('\nok'):
            passed.append(identifier)
            if tail.splitlines()[0] != 'ok':
                multiline.append(identifier)
        else:
            unfinished.append(identifier)
    expected_interrupted = 'test_mixed_two_coordinate_chart.TwoCoordinateTests.test_changed_polynomial_normal_is_rejected'
    if unfinished != [expected_interrupted] or headers[-1].group(1) != expected_interrupted:
        raise RuntimeError(f'unexpected prefix completion shape: {unfinished}')
    if len(passed) != len(set(passed)):
        raise RuntimeError('duplicate completed prefix test')
    return passed, unfinished[0], multiline


def make_plan():
    frozen()
    comparison = source_comparison()
    passed, interrupted, multiline = prefix_results()
    old_aggregation = [i for i in passed if i.startswith(MODULE)]
    prefix = [i for i in passed if not i.startswith(MODULE)]
    if len(old_aggregation) != 6:
        raise RuntimeError('the old loaded aggregation module did not contain six passed cases')
    focused_path = HERE / 'focused-tests-frozen.log'
    focused_log = focused_path.read_text()
    focused = re.findall(r'^\S+ \(([^)]+)\) \.\.\. ok$', focused_log, re.M)
    if len(focused) != 11 or not focused_log.endswith('OK\n') or not all(i.startswith(MODULE) for i in focused):
        raise RuntimeError('the final focused receipt is not the complete eleven-case module')
    validation = json.loads((ROOT / PACKAGE / 'validation.json').read_text())['focused_tests']
    if digest(ROOT / 'tests/test_aggregation_families.py') != validation['test_module_sha256']:
        raise RuntimeError('the final focused module changed')
    if digest(ROOT / PACKAGE / 'verify.py') != validation['verifier_sha256']:
        raise RuntimeError('the final focused verifier changed')
    if digest(ROOT / PACKAGE / 'evaluate_binary.py') != validation['binary_evaluator_sha256']:
        raise RuntimeError('the final focused evaluator changed')
    _, expected = discover()
    if not set(passed) <= set(expected) or set(focused) != {i for i in expected if i.startswith(MODULE)}:
        raise RuntimeError('receipt identifiers differ from final discovery')
    covered = set(prefix) | set(focused)
    pending = [i for i in expected if i not in covered]
    ledger_reader = 'test_research.RepositoryTests.test_claim_ledger_status'
    if ledger_reader not in pending:
        raise RuntimeError('changed claim ledger would not be checked on the frozen final checkpoint')
    groups = {}
    for identifier in pending:
        groups.setdefault(identifier.split('.')[0], []).append(identifier)
    shards = [[], []]
    for _, identifiers in sorted(groups.items(), key=lambda item: (-len(item[1]), item[0])):
        chosen = min(range(2), key=lambda i: len(shards[i]))
        shards[chosen].extend(identifiers)
    plan = {'checkpoint': CHECKPOINT, 'tree': TREE, 'expected_ids': expected,
            'prefix_passed_ids': prefix, 'discarded_old_aggregation_ids': old_aggregation,
            'final_focused_ids': focused,
            'prefix_command': 'python -m unittest discover -s tests -v',
            'prefix_exit_code': 130,
            'interruption_reason': 'Preserve completed baseline tests and parallelize only the remaining tests',
            'interrupted_uncompleted_id': interrupted, 'multiline_prefix_success_ids': multiline,
            'prefix_log_sha256': digest(HERE / 'full-tests-prefix.log'),
            'focused_log_sha256': digest(focused_path),
            'changed_ledger_reader_in_remaining_ids': ledger_reader,
            'source_comparison': comparison, 'shards': shards}
    (HERE / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    frozen()
    print(json.dumps({'expected_tests': len(expected), 'passed_prefix_retained': len(prefix),
                      'old_aggregation_cases_replaced': len(old_aggregation), 'final_focused': len(focused),
                      'remaining': len(pending), 'shard_sizes': [len(s) for s in shards]}, indent=2))


class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed_ids, self.skipped_ids, self.completed_ids = [], [], []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.passed_ids.append(test.id())

    def addSkip(self, test, reason):
        super().addSkip(test, reason)
        self.skipped_ids.append(test.id())

    def stopTest(self, test):
        super().stopTest(test)
        self.completed_ids.append(test.id())


def run_shard(number):
    frozen()
    plan = json.loads((HERE / 'plan.json').read_text())
    tests, identifiers = discover()
    if identifiers != plan['expected_ids']:
        raise RuntimeError('test discovery changed after planning')
    selected = set(plan['shards'][number])
    suite = unittest.TestSuite(test for test in tests if test.id() in selected)
    start = time.monotonic()
    result = unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run(suite)
    frozen()
    exact = set(result.completed_ids) == selected and len(result.completed_ids) == len(selected)
    record = {'checkpoint': CHECKPOINT, 'tree': TREE, 'shard': number,
              'seconds': round(time.monotonic() - start, 3), 'tests_run': result.testsRun,
              'passed_ids': result.passed_ids, 'skipped_ids': result.skipped_ids,
              'completed_ids': result.completed_ids, 'exact_expected_coverage': exact,
              'successful': result.wasSuccessful(), 'failures': len(result.failures),
              'errors': len(result.errors), 'unexpected_successes': len(result.unexpectedSuccesses)}
    (HERE / f'shard-{number}.json').write_text(json.dumps(record, indent=2) + '\n')
    sys.exit(0 if result.wasSuccessful() and exact else 1)


parser = argparse.ArgumentParser()
parser.add_argument('--plan', action='store_true')
parser.add_argument('--shard', type=int, choices=range(2))
args = parser.parse_args()
if args.plan:
    make_plan()
else:
    run_shard(args.shard)
