"""Audit the 164 topic snapshots and the separate concurrent integration correction."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
TESTED = "72f5c524fd72c894d4420067fd10206944bce405"
CONCURRENT = "5d1441090e1c3c804d0ba0797a20ec303b5c08d5"
PREFIX = "docs/consolidation/2026-10-23/"
RECEIPT_PATHS = {PREFIX + name for name in ["central_resolution_manifest.json", "preservation_report.json", "packaged_evidence_index.json"]}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", default=str(ROOT / "nextwave_publication_repo"))
    p.add_argument("--commit", required=True)
    p.add_argument("--superseding-report", action="append", default=[])
    args = p.parse_args()

    def git(*parts):
        return subprocess.check_output(["git", "-C", args.repo, *parts])

    prior_path = ROOT / "nextwave_resolution_manifest.json"
    prior = json.loads(prior_path.read_bytes())
    outputs = {r["path"]: deepcopy(r) for r in prior["outputs"]}
    superseded = deepcopy(prior["superseded_outputs"])
    inputs = {str(prior_path): digest(prior_path.read_bytes())}
    conflicts = set(prior["covered_conflicts"])
    logs = ["merge_log.json", "catchup_merge_log.json", "final_catchup_merge_log.json", "late_merge_log.json",
            "receipt_merge_log.json", "postvalidation_merge_log.json", "closure_merge_log.json", "nextwave_merge_log.json",
            "nextwave_concurrent_merge_log.json"]
    for name in logs:
        data = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(data)
        for r in json.loads(data):
            conflicts.update(r.get("provisional_conflicts", []))

    def add(row, report):
        row = deepcopy(row)
        assert row["reason"]
        if row["path"] in RECEIPT_PATHS:
            return
        previous = outputs.get(row["path"])
        if previous:
            if previous["sha256"] != row["sha256"]:
                superseded.append({"path": row["path"], "previous_sha256": previous["sha256"],
                    "previous_report": previous["report"], "final_sha256": row["sha256"], "final_report": report,
                    "reason": row["reason"]})
            row["origins"] = previous.get("origins", []) + row.get("origins", [])
        row["report"] = report
        row.setdefault("origins", []).append({k: row[k] for k in ["source_commit", "source_path", "report", "reason"] if k in row})
        outputs[row["path"]] = row

    claim_path = ROOT / "nextwave_concurrent_output/resolution_report.json"
    claim_report = json.loads(claim_path.read_bytes())
    assert claim_report["consolidated_claim_count"] == 612
    inputs[str(claim_path)] = digest(claim_path.read_bytes())
    for name in ["nextwave_concurrent_resolution.json"] + args.superseding_report:
        data = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(data)
        for row in json.loads(data)["output_files"]:
            add(row, name)
    assert not (set(outputs) & RECEIPT_PATHS), "Do not introduce self-referential receipt hashes."
    manifest = deepcopy(prior)
    manifest.update({"assembled_at": datetime.now(timezone.utc).isoformat(),
        "baseline_tested_head": TESTED, "concurrent_integration_correction": CONCURRENT,
        "topic_source_snapshots": 164, "topic_branch_names": 136,
        "outputs": [outputs[x] for x in sorted(outputs)], "covered_conflicts": sorted(conflicts),
        "superseded_outputs": superseded, "inputs": inputs,
        "method": "Extend the complete frozen 72f5c524 preservation decisions; apply the exact independently inspected concurrent statement correction and explicit metadata supersessions. Preserve all historical reports under revision names.",
        "receipt_hash_scope": "The current central manifest, preservation receipt and evidence index cannot contain their own hashes. Their exact bytes and metadata-only publication transitions are verified by the external transfer/equivalence receipt and evidence index; historical copies remain hash-checked outputs."})
    manifest["conflict_decisions"] = [{"path": x, "resolution_report": outputs[x]["report"] if x in outputs else "prior published resolution",
        "decision": outputs[x]["reason"] if x in outputs else "Retain the prior explicit remapping/deletion decision."} for x in sorted(conflicts)]
    resolution_path = ROOT / "nextwave_concurrent_resolution_manifest.json"
    write_json(resolution_path, manifest)
    plans = ["catchup_plan.json", "final_catchup_plan.json", "supplemental_catchup_plan.json", "late_catchup_plan.json",
             "receipt_catchup_plan.json", "claims_output/postvalidation_plan.json", "claims_output/closure_plan.json", "nextwave_plan.json"]
    archives = ["archive_tags.json", "archive_update_tags.json", "archive_final_tags.json", "archive_shift_window_tags.json",
                "archive_late_tags.json", "archive_receipt_tags.json", "archive_postvalidation_tags.normalized.json",
                "archive_closure_tags.normalized.json", "archive_nextwave_tags.normalized.json"]
    report_path = ROOT / "nextwave_concurrent_preservation_report.json"
    command = [sys.executable, str(ROOT / "claims_output/audit_preservation.py"), "--repo", args.repo,
        "--commit", args.commit, "--snapshot", str(ROOT / "snapshot.json"), "--claims-report", str(claim_path),
        "--resolutions", str(resolution_path), "--conflicts", str(ROOT / "provisional_conflicts.json"),
        "--output", str(report_path)]
    for option, names in [("--catchup", plans), ("--archive-tags", archives), ("--merge-log", logs)]:
        for name in names:
            command += [option, str(ROOT / name)]
    subprocess.run(command, check=True)
    report = json.loads(report_path.read_bytes())
    assert report["archive_tag_receipts_checked"] == 164 and report["final_claim_ids"] == 612
    subprocess.run(["git", "-C", args.repo, "merge-base", "--is-ancestor", CONCURRENT, args.commit], check=True)
    subprocess.run(["git", "-C", args.repo, "merge-base", "--is-ancestor", TESTED, args.commit], check=True)
    capture = json.loads((ROOT / "concurrent_correction_capture.json").read_bytes())
    assert capture["archive"]["sha"] == CONCURRENT and capture["archive"]["verified"]
    before_bytes = git("show", TESTED + ":research/claims.json")
    after_bytes = git("show", args.commit + ":research/claims.json")
    by_id = lambda data: {r["id"]: r for r in json.loads(data)["claims"]}
    before, after = by_id(before_bytes), by_id(after_bytes)
    incoming = by_id(git("show", CONCURRENT + ":research/claims.json"))
    cid = "AI-OBLIQUE-PAIRED-REPAIR-001"
    assert set(before) == set(after) and len(after) == 612
    assert [i for i in before if before[i] != after[i]] == [cid]
    assert after[cid] == incoming[cid]
    assert {k for k in before[cid] if before[cid][k] != after[cid][k]} == {"statement"}
    assert after_bytes == (ROOT / "nextwave_concurrent_output/claims.json").read_bytes()
    historical = []
    for name in ["central_resolution_manifest.json", "claim_resolution.json", "packaged_evidence_index.json"]:
        for suffix, source in [("72f5c524", TESTED), ("5d144109", CONCURRENT)]:
            path = PREFIX + name.removesuffix(".json") + "." + suffix + ".json"
            original = git("show", source + ":" + PREFIX + name)
            assert git("show", args.commit + ":" + path) == original
            historical.append({"path": path, "source_commit": source, "source_path": PREFIX + name, "sha256": digest(original)})
    integration = {"status": "passed", "head": args.commit, "tested_baseline": TESTED,
        "concurrent_commit": CONCURRENT, "archive": capture["archive"],
        "topic_source_snapshots": 164, "topic_branch_names": 136,
        "concurrent_correction_is_separate_from_topic_snapshot_counts": True,
        "both_parent_histories_preserved": True, "claims": 612, "unchanged_claim_records": 611,
        "changed_claim_id": cid, "changed_fields": ["statement"],
        "correction_matches_exact_source_record": True, "all_status_and_evidence_fields_preserved": True,
        "claims_sha256": digest(after_bytes), "exact_historical_audit_copies": historical,
        "topic_preservation_report": {"path": report_path.name, "sha256": digest(report_path.read_bytes())},
        "recorded_at": datetime.now(timezone.utc).isoformat()}
    write_json(ROOT / "nextwave_concurrent_integration_receipt.json", integration)


if __name__ == "__main__":
    main()
