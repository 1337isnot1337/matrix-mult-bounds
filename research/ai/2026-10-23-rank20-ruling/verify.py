"""Exact controls for the written rank20 classification and dimension bound."""
from __future__ import annotations

import argparse
from functools import reduce
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULT = ROOT / "results/rank20-ruling-2026-10-23/controls.json"
BASE = "fc0a139ef447a4d8640f0fdf1781836ea7fa868a"
DEPENDENCIES = {
    "research/ai/2026-10-20-anisotropic-constructions/slice_rank_gap.md",
    "research/ai/2026-10-20-anisotropic-constructions/polynomial_rank_locus.md",
    "research/ai/2026-10-23-singular-long-ruling/proof.md",
    "research/ai/2026-10-23-singular-long-ruling/verify.py",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_sources(record=None):
    if record is None:
        record = json.loads((PACKAGE / "sources.json").read_text())
    require(record["base_commit"] == BASE and record["field"] == "C",
            "Changed base or field")
    entries = record["local_dependencies"]
    require(len(entries) == len(DEPENDENCIES)
            and {e["path"] for e in entries} == DEPENDENCIES,
            "Changed dependency inventory")
    for entry in entries:
        actual = hashlib.sha256((ROOT / entry["path"]).read_bytes()).hexdigest()
        require(actual == entry["sha256"], "Source digest mismatch: " + entry["path"])
    external = record["external_dependency"]
    require(external["doi"] == "10.2307/2372388"
            and external["theorem"] == "2.1, printed page126",
            "Changed splitting dependency")
    return len(entries)


def predecessor():
    path = ROOT / "research/ai/2026-10-23-singular-long-ruling/verify.py"
    spec = importlib.util.spec_from_file_location("rank20_source_predecessor", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def splitting_controls():
    records = []
    for d in range(4):
        allowed = []
        for degrees in product(range(4*d+1), repeat=3):
            if sum(degrees) != 4*d or sum(min(4, z) for z in degrees) > 4:
                continue
            if d >= 2:
                require(sorted(degrees) == [0, 0, 4*d],
                        "Unexpected splitting degrees at rank20")
            allowed.append(list(degrees))
        records.append({"primitive_degree": d, "admissible_degrees": allowed})
    require([len(c["admissible_degrees"]) for c in records] == [1, 15, 3, 3],
            "Incomplete splitting-degree enumeration")
    return records


def gcd_degree(expressions, x, y, scalar=None):
    domain = s.QQ if scalar is None else s.QQ.frac_field(scalar)
    polynomials = [s.Poly(s.expand(e), x, y, domain=domain) for e in expressions if e != 0]
    require(bool(polynomials), "GCD control needs a nonzero vector")
    return int(reduce(lambda a, b: a.gcd(b), polynomials).total_degree())


def pencil_controls():
    x, y, t = s.symbols("x y t")
    records = []
    for h in (x*x, y*y, (x-y)**2, x*x+y*y):
        f = s.Matrix([h*x, h*y, 0, 0])
        g = s.Matrix([0, h*x, h*y, 0])
        require(f.row_join(g).rank() == 2, "Dependent positive pencil control")
        joint = gcd_degree(list(f)+list(g), x, y)
        generic = gcd_degree(list(f+t*g), x, y, t)
        require(joint == generic == 2, "Generic-pencil shared divisor failed")
        records.append({"divisor": str(s.expand(h)), "rational_function_rank": 2,
                        "joint_gcd_degree": joint, "generic_gcd_degree": generic})
    f = s.Matrix([x**3, x*x*y, 0, 0])
    g = s.Matrix([0, x*y*y, y**3, 0])
    require(f.row_join(g).rank() == 2, "Invalid divisor-loss negative control")
    joint = gcd_degree(list(f)+list(g), x, y)
    generic = gcd_degree(list(f+t*g), x, y, t)
    require(joint == generic == 0, "Independent pencil falsely kept a quadratic divisor")
    independent_negative = {"rational_function_rank": 2, "joint_gcd_degree": joint,
                            "generic_gcd_degree": generic}
    # Without independence, a new scalar quadratic can vary in every pencil.
    f = s.Matrix([x**3, x*x*y, 0, 0])
    g = s.Matrix([x*y*y, y**3, 0, 0])
    require(f.row_join(g).rank() == 1, "Invalid dependent-pencil negative control")
    joint = gcd_degree(list(f)+list(g), x, y)
    generic = gcd_degree(list(f+t*g), x, y, t)
    require(joint == 0 and generic == 2,
            "Lost the independence hypothesis of the pencil lemma")
    dependent_negative = {"rational_function_rank": 1, "joint_gcd_degree": joint,
                          "generic_gcd_degree": generic}
    return records, independent_negative, dependent_negative


def divisor_coefficients(h, coefficient_matrix, transpose=False):
    result = {}
    for i in range(4):
        for j in range(4):
            value = sum(h[i-p]*coefficient_matrix[p, j]
                        for p in range(2) if 0 <= i-p < 3)
            if value:
                result[(j, 0, i) if transpose else (i, 0, j)] = value
    return result


def fixed_divisor_controls():
    source = predecessor()
    records = []
    divisors = ([1, 0, 0], [0, 0, 1], [1, -2, 1], [1, 0, 1])
    mixed = [s.Matrix([[1, 1, 1, 1], [0, 1, 2, 3]]),
             s.Matrix([[0, 0, 1, 0], [1, 0, 0, 1]])]
    for transpose in (False, True):
        for h in divisors:
            coefficient_vectors = []
            for p, j in product(range(2), range(4)):
                basis = s.zeros(2, 4)
                basis[p, j] = 1
                coefficients = divisor_coefficients(h, basis, transpose)
                coefficient_vectors.append(s.Matrix([
                    coefficients.get((i, 0, q), 0) for i, q in product(range(4), repeat=2)]))
            dimension = s.Matrix.hstack(*coefficient_vectors).rank()
            require(dimension == 8, "Fixed-divisor source space lost dimension")
            basis = s.zeros(2, 4)
            basis[0, 0] = 1
            ranks = []
            for small in [basis]+mixed:
                coefficients = divisor_coefficients(h, small, transpose)
                ranks.append(source.exact_rank(source.source_matrix(4, coefficients)))
            require(ranks == [16, 20, 20], "Fixed-divisor source ranks failed")
            records.append({"divisor_leg": "z" if transpose else "x",
                            "quadratic_coefficients": list(h), "space_dimension": dimension,
                            "actual_source_ranks": ranks})
    return records


def a4_criterion(rank):
    require(type(rank) is int and 0 <= rank <= 110, "Invalid A4 long-map rank")
    cap = 11+2+112-rank
    applicable = cap <= 20
    margin = 16-(112-rank)-2
    return {"long_limit_rank": rank, "source_rank_cap": cap,
            "dimension_eight_bound_applies": applicable,
            "source_space_dimension_bound": 8 if applicable else None,
            "target_ruling_dimension": 10, "nonzero_lift_margin": margin,
            "excluded_by_this_criterion": applicable and margin > 0}


def report():
    pencils, independent, dependent = pencil_controls()
    cases = [a4_criterion(c) for c in range(110, 102, -1)]
    require([c["excluded_by_this_criterion"] for c in cases] == [True]*6+[False]*2,
            "Changed rank105 sufficient threshold")
    return {"scope": "Finite exact controls; universal rank20 proof is written and unreviewed.",
            "proof_status": "proof-written-unreviewed", "independent_review": False,
            "improves_omega": False, "source_pin_count": check_sources(),
            "splitting_degrees": splitting_controls(), "independent_pencils": pencils,
            "independent_divisor_loss": independent, "dependent_pencil_negative": dependent,
            "fixed_divisor_spaces": fixed_divisor_controls(), "a4_long_limit_cases": cases}


def verify(record):
    require(record == report(), "Changed controls, scope or evidence status")
    return {"fixed_divisor_spaces": len(record["fixed_divisor_spaces"]),
            "actual_source_ranks": sum(len(c["actual_source_ranks"])
                                       for c in record["fixed_divisor_spaces"]),
            "independent_pencils": len(record["independent_pencils"]),
            "splitting_degree_cases": sum(len(c["admissible_degrees"])
                                           for c in record["splitting_degrees"]),
            "a4_long_limit_cases": len(record["a4_long_limit_cases"]),
            "sharp_linear_space_dimension": 8, "minimum_excluded_long_limit_rank": 105,
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
