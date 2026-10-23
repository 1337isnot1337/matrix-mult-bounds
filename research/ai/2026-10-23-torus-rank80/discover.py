"""Discover the small coherent and source minors for the rank-80 frontier."""

from __future__ import annotations

import argparse
from itertools import combinations, product
import json
from pathlib import Path
import random


SHORT = tuple(product(range(4), repeat=2))
SOURCE = tuple(product(range(4), range(7), range(4)))
SHAPES = tuple(shape for shape in product(range(5), repeat=4)
               if all(shape[i] >= shape[i + 1] for i in range(3)))
PROFILES = ((16, 16, 12, 4, 3), (16, 16, 11, 4, 4), (16, 15, 12, 4, 4))


def matrices():
    coherent = {coordinate: [0] * 28 for coordinate in SHORT}
    source = {coordinate: [0] * 112 for coordinate in SOURCE}
    for row, column in product(range(28), repeat=2):
        j, ell = divmod(row, 7)
        h, r = divmod(column, 4)
        coordinate = h - j, ell - r
        if coordinate in coherent:
            coherent[coordinate][row] |= 1 << column
    for row, column in product(range(112), repeat=2):
        jp, ell = divmod(row, 7)
        j, p = divmod(jp, 4)
        hq, r = divmod(column, 4)
        h, q = divmod(hq, 4)
        coordinate = h - j, p + q, ell - r
        if coordinate in source:
            source[coordinate][row] |= 1 << column
    return coherent, source


def matrix_sum(basis, coordinates, size):
    rows = [0] * size
    for coordinate in coordinates:
        for row, value in enumerate(basis[coordinate]):
            rows[row] ^= value
    return rows


def find_minor(rows, target):
    basis, row_indices, column_indices = {}, [], []
    for index, original in enumerate(rows):
        row = original
        while row:
            column = row.bit_length() - 1
            if column not in basis:
                basis[column] = row
                row_indices.append(index)
                column_indices.append(column)
                break
            row ^= basis[column]
        if len(basis) == target:
            return row_indices, column_indices
    return None


def mask(indices):
    return hex(sum(1 << index for index in indices))


def minor_record(coordinates, inventory, minor, shape=None):
    rows, columns = minor
    record = {"coefficient_mask": mask(inventory.index(coordinate) for coordinate in coordinates),
              "minor_rows_mask": mask(rows), "minor_columns_mask": mask(columns)}
    if shape is not None:
        record = {"shape": shape, **record}
    return record


def coherent_records(basis, volume, rank):
    records = []
    for shape in SHAPES:
        if sum(shape) != volume:
            continue
        allowed = [coordinate for coordinate in SHORT if coordinate[1] < shape[coordinate[0]]]
        witness = None
        for count in range(1, 4):
            for chosen in combinations(allowed, count):
                minor = find_minor(matrix_sum(basis, chosen, 28), rank)
                if minor is not None:
                    witness = minor_record(chosen, SHORT, minor, shape)
                    break
            if witness:
                break
        if witness is None:
            raise ArithmeticError("no sparse coherent witness found")
        records.append(witness)
    return records


def source_ideals():
    ideals = []
    for profile in PROFILES:
        layers = [[shape for shape in SHAPES if sum(shape) == volume] for volume in profile]
        for candidate in product(*layers):
            if candidate[3] not in ((4, 0, 0, 0), (1, 1, 1, 1)):
                continue
            if all(candidate[k][i] >= candidate[k + 1][i] for k in range(4) for i in range(4)):
                ideals.append(candidate + ((0, 0, 0, 0), (0, 0, 0, 0)))
    return sorted(ideals)


def discover():
    coherent, source = matrices()
    pair = ((0, 1), (1, 0))
    pair_minor = find_minor(matrix_sum(coherent, pair, 28), 20)
    if pair_minor is None:
        raise ArithmeticError("rank20 pair failed discovery")
    records = []
    for shape in source_ideals():
        allowed = [coordinate for coordinate in SOURCE if coordinate[2] < shape[coordinate[1]][coordinate[0]]]
        # Reset for each ideal. Acceptance never reconstructs these choices.
        generator = random.Random(0)
        chosen = [coordinate for coordinate in allowed if generator.randrange(2)]
        minor = find_minor(matrix_sum(source, chosen, 112), 80)
        if minor is None:
            raise ArithmeticError("the fixed source candidate has no rank80 minor")
        records.append(minor_record(chosen, SOURCE, minor, shape))
    return {"schema": "torus-rank80-minors-v1", "coefficient_domain": "integers 0 and 1",
            "verification_modulus": 2,
            "mask_encoding": "canonical hexadecimal; bit n selects index n",
            "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
            "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
            "coherent20_pair": minor_record(pair, SHORT, pair_minor),
            "coherent9_ideals": coherent_records(coherent, 9, 24),
            "coherent13_ideals": coherent_records(coherent, 13, 28),
            "source51_ideals": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n")
    print("Discovered candidate minors: one rank20 pair, seven coherent9 ideals, three coherent13 ideals, 24 source51 ideals.")
    print("Run the separate exact acceptance replay before using these candidates.")


if __name__ == "__main__":
    main()
