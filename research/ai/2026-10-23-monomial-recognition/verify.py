"""Recognize additive convolution supports and audit both input orientations."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PINS = json.loads(Path(__file__).with_name("sources.json").read_text())
SOURCE = ROOT / PINS["archive"]["path"]
if hashlib.sha256(SOURCE.read_bytes()).hexdigest() != PINS["archive"]["sha256"]:
    raise ValueError("archived search source does not match its pin")
SPEC = importlib.util.spec_from_file_location("archived_monomial_source", SOURCE)
ARCHIVE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ARCHIVE)


def recognize(terms):
    """Return explicit ordered coordinate maps, or None; see proof.md."""
    terms = tuple(terms)
    if not terms or len(set(terms)) != len(terms):
        raise ValueError("expected a nonempty set of distinct triples")
    if any(x + y != z for x, y, z in terms):
        raise ValueError("support must satisfy x+y=z")
    axes = [sorted({term[k] for term in terms}) for k in range(3)]
    dimensions = list(map(len, axes))
    for output in range(3):
        inputs = [k for k in range(3) if k != output]
        r, s = (dimensions[k] for k in inputs)
        if dimensions[output] != r + s - 1 or len(terms) != r * s:
            continue
        maps = [list(axis) for axis in axes]
        if output != 2:
            maps[1 - output].reverse()
        indexes = [{value: i for i, value in enumerate(axis)} for axis in maps]
        if any(indexes[output][t[output]] != sum(indexes[k][t[k]] for k in inputs)
               for t in terms):
            raise AssertionError("additive recognition theorem failed")
        return {"a": r, "b": s, "output_axis": output,
                "coordinate_orders": maps}
    return None


def score(wx, wy, h):
    sectors, _ = ARCHIVE.components(wx, wy)
    blocks = []
    for sector in sectors:
        block = recognize(sector)
        if block is None:
            # Each fixed-coordinate slice is a matching in x+y=z.
            d = max(sum(t[k] == value for t in sector)
                    for k in range(3) for value in {t[k] for t in sector})
            block = {"a": 1, "b": d, "kind": "slice_lower_bound"}
        else:
            block["kind"] = "convolution"
        blocks.append(block)
    target = sum((ARCHIVE.profile(b["a"], b["b"], h) for b in blocks), Fraction())
    source = ARCHIVE.profile(len(wx), len(wy), h)
    return {"weights": [list(wx), list(wy)], "blocks": blocks,
            "source_exact": str(source), "target_exact": str(target),
            "ratio_exact": str(target / source)}


def expected_count(q, max_sum):
    return sum((q**a - (q-1)**a) * (q**b - (q-1)**b)
               for a in range(2, max_sum-1) for b in range(2, max_sum-a+1))


def run(q, max_sum):
    h = ARCHIVE.slopes(max_sum)
    counts = {"a<b": 0, "a=b": 0, "a>b": 0}
    best = None
    nontrivial = None
    first_asymmetry = None
    unequal_pairs = 0
    violations = 0
    for a in range(2, max_sum-1):
        for b in range(a, max_sum-a+1):
            for wx in product(range(q), repeat=a):
                if min(wx) != 0:
                    continue
                for wy in product(range(q), repeat=b):
                    if min(wy) != 0:
                        continue
                    records = [score(wx, wy, h)]
                    counts["a=b" if a == b else "a<b"] += 1
                    if a < b:
                        records.append(score(wy, wx, h))
                        counts["a>b"] += 1
                        if records[0]["ratio_exact"] != records[1]["ratio_exact"]:
                            unequal_pairs += 1
                            if first_asymmetry is None:
                                first_asymmetry = records
                    for record in records:
                        ratio = Fraction(record["ratio_exact"])
                        violations += ratio > 1
                        if best is None or ratio > Fraction(best["ratio_exact"]):
                            best = record
                        if len(record["blocks"]) > 1 and (
                            nontrivial is None or ratio > Fraction(nontrivial["ratio_exact"])
                        ):
                            nontrivial = record
    count = sum(counts.values())
    if count != expected_count(q, max_sum):
        raise AssertionError("ordered candidate coverage does not match the count formula")
    return {"schema_version": 1, "archive": PINS["archive"],
            "parameters": {"alphabet_size": q, "max_sum": max_sum},
            "cases_tested": count, "orientation_counts": counts,
            "unequal_dimension_pairs_with_different_scores": unequal_pairs,
            "exact_violation_count": violations, "best": best,
            "best_nontrivial": nontrivial, "first_asymmetric_pair": first_asymmetry,
            "scope": "All ordered a,b>=2 with a+b<=max_sum; independent minimum-zero "
                     "normalization; exact whole-convolution or slice-fallback scores. "
                     "No general-basis, all-weight, or exponent conclusion."}


def replay_record(record):
    wx, wy = map(tuple, record["weights"])
    if record != score(wx, wy, ARCHIVE.slopes(len(wx) + len(wy))):
        raise ValueError("record does not replay")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alphabet-size", type=int, choices=(2, 3), required=True)
    parser.add_argument("--max-sum", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.max_sum < 4:
        parser.error("max-sum must be at least four")
    report = run(args.alphabet_size, args.max_sum)
    for record in [report["best"], report["best_nontrivial"]] + (
        report["first_asymmetric_pair"] or []
    ):
        if record is not None:
            replay_record(record)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: report[k] for k in ("cases_tested", "orientation_counts",
                     "unequal_dimension_pairs_with_different_scores", "exact_violation_count")}))


if __name__ == "__main__":
    main()
