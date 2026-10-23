"""Exact standard-library higher Koszul ranks by occupancy and torus grade.

All acceptance ranks use integer row operations valid over the rational numbers.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, gcd
import argparse
import json
from pathlib import Path


SOURCE = {"F10": 10}
TARGET = {"F2": 7, "F3": 10, "O33": 4, "O42": 2, "M2": 6}


@lru_cache(None)
def tensor(name):
    if name.startswith("F"):
        b = int(name[1:])
        return b, b + 4, [(i, j, i + j) for i in range(5) for j in range(b)], list(range(b)), [-k for k in range(b + 4)]
    if name.startswith("M"):
        c = int(name[1:])
        return c + 4, c, [(i, i + j, j) for i in range(5) for j in range(c)], [-k for k in range(c + 4)], list(range(c))
    b, c = int(name[1]), int(name[2])
    return b, c, [(j + k, j, k) for j in range(b) for k in range(c)], [-j for j in range(b)], [-k for k in range(c)]


def oriented(name, axis):
    b, c, entries, wb, wc = tensor(name)
    if axis == "B":
        return b, c, entries, wb, wc
    return c, b, [(a, z, y) for a, y, z in entries], wc, wb


def graded_matrices(names, occupancy, axis="B"):
    """Return integer matrices, one per grade, of one occupancy component."""
    blocks = [oriented(name, axis) for name in names]
    groups = {}
    row_indices = {}
    row_options = [list(combinations(range(x), q)) for (x, _, _, _, _), q in zip(blocks, occupancy)]
    for subsets in product(*row_options):
        weight = sum(sum(block[3][j] for j in subset) for block, subset in zip(blocks, subsets))
        for a in range(5):
            grade = a + weight
            group = groups.setdefault(grade, {"rows": 0, "columns": []})
            row_indices[a, subsets] = (grade, group["rows"])
            group["rows"] += 1
    for selected, (xdim, ydim, entries, _, wy) in enumerate(blocks):
        column_options = [list(combinations(range(block[0]), q - (j == selected)))
                          for j, (block, q) in enumerate(zip(blocks, occupancy))]
        by_y = [[] for _ in range(ydim)]
        for a, x, y in entries:
            by_y[y].append((a, x))
        for subsets in product(*column_options):
            weight = sum(sum(block[3][j] for j in subset) for block, subset in zip(blocks, subsets))
            for y in range(ydim):
                grade = weight - wy[y]
                column = {}
                for a, x in by_y[y]:
                    if x in subsets[selected]:
                        continue
                    output = list(subsets)
                    output[selected] = tuple(sorted(subsets[selected] + (x,)))
                    row_grade, row = row_indices[a, tuple(output)]
                    if row_grade != grade:
                        raise ValueError("torus grade mismatch")
                    sign = (-1) ** (sum(occupancy[:selected]) + sum(j < x for j in subsets[selected]))
                    column[row] = column.get(row, 0) + sign
                groups.setdefault(grade, {"rows": 0, "columns": []})["columns"].append(column)
    answer = {}
    for grade, group in groups.items():
        columns = group["columns"]
        matrix = [[0] * len(columns) for _ in range(group["rows"])]
        for j, col in enumerate(columns):
            for i, value in col.items():
                matrix[i][j] = value
        answer[grade] = matrix
    return answer


def rational_rank(matrix):
    """Fraction-free primitive-row elimination over the rational numbers."""
    basis = {}
    for original in matrix:
        row = {j: value for j, value in enumerate(original) if value}
        while row:
            col = min(row)
            if col not in basis:
                divisor = 0
                for value in row.values():
                    divisor = gcd(divisor, value)
                if row[col] < 0:
                    divisor = -divisor
                if divisor != 1:
                    row = {j: value // divisor for j, value in row.items()}
                basis[col] = row
                break
            pivot = basis[col]
            x, y = row[col], pivot[col]
            divisor = gcd(x, y)
            x, y = x // divisor, y // divisor
            if y != 1:
                row = {j: value * y for j, value in row.items()}
            for j, value in pivot.items():
                new = row.get(j, 0) - x * value
                if new:
                    row[j] = new
                else:
                    row.pop(j, None)
            if row:
                divisor = 0
                for value in row.values():
                    divisor = gcd(divisor, value)
                if divisor > 1:
                    row = {j: value // divisor for j, value in row.items()}
    return len(basis)


def partitions(total, bound=None):
    if total == 0:
        yield ()
        return
    for first in range(min(total, bound or total), 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def components(profile, degree):
    names = list(profile)
    for occupancy in partitions(degree + 1):
        for indices in product(range(len(names)), repeat=len(occupancy)):
            if any(occupancy[j] == occupancy[j + 1] and indices[j] > indices[j + 1]
                   for j in range(len(indices) - 1)):
                continue
            selected = tuple(names[j] for j in indices)
            multiplicity = 1
            for name, copies in Counter(selected).items():
                if copies > profile[name]:
                    multiplicity = 0
                    break
                multiplicity *= factorial(profile[name]) // factorial(profile[name] - copies)
            for copies in Counter(zip(selected, occupancy)).values():
                multiplicity //= factorial(copies)
            if multiplicity:
                yield selected, occupancy, multiplicity


def calculate(profile, degree, axis="B"):
    output = []
    total = 0
    for names, occupancy, count in components(profile, degree):
        matrices = graded_matrices(names, occupancy, axis)
        grades = {str(g): rational_rank(matrix) for g, matrix in sorted(matrices.items())}
        rank = sum(grades.values())
        total += count * rank
        output.append({"names": list(names), "occupancy": list(occupancy),
                       "count": count, "rank": rank, "grades": grades})
    return {"degree": degree, "axis": axis,
            "method": "rational primitive-row elimination",
            "profile": profile, "rank": total, "components": output}


def source_b_formula(degree):
    return 5 * comb(100, degree + 1) - max(4 - degree, 0) * comb(90, degree + 1)


def report():
    degrees = {}
    for degree in (1, 2, 3):
        target = calculate(TARGET, degree)
        source = source_b_formula(degree)
        if degree <= 2:
            literal_source = calculate(SOURCE, degree)
            if literal_source["rank"] != source:
                raise ValueError("literal source rank disagrees with written formula")
        else:
            literal_source = None
        if target["rank"] > source:
            raise ValueError("recorded candidate comparison changed")
        degrees[str(degree)] = {"source_rank": source,
                              "source_literal_control": literal_source,
                              "target": target,
                              "slack": source - target["rank"]}
    return {"field": "C", "status": "exact finite coefficient ranks",
            "coefficient_scope": "canonical common first basis at both endpoints",
            "source_format": [5, 100, 140], "target_format": [5, 100, 140],
            "source_b_formula": "5*binom(100,p+1)-max(4-p,0)*binom(90,p+1)",
            "source_formula_status": "separate written evaluation-kernel proof",
            "degrees": degrees,
            "all_B_degrees_pass": True,
            "all_B_degrees_reason": "p0 is the ordinary third flattening of rank140 on both endpoints; p1,p2,p3 are recorded; p>=4 has maximal source row rank by the written formula.",
            "degeneration_constructed": False, "new_exponent_established": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({p: {"source": v["source_rank"], "target": v["target"]["rank"],
                         "slack": v["slack"]} for p, v in result["degrees"].items()}, indent=2))


if __name__ == "__main__":
    main()
