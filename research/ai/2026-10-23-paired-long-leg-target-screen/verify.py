"""Exact conditional comparison of paired long-leg source and target ranks."""

from importlib.util import module_from_spec, spec_from_file_location
from math import comb
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
FRONTIER = ROOT / "results/paired-sources-2026-10-20/all-power-frontier.json"
FRONTIER_SHA256 = "3166e032019c24b0f3f4ba21ad2b23a62fdb357154169b91305ca7f0cb045d54"
ALL_RANKS = ROOT / "research/ai/2026-10-20-paired-sources/all_ranks.py"
ALL_RANKS_SHA256 = "1d63dfbcbb7fb34dd3b1d29fe0a41bd90e0db7295597189d1a7154c6e44d7dff"
UPSTREAM_COMMIT = "a629c557d3ee155cbd1c8c2f97ce3d367a115475"
UPSTREAM_PROOF_SHA256 = "c6d00fd0ce8807c4ad6d16beaabb155faa1ed5323552e990a99045104dfebf49"


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def kernel_sections_upper(a, p):
    """Associated-graded H0 upper bound from the pinned upstream proof."""
    if a < 2 or not 0 <= p <= a * (2 * a - 1):
        raise ValueError("a>=2 and a valid exterior degree are required")
    d, h = a - 1, 2 * a - 1
    return sum(
        a * (choose(h, k) - choose(h, k + 1))
        * choose(d * h, p - k)
        * max(p + d - a * k + 1, 0)
        for k in range(a, h + 1)
    )


def source_rank_lower(a, p):
    n = a * (2 * a - 1)
    return max(0, a * a * choose(n, p) - kernel_sections_upper(a, p))


def contiguous_runs(values):
    runs = []
    for power in sorted(set(values)):
        if not runs or power != runs[-1][-1] + 1:
            runs.append([power, power])
        else:
            runs[-1][-1] = power
    return runs


def load_all_ranks():
    digest = hashlib.sha256(ALL_RANKS.read_bytes()).hexdigest()
    if digest != ALL_RANKS_SHA256:
        raise ValueError(f"pinned target-rank source changed: {digest}")
    spec = spec_from_file_location("paired_target_all_ranks", ALL_RANKS)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_report():
    if hashlib.sha256(FRONTIER.read_bytes()).hexdigest() != FRONTIER_SHA256:
        raise ValueError("pinned paired-source frontier changed")
    sources = json.loads((PACKAGE / "sources.json").read_text())
    upstream = sources["upstream_open_pr"]
    if (upstream["head_commit"] != UPSTREAM_COMMIT
            or upstream["proof_sha256"] != UPSTREAM_PROOF_SHA256):
        raise ValueError("upstream proof pin changed")

    target_ranks = load_all_ranks()
    frontier = json.loads(FRONTIER.read_text())
    records = []
    total_survivors = 0
    for item in frontier["records"]:
        a = item["a"]
        if a not in (14, 15, 16):
            continue
        n = a * (2 * a - 1)
        first_power = a * (a - 1) + 1
        last_power = n - a - 1
        shapes = [entry["shape"] for entry in item["remaining_after_this_screen"]]
        total_survivors += len(shapes)
        per_target = []
        safe_by_target = []
        for l, b, r in shapes:
            both_legs_safe = []
            for p in range(first_power, last_power + 1):
                source_lower = source_rank_lower(a, p)
                target_b = target_ranks.padded_matrix_rank((l, r, b), n, p)
                target_c = target_ranks.padded_matrix_rank((r, l, b), n, p)
                if target_b <= source_lower and target_c <= source_lower:
                    both_legs_safe.append(p)
            safe_by_target.append(both_legs_safe)
            per_target.append({
                "shape": [l, b, r],
                "both_long_leg_target_ranks_at_most_source_lower_bound":
                    contiguous_runs(both_legs_safe),
            })

        all_targets_safe = [
            p for p in range(first_power, last_power + 1)
            if all(p in powers for powers in safe_by_target)
        ]
        records.append({
            "a": a,
            "saved_targets": len(shapes),
            "intermediate_power_range": [first_power, last_power],
            "all_targets_both_legs_at_most_source_lower_bound":
                contiguous_runs(all_targets_safe),
            "powers_with_at_least_one_target_not_dominated":
                (last_power - first_power + 1) - len(all_targets_safe),
            "per_target": per_target,
        })
    if total_survivors != 28:
        raise ValueError(f"expected 28 saved targets, found {total_survivors}")

    return {
        "schema": "paired-long-leg-filtered-target-screen-v1",
        "proof_status": "conditional-on-unreviewed-upstream-proof",
        "upstream_proof_commit": UPSTREAM_COMMIT,
        "upstream_proof_sha256": UPSTREAM_PROOF_SHA256,
        "source_bound": "max(0,a^2*binom(N,p)-U(a,p))",
        "kernel_sections_upper": "sum_{k=a}^{2a-1} a*(binom(2a-1,k)-binom(2a-1,k+1))*binom((a-1)(2a-1),p-k)*max(p+(a-1)-a*k+1,0)",
        "target_rank_method": "exact padded matrix Koszul ranks from pinned all_ranks.py",
        "target_rank_source_sha256": ALL_RANKS_SHA256,
        "frontier_sha256": FRONTIER_SHA256,
        "records": records,
        "independent_review": False,
        "improves_omega": False,
    }


def verify_report(report):
    expected = build_report()
    if report != expected:
        raise ValueError("target-screen certificate differs from exact regeneration")
    return {
        "verified": True,
        "saved_targets": sum(record["saved_targets"] for record in report["records"]),
        "all_target_safe_windows": {
            record["a"]: record["all_targets_both_legs_at_most_source_lower_bound"]
            for record in report["records"]
        },
        "conditional_on_unreviewed_upstream_proof": True,
        "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    report = verify_report(json.loads(args.verify.read_text())) if args.verify else build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")
