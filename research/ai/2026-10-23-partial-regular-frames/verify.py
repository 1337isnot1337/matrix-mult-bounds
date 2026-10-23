"""Finite exact controls for the written partial-regular-frame theorem."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/partial-regular-frames-2026-10-23/controls.json"
PREVIOUS = ROOT / "research/ai/2026-10-23-regular-unit-image"
SPEC = importlib.util.spec_from_file_location("partial_frames_predecessor", PREVIOUS / "verify.py")
prior = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(prior)
require = prior.require


def check_sources(record=None):
    record = json.loads((PACKAGE / "sources.json").read_text()) if record is None else record
    paths = {"research/ai/2026-10-23-regular-unit-image/proof.md",
             "research/ai/2026-10-23-regular-unit-image/verify.py",
             "research/ai/2026-10-20-koszul/cyclic_finite_target.md"}
    entries = record["local_dependencies"]
    require(len(entries) == 3 and {x["path"] for x in entries} == paths,
            "Changed predecessor inventory")
    for x in entries:
        require(hashlib.sha256((ROOT / x["path"]).read_bytes()).hexdigest() == x["sha256"],
                "Changed predecessor: " + x["path"])
    return len(entries)


def complete(columns):
    """Deterministic constant completion; finite controls only."""
    n = columns.rows
    result = columns
    for j in range(n):
        candidate = result.row_join(s.eye(n)[:, j])
        if candidate.rank() > result.cols:
            result = candidate
        if result.cols == n:
            return result
    raise ValueError("Could not complete frame")


def independent_frame_controls():
    records = []
    for r in range(1, 5):
        target, n = r+1, r+3
        h = s.eye(target)[:, :r]
        j = s.eye(target)[:, 1:]
        p = j.T
        b = s.eye(n)[:target, :]
        c = b.T
        u, v = c*j, c*h
        qb, qc = complete(u), complete(v)
        mt = qb.inv()*qc
        bp = p*b*qb
        ch = qc.inv()*c*h
        require(h != j and p*j == s.eye(r), "Independent target frames lost")
        require(b*u == j, "Partial right inverse failed")
        require(bp[:, :r] == s.eye(r), "Row-frame normalization failed")
        require(ch == s.eye(n)[:, :r], "Column-frame normalization failed")
        require(bp*mt*ch == p*h, "Source-frame tensor identity failed")
        require((p*h).rank() == r-1, "Independent-frame rank loss control failed")
        records.append({"retained": r, "target_dimension": target,
                        "target_frames_distinct": True,
                        "compressed_identity_rank": r-1,
                        "source_frame_determinants": [int(qb.det()), int(qc.det())]})
    return records


def polar_unit_controls():
    """Both unselected long columns and the unit slice may have poles."""
    t = s.Symbol("t", nonzero=True)
    records = []
    for r in range(1, 5):
        for pole in (1, 2, 3):
            target, n = r+1, r+3
            h = s.eye(target)[:, :r]
            c = s.eye(n)[:, :target]
            c[r, r] = t**(-pole)
            unit = s.eye(n)
            unit[r, r] = t**(-pole)
            b = s.eye(n)[:target, :]
            b[r, r] = t**(2*pole)
            v, u = c*h, unit*c*h
            require(b*unit*c == s.eye(target), "Polar unit equation failed")
            require(v == s.eye(n)[:, :r] and u == v, "Selected frames are not regular")
            require(b*u == h, "Partial right inverse lost")
            require(c[r, r] == unit[r, r] == t**(-pole), "Polar escape control lost")
            records.append({"retained": r, "unselected_long_pole_order": pole,
                            "unit_pole_order": pole, "partial_frame_ranks": [r, r],
                            "unit_equation_exact": True,
                            "source_rank_hypotheses_asserted": False})
    return records


def column_kernel_controls():
    records = []
    for n in range(4, 8):
        for q in range(1, 4):
            r, d = n-q, n+2
            contraction = s.eye(n).row_join(s.zeros(n, 2))
            b0 = s.eye(n)[:r, :]
            constrained = b0*contraction
            kernel = s.Matrix.hstack(*constrained.nullspace())
            require(contraction.rank() == n and constrained.rank() == n-q,
                    "Column projection rank budget failed")
            require(kernel.cols == d-n+q and kernel.rank() == kernel.cols,
                    "Column kernel dimension incorrect")
            require(constrained*kernel == s.zeros(r, kernel.cols),
                    "Equality-boundary kernel witness failed")
            records.append({"source_parameter_dimension": d, "column_minimum_for_this_map": n,
                            "source_projection_defect": q, "projected_rank": n-q,
                            "kernel_dimension": d-n+q,
                            "equality_allows_injective_kernel_map": True})
    return records


def report():
    base = dict(source_dimension=112, matrix_dimension=112, target_dimension=110,
                parameter_dimension=100, source_minimum=16, row_minimum=16,
                target_minimum=11)
    margins = []
    for r in (110, 109, 108):
        row = prior.margins(**base, retained=r)
        column_margin = 100-112+16-(112-r)
        row["strict_margins"]["column_kernel_dimension"] = column_margin
        row["forces_all_maps_regular"] = row["forces_regularity"] and column_margin > 0
        margins.append(row)
    require([x["forces_all_maps_regular"] for x in margins] == [True, True, False],
            "Changed A4 escape boundary")
    prior.verify(json.loads(prior.RESULT.read_text()))
    return {"scope": "Finite matrix controls for a written all-order theorem; partial frames are hypotheses.",
            "proof_status": "proof-written-unreviewed", "improves_omega": False,
            "source_pins": check_sources(), "a4_rank_cases": margins,
            "independent_target_frames": independent_frame_controls(),
            "polar_unit_and_long_map_examples": polar_unit_controls(),
            "column_kernel_examples": column_kernel_controls()}


def verify(record):
    require(record == report(), "Changed evidence, hypotheses or proof status")
    return {"independent_frame_examples": len(record["independent_target_frames"]),
            "polar_unit_examples": len(record["polar_unit_and_long_map_examples"]),
            "column_kernel_examples": len(record["column_kernel_examples"]),
            "a4_rank_cases": len(record["a4_rank_cases"]), "improves_omega": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True) + "\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
