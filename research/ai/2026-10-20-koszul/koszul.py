"""Closed Koszul ranks for convolutions; exact necessary degeneration tests.

The formulas are proved in research_note.md. Passing these tests does not
construct a degeneration. No floating point arithmetic is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARCHIVED_SEARCH = ROOT / "results/session2-2026-10-20/dimension_search.json.gz"


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def intrinsic_rank(h: int, y: int, z: int, p: int) -> int:
    """Rank of Y* tensor wedge^p X -> Z tensor wedge^(p+1) X.

    (h,y,z) are the dimensions of a convolution in the specified orientation.
    Exterior degrees outside [0,h-1] contribute zero to padding formulas.
    """
    if min(h, y, z) < 1:
        raise ValueError("convolution dimensions must be positive")
    if max(h, y, z) * 2 != h + y + z - 1:
        raise ValueError("dimensions do not describe a convolution")
    if not 0 <= p < h:
        return 0
    if h == y + z - 1:
        return min(y * choose(h, p), z * choose(h, p + 1))
    if z == h + y - 1:
        return y * choose(h, p) - max(y - h + p, 0) * choose(h - 1, p - 1)
    # Swap the nonshared legs and dualize the exterior powers.
    return intrinsic_rank(h, z, y, h - 1 - p)


def padded_rank(h: int, y: int, z: int, ambient: int, p: int) -> int:
    if ambient < h:
        raise ValueError("ambient shared dimension is too small")
    return sum(choose(ambient - h, q) * intrinsic_rank(h, y, z, p - q)
               for q in range(ambient - h + 1))


def profile(a: int, b: int) -> Fraction:
    a, b = sorted((a, b))
    if a < 1:
        raise ValueError("profile lengths must be positive")
    value = Fraction(2 * b + a - 1, 2)
    for j in range(1, a):
        value *= Fraction(3 * j + 1, 3 * j)
    return value


def audit_case(case: dict) -> dict:
    dims = case["source_dimensions"]
    h = dims[case["shared"]]
    y, z = [d for i, d in enumerate(dims) if i != case["shared"]]
    source = [intrinsic_rank(h, y, z, p) for p in range(h)]
    blocks = [[padded_rank(s["shared_dimension"], *s["nonshared"], h, p)
               for p in range(h)] for s in case["sectors"]]
    target = [sum(block[p] for block in blocks) for p in range(h)]
    witnesses = [p for p in range(h) if target[p] > source[p]]
    return {"source": [case["a"], case["b"]], "shared_axis": case["shared"],
            "shared_dimension": h, "profile_ratio": case["ratio"],
            "sectors": case["sectors"], "source_ranks": source,
            "sector_ranks": blocks, "target_ranks": target,
            "obstructing_degrees": witnesses, "excluded": bool(witnesses)}


def audit_archive() -> dict:
    raw = ARCHIVED_SEARCH.read_bytes()
    archive = json.loads(gzip.decompress(raw))
    cases = [audit_case(c) for c in archive["candidates"]]
    return {"status": "exact necessary tests; general formulas have an unreviewed written proof",
            "new_exponent_established": False,
            "archive_path": str(ARCHIVED_SEARCH.relative_to(ROOT)),
            "archive_sha256": hashlib.sha256(raw).hexdigest(),
            "coverage": archive["coverage"], "candidate_cases": len(cases),
            "excluded_cases": sum(c["excluded"] for c in cases),
            "surviving_cases": sum(not c["excluded"] for c in cases),
            "cases": cases}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = audit_archive()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "cases"}, indent=2))


if __name__ == "__main__":
    main()
