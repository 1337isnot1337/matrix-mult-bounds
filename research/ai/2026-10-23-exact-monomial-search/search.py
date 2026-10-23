"""Exact, replayable search for monomial convolution support degenerations."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import random


def slopes(n: int) -> list[Fraction]:
    if n < 1:
        raise ValueError("n must be positive")
    values = [Fraction(0), Fraction(1)]
    for k in range(1, n):
        values.append(values[-1] * Fraction(3 * k + 1, 3 * k))
    return values


def profile(a: int, b: int, h: list[Fraction]) -> Fraction:
    if a < 1 or b < 1 or min(a, b) >= len(h):
        raise ValueError("profile dimensions are outside the slope table")
    a, b = sorted((a, b))
    return h[a] * Fraction(2 * b + a - 1, 2)


def normalize_weights(
    wx: tuple[int, ...], wy: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if not wx or not wy:
        raise ValueError("weight arrays must be nonempty")
    wx = tuple(value - min(wx) for value in wx)
    wy = tuple(value - min(wy) for value in wy)
    return wx, wy


def component_sectors(
    terms: tuple[tuple[int, int, int], ...], y_size: int, z_size: int
) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    parent = list(range(y_size + z_size))

    def root(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for _, j, k in terms:
        left, right = root(j), root(y_size + k)
        if left != right:
            parent[left] = right

    groups: dict[int, list[tuple[int, int, int]]] = {}
    for term in terms:
        groups.setdefault(root(term[1]), []).append(term)
    sectors = [tuple(sorted(group)) for group in groups.values()]
    return tuple(sorted(sectors))


def support_parts(wx: tuple[int, ...], wy: tuple[int, ...]) -> tuple:
    wx, wy = normalize_weights(wx, wy)
    z_size = len(wx) + len(wy) - 1
    minima = []
    for k in range(z_size):
        i_values = range(max(0, k - len(wy) + 1), min(len(wx) - 1, k) + 1)
        minima.append(min(wx[i] + wy[k - i] for i in i_values))
    terms = tuple(
        (i, j, i + j)
        for i in range(len(wx))
        for j in range(len(wy))
        if wx[i] + wy[j] == minima[i + j]
    )
    sectors = component_sectors(terms, len(wy), z_size)
    return wx, wy, z_size, minima, terms, sectors


def certificate_from_parts(
    wx: tuple[int, ...],
    wy: tuple[int, ...],
    z_size: int,
    minima: list[int],
    terms: tuple[tuple[int, int, int], ...],
    sectors: tuple[tuple[tuple[int, int, int], ...], ...],
) -> dict:
    return {
        "version": 1,
        "weights": {
            "x": list(wx),
            "y": list(wy),
            "z": [-value for value in minima],
        },
        "dimensions": [len(wx), len(wy), z_size],
        "minimum_sums": minima,
        "zero_terms": [list(term) for term in terms],
        "sectors": [
            [list(term) for term in sector]
            for sector in sectors
        ],
    }


def make_support_certificate(wx: tuple[int, ...], wy: tuple[int, ...]) -> dict:
    return certificate_from_parts(*support_parts(wx, wy))


def recognize(terms: tuple[tuple[int, int, int], ...]) -> dict:
    axes = [sorted({term[axis] for term in terms}) for axis in range(3)]
    dimensions = list(map(len, axes))
    indexes = [{value: index for index, value in enumerate(axis)} for axis in axes]
    for output in range(3):
        inputs = [axis for axis in range(3) if axis != output]
        r, s = dimensions[inputs[0]], dimensions[inputs[1]]
        if dimensions[output] != r + s - 1 or len(terms) != r * s:
            continue
        for flips in product((False, True), repeat=3):
            mapped = []
            for term in terms:
                ids = [indexes[axis][term[axis]] for axis in range(3)]
                mapped.append(tuple(
                    dimensions[axis] - 1 - value if flips[axis] else value
                    for axis, value in enumerate(ids)
                ))
            if all(term[output] == term[inputs[0]] + term[inputs[1]] for term in mapped):
                return {
                    "kind": "convolution",
                    "a": r,
                    "b": s,
                    "output_axis": output,
                    "reversals": list(flips),
                    "dimensions": dimensions,
                }
    max_slice = max(
        max(Counter(term[axis] for term in terms).values())
        for axis in range(3)
    )
    return {
        "kind": "slice_lower_bound",
        "a": 1,
        "b": max_slice,
        "dimensions": dimensions,
    }


def score_from_parts(wx: tuple[int, ...], wy: tuple[int, ...], z_size: int,
                     sectors: tuple[tuple[tuple[int, int, int], ...], ...],
                     h: list[Fraction]) -> dict:
    blocks = [recognize(sector) for sector in sectors]
    target = sum(
        (profile(block["a"], block["b"], h) for block in blocks),
        Fraction(0),
    )
    dimensions = [len(wx), len(wy), z_size]
    source = profile(*dimensions[:2], h)
    ratio = target / source
    return {
        "dimensions": dimensions,
        "weights": {"x": list(wx), "y": list(wy)},
        "blocks": blocks,
        "score": {
            "source_exact": str(source),
            "target_exact": str(target),
            "ratio_exact": str(ratio),
            "violation_exact": target > source,
        },
    }


def score_candidate(wx: tuple[int, ...], wy: tuple[int, ...],
                    h: list[Fraction]) -> dict:
    wx, wy, z_size, _, _, sectors = support_parts(wx, wy)
    return score_from_parts(wx, wy, z_size, sectors, h)


def make_record(wx: tuple[int, ...], wy: tuple[int, ...],
                h: list[Fraction] | None = None) -> dict:
    parts = support_parts(wx, wy)
    wx, wy, z_size, minima, terms, sectors = parts
    if h is None:
        h = slopes(max(len(wx) + len(wy) - 1, len(wx), len(wy)))
    record = score_from_parts(wx, wy, z_size, sectors, h)
    record["support_certificate"] = certificate_from_parts(*parts)
    return record


def replay_record(record: dict) -> None:
    certificate = record["support_certificate"]
    weights = record["weights"]
    expected = make_record(tuple(weights["x"]), tuple(weights["y"]))
    if record != expected:
        raise ValueError("candidate record does not replay from its support certificate")


def record_key(record: dict) -> tuple:
    return (
        -Fraction(record["score"]["ratio_exact"]),
        tuple(record["dimensions"]),
        tuple(record["weights"]["x"]),
        tuple(record["weights"]["y"]),
    )


def offer(top: list[dict], record: dict, limit: int) -> None:
    weights = record["weights"]
    identity = (
        tuple(record["dimensions"]),
        tuple(weights["x"]),
        tuple(weights["y"]),
    )
    if any(
        identity == (
            tuple(item["dimensions"]),
            tuple(item["weights"]["x"]),
            tuple(item["weights"]["y"]),
        )
        for item in top
    ):
        return
    top.append(record)
    top.sort(key=record_key)
    del top[limit:]


def candidates(mode: str, max_sum: int, samples: int, seed: int):
    if mode == "random":
        rng = random.Random(seed)
        for _ in range(samples):
            wx = tuple(rng.randint(-8, 8) for _ in range(rng.randint(2, 15)))
            wy = tuple(rng.randint(-8, 8) for _ in range(rng.randint(2, 15)))
            yield wx, wy
        return
    alphabet = range(2 if mode == "binary" else 3)
    for a in range(2, max_sum - 1):
        for b in range(a, max_sum - a + 1):
            for wx in product(alphabet, repeat=a):
                if min(wx) != 0:
                    continue
                for wy in product(alphabet, repeat=b):
                    if min(wy) == 0:
                        yield wx, wy


def run_search(
    mode: str, max_sum: int = 11, samples: int = 20000,
    seed: int = 20261020, top_k: int = 10,
) -> dict:
    if mode not in {"binary", "ternary", "random"}:
        raise ValueError("unknown search mode")
    if top_k < 1:
        raise ValueError("top_k must be positive")
    h = slopes(29 if mode == "random" else max(1, max_sum - 1))
    leaderboard_summaries: list[dict] = []
    nontrivial_summaries: list[dict] = []
    first_violation = None
    violation_count = 0
    count = 0
    for wx, wy in candidates(mode, max_sum, samples, seed):
        record = score_candidate(wx, wy, h)
        count += 1
        offer(leaderboard_summaries, record, top_k)
        if len(record["blocks"]) > 1:
            offer(nontrivial_summaries, record, top_k)
        if record["score"]["violation_exact"]:
            violation_count += 1
            if first_violation is None:
                first_violation = record

    leaderboard = [
        make_record(tuple(record["weights"]["x"]), tuple(record["weights"]["y"]), h)
        for record in leaderboard_summaries
    ]
    nontrivial = [
        make_record(tuple(record["weights"]["x"]), tuple(record["weights"]["y"]), h)
        for record in nontrivial_summaries
    ]
    if first_violation is not None:
        first_violation = make_record(
            tuple(first_violation["weights"]["x"]),
            tuple(first_violation["weights"]["y"]),
            h,
        )
    for record in leaderboard + nontrivial:
        replay_record(record)
    if first_violation is not None:
        replay_record(first_violation)
    return {
        "schema_version": 1,
        "mode": mode,
        "parameters": {
            "max_sum": max_sum if mode != "random" else None,
            "samples": samples if mode == "random" else None,
            "seed": seed if mode == "random" else None,
            "top_k": top_k,
        },
        "cases_tested": count,
        "exact_violation_count": violation_count,
        "first_exact_violation": first_violation,
        "leaderboard": leaderboard,
        "nontrivial_leaderboard": nontrivial,
        "scope": (
            "Exact rational scores for the specified finite integer-weight arrays. "
            "Each retained support certificate replays its zero-weight support, "
            "sector partition, block recognition, and score. No exponent follows "
            "from this relaxation alone."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("binary", "ternary", "random"), default="binary")
    parser.add_argument("--max-sum", type=int, default=11)
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=20261020)
    parser.add_argument("--top-k", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run_search(args.mode, args.max_sum, args.samples, args.seed, args.top_k)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"tested {report['cases_tested']} cases; exact violations: {report['exact_violation_count']}")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
