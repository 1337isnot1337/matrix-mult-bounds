"""Complete ordinary square-sum screen through source leg dimension 1377.

Applies the credited existing gates and integer recurrence without changing
their files. Necessary-test survivors are not tensor constructions.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "unbalanced_frontier_prior_application",
    ROOT / "research/ai/2026-10-21-hankel-pencil-degree/application.py",
)
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
prior.squares.allowed_blocks = prior.extended_allowed_blocks


def source_formats(maximum):
    a = 2
    while a*a*(2*a-1) <= maximum:
        b = a
        while a*b*(a+b-1) <= maximum:
            yield a, b
            b += 1
        a += 1


def source_report(a, b):
    record = prior.squares.source_frontier(a, b, retain_dimensions=True)
    rows = record.pop("dimension_frontier")
    record["dimension_score_upper_numerators"] = [
        row["upper_score_numerator"] for row in rows
    ]
    record["maximum"]["lower_score_numerator"] = sum(
        prior.squares.score_interval(n)[0]
        for n in record["maximum"]["maximizing_relaxed_partition"]
    )
    record["linear_annihilator_gates"] = [
        {"rank": r, "symbol_image_cap": cap}
        for r in range(1, min(a, b))
        if (cap := prior.controls.symbol_cap(a, b, r)) is not None
    ]
    return record


def single_target():
    a, b, n = 8, 9, 30
    dimension = n*n
    allowed, _, _ = prior.extended_allowed_blocks(a, b, dimension)
    return {
        "source": [a, b], "source_leg_dimension": a*b*(a+b-1),
        "square_block": n, "target_leg_dimension": dimension,
        "loss_per_long_leg": a*b*(a+b-1)-dimension,
        "lift_rank_upper_bound": n+2*(a*b*(a+b-1)-dimension),
        "ordinary_necessary_tests_pass": n in allowed,
        "score_interval_numerators": list(prior.squares.score_interval(n)),
        "score_denominator": prior.squares.SCALE,
        "critical_score_threshold": (3*(a+b)-2)**3,
        "exact_improving_comparison": 180**9 > 49**12,
        "conditional_exponent": [5621, 2500],
        "conditional_integer_comparison": 180**5621 > 49**7500,
        "target_constructed": False, "improves_omega": False,
    }


def report(maximum=1377):
    records = [source_report(a, b) for a, b in source_formats(maximum)]
    records.sort(key=lambda r: (r["source_leg_dimension"], r["a"], r["b"]))
    passing = [r for r in records if not r["all_partitions_below_critical_score"]]
    return {
        "scope": "Ordinary restrictions over C to square matrix direct sums; 2<=a<=b; all target leg dimensions and all square partitions.",
        "maximum_source_dimension": maximum,
        "source_count": len(records),
        "dimensions_screened": sum(r["dimensions_screened"] for r in records),
        "score_denominator": prior.squares.SCALE,
        "first_surviving_source": [passing[0]["a"], passing[0]["b"]] if passing else None,
        "surviving_source_formats": [[r["a"], r["b"]] for r in passing],
        "source_frontiers": records,
        "unconstructed_single_target": single_target(),
        "singular_degenerations_excluded": False,
        "independent_review": False, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = report()
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Checked {result['source_count']} sources and {result['dimensions_screened']} target dimensions; first survivor {result['first_surviving_source']}.")
