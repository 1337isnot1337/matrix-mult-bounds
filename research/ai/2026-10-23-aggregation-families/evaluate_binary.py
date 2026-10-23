#!/usr/bin/env python3
"""Exact bit-packed evaluation of every rank-one position over F2 at n=2.

Bytes are 0/1 field elements. XOR adds vectors, AND multiplies them
coordinatewise, and bit_count parity sums every coordinate. This evaluates
one complete seeded input assignment; it is not a coefficientwise proof.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("aggregation_reference_evaluate", HERE / "evaluate.py")
reference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reference)


def lift(values: list[int], kept: tuple[int, ...], remaining: tuple[int, ...], base: int) -> int:
    """Replicate bytes along omitted axes, then pack the complete vector exactly."""
    if not set(kept) <= set(remaining):
        raise ValueError("Cannot lift an active coordinate that was deleted")
    packed = bytes(values)
    axes = list(kept)
    for position, coordinate in enumerate(remaining):
        if position < len(axes) and axes[position] == coordinate:
            continue
        stride = base ** (len(axes) - position)
        packed = b"".join(packed[start:start + stride] * base for start in range(0, len(packed), stride))
        axes.insert(position, coordinate)
    if len(packed) != base ** len(remaining):
        raise ValueError("Lift has the wrong number of coordinate positions")
    return int.from_bytes(packed, "little")


def evaluate(data: dict, seed: int = 20261023) -> dict:
    d = data["coordinate_count"]
    universe = tuple(range(d))
    rows = [tuple(frozenset(row[key]) for key in ("U", "V", "W")) for row in data["products"]]
    e = [[1, 0], [0, 1], [1, 1]]
    dual = [[0, 1], [1, 0], [1, 1]]
    rng = random.Random(seed)
    originals, embeddings, active = [], [], []
    for row in rows:
        original_row, embedded_row, active_row = [], [], []
        for leg, omitted in enumerate(row):
            kept = tuple(r for r in universe if r not in omitted)
            values = [rng.randrange(2) for _ in range(2 ** len(kept))]
            maps = []
            for r in kept:
                partners = [other for other in range(3) if r not in row[other]]
                maps.append(e if leg == min(partners) else dual)
            original_row.append(values)
            embedded_row.append(reference.transform(values, maps, 2, 2))
            active_row.append(kept)
        originals.append(original_row)
        embeddings.append(embedded_row)
        active.append(active_row)

    target = 0
    for t in range(len(rows)):
        vectors = [lift(originals[t][leg], active[t][leg], universe, 2) for leg in range(3)]
        target ^= (vectors[0] & vectors[1] & vectors[2]).bit_count() & 1

    aggregate = 0
    rank_one_positions = 0
    nonzero_corrections = 0
    subsets = [frozenset(), *(frozenset(p) for p in data["correction_subsets"])]
    for subset in subsets:
        remaining = tuple(r for r in universe if r not in subset)
        vectors = [0, 0, 0]
        for leg in range(3):
            for t, row in enumerate(rows):
                if subset <= row[leg]:
                    vectors[leg] ^= lift(embeddings[t][leg], active[t][leg], remaining, 3)
        value = (vectors[0] & vectors[1] & vectors[2]).bit_count() & 1
        # (-3)^|P| is one in F2; all positions still contribute to the exact cost.
        aggregate ^= value
        rank_one_positions += 3 ** len(remaining)
        nonzero_corrections += bool(subset) and bool(value)
    expected = sum(value * 3 ** int(power) for power, value in data["rank_polynomial_coefficients"].items())
    if rank_one_positions != expected:
        raise ValueError("Packed evaluator has the wrong multiplication budget")
    if target != aggregate:
        raise ValueError("Packed aggregate differs from the independent matrix target")
    return {"accepted": True, "products": len(rows), "local_dimension": 2,
            "matrix_dimension": 2 ** data["part_size"], "field_modulus": 2,
            "random_seed": seed, "target_value": target, "aggregate_value": aggregate,
            "rank_one_positions_evaluated": rank_one_positions,
            "nonzero_correction_aggregate_values": nonzero_corrections,
            "scope": "One exact seeded assignment, all rank-one positions evaluated by byte-packed F2 arithmetic; an implementation control, not the uniform proof"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", type=Path, default=HERE / "witness_106.json")
    parser.add_argument("--seed", type=int, default=20261023)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate(json.loads(args.witness.read_text()), args.seed)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
