"""Exact finite controls for the written one-regular-long-leg obstruction."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/one-regular-leg-2026-10-23/controls.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "1c04903c215f396150605c0778024e856ec0b0d4",
            "Changed source baseline")
    expected = {
        "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
        "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
        "research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md",
        "research/ai/2026-10-23-regular-unit-image/proof.md",
    }
    entries = record["local_dependencies"]
    require(len(entries) == len(expected) and {e["path"] for e in entries} == expected,
            "Changed source dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def polar_projection_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in range(1, 5):
        for k in range(1, 4):
            for order in (1, 2, 4):
                l = s.Matrix(r, k, lambda i, j: int(i == j))
                b = s.eye(r).row_join(t**(-order)*l)
                d = s.eye(r).col_join(s.zeros(k, r))
                kernel = (-l).col_join(t**order*s.eye(k))
                p = s.eye(r+k)-d*b
                require(b*d == s.eye(r) and p*p == p and b*p == s.zeros(r, r+k),
                        "Right inverse or kernel projection failed")
                require(p.rank() == k, "Incorrect generic kernel rank")
                require(any(s.expand(z).coeff(t, -order) != 0 for z in p),
                        "Expected a genuinely polar projection")
                z = s.eye(r)
                w = s.Matrix(k, r, lambda i, j: (i+1)*(j+1))
                y = d*z+kernel*w
                correction = (y-d*(b*y)).applyfunc(s.expand)
                require(b*y == z and correction == kernel*w,
                        "Regular correction identity failed")
                require(all(s.denom(v).subs(t, 0) != 0 for v in correction),
                        "Correction is not regular")
                leading = correction.subs(t, 0)
                require(leading.rank() <= k, "Specialized correction exceeds kernel rank")
                require(y.subs(t, 0) == d*z+leading, "Specialized output identity failed")
                records.append({"target_size": r, "defect": k, "pole_order": order,
                                "projection_rank": k, "correction_limit_rank": leading.rank()})
    return records


def vanishing_unit_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in (1, 2, 4):
        for order in (1, 3):
            b = (t**(-order)*s.eye(r)).row_join(s.zeros(r, 2))
            d = (t**order*s.eye(r)).col_join(s.zeros(2, r))
            p = (s.eye(r+2)-d*b).applyfunc(s.expand)
            require(b*d == s.eye(r) and d.subs(t, 0).rank() == 0,
                    "Zero-rank limiting unit control failed")
            require(p.rank() == 2 and p.subs(t, 0).rank() == 2,
                    "Vanishing unit lost the kernel projection")
            records.append({"target_size": r, "pole_order": order, "unit_limit_rank": 0,
                            "kernel_rank": 2})
    return records


def scalar_balancing_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for valuation in (-4, -1, 0, 2, 5):
        f = t**valuation*s.Matrix([[1+t, t], [0, 1-t]])
        b = s.Matrix([[1/t, 1], [0, t]])
        balanced = (t**(-valuation)*f).applyfunc(s.expand)
        require(balanced.subs(t, 0) != s.zeros(2), "Leading first map vanished")
        require((t**valuation*b*balanced-b*f).applyfunc(s.expand) == s.zeros(2),
                "Scalar balancing changed the output")
        records.append({"original_minimum_valuation": valuation, "balanced_limit_rank": 2,
                        "output_preserved": True})
    return records


def rank_budget_controls():
    # Isolated per-slice budgets, not examples satisfying the theorem's tensor hypotheses.
    records = []
    for rho in (1, 3, 11):
        for k in (1, 2, 3):
            n, r = rho+2*k, rho+k
            source = s.eye(n)
            c = s.eye(n)[:, :r]
            d = c
            target = s.diag(*([1]*rho+[0]*k))
            correction = source*c-d*target
            require(source.rank() == rho+2*k and (source*c).rank() == rho+k,
                    "Sharp column-loss control failed")
            require(target.rank() == rho and correction.rank() == k,
                    "Sharp target-plus-correction control failed")
            records.append({"target_slice_rank": rho, "defect": k,
                            "source_rank": source.rank(), "compressed_rank": (source*c).rank(),
                            "correction_rank": correction.rank()})
    return records


def a4_controls():
    path = ROOT / "research/ai/2026-10-20-koszul/cyclic_finite_target.py"
    spec = importlib.util.spec_from_file_location("one_regular_source", path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    # Literal coordinate slice: all nonzeros are distinct row/column pivots.
    f = [1]+[0]*111
    rows = [(j, p, ell) for j in range(4) for p in range(4) for ell in range(7)]
    columns = [(h, q, r) for h in range(7) for q in range(4) for r in range(4)]
    pivots = [(i, j) for i, row in enumerate(rows) for j, col in enumerate(columns)
              if source.slice_entry(f, 4, row, col)]
    require(len(pivots) == len({i for i, _ in pivots}) == len({j for _, j in pivots}) == 16,
            "Literal source coordinate rank changed")
    deleted = {j for _, j in pivots[:2]}
    require(sum(j not in deleted for _, j in pivots) == 14,
            "Actual source column-loss control failed")
    identity = s.zeros(110)
    generators = []
    for i in range(10):
        for j in range(10):
            pairs = [(11*i+a, 11*j+a) for a in range(11)]
            require(len({row for row, _ in pairs}) == len({col for _, col in pairs}) == 11,
                    "Target generator rank changed")
            generators.append({"matrix_unit": [i, j], "slice_rank": len(pairs)})
            if i == j:
                for row, col in pairs:
                    identity[row, col] += 1
    require(identity == s.eye(110), "Target diagonal generators do not give the unit")
    return {"source_dimension": 112, "source_minimum_from_written_proof": 16,
            "literal_coordinate_rank": len(pivots), "coordinate_rank_after_two_deletions": 14,
            "target_size": 110, "defect": 2, "target_generators": generators,
            "target_generator_rank": 11, "strict_rank_margin": 16-11-2*2,
            "unit_lift_rank_hypothesis": None,
            "both_balanced_long_maps_singular_excluded": False}


def report():
    return {"scope": "Finite exact controls; the arbitrary-series proof is written and unreviewed.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "polar_projections": polar_projection_controls(),
            "vanishing_units": vanishing_unit_controls(),
            "scalar_balancing": scalar_balancing_controls(),
            "isolated_rank_budgets": rank_budget_controls(), "a4": a4_controls()}


def verify(record):
    require(record == report(), "Changed finite controls, theorem scope or proof status")
    return {"polar_projection_controls": len(record["polar_projections"]),
            "vanishing_unit_controls": len(record["vanishing_units"]),
            "scalar_balancing_controls": len(record["scalar_balancing"]),
            "rank_budget_controls": len(record["isolated_rank_budgets"]),
            "target_generators": len(record["a4"]["target_generators"]),
            "strict_a4_rank_margin": record["a4"]["strict_rank_margin"],
            "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate finite controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
