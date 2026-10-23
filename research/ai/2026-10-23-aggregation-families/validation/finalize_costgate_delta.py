"""Record the exact validation delta after the separately committed size gate."""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path.cwd()
HERE = ROOT / 'results/local/aggregation-search'
PACKAGE = ROOT / 'research/ai/2026-10-23-aggregation-families'
DEST = PACKAGE / 'validation'
CODE = '7636f7a4b1c84032a32ea03cb17b33b50ebeb7e5'
APPLIED = 'da2dda0b104b2b2ee76a51d1eff352a4687442e0'
META_IDS = {'test_research.RepositoryTests.test_claim_ledger_status',
            'test_research.RepositoryTests.test_relative_markdown_links'}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip() == APPLIED
applied_tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip()
prefix = 'research/ai/2026-10-23-aggregation-families/'
differences = subprocess.check_output(['git', 'diff', '--name-only', CODE, '--'], text=True).splitlines()
allowed_docs = {prefix + name for name in ['README.md', 'proof.md', 'validation.json']}
assert all(path.startswith(prefix + 'validation/') or path in allowed_docs for path in differences)

original = json.loads((DEST / 'combined_report.json').read_text())
assert original['status'] == 'passed_combined_exact_coverage'
for name, value in original['file_sha256'].items():
    assert digest(DEST / name) == value, name
plan = json.loads((DEST / 'plan.json').read_text())
focused = json.loads((DEST / 'costgate-focused-receipt.json').read_text())
assert focused['code_matches_commit'] == CODE
assert digest(ROOT / 'tests/test_aggregation_families.py') == focused['test_module_sha256']
assert digest(DEST / 'costgate-focused.log') == focused['log_sha256']
assert len(focused['test_ids']) == 12

metadata_text = (HERE / 'costgate-metadata.log').read_text()
metadata_ids = re.findall(r'^\S+ \(([^)]+)\) \.\.\. ok$', metadata_text, re.M)
assert set(metadata_ids) == META_IDS and len(metadata_ids) == 2
assert metadata_text.endswith('OK\n')
runtime = re.search(r'Ran 2 tests in ([0-9.]+)s', metadata_text)
assert runtime
shutil.copyfile(HERE / 'costgate-metadata.log', DEST / 'costgate-metadata.log')
shutil.copyfile(HERE / 'finalize_costgate_delta.py', DEST / 'finalize_costgate_delta.py')

tests = list(flatten(unittest.TestLoader().discover('tests')))
expected = [test.id() for test in tests]
assert len(expected) == len(set(expected)) and not any('_FailedTest' in i for i in expected)
old = set(plan['expected_ids'])
replaced = set(plan['final_focused_ids']) | META_IDS
retained = old - replaced
fresh = set(focused['test_ids']) | META_IDS
assert len(fresh) == 14 and len(replaced) == 13
assert retained.isdisjoint(fresh)
assert retained | fresh == set(expected)
assert len(retained) == 895 and len(expected) == 909
added = sorted(set(expected) - old)
assert added == ['test_aggregation_families.AggregationFamilyTests.test_induced_edge_hypothesis_and_sharp_n1_control']

filenames = ['costgate-focused.log', 'costgate-focused-receipt.json',
             'costgate-metadata.log', 'finalize_costgate_delta.py']
report = {
    'status': 'passed_combined_exact_coverage_with_costgate_delta',
    'construction_receipt': 'combined_report.json',
    'construction_tests': original['covered_tests'],
    'costgate_source_commit': CODE,
    'costgate_source_tree': focused['code_tree'],
    'applied_commit_before_documentation_and_receipt_updates': APPLIED,
    'applied_tree_before_documentation_and_receipt_updates': applied_tree,
    'focused_code_equivalence_verified': True,
    'differences_from_focused_code_commit': differences,
    'expected_tests': len(expected), 'covered_tests': len(retained | fresh),
    'retained_unchanged_tests': len(retained),
    'replaced_prior_ids': sorted(replaced),
    'final_focused_ids': focused['test_ids'],
    'final_metadata_ids': metadata_ids,
    'added_test_ids': added,
    'coverage_sets_pairwise_disjoint': True,
    'coverage_union_equals_final_discovery': True,
    'discovered_ids_sha256': hashlib.sha256(('\n'.join(sorted(expected)) + '\n').encode()).hexdigest(),
    'failures': 0, 'errors': 0, 'skipped_tests': 0,
    'focused_runtime_seconds': focused['runtime_seconds'],
    'metadata_runtime_seconds': float(runtime.group(1)),
    'metadata_command': 'python -m unittest discover -s tests -p test_research.py -k test_claim_ledger_status -k test_relative_markdown_links -v',
    'full_monolithic_run_claimed': False,
    'scope': 'The prior 908-case receipt supplies 895 unchanged cases after excluding its eleven aggregation cases and its ledger/link checks. The complete final twelve-case aggregation module and two final metadata tests replace those cases. Their disjoint union equals all 909 currently discovered IDs. The cost-gate focused pass used code matching 7636f7a; all differences in the applied tree are validation evidence and documentation. Final proof and README edits were present for the metadata checks. No other baseline implementation, test source, or construction witness changed.',
    'final_markdown_sha256': {
        str(path.relative_to(ROOT)): digest(path)
        for path in [PACKAGE / 'README.md', PACKAGE / 'proof.md', DEST / 'README.md']
    },
    'file_sha256': {name: digest(DEST / name) for name in filenames},
    'preserved_interrupted_log_terminal_space': True,
    'independent_mathematical_review': False
}
(DEST / 'costgate_delta_report.json').write_text(json.dumps(report, indent=2) + '\n')

validation_path = PACKAGE / 'validation.json'
validation = json.loads(validation_path.read_text())
validation['focused_tests'] = {
    'command': 'python -m unittest discover -s tests -p test_aggregation_families.py -v',
    'passed': 12, 'failures': 0, 'errors': 0,
    'runtime_seconds': focused['runtime_seconds'],
    'scope': 'Final 29-product and 106-product constructions, exact N<=10 cost floor, and exhaustive N=1 hypothesis control; source equivalence to the applied cost-gate checkpoint is verified in the delta receipt.',
    'code_matches_commit': CODE,
    'test_module_sha256': focused['test_module_sha256'],
    'verifier_sha256': digest(PACKAGE / 'verify.py'),
    'binary_evaluator_sha256': digest(PACKAGE / 'evaluate_binary.py'),
    'log': 'validation/costgate-focused.log'
}
validation['full_regression_suite'] = {
    'status': report['status'], 'expected_tests': len(expected), 'covered_tests': len(expected),
    'retained_unchanged_tests': len(retained), 'final_focused_aggregation_tests': 12,
    'final_metadata_tests': 2, 'failures': 0, 'errors': 0, 'skipped_tests': 0,
    'construction_checkpoint': original['code_checkpoint'],
    'costgate_checkpoint': APPLIED,
    'construction_receipt': 'validation/combined_report.json',
    'final_receipt': 'validation/costgate_delta_report.json',
    'scope': report['scope']
}
validation['exact_cost_scope']['all_family_rows_checked'] = list(range(1, 12))
validation['exact_cost_scope']['all_family_sizes_excluded'] = list(range(1, 11))
validation_path.write_text(json.dumps(validation, indent=2) + '\n')
print(json.dumps({key: report[key] for key in ['status', 'expected_tests', 'retained_unchanged_tests', 'focused_runtime_seconds', 'metadata_runtime_seconds', 'added_test_ids']}, indent=2))
