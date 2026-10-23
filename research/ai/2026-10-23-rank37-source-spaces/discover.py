"""Discover candidate minors for the thirteen size17 source ideals."""

from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path
import random


SOURCE = tuple(product(range(4), range(7), range(4)))
SHORT = tuple(product(range(4), repeat=2))


def matrix(points, coherent=False):
    size = 28 if coherent else 112
    selected = set(points)
    rows = [0] * size
    for row, column in product(range(size), repeat=2):
        if coherent:
            j, ell = divmod(row, 7)
            h, r = divmod(column, 4)
            coordinate = h - j, ell - r
        else:
            jp, ell = divmod(row, 7)
            j, p = divmod(jp, 4)
            hq, r = divmod(column, 4)
            h, q = divmod(hq, 4)
            coordinate = h - j, p + q, ell - r
        if coordinate in selected:
            rows[row] |= 1 << column
    return rows


def minor(rows, target):
    basis, rr, cc = {}, [], []
    for index, original in enumerate(rows):
        row = original
        while row:
            column = row.bit_length() - 1
            if column not in basis:
                basis[column] = row
                rr.append(index)
                cc.append(column)
                break
            row ^= basis[column]
        if len(basis) == target:
            return rr, cc
    raise ArithmeticError("candidate has no minor of the requested rank")


def mask(indices):
    return hex(sum(1 << index for index in indices))


def record(points, coordinates, pivots, shape=None):
    rows, columns = pivots
    result = {"coefficient_mask": mask(coordinates.index(point) for point in points),
              "minor_rows_mask": mask(rows), "minor_columns_mask": mask(columns)}
    return {"shape": shape, **result} if shape is not None else result


def discover():
    shapes = [h for h in product(range(5), repeat=4) if all(h[i] >= h[i + 1] for i in range(3))]
    ideals = []
    for length in range(1, 5):
        axes = {(length, 0, 0, 0), tuple(int(i < length) for i in range(4))}
        for bottom in shapes:
            if sum(bottom) != 17 - length:
                continue
            for top in axes:
                if all(x <= y for x, y in zip(top, bottom)):
                    ideals.append((bottom, top))
    records = []
    for shape in sorted(ideals):
        allowed = [point for point in SOURCE if point[1] < 2 and point[2] < shape[point[1]][point[0]]]
        generator = random.Random(0)
        chosen = [point for point in allowed if generator.randrange(2)]
        records.append(record(chosen, SOURCE, minor(matrix(chosen), 37), shape))
    pair = ((0, 1), (1, 0))
    return {"schema": "rank37-source-minors-v1", "coefficient_domain": "integers 0 and 1",
            "verification_modulus": 2,
            "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
            "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
            "mask_encoding": "canonical hexadecimal; bit n selects index n",
            "coherent20_pair": record(pair, SHORT, minor(matrix(pair, True), 20)),
            "source17_ideals": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    document = discover()
    if len(document["source17_ideals"]) != 13:
        raise ArithmeticError("unexpected ideal inventory")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n")
    print("Discovered thirteen37-minors and the coherent20-minor; separate exact acceptance is required.")


if __name__ == "__main__":
    main()
