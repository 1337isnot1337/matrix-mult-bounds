"""Sample coupled-coordinate weights on low-border-rank algebra sources."""
from __future__ import annotations

import argparse
from itertools import product
import json
from math import prod
import os
from pathlib import Path
import random

from truncated_search import search_size


def product_support(sizes):
    terms = [(0, 0, 0)]
    for size in sizes:
        factor = [(i, j, size - 1 - i - j) for i in range(size) for j in range(size - i)]
        terms = [tuple(a * size + b for a, b in zip(left, right))
                 for left, right in product(terms, factor)]
    return terms


def cw_support(q):
    return ([(0, i, i) for i in range(1, q + 1)]
            + [(i, 0, i) for i in range(1, q + 1)]
            + [(i, i, 0) for i in range(1, q + 1)]
            + [(0, 0, q + 1), (0, q + 1, 0), (q + 1, 0, 0)])


def weights(r, count, seed, max_weight=3):
    rng = random.Random(seed)
    for _ in range(count):
        pair = []
        for leg in range(2):
            values = [rng.randrange(max_weight + 1) for _ in range(r)]
            minimum = min(values)
            pair.append(tuple(value - minimum for value in values))
        yield tuple(pair)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=("product", "cw"), default="product")
    parser.add_argument("--sizes", default="2,2;2,3;2,2,2;3,3")
    parser.add_argument("--q", default="2,3,4,5,6")
    parser.add_argument("--samples", type=int, default=2000)
    parser.add_argument("--max-weight", type=int, default=3)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--delete-outputs", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seed = args.seed if args.seed is not None else int.from_bytes(os.urandom(16), "big")
    print("seed", seed, flush=True)
    sources = []
    if args.kind == "product":
        for item in args.sizes.split(";"):
            sizes = tuple(map(int, item.split(",")))
            sources.append((prod(sizes), product_support(sizes), {"factor_sizes": sizes}, "product-truncated-polynomial"))
    else:
        for q in map(int, args.q.split(",")):
            sources.append((q + 2, cw_support(q), {"q": q}, "coppersmith-winograd"))
    reports = []
    for rank, terms, metadata, name in sources:
        report = search_size(rank, terms=terms, source_name=name,
                             weight_pairs=weights(rank, args.samples, seed, args.max_weight),
                             delete_outputs=args.delete_outputs)
        report.update(metadata)
        reports.append(report)
        data = {"seed": seed, "seed_origin": "provided" if args.seed is not None else "os.urandom(16)",
                "samples_per_source": args.samples, "max_input_weight": args.max_weight,
                "sources": reports,
                "scope": "Finite seeded weight samples; arbitrary supplied source-rank bounds need separate certificates."}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2) + "\n")
        print({key: value for key, value in report.items() if key != "best"}, flush=True)
