#!/usr/bin/env python3
"""Exact finite controls for the fixed long-leg correction obstruction."""

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


MAPS = ("zero", "identity", "transpose", "rank-one", "diagonal-shift", "dense-rational")


def first_leg_map(n, name):
    """Build one rational linear map from the source A leg to the target."""
    result = [[Fraction(0) for _ in range(n * n)] for _ in range(n * n)]
    for p in range(n):
        for q in range(n):
            source = p * n + q
            if name == "zero":
                continue
            if name == "identity":
                result[source][p * n + q] = 1
            elif name == "transpose":
                result[source][q * n + p] = 1
            elif name == "rank-one":
                result[source][0] = p + 2 * q + 1
            elif name == "diagonal-shift":
                for t in range(4):
                    i, h = q + t, p + t
                    if i < n and h < n:
                        result[source][i * n + h] += 1
            elif name == "dense-rational":
                for i in range(n):
                    for h in range(n):
                        numerator = (p + 1) * (h + 1) + (q + 1) * (i + 1)
                        denominator = p + q + i + h + 1
                        result[source][i * n + h] = Fraction(numerator, denominator)
            else:
                raise ValueError(f"unknown first-leg map: {name}")
    return result


def correction(n, first_map):
    """Build target minus the source image under the coordinate long maps."""
    out = defaultdict(Fraction)
    for p in range(n):
        for q in range(n):
            source = p * n + q
            for y in range(4):
                for v in range(4):
                    s, z = q + v, p + y
                    if s >= n or z >= n:
                        continue
                    for first, coefficient in enumerate(first_map[source]):
                        if coefficient:
                            out[(first, s * 4 + y, v * n + z)] -= coefficient

    for i in range(n):
        for h in range(n):
            for j in range(4):
                out[(i * n + h, i * 4 + j, j * n + h)] += 1
    return {key: value for key, value in out.items() if value}


def projected_matrix(n, tensor, inner_pair):
    """Project to one pair (y,v), with (s,z) rows and first-leg columns."""
    y, v = inner_pair
    matrix = [[Fraction(0) for _ in range(n * n)] for _ in range(n * n)]
    for (first, second, third), value in tensor.items():
        s, source_y = divmod(second, 4)
        source_v, z = divmod(third, n)
        if (source_y, source_v) == (y, v):
            matrix[s * n + z][first] += value
    return matrix


def formula_matrix(n, first_map, inner_pair):
    """Build the projected coefficient matrix from the proof formulas."""
    y, v = inner_pair
    matrix = [[Fraction(0) for _ in range(n * n)] for _ in range(n * n)]
    for s in range(n):
        for z in range(n):
            row = s * n + z
            matrix[row][row] = 1
            if (y, v) == (0, 0):
                source = z * n + s
            elif (y, v) == (1, 1) and s > 0 and z > 0:
                source = (z - 1) * n + s - 1
            else:
                continue
            matrix[row] = [value - coefficient for value, coefficient in zip(matrix[row], first_map[source])]
    return matrix


def rank(matrix):
    """Gaussian elimination over the rationals, including rectangular matrices."""
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    result = 0
    for column in range(columns):
        pivot = next((i for i in range(result, rows) if work[i][column]), None)
        if pivot is None:
            continue
        work[result], work[pivot] = work[pivot], work[result]
        scale = work[result][column]
        work[result] = [value / scale for value in work[result]]
        for i in range(rows):
            if i != result and work[i][column]:
                scale = work[i][column]
                work[i] = [a - scale * b for a, b in zip(work[i], work[result])]
        result += 1
        if result == rows:
            break
    return result


def verify(max_n):
    if type(max_n) is not int or max_n < 1:
        raise ValueError("max_n must be a positive integer")
    records = []
    for name in MAPS:
        sizes = []
        for n in range(1, max_n + 1):
            first_map = first_leg_map(n, name)
            tensor = correction(n, first_map)
            blocks = []
            for pair in ((0, 0), (1, 1)):
                projected = projected_matrix(n, tensor, pair)
                formula = formula_matrix(n, first_map, pair)
                if projected != formula:
                    raise AssertionError(f"coefficient formula disagrees for {name}, n={n}, pair={pair}")
                blocks.extend(projected)
            projected_rank = rank(blocks)
            if projected_rank != n * n:
                raise AssertionError(
                    f"stacked projected rank {projected_rank} != {n*n} for {name}, n={n}"
                )
            sizes.append({"n": n, "stacked_projected_rank_over_Q": projected_rank})
        records.append({"first_leg_map": name, "sizes": sizes})
    return {
        "claim": "AI-Q64-FIXED-LONG-COORDINATES-001",
        "exact_rational_replay": True,
        "projection": "stacked (0,0) and (1,1) inner-coordinate blocks",
        "all_size_argument": "proof.md, diagonal recurrence from boundary rows",
        "first_leg_maps_tested": len(MAPS),
        "cases": records,
        "general_q_maps_excluded": False,
        "exponent_improvement": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=6)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.max_n)
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
    print(serialized, end="")
