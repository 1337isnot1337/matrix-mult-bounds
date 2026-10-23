"""Exact changed-source-basis control outside the fixed spin/radix family.

Claim AI-SPIN-BASIS-ESCAPE-126.  Standard-library replay only.  The output
is not M9; three of its coefficients violate the fixed-family identity124.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from spin_fiber_compression import LOCAL

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "results/anisotropic-constructions-2026-10-20"
PREFIX = "parity_structure_spin_basis_escape"
CLAIM = "AI-SPIN-BASIS-ESCAPE-126"
MATRICES = [[[1, 1], [0, 1]], [[1, 0], [-1, 1]], [[0, 1], [-1, 0]]]
POINTS = [[0, 1, 39], [30, 31, 39], [30, 31, 69]]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, column))
             for column in zip(*b)] for row in a]


def inverse(a):
    n = len(a)
    work = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for column in range(n):
        pivot = next((i for i in range(column, n) if work[i][column]), None)
        if pivot is None:
            raise ArithmeticError("Singular change of source basis")
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        work[column] = [x / scale for x in work[column]]
        for i in range(n):
            if i != column and work[i][column]:
                scale = work[i][column]
                work[i] = [x - scale * y for x, y in zip(work[i], work[column])]
    return [row[n:] for row in work]


def kron(a, b):
    return [[x * y for x in ar for y in br] for ar in a for br in b]


def symmetric_square(g):
    (a, b), (c, d) = g
    return [[a * a, a * b, b * b],
            [2 * a * c, a * d + b * c, 2 * b * d],
            [c * c, c * d, d * d]]


def local_numerators(matrices):
    for (a, b), (c, d) in matrices:
        if a * d - b * c != 1:
            raise ArithmeticError("The control requires three SL2 matrices")
    dual = [transpose(inverse(symmetric_square(g))) for g in matrices]
    answer = []
    for leg in range(3):
        action = kron(kron(matrices[(leg + 2) % 3], dual[leg]),
                      matrices[(leg + 1) % 3])
        rows = multiply(LOCAL, transpose(action))
        if any(Fraction(x).denominator != 1 for row in rows for x in row):
            raise ArithmeticError("The chosen local control lost integrality")
        answer.append([[int(x) for x in row] for row in rows])
    return answer


def compress(low):
    """The high local digit is LOCAL; all raw weights equal one."""
    answer = [[[0] * 112 for _ in range(81)] for _ in range(3)]
    for lo, hi in product(range(12), repeat=2):
        i0, remainder = divmod(lo, 6)
        m0, s0 = divmod(remainder, 2)
        i1, remainder = divmod(hi, 6)
        m1, s1 = divmod(remainder, 2)
        column = ((i0 + 2 * i1) * 7 + m0 + 2 * m1) * 4 + s0 + 2 * s1
        for rl, rh in product(range(9), repeat=2):
            row = 9 * (rl // 3 + 3 * (rh // 3)) + rl % 3 + 3 * (rh % 3)
            for leg in range(3):
                answer[leg][row][column] += low[leg][rl][lo] * LOCAL[rh][hi]
    return answer


def sparse(matrix):
    return [[i, j, x] for i, row in enumerate(matrix)
            for j, x in enumerate(row) if x]


def dense(entries, shape):
    a = [[0] * shape[1] for _ in range(shape[0])]
    used = set()
    for i, j, x in entries:
        if not (0 <= i < shape[0] and 0 <= j < shape[1]) or (i, j) in used:
            raise ArithmeticError("Invalid or repeated sparse map coordinate")
        if not isinstance(x, int) or x == 0:
            raise ArithmeticError("Sparse map entries must be nonzero integers")
        used.add((i, j))
        a[i][j] = x
    return a


def source_terms(n):
    m = 2 * n - 1
    for i, p, r, j, q, s in product(range(n), repeat=6):
        yield ((i * m + p + q) * n + s,
               (p * m + r + s) * n + j,
               (r * m + i + j) * n + q)


def local_output(maps):
    columns = []
    for matrix in maps:
        columns.append([[(i, row[j]) for i, row in enumerate(matrix) if row[j]]
                        for j in range(12)])
    output = Counter()
    for x, y, z in source_terms(2):
        for (a, u), (b, v), (c, w) in product(columns[0][x], columns[1][y], columns[2][z]):
            output[a, b, c] += u * v * w
    return output


def selected_coefficients(maps):
    answer = [0] * len(POINTS)
    for x, y, z in source_terms(4):
        for k, (a, b, c) in enumerate(POINTS):
            answer[k] += maps[0][a][x] * maps[1][b][y] * maps[2][c][z]
    return answer


def witness():
    local = local_numerators(MATRICES)
    full = compress(local)
    return {
        "claim": CLAIM,
        "source_basis_matrices": MATRICES,
        "local": {"shape": [9, 12], "denominators": [2, 2, 2],
                  "maps": [sparse(m) for m in local]},
        "compressed": {"source": "A(4,4)", "shape": [81, 112],
                       "denominators": [4, 4, 4], "maps": [sparse(m) for m in full]},
        "selected_points": POINTS,
        "selected_numerators_over64": [64, 128, 448],
        "linear_combination_numerator_over64": 384,
    }


def verify(data=None):
    if data is None:
        data = json.loads((OUT / (PREFIX + "_witness.json")).read_text())
    if data != witness():
        raise ArithmeticError("Saved maps or coefficient claims differ from the exact construction")
    local = [dense(m, [9, 12]) for m in data["local"]["maps"]]
    full = [dense(m, [81, 112]) for m in data["compressed"]["maps"]]
    output = local_output(local)
    expected = Counter()
    for i, j, k in product(range(3), repeat=3):
        expected[3 * i + j, 3 * j + k, 3 * k + i] += 8
        expected[4 * i, 4 * j, 4 * k] += 8
    for point in product(range(9), repeat=3):
        if output[point] != expected[point]:
            raise ArithmeticError("Changed local maps fail the complete source identity")
    values = selected_coefficients(full)
    if values != data["selected_numerators_over64"]:
        raise ArithmeticError("Original A(4,4) contraction fails the selected coefficients")
    combination = values[0] - values[1] + values[2]
    if combination != 384 or combination == 0:
        raise ArithmeticError("The changed basis did not escape the fixed-family hyperplane")
    return {
        "claim": CLAIM,
        "local_source_terms": 64,
        "local_output_coefficients_checked": 729,
        "local_output": "M3 + tr(X)tr(Y)tr(Z)",
        "local_map_nonzeros": [len(x) for x in data["local"]["maps"]],
        "compressed_map_nonzeros": [len(x) for x in data["compressed"]["maps"]],
        "original_A44_terms_per_selected_coefficient": 4096,
        "selected_points": POINTS,
        "selected_numerators_over64": values,
        "linear_combination": "6",
        "claim124_linear_combination": "0",
        "M9_linear_combination": "-1",
        "fixed_family_hyperplane_escaped": True,
        "M9_constructed": False,
        "new_exponent_established": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.write:
        OUT.mkdir(parents=True, exist_ok=True)
        data = witness()
        (OUT / (PREFIX + "_witness.json")).write_text(json.dumps(data, separators=(",", ":")) + "\n")
        report = verify(data)
        (OUT / (PREFIX + "_certificate.json")).write_text(json.dumps(report, indent=2) + "\n")
    else:
        report = verify()
        saved = json.loads((OUT / (PREFIX + "_certificate.json")).read_text())
        if report != saved:
            raise ArithmeticError("Saved replay report differs from the complete exact replay")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
