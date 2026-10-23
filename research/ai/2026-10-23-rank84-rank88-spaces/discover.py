"""Export the small witnesses for the sharp source caps below ranks84/88."""

from itertools import product
import argparse
import json
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parents[3]
SOURCE = tuple(product(range(4), range(7), range(4)))


def source_basis():
    result = {coordinate: {} for coordinate in SOURCE}
    # Matrix-entry reconstruction, separate from acceptance's six-index sum.
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


def minor(rows, wanted):
    pivots, chosen_rows, chosen_columns = {}, [], []
    for index, value in enumerate(rows):
        while value:
            column = value.bit_length() - 1
            if column not in pivots:
                pivots[column] = value
                chosen_rows.append(index)
                chosen_columns.append(column)
                break
            value ^= pivots[column]
        if len(pivots) == wanted:
            return chosen_rows, chosen_columns
    return None


def mask(indices):
    return hex(sum(1 << index for index in indices))


def sharp_record(middle_cutoff, basis):
    allowed = [n for n, (i, k, s) in enumerate(SOURCE)
               if i < 2 or (i == 2 and k < middle_cutoff)]
    wanted = 80 + 4 * middle_cutoff
    generator = random.Random(0)
    for trial in range(256):
        selected = [n for n in allowed if generator.randrange(2)]
        rows = [0] * 112
        for n in selected:
            for row, value in basis[SOURCE[n]].items():
                rows[row] ^= value
        witness = minor(rows, wanted)
        if witness is not None:
            chosen_rows, chosen_columns = witness
            return {
                "d": 2, "m": middle_cutoff, "dimension": len(allowed),
                "rank_upper": wanted, "coefficient_mask": mask(selected),
                "minor_rows_mask": mask(chosen_rows),
                "minor_columns_mask": mask(chosen_columns),
            }, trial + 1
    raise ArithmeticError("No witness in the bounded 256-choice search")


def discover():
    old = json.loads((ROOT / "results/torus-rank80-2026-10-23/certificates.json").read_text())
    basis = source_basis()
    records, trials = [], []
    for middle_cutoff in (0, 1):
        record, attempts = sharp_record(middle_cutoff, basis)
        records.append(record)
        trials.append(attempts)
    return {
        "schema": "rank84-rank88-source-caps-v1",
        "coefficient_domain": "integers 0 and 1",
        "verification_modulus": 2,
        "coherent20_pair": old["coherent20_pair"],
        "coherent9_ideals": old["coherent9_ideals"],
        "coherent13_ideals": old["coherent13_ideals"],
        "sharp_spaces": records,
        "boundary_space": {"d": 2, "m": 2, "dimension": 64, "rank_upper": 88},
    }, trials


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document, trials = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n")
    print(json.dumps({"binary_attempts": trials, "acceptance_required": True}))


if __name__ == "__main__":
    main()
