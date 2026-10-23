"""Discover seven matching and forced-cover witnesses for defect(12,12)."""

from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path


def shapes():
    return [shape for shape in product(range(5), repeat=4)
            if sum(shape) == 10 and all(shape[i] >= shape[i + 1] for i in range(3))]


def graph(shape):
    neighbors = [set() for _ in range(28)]
    for row, column in product(range(28), repeat=2):
        j, ell = divmod(row, 7)
        h, r = divmod(column, 4)
        i, s = h - j, ell - r
        if 0 <= i < 4 and 0 <= s < shape[i]:
            neighbors[row].add(column)
    return neighbors


def maximum_matching(neighbors):
    owner = {}

    def augment(row, seen):
        for column in sorted(neighbors[row]):
            if column in seen:
                continue
            seen.add(column)
            if column not in owner or augment(owner[column], seen):
                owner[column] = row
                return True
        return False

    for row in range(28):
        augment(row, set())
    return sorted((row, column) for column, row in owner.items())


def forced_cover(neighbors, matching):
    row_match = {row: index for index, (row, column) in enumerate(matching)}
    column_match = {column: index for index, (row, column) in enumerate(matching)}
    for side in ("rows", "columns"):
        forced, steps = set(), []
        while len(forced) < len(matching):
            old = len(forced)
            for index, (row, column) in enumerate(matching):
                if index in forced:
                    continue
                if side == "rows":
                    edges = [(row, other) for other in sorted(neighbors[row])
                             if other not in column_match or column_match[other] in forced]
                else:
                    edges = [(other, column) for other in range(28) if column in neighbors[other]
                             and (other not in row_match or row_match[other] in forced)]
                if edges:
                    steps.append({"matching_index": index, "forcing_edge": edges[0]})
                    forced.add(index)
            if len(forced) == old:
                break
        if len(forced) == len(matching):
            return {"side": side, "steps": steps}
    raise ArithmeticError("matching did not admit a complete one-sided forcing certificate")


def discover():
    records = []
    for shape in shapes():
        neighbors = graph(shape)
        matching = maximum_matching(neighbors)
        if len(matching) not in (24, 28):
            raise ArithmeticError("unexpected matching size")
        records.append({"shape": shape, "matching": matching,
                        "forced_cover": forced_cover(neighbors, matching) if len(matching) == 24 else None})
    return {"schema": "a4-defect12-matching-certificates-v1", "field_of_application": "C",
            "source_layer": 0, "coherent_coordinate_order": "(i,s), 0<=i,s<4",
            "row_index": "7*j+L", "column_index": "4*H+r",
            "row_deletion_budget": 12, "column_deletion_budget": 12,
            "size10_ideals": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    document = discover()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, indent=2) + "\n")
    print(json.dumps({"ideals": len(document["size10_ideals"]),
                      "matching_sizes": [len(record["matching"]) for record in document["size10_ideals"]],
                      "acceptance_required": True}))


if __name__ == "__main__":
    main()
