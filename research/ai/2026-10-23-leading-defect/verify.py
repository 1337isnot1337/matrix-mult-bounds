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
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
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
    require(len(entries) == 5 and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed predecessor inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Changed source: " + entry["path"])
    require(record["external_theorems_added"] is True and
            {entry["tag"] for entry in record["external_dependencies"]} == {"DSP16-T1.1", "GRO57-T2.1"},
            "Missing bounded-rank or source-gap attribution")
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
        compressed_unit_rank = sum(j not in killed_cols for _, j in pivots)
        require(compressed_unit_rank == qb and compressed_unit_rank > 2,
                "The invertible-kernel correction contradiction failed")
        records.append({"row_defect": qb, "column_defect": qc,
                        "leading_ranks": [112-qb, 112-qc],
                        "row_deleted_coordinates": killed_rows,
                        "row_restored_at_degree_one": killed_rows[:-2],
                        "column_deleted_coordinates": killed_cols,
                        "column_restored_at_degree_one": killed_cols[:-2],
                        "negative_output_entries": 0, "constant_output_rank": 12,
                        "complete_target_identity": False,
                        "trace_kernel_parameter_invertible": True,
                        "compressed_unit_rank": compressed_unit_rank, "kernel_correction_rank_bound": 2,
                        "all_order_rank_contradiction_margin": qb-2})
    return records


def source_gap_controls(source):
    rows, columns = source_indices()
    records = []
    for support, expected in (([(0, 0)], 16), ([(0, 0), (1, 1)], 20)):
        g = [[int((i, z) in support) for z in range(4)] for i in range(4)]
        f = [g[i][z]*int(k == 0) for i in range(4) for k in range(7) for z in range(4)]
        for row in rows:
            j, p, ell = row
            for col in columns:
                h, q, r = col
                value = (g[h-j][ell-r]
                         if p == q == 0 and 0 <= h-j < 4 and 0 <= ell-r < 4 else 0)
                require(source.slice_entry(f, 4, row, col) == value,
                        "Literal source biform factorization failed")
        active = s.Matrix([[source.slice_entry(f, 4, row, col)
                            for col in columns if col[1] == 0]
                           for row in rows if row[1] == 0])
        rank = active.rank()
        require(rank == expected, "Source gap endpoint rank changed")
        records.append({"biform": g, "literal_rank": rank,
                        "literal_coefficients_checked": 112*112})
    return records


def invertible_kernel_controls():
    # Exact witnesses for the rank-one leading functional used in the d16 controls.
    shift = s.zeros(10)
    for i in range(10):
        shift[i, (i+1) % 10] = 1
    require(shift.trace() == 0 and shift.det() != 0,
            "Trace-zero target parameter is not invertible")
    require(s.eye(10).trace() == 10, "Target unit lost its nonzero lift")
    records = []
    for n in range(2, 11):
        dimension = n*n-(n-1)
        bound = n*(n-1)
        require(dimension-bound == 1, "Flanders strict dimension margin changed")
        # At codimension n, all matrices with first row zero form a singular kernel.
        records.append({"matrix_size": n, "leading_map_rank": n-1,
                        "kernel_dimension": dimension, "singular_space_dimension_bound": bound,
                        "strict_margin": 1, "boundary_zero_row_kernel_dimension": bound})
    return {"trace_kernel_permutation": [(i+1) % 10 for i in range(10)],
            "trace_kernel_determinant": int(shift.det()), "dimension_controls": records,
            "a4_source_minimum": 16, "correction_rank_bound": 2,
            "maximum_total_defect_for_minimum_rank_contradiction": 27,
            "minimum_source_slice_rank_bound_at_defect27": 2+27//2}


def general_kernel_examples():
    """Full Laurent identities in synthetic matrix sources with minimum rank one."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for m in (2, 3, 4):
        shift = s.zeros(m)
        for i in range(m):
            shift[i, (i+1) % m] = 1
        require(shift.trace() == 0 and shift.det() != 0,
                "General leading kernel lost its invertible parameter")
        for n in (1, 2):
            for k in (1, 2):
                r, dimension = m*n, m*n+k
                c = s.eye(dimension)[:, :r]
                b = c.T
                leading = s.zeros(dimension)
                leading[-1, -1] = 1
                for i in range(m):
                    for j in range(m):
                        unit = s.zeros(m)
                        unit[i, j] = 1
                        target = s.kronecker_product(unit, s.eye(n))
                        lift = s.zeros(dimension)
                        lift[:r, :r] = target
                        lift += int(i == j)*leading/t
                        require(b*lift*c == target, "Synthetic full Laurent identity failed")
                require(leading.rank() == 1 <= 2*k,
                        "Synthetic leading slice violates the general bound")
                records.append({"matrix_parameter_size": m, "multiplicity": n,
                                "source_matrix_size": dimension, "long_defect": k,
                                "basis_identities_checked": m*m, "leading_source_rank": 1,
                                "source_minimum": 1, "general_rank_bound": 2*k,
                                "a4_source": False})
    return records


def report():
    source = source_module()
    return {"scope": "All-order exclusion below total defect20; no full target or exponent gain.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "necessary_total_defect": 20, "maximum_total_leading_rank": 204,
            "coherent_defect_interval": [20, 31], "coherent_leading_rank_bound": 16,
            "intermediate_defect_interval": [20, 27], "intermediate_first_map_rank_interval": [10, 16],
            "leading_equation_controls": endpoint_controls(source),
            "source_gap_controls": source_gap_controls(source),
            "invertible_kernel_controls": invertible_kernel_controls(),
            "general_kernel_examples": general_kernel_examples()}


def verify(record):
    require(record == report(), "Changed leading certificate or mathematical scope")
    return {"leading_equation_controls": len(record["leading_equation_controls"]),
            "source_gap_controls": len(record["source_gap_controls"]),
            "literal_source_coefficients_checked": sum(
                row["literal_coefficients_checked"] for row in record["source_gap_controls"]),
            "dimension_controls": len(record["invertible_kernel_controls"]["dimension_controls"]),
            "general_laurent_examples": len(record["general_kernel_examples"]),
            "general_basis_identities": sum(x["basis_identities_checked"]
                                            for x in record["general_kernel_examples"]),
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
