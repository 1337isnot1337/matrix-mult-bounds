"""Exact incidence check for the shared factors in the T_4 interpolation."""
import argparse
import json
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path


def nodes_and_points():
    """Return grid labels and projective integer representatives of w_(i,j)."""
    labels = []
    points = []
    for i in range(4):
        for j in range(4 - i):
            k = 3 - i - j
            # The exact interpolation factor has the extra nonzero scalar
            # 1/(i! j! k!). Remove it, then choose a projective sign.
            point = [
                (-1) ** k * comb(k, x - i)
                if 0 <= x - i <= k else 0
                for x in range(4)
            ]
            first = next(value for value in point if value)
            if first < 0:
                point = [-value for value in point]
            labels.append([i, j, k])
            points.append(point)
    return labels, points


def quadratic_evaluation_matrix(points):
    monomials = list(combinations_with_replacement(range(4), 2))
    matrix = [[point[i] * point[j] for i, j in monomials]
              for point in points]
    return monomials, matrix


def determinant_bareiss(matrix):
    """Exact determinant over Z using fraction-free Gaussian elimination."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError("determinant requires a square matrix")
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise ArithmeticError("Bareiss division was not exact")
                a[i][j] = numerator // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def projectively_distinct(points):
    normalized = set()
    for point in points:
        first = next(value for value in point if value)
        normalized.add(tuple(value // first for value in point))
    return len(normalized) == len(points)


def report():
    labels, points = nodes_and_points()
    monomials, matrix = quadratic_evaluation_matrix(points)
    det = determinant_bareiss(matrix)
    return {
        "status": "exact finite incidence certificate",
        "source_shared_curve": "twisted cubic [1:t:t^2:t^3]",
        "target_interpolation_nodes_ijk": labels,
        "target_shared_points_projective_integer_representatives": points,
        "quadratic_monomials_lexicographic_pairs": [list(pair) for pair in monomials],
        "quadratic_evaluation_matrix": matrix,
        "quadratic_evaluation_determinant": det,
        "points_projectively_distinct": projectively_distinct(points),
        "no_nonzero_quadric_contains_all_target_points": det != 0,
        "scope": (
            "excludes a termwise limit of the ten-point source evaluation "
            "decomposition to the ten shared factors in the displayed T_4 "
            "interpolation certificate; not a general border-degeneration obstruction"
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = report()
    if data["quadratic_evaluation_determinant"] != 1:
        raise SystemExit("unexpected quadratic evaluation determinant")
    if not data["points_projectively_distinct"]:
        raise SystemExit("target shared points are not distinct")
    rendered = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
