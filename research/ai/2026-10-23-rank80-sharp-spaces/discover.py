"""Discover integer minor certificates for the sharp rank80 dimension cap."""

from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[3]
SHORT = tuple(product(range(4), repeat=2))
SOURCE = tuple(product(range(4), range(7), range(4)))
SHAPES = tuple(shape for shape in product(range(5), repeat=4)
               if all(shape[i] >= shape[i + 1] for i in range(3)))
CHILDREN = {shape: tuple(child for child in SHAPES
                        if all(child[i] <= shape[i] for i in range(4)))
            for shape in SHAPES}
SHARP_SHAPE = ((4, 4, 4, 4), (4, 4, 4, 4), (4, 4, 4, 0),
               (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))


def source_ideals(volume=45):
    chosen = []

    def visit(k, remaining):
        if k == 7:
            if remaining == 0:
                yield tuple(chosen)
            return
        parent = chosen[-1] if chosen else (4, 4, 4, 4)
        for shape in CHILDREN[parent]:
            size = sum(shape)
            if size > remaining or size * (7 - k) < remaining:
                continue
            if k == 2 and size > 12:
                continue
            if k == 3 and shape[0] >= 2 and shape[1] >= 1:
                continue
            if k == 5 and size and sum(chosen[1]) > 8:
                continue
            chosen.append(shape)
            yield from visit(k + 1, remaining - size)
            chosen.pop()

    return tuple(visit(0, volume))


def source_basis():
    result = {coordinate: {} for coordinate in SOURCE}
    for row, column in product(range(112), repeat=2):
        jp, ell = divmod(row, 7)
        j, p = divmod(jp, 4)
        hq, r = divmod(column, 4)
        h, q = divmod(hq, 4)
        coordinate = h - j, p + q, ell - r
        if coordinate in result:
            values = result[coordinate]
            values[row] = values.get(row, 0) | (1 << column)
    return result


def find_minor(rows, rank):
    pivots, selected_rows, selected_columns = {}, [], []
    for index, original in enumerate(rows):
        row = original
        while row:
            column = row.bit_length() - 1
            if column not in pivots:
                pivots[column] = row
                selected_rows.append(index)
                selected_columns.append(column)
                break
            row ^= pivots[column]
        if len(pivots) == rank:
            return selected_rows, selected_columns
    return None


def mask(indices):
    return hex(sum(1 << index for index in indices))


def discover_record(shape, basis, rank):
    allowed = [coordinate for coordinate in SOURCE
               if coordinate[2] < shape[coordinate[1]][coordinate[0]]]
    generator = random.Random(0)
    for trial in range(32):
        chosen = [coordinate for coordinate in allowed if generator.randrange(2)]
        rows = [0] * 112
        for coordinate in chosen:
            for row, bits in basis[coordinate].items():
                rows[row] ^= bits
        minor = find_minor(rows, rank)
        if minor is not None:
            selected_rows, selected_columns = minor
            return {"shape": shape,
                    "coefficient_mask": mask(SOURCE.index(coordinate) for coordinate in chosen),
                    "minor_rows_mask": mask(selected_rows),
                    "minor_columns_mask": mask(selected_columns)}, trial + 1
    raise ArithmeticError("no witness in the bounded discovery batch")


def discover():
    old = json.loads((ROOT / "results/torus-rank80-2026-10-23/certificates.json").read_text())
    basis = source_basis()
    records, trials = [], {}
    for shape in source_ideals():
        record, count = discover_record(shape, basis, 80)
        records.append(record)
        trials[count] = trials.get(count, 0) + 1
    sharp, _ = discover_record(SHARP_SHAPE, basis, 79)
    cover_rows = [(4 * j + p) * 7 + ell for j, p, ell in product(range(4), range(4), range(7))
                  if p == 0 or (p == 1 and j == 3)]
    cover_columns = [(4 * h + q) * 4 + r for h, q, r in product(range(7), range(4), range(4))
                     if (q == 0 and h <= 5) or (q == 1 and h <= 4)]
    document = {
        "schema": "rank80-sharp-spaces-minors-v1",
        "coefficient_domain": "integers 0 and 1", "verification_modulus": 2,
        "mask_encoding": "canonical hexadecimal; bit n selects index n",
        "coherent_coordinate_order": "(i,s) lexicographic on range(4) x range(4)",
        "source_coordinate_order": "(i,k,s) lexicographic on range(4) x range(7) x range(4)",
        "coherent20_pair": old["coherent20_pair"],
        "coherent9_ideals": old["coherent9_ideals"],
        "coherent13_ideals": old["coherent13_ideals"],
        "source45_ideals": records,
        "sharp44_space": {"shape": SHARP_SHAPE, "cover_rows_mask": mask(cover_rows),
                          "cover_columns_mask": mask(cover_columns), "rank79_minor": sharp},
    }
    return document, trials


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document, trials = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Keep each large-family witness on one line so the finite inventory is
    # inspectable without an eighty-thousand-line formatting-only expansion.
    items = []
    for key, value in document.items():
        if key == "source45_ideals":
            encoded = "[\n" + ",\n".join("    " + json.dumps(record, separators=(",", ":"))
                                             for record in value) + "\n  ]"
        else:
            encoded = json.dumps(value, separators=(",", ":"))
        items.append("  " + json.dumps(key) + ": " + encoded)
    args.output.write_text("{\n" + ",\n".join(items) + "\n}\n")
    print(json.dumps({"source45_ideals": len(document["source45_ideals"]),
                      "binary_attempt_histogram": trials, "sharp_space_dimension": 44,
                      "acceptance_required": True}, sort_keys=True))


if __name__ == "__main__":
    main()
