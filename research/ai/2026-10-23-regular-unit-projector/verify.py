"""Exact controls for the written regular-right-inverse Laurent argument.

Finite matrix controls do not formalize all series or prove a degeneration.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/regular-unit-projector-2026-10-23/controls.json"
BASE = "1c04903c215f396150605c0778024e856ec0b0d4"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-23-regular-unit-image/proof.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == BASE, "Changed source baseline")
    require(record["field"] == "C" and record["external_theorems_added"] is False,
            "Changed source field or external dependency scope")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {entry["path"] for entry in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def margins(*, source_dimension, matrix_dimension, target_dimension,
            parameter_dimension, source_minimum, row_minimum,
            target_minimum, retained):
    values = (source_dimension, matrix_dimension, target_dimension,
              parameter_dimension, source_minimum, row_minimum,
              target_minimum, retained)
    require(all(type(x) is int and x > 0 for x in values), "Invalid dimension")
    require(retained <= target_dimension <= matrix_dimension,
            "Invalid unit-image dimension")
    require(source_minimum <= matrix_dimension
            and row_minimum <= min(source_dimension, matrix_dimension)
            and target_minimum <= target_dimension, "Impossible rank bound")
    k = matrix_dimension - target_dimension
    q = matrix_dimension - retained
    strict = {
        "first_pole": source_minimum - 2*k,
        "first_injectivity": target_minimum - q,
        "row_kernel_dimension": parameter_dimension-source_dimension+row_minimum-k,
    }
    return {"retained": retained, "long_defect": k, "unit_image_defect": q,
            "strict_margins": strict,
            "forces_first_regularity": strict["first_pole"] > 0,
            "forces_all_regularity": all(x > 0 for x in strict.values())}


def zero(matrix):
    return matrix.applyfunc(s.cancel) == s.zeros(*matrix.shape)


def valuation(matrix, t):
    return min(int(s.cancel(x).as_leading_term(t).as_powers_dict().get(t, 0))
               for x in matrix if x != 0)


def projector_controls():
    """Singular regular right inverses, polar projectors, and rank-safe limits."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for k in range(1, 4):
        for missing in range(1, 4):
            r = k + missing + 1
            n = r + k
            diagonal = s.diag(*[t**(i+1) if i < missing else 1 for i in range(r)])
            # A constant source shear prevents reliance on diagonal frame ordering.
            frame = s.eye(n)
            frame[n-1, 0] = 2
            tail = s.Matrix(r, k, lambda i, j: (i+j+1)/t**(missing+j+2))
            right_inverse = frame * diagonal.col_join(s.zeros(k, r))
            b = diagonal.inv().row_join(tail) * frame.inv()
            p = s.eye(n) - right_inverse*b
            require(zero(b*right_inverse-s.eye(r)), "Right inverse identity failed")
            require(zero(p*p-p) and p.rank() == k, "Projector identity/rank failed")
            require(valuation(right_inverse, t) >= 0 and valuation(p, t) < 0,
                    "Lost regular inverse or polar projector control")
            require(right_inverse.subs(t, 0).rank() == r-missing,
                    "Wrong singular right-inverse rank")
            kernel = frame * (-diagonal*tail).col_join(s.eye(k))
            w = s.eye(r)[:k, :]
            y = right_inverse + kernel*w
            z = b*y
            require(zero(z-s.eye(r)), "Regular target identity failed")
            require(zero(p*y-y+right_inverse*z), "Product regularization failed")
            order = -valuation(y, t)
            require(order > 0, "Missing first-pole control")
            leading_y = (t**order*y).applyfunc(s.cancel).subs(t, 0)
            leading_product = (t**order*p*y).applyfunc(s.cancel).subs(t, 0)
            require(zero(leading_y-leading_product) and leading_y.rank() <= k,
                    "Regularized leading-rank bound failed")
            records.append({"long_defect": k, "target_dimension": r,
                            "unit_image_rank": r-missing, "pole_order": order,
                            "projector_rank": k, "regularized_rank": leading_y.rank()})
    return records


def raw_coefficient_control():
    t = s.Symbol("t", nonzero=True)
    inverse = s.Matrix([t, 0])
    b = s.Matrix([[1/t, 1/t**2]])
    p = s.eye(2)-inverse*b
    y = s.Matrix([[0, 0], [1, t]])
    product = p*y
    raw = product.applyfunc(lambda x: s.expand(x).coeff(t, 0))
    leading = (t*product).applyfunc(s.cancel).subs(t, 0)
    require(zero(b*inverse-s.eye(1)) and p.rank() == 1, "Invalid polar control")
    require(raw.rank() == 2 and leading.rank() == 1,
            "Raw constant and regularized leading coefficient were conflated")
    return {"projector_rank": 1, "raw_constant_rank": 2, "regularized_rank": 1}


def source_rank_controls():
    records = []
    for k in range(1, 6):
        r, n = 2*k+1, 3*k+1
        x = s.zeros(n)
        for j in range(k):
            x[j, j] = 1
            x[k+j, r+j] = 1
        c = s.eye(n)[:, :r]
        require(c.rank() == r and (x*c).rank() == k and x.rank() == 2*k,
                "Sharp source restriction rank budget failed")
        records.append({"long_defect": k, "restricted_rank": k, "full_rank": 2*k})
    return records


def target_boundary_controls():
    records = []
    # On the first 11-dimensional target block, deleting e directions from
    # T(0) leaves exactly 11-e; all other blocks of Xi(E_11) are zero.
    for retained in (103, 102, 101, 100):
        missing = 110-retained
        xi = s.eye(11)
        t0_block = s.diag(*([0]*missing + [1]*(11-missing)))
        rank = (t0_block*xi).rank()
        require(rank == 11-missing, "Target one-sided rank loss failed")
        records.append({"unit_image_rank": retained, "target_slice_rank": 11,
                        "product_rank": rank, "long_defect": 2,
                        "forces_nonzero_lift": rank > 2})
    require(records[1]["product_rank"] == 3 and records[2]["product_rank"] == 2,
            "Lost the exact rank102/rank101 boundary")
    return records


def row_contraction_controls():
    records = []
    for k in range(5):
        d, n = 3*k+5, 2*k+5
        r, mu = n-k, k+3
        contraction = s.zeros(n, d)
        for j in range(3):
            contraction[j, j] = 1
        for j in range(k):
            contraction[r+j, 3+j] = 1
        c = s.eye(n)[:, :r]
        restricted = c.T*contraction
        require(contraction.rank() == mu and restricted.rank() == mu-k,
                "Source-row contraction rank loss failed")
        kernel = restricted.nullspace()
        require(len(kernel) == d-mu+k, "Source-row kernel dimension failed")
        require(all(zero(restricted*v) for v in kernel), "Invalid kernel witness")
        records.append({"long_defect": k, "source_dimension": d,
                        "row_contraction_rank": mu, "restricted_rank": mu-k,
                        "kernel_dimension": len(kernel)})
    return records


def report():
    common = dict(source_dimension=112, matrix_dimension=112, target_dimension=110,
                  parameter_dimension=100, source_minimum=16, row_minimum=16,
                  target_minimum=11)
    cases = [margins(**common, retained=r) for r in range(110, 99, -1)]
    require([c["forces_all_regularity"] for c in cases] == [True]*9+[False]*2,
            "Changed the A4 sufficient threshold")
    return {"scope": "Finite exact controls; all-order proof is written and unreviewed.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "a4_rank_margins": cases, "ordinary_rank_floor": 12,
            "target_rank_one_slice": 11, "polar_projectors": projector_controls(),
            "raw_coefficient_negative_control": raw_coefficient_control(),
            "source_rank_budgets": source_rank_controls(),
            "target_injectivity_boundary": target_boundary_controls(),
            "row_contraction_budgets": row_contraction_controls()}


def verify(record):
    require(record == report(), "Changed controls, hypotheses or evidence status")
    return {"polar_projectors": len(record["polar_projectors"]),
            "source_rank_budgets": len(record["source_rank_budgets"]),
            "target_boundary_controls": len(record["target_injectivity_boundary"]),
            "row_contraction_budgets": len(record["row_contraction_budgets"]),
            "a4_rank_cases": len(record["a4_rank_margins"]),
            "minimum_sufficient_unit_image_rank": 102, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate exact controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
