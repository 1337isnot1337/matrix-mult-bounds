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
HERE = ROOT / 'results/local/conjugation-limit'
CHECKPOINT = '6db05f5592b2f252ebc718cfececd5625a44aed5'
TREE = '363271b34a2b82dd033b388d7b48d00f1e76d1f9'

def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item

def frozen():
    actual = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'HEAD^{tree}'], text=True).splitlines()
    if actual != [CHECKPOINT, TREE]:
        raise RuntimeError('the validation tree changed')

def make_plan():
    frozen()
    log = (HERE / 'full-tests.log').read_text()
    headers = re.findall(r'^\S+ \(([^)]+)\) \.\.\.', log, flags=re.M)
    passed = re.findall(r'^\S+ \(([^)]+)\) \.\.\. ok$', log, flags=re.M)
    if len(headers) != len(passed) + 1 or not headers[-1].startswith('test_generic_partner_all_graphs.'):
        raise RuntimeError('unexpected interrupted-prefix shape; inspect it manually')
    if len(set(passed)) != len(passed):
        raise RuntimeError('duplicate completed tests in the prefix')
    tests = list(flatten(unittest.TestLoader().discover('tests')))
    expected = [test.id() for test in tests]
    if len(set(expected)) != len(expected) or not set(passed) <= set(expected):
        raise RuntimeError('discovery identifiers differ from the completed prefix')
    pending = [identifier for identifier in expected if identifier not in set(passed)]
    groups = {}
    for identifier in pending:
        groups.setdefault(identifier.split('.')[0], []).append(identifier)
    shards = [[], [], []]
    for _, identifiers in sorted(groups.items(), key=lambda item: (-len(item[1]), item[0])):
        index = min(range(3), key=lambda i: len(shards[i]))
        shards[index].extend(identifiers)
    plan = {'checkpoint': CHECKPOINT, 'tree': TREE, 'expected_ids': expected,
            'prefix_passed_ids': passed, 'prefix_command': 'python -m unittest discover -s tests -v',
            'prefix_exit_code': 130, 'interruption_reason': 'Parallelize only uncompleted tests',
            'interrupted_uncompleted_id': headers[-1],
            'prefix_log_sha256': hashlib.sha256((HERE / 'full-tests.log').read_bytes()).hexdigest(),
            'shards': shards}
    (HERE / 'plan.json').write_text(json.dumps(plan, indent=2) + '\n')
    print({'expected_tests': len(expected), 'passed_prefix': len(passed),
           'remaining': len(pending), 'shard_sizes': [len(shard) for shard in shards]})

class RecordedResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passed_ids = []
        self.skipped_ids = []
        self.completed_ids = []
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
    tests = list(flatten(unittest.TestLoader().discover('tests')))
    if [test.id() for test in tests] != plan['expected_ids']:
        raise RuntimeError('test discovery changed after the interruption')
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
parser.add_argument('--shard', type=int, choices=range(3))
args = parser.parse_args()
if args.plan:
    make_plan()
else:
    run_shard(args.shard)
