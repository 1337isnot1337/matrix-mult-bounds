"""Exact controls for the stacked Laurent rank bound and rank105 consequence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/unit-image-stacked-rank-2026-10-23/controls.json"
BASE = "b407136ffc5abe194c3acf3b64d31517ed6a1e89"
DEPENDENCIES = (
    "research/ai/2026-10-23-unit-image-rank-gap/proof.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    entries = record["local_dependencies"]
    require(record["base_commit"] == BASE, "Changed source baseline")
    require(len(entries) == len(DEPENDENCIES) and
            {e["path"] for e in entries} == set(DEPENDENCIES),
            "Changed dependency inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def margins(a, m, n, retained):
    require(all(type(v) is int and v > 0 for v in (a, m, n, retained)) and
            a >= 2 and m >= 2, "Invalid dimensions")
    source, target = a*a*(2*a-1), m*n
    require(retained <= target <= source, "Invalid retained image")
    e, q, k = target-retained, source-retained, source-target
    gaps = {"first_pole": a*a-2*q, "kernel_rank_two": 2*n-q-e,
            "source_rank_locus": 2*a*a-n-2*q, "image_dimension": m*m-m-a*a}
    regular = all(value > 0 for value in gaps.values())
    return {"retained": retained, "target_defect": e, "source_defect": q,
            "strict_margins": gaps, "forces_regularity": regular,
            "kernel_rank_bound": (q+e)//n,
            "kernel_dimension_budget": m if q+e < 2*n else None,
            "first_image_dimension_floor": m*m-m if q+e < 2*n else None,
            "ordinary_rank_floor": a*a-2*k,
            "target_rank_one": n, "excludes_target": regular and n < a*a-2*k}


def stacked_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for q in range(1, 9):
        for h in (1, 2, 4):
            for pole in (1, 3):
                retained = 2*q
                left = (t**(-pole)*s.eye(q)).col_join(s.zeros(q))
                lower = t**(pole-h)*s.eye(q).row_join(s.zeros(q))
                upper = -left*lower
                matrix = upper.row_join(s.zeros(retained, q)).col_join(
                    lower.row_join(t**(-h)*s.eye(q)))
                regularized = (t**h*matrix).applyfunc(s.expand)
                require(all(s.denom(x).subs(t, 0) != 0 for x in regularized),
                        "Source pole was not cleared")
                leading = regularized.subs(t, 0)
                stacked = ((t**h)*(-left).col_join(s.eye(q))*lower).applyfunc(s.expand)
                require(stacked.subs(t, 0) == leading[:, :retained],
                        "Stacked leading coefficient mismatch")
                require(leading[:, :retained].rank() == q and leading.rank() == 2*q,
                        "Changed the sharp stacked rank budget")
                long_map = s.eye(retained).row_join(left)
                require(long_map*matrix[:, :retained] == s.zeros(retained),
                        "Negative source coefficients do not cancel")
                records.append({"inner_dimension": q, "source_pole_order": h,
                                "long_pole_order": pole, "first_columns_rank": q,
                                "source_leading_rank": 2*q})
    return records


def rank_one_kernel_controls():
    records = []
    for m in (2, 3, 10):
        variables = s.Matrix(1, m, s.symbols(f"x0:{m}"))
        unit = s.eye(m)[:, 0]
        common_column = unit*variables
        common_row = common_column.T
        require(common_column.rank() == common_row.rank() == 1,
                "Symbolic common-factor space has rank greater than one")
        bases = []
        for j in range(m):
            element = s.zeros(m)
            element[0, j] = 1
            bases.append(s.Matrix(1, m*m, list(element)))
        dimension = s.Matrix.vstack(*bases).rank()
        mixed = s.zeros(m)
        mixed[0, 0] = mixed[1, 1] = 1
        require(dimension == m and mixed.rank() == 2,
                "Rank-one space dimension or mixed-factor control failed")
        records.append({"matrix_size": m, "common_factor_dimension": dimension,
                        "generic_common_row_rank": 1, "generic_common_column_rank": 1,
                        "independent_both_factors_sum_rank": 2})
    return records


def report():
    cases = [margins(4, 10, 11, r) for r in range(110, 103, -1)]
    require([c["excludes_target"] for c in cases] == [True]*6+[False],
            "Changed the strict rank105 boundary")
    return {"scope": "Finite block controls, not cyclic degenerations or a formal Laurent proof.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pin_count": check_sources(), "a4_rank_margins": cases,
            "stacked_products": stacked_controls(),
            "rank_one_kernel_spaces": rank_one_kernel_controls()}


def verify(record):
    require(record == report(), "Changed evidence, scope or strict rank margins")
    return {"stacked_products": len(record["stacked_products"]),
            "rank_one_kernel_spaces": len(record["rank_one_kernel_spaces"]),
            "a4_rank_cases": len(record["a4_rank_margins"]),
            "lowest_excluded_unit_image_rank": 105, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
