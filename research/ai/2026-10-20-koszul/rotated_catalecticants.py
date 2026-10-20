"""Exact checks of the arbitrary-constant-shared-basis obstruction."""
import argparse
import json
from pathlib import Path

import sympy as sp


def block_matrix(p, q, j):
    d = p.rows - 1
    return sp.Matrix([[p[r + s, a + c]
                       for s in range(d - q + 1) for c in range(d - j + 1)]
                      for r in range(q + 1) for a in range(j + 1)])


def lower_bound(d, q, j):
    return 1 + min(q + j, 2 * d - q - j)


def bases(m):
    permutation = list(range(m))
    permutation[0], permutation[1] = permutation[1], permutation[0]
    return {
        "identity": sp.eye(m),
        "pascal": sp.Matrix([[sp.binomial(i, j) for j in range(m)] for i in range(m)]),
        "vandermonde": sp.Matrix([[(i + 1) ** j for j in range(m)] for i in range(m)]),
        "swap_0_1": sp.eye(m)[:, permutation],
    }


def report(max_m=6):
    records = []
    for m in range(2, max_m + 1):
        for name, p in bases(m).items():
            assert p.det() != 0
            ranks = [[int(block_matrix(p, q, j).rank()) for j in range(m)]
                     for q in range(m)]
            assert all(ranks[q][j] >= lower_bound(m - 1, q, j)
                       for q in range(m) for j in range(m))
            records.append({"m": m, "basis": name, "determinant": str(p.det()),
                            "ranks": ranks})
    return {"status": "exact finite checks of an unreviewed written proof",
            "new_exponent_established": False,
            "block_rank_cases": sum(r["m"] ** 2 for r in records),
            "records": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=6)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = report(args.max_m)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}))
