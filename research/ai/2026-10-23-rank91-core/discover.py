"""Export the two small new certificates for the rank91 endpoint obstruction."""

import argparse
from itertools import product
import json
from pathlib import Path
import random


SHORT = tuple(product(range(4), repeat=2))
SOURCE = tuple(product(range(4), range(7), range(4)))
CORE = ((4, 4, 4, 4), (4, 4, 4, 0), (4, 4, 0, 0), (4, 4, 0, 0),
        (4, 4, 0, 0), (4, 0, 0, 0), (0, 0, 0, 0))


def entries(coordinates, size):
    result = {coordinate: [0]*size for coordinate in coordinates}
    for row, column in product(range(size), repeat=2):
        if size == 28:
            j, ell = divmod(row, 7)
            h, r = divmod(column, 4)
            coordinate = h-j, ell-r
        else:
            jp, ell = divmod(row, 7)
            j, p = divmod(jp, 4)
            hq, r = divmod(column, 4)
            h, q = divmod(hq, 4)
            coordinate = h-j, p+q, ell-r
        if coordinate in result:
            result[coordinate][row] |= 1 << column
    return result


def minor(rows, wanted):
    pivots, chosen_rows, chosen_columns = {}, [], []
    for index, value in enumerate(rows):
        while value:
            column = value.bit_length()-1
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


def record(chosen, coordinates, basis, size, rank):
    rows = [0]*size
    for coordinate in chosen:
        for index, bits in enumerate(basis[coordinate]):
            rows[index] ^= bits
    witness = minor(rows, rank)
    if witness is None:
        return None
    selected_rows, selected_columns = witness
    return {"coefficient_mask": mask(coordinates.index(c) for c in chosen),
            "minor_rows_mask": mask(selected_rows), "minor_columns_mask": mask(selected_columns)}


def discover():
    coherent = entries(SHORT, 28)
    source = entries(SOURCE, 112)
    pairs = []
    for d, rank in ((1, 20), (2, 24), (3, 26)):
        witness = record([(d, 0), (0, d)], SHORT, coherent, 28, rank)
        if witness is None:
            raise ArithmeticError("Coherent binomial certificate was not found")
        pairs.append({"d": d, "rank_lower": rank, **witness})
    allowed = [c for c in SOURCE if c[2] < CORE[c[1]][c[0]]]
    generator = random.Random(0)
    for trial in range(64):
        chosen = [c for c in allowed if generator.randrange(2)]
        witness = record(chosen, SOURCE, source, 112, 91)
        if witness is not None:
            return {"schema": "rank91-core-minors-v1", "verification_modulus": 2,
                    "coefficient_domain": "integers 0 and 1", "coherent_pairs": pairs,
                    "core": {"layers": CORE, "dimension": 56, "rank_lower": 91, **witness}}, trial+1
    raise ArithmeticError("No core minor in the bounded64-mask discovery search")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document, attempts = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2)+"\n")
    print(json.dumps({"core_binary_attempts": attempts, "acceptance_required": True}))


if __name__ == "__main__":
    main()
