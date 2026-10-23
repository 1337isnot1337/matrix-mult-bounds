"""Recover SL2 x SL2 kernel types from exact bidegree rank-atlas reports."""

import argparse
import json
from pathlib import Path


def decompose_record(record):
    a = record["a"]
    p = record["p"]
    d = a - 1
    weights = {}
    for block in record["rationally_deficient_blocks"]:
        g1, g2 = block["grade"]
        weight = (2 * g1 - (p - 1) * d, 2 * g2 - (2 * p + 1) * d)
        defect = block["columns"] - block["rank_over_q"]
        if defect < 0:
            raise ValueError("block rank exceeds its column count")
        weights[weight] = weights.get(weight, 0) + defect

    if not weights:
        return None

    parity_1 = next(iter(weights))[0] % 2
    parity_2 = next(iter(weights))[1] % 2
    if any(w1 % 2 != parity_1 or w2 % 2 != parity_2 for w1, w2 in weights):
        raise ValueError("inconsistent weight parity")
    for (w1, w2), dimension in weights.items():
        if (
            weights.get((-w1, w2), 0) != dimension
            or weights.get((w1, -w2), 0) != dimension
        ):
            raise ValueError("weight table is not symmetric under the Weyl group")

    max_1 = max(abs(w1) for w1, _ in weights)
    max_2 = max(abs(w2) for _, w2 in weights)

    def multiplicity(w1, w2):
        return weights.get((w1, w2), 0)

    # Each difference removes the weights contributed by higher SL2 types.
    irreducibles = []
    for highest_1 in range(max_1, -1, -2):
        if highest_1 % 2 != parity_1:
            continue
        for highest_2 in range(max_2, -1, -2):
            if highest_2 % 2 != parity_2:
                continue
            copies = (
                multiplicity(highest_1, highest_2)
                - multiplicity(highest_1 + 2, highest_2)
                - multiplicity(highest_1, highest_2 + 2)
                + multiplicity(highest_1 + 2, highest_2 + 2)
            )
            if copies < 0:
                raise ValueError("weight table is not an SL2 x SL2 character")
            if copies:
                irreducibles.append({
                    "highest_weight": [highest_1, highest_2],
                    "multiplicity": copies,
                    "dimension": copies * (highest_1 + 1) * (highest_2 + 1),
                })

    kernel_dimension = sum(weights.values())
    decomposed_dimension = sum(item["dimension"] for item in irreducibles)
    if decomposed_dimension != kernel_dimension:
        raise ValueError("irreducible dimensions do not recover the kernel")

    return {
        "a": a,
        "p": p,
        "kernel_dimension": kernel_dimension,
        "weight_multiplicities": [
            {"weight": list(weight), "dimension": dimension}
            for weight, dimension in sorted(weights.items())
            if dimension
        ],
        "irreducibles": irreducibles,
    }


def report(paths):
    records = []
    for path in paths:
        source = json.loads(path.read_text())
        for record in source["records"]:
            decomposition = decompose_record(record)
            if decomposition is not None:
                decomposition["rank_report"] = path.name
                records.append(decomposition)
    return {
        "group": "SL2 x SL2 over Q",
        "method": "finite differences of exact torus weight multiplicities",
        "records": sorted(records, key=lambda item: (item["a"], item["p"])),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = report(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(args.output),
        "records": [
            {"a": item["a"], "p": item["p"],
             "kernel_dimension": item["kernel_dimension"],
             "irreducible_types": len(item["irreducibles"])}
            for item in result["records"]
        ],
    }, sort_keys=True))
