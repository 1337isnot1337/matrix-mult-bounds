"""Dimension-only relaxation. A feasible packing is NOT a tensor degeneration.

Reconstructed from the preceding session's recorded program. This version removes
unused SciPy imports, adds deterministic output, and verifies every packing.
"""
from __future__ import annotations
import argparse
import gzip
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
import json
from pathlib import Path


@lru_cache(None)
def h(n: int) -> Fraction:
    if n < 1:
        raise ValueError("n must be positive")
    return Fraction(1) if n == 1 else h(n - 1) * Fraction(3 * n - 2, 3 * n - 3)


def profile(a: int, b: int) -> Fraction:
    a, b = sorted((a, b))
    return h(a) * (b + Fraction(a - 1, 2))


def solve(a: int, b: int, shared: int) -> dict:
    if min(a, b) < 1 or shared not in (0, 1, 2):
        raise ValueError("positive lengths and a valid shared axis are required")
    dims = (a, b, a + b - 1)
    H = dims[shared]
    R, S = [dims[i] for i in range(3) if i != shared]
    items = []
    for u in range(1, max(dims) + 1):
        for v in range(u, max(dims) + 1):
            for hd, r, s in sorted(set(permutations((u, v, u + v - 1)))):
                if hd <= H and r <= R and s <= S:
                    items.append((r, s, profile(u, v), u, v, hd))
    dp = [[Fraction(0) for _ in range(S + 1)] for _ in range(R + 1)]
    predecessor = {}
    for r in range(1, R + 1):
        for s in range(1, S + 1):
            best, pred = dp[r - 1][s], (r - 1, s, None)
            if dp[r][s - 1] > best:
                best, pred = dp[r][s - 1], (r, s - 1, None)
            for k, (ri, si, val, *_rest) in enumerate(items):
                if ri <= r and si <= s and dp[r - ri][s - si] + val > best:
                    best = dp[r - ri][s - si] + val
                    pred = (r - ri, s - si, k)
            dp[r][s], predecessor[r, s] = best, pred
    r, s, chosen = R, S, []
    while r and s:
        r0, s0, k = predecessor[r, s]
        if k is not None:
            chosen.append(items[k])
        r, s = r0, s0
    if sum(x[0] for x in chosen) > R or sum(x[1] for x in chosen) > S:
        raise AssertionError("packing exceeds a nonshared dimension")
    if any(x[5] > H for x in chosen):
        raise AssertionError("packing exceeds the shared dimension")
    if sum((x[2] for x in chosen), Fraction(0)) != dp[R][S]:
        raise AssertionError("packing score does not reproduce the dynamic program")
    return {"a": a, "b": b, "shared": shared,
            "source_dimensions": list(dims), "source_score": str(profile(a, b)),
            "target_score": str(dp[R][S]), "ratio": str(dp[R][S] / profile(a, b)),
            "sectors": [{"nonshared": [x[0], x[1]], "score": str(x[2]),
                         "convolution": [x[3], x[4]], "shared_dimension": x[5]}
                        for x in chosen]}


def run() -> dict:
    records = [solve(a, b, shared) for a in range(2, 11)
               for b in range(a, 13) for shared in range(3)]
    candidates = [r for r in records if Fraction(r["ratio"]) > 1]
    return {"status": "dimension-only relaxation; not certified degenerations",
            "source_pairs": 63, "orientation_cases": len(records),
            "candidate_cases": len(candidates), "exact_arithmetic": True,
            "coverage": "2 <= a <= 10; a <= b <= 12; all three shared axes",
            "best": max(records, key=lambda r: Fraction(r["ratio"])),
            "candidates": candidates}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(report, separators=(",", ":")) + "\n").encode()
    args.output.write_bytes(gzip.compress(payload, mtime=0) if args.output.suffix == ".gz" else payload)
    print(json.dumps({k: v for k, v in report.items() if k != "candidates"}, indent=2))
