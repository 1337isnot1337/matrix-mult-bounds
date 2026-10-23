"""Exact finite controls for the proposed rank106/rank-sum204 continuation.

These are algebraic controls, not an exhaustive proof of the classification
of all rank-one preservers or of the credited source slice-rank gap.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import random

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/long-leg-rank-gap-2026-10-23/controls.json"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "gap_sources.json").read_text())
    require(record["base_commit"] == "87d2f3722cea61743de8927122bd9e7bc4be19f9",
            "Changed gap-extension source baseline")
    expected = {
        "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
        "research/ai/2026-10-20-koszul/cyclic_finite_target.md",
        "research/ai/2026-10-23-long-leg-rank-obstruction/proof.md",
        "research/ai/2026-10-23-long-leg-rank-obstruction/corank_one.md",
        "research/ai/2026-10-23-long-leg-rank-obstruction/sources.json",
    }
    entries = record["local_dependencies"]
    require(len(entries) == len(expected) and {e["path"] for e in entries} == expected,
            "Changed gap-extension predecessor inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Changed source bytes: " + entry["path"])
    external = record["inherited_external_dependency"]
    require(external["doi"] == "10.2307/2372388"
            and external["theorem"] == "Theorem 2.1, printed page 126"
            and external["hypotheses"] == "Vector bundles on the complex projective line",
            "Changed inherited splitting-theorem attribution or hypotheses")
    require(record["concurrent_kernel_predecessor"]["commit"] ==
            "08ac3e983e270cf3df4e26d960ceb16415f7ef31",
            "Changed concurrent regular-kernel attribution")
    return len(entries)


def unimodular(size, rng):
    matrix = s.eye(size)
    for _ in range(3*size):
        i, j = rng.sample(range(size), 2)
        matrix[i, :] += rng.choice((-2, -1, 1, 2))*matrix[j, :]
    require(matrix.det() == 1, "Elementary row operations lost unimodularity")
    return matrix


def factor_kernel_controls():
    rng = random.Random(106204)
    records = []
    for p in range(1, 5):
        for q in range(1, 5):
            left_basis = unimodular(10, rng)
            right_basis = unimodular(10, rng)
            left_output = unimodular(4, rng)
            right_output = unimodular(4, rng)
            p0, q0 = s.zeros(4, 10), s.zeros(4, 10)
            for i in range(p):
                p0[i, i] = 1
            for j in range(q):
                q0[j, j] = 1
            pmap = left_output*p0*left_basis
            qmap = right_output*q0*right_basis
            selected = list(range(p, p+q))
            permutation = selected+[j for j in range(10) if j not in selected]
            unit = s.zeros(10)
            for j, i in enumerate(permutation):
                unit[i, j] = 1
            kernel_unit = left_basis.inv()*unit*right_basis.inv().T
            require(pmap.rank() == p and qmap.rank() == q,
                    "Factor maps have incorrect prescribed rank")
            require(abs(kernel_unit.det()) == 1 and pmap*kernel_unit*qmap.T == s.zeros(4),
                    "Factored preserver kernel did not contain the explicit unit")
            pure_count = 0
            for _ in range(3):
                a = s.Matrix([rng.randrange(-2, 3) for _ in range(10)])
                b = s.Matrix([rng.randrange(-2, 3) for _ in range(10)])
                target = a*b.T
                image = pmap*target*qmap.T
                require(image == (pmap*a)*(qmap*b).T and image.rank() <= 1,
                        "Factored map did not preserve a rank-one input")
                pure_count += 1
            for transpose in (False, True):
                x = kernel_unit.T if transpose else kernel_unit
                image = pmap*(x.T if transpose else x)*qmap.T
                require(image == s.zeros(4) and x.det() != 0,
                        "Transpose preserver kernel unit failed")
                records.append({"left_rank": p, "right_rank": q,
                                "transpose": transpose,
                                "kernel_unit_determinant": int(x.det()),
                                "pure_inputs_checked": pure_count})
    return records


def fixed_factor_controls():
    rng = random.Random(410)
    records = []
    for transpose in (False, True):
        # Arbitrary linear coordinates on Mat10, rather than only a block map.
        functionals = s.Matrix(4, 100, lambda i, j: rng.randrange(-2, 3))
        reduced, pivots = functionals.rref()
        require(len(pivots) == 4, "Generic fixed-factor coordinate map lost rank")
        free = [j for j in range(100) if j not in pivots]
        x = None
        for attempt in range(1, 21):
            vector = s.Matrix([rng.randrange(-2, 3) if j in free else 0
                               for j in range(100)])
            for i, pivot in enumerate(pivots):
                vector[pivot] = -sum(reduced[i, j]*vector[j] for j in free)
            candidate = vector.reshape(10, 10)
            if candidate.det() != 0:
                x = candidate
                break
        require(x is not None, "Finite fixed-factor kernel search found no unit")
        require(functionals*x.reshape(100, 1) == s.zeros(4, 1),
                "Fixed-factor kernel certificate failed")
        fixed = s.Matrix([1, 2, -1, 1])
        for _ in range(3):
            target = s.Matrix(10, 10, lambda i, j: rng.randrange(-2, 3))
            coordinate = functionals*target.reshape(100, 1)
            image = fixed*coordinate.T
            if transpose:
                image = image.T
            require(image.rank() <= 1, "Fixed-factor map has a rank-two image")
        records.append({"transpose": transpose, "image_dimension": 4,
                        "kernel_dimension": 96, "kernel_unit_found": True,
                        "search_attempts": attempt})
    return records


def source_block(coefficients):
    rows = [(j, ell) for j in range(4) for ell in range(7)]
    columns = [(h, r) for h in range(7) for r in range(4)]
    return s.Matrix(28, 28, lambda row, col:
                    coefficients[columns[col][0]-rows[row][0],
                                 rows[row][1]-columns[col][1]]
                    if (0 <= columns[col][0]-rows[row][0] < 4
                        and 0 <= rows[row][1]-columns[col][1] < 4) else 0)


def boundary_controls():
    records = []
    for width in (1, 2, 3, 4):
        coefficients = s.diag(*([1]*width+[0]*(4-width)))
        block = source_block(coefficients)
        expected = 12+4*width
        require(block.rank() == expected, "Explicit source biform rank changed")
        records.append({"coefficient_matrix_rank": width,
                        "source_slice_rank_with_coherent_middle": expected})

    # A map preserving rank-one matrices need not have four-dimensional image.
    pmap = s.eye(10)[:4, :]
    image_basis = []
    for i in range(4):
        for j in range(4):
            x = s.zeros(10)
            x[i, j] = 1
            image = pmap*x*pmap.T
            image_basis.append(image.reshape(16, 1))
    require(s.Matrix.hstack(*image_basis).rank() == 16,
            "Full Mat4 preserver-image negative control failed")
    require(source_block(pmap*s.eye(10)*pmap.T).rank() == 28,
            "Non-minimum image of an invertible target control failed")

    # The output-dimension hypothesis matters: a 6-by-6 corner preserver
    # on Mat10 has an entirely singular kernel, of maximum rank eight.
    large = s.eye(10)[:6, :]
    singular = s.zeros(10)
    for i in range(4):
        singular[i, 6+i] = 1
        singular[6+i, i] = 1
    require(large*singular*large.T == s.zeros(6) and singular.rank() == 8,
            "Oversized-output negative control failed")
    return {"source_examples": records,
            "rank_one_preserver_image_dimension_can_be": 16,
            "invertible_target_source_image_rank_can_be": 28,
            "oversized_output": {"target_size": 10, "output_size": 6,
                                 "sum_factor_ranks": 12,
                                 "maximum_kernel_matrix_rank": 8,
                                 "kernel_contains_invertible": False}}


def arithmetic_controls():
    pairs = [(rb, rc) for rb in range(1, 111) for rc in range(1, 111)]
    minimum_forced = [(rb, rc) for rb, rc in pairs
                      if 16 <= 224-rb-rc < 20]
    strict_minimum_excluded = [(rb, rc) for rb, rc in pairs if 224-rb-rc < 16]
    excluded_by_gap_continuation = [(rb, rc) for rb, rc in pairs if rb+rc >= 205]
    require(len(minimum_forced)+len(strict_minimum_excluded)
            == len(excluded_by_gap_continuation), "Rank-sum partition failed")
    require(all(max(rb, rc)-96 >= 7 for rb, rc in excluded_by_gap_continuation),
            "Rank-sum unit-image floor failed")
    individual = []
    for r in range(106, 111):
        d = 112-r
        require(13+d <= 19 and 16-d > 2, "Individual rank continuation budget failed")
        individual.append({"long_leading_rank": r, "source_column_defect": d,
                           "rank_one_lift_upper_bound": 13+d,
                           "unit_image_rank_lower_bound": 16-d})
    require(13+(112-105) == 20 and 224-102-102 == 20,
            "First unexcluded rank budgets changed")
    return {"normalized_rank_pairs": len(pairs),
            "strict_minimum_exclusions": len(strict_minimum_excluded),
            "additional_gap_exclusions": len(minimum_forced),
            "rank_sum_exclusions": len(excluded_by_gap_continuation),
            "individual_rank_controls": individual,
            "maximum_remaining_individual_rank": 105,
            "maximum_remaining_rank_sum": 204,
            "first_unexcluded_individual_source_budget": 20,
            "first_unexcluded_sum_source_budget": 20,
            "boundary_is_construction": False}


@lru_cache(maxsize=1)
def report():
    return {"proof_status": "proof-written-unreviewed", "improves_omega": False,
            "scope": "Finite exact controls; no exhaustive Laurent search or formal proof.",
            "source_pin_count": check_sources(),
            "random_seeds": {"factored_maps": 106204, "fixed_factor_maps": 410},
            "factor_kernels": factor_kernel_controls(),
            "fixed_factor_kernels": fixed_factor_controls(),
            "boundaries": boundary_controls(),
            "rank_budgets": arithmetic_controls()}


def verify(record):
    check_sources()
    require(record == report(), "Changed rank-gap controls or theorem scope")
    return {"factored_or_transpose_kernel_units": len(record["factor_kernels"]),
            "fixed_factor_kernel_units": len(record["fixed_factor_kernels"]),
            "explicit_source_ranks": [r["source_slice_rank_with_coherent_middle"]
                                      for r in record["boundaries"]["source_examples"]],
            "negative_boundary_controls": 2,
            "normalized_rank_pairs": record["rank_budgets"]["normalized_rank_pairs"],
            "source_pin_count": record["source_pin_count"],
            "maximum_remaining_individual_rank": 105,
            "maximum_remaining_rank_sum": 204,
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Regenerate the exact controls")
    args = parser.parse_args()
    if args.write:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(json.dumps(report(), indent=2, sort_keys=True)+"\n")
    print(json.dumps(verify(json.loads(RESULT.read_text())), indent=2, sort_keys=True))
