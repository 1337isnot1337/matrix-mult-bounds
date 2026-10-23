"""Exact finite controls for the shared-correction target-ruling proof."""
from __future__ import annotations

import argparse
import hashlib
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/singular-long-ruling-2026-10-23/controls.json"
BASE = "1c04903c215f396150605c0778024e856ec0b0d4"
DEPENDENCIES = {
    "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == BASE and record["field"] == "C",
            "Changed source baseline or field")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed source dependency inventory")
    for entry in entries:
        digest = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(digest == entry["sha256"], "Source digest mismatch: " + entry["path"])
    prior = record["concurrent_predecessor"]
    require(prior["pr"] == 113
            and prior["commit"] == "08ac3e983e270cf3df4e26d960ceb16415f7ef31",
            "Changed correction predecessor")
    external = record["external_dependency_in_prior_gap_proof"]
    require(external["doi"] == "10.2307/2372388"
            and external["theorem"] == "2.1, printed page126",
            "Changed external splitting-theorem attribution")
    return len(entries)


def zero(matrix):
    return matrix.applyfunc(s.cancel) == s.zeros(*matrix.shape)


def shared_correction_controls():
    t = s.Symbol("t", nonzero=True)
    records = []
    m, n, r = 2, 2, 4
    for k in range(1, 4):
        for missing in (1, 2, 4):
            diagonal = s.diag(*([t]*missing+[1]*(r-missing)))
            u = s.eye(r)[:, :k]
            inverse = diagonal.col_join(s.zeros(k, r))
            b = diagonal.inv().row_join(diagonal.inv()*u/t)
            p = s.eye(r+k)-inverse*b
            kernel = (-u).col_join(t*s.eye(k))
            require(zero(b*inverse-s.eye(r)) and zero(p*p-p) and p.rank() == k,
                    "Invalid regular inverse or polar projector")
            require(zero(b*kernel), "Invalid regular common kernel basis")
            corrections, sources = [], []
            for i, j in product(range(m), repeat=2):
                unit = s.zeros(m)
                unit[i, j] = 1
                xi = s.kronecker_product(unit, s.eye(n))
                if i == j:
                    coefficient = (-1)**i * s.eye(r)[:k, :]
                else:
                    coefficient = s.Matrix(k, r, lambda a, q: (a+1)*(q+1)+i-j)
                w = kernel*coefficient
                y = inverse*xi+w
                require(zero(b*y-xi) and zero(p*y-w), "Correction identity failed")
                require(zero(y-inverse*(b*y)-w), "Regularization identity failed")
                corrections.append(w)
                sources.append(y)
            require(zero(sources[0]+sources[3]-inverse), "Unit correction is not zero")
            joint = s.Matrix.hstack(*corrections)
            at_zero = joint.subs(t, 0)
            require(joint.rank() == k and at_zero.rank() == k,
                    "Shared correction dimension failed")
            quotient = s.eye(r+k)[k:, :]
            require(zero(quotient*at_zero), "Invalid constant correction quotient")
            records.append({"long_defect": k, "unit_image_rank": r-missing,
                            "individual_rank_bound": k, "joint_rank": k,
                            "constant_joint_rank": k, "target_generators": m*m})
    # Individual bounds alone do not supply a common one-dimensional space.
    separate = [s.Matrix([[1, 0], [0, 0]]), s.Matrix([[0, 0], [1, 0]])]
    require(all(w.rank() == 1 for w in separate)
            and s.Matrix.hstack(*separate).rank() == 2,
            "Missing individual-versus-shared-space negative control")
    return records, {"individual_ranks": [1, 1], "joint_rank": 2,
                     "compatible_with_common_rank_one_projector": False}


def target_ruling_controls():
    records = []
    for m in range(2, 6):
        for n in range(1, 4):
            r = m*n
            a = s.Matrix(2, r, lambda i, j: (i+1)*(j+1))
            u = s.Matrix([1]+[0]*(m-1))
            require(a*s.kronecker_product(u, s.eye(n)) != s.zeros(2, n),
                    "Zero quotient unit-image block")
            images = []
            for j in range(m):
                row = s.zeros(1, m)
                row[0, j] = 1
                image = a*s.kronecker_product(u*row, s.eye(n))
                images.append(image.reshape(2*r, 1))
            rank = s.Matrix.hstack(*images).rank()
            require(rank == m, "Nonzero quotient lost target ruling injectivity")
            records.append({"matrix_size": m, "multiplicity": n,
                            "ruling_dimension": m, "image_dimension": rank})
    return records


def source_matrix(a, coefficients):
    rows = list(product(range(a), range(a), range(2*a-1)))
    columns = list(product(range(2*a-1), range(a), range(a)))
    return s.Matrix([
        [coefficients.get((h-j, p+q, long_row-r), 0)
         if 0 <= h-j < a and 0 <= long_row-r < a else 0
         for h, q, r in columns]
        for j, p, long_row in rows])


def exact_rank(matrix):
    return matrix.to_DM().rank()


def actual_source_controls():
    a = 4
    records = []
    vectors = s.eye(4).columnspace() + [s.ones(4, 1), s.Matrix([1, -2, 3, -4])]
    for vector in vectors:
        coefficients = {(i, 0, 0): vector[i] for i in range(a)}
        rank = exact_rank(source_matrix(a, coefficients))
        require(rank == 16, "Minimum-cone ruling rank failed")
        records.append({"varying_outer_vector": list(map(int, vector)), "slice_rank": rank})
    gap = {(0, 0, 0): 1, (1, 0, 1): 1}
    rank = exact_rank(source_matrix(a, gap))
    require(rank == 20, "Actual first-gap boundary slice changed rank")
    return records, {"coefficients": [[0, 0, 0, 1], [1, 0, 1, 1]],
                     "slice_rank": rank, "inside_minimum_cone": False}


def a4_criterion(rank):
    require(type(rank) is int and 0 <= rank <= 110, "Invalid A4 long-map rank")
    lost = 112-rank
    cap = 11+2+lost
    minimum_cone_applies = cap < 20
    strict_nonzero = 16-lost-2
    return {"long_limit_rank": rank, "source_rank_cap": cap,
            "minimum_cone_applies": minimum_cone_applies,
            "source_ruling_dimension_bound": 4 if minimum_cone_applies else None,
            "target_ruling_dimension": 10, "nonzero_lift_margin": strict_nonzero,
            "excluded_by_this_criterion": minimum_cone_applies and strict_nonzero > 0}


def report():
    shared, negative = shared_correction_controls()
    source, gap = actual_source_controls()
    cases = [a4_criterion(c) for c in range(110, 103, -1)]
    require([c["excluded_by_this_criterion"] for c in cases] == [True]*5+[False]*2,
            "Changed singular-long-map threshold")
    return {"scope": "Finite exact controls; all-order ruling proof is written and unreviewed.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "shared_corrections": shared, "individual_rank_negative_control": negative,
            "target_rulings": target_ruling_controls(), "minimum_source_ruling": source,
            "first_gap_source_witness": gap, "a4_long_limit_cases": cases}


def verify(record):
    require(record == report(), "Changed controls, scope or review status")
    return {"shared_correction_families": len(record["shared_corrections"]),
            "target_rulings": len(record["target_rulings"]),
            "minimum_source_slices": len(record["minimum_source_ruling"]),
            "first_gap_source_rank": record["first_gap_source_witness"]["slice_rank"],
            "a4_long_limit_cases": len(record["a4_long_limit_cases"]),
            "minimum_excluded_long_limit_rank": 106, "improves_omega": False}


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
