"""Finite exact kernel witnesses and source-gap controls; no formal proof."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/singular-long-gap-2026-10-23/controls.json"
BASE = "08ac3e983e270cf3df4e26d960ceb16415f7ef31"
DEPENDENCIES = (
    "research/ai/2026-10-23-one-regular-leg/proof.md",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
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
            {entry["path"] for entry in entries} == set(DEPENDENCIES),
            "Changed dependency inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    require(record["external_dependencies"] == [{
        "name": "Flanders bounded-rank dimension inequality",
        "url": "https://arxiv.org/pdf/1507.05375v2", "location": "Theorem 1.1, page 3",
        "field": "C", "application": "A singular linear subspace of Mat_m has dimension at most m(m-1)."}],
        "Changed external theorem scope")
    return len(entries)


def complete_basis(columns, dimension):
    frame = s.Matrix.hstack(*columns) if columns else s.zeros(dimension, 0)
    for j in range(dimension):
        candidate = frame.row_join(s.eye(dimension)[:, j])
        if candidate.to_DM().rank() > frame.cols:
            frame = candidate
        if frame.cols == dimension:
            return frame
    require(False, "Independent columns did not complete to a basis")


def invertible_compression_kernel(p, q):
    """Map im Q into ker P, then extend that injection to an isomorphism."""
    dimension = p.cols
    require(q.rows == dimension and p.rank()+q.rank() <= dimension,
            "Compression dimensions do not guarantee a kernel unit")
    columns = q.columnspace()
    source_frame = complete_basis(columns, dimension)
    target_frame = complete_basis(p.nullspace()[:len(columns)], dimension)
    witness = target_frame*source_frame.inv()
    require(witness.det() != 0 and p*witness*q == s.zeros(p.rows, q.cols),
            "Invalid invertible compression-kernel witness")
    return witness


def encode(matrix):
    return [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def compression_controls():
    cases = [(a, 2*a, p, q) for a in (2, 3, 4)
             for p in range(a+1) for q in range(a+1)]
    cases += [(4, 10, 4, 4), (4, 10, 1, 4), (4, 10, 4, 1)]
    records = []
    for a, m, p_rank, q_rank in cases:
        left = s.eye(m)
        right = s.eye(m)
        for i in range(m):
            for j in range(i):
                left[i, j] = (i+2*j)%3-1
                right[j, i] = (2*i+j)%3-1
        p = s.zeros(a, m)
        q = s.zeros(m, a)
        for j in range(p_rank):
            p[j, j] = 1
        for j in range(q_rank):
            q[j, j] = 1
        p, q = p*left, right*q
        witness = invertible_compression_kernel(p, q)
        records.append({"a": a, "m": m, "p_rank": p_rank, "q_rank": q_rank,
                        "P": encode(p), "Q": encode(q), "kernel_unit": encode(witness)})
    return records


def degenerate_controls():
    rng = random.Random(20261023)
    records = []
    for a, m in ((2, 4), (3, 6), (4, 10)):
        forms = s.Matrix(a, m*m, lambda i, j: rng.randrange(-2, 3))
        kernel = s.Matrix.hstack(*forms.nullspace())
        for attempt in range(1, 51):
            vector = kernel*s.Matrix(kernel.cols, 1, lambda i, j: rng.randrange(-2, 3))
            witness = s.Matrix(m, m, list(vector))
            if witness.det() != 0:
                break
        else:
            raise ValueError("No finite discovery witness found")
        require(forms*s.Matrix(list(witness)) == s.zeros(a, 1), "Kernel forms do not vanish")
        require(m*m-forms.rank() > m*(m-1), "Degenerate Flanders margin failed")
        records.append({"a": a, "m": m, "linear_forms": encode(forms),
                        "kernel_unit": encode(witness), "discovery_attempts": attempt,
                        "kernel_dimension": m*m-forms.rank(), "singular_dimension_cap": m*(m-1)})
    return records


def source_controls():
    a, middle = 4, 7
    rows = [(j, p, ell) for j in range(a) for p in range(a) for ell in range(middle)]
    cols = [(height, q, r) for height in range(middle) for q in range(a) for r in range(a)]
    records = []
    for positions, expected in (([(0, 0, 0)], 16), ([(0, 0, 0), (1, 0, 1)], 20)):
        coefficients = {tuple(index): 1 for index in positions}
        matrix = s.Matrix([[coefficients.get((height-j, p+q, ell-r), 0)
                            for height, q, r in cols] for j, p, ell in rows])
        rank = matrix.to_DM().rank()
        require(rank == expected, "Literal A4 gap control failed")
        records.append({"nonzero_coefficients": [list(index) for index in positions],
                        "exact_rank": rank})
    return records


def a4_margins():
    return [{"long_limit_rank": 110-corank, "target_corank": corank,
             "rank_one_source_budget": 15+corank, "minimum_gap_margin": 5-corank,
             "unit_image_margin": 12-corank, "excludes_target": corank <= 4}
            for corank in range(6)]


def report():
    return {"scope": "Finite exact witnesses; no formal Laurent proof or exponent gain.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pin_count": check_sources(), "a4_margins": a4_margins(),
            "compression_kernel_units": compression_controls(),
            "degenerate_kernel_units": degenerate_controls(), "source_gap": source_controls()}


def verify(record):
    require(record["scope"] == "Finite exact witnesses; no formal Laurent proof or exponent gain."
            and record["proof_status"] == "proof-written-unreviewed"
            and record["improves_omega"] is False, "Changed evidence scope")
    require(record["source_pin_count"] == check_sources(), "Changed source count")
    expected_formats = [(a, 2*a, p, q) for a in (2, 3, 4)
                        for p in range(a+1) for q in range(a+1)]
    expected_formats += [(4, 10, 4, 4), (4, 10, 1, 4), (4, 10, 4, 1)]
    require([(r["a"], r["m"], r["p_rank"], r["q_rank"])
             for r in record["compression_kernel_units"]] == expected_formats,
            "Changed compression witness inventory")
    for entry in record["compression_kernel_units"]:
        p, q, witness = (s.Matrix(entry[name]) for name in ("P", "Q", "kernel_unit"))
        require(p.shape == (entry["a"], entry["m"]) and
                q.shape == (entry["m"], entry["a"]) and
                witness.shape == (entry["m"], entry["m"]), "Wrong witness format")
        require(p.rank() == entry["p_rank"] and q.rank() == entry["q_rank"], "Wrong factor rank")
        require(witness.det() != 0 and p*witness*q == s.zeros(p.rows, q.cols),
                "Invalid compression kernel unit")
    require([(r["a"], r["m"]) for r in record["degenerate_kernel_units"]] ==
            [(2, 4), (3, 6), (4, 10)], "Changed degenerate inventory")
    for entry in record["degenerate_kernel_units"]:
        a, m = entry["a"], entry["m"]
        forms, witness = s.Matrix(entry["linear_forms"]), s.Matrix(entry["kernel_unit"])
        require(forms.shape == (a, m*m) and witness.shape == (m, m), "Wrong degenerate format")
        require(witness.det() != 0 and forms*s.Matrix(list(witness)) == s.zeros(a, 1),
                "Invalid degenerate kernel unit")
        require(entry["kernel_dimension"] == m*m-forms.rank() > m*(m-1) ==
                entry["singular_dimension_cap"], "Changed dimension margin")
    require(record["a4_margins"] == a4_margins() and record["source_gap"] == source_controls(),
            "Changed strict boundary or source gap")
    return {"compression_kernel_units": 53, "degenerate_kernel_units": 3,
            "source_gap_matrices": 2, "lowest_excluded_long_limit_rank": 106,
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
