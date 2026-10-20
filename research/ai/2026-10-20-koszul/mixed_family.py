"""An all-k packing that survives shared-leg Koszul tests; existence is open."""
import argparse
import json
from pathlib import Path

from koszul import intrinsic_rank, profile


def certificate(k):
    if k < 1:
        raise ValueError("k must be positive")
    # Every block shares its full four-dimensional output. The other legs are
    # disjoint. Reversal is represented by interchanging the nonshared lengths.
    shapes = [(1, 4), (4, 1), (2, 3), (3, 2)]
    source = [intrinsic_rank(4, 10 * k, 10 * k + 3, p) for p in range(4)]
    blocks = [[intrinsic_rank(4, a, b, p) for p in range(4)] for a, b in shapes]
    target = [k * sum(r[p] for r in blocks) for p in range(4)]
    source_score = profile(4, 10 * k)
    target_score = k * sum(profile(a, b) for a, b in shapes)
    return {"k": k, "source_convolution": [4, 10 * k],
            "source_dimensions": [4, 10 * k, 10 * k + 3],
            "target_dimensions": [4, 10 * k, 10 * k],
            "shared_identification": "All outputs use the same coefficient basis s^x t^(3-x).",
            "target_border_rank": 10 * k,
            "sector_types": [{"convolution": [a, b], "shared_axis": "output",
                              "multiplicity": k} for a, b in shapes],
            "block_ranks": blocks, "source_ranks": source, "target_ranks": target,
            "rank_slack": [s - t for s, t in zip(source, target)],
            "source_profile": str(source_score), "target_profile": str(target_score),
            "profile_surplus": str(target_score - source_score),
            "profile_ratio": str(target_score / source_score),
            "passes_shared_leg_koszul": all(t <= s for s, t in zip(source, target)),
            "passes_other_full_leg_koszul": True,
            "other_leg_justification": "research_note.md Section 7: maximal source ranks or the target border-rank bound",
            "coordinate_weight_source_length_lower_bound": 12 * k - 1,
            "coordinate_weight_degeneration_excluded": True,
            "degeneration_constructed": False}


def run():
    return {"status": "necessary-test survivor; not a tensor degeneration or exponent bound",
            "proof": "research_note.md, Section 6",
            "first_positive_surplus_in_this_family": 53,
            "limiting_profile_ratio": "351/350",
            "cases": [certificate(k) for k in (1, 52, 53, 54, 100)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    report = run()
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))
