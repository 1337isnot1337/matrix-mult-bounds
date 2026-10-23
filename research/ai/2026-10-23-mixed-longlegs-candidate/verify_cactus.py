#!/usr/bin/env python3
"""Exact coefficient controls for cactus_rank.md; standard library only.

The finite checks certify input conventions and interpolation witnesses.
The lower bound for arbitrary finite schemes is proved in cactus_rank.md.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import prod
from pathlib import Path


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
INPUT = PACKAGE / "discovery_input.json"
OUTPUT = ROOT / "results/mixed-longlegs-candidate-2026-10-23/cactus_rank_verification.json"
INPUT_SHA256 = "c53abefde0cb5d5e2e816f96ae6c257ee843f59e6c28d13a6ae1994de9ab88f3"

# Each tuple is (orientation, first polynomial input, second polynomial input).
# Out puts the polynomial output on the shared first leg.
BLOCK_TYPES = {
    "S": ("Full", 5, 10),
    "F2": ("Full", 5, 2),
    "F3": ("Full", 5, 3),
    "O33": ("Out", 3, 3),
    "O42": ("Out", 4, 2),
    "M2": ("Mid", 5, 2),
}
SOURCE = [("S", 10)]
TARGET = [("F2", 7), ("F3", 10), ("O33", 4), ("O42", 2), ("M2", 6)]


def literal_block(name):
    kind, u, v = BLOCK_TYPES[name]
    m = u + v - 1
    if kind == "Full":
        dimensions = (u, v, m)
        coefficients = {(i, j, i + j): 1 for i in range(u) for j in range(v)}
    elif kind == "Mid":
        dimensions = (u, m, v)
        coefficients = {(i, i + k, k): 1 for i in range(u) for k in range(v)}
    else:
        dimensions = (m, u, v)
        coefficients = {(j + k, j, k): 1 for j in range(u) for k in range(v)}
    return dimensions, coefficients


def assemble(profile):
    coefficients = {}
    b_offset = c_offset = 0
    first = None
    for name, copies in profile:
        dimensions, local = literal_block(name)
        if first is None:
            first = dimensions[0]
        if dimensions[0] != first:
            raise ValueError("The blocks do not share the full first dimension")
        for _ in range(copies):
            for (i, j, k), value in local.items():
                coefficients[i, j + b_offset, k + c_offset] = value
            b_offset += dimensions[1]
            c_offset += dimensions[2]
    return (first, b_offset, c_offset), coefficients


def rational_rank(rows):
    """Sparse row elimination over Q; input rows are column/value mappings."""
    pivots = {}
    for original in rows:
        row = {column: Fraction(value) for column, value in original.items() if value}
        while row:
            pivot = min(row)
            if pivot not in pivots:
                leading = row[pivot]
                pivots[pivot] = {column: value / leading for column, value in row.items()}
                break
            scale = row[pivot]
            for column, value in pivots[pivot].items():
                updated = row.get(column, 0) - scale * value
                if updated:
                    row[column] = updated
                else:
                    row.pop(column, None)
    return len(pivots)


def flattening_ranks(dimensions, coefficients):
    answer = []
    for mode in range(3):
        other = [axis for axis in range(3) if axis != mode]
        rows = [{} for _ in range(dimensions[mode])]
        for index, value in coefficients.items():
            column = index[other[0]] * dimensions[other[1]] + index[other[1]]
            rows[index[mode]][column] = value
        answer.append(rational_rank(rows))
    return answer


def first_slice_rank(dimensions, coefficients, alpha):
    if len(alpha) != dimensions[0]:
        raise ValueError("Incorrect first-slice dimension")
    rows = [{} for _ in range(dimensions[1])]
    for (i, j, k), value in coefficients.items():
        rows[j][k] = rows[j].get(k, 0) + value * alpha[i]
    return rational_rank(rows)


def polynomial_value(coefficients, value):
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def lagrange_row(nodes, selected):
    coefficients = [Fraction(1)]
    denominator = 1
    for node in nodes:
        if node == selected:
            continue
        expanded = [Fraction(0)] * (len(coefficients) + 1)
        for degree, value in enumerate(coefficients):
            expanded[degree] -= node * value
            expanded[degree + 1] += value
        coefficients = expanded
        denominator *= selected - node
    return [value / denominator for value in coefficients]


def interpolation_witness(name):
    kind, u, v = BLOCK_TYPES[name]
    nodes = list(range(u + v - 1))
    return {
        "block": name,
        "orientation": kind,
        "input_lengths": [u, v],
        "nodes": nodes,
        "lagrange_coefficient_rows": [
            [str(value) for value in lagrange_row(nodes, node)] for node in nodes
        ],
        "rank_one_terms": len(nodes),
    }


def verify_interpolation_witness(name, witness):
    """Accept saved rational coefficients by full tensor reconstruction."""
    kind, u, v = BLOCK_TYPES[name]
    dimensions, expected = literal_block(name)
    m = u + v - 1
    if witness.get("block") != name or witness.get("orientation") != kind:
        raise ValueError("Interpolation block label mismatch")
    if witness.get("input_lengths") != [u, v]:
        raise ValueError("Interpolation input dimensions changed")
    nodes = witness["nodes"]
    if len(nodes) != m or len(set(nodes)) != m or witness["rank_one_terms"] != m:
        raise ValueError("Interpolation requires exactly m distinct nodes")
    lagrange = [[Fraction(value) for value in row] for row in witness["lagrange_coefficient_rows"]]
    if len(lagrange) != m or any(len(row) != m for row in lagrange):
        raise ValueError("Wrong Lagrange coefficient shape")
    for i, row in enumerate(lagrange):
        for j, node in enumerate(nodes):
            if polynomial_value(row, node) != int(i == j):
                raise ValueError("Invalid exact Lagrange value")

    reconstructed = {}
    for node, output in zip(nodes, lagrange):
        first = [Fraction(node**i) for i in range(u)]
        second = [Fraction(node**j) for j in range(v)]
        if kind == "Full":
            factors = (first, second, output)
        elif kind == "Mid":
            factors = (first, output, second)
        else:
            factors = (output, first, second)
        for index in product(*(range(size) for size in dimensions)):
            value = prod(factors[axis][index[axis]] for axis in range(3))
            reconstructed[index] = reconstructed.get(index, 0) + value
    for index in product(*(range(size) for size in dimensions)):
        if reconstructed.get(index, 0) != expected.get(index, 0):
            raise ValueError(f"Tensor coefficient mismatch for {name} at {index}")
    return {
        "dimensions": list(dimensions),
        "coefficient_equalities": prod(dimensions),
        "nonzero_literal_coefficients": len(expected),
        "lagrange_value_equalities": m * m,
    }


def check_discovery_input(path):
    contents = Path(path).read_bytes()
    digest = sha256(contents).hexdigest()
    if digest != INPUT_SHA256:
        raise ValueError("Discovery input byte pin does not match the frozen candidate")
    data = json.loads(contents)
    if data["source"]["long_dimensions"] != [100, 140]:
        raise ValueError("Source dimensions changed")
    if data["target"]["long_dimensions"] != [100, 140]:
        raise ValueError("Target dimensions changed")
    expected_target = [
        ("Full", 7, [5, 2, 6]),
        ("Full", 10, [5, 3, 7]),
        ("SharedOutput", 4, [5, 3, 3]),
        ("SharedOutput", 2, [5, 4, 2]),
        ("Mid", 6, [5, 6, 2]),
    ]
    actual = [(block["kind"], block["copies"], block["dimensions"]) for block in data["target"]["blocks"]]
    if actual != expected_target:
        raise ValueError("Target profile disagrees with the literal reconstruction")
    source = data["source"]["blocks"]
    if len(source) != 1 or (source[0]["kind"], source[0]["copies"], source[0]["dimensions"]) != ("Full", 10, [5, 10, 14]):
        raise ValueError("Source profile disagrees with the literal reconstruction")
    return digest


def wild_toy_controls():
    dimensions = (2, 3, 3)
    coefficients = {(0, 0, 0): 1, (1, 0, 1): 1, (0, 1, 2): 1, (1, 2, 2): 1}
    flattenings = flattening_ranks(dimensions, coefficients)
    covectors = [[1, 0], [1, 1], [1, 2], [0, 1]]
    ranks = [first_slice_rank(dimensions, coefficients, alpha) for alpha in covectors]
    if flattenings != [2, 3, 3] or ranks != [2] * 4:
        raise ValueError("Small wild-tensor control failed")
    return {
        "profile": "Full(2,1)+Mid(2,1), with canonical shared first basis",
        "dimensions": list(dimensions),
        "nonzero_coefficients": [[*index, value] for index, value in sorted(coefficients.items())],
        "flattening_ranks": flattenings,
        "first_covectors": covectors,
        "first_slice_ranks": ranks,
        "cactus_rank": 4,
        "smoothable_rank": 4,
        "ordinary_rank": 4,
        "border_rank": 3,
        "border_rank_proof": "Section 6: dense open pencils are equivalent to (I_3, diagonal), so rank-3 tensors are dense in format (2,3,3).",
    }


def build_report(input_path=INPUT):
    digest = check_discovery_input(input_path)
    source_dimensions, source_coefficients = assemble(SOURCE)
    target_dimensions, target_coefficients = assemble(TARGET)
    source_flattenings = flattening_ranks(source_dimensions, source_coefficients)
    target_flattenings = flattening_ranks(target_dimensions, target_coefficients)
    if source_flattenings != [5, 100, 140] or target_flattenings != [5, 100, 140]:
        raise ValueError("Conciseness check failed")

    finite_parameters = [0, 1, 2, 3, 4]
    alphas = [[t**i for i in range(5)] for t in finite_parameters] + [[0, 0, 0, 0, 1]]
    source_curve_ranks = [first_slice_rank(source_dimensions, source_coefficients, alpha) for alpha in alphas]
    target_curve_ranks = [first_slice_rank(target_dimensions, target_coefficients, alpha) for alpha in alphas]
    if source_curve_ranks != [100] * 6 or target_curve_ranks != [62] * 6:
        raise ValueError("Evaluation-curve slice ranks disagree with the proof")
    generic_alpha = [1, 2, 3, 5, 7]
    generic_rank = first_slice_rank(target_dimensions, target_coefficients, generic_alpha)
    if generic_rank != 72:
        raise ValueError("Explicit rank-72 slice was not reproduced")

    block_slices = {}
    witnesses = []
    for name in BLOCK_TYPES:
        dimensions, coefficients = literal_block(name)
        block_slices[name] = [first_slice_rank(dimensions, coefficients, alpha) for alpha in alphas]
        witness = interpolation_witness(name)
        witness["verification"] = verify_interpolation_witness(name, witness)
        witnesses.append(witness)

    source_upper = sum(copies * (BLOCK_TYPES[name][1] + BLOCK_TYPES[name][2] - 1) for name, copies in SOURCE)
    target_upper = sum(copies * (BLOCK_TYPES[name][1] + BLOCK_TYPES[name][2] - 1) for name, copies in TARGET)
    target_lower = target_dimensions[1] + target_dimensions[2] - 62
    if (source_upper, target_upper, target_lower) != (140, 178, 178):
        raise ValueError("Rank arithmetic failed")
    vandermonde_determinant = prod(finite_parameters[j] - finite_parameters[i] for i in range(5) for j in range(i + 1, 5))

    return {
        "schema_version": 1,
        "input": {
            "path": "research/ai/2026-10-23-mixed-longlegs-candidate/discovery_input.json",
            "sha256": digest,
        },
        "scope": {
            "field": "complex numbers; finite coefficient controls use exact rational arithmetic",
            "identifications": "one canonical first coefficient basis shared by all blocks",
            "written_lower_bound": "research/ai/2026-10-23-mixed-longlegs-candidate/cactus_rank.md",
            "independent_first_identifications_covered_by_178_equality": False,
            "target_border_rank_determined": False,
            "degeneration_constructed": False,
        },
        "source": {
            "dimensions": list(source_dimensions),
            "nonzero_coefficients": len(source_coefficients),
            "flattening_ranks": source_flattenings,
            "interpolation_upper_bound": source_upper,
            "ordinary_rank": 140,
            "border_rank": 140,
            "curve_slice_ranks": source_curve_ranks,
        },
        "target": {
            "dimensions": list(target_dimensions),
            "nonzero_coefficients": len(target_coefficients),
            "flattening_ranks": target_flattenings,
            "curve_slice_ranks": target_curve_ranks,
            "explicit_generic_slice": generic_alpha,
            "explicit_generic_slice_rank": generic_rank,
            "generic_slice_cactus_lower_bound": target_dimensions[1] + target_dimensions[2] - generic_rank,
            "independent_first_identifications_cactus_lower_bound": 168,
            "curve_cactus_lower_bound": target_lower,
            "interpolation_upper_bound": target_upper,
            "cactus_rank": 178,
            "smoothable_rank": 178,
            "ordinary_rank": 178,
            "proved_border_rank_interval": [140, 178],
            "necessary_border_rank_if_source_degeneration_exists": 140,
            "conditional_wildness_gap": 38,
        },
        "evaluation_curve": {
            "finite_parameters": finite_parameters,
            "infinity_coefficients": alphas[-1],
            "vandermonde_determinant": vandermonde_determinant,
            "block_slice_ranks_finite_then_infinity": block_slices,
        },
        "interpolation_witnesses": witnesses,
        "small_wild_tensor": wild_toy_controls(),
        "coverage": {
            "literal_tensors": 3,
            "full_flattening_ranks": 9,
            "full_curve_slice_ranks": 12,
            "local_curve_slice_ranks": 36,
            "explicit_generic_slice_ranks": 1,
            "toy_slice_ranks": 4,
            "interpolation_identities": len(witnesses),
            "interpolation_coefficient_equalities": sum(item["verification"]["coefficient_equalities"] for item in witnesses),
            "lagrange_value_equalities": sum(item["verification"]["lagrange_value_equalities"] for item in witnesses),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=INPUT)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true", help="Compare against the existing report without writing")
    args = parser.parse_args()
    report = build_report(args.input)
    if args.check:
        if json.loads(args.output.read_text()) != report:
            raise SystemExit("Saved cactus-rank report differs from exact replay")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verified": True, "cactus_rank": 178, "ordinary_rank": 178, "target_border_rank_determined": False, "report": str(args.output), "coverage": report["coverage"]}, sort_keys=True))


if __name__ == "__main__":
    main()
