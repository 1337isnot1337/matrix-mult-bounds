"""Exact finite controls for one-sided partial-unit Laurent regularity."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/one-sided-unit-image-2026-10-23/controls.json"
SCOPE = "Finite exact rank controls; the all-order proof is written and unreviewed."
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
    "research/ai/2026-10-23-regular-unit-image/proof.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "1c04903c215f396150605c0778024e856ec0b0d4",
            "Changed research baseline")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    return len(entries)


def margins(*, source_dimension, matrix_dimension, target_dimension,
            parameter_dimension, source_minimum, row_minimum,
            target_minimum, retained):
    values = (source_dimension, matrix_dimension, target_dimension,
              parameter_dimension, source_minimum, row_minimum,
              target_minimum, retained)
    require(all(type(v) is int and v > 0 for v in values), "Invalid dimension")
    require(retained <= target_dimension <= matrix_dimension, "Invalid unit image")
    k = matrix_dimension - target_dimension
    e = target_dimension - retained
    q = matrix_dimension - retained
    strict = {
        "first_pole": source_minimum - 3*q,
        "first_injectivity": target_minimum - e - q,
        "full_row_kernel_dimension": parameter_dimension - source_dimension + row_minimum - k,
    }
    return {"retained": retained, "target_defect": e, "source_defect": q,
            "long_map_defect": k, "strict_margins": strict,
            "forces_regularity": all(v > 0 for v in strict.values())}


def rank(matrix):
    """Exact rank over the matrix coefficient domain."""
    return matrix.to_DM().rank()


def one_sided_controls():
    """A genuine matrix target slice loses exactly e under column deletion."""
    x = s.SparseMatrix.zeros(10)
    x[0, 0] = 1
    target = s.kronecker_product(x, s.SparseMatrix.eye(11))
    records = []
    for e in range(5):
        h = s.SparseMatrix.eye(110)[:, e:]
        require(rank(h) == 110-e, "Column selector is not full rank")
        before, after = rank(target), rank(target*h)
        require((before, after) == (11, 11-e), "One-sided target rank loss failed")
        records.append({"deleted_columns": e, "target_rank": before,
                        "retained_rank": after, "rank_loss": e})
    return records


def full_column_controls():
    """The original C gives a stronger source kernel count than C H."""
    contraction = s.SparseMatrix.diag(*([0]*96 + [1]*16))
    c = s.SparseMatrix.eye(112)[:, :110]
    full_rank = rank(contraction*c)
    require(full_rank == 14, "Full-column rank loss must be exactly two")
    records = []
    for retained in range(106, 111):
        h = s.SparseMatrix.eye(110)[:, :retained]
        compressed_rank = rank(contraction*c*h)
        require(compressed_rank == retained-96, "Compressed-column rank changed")
        records.append({"retained": retained, "contraction_rank": 16,
                        "full_column_rank": full_rank,
                        "full_kernel_dimension": 112-full_rank,
                        "compressed_column_rank": compressed_rank,
                        "compressed_kernel_dimension": 112-compressed_rank})
    return records


def first_pole_controls():
    """The three-part block estimate is sharp without more source structure."""
    records = []
    for q in range(1, 7):
        n, r = 4*q, 3*q
        matrix = s.zeros(n)
        for j in range(q):
            matrix[j, j] = 1
            matrix[r+j, q+j] = 1
            matrix[q+j, r+j] = 1
        ranks = [rank(matrix[:r, :r]), rank(matrix[:, :r]), rank(matrix)]
        require(ranks == [q, 2*q, 3*q], "First-pole rank budget failed")
        records.append({"defect": q, "block_ranks": ranks})
    return records


def product_controls():
    """A raw Laurent coefficient can exceed the rank of a regularized limit."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for q in range(1, 7):
        left = s.eye(q).col_join(t*s.eye(q))/t
        right = s.eye(q).row_join(t*s.eye(q))
        product = left*right
        raw = product.applyfunc(lambda z: s.expand(z).coeff(t, 0))
        regular = (t*product).applyfunc(s.expand)
        require(all(s.denom(z).subs(t, 0) != 0 for z in regular),
                "Product is not regular at zero")
        leading = regular.subs(t, 0)
        require(rank(raw) == 2*q and rank(leading) == q,
                "Raw/regularized rank distinction failed")
        records.append({"inner_dimension": q, "raw_constant_rank": 2*q,
                        "regularized_limit_rank": q})
    return records


def report():
    common = dict(source_dimension=112, matrix_dimension=112,
                  target_dimension=110, parameter_dimension=100,
                  source_minimum=16, row_minimum=16, target_minimum=11)
    cases = [margins(**common, retained=r) for r in range(110, 105, -1)]
    require([c["forces_regularity"] for c in cases] == [True]*4+[False],
            "Rank106 must remain outside the sufficient theorem")
    require(cases[-1]["strict_margins"] == {
        "first_pole": -2, "first_injectivity": 1, "full_row_kernel_dimension": 2},
        "Changed rank106 obstruction to this proof")
    return {"scope": SCOPE, "proof_status": "proof-written-unreviewed",
            "improves_omega": False, "source_pin_count": check_sources(),
            "a4_rank_margins": cases, "ordinary_rank_floor": 12,
            "target_rank_one_slice": 11,
            "one_sided_target_controls": one_sided_controls(),
            "full_column_kernel_controls": full_column_controls(),
            "first_pole_controls": first_pole_controls(),
            "regularized_product_controls": product_controls()}


def verify(record):
    require(record == report(), "Changed controls, rank margins or evidence scope")
    return {"a4_rank_cases": len(record["a4_rank_margins"]),
            "one_sided_target_controls": len(record["one_sided_target_controls"]),
            "full_column_kernel_controls": len(record["full_column_kernel_controls"]),
            "first_pole_controls": len(record["first_pole_controls"]),
            "regularized_product_controls": len(record["regularized_product_controls"]),
            "improves_omega": False}


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
