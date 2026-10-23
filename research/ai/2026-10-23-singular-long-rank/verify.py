"""Exact controls for the written singular-long-leg rank-gap obstruction.

Only the Python standard library is needed. The all-series result rests on
proof.md and its pinned prior rank-gap theorem, not on these finite controls.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/singular-long-rank-2026-10-23/controls.json"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def zeros(rows, columns):
    return [[0 for _ in range(columns)] for _ in range(rows)]


def identity(size):
    return [[int(i == j) for j in range(size)] for i in range(size)]


def multiply(a, b):
    require(bool(a) and bool(b) and len(a[0]) == len(b), "Incompatible product")
    result = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value:
                for ell, right in enumerate(b[j]):
                    if right:
                        result[i][ell] += value * right
    return result


def subtract(a, b):
    require(len(a) == len(b) and len(a[0]) == len(b[0]), "Incompatible difference")
    return [[x-y for x, y in zip(left, right)] for left, right in zip(a, b)]


def rank(matrix):
    """Exact rational elimination, with zero rows and columns removed first."""
    nonzero = [row for row in matrix if any(row)]
    if not nonzero:
        return 0
    columns = [j for j in range(len(nonzero[0])) if any(row[j] for row in nonzero)]
    work = [[Fraction(row[j]) for j in columns] for row in nonzero]
    pivot_row = 0
    for column in range(len(columns)):
        candidate = next((i for i in range(pivot_row, len(work)) if work[i][column]), None)
        if candidate is None:
            continue
        work[pivot_row], work[candidate] = work[candidate], work[pivot_row]
        pivot = work[pivot_row][column]
        for i in range(pivot_row+1, len(work)):
            if work[i][column]:
                scale = work[i][column] / pivot
                for j in range(column, len(columns)):
                    work[i][j] -= scale * work[pivot_row][j]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "1c04903c215f396150605c0778024e856ec0b0d4",
            "Changed source baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES) and {entry["path"] for entry in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    predecessor = record["concurrent_predecessor"]
    require(predecessor["pr"] == 113 and
            predecessor["commit"] == "08ac3e983e270cf3df4e26d960ceb16415f7ef31" and
            predecessor["path"] == "research/ai/2026-10-23-one-regular-leg/proof.md",
            "Changed unit-kernel predecessor")
    return len(entries)


def source_matrix(terms, maintained):
    coefficients = {tuple(item[:3]): item[3] for item in terms}
    require(len(coefficients) == len(terms), "Repeated source parameter coordinate")
    rows = [(j, p, ell) for j in range(4) for p in range(4) for ell in range(7)]
    columns = [(h, q, r) for h in range(7) for q in range(4) for r in range(4)]
    parameter = [coefficients.get((i, k, s), 0)
                 for i in range(4) for k in range(7) for s in range(4)]
    matrix = [[coefficients.get((h-j, p+q, ell-r), 0)
               for h, q, r in columns] for j, p, ell in rows]
    for i, row in enumerate(rows):
        for j, column in enumerate(columns):
            require(matrix[i][j] == maintained.slice_entry(parameter, 4, row, column),
                    "Literal source differs from the maintained convention")
    return matrix


def source_controls():
    path = ROOT / "research/ai/2026-10-20-koszul/cyclic_finite_target.py"
    spec = importlib.util.spec_from_file_location("singular_long_source", path)
    maintained = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(maintained)
    factors = [([int(i == j) for i in range(4)], [1]+[0]*6, [1, 0, 0, 0])
               for j in range(4)]
    factors += [([1, -2, 3, -4], [1]+[0]*6, [1, 0, 0, 0]),
                ([1, 2, 0, -1], [2**j for j in range(7)], [1, 0, 2, 3]),
                ([1, 0, -1, 2], [0]*6+[1], [2, 1, 0, -1])]
    records = []
    for u, h, v in factors:
        terms = [[i, k, ell, u[i]*h[k]*v[ell]]
                 for i in range(4) for k in range(7) for ell in range(4)
                 if u[i]*h[k]*v[ell]]
        value = rank(source_matrix(terms, maintained))
        hankel_rank = rank([[h[i+j] for j in range(4)] for i in range(4)])
        require(value == 16 and hankel_rank == 1, "Minimum source control failed")
        records.append({"parameter_terms": terms, "source_rank": value,
                        "middle_hankel_rank": hankel_rank})
    next_terms = [[0, 0, 0, 1], [1, 0, 1, 1]]
    next_rank = rank(source_matrix(next_terms, maintained))
    require(next_rank == 20, "First source rank above the gap changed")
    return {"minimum_cases": records,
            "next_rank_case": {"parameter_terms": next_terms, "source_rank": next_rank},
            "literal_coefficients_per_case": 112*112,
            "coefficient_comparisons": (len(records)+1)*112*112}


def ruling_control(m, n, qrank, b):
    require(len(b) == m and any(b), "A ruling vector must be nonzero")
    require(0 <= qrank <= n, "Invalid image rank")
    right = zeros(n, m*n)
    for i, value in enumerate(b):
        for j in range(n):
            right[j][i*n+j] = value
    pivot = next(i for i, value in enumerate(b) if value)
    section = zeros(m*n, n)
    for j in range(n):
        section[pivot*n+j][j] = Fraction(1, b[pivot])
    q = zeros(n+3, n)
    for i in range(qrank):
        q[i][i] = i+1
    product = multiply(q, right)
    require(multiply(right, section) == identity(n), "Ruling factor is not surjective")
    require(multiply(product, section) == q, "Ruling right inverse failed")
    require(rank(product) == rank(q) == qrank, "Ruling changed the fixed-left image rank")
    return {"matrix_size": m, "multiplicity": n, "b": b, "fixed_image_rank": qrank,
            "product_rank": rank(product), "right_inverse_verified": True}


def ruling_controls():
    return [ruling_control(*args) for args in (
        (10, 11, 2, [1]+[0]*9),
        (10, 11, 8, [0, 2, -1]+[0]*7),
        (10, 11, 11, list(range(1, 11))),
        (3, 2, 1, [0, -2, 3]),
        (3, 2, 2, [2, 0, 1]),
        (2, 1, 1, [0, -3]),
    )]


def singular_column_budgets():
    # These matrices check the isolated rank losses. They are not source
    # slices or tensor degenerations satisfying all theorem hypotheses.
    records = []
    for defect in range(6):
        source = zeros(112, 112)
        for i in list(range(13+defect))+[110, 111]:
            source[i][i] = 1
        column = zeros(112, 110)
        for i in range(defect, 110):
            column[i][i] = 1
        y = multiply(source, column)
        target = zeros(110, 110)
        for i in range(defect, defect+11):
            target[i][i] = 1
        d = y
        correction = subtract(y, multiply(d, target))
        values = {"long_defect": defect, "long_limit_rank": rank(column),
                  "source_matrix_rank": rank(source), "compressed_rank": rank(y),
                  "target_rank": rank(target), "correction_rank": rank(correction)}
        require(values == {"long_defect": defect, "long_limit_rank": 110-defect,
                           "source_matrix_rank": 15+defect, "compressed_rank": 13,
                           "target_rank": 11, "correction_rank": 2},
                "Singular-column rank budget changed")
        records.append(values)
    return records


def threshold(defect):
    require(isinstance(defect, int) and 0 <= defect <= 110, "Invalid long-leg defect")
    upper = 11+2*2+defect
    active_lower = 16-2*2-defect
    return {"long_defect": defect, "long_limit_rank": 110-defect,
            "source_rank_upper": upper, "next_source_rank": 20,
            "strict_gap_margin": 20-upper, "active_image_rank_lower": active_lower,
            "correction_rank_upper": 2, "strict_ruling_margin": active_lower-2,
            "excluded_by_written_gap_ruling_theorem": upper < 20 and active_lower > 2}


def report():
    return {"scope": "Exact finite controls for the written all-series proof; no general degeneration search.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "source_controls": source_controls(), "ruling_controls": ruling_controls(),
            "isolated_singular_column_budgets": singular_column_budgets(),
            "thresholds": [threshold(c) for c in range(6)],
            "source_minimum_pure_tensor_format": [4, 7, 4],
            "pure_tensor_linear_space_bound_from_written_lemma": 7,
            "target_ruling_dimension": 10,
            "remaining_balanced_long_rank_upper": 105,
            "rank105_long_limits_excluded": False}


def verify(record):
    require(record == report(), "Changed controls, source scope, threshold or proof status")
    return {"source_slice_controls": len(record["source_controls"]["minimum_cases"])+1,
            "literal_source_coefficients_checked": record["source_controls"]["coefficient_comparisons"],
            "ruling_controls": len(record["ruling_controls"]),
            "isolated_rank_budget_controls": len(record["isolated_singular_column_budgets"]),
            "excluded_defects": [entry["long_defect"] for entry in record["thresholds"]
                                 if entry["excluded_by_written_gap_ruling_theorem"]],
            "remaining_balanced_long_rank_upper": 105, "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the finite controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
