"""Exact finite controls for the written partial-unit-image Laurent theorem.

This program does not formalize the proof or enumerate formal degenerations.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/regular-unit-image-2026-10-23/controls.json"
SCOPE = "Finite exact matrix controls; all-order result is written and unreviewed."


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "539b539dc4eac09114899fd76472aee2d78d9f62",
            "Changed source baseline")
    expected = {
        "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
        "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
        "research/ai/2026-10-21-cyclic-slice-determinants/unital_chart.md",
    }
    entries = record["local_dependencies"]
    require(len(entries) == len(expected) and {e["path"] for e in entries} == expected,
            "Changed source dependency inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def margins(*, source_dimension, matrix_dimension, target_dimension,
            parameter_dimension, source_minimum, row_minimum,
            target_minimum, retained):
    """Evaluate only the sufficient regularity inequalities in the proof."""
    values = (source_dimension, matrix_dimension, target_dimension,
              parameter_dimension, source_minimum, row_minimum,
              target_minimum, retained)
    require(all(type(v) is int and v > 0 for v in values), "Invalid dimension")
    require(retained <= target_dimension <= matrix_dimension, "Invalid retained image")
    e = target_dimension - retained
    q = matrix_dimension - retained
    differences = {
        "first_pole": source_minimum - 3*q,
        "first_injectivity": target_minimum - 2*e - q,
        "row_kernel_dimension": parameter_dimension - source_dimension + row_minimum - q,
    }
    return {"retained": retained, "target_defect": e, "source_defect": q,
            "strict_margins": differences,
            "forces_regularity": all(v > 0 for v in differences.values())}


def recovery_controls():
    """Recover every bottom Laurent row using e+1 distinct left inverses."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in range(1, 5):
        for e in range(1, 5):
            h = s.eye(r + e)[:, :r]
            p0 = h.T
            top = s.Matrix(r, 3, lambda i, j: (i+1)*t + j)
            bottom = s.Matrix(e, 3, lambda i, j: (j+1)/t**(i+1) + i)
            whole = top.col_join(bottom)
            require(p0*h == s.eye(r), "Invalid base left inverse")
            require(p0*whole == top, "Top row recovery failed")
            projected_poles = 0
            for j in range(e):
                p = p0.copy()
                p[0, r+j] = 1
                require(p*h == s.eye(r), "Invalid varied left inverse")
                recovered = (p-p0)*whole
                require(recovered[0, :] == bottom[j, :], "Bottom row recovery failed")
                require(recovered[1:, :] == s.zeros(r-1, 3), "Unexpected recovered rows")
                projected_poles += int(any(z.as_leading_term(t).as_powers_dict().get(t, 0) < 0
                                           for z in (p*whole)[0, :]))
            require(projected_poles == e, "A varied projection missed the hidden pole")
            records.append({"retained": r, "missing": e, "left_inverses": e+1,
                            "hidden_pole_rows_recovered": projected_poles})
    return records


def rank_controls():
    """Sharp small matrices for the three rank losses in the proof."""
    records = []
    for q in range(1, 5):
        n, r = 4*q, 3*q
        x = s.zeros(n)
        for j in range(q):
            x[j, j] = 1
            x[r+j, q+j] = 1
            x[q+j, r+j] = 1
        ranks = [x[:r, :r].rank(), x[:, :r].rank(), x.rank()]
        require(ranks == [q, 2*q, 3*q], "Three-part leading-slice budget failed")
        records.append({"kind": "leading_slice", "defect": q, "ranks": ranks})
    for e in range(4):
        # A rank-(2e+1) permutation slice loses exactly e rows and e columns.
        r, n = 2*e+1, 3*e+1
        x = s.zeros(n)
        for j in range(e):
            x[j, r+j] = 1
            x[r+j, e+j] = 1
        x[2*e, 2*e] = 1
        original, compressed = x.rank(), x[:r, :r].rank()
        require(original == 2*e+1 and compressed == 1,
                "Two-sided compression loss failed")
        records.append({"kind": "two_sided_compression", "defect": e,
                        "ranks": [original, compressed], "loss": 2*e})
    return records


def regularized_product_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for q in range(1, 5):
        left = s.zeros(2*q, q)
        right = s.zeros(q, 2*q)
        for j in range(q):
            left[j, j] = 1/t
            left[q+j, j] = 1
            right[j, j] = 1
            right[j, q+j] = t
        product = left*right
        raw_constant = product.applyfunc(lambda z: s.expand(z).coeff(t, 0))
        regularized = (t*product).applyfunc(s.expand)
        require(all(s.denom(z).subs(t, 0) != 0 for z in regularized),
                "Product was not regularized")
        leading = regularized.subs(t, 0)
        require(leading.rank() == q and raw_constant.rank() == 2*q,
                "Raw constant/regularized coefficient distinction failed")
        records.append({"inner_dimension": q, "raw_constant_rank": 2*q,
                        "regularized_leading_rank": q})
    return records


def singular_unit_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in range(1, 5):
        target, n = r+1, r+3
        unit = s.eye(n)
        unit[r, r] = t
        c = s.eye(n)[:, :target]
        b = c.T
        b[r, r] = 1/t
        h = s.eye(target)[:, :r]
        p0 = h.T
        p1 = p0.copy()
        p1[0, r] = 1
        require(b*unit*c == s.eye(target), "Exact singular unit identity failed")
        require(unit.subs(t, 0).rank() == n-1, "Unit is not corank one")
        require((unit*c).subs(t, 0).rank() == r, "Unit-image rank incorrect")
        require(p0*b == s.eye(n)[:r, :], "Fixed projection did not hide the pole")
        require((p1*b)[0, r] == 1/t, "Varied projection did not detect the pole")
        records.append({"matrix_dimension": n, "long_dimension": target,
                        "unit_corank": 1, "unit_image_rank": r,
                        "one_projection_hides_pole": True,
                        "varied_projection_detects_pole": True})
    return records


def report():
    common = dict(source_dimension=112, matrix_dimension=112,
                  target_dimension=110, parameter_dimension=100,
                  source_minimum=16, row_minimum=16, target_minimum=11)
    cases = [margins(**common, retained=r) for r in (110, 109, 108)]
    require([x["forces_regularity"] for x in cases] == [True, True, False],
            "The rank-108 boundary must remain open to this argument")
    require(cases[-1]["strict_margins"]["row_kernel_dimension"] == 0,
            "Lost the strict dimension boundary")
    return {"scope": SCOPE, "proof_status": "proof-written-unreviewed",
            "improves_omega": False, "source_pin_count": check_sources(),
            "a4_rank_margins": cases, "ordinary_rank_floor": 12,
            "target_rank_one_slice": 11,
            "projection_recovery": recovery_controls(),
            "rank_budgets": rank_controls(),
            "regularized_products": regularized_product_controls(),
            "singular_units_without_source_rank_hypotheses": singular_unit_controls()}


def verify(record):
    require(record == report(), "Changed controls, scope or rank hypotheses")
    return {"projection_families": len(record["projection_recovery"]),
            "rank_budget_controls": len(record["rank_budgets"]),
            "regularized_product_controls": len(record["regularized_products"]),
            "singular_unit_controls": len(record["singular_units_without_source_rank_hypotheses"]),
            "a4_rank_cases": len(record["a4_rank_margins"]),
            "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate finite controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
