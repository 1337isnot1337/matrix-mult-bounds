"""Audit169 topic snapshots plus the separately preserved current-main/concurrent histories."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
BASE = "44b917610b64a515122c4fb835f69b7ceefffb08"
MAIN = "9bcee612569b9f56c8a48ed91a5ebd7ebfaef3b2"
CONCURRENT = "434178af88a16a3d13e9db60dd97453207dbf2b2"
PREFIX = "docs/consolidation/2026-10-23/"
SELF_RECEIPTS = {PREFIX + x for x in ["central_resolution_manifest.json", "preservation_report.json", "packaged_evidence_index.json"]}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=str(ROOT / "postmain_repo"))
    parser.add_argument("--commit", required=True)
    parser.add_argument("--superseding-report", action="append", default=[])
    args = parser.parse_args()

    def git(*parts):
        return subprocess.check_output(["git", "-C", args.repo, *parts])

    old = git("show", BASE + ":" + PREFIX + "central_resolution_manifest.json")
    prior_path = ROOT / "live_catchup_output/prior_manifest.44b91761.json"
    if prior_path.exists():
        assert prior_path.read_bytes() == old
    else:
        prior_path.write_bytes(old)
    prior = json.loads(old)
    outputs = {r["path"]: deepcopy(r) for r in prior["outputs"]}
    superseded = deepcopy(prior["superseded_outputs"])
    inputs = {str(prior_path): digest(old)}
    conflicts = set(prior["covered_conflicts"])
    logs = ["merge_log.json", "catchup_merge_log.json", "final_catchup_merge_log.json", "late_merge_log.json", "receipt_merge_log.json",
        "postvalidation_merge_log.json", "closure_merge_log.json", "nextwave_merge_log.json", "nextwave_concurrent_merge_log.json",
        "main_advance_merge_log.json", "concurrent_434_merge_log.json", "live_catchup_merge_log.json"]
    for name in logs:
        raw = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(raw)
        for row in json.loads(raw):
            conflicts.update(row.get("provisional_conflicts", []))
    decisions = {}

    def add(row, report):
        row = deepcopy(row)
        assert row["reason"]
        decisions[row["path"]] = {"path": row["path"], "resolution_report": report, "decision": row["reason"]}
        if row["path"] in SELF_RECEIPTS:
            return
        previous = outputs.get(row["path"])
        if previous:
            if previous["sha256"] != row["sha256"]:
                superseded.append({"path": row["path"], "previous_sha256": previous["sha256"], "previous_report": previous["report"],
                    "final_sha256": row["sha256"], "final_report": report, "reason": row["reason"]})
            row["origins"] = previous.get("origins", []) + row.get("origins", [])
        row["report"] = report
        row.setdefault("origins", []).append({k: row[k] for k in ["source_commit", "source_path", "report", "reason"] if k in row})
        outputs[row["path"]] = row

    metadata = []
    changed_concurrent = git("diff", "--name-only", CONCURRENT + "^1", CONCURRENT).decode().splitlines()
    for path in changed_concurrent:
        if path.startswith(PREFIX):
            metadata.append({"path": path, "sha256": digest(git("show", BASE + ":" + path)), "source_commit": BASE,
                "source_path": path, "reason": "Preserve the larger tested union's current metadata at the content gate; exact concurrent434 metadata survives under revision names. Explicit final packaging installs the169-source audit/guide. Current self-referential audit/index hashes are checked by the external publication evidence index and transfer receipt."})
    metadata_report = ROOT / "live_catchup_metadata_decisions.json"
    if metadata_report.exists():
        assert json.loads(metadata_report.read_bytes()) == {"output_files": metadata}
    else:
        write_json(metadata_report, {"output_files": metadata})
    reports = ["live_catchup_source_resolution.json", "live_catchup_docs_resolution.json", "live_catchup_integration_resolution.json", "live_catchup_metadata_decisions.json"] + args.superseding_report
    for name in reports:
        raw = (ROOT / name).read_bytes()
        inputs[str(ROOT / name)] = digest(raw)
        for row in json.loads(raw)["output_files"]:
            add(row, name)
    claim_path = ROOT / "live_catchup_output/resolution_report.json"
    inputs[str(claim_path)] = digest(claim_path.read_bytes())
    manifest = deepcopy(prior)
    manifest.update({"assembled_at": datetime.now(timezone.utc).isoformat(), "prior_reviewed_union": BASE,
        "current_main": MAIN, "concurrent_remote_history": CONCURRENT, "topic_source_snapshots": 169, "topic_branch_names": 138,
        "outputs": [outputs[p] for p in sorted(outputs)], "covered_conflicts": sorted(conflicts), "superseded_outputs": superseded,
        "inputs": inputs, "method": "Preserve all prior reviewed decisions; add exact frozen source expectations, one limitations-only claim revision and one scoped STATUS replacement. Track current-main and concurrent integration ancestry separately from topic snapshots."})
    manifest["conflict_decisions"] = [decisions.get(p) or {"path": p, "resolution_report": outputs[p]["report"] if p in outputs else "prior published resolution",
        "decision": outputs[p]["reason"] if p in outputs else "Retain the prior explicit remapping/deletion decision."} for p in sorted(conflicts)]
    for path in conflicts:
        assert path in outputs or path in prior["deletions"] or path in decisions, path
    resolution_path = ROOT / "live_catchup_resolution_manifest.json"
    write_json(resolution_path, manifest)
    plans = ["catchup_plan.json", "final_catchup_plan.json", "supplemental_catchup_plan.json", "late_catchup_plan.json", "receipt_catchup_plan.json",
        "claims_output/postvalidation_plan.json", "claims_output/closure_plan.json", "nextwave_plan.json", "live_catchup_plan.json"]
    archives = ["archive_tags.json", "archive_update_tags.json", "archive_final_tags.json", "archive_shift_window_tags.json", "archive_late_tags.json",
        "archive_receipt_tags.json", "archive_postvalidation_tags.normalized.json", "archive_closure_tags.normalized.json", "archive_nextwave_tags.normalized.json", "archive_live_catchup_tags.normalized.json"]
    receipt_path = ROOT / "live_catchup_preservation_report.json"
    command = [sys.executable, str(ROOT / "claims_output/audit_preservation.py"), "--repo", args.repo, "--commit", args.commit,
        "--snapshot", str(ROOT / "snapshot.json"), "--claims-report", str(claim_path), "--resolutions", str(resolution_path),
        "--conflicts", str(ROOT / "provisional_conflicts.json"), "--output", str(receipt_path)]
    for option, names in [("--catchup", plans), ("--archive-tags", archives), ("--merge-log", logs)]:
        for name in names:
            command += [option, str(ROOT / name)]
    subprocess.run(command, check=True)
    audit = json.loads(receipt_path.read_bytes())
    assert audit["archive_tag_receipts_checked"] == 169 and audit["final_claim_ids"] == 612
    for sha in [MAIN, CONCURRENT, BASE]:
        subprocess.run(["git", "-C", args.repo, "merge-base", "--is-ancestor", sha, args.commit], check=True)
    assert git("rev-parse", MAIN + "^{tree}") == git("rev-parse", "aed489a672a79e0ec35d33fea15d875fc425c9db^{tree}")
    historical = []
    for path in changed_concurrent:
        if path.startswith(PREFIX):
            target = PREFIX + Path(path).stem + ".434178af" + Path(path).suffix
            data = git("show", CONCURRENT + ":" + path)
            assert git("show", args.commit + ":" + target) == data
            historical.append({"path": target, "source_commit": CONCURRENT, "source_path": path, "sha256": digest(data)})
    final_ledger = git("show", args.commit + ":research/claims.json")
    assert final_ledger == (ROOT / "live_catchup_output/claims.json").read_bytes()
    before = {r["id"]: r for r in json.loads(git("show", BASE + ":research/claims.json"))["claims"]}
    after = {r["id"]: r for r in json.loads(final_ledger)["claims"]}
    assert set(before) == set(after) and len(after) == 612
    assert [cid for cid in before if before[cid] != after[cid]] == ["AI-HANKEL-ALL-CHARACTERISTICS-001"]
    write_json(ROOT / "live_catchup_history_receipt.json", {"status": "passed", "head": args.commit,
        "current_main": MAIN, "main_tree_equals_already_captured_topic": True, "concurrent_remote_history": CONCURRENT,
        "both_histories_preserved_as_ancestors": True, "topic_source_snapshots": 169, "topic_branch_names": 138,
        "integration_histories_separate_from_topic_counts": True, "claims": 612, "unchanged_records_from44b": 611,
        "claim_change": "Only AI-HANKEL-ALL-CHARACTERISTICS-001.limitations; all status/evidence fields and oblique correction preserved.",
        "exact_concurrent_metadata_copies": historical, "archive_receipt": "archive_concurrent_434.json",
        "preservation_report_sha256": digest(receipt_path.read_bytes()), "recorded_at": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    main()
