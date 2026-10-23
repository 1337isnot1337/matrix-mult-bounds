"""Preserve the concurrent correction in a new, revision-bound publication tree."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parent
SOURCE_REPO = ROOT / "repo"
REPO = ROOT / "nextwave_publication_repo"
OUT = ROOT / "nextwave_concurrent_output"
TESTED = "72f5c524fd72c894d4420067fd10206944bce405"
CONCURRENT = "5d1441090e1c3c804d0ba0797a20ec303b5c08d5"
BASE = "a764cf16c5f453709aa29bfafa1314c103f3d516"
PREFIX = "docs/consolidation/2026-10-23/"
CLAIM_ID = "AI-OBLIQUE-PAIRED-REPAIR-001"
META = ["central_resolution_manifest.json", "claim_resolution.json", "packaged_evidence_index.json"]


def git(*args, repo=SOURCE_REPO):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def record_hash(row):
    return digest(json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    assert not REPO.exists(), "Never replace an existing worktree."
    assert git("rev-parse", "HEAD", repo=ROOT / "nextwave_repo").decode().strip() == TESTED
    assert not git("status", "--porcelain", repo=ROOT / "nextwave_repo")
    assert git("rev-parse", CONCURRENT + "^").decode().strip() == BASE
    changed_source = git("diff", "--no-renames", "--name-only", BASE, CONCURRENT).decode().splitlines()
    assert set(changed_source) == {"research/claims.json", *[PREFIX + x for x in META]}
    capture = json.loads((ROOT / "concurrent_correction_capture.json").read_bytes())
    assert capture["archive"]["sha"] == CONCURRENT and capture["archive"]["verified"]
    review = json.loads((ROOT / "concurrent_oblique_claim_review.json").read_bytes())
    assert review["reviewed_commit"] == CONCURRENT and review["status"] == "approved"
    prior_bytes = git("show", TESTED + ":research/claims.json")
    source_bytes = git("show", CONCURRENT + ":research/claims.json")
    prior = json.loads(prior_bytes)
    by_id = {r["id"]: r for r in prior["claims"]}
    correction = next(r for r in json.loads(source_bytes)["claims"] if r["id"] == CLAIM_ID)
    old = by_id[CLAIM_ID]
    assert len(by_id) == len(prior["claims"]) == 612
    assert {k for k in set(old) | set(correction) if old.get(k) != correction.get(k)} == {"statement"}
    old_json = json.dumps(old["statement"], ensure_ascii=False).encode()
    new_json = json.dumps(correction["statement"], ensure_ascii=False).encode()
    assert prior_bytes.count(old_json) == 1
    merged_bytes = prior_bytes.replace(old_json, new_json)
    merged = json.loads(merged_bytes)
    new_by_id = {r["id"]: r for r in merged["claims"]}
    assert len(new_by_id) == 612 and new_by_id[CLAIM_ID] == correction
    assert [cid for cid in by_id if by_id[cid] != new_by_id[cid]] == [CLAIM_ID]
    for cid in by_id:
        for flag in ["status", "independent_review", "lean_formalized", "improves_omega"]:
            assert by_id[cid].get(flag) == new_by_id[cid].get(flag)
    OUT.mkdir()
    (OUT / "claims.json").write_bytes(merged_bytes)
    claim_report = deepcopy(json.loads((ROOT / "nextwave_output/resolution_report.json").read_bytes()))
    row = next(r for r in claim_report["claim_sources"] if r["id"] == CLAIM_ID)
    original_row = deepcopy(row)
    assert record_hash(old) == row["record_sha256"]
    row["record_sha256"] = record_hash(correction)
    row["intentional_correction"] = "scope_correction_addendum"
    row["correction_source_sha"] = CONCURRENT
    row["correction_source_record_sha256"] = record_hash(correction)
    source_report = json.loads(git("show", CONCURRENT + ":" + PREFIX + "claim_resolution.json"))
    addendum = {
        "prepared_at": datetime.now(timezone.utc).isoformat(),
        "tested_baseline": TESTED, "concurrent_source_commit": CONCURRENT,
        "concurrent_source_parent": BASE, "concurrent_archive": capture["archive"],
        "claim_id": CLAIM_ID, "changed_fields": ["statement"],
        "reason": "The unchanged proof gives a lower bound for every first map and equality for the supplied attaining map. Preserve the owner's exact concurrent correction through a real merge.",
        "ledger_before_sha256": digest(prior_bytes), "ledger_after_sha256": digest(merged_bytes),
        "claims_before": 612, "claims_after": 612, "unchanged_claim_records": 611,
        "before_record": old, "after_record": correction,
        "before_record_sha256": record_hash(old), "after_record_sha256": record_hash(correction),
        "original_source": original_row,
        "all_original_source_sha_and_record_hashes_retained": True,
        "all_evidence_and_status_flags_preserved": True,
        "five_nextwave_records_preserved_exactly": claim_report["nextwave_addendum"]["added_ids"],
        "source_correction_addendum": source_report["scope_correction_addendum"],
        "independent_scope_review": "concurrent_oblique_claim_review.json",
        "scope_review_does_not_promote_mathematical_review_status": True,
        "topic_source_snapshots": 164, "topic_branch_names": 136,
        "integration_correction_counted_separately": True,
    }
    claim_report["scope_correction_addendum"] = addendum
    write_json(OUT / "resolution_report.json", claim_report)
    write_json(ROOT / "nextwave_concurrent_claim_report.json", addendum)
    decisions = {"schema": "matrix-nextwave-concurrent-resolution-v1", "output_files": [{
        "path": "research/claims.json", "sha256": digest(merged_bytes),
        "source_commit": None, "source_path": "research/claims.json",
        "source_commits": [TESTED, CONCURRENT],
        "reason": "Retain 611 complete records and all 612 evidence/status fields from the tested union; apply only the exact source-authored lower-bound/attainment statement correction from 5d144109. Preserve every original provenance hash and all five added records."
    }]}
    subprocess.run(["git", "-C", str(SOURCE_REPO), "worktree", "add", "-b", "consolidation/nextwave-publication-20261023", str(REPO), TESTED], check=True)
    result = subprocess.run(["git", "-C", str(REPO), "-c", "merge.renames=false", "-c", "merge.directoryRenames=false", "merge", "--no-ff", "--no-commit", CONCURRENT], capture_output=True, text=True)
    assert result.returncode in [0, 1], result.stderr
    conflicts = sorted(set(git("diff", "--name-only", "--diff-filter=U", repo=REPO).decode().splitlines()))
    assert set(conflicts) <= set(changed_source), conflicts
    (REPO / "research/claims.json").write_bytes(merged_bytes)
    docs = REPO / PREFIX
    for name in META:
        before = git("show", TESTED + ":" + PREFIX + name)
        incoming = git("show", CONCURRENT + ":" + PREFIX + name)
        (docs / name).write_bytes(before)
        for suffix, data, sha in [("72f5c524", before, TESTED), ("5d144109", incoming, CONCURRENT)]:
            target = name.removesuffix(".json") + "." + suffix + ".json"
            assert not (docs / target).exists()
            (docs / target).write_bytes(data)
            decisions["output_files"].append({"path": PREFIX + target, "sha256": digest(data),
                "source_commit": sha, "source_path": PREFIX + name,
                "reason": "Preserve the exact historical audit bytes before reconciling the current 612-record audit metadata."})
        decisions["output_files"].append({"path": PREFIX + name, "sha256": digest(before),
            "source_commit": TESTED, "source_path": PREFIX + name,
            "reason": "Retain the tested checkpoint's historical current-report bytes for the content gate; the source correction's exact reports are separately preserved. A later explicit metadata report will install the full 612-record current audit."})
    for source, target in [
        ("nextwave_concurrent_output/resolution_report.json", "nextwave_corrected_claim_resolution.json"),
        ("nextwave_concurrent_claim_report.json", "nextwave_concurrent_claim_report.json"),
        ("concurrent_correction_capture.json", "concurrent_correction_capture.json"),
        ("concurrent_oblique_claim_review.json", "concurrent_oblique_claim_review.json"),
    ]:
        (docs / target).write_bytes((ROOT / source).read_bytes())
    write_json(ROOT / "nextwave_concurrent_resolution.json", decisions)
    (docs / "nextwave_concurrent_resolution.json").write_bytes((ROOT / "nextwave_concurrent_resolution.json").read_bytes())
    git("add", "--all", repo=REPO)
    assert not git("diff", "--name-only", "--diff-filter=U", repo=REPO)
    staged = git("diff", "--cached", "--no-renames", "--name-only", TESTED, repo=REPO).decode().splitlines()
    assert [p for p in staged if not p.startswith(PREFIX)] == ["research/claims.json"]
    git("commit", "-m", "Merge concurrent oblique scope correction into the tested 612-claim union", repo=REPO)
    head = git("rev-parse", "HEAD", repo=REPO).decode().strip()
    parents = git("show", "-s", "--format=%P", "HEAD", repo=REPO).decode().split()
    assert parents == [TESTED, CONCURRENT]
    assert not git("status", "--porcelain", repo=REPO)
    merge_log = [{"branch": "consolidation/all-branches-20261023", "source_sha": CONCURRENT,
        "previous_head": TESTED, "merge_commit": head, "provisional_conflicts": conflicts,
        "resolution_report": "nextwave_concurrent_resolution.json", "preserved_integrated_archive": capture["archive"]["archive_tag"],
        "topic_snapshot_count_unchanged": 164, "stdout": result.stdout, "stderr": result.stderr}]
    write_json(ROOT / "nextwave_concurrent_merge_log.json", merge_log)
    frozen = {"head": head, "tree": git("rev-parse", "HEAD^{tree}", repo=REPO).decode().strip(),
        "baseline": TESTED, "concurrent_source": CONCURRENT, "clean": True,
        "claims": 612, "unchanged_claim_records": 611, "changed_claim_id": CLAIM_ID,
        "changed_claim_fields": ["statement"], "claims_sha256": digest(merged_bytes),
        "all_status_flags_preserved": True, "topic_source_snapshots": 164, "topic_branch_names": 136,
        "separately_archived_integration_correction": capture["archive"],
        "validation_plan": "nextwave_publication_validation_plan.json"}
    write_json(ROOT / "nextwave_publication_frozen.json", frozen)
    print(json.dumps(frozen, indent=2))


if __name__ == "__main__":
    main()
