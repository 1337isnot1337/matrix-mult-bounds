"""Bind the passing 1,950-test inventory to the corrected publication tree."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

import run_full_validation as evidence


BASE = Path(__file__).resolve().parent
PASSING = "72f5c524fd72c894d4420067fd10206944bce405"
CORRECTION = "5d1441090e1c3c804d0ba0797a20ec303b5c08d5"
CLAIM = "AI-OBLIQUE-PAIRED-REPAIR-001"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def tree_entries(repo, commit):
    entries = {}
    for line in git(repo, "ls-tree", "-r", "-z", commit).split(b"\0"):
        if line:
            metadata, path = line.split(b"\t", 1)
            entries[path.decode()] = metadata.decode()
    return entries


def ledger(repo, commit):
    return json.loads(git(repo, "show", commit + ":research/claims.json"))


def active_code(path):
    return (not path.startswith("docs/consolidation/") and (
        path.endswith((".py", ".lean", ".sh", ".toml", ".lock"))
        or path.startswith(("tests/", ".github/workflows/"))
        or Path(path).name in {"requirements.txt", "lean-toolchain"}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expected-head", required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--log-dir", type=Path, default=BASE / "test_logs/nextwave_publication")
    args = parser.parse_args()
    logs = args.log_dir.resolve()
    path = logs / "equivalence.json"
    if path.exists():
        parser.error("Do not replace an existing equivalence receipt")
    summary_path = logs / "summary.json"
    summary = json.loads(summary_path.read_text())
    if not summary["passed"] or summary["head"] != args.expected_head or summary["tests_run"] != 2:
        parser.error("Require two passing ledger/link checks at this exact head")
    evidence.REPO = args.repo.resolve()
    snapshot = evidence.snapshot()
    if snapshot["head"] != args.expected_head or snapshot["status"]:
        parser.error("The checked publication head must still be clean and unchanged")
    source_entries = tree_entries(evidence.REPO, PASSING)
    final_entries = tree_entries(evidence.REPO, args.expected_head)
    changed = sorted(p for p in source_entries.keys() | final_entries.keys()
                     if source_entries.get(p) != final_entries.get(p))
    unexpected = [p for p in changed if p != "research/claims.json"
                  and not p.startswith("docs/consolidation/")]
    code_paths = [p for p in source_entries if active_code(p)]
    test_paths = [p for p in source_entries if p.startswith("tests/")]
    old_ledger = ledger(evidence.REPO, PASSING)
    new_ledger = ledger(evidence.REPO, args.expected_head)
    old_claims = {claim["id"]: claim for claim in old_ledger["claims"]}
    new_claims = {claim["id"]: claim for claim in new_ledger["claims"]}
    source_claim = {claim["id"]: claim for claim in ledger(evidence.REPO, CORRECTION)["claims"]}[CLAIM]
    changed_claims = sorted(key for key in old_claims.keys() | new_claims.keys()
                           if old_claims.get(key) != new_claims.get(key))
    changed_fields = {key: sorted(field for field in old_claims.get(key, {}).keys() | new_claims.get(key, {}).keys()
                                 if old_claims.get(key, {}).get(field) != new_claims.get(key, {}).get(field))
                      for key in changed_claims}
    claim_headers_unchanged = ({key: value for key, value in old_ledger.items() if key != "claims"}
                               == {key: value for key, value in new_ledger.items() if key != "claims"})
    flags = ("status", "independent_review", "lean_formalized", "improves_omega")
    statuses_unchanged = old_claims.keys() == new_claims.keys() and all(
        all(old_claims[key].get(flag) == new_claims[key].get(flag) for flag in flags)
        for key in old_claims)
    original_paths = json.loads((BASE / "nextwave_publication_previous_hashes.json").read_text())
    changed_prior = [name for name, sha in original_paths.items()
                     if not Path(name).is_file() or digest(Path(name)) != sha]
    inventory_path = BASE / "test_logs/nextwave/discovery.json"
    coverage_path = BASE / "test_logs/nextwave/coverage_union.json"
    source_summary_path = BASE / "test_logs/nextwave/summary.json"
    inventory = json.loads(inventory_path.read_text())
    coverage = json.loads(coverage_path.read_text())
    passing_summary = json.loads(source_summary_path.read_text())
    receipt = {
        "schema": "matrix-mult-bounds-nextwave-publication-equivalence-v1",
        "recorded_at": evidence.utc_now(),
        "passing_source_commit": PASSING,
        "correction_source_commit": CORRECTION,
        "validated_final_commit": args.expected_head,
        "validated_final_tree": snapshot["head_tree"],
        "changed_paths": changed,
        "unexpected_changes": unexpected,
        "existing_code_and_config_paths_compared": len(code_paths),
        "existing_code_and_config_bytes_and_modes_unchanged": all(p not in changed for p in code_paths),
        "test_paths_compared": len(test_paths),
        "test_bytes_and_modes_unchanged": all(p not in changed for p in test_paths),
        "proof_witness_and_dependency_files_unchanged": not unexpected,
        "claims_count": len(new_claims),
        "changed_claim_fields": changed_fields,
        "corrected_claim_matches_source_commit": new_claims.get(CLAIM) == source_claim,
        "claim_status_flags_unchanged": statuses_unchanged,
        "ledger_header_fields_unchanged": claim_headers_unchanged,
        "test_inventory_transferred_by_exact_file_equivalence": {
            "tests": inventory["total_tests"], "modules": inventory["total_modules"],
            "inventory_path": str(inventory_path), "inventory_sha256": digest(inventory_path),
            "coverage_path": str(coverage_path), "coverage_sha256": digest(coverage_path)},
        "metadata_gate": {"tests": summary["tests_run"], "passed": summary["passed"],
                          "elapsed_seconds": summary["elapsed_seconds"],
                          "summary_sha256": digest(summary_path)},
        "previous_validation_files_checked": len(original_paths),
        "changed_previous_validation_files": changed_prior,
        "protected_archives_unchanged": summary["archive_unchanged"],
        "protected_archive_files_hashed": summary["archive_files_hashed"],
        "tracked_changes_during_validation": summary["tracked_files_changed_during_validation"],
        "source_receipts": [{"path": str(p), "sha256": digest(p)} for p in (
            source_summary_path, coverage_path, inventory_path,
            BASE / "nextwave_publication_previous_hashes.json")],
        "scope_caveat": (
            "The publication correction changes one written claim statement and provenance metadata. "
            "All mathematical executable, proof, witness, dependency, and test bytes remain identical "
            "to the passing 72f5c524 tree. Two ledger/link checks passed on this corrected "
            "revision. The 1,950-test composite transfers by exact file identity; no fresh uninterrupted "
            "full suite or unchanged census was rerun. Hosted final-head CI remains required. "
            "Mathematical status and review flags are unchanged."
        ),
    }
    receipt["passed"] = (
        summary["passed"] and passing_summary["passed"] and coverage["passed"]
        and passing_summary["head"] == coverage["head"] == PASSING
        and not unexpected and not changed_prior and len(new_claims) == 612
        and changed_fields == {CLAIM: ["statement"]}
        and receipt["corrected_claim_matches_source_commit"] and statuses_unchanged
        and claim_headers_unchanged and receipt["protected_archives_unchanged"]
        and inventory["total_tests"] == 1950 and inventory["total_modules"] == 437
        and not summary["tracked_files_changed_during_validation"]
    )
    evidence.write_json(path, receipt)
    print(json.dumps({key: receipt[key] for key in (
        "passed", "validated_final_commit", "unexpected_changes", "claims_count",
        "changed_claim_fields", "existing_code_and_config_paths_compared", "test_paths_compared",
        "test_inventory_transferred_by_exact_file_equivalence", "changed_previous_validation_files")}), flush=True)
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
