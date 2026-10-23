"""Finite source controls for the written highest-pole flag restrictions."""
from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/unit-image-pole-flags-2026-10-23/controls.json"
SCOPE = "Necessary highest-pole flags only; no lower-pole or target construction claim."
DEPENDENCIES = {
    "research/ai/2026-10-23-one-sided-unit-image/proof.md",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "c5aab5b503bb48625ccdf83fec1ab2a4d43cfde0",
            "Changed research baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        require(hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
                == entry["sha256"], "Source pin mismatch: " + entry["path"])
    return len(entries)


def source_matrix(f, a=4):
    """Rebuild all coefficients from the six original short factor indices."""
    m, n = 2*a-1, a*a*(2*a-1)
    require(len(f) == n, "Wrong first-leg coefficient count")
    entries = {}
    for i, j, p, q, r, z in product(range(a), repeat=6):
        value = f[(i*m+p+q)*a+z]
        if value:
            row = (j*a+p)*m+r+z
            column = ((i+j)*a+q)*a+r
            entries[row, column] = value
    return s.SparseMatrix(n, n, entries)


def factored(u, alpha, beta, v):
    return [u[i]*alpha**(6-k)*beta**k*v[z]
            for i, k, z in product(range(4), range(7), range(4))]


def rank(matrix):
    return matrix.to_DM().rank()


def ruling_controls():
    records = []
    fixed = (1, 2, 0, -1)
    for alpha, beta in ((1, 0), (0, 1), (1, 1), (1, 2)):
        for side in ("left", "right"):
            basis = []
            for i in range(4):
                unit = tuple(int(i == j) for j in range(4))
                u, v = (unit, fixed) if side == "left" else (fixed, unit)
                basis.append(factored(u, alpha, beta, v))
            require(rank(s.Matrix.hstack(*(s.Matrix(f) for f in basis))) == 4,
                    "The purported ruling has dimension below four")
            ranks = []
            for t in (-1, 0, 2):
                coefficients = (1, t, t*t, 1-t)
                f = [sum(c*column[j] for c, column in zip(coefficients, basis))
                     for j in range(112)]
                ranks.append(rank(source_matrix(f)))
            require(ranks == [16]*3, "Minimum-rank ruling control failed")
            records.append({"variable_short_factor": side, "alpha": alpha,
                            "beta": beta, "fixed_short_factor": list(fixed),
                            "coefficient_parameters": [-1, 0, 2],
                            "dimension": 4, "source_ranks": ranks})
    return records


def controls():
    e0, e1 = (1, 0, 0, 0), (0, 1, 0, 0)
    f0 = factored(e0, 1, 0, e0)
    f1 = factored(e1, 1, 0, e1)
    mixed_short_rank = rank(source_matrix([x+y for x, y in zip(f0, f1)]))
    other_hankel = factored(e0, 0, 1, e0)
    mixed_hankel_rank = rank(source_matrix([x+y for x, y in zip(f0, other_hankel)]))
    require((mixed_short_rank, mixed_hankel_rank) == (20, 32),
            "The excluded two-factor pencils have changed source ranks")

    matrix = source_matrix(f0)
    pivots = sorted(matrix.todok())
    require(len(pivots) == 16 and len({i for i, j in pivots}) == 16
            and len({j for i, j in pivots}) == 16,
            "Minimum source slice is not a partial permutation")
    last_rows = {i for i, j in pivots[:6]}
    last_columns = {j for i, j in pivots[6:12]}
    rows = [i for i in range(112) if i not in last_rows]
    columns = [j for j in range(112) if j not in last_columns]
    block_ranks = [rank(matrix.extract(rows, columns)),
                   rank(matrix.extract(range(112), columns)), rank(matrix)]
    require(block_ranks == [4, 10, 16], "Lost the rank106 block-budget survivor")
    return {"mixed_short_factor_source_rank": mixed_short_rank,
            "mixed_hankel_profile_source_rank": mixed_hankel_rank,
            "rank106_block_budget_survivor": {
                "deleted_rows": sorted(last_rows), "deleted_columns": sorted(last_columns),
                "retained_dimension": 106, "block_ranks": block_ranks,
                "unit_frame_compatibility_claimed": False,
                "target_constructed": False}}


def report():
    return {"scope": SCOPE, "proof_status": "proof-written-unreviewed",
            "improves_omega": False, "source_pin_count": check_sources(),
            "a4_leading_image_dimension_bounds": [
                {"unit_image_rank": r, "source_defect": 112-r,
                 "source_rank_budget": 3*(112-r),
                 "leading_image_dimension_bound": 4 if r == 106 else 16,
                 "first_map_must_be_polar": r == 106}
                for r in range(106, 101, -1)],
            "ruling_controls": ruling_controls(), "source_controls": controls()}


def verify(record):
    require(record == report(), "Changed pole scope, source controls or boundary")
    return {"unit_image_rank_cases": 5, "ruling_families": 8,
            "literal_minimum_source_ranks": 24, "source_countercontrols": 3,
            "improves_omega": False}


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
