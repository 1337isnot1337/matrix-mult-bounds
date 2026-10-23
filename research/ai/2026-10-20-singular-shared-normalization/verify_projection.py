#!/usr/bin/env python3
"""Verify the explicit projected-target degeneration on every coefficient."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result or [0]


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return trim(result)


def monic_division(poly, divisor):
    assert divisor[-1] == 1
    remainder = trim(poly)
    if len(remainder) < len(divisor):
        return [0], remainder
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and remainder != [0]:
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1]
        quotient[shift] = coefficient
        for i, value in enumerate(divisor):
            remainder[shift + i] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), remainder


def evaluate(poly, value):
    answer = 0
    for coefficient in reversed(poly):
        answer = answer * value + coefficient
    return answer


def digits(poly, divisor, count):
    result = []
    remaining = list(poly)
    for _ in range(count):
        remaining, residue = monic_division(remaining, divisor)
        result.append(residue)
    assert trim(remaining) == [0]
    return result


def lagrange(node, nodes):
    numerator = [1]
    denominator = 1
    for other in nodes:
        if other != node:
            numerator = multiply(numerator, [-other, 1])
            denominator *= node - other
    return [Fraction(value, denominator) for value in numerator]


def pair_indices(degree):
    return [(a, total - a) for total in range(degree + 1)
            for a in range(total + 1)]


def verify_size(s):
    m = 2 * s
    degree = m - 1
    r = s + 1
    n = m * (m + 1) // 2
    nodes = list(range(r))
    g = [1]
    for node in nodes:
        g = multiply(g, [-node, 1])
    powers = [[1]]
    for _ in range(degree):
        powers.append(multiply(powers[-1], g))
    first = [lagrange(node, nodes) for node in nodes]
    pairs = pair_indices(degree)
    input_polys = []
    for a, b in pairs:
        h = degree - a - b
        residue = monic_division([0] * a + [1], g)[1]
        poly = multiply(powers[h], residue)
        assert len(poly) <= n
        input_polys.append((h, poly))
    count = 0
    negative_count = 0
    zero_count = 0
    first_order_nonzero = 0
    maximum_denominator = 1
    for j, first_poly in enumerate(first):
        for (a, b), (h, input_poly) in zip(pairs, input_polys):
            # This is the literal product in the source C(R,N), before the
            # output map is applied. It is not the target rank formula.
            source_product = multiply(first_poly, input_poly)
            expansion = digits(source_product, g, degree + 1)
            for c, d in pairs:
                v = c + d
                exponent = v - h
                coefficient = sum(node ** c * evaluate(expansion[v], node)
                                  for node in nodes)
                count += 1
                maximum_denominator = max(maximum_denominator,
                                          Fraction(coefficient).denominator)
                if exponent < 0:
                    negative_count += 1
                    assert coefficient == 0
                if exponent == 0:
                    assert a + b + c + d == degree
                    assert coefficient == nodes[j] ** (a + c)
                if exponent not in (0, 1):
                    assert coefficient == 0
                if coefficient == 0:
                    zero_count += 1
                if exponent == 1 and coefficient:
                    first_order_nonzero += 1
    return {"s": s, "m": m, "source_dimensions": [r, n, n + r - 1],
            "target_dimensions": [r, n, n],
            "target_nonshared_ranks": n - s * (s - 1) // 2,
            "g_coefficients": g,
            "coefficient_checks": count,
            "negative_exponent_zero_checks": negative_count,
            "zero_coefficients": zero_count,
            "nonzero_first_order_errors": first_order_nonzero,
            "maximum_reduced_denominator": maximum_denominator,
            "full_tensor_identity": "mapped_source = projected_target + epsilon * error"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-s", type=int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_s < 2:
        parser.error("--max-s must be at least 2")
    records = [verify_size(s) for s in range(2, args.max_s + 1)]
    report = {"status": "exact-projected-degenerations-verified",
              "constructs_full_fatpoint_target": False,
              "improves_omega": False,
              "arithmetic": "Python integers and fractions.Fraction",
              "coverage": {"coefficient_checks": sum(x["coefficient_checks"] for x in records),
                           "negative_exponent_zero_checks": sum(x["negative_exponent_zero_checks"]
                                                                 for x in records)},
              "records": records}
    serialized = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized)
        print(json.dumps({"status": report["status"], "coverage": report["coverage"],
                          "output": str(args.output)}))
    else:
        print(serialized, end="")


if __name__ == "__main__":
    main()
