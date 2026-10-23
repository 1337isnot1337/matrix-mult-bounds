#!/usr/bin/env python3
"""Exact finite-field evaluation of the explicit rank-one aggregate formula.

This is a control of the tensor realization, separate from the all-triples
combinatorial certificate and the uniform proof. It enumerates every
rank-one contribution for one full random assignment of matrix entries.
No sampled evaluation is represented as a proof of a tensor identity.
"""
from __future__ import annotations
import argparse
from itertools import product
import json
from math import prod
from pathlib import Path
import random

HERE = Path(__file__).resolve().parent


def transform(array: list[int], maps: list[list[list[int]]], n: int, modulus: int) -> list[int]:
    dims = [n] * len(maps)
    for axis, matrix in enumerate(maps):
        stride = prod(dims[axis + 1:])
        old = dims[axis]
        size = len(matrix)
        block = old * stride
        result = [0] * (len(array) // old * size)
        for start in range(0, len(array), block):
            output_start = start // old * size
            for new_coordinate in range(size):
                for tail in range(stride):
                    result[output_start + new_coordinate * stride + tail] = sum(
                        matrix[new_coordinate][j] * array[start + j * stride + tail]
                        for j in range(old)) % modulus
        array = result
        dims[axis] = size
    return array


def index_at(assignment: tuple[int, ...], positions: tuple[int, ...], base: int) -> int:
    index = 0
    for position in positions:
        index = base * index + assignment[position]
    return index


def evaluate(data: dict, n: int = 2, modulus: int = 101, seed: int = 20261023) -> dict:
    x = n + 1
    if n < 1 or x % modulus == 0:
        raise ValueError("The centered dual embedding needs n+1 nonzero in the field")
    d = data["coordinate_count"]
    universe = tuple(range(d))
    rows = [tuple(frozenset(row[key]) for key in ("U", "V", "W")) for row in data["products"]]
    correction_subsets = [frozenset(), *(frozenset(p) for p in data["correction_subsets"])]
    rng = random.Random(seed)
    e = [[int(i == j) for j in range(n)] for i in range(n)] + [[-1] * n]
    inv_x = pow(x, -1, modulus)
    g_inverse = [[(int(i == j) - inv_x) % modulus for j in range(n)] for i in range(n)]
    dual = [[sum(e[i][k] * g_inverse[k][j] for k in range(n)) % modulus for j in range(n)] for i in range(x)]
    original, embedded, active = [], [], []
    for row in rows:
        originals, embeddings, coordinates = [], [], []
        for leg, omitted in enumerate(row):
            kept = tuple(r for r in universe if r not in omitted)
            values = [rng.randrange(modulus) for _ in range(n ** len(kept))]
            maps = []
            for r in kept:
                partners = [other for other in range(3) if r not in row[other]]
                maps.append(e if leg == min(partners) else dual)
            originals.append(values)
            embeddings.append(transform(values, maps, n, modulus))
            coordinates.append(kept)
        original.append(originals)
        embedded.append(embeddings)
        active.append(coordinates)

    target = 0
    for t in range(len(rows)):
        for assignment in product(range(n), repeat=d):
            value = 1
            for leg in range(3):
                value *= original[t][leg][index_at(assignment, active[t][leg], n)]
            target = (target + value) % modulus

    actual = 0
    rank_one_terms = 0
    nonzero_aggregate_values = 0
    for subset in correction_subsets:
        remaining = tuple(r for r in universe if r not in subset)
        position = {r: j for j, r in enumerate(remaining)}
        eligible = [[(embedded[t][leg], tuple(position[r] for r in active[t][leg]))
                     for t, row in enumerate(rows) if subset <= row[leg]] for leg in range(3)]
        aggregate = 0
        for assignment in product(range(x), repeat=len(remaining)):
            factors = [sum(array[index_at(assignment, positions, x)] for array, positions in entries) % modulus
                       for entries in eligible]
            aggregate = (aggregate + prod(factors)) % modulus
            rank_one_terms += 1
        nonzero_aggregate_values += aggregate != 0
        actual = (actual + pow(-x, len(subset), modulus) * aggregate) % modulus
    advertised_terms = sum(coefficient * x ** int(power)
                           for power, coefficient in data["rank_polynomial_coefficients"].items())
    if rank_one_terms != advertised_terms:
        raise ValueError("Realized rank-one term count differs from the advertised bound")
    if actual != target:
        raise ValueError(f"Aggregate evaluation {actual} differs from target {target}")
    return {"accepted": True, "local_dimension": n, "field_modulus": modulus,
            "random_seed": seed, "products": len(rows), "target_value": target,
            "aggregate_value": actual, "rank_one_contributions_enumerated": rank_one_terms,
            "correction_aggregates_including_main": len(correction_subsets),
            "nonzero_aggregate_values": nonzero_aggregate_values,
            "scope": "One exact finite-field evaluation of all rank-one contributions; a control, not the uniform proof"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--witness", type=Path, default=HERE / "witness_29.json")
    parser.add_argument("--n", type=int, default=2)
    parser.add_argument("--modulus", type=int, default=101)
    parser.add_argument("--seed", type=int, default=20261023)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = evaluate(json.loads(args.witness.read_text()), args.n, args.modulus, args.seed)
    rendered = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
