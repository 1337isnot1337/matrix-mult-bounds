#!/usr/bin/env python3
"""Validate the new rectangular delta and account for unchanged prior tests."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import time
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASELINE = "7792abbf2e414b9f7876fa85d95a8b684174a4a9"


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if Path.cwd().resolve() != ROOT:
        raise ValueError("Run this validator from the repository root")
    prior_path = HERE.parent / "validation/costgate_delta_report.json"
    prior = json.loads(prior_path.read_text())
    tests = list(flatten(unittest.TestLoader().discover("tests")))
    ids = [test.id() for test in tests]
    if len(ids) != len(set(ids)) or any("_FailedTest" in value for value in ids):
        raise ValueError("Duplicate test ID or discovery import failure")
    new = {value for value in ids if value.startswith("test_aggregation_rectangular.")}
    old = set(ids) - new
    old_digest = hashlib.sha256(("\n".join(sorted(old)) + "\n").encode()).hexdigest()
    if len(new) != 5 or len(old) != prior["expected_tests"] or old_digest != prior["discovered_ids_sha256"]:
        raise ValueError("The exact new/prior test partition does not match")
    metadata = set(prior["final_metadata_ids"])
    selected = new | metadata
    retained = old - metadata
    changed = subprocess.check_output(["git", "diff", BASELINE, "--name-only"], text=True).splitlines()
    allowed_existing = {"STATUS.md", "PROVENANCE.md", "research/claims.json",
                        "research/ai/2026-10-23-aggregation-families/README.md"}
    allowed_new_prefix = "research/ai/2026-10-23-aggregation-families/rectangular/"
    if any(path not in allowed_existing and path != "tests/test_aggregation_rectangular.py"
           and not path.startswith(allowed_new_prefix) for path in changed):
        raise ValueError("An existing baseline implementation, test or witness changed")
    destination = HERE / "validation"
    destination.mkdir(exist_ok=True)
    log = destination / "focused.log"
    start = time.monotonic()
    with log.open("w") as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(
            unittest.TestSuite(test for test in tests if test.id() in selected))
    elapsed = time.monotonic() - start
    if not result.wasSuccessful() or result.skipped or result.testsRun != len(selected):
        raise ValueError("Focused validation did not pass completely")
    assert retained.isdisjoint(selected) and retained | selected == set(ids)
    proof_files = [HERE / "README.md", HERE / "proof.md", HERE / "certificate.json",
                   HERE / "verify.py", HERE / "validate.py", ROOT / "tests/test_aggregation_rectangular.py"]
    report = {
        "status": "passed_combined_exact_coverage_with_rectangular_delta",
        "baseline_commit": BASELINE,
        "baseline_tree": subprocess.check_output(["git", "rev-parse", BASELINE + "^{tree}"], text=True).strip(),
        "prior_receipt": "../validation/costgate_delta_report.json",
        "prior_receipt_sha256": sha(prior_path),
        "prior_discovered_id_hash_verified": old_digest,
        "existing_source_changes": [],
        "changed_existing_metadata": sorted(set(changed) & allowed_existing),
        "retained_unchanged_tests": len(retained),
        "fresh_test_ids": sorted(selected),
        "new_test_ids": sorted(new),
        "expected_tests": len(ids), "covered_tests": len(retained) + result.testsRun,
        "coverage_union_equals_final_discovery": True, "coverage_sets_pairwise_disjoint": True,
        "failures": 0, "errors": 0, "skipped_tests": 0,
        "focused_runtime_seconds": round(elapsed, 6),
        "full_monolithic_run_claimed": False,
        "archived_replays": "The five passed replays in the prior receipt are retained; no archived or replay source changed",
        "scope": "907 unchanged prior test IDs plus five new rectangular tests and two rerun metadata tests cover all 914 discovered cases. No baseline implementation, test source, construction witness, or archived file changed. This is combined coverage, not a fresh monolithic run.",
        "file_sha256": {str(path.relative_to(ROOT)): sha(path) for path in proof_files + [log]},
        "independent_mathematical_review": False}
    (destination / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("status", "retained_unchanged_tests", "expected_tests",
                                                 "covered_tests", "focused_runtime_seconds")}, indent=2))


if __name__ == "__main__":
    main()
