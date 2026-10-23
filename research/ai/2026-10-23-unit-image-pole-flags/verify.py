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
SCOPE = "Finite source and pole-factor controls; no full chart closure or target construction."
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


def contraction_controls():
    """Canonical row contractions; input coefficients index rows, outputs columns."""
    u, v = (1, 2, 0, -1), (2, 0, -1, 1)
    records = []
    for alpha, beta in ((1, 0), (0, 1), (1, 1), (1, 2)):
        entries = {}
        for i, j, p, q, r, z in product(range(4), repeat=6):
            value = u[j]*v[p]*alpha**(6-r-z)*beta**(r+z)
            if value:
                entries[(i*7+p+q)*4+z, ((i+j)*4+q)*4+r] = value
        actual = s.SparseMatrix(112, 112, entries)
        mu = multiplication(u)
        lv = s.SparseMatrix(4, 7, {(q, p+q): v[p]
                                  for p, q in product(range(4), repeat=2)})
        w = s.Matrix([alpha**(3-i)*beta**i for i in range(4)])
        expected = s.kronecker_product(mu.T, lv.T, s.SparseMatrix(w*w.T))
        require(actual == expected and rank(actual) == 16,
                "Literal row contraction does not match its support factors")
        records.append({"alpha": alpha, "beta": beta,
                        "left_cubic": list(u), "right_cubic": list(v),
                        "rank": 16, "all_entries_match_factorization": True})
    return {"factorizations": records}


def multiplication(coefficients):
    return s.SparseMatrix(7, 4, {(i+j, i): coefficients[j]
                                for i, j in product(range(4), repeat=2)})


def gaussian_polar_control():
    """One polar factor can have higher-rank raw negative coefficients."""
    t = s.Symbol("t", nonzero=True)
    c = s.Matrix([1, t, t*t, 1+t])
    ell = s.Matrix([[1+t, t, 1, t*t, 0]])
    regular = s.zeros(4, 5)
    for i in range(1, 4):
        regular[i, i] = t**(i-1)
    matrix = regular + c*ell/t**3
    pivot_column = (matrix[:, 0]/matrix[0, 0]).applyfunc(s.cancel)
    residual = (matrix-pivot_column*matrix[0, :]).applyfunc(s.cancel)
    require(pivot_column == c and residual == regular,
            "Regular Gaussian row elimination did not isolate the polar factor")
    coefficient_ranks = [rank(matrix.applyfunc(lambda z: s.expand(z).coeff(t, -j)))
                         for j in (3, 2, 1)]
    require(coefficient_ranks == [1, 2, 3], "Lost the raw negative-rank countercontrol")
    return {"pole_order": 3, "raw_negative_coefficient_ranks": coefficient_ranks,
            "one_rank_one_polar_term": True, "gaussian_residual_regular": True,
            "actual_source_or_target_claimed": False}


def unit_slice_budget_controls():
    """Sharp abstract rank losses; these are not source-unit trajectories."""
    n, r = 24, 22
    unit = s.eye(n)
    unit.row_swap(0, 2)
    unit.row_swap(1, 3)
    source_slice = s.diag(*([1]*16+[0]*8))
    records = []
    for m in range(1, 5):
        deleted = set(range(2, 4+m))
        keep = [j for j in range(n) if j not in deleted]
        regular = s.eye(n).extract(keep, range(n)).col_join(s.zeros(m, n))
        unit_columns = keep + sorted(deleted-{2, 3})
        column = unit.T[:, unit_columns]
        unit_residue = s.eye(r)-regular*unit*column
        unit_rank, slice_rank = rank(unit_residue), rank(regular*source_slice*column)
        require(rank(regular) == r-m and unit_rank == m and slice_rank == 12-m,
                "Unit/slice rank-loss control failed")
        require(slice_rank > m, "The first-pole contradiction must stay strict")
        records.append({"polar_rank_cap": m, "source_slice_rank": 16,
                        "long_defect": 2, "regular_unit_rank": r-m,
                        "unit_residue_rank": unit_rank, "compressed_slice_rank": slice_rank,
                        "strict_rank_margin": slice_rank-m,
                        "actual_source_unit_trajectory_claimed": False})
    return records


def report():
    return {"scope": SCOPE, "proof_status": "proof-written-unreviewed",
            "improves_omega": False, "source_pin_count": check_sources(),
            "a4_leading_image_dimension_bounds": [
                {"unit_image_rank": r, "source_defect": 112-r,
                 "source_rank_budget": 3*(112-r),
                 "leading_image_dimension_bound": 4 if r == 106 else 16,
                 "first_map_must_be_polar": r == 106}
                for r in range(106, 101, -1)],
            "ruling_controls": ruling_controls(), "source_controls": controls(),
            "contraction_controls": contraction_controls(),
            "small_principal_budgets": [
                {"principal_rank": p, "regular_parameter_dimension": 100-p,
                 "full_row_contraction_rank_upper": 14+p,
                 "minimum_rank_forced_by_gap": 14+p < 20,
                 "polar_long_map_rank_cap": 4 if p <= 5 else None,
                 "excluded_by_unit_slice_budget": p <= 5}
                for p in range(2, 7)],
            "gaussian_polar_control": gaussian_polar_control(),
            "unit_slice_budget_controls": unit_slice_budget_controls()}


def verify(record):
    require(record == report(), "Changed pole scope, source controls or boundary")
    return {"unit_image_rank_cases": 5, "ruling_families": 8,
            "literal_minimum_source_ranks": 24, "source_countercontrols": 3,
            "literal_row_factorizations": 4, "principal_rank_cases": 5,
            "gaussian_polar_controls": 1,
            "unit_slice_budget_controls": 4,
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
