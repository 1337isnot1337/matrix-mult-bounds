"""Reproduce candidate integer minors; acceptance is in the separate verify.py."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path
import random


COORDINATES = tuple(product(range(4), range(3), range(4)))


def candidate_ideals():
    shapes = [shape for shape in product(range(5), repeat=4)
              if all(shape[i] >= shape[i + 1] for i in range(3))]
    ideals = []
    for a in shapes:
        for b in shapes:
            if any(x < y for x, y in zip(a, b)):
                continue
            for c in shapes:
                if any(x < y for x, y in zip(b, c)) or sum(a) + sum(b) + sum(c) != 33:
                    continue
                shape = a, b, c
                indices = [n for n, (i, k, s) in enumerate(COORDINATES) if s < shape[k][i]]
                ideals.append((shape, indices))
    return ideals


def coordinate_matrices():
    """Direct coefficient formula, independently rebuilt from literal terms in acceptance."""
    matrices = {coordinate: [0] * 112 for coordinate in COORDINATES}
    for row, column in product(range(112), repeat=2):
        jp, ell = divmod(row, 7)
        j, p = divmod(jp, 4)
        hq, r = divmod(column, 4)
        h, q = divmod(hq, 4)
        coordinate = h - j, p + q, ell - r
        if coordinate in matrices:
            matrices[coordinate][row] |= 1 << column
    return matrices


def find_minor(rows):
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
        if len(basis) == 64:
            return row_indices, column_indices
    return None


def mask(indices):
    return hex(sum(1 << index for index in indices))


def discover(seed_limit=256):
    matrices = coordinate_matrices()
    pending, records, counts = candidate_ideals(), [], Counter()
    if len(pending) != 611:
        raise ArithmeticError("unexpected discovery inventory")
    for seed in range(seed_limit):
        generator = random.Random(seed)
        selected = {n for n in range(48) if generator.getrandbits(1)}
        remaining = []
        for shape, indices in pending:
            chosen = [n for n in indices if n in selected]
            rows = [0] * 112
            for n in chosen:
                for row, value in enumerate(matrices[COORDINATES[n]]):
                    rows[row] ^= value
            minor = find_minor(rows)
            if minor is None:
                remaining.append((shape, indices))
                continue
            row_indices, column_indices = minor
            records.append({"shape": shape, "coefficient_mask": mask(chosen),
                            "minor_rows_mask": mask(row_indices),
                            "minor_columns_mask": mask(column_indices)})
            counts[seed] += 1
        pending = remaining
        if not pending:
            break
    if pending:
        raise ArithmeticError(f"discovery left {len(pending)} ideals uncovered; no certificate written")
    document = {"schema": "torus-order-ideal-minors-v1", "source": "canonical cyclic A4",
                "coefficient_domain": "integers 0 and 1", "verification_modulus": 2,
                "minor_size": 64, "ideal_size": 33,
                "coordinate_order": "(i,k,s) lexicographic on range(4) x range(3) x range(4)",
                "mask_encoding": "canonical hexadecimal; bit n selects index n",
                "records": sorted(records, key=lambda record: record["shape"])}
    return document, counts


def serialize(document):
    lines = ["{"]
    for key, value in document.items():
        if key != "records":
            lines.append(f"  {json.dumps(key)}: {json.dumps(value)},")
    lines.append('  "records": [')
    for index, record in enumerate(document["records"]):
        comma = "," if index + 1 < len(document["records"]) else ""
        lines.append("    " + json.dumps(record, separators=(",", ":")) + comma)
    return "\n".join(lines + ["  ]", "}", ""])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path,
                        help="explicit destination; this does not run acceptance")
    parser.add_argument("--seed-limit", type=int, default=256)
    args = parser.parse_args()
    document, counts = discover(args.seed_limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(serialize(document))
    print(f"Discovered {len(document['records'])} candidate minors; new certificates by seed: {dict(counts)}.")
    print("These candidates require the separate exact acceptance replay.")


if __name__ == "__main__":
    main()
