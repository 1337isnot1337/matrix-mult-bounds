"""Export exact witnesses for the sharp A4 source dimensions below ranks92/96."""

import argparse
from itertools import product
import json
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[3]
SOURCE = tuple(product(range(4), range(7), range(4)))


def source_basis():
    """Matrix-entry reconstruction, separate from acceptance's literal sum."""
    basis = {coordinate: {} for coordinate in SOURCE}
    for row, column in product(range(112), repeat=2):
        jp, ell = divmod(row, 7)
        j, p = divmod(jp, 4)
        hq, r = divmod(column, 4)
        h, q = divmod(hq, 4)
        coordinate = h-j, p+q, ell-r
        if coordinate in basis:
            values = basis[coordinate]
            values[row] = values.get(row, 0) | (1 << column)
    return basis


def minor(rows, wanted):
    pivots, selected_rows, selected_columns = {}, [], []
    for index, value in enumerate(rows):
        while value:
            column = value.bit_length()-1
            if column not in pivots:
                pivots[column] = value
                selected_rows.append(index)
                selected_columns.append(column)
                break
            value ^= pivots[column]
        if len(pivots) == wanted:
            return selected_rows, selected_columns
    return None


def mask(indices):
    return hex(sum(1 << index for index in indices))


def sharp_record(m, basis):
    allowed = [n for n, (i, k, s) in enumerate(SOURCE)
               if i < 2 or (i == 2 and k < m) or (i == 3 and k == 0)]
    wanted = 83+4*m
    generator = random.Random(0)
    for trial in range(256):
        selected = [n for n in allowed if generator.randrange(2)]
        rows = [0]*112
        for n in selected:
            for row, value in basis[SOURCE[n]].items():
                rows[row] ^= value
        witness = minor(rows, wanted)
        if witness is not None:
            selected_rows, selected_columns = witness
            row_cover = [(4*3+0)*7+ell for ell in range(7)]
            column_cover = [(4*h+q)*4+r for h, q, r in product(range(7), range(4), range(4))
                            if h <= 4 or (h == 5 and q < m-1)]
            return {
                "m": m, "dimension": len(allowed), "rank_upper": wanted,
                "row_cover_mask": mask(row_cover), "column_cover_mask": mask(column_cover),
                "coefficient_mask": mask(selected),
                "minor_rows_mask": mask(selected_rows),
                "minor_columns_mask": mask(selected_columns),
            }, trial+1
    raise ArithmeticError("No exact witness in the bounded 256-choice discovery search")


def discover():
    old = json.loads((ROOT / "results/torus-rank80-2026-10-23/certificates.json").read_text())
    basis = source_basis()
    records, trials = [], []
    for m in (2, 3):
        record, attempts = sharp_record(m, basis)
        records.append(record)
        trials.append(attempts)
    return {
        "schema": "rank92-rank96-source-caps-v1",
        "coefficient_domain": "integers 0 and 1", "verification_modulus": 2,
        "coherent20_pair": old["coherent20_pair"],
        "coherent9_ideals": old["coherent9_ideals"],
        "coherent13_ideals": old["coherent13_ideals"],
        "sharp_spaces": records,
    }, trials


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document, trials = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print(json.dumps({"binary_attempts": trials, "acceptance_required": True}))


if __name__ == "__main__":
    main()
