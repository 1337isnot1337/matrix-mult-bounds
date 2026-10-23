#!/usr/bin/env python3
"""Replay the exact seven-point twisted-cubic incidence screen for T4."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results/mixed-family-twisted-cubic-screen-2026-10-23"
INPUT = RESULTS / "input-points.json"
OUTPUT = RESULTS / "certificate.json"


def rref(matrix: list[list[Fraction]], ncols: int) -> tuple[list[list[Fraction]], list[int]]:
    rows = [[Fraction(value) for value in row] for row in matrix]
    pivots: list[int] = []
    pivot_row = 0
    for column in range(ncols):
        selected = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]), None
        )
        if selected is None:
            continue
        rows[pivot_row], rows[selected] = rows[selected], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row != pivot_row and rows[row][column]:
                scale = rows[row][column]
                rows[row] = [
                    value - scale * pivot_value
                    for value, pivot_value in zip(rows[row], rows[pivot_row])
                ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return rows, pivots


def nullspace(matrix: list[list[int]], ncols: int) -> tuple[list[list[Fraction]], int]:
    reduced, pivots = rref(matrix, ncols)
    basis: list[list[Fraction]] = []
    for free_column in (column for column in range(ncols) if column not in pivots):
        vector = [Fraction(0)] * ncols
        vector[free_column] = Fraction(1)
        for row, pivot_column in enumerate(pivots):
            vector[pivot_column] = -reduced[row][free_column]
        basis.append(vector)
    return basis, len(pivots)


def rank(matrix: list[list[Fraction]], ncols: int) -> int:
    return len(rref(matrix, ncols)[1])


def main() -> None:
    source = json.loads(INPUT.read_text())
    points = source["points"]
    quadratic_pairs = [tuple(pair) for pair in source["quadratic_monomials"]]
    cubic_monomials = [
        exponents
        for exponents in itertools.product(range(4), repeat=4)
        if sum(exponents) == 3
    ]
    cubic_position = {exponents: index for index, exponents in enumerate(cubic_monomials)}

    def quadratic_evaluation(point: list[int]) -> list[int]:
        return [point[left] * point[right] for left, right in quadratic_pairs]

    point_quadrics = [quadratic_evaluation(point) for point in points]

    def syzygy_dimension(indices: tuple[int, ...]) -> tuple[int, int]:
        quadrics, evaluation_rank = nullspace([point_quadrics[index] for index in indices], 10)
        if evaluation_rank != 7 or len(quadrics) != 3:
            raise AssertionError("every seven-point set must impose seven independent conditions")

        # The columns are the twelve products x_k*q_j in the 20-dimensional cubic space.
        products = [[Fraction(0) for _ in range(12)] for _ in cubic_monomials]
        for quadric_index, quadric in enumerate(quadrics):
            for variable in range(4):
                column = 4 * quadric_index + variable
                for coefficient, (left, right) in zip(quadric, quadratic_pairs):
                    exponents = [0, 0, 0, 0]
                    exponents[left] += 1
                    exponents[right] += 1
                    exponents[variable] += 1
                    products[cubic_position[tuple(exponents)]][column] += coefficient
        return evaluation_rank, 12 - rank(products, 12)

    seven_sets: dict[tuple[int, ...], int] = {}
    for indices in itertools.combinations(range(len(points)), 7):
        evaluation_rank, dimension = syzygy_dimension(indices)
        assert evaluation_rank == 7
        seven_sets[indices] = dimension

    seven_by_dimension: dict[str, list[list[int]]] = {}
    for indices, dimension in seven_sets.items():
        seven_by_dimension.setdefault(str(dimension), []).append(
            [index + 1 for index in indices]
        )

    larger_sets: dict[str, dict[str, object]] = {}
    for size in (8, 9, 10):
        minima: Counter[int] = Counter()
        rows: list[dict[str, object]] = []
        for indices in itertools.combinations(range(len(points)), size):
            subset_dimensions = [
                seven_sets[seven]
                for seven in itertools.combinations(indices, 7)
            ]
            minimum = min(subset_dimensions)
            minima[minimum] += 1
            rows.append(
                {
                    "indices_one_based": [index + 1 for index in indices],
                    "minimum_seven_subset_syzygy_dimension": minimum,
                }
            )
        larger_sets[str(size)] = {
            "count_by_minimum_seven_subset_syzygy_dimension": {
                str(dimension): count for dimension, count in sorted(minima.items())
            },
            "all_seven_subsets_pass_necessary_dimension_at_least_two": sum(
                count for dimension, count in minima.items() if dimension >= 2
            ),
            "sets": rows,
        }

    result = {
        "status": "exact finite rational linear-algebra certificate",
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "field": "Q; ranks remain the same after extension to C",
        "point_count": len(points),
        "quadratic_evaluation_rank_distribution_for_seven_point_sets": {"7": len(seven_sets)},
        "seven_point_sets_by_linear_syzygy_dimension": {
            key: {"count": len(value), "sets_one_based": value}
            for key, value in sorted(seven_by_dimension.items(), key=lambda item: int(item[0]))
        },
        "larger_sets": larger_sets,
        "necessary_condition": (
            "A limit of projectively transformed twisted cubics supplies a limiting 3-space of "
            "quadrics with at least two independent linear syzygies. If seven target points "
            "impose rank 7 on quadrics, their common-quadric space has dimension 3 and must "
            "have syzygy dimension at least 2 to lie on such a limit."
        ),
        "scope": (
            "Rules out termwise convergence of eight or more of the ten source evaluation "
            "factors to the ten displayed T4 interpolation factors under one common varying "
            "shared-space change of basis. It does not rule out a general degeneration, "
            "other target decompositions, collisions, or cancellations."
        ),
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(
        "seven-set syzygy dimensions:",
        {key: len(value) for key, value in sorted(seven_by_dimension.items())},
    )
    for size, entry in larger_sets.items():
        print(
            f"{size}-sets:",
            entry["count_by_minimum_seven_subset_syzygy_dimension"],
            "passing necessary screen:",
            entry["all_seven_subsets_pass_necessary_dimension_at_least_two"],
        )


if __name__ == "__main__":
    main()
