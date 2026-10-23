"""Exact leading-equation controls; no complete degeneration is constructed."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/leading-defect-2026-10-23/controls.json"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-koszul/cyclic_finite_target.py",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-23-one-regular-leg/proof.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == "08ac3e983e270cf3df4e26d960ceb16415f7ef31",
            "Changed predecessor commit")
    entries = record["local_dependencies"]
    require(len(entries) == 4 and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed predecessor inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Changed source: " + entry["path"])
    require(record["external_theorems_added"] is True and
            {entry["tag"] for entry in record["external_dependencies"]} == {"02LS", "0AB1"},
            "Missing graph-descent attribution")
    return len(entries)


def source_module():
    path = ROOT / "research/ai/2026-10-20-koszul/cyclic_finite_target.py"
    spec = importlib.util.spec_from_file_location("leading_defect_source", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_indices():
    rows = [(j, p, ell) for j in range(4) for p in range(4) for ell in range(7)]
    columns = [(h, q, r) for h in range(7) for q in range(4) for r in range(4)]
    return rows, columns


def endpoint_controls(source):
    rows, columns = source_indices()
    f = [1]+[0]*111
    pivots = [(i, j) for i, row in enumerate(rows) for j, col in enumerate(columns)
              if source.slice_entry(f, 4, row, col)]
    require(len(pivots) == len({i for i, _ in pivots}) == len({j for _, j in pivots}) == 16,
            "Source coordinate is not rank16")
    records = []
    for qb in range(3, 14):
        qc = 16-qb
        killed_rows = [i for i, _ in pivots[:qb]]
        killed_cols = [j for _, j in pivots[qb:]]
        b_columns = [(i, 0) for i in range(112) if i not in killed_rows]
        b_columns += [(i, 1) for i in killed_rows[:-2]]
        c_rows = [(j, 0) for j in range(112) if j not in killed_cols]
        c_rows += [(j, 1) for j in killed_cols[:-2]]
        require(len(b_columns) == len(c_rows) == 110, "Wrong Laurent long-map format")
        require(len({i for i, _ in b_columns}) == len({j for j, _ in c_rows}) == 110,
                "Long map does not have generic rank110")
        b_lookup = {i: (a, exponent) for a, (i, exponent) in enumerate(b_columns)}
        c_lookup = {j: (b, exponent) for b, (j, exponent) in enumerate(c_rows)}
        output = []
        for i, j in pivots:
            if i in b_lookup and j in c_lookup:
                a, eb = b_lookup[i]
                b, ec = c_lookup[j]
                output.append((a, b, eb+ec-1))
        require(len(output) == 12 and all(e == 0 for _, _, e in output),
                "Leading pole failed to cancel or constant rank changed")
        require(len({a for a, _, _ in output}) == len({b for _, b, _ in output}) == 12,
                "Constant output is not a rank12 partial permutation")
        records.append({"row_defect": qb, "column_defect": qc,
                        "leading_ranks": [112-qb, 112-qc],
                        "row_deleted_coordinates": killed_rows,
                        "row_restored_at_degree_one": killed_rows[:-2],
                        "column_deleted_coordinates": killed_cols,
                        "column_restored_at_degree_one": killed_cols[:-2],
                        "negative_output_entries": 0, "constant_output_rank": 12,
                        "complete_target_identity": False})
    return records


def pencil_controls(source):
    rows, columns = source_indices()
    records = []
    for varying in ("u", "v"):
        annihilators = []
        ranks = []
        for parameter in range(5):
            u, v = [1, 0, 0, 0], [1, 0, 0, 0]
            if varying == "u":
                u[1] = parameter
            else:
                v[1] = parameter
            f = [u[i]*int(k == 0)*v[z]
                 for i in range(4) for k in range(7) for z in range(4)]
            # Independently compare every literal coefficient to the tensor-product formula.
            for row in rows:
                j, p, ell = row
                for col in columns:
                    h, q, r = col
                    expected = (u[h-j]*v[ell-r]
                                if p == q == 0 and 0 <= h-j < 4 and 0 <= ell-r < 4 else 0)
                    require(source.slice_entry(f, 4, row, col) == expected,
                            "Minimum-slice row/column factorization failed")
            polynomial = u if varying == "u" else v
            multiples = s.Matrix(4, 7, lambda shift, degree:
                                 polynomial[degree-shift] if 0 <= degree-shift < 4 else 0)
            require(multiples.rank() == 4, "Polynomial multiplication lost rank")
            annihilators.extend(vector.T for vector in multiples.nullspace())
            ranks.append(16)
        constraints = s.Matrix.vstack(*annihilators)
        pivot_rows = list(constraints.T.rref()[1])
        require(len(pivot_rows) == 7, "Five pencil fibers have a nonzero common factor space")
        determinant = constraints[pivot_rows, :].det()
        require(determinant != 0, "Intersection determinant vanished")
        records.append({"varying_factor": varying, "parameters": list(range(5)),
                        "literal_source_coefficients_checked": 5*112*112,
                        "source_slice_ranks_from_factorization": ranks,
                        "polynomial_intersection_dimension": 0,
                        "annihilator_pivot_rows": pivot_rows,
                        "annihilator_minor_determinant": str(determinant)})
    return records


def bilinear_kernel_controls():
    records = []
    for p in range(9):
        # Independent cyclic bilinear forms, evaluated on ten separate a-fibers.
        constraints = [s.Matrix(p, 10, lambda j, b: int(b == (a+j) % 10))
                       for a in range(10)]
        dimensions = [10-m.rank() for m in constraints]
        shared_dimensions = [10-constraints[a].col_join(constraints[b]).rank()
                             for a in range(10) for b in range(a+1, 10)]
        require(dimensions == [10-p]*10 and min(shared_dimensions) >= 10-2*p,
                "Bilinear common-kernel dimensions failed")
        require(sum(dimensions) > 16 and min(dimensions) >= 2,
                "The small-codimension ruling argument lost a strict margin")
        records.append({"constraint_count": p, "individual_fiber_dimensions": dimensions,
                        "basis_pairs_checked": len(shared_dimensions),
                        "minimum_shared_fiber_dimension": min(shared_dimensions),
                        "direct_sum_rankone_span_dimension": sum(dimensions),
                        "pairwise_intersection_argument_suffices": p <= 4})
    return records


def report():
    source = source_module()
    return {"scope": "Necessary leading flags only; no complete target or exponent gain.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "necessary_total_defect": 16, "equality_leading_first_map_rank": 1,
            "equality_minimum_balanced_first_map_pole_order": 9,
            "coherent_leading_rank_bound": 16, "coherent_defect_upper_exclusive": 32,
            "leading_equation_controls": endpoint_controls(source),
            "minimum_slice_pencils": pencil_controls(source),
            "bilinear_kernel_controls": bilinear_kernel_controls()}


def verify(record):
    require(record == report(), "Changed leading certificate or mathematical scope")
    return {"leading_equation_controls": len(record["leading_equation_controls"]),
            "pencil_controls": len(record["minimum_slice_pencils"]),
            "bilinear_kernel_controls": len(record["bilinear_kernel_controls"]),
            "literal_source_coefficients_checked": sum(
                row["literal_source_coefficients_checked"] for row in record["minimum_slice_pencils"]),
            "complete_target_constructed": False, "improves_omega": False}


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
