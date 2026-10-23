#!/usr/bin/env python3
"""Record the new pruned-grid delta, retaining exact unchanged prior coverage."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import time
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASELINE = "730a7db2f922ce117f76f4ea75bd48111928f2a8"


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def id_hash(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if Path.cwd().resolve() != ROOT:
        raise ValueError("Run from the repository root")
    prior_path = HERE.parent / "rectangular/validation/report.json"
    prior = json.loads(prior_path.read_text())
    tests = list(flatten(unittest.TestLoader().discover("tests")))
    ids = [test.id() for test in tests]
    if len(ids) != len(set(ids)) or any("_FailedTest" in value for value in ids):
        raise ValueError("Duplicate IDs or failed discovery")
    new = {value for value in ids if value.startswith("test_aggregation_pruned.")}
    old = set(ids) - new
    old_rectangular = set(prior["new_test_ids"])
    if len(new) != 6 or len(old) != prior["expected_tests"] or not old_rectangular <= old:
        raise ValueError("The prior/new discovery partition changed")
    if id_hash(old - old_rectangular) != prior["prior_discovered_id_hash_verified"]:
        raise ValueError("The exact retained pre-rectangular test ID set changed")
    metadata = {"test_research.RepositoryTests.test_claim_ledger_status",
                "test_research.RepositoryTests.test_relative_markdown_links"}
    fresh, retained = new | metadata, old - metadata
    changed = subprocess.check_output(["git", "diff", BASELINE, "--name-only"], text=True).splitlines()
    allowed_existing = {"STATUS.md", "PROVENANCE.md", "research/claims.json",
                        "research/ai/2026-10-23-aggregation-families/README.md"}
    prefix = "research/ai/2026-10-23-aggregation-families/pruned/"
    if any(path not in allowed_existing and path != "tests/test_aggregation_pruned.py"
           and not path.startswith(prefix) for path in changed):
        raise ValueError("An existing baseline implementation, test or witness changed")
    old_paths = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BASELINE], text=True).splitlines()
    old_code = [path for path in old_paths if Path(path).suffix in (".py", ".cpp", ".c", ".h", ".hpp", ".sh")]
    if set(old_code) & set(changed):
        raise ValueError("An old code source changed")
    destination = HERE / "validation"
    destination.mkdir(exist_ok=True)
    receipt_path = destination / "report.json"
    receipt_path.write_text('{"status": "validation_in_progress"}\n')
    log = destination / "focused.log"
    start = time.monotonic()
    with log.open("w") as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
            unittest.TestSuite(test for test in tests if test.id() in fresh))
    elapsed = time.monotonic() - start
    if not result.wasSuccessful() or result.skipped or result.testsRun != len(fresh):
        raise ValueError("The complete focused delta did not pass")
    if retained & fresh or retained | fresh != set(ids):
        raise ValueError("The coverage sets do not form an exact partition")
    paths = sorted(path for path in HERE.rglob("*") if path.is_file()
                   and path.suffix in (".py", ".md", ".json", ".txt")
                   and destination not in path.parents)
    paths.append(ROOT / "tests/test_aggregation_pruned.py")
    paths.append(log)
    report = {
        "status": "passed_combined_exact_coverage_with_pruned_grid_delta",
        "baseline_commit": BASELINE,
        "baseline_tree": subprocess.check_output(["git", "rev-parse", BASELINE + "^{tree}"], text=True).strip(),
        "prior_receipt": "../rectangular/validation/report.json", "prior_receipt_sha256": sha(prior_path),
        "retained_prior_test_id_set_verified": True, "unchanged_baseline_code_files": len(old_code),
        "existing_source_changes": [], "changed_existing_metadata": sorted(set(changed) & allowed_existing),
        "retained_unchanged_tests": len(retained), "fresh_test_ids": sorted(fresh), "new_test_ids": sorted(new),
        "expected_tests": len(ids), "covered_tests": len(retained) + result.testsRun,
        "discovered_ids_sha256": id_hash(ids), "coverage_sets_pairwise_disjoint": True,
        "coverage_union_equals_final_discovery": True, "failures": 0, "errors": 0, "skipped_tests": 0,
        "focused_runtime_seconds": round(elapsed, 6), "full_monolithic_run_claimed": False,
        "scope": "912 unchanged prior successes plus six new pruned-grid tests and two rerun metadata checks cover all 920 discovered IDs. No baseline implementation, test source, construction witness, or archive changed. The five previously passed archive replays are retained. This is combined evidence, not a fresh complete run.",
        "resolved_development_failure": "The first six-test run found that in-memory correction-count keys were integers while JSON keys were strings. The verifier now emits string keys consistently; the complete saved-report comparison and all six tests then passed. No mathematical certificate or construction changed.",
        "same_session_audit": "proof_boundaries separately checked the rectangular proofs and the common-support argument; this does not count as independent mathematical review",
        "file_sha256": {str(path.relative_to(ROOT)): sha(path) for path in paths},
        "independent_mathematical_review": False}
    receipt_path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("status", "retained_unchanged_tests", "expected_tests",
                                                 "covered_tests", "unchanged_baseline_code_files",
                                                 "focused_runtime_seconds")}, indent=2))


if __name__ == "__main__":
    main()
