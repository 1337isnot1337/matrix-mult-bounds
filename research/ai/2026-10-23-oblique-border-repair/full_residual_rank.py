#!/usr/bin/env python3
"""Exact inputs to the full one-dependency residual's ordinary-rank proof.

The two-leg projection lemma and the core lower bound are written proofs.
This standard-library verifier checks their concrete support hypotheses,
the inherited upper bound, and the actual exported n=6 source maps.
"""

import argparse
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from math import comb
from pathlib import Path
import re


PACKAGE = Path(__file__).resolve().parent
REPOSITORY = PACKAGE.parents[2]
PREDECESSOR = PACKAGE.with_name("2026-10-23-oblique-paired-repair")


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add(*tensors):
    result = {}
    for tensor in tensors:
        for key, value in tensor.items():
            result[key] = result.get(key, 0) + value
    return {key: value for key, value in result.items() if value}


def outer(first, second, third):
    return {(a, b, c): x * y * z
            for a, x in first.items()
            for b, y in second.items()
            for c, z in third.items()}


def records(tensor):
    return [list(key) + [value] for key, value in sorted(tensor.items())]


def vector_records(vectors):
    return [[[index, value] for index, value in sorted(vector.items())]
            for vector in vectors]


def expand(tensor, bases):
    return add(*(outer({i: value * x for i, x in bases[0][a].items()},
                       bases[1][b], bases[2][c])
                 for (a, b, c), value in tensor.items()))


def unit_rank(tensor, leg):
    """Sparse integer elimination; unit pivots certify every characteristic."""
    rows = {}
    for key, value in tensor.items():
        column = tuple(key[index] for index in range(3) if index != leg)
        rows.setdefault(key[leg], {})[column] = value
    basis = {}
    pivots = []
    for index in sorted(rows):
        row = dict(rows[index])
        while row:
            pivot = min(row)
            if pivot not in basis:
                value = row[pivot]
                require(abs(value) == 1, "A flattening pivot is not a unit")
                basis[pivot] = {key: value * x for key, x in row.items()}
                pivots.append([index, list(pivot), value])
                break
            factor = row[pivot]
            for key, value in basis[pivot].items():
                updated = row.get(key, 0) - factor * value
                if updated:
                    row[key] = updated
                else:
                    row.pop(key, None)
    return len(basis), pivots


def unit_minor(vectors, selected_rows):
    require(len(vectors) == len(selected_rows), "An embedding minor is not square")
    matrix = [[vector.get(row, 0) for vector in vectors] for row in selected_rows]
    work = [row[:] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next((i for i in range(column, len(work)) if work[i][column]), None)
        require(pivot is not None, "The displayed support vectors are dependent")
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            determinant *= -1
        value = work[column][column]
        require(abs(value) == 1, "An embedding minor requires a nonunit pivot")
        determinant *= value
        for i in range(column + 1, len(work)):
            factor = work[i][column] * value
            work[i] = [x - factor * y for x, y in zip(work[i], work[column])]
    return {"rows": selected_rows, "determinant": determinant}


def family_data(b):
    if type(b) is not int or b < 2:
        raise ValueError("Require an integer b>=2; n=b+2 and r=b+1.")
    r, s = b + 1, b - 1
    wings = [i for i in range(r) if i not in (0, s)]
    first = [{r * s: 1}, {s: 1}, {r * s + s: 1}]
    first += [{r * s + j: 1} for j in wings]
    first += [{r * i + s: 1} for i in wings]
    second = [{4 * s: 1, 1: -1}, {4 * s + 2: 1, 3: -1},
              {0: 1}, {1: 1}, {4 * s + 1: 1}]
    second += [{4 * i + h: 1} for i in wings for h in (0, 1)]
    third = [{0: 1}, {2 * r: 1}, {s: 1, 2 * r: -1},
             {r + s: 1, 3 * r: -1}, {2 * r + s: 1}]
    third += [{h * r + j: 1} for j in wings for h in (0, 2)]
    core_module = load_module("full_residual_core_input", PACKAGE / "ordinary_rank.py")
    core = core_module.canonical_core()
    horizontal, vertical = {}, {}
    for index in range(len(wings)):
        horizontal[3 + index, 0, 5 + 2 * index] = 1
        horizontal[3 + index, 1, 6 + 2 * index] = 1
        vertical[3 + len(wings) + index, 5 + 2 * index, 2] = 1
        vertical[3 + len(wings) + index, 6 + 2 * index, 3] = 1
    return r, s, wings, [first, second, third], core, horizontal, vertical


def inherited_formula(b):
    """The prior three-term formula specialized to its one bad mode s."""
    r, s = b + 1, b - 1
    terms = []
    xx = [{4 * s: 1, 1: -1}, {4 * s + 2: 1, 3: -1}]
    yy = [{s: 1, 2 * r: -1}, {r + s: 1, 3 * r: -1}]
    for j, h in product(range(r), range(2)):
        terms.append(outer({r * s + j: 1}, xx[h], {2 * h * r + j: 1}))
    for i, h in product(range(r), range(2)):
        terms.append(outer({r * i + s: 1}, {4 * i + h: 1}, yy[h]))
    terms.append(outer({r * s + s: -1}, xx[0], yy[0]))
    return add(*terms)


def check_family(b, expected_residual=None):
    r, s, wings, bases, core, horizontal, vertical = family_data(b)
    concise = add(core, horizontal, vertical)
    actual = expand(concise, bases)
    expected = inherited_formula(b) if expected_residual is None else expected_residual
    require(actual == expected, "The core and wings do not equal the full residual")

    upper = load_module("full_residual_ordinary_upper", PREDECESSOR / "karatsuba_repair.py")
    upper_terms = upper.one_dependency_terms(b + 2, b)
    require(upper.expand_terms(upper_terms) == actual,
            "The inherited ordinary upper bound does not equal this residual")
    require(len(upper_terms) == 4 * r - 1, "The ordinary upper term count changed")

    first_rows = [next(iter(vector)) for vector in bases[0]]
    second_rows = [4 * s, 4 * s + 2, 0, 1, 4 * s + 1]
    second_rows += [4 * i + h for i in wings for h in (0, 1)]
    third_rows = [0, 2 * r, s, r + s, 2 * r + s]
    third_rows += [h * r + j for j in wings for h in (0, 2)]
    minors = [unit_minor(vectors, rows) for vectors, rows
              in zip(bases, [first_rows, second_rows, third_rows])]
    require(all(minor["determinant"] == 1 for minor in minors),
            "A support-basis determinant changed")
    flattenings = [unit_rank(concise, leg) for leg in range(3)]
    dimensions = [2 * r - 1, 2 * r + 1, 2 * r + 1]
    require([rank for rank, _ in flattenings] == dimensions,
            "The claimed concise dimensions are incorrect")
    horizontal_rank, horizontal_pivots = unit_rank(horizontal, 2)
    vertical_rank, vertical_pivots = unit_rank(vertical, 1)
    require(horizontal_rank == vertical_rank == 2 * (r - 2),
            "The peeled long support has the wrong dimension")
    require(set(a for a, _, _ in horizontal).isdisjoint(a for a, _, _ in add(core, vertical)),
            "The horizontal first support is not separate")
    require(set(c for _, _, c in horizontal).isdisjoint(c for _, _, c in add(core, vertical)),
            "The horizontal third support is not separate")
    require(set(a for a, _, _ in vertical).isdisjoint(a for a, _, _ in core),
            "The vertical first support is not separate")
    require(set(bb for _, bb, _ in vertical).isdisjoint(bb for _, bb, _ in core),
            "The vertical second support is not separate")
    return {
        "b": b, "n": b + 2, "r": r, "sole_bad_mode": s,
        "wing_indices": wings,
        "original_format": [r * r, 4 * r, 4 * r],
        "concise_format": dimensions,
        "integer_embedding_bases": [vector_records(vectors) for vectors in bases],
        "embedding_unit_minors": minors,
        "concise_tensor_coefficients": records(concise),
        "flattening_unit_pivots": [pivots for _, pivots in flattenings],
        "horizontal_third_support_unit_pivots": horizontal_pivots,
        "vertical_second_support_unit_pivots": vertical_pivots,
        "horizontal_peel_dimension": horizontal_rank,
        "vertical_peel_dimension": vertical_rank,
        "core_ordinary_rank_from_written_proof": 7,
        "ordinary_rank_lower_bound_from_written_proof": 7 + horizontal_rank + vertical_rank,
        "ordinary_rank_upper_bound": len(upper_terms),
        "exact_ordinary_rank": 4 * r - 1,
        "border_rank_flattening_lower_bound": 2 * r + 1,
        "inherited_formal_border_upper_bound": 4 * r - 2,
        "full_residual_identity": True,
        "inherited_ordinary_terms_replayed": True,
        "support_splittings_checked": True,
        "original_target_coordinates_compared": 16 * r ** 4,
    }


def replay_native_witness(saved_case=None):
    if saved_case is None:
        saved = json.loads((PREDECESSOR / "witness.json").read_text())
        saved_case = next(case for case in saved["cases"]
                          if case["variant"] == "product-oblique")
    require(saved_case["source"] == [6, 4] and saved_case["target"] == [5, 4, 5],
            "The actual-source control has the wrong source or target")

    def integer(value):
        fraction = Fraction(value)
        require(fraction.denominator == 1, "A source-map entry is not integral")
        return int(fraction)

    maps = [[[integer(value) for value in row] for row in matrix]
            for matrix in saved_case["maps"]]
    require([len(matrix) for matrix in maps] == [25, 20, 20],
            "Wrong source-map output dimensions")
    require(all(len(row) == 36 for matrix in maps for row in matrix),
            "Wrong source-map input dimensions")
    columns = [[{i: row[j] for i, row in enumerate(matrix) if row[j]}
                for j in range(36)] for matrix in maps]
    images = []
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        source = (6 * p + q, 9 * y + q + v, 4 * (p + y) + v)
        images.append(outer(*(columns[leg][source[leg]] for leg in range(3))))
    image = add(*images)
    target = {(5 * i + j, 4 * i + h, 5 * h + j): 1
              for i, h, j in product(range(5), range(4), range(5))}
    residual = add(target, {key: -value for key, value in image.items()})
    saved_residual = {(a, bb, c): integer(value)
                      for a, bb, c, value in saved_case["verification"]["residual_coefficients"]}
    require(residual == saved_residual == inherited_formula(4),
            "The actual exported maps do not have the claimed residual")
    check_family(4, expected_residual=residual)
    return {"source_coefficients_contracted": len(images),
            "target_coordinates_compared": 10000,
            "nonzero_residual_coefficients": len(residual),
            "saved_maps_and_residual_replayed": True,
            "adapted_core_and_wings_replayed": True}


def source_pins(repository=REPOSITORY):
    source = json.loads((PACKAGE / "sources.json").read_text())
    inherited = source["local_sources"]
    followup = source["full_ordinary_rank_followup"]["local_sources"]
    for record in inherited + followup:
        path = Path(repository) / record["path"]
        require(hashlib.sha256(path.read_bytes()).hexdigest() == record["sha256"],
                "Source hash mismatch: " + record["path"])
    return {"inherited_sources": len(inherited), "followup_sources": len(followup),
            "all_match": True}


def build_certificate():
    pins = source_pins()
    core = load_module("full_residual_core_check", PACKAGE / "ordinary_rank.py")
    core.verify_saved(PACKAGE / "ordinary-rank-certificate.json")
    controls = [check_family(b) for b in [2, 3, 4, 5, 6, 7, 8, 12]]
    return {
        "claim": "AI-OBLIQUE-FULL-ORDINARY-RANK-004",
        "statement": "For b>=2,n=b+2,r=b+1, the fixed product-oblique residual has ordinary rank 4*r-1 over every field.",
        "verification_scope": "Exact support and coefficient inputs to the written projection proof; not a decomposition search.",
        "source_pin_verification": pins,
        "controls": controls,
        "native_n6_control": replay_native_witness(),
        "n6_ordinary_rank": 19,
        "n6_border_rank_interval": [11, 18],
        "first_leg_Koszul_note": {
            "support": "A tensor (span(X,Z) tensor C + B tensor span(R,S))",
            "rank_ceiling": "2*binom(a,p)+2*binom(a,p+1)",
            "n6_middle_matrix_shape": [11 * comb(9, 5), 11 * comb(9, 4)],
            "n6_middle_rank_ceiling": 2 * comb(9, 4) + 2 * comb(9, 5),
            "n6_rank_one_divisor": comb(8, 4),
            "n6_rank_required_to_prove_border_at_least_18": 17 * comb(8, 4) + 1,
            "exact_Koszul_rank_computation_claimed": False,
        },
        "whole_residual_border_rank_optimality_claimed": False,
        "arbitrary_source_map_optimality_claimed": False,
        "historical_novelty_claimed": False,
        "independent_mathematical_review": False,
        "formalized": False,
        "improves_omega": False,
    }


def verify_saved(path):
    actual = build_certificate()
    require(json.loads(Path(path).read_text()) == actual,
            "Saved full-residual ordinary-rank certificate does not replay")
    return actual


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=PACKAGE / "full-residual-rank-certificate.json")
    args = parser.parse_args()
    report = build_certificate()
    encoded = json.dumps(report, indent=2)
    encoded = re.sub(r"\[[\d,\s\[\]-]*\]",
                     lambda match: json.dumps(json.loads(match.group()), separators=(", ", ": ")),
                     encoded)
    args.output.write_text(encoded + "\n")
    print(json.dumps({"certificate": str(args.output), "passed": True,
                      "family_controls": len(report["controls"]),
                      "n6_ordinary_rank": 19, "n6_border_rank_interval": [11, 18]}))
