"""Discover rank84/88 integer minors; acceptance does not import this module."""
from __future__ import annotations

import argparse
from functools import lru_cache
import gzip
import importlib.util
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "results/rank84-88-source-caps-2026-10-23"
SPEC = importlib.util.spec_from_file_location(
    "prior_rank80_discovery", ROOT / "research/ai/2026-10-23-torus-rank80/discover.py")
old = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(old)
CASES = {84: 57, 88: 61}
MULTIPLICITIES = (1, 2, 3, 4, 3, 2, 1)


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            column = row.bit_length()-1
            if column in pivots:
                row ^= pivots[column]
            else:
                pivots[column] = row
                break
    return len(pivots)


def coherent_records(basis):
    records = []
    for index, shape in enumerate(old.SHAPES):
        allowed = [v for v in old.SHORT if v[1] < shape[v[0]]]
        generator = random.Random(20261023+index)
        best, coefficients = 0, []
        for attempt in range(32):
            chosen = [v for v in allowed if generator.randrange(2)]
            size = rank(old.matrix_sum(basis, chosen, 28))
            if size > best:
                best, coefficients = size, chosen
        minor = old.find_minor(old.matrix_sum(basis, coefficients, 28), best)
        if best == 0:
            minor = ([], [])
        record = old.minor_record(coefficients, old.SHORT, minor, shape)
        record["rank_lower"] = best
        records.append(record)
    return records


def source_ideals(threshold, coherent):
    shapes = old.SHAPES
    sizes = [sum(shape) for shape in shapes]
    lower = [record["rank_lower"] for record in coherent]
    children = [[j for j, y in enumerate(shapes)
                 if all(y[i] <= x[i] for i in range(4))] for x in shapes]
    full = shapes.index((4, 4, 4, 4))

    @lru_cache(None)
    def count(k, parent, remaining, rank1):
        if k == 7:
            return int(remaining == 0)
        if remaining < 0 or remaining > sizes[parent]*(7-k):
            return 0
        total = 0
        for j in children[parent]:
            size = sizes[j]
            if (size > remaining or size*(7-k) < remaining
                    or MULTIPLICITIES[k]*lower[j] >= threshold):
                continue
            if k == 5 and 2*rank1+2*lower[j] >= threshold:
                continue
            total += count(k+1, j, remaining-size, lower[j] if k == 1 else rank1)
        return total

    def visit(k, parent, remaining, rank1, chosen):
        if k == 7:
            if remaining == 0:
                yield tuple(chosen)
            return
        for j in children[parent]:
            size = sizes[j]
            if (size > remaining or size*(7-k) < remaining
                    or MULTIPLICITIES[k]*lower[j] >= threshold):
                continue
            if k == 5 and 2*rank1+2*lower[j] >= threshold:
                continue
            next_rank1 = lower[j] if k == 1 else rank1
            if count(k+1, j, remaining-size, next_rank1):
                yield from visit(k+1, j, remaining-size, next_rank1, chosen+[shapes[j]])

    return sorted(visit(0, full, CASES[threshold], 0, []))


def discover(threshold):
    coherent, source = old.matrices()
    controls = coherent_records(coherent)
    records = []
    for shape in source_ideals(threshold, controls):
        allowed = [v for v in old.SOURCE if v[2] < shape[v[1]][v[0]]]
        witness = None
        for attempt in range(32):
            generator = random.Random(attempt)
            coefficients = [v for v in allowed if generator.randrange(2)]
            minor = old.find_minor(old.matrix_sum(source, coefficients, 112), threshold)
            if minor is not None:
                witness = old.minor_record(coefficients, old.SOURCE, minor, shape)
                break
        if witness is None:
            raise ArithmeticError("Unresolved source ideal: " + str(shape))
        records.append(witness)
    return {"schema": "rank84-88-source-caps-v1", "field_of_geometric_reduction": "C",
            "threshold": threshold, "dimension": CASES[threshold],
            "coefficient_domain": "integers zero and one", "verification_modulus": 2,
            "coherent_minors": controls, "source_minors": records}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rank", type=int, choices=sorted(CASES), required=True)
    args = parser.parse_args()
    document = discover(args.rank)
    RESULT.mkdir(parents=True, exist_ok=True)
    path = RESULT / f"rank{args.rank}-minors.json.gz"
    path.write_bytes(gzip.compress(json.dumps(document, separators=(",", ":")).encode(), mtime=0))
    print(json.dumps({"threshold": args.rank, "coherent_shapes": len(document["coherent_minors"]),
                      "source_ideals": len(document["source_minors"]),
                      "compressed_bytes": path.stat().st_size}))
