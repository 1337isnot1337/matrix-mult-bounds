"""Exact regression certificates for the written all-size concavity proof."""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import cache
from itertools import product
import json
from pathlib import Path


@cache
def h(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive integer required")
    value = Fraction(1)
    for r in range(1, n):
        value *= Fraction(3 * r + 1, 3 * r)
    return value


def profile(a, b):
    if any(not isinstance(n, int) or n < 1 for n in (a, b)):
        raise ValueError("positive integer dimensions required")
    m, n = sorted((a, b))
    return h(m) * (n + Fraction(m - 1, 2))


def row_certificate(a, b, c, d):
    """Return all successive upper bounds in equation (3), including (2)."""
    if any(not isinstance(n, int) or n < 1 for n in (a, b, c, d)):
        raise ValueError("positive integer dimensions required")
    if b > d:
        a, b, c, d = c, d, a, b
    length = a + c - 1
    values = [
        sum((profile(length, b + d - 1 - 2 * j) for j in range(b)), Fraction()),
        b * profile(length, d),
        b * (profile(a, d) + profile(c, d) - d),
        Fraction(b, d) * profile(a, d) * profile(c, d),
        profile(a, b) * profile(c, d),
    ]
    if any(x > y for x, y in zip(values, values[1:])):
        raise ArithmeticError((a, b, c, d, values))
    return values


def verify_case(a, b, c, d):
    row = row_certificate(a, b, c, d)
    column = row_certificate(b, a, d, c)
    aa = [a + c - 1 - 2 * i for i in range(min(a, c))]
    bb = [b + d - 1 - 2 * j for j in range(min(b, d))]
    grid = [[profile(x, y) for y in bb] for x in aa]
    checks = 8  # Four ordered steps in each of two certificates.
    for values in grid:
        if sum(values) > row[0]:
            raise ArithmeticError("row domination")
        checks += 1
    for j in range(len(bb)):
        if sum(values[j] for values in grid) > column[0]:
            raise ArithmeticError("column domination")
        checks += 1
    for k in range(len(aa) + len(bb) - 1):
        diagonal = sum(grid[i][k - i] for i in range(len(aa))
                       if 0 <= k - i < len(bb))
        if diagonal > row[0]:
            raise ArithmeticError("diagonal domination")
        checks += 1
    return checks


def run(n=8):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive integer grid size required")
    checks = 0
    for a, b in product(range(1, 2 * n + 1), repeat=2):
        if profile(a, b + 1) < profile(a, b):
            raise ArithmeticError("monotonicity")
        if profile(a, 2) > 2 * profile(a, 1):
            raise ArithmeticError("sublinear boundary")
        if b >= 2 and 2 * profile(a, b) < profile(a, b - 1) + profile(a, b + 1):
            raise ArithmeticError("concavity")
        checks += 2 + (b >= 2)
    for a, b, c, d in product(range(1, n + 1), repeat=4):
        checks += verify_case(a, b, c, d)
    return {"max_source_dimension": n, "source_quadruples": n**4,
            "exact_comparisons": checks, "violations": 0,
            "arithmetic": "fractions.Fraction",
            "scope": "Finite regression for a separate written all-integer proof; no omega improvement."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-size", type=int, default=8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run(args.max_size)
    content = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    print(content, end="")
