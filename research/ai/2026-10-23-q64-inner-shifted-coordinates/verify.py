#!/usr/bin/env python3
"""Exact finite controls for neighboring inner-index shifted charts."""

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


MAPS = ("zero", "identity", "transpose", "rank-one", "diagonal-shift", "dense-rational")
SHIFT_PAIRS = ((0, 0), (1, 0), (0, 1), (1, 1))


def first_leg_map(n, name):
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


def correction(n, first_map, epsilon_b, epsilon_c):
    out = defaultdict(Fraction)
    for p in range(n):
        for q in range(n):
            source = p * n + q
            for y in range(4):
                for v in range(4):
                    s = q + v - epsilon_b * y
                    z = p + y - epsilon_c * v
                    if 0 <= s < n and 0 <= z < n:
                        for first, coefficient in enumerate(first_map[source]):
                            if coefficient:
                                out[(first, s * 4 + y, v * n + z)] -= coefficient

    for i in range(n):
        for h in range(n):
            for j in range(4):
                out[(i * n + h, i * 4 + j, j * n + h)] += 1
    return {key: value for key, value in out.items() if value}


def projected_matrix(n, tensor, inner_pair):
    y, v = inner_pair
    matrix = [[Fraction(0) for _ in range(n * n)] for _ in range(n * n)]
    for (first, second, third), value in tensor.items():
        s, source_y = divmod(second, 4)
        source_v, z = divmod(third, n)
        if (source_y, source_v) == (y, v):
            matrix[s * n + z][first] += value
    return matrix


def formula_matrix(n, first_map, inner_pair, epsilon_b, epsilon_c):
    y, v = inner_pair
    matrix = [[Fraction(0) for _ in range(n * n)] for _ in range(n * n)]
    for p in range(n):
        for q in range(n):
            source = p * n + q
            if (y, v) == (0, 0):
                s, z = q, p
                matrix[s * n + z][s * n + z] += 1
            elif (y, v) == (1, 0) and q >= epsilon_b and p <= n - 2:
                s, z = q - epsilon_b, p + 1
            elif (y, v) == (0, 1) and q <= n - 2 and p >= epsilon_c:
                s, z = q + 1, p - epsilon_c
            else:
                continue
            row = s * n + z
            matrix[row] = [value - coefficient for value, coefficient in zip(matrix[row], first_map[source])]
    return matrix


def rank(matrix):
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
    cases = []
    for epsilon_b, epsilon_c in SHIFT_PAIRS:
        for name in MAPS:
            projected_ranks = []
            for n in range(1, max_n + 1):
                first_map = first_leg_map(n, name)
                tensor = correction(n, first_map, epsilon_b, epsilon_c)
                blocks = []
                for pair in ((0, 0), (1, 0), (0, 1)):
                    projected = projected_matrix(n, tensor, pair)
                    formula = formula_matrix(n, first_map, pair, epsilon_b, epsilon_c)
                    if projected != formula:
                        raise AssertionError(
                            f"formula disagrees for eps=({epsilon_b},{epsilon_c}), {name}, n={n}, pair={pair}"
                        )
                    blocks.extend(projected)
                projected_rank = rank(blocks)
                lower_bound = max(n * n - 1 - epsilon_b * epsilon_c, 0)
                if projected_rank < lower_bound:
                    raise AssertionError(
                        f"rank {projected_rank} < {lower_bound} for eps=({epsilon_b},{epsilon_c}), {name}, n={n}"
                    )
                projected_ranks.append(projected_rank)
            cases.append({
                "epsilon_b": epsilon_b,
                "epsilon_c": epsilon_c,
                "first_leg_map": name,
                "stacked_projected_ranks_over_Q": projected_ranks,
            })
    return {
        "claim": "AI-Q64-INNER-SHIFTED-COORDINATES-001",
        "exact_rational_replay": True,
        "sizes": list(range(1, max_n + 1)),
        "projection": "stacked (0,0), (1,0), and (0,1) inner-coordinate blocks",
        "shift_pairs_tested": [list(pair) for pair in SHIFT_PAIRS],
        "first_leg_maps_tested_per_shift_pair": len(MAPS),
        "cases": cases,
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
