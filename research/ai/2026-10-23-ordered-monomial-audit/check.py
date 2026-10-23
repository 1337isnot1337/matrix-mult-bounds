"""Independent exact replay and complete ordered monomial-weight census."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


@lru_cache(maxsize=None)
def profile(a, b):
    m, n = sorted((a, b))
    value = Fraction(2 * n + m - 1, 2)
    for k in range(1, m):
        value *= Fraction(3 * k + 1, 3 * k)
    return value


def support(wx, wy):
    if not wx or not wy or any(type(w) is not int for w in (*wx, *wy)):
        raise ValueError("nonempty integer weight arrays required")
    diagonals = [[] for _ in range(len(wx) + len(wy) - 1)]
    for i, u in enumerate(wx):
        for j, v in enumerate(wy):
            diagonals[i + j].append((u + v, (i, j, i + j)))
    minima = [min(weight for weight, _ in diagonal) for diagonal in diagonals]
    terms = {term for diagonal, low in zip(diagonals, minima)
             for weight, term in diagonal if weight == low}
    # Flood-fill term adjacency, independently of the reviewed union-find code.
    neighbors = {}
    for term in terms:
        for axis in (1, 2):
            neighbors.setdefault((axis, term[axis]), set()).add(term)
    remaining = set(terms)
    sectors = []
    while remaining:
        pending = [min(remaining)]
        component = set()
        while pending:
            term = pending.pop()
            if term in component:
                continue
            component.add(term)
            for axis in (1, 2):
                pending.extend(neighbors[axis, term[axis]] - component)
        remaining -= component
        sectors.append(sorted(component))
    return minima, sorted(terms), sorted(sectors)


def block(terms):
    axes = [sorted({t[k] for t in terms}) for k in range(3)]
    dims = list(map(len, axes))
    for out in range(3):
        inputs = [k for k in range(3) if k != out]
        a, b = (dims[k] for k in inputs)
        if dims[out] != a + b - 1 or len(terms) != a * b:
            continue
        expected = set()
        for i, j in product(range(a), range(b)):
            t = [0, 0, 0]
            t[inputs[0]], t[inputs[1]], t[out] = i, j, i + j
            expected.add(tuple(t))
        for reversals in product((False, True), repeat=3):
            orders = [axis[::-1] if reverse else axis
                      for axis, reverse in zip(axes, reversals)]
            actual = {tuple(orders[k].index(t[k]) for k in range(3)) for t in terms}
            if actual == expected:
                return {"kind": "convolution", "a": a, "b": b,
                        "output_axis": out, "reversals": list(reversals),
                        "dimensions": dims}
    size = max(max(Counter(t[k] for t in terms).values()) for k in range(3))
    return {"kind": "slice_lower_bound", "a": 1, "b": size, "dimensions": dims}


def inspect(wx, wy):
    minima, terms, sectors = support(wx, wy)
    blocks = [block(sector) for sector in sectors]
    target = sum((profile(q["a"], q["b"]) for q in blocks), Fraction(0))
    source = profile(len(wx), len(wy))
    return {"weights": {"x": list(wx), "y": list(wy)},
            "blocks": blocks, "source_exact": str(source),
            "target_exact": str(target), "ratio_exact": str(target / source),
            "minimum_sums": minima, "zero_terms": [list(t) for t in terms],
            "sectors": [[list(t) for t in sector] for sector in sectors]}


def expected_record(wx, wy):
    """Reconstruct a PR118 schema-v1 record without importing its producer."""
    actual = inspect(wx, wy)
    if min(wx) != 0 or min(wy) != 0:
        raise ValueError("record weights are not normalized")
    weights = {"x": list(wx), "y": list(wy)}
    dims = [len(wx), len(wy), len(wx) + len(wy) - 1]
    certificate = {"version": 1, "dimensions": dims,
                   "weights": {**weights, "z": [-v for v in actual["minimum_sums"]]},
                   **{key: actual[key] for key in ("minimum_sums", "zero_terms", "sectors")}}
    score = {key: actual[key] for key in ("source_exact", "target_exact", "ratio_exact")}
    score["violation_exact"] = Fraction(actual["ratio_exact"]) > 1
    return {"dimensions": dims, "weights": weights, "blocks": actual["blocks"],
            "score": score, "support_certificate": certificate}


def verify_record(record):
    """Reject a support, recognition or score certificate that does not replay."""
    expected = expected_record(record["weights"]["x"], record["weights"]["y"])
    if record != expected:
        raise ValueError("certificate, block recognition or score mismatch")


def census(alphabet_size, max_sum):
    summaries = []
    for a in range(2, max_sum - 1):
        for b in range(2, max_sum - a + 1):
            count = violations = 0
            best = nontrivial = None
            for wx in product(range(alphabet_size), repeat=a):
                if min(wx):
                    continue
                for wy in product(range(alphabet_size), repeat=b):
                    if min(wy):
                        continue
                    record = inspect(wx, wy)
                    ratio = Fraction(record["ratio_exact"])
                    count += 1
                    violations += ratio > 1
                    if best is None or ratio > Fraction(best["ratio_exact"]):
                        best = record
                    if len(record["blocks"]) > 1 and (nontrivial is None or
                            ratio > Fraction(nontrivial["ratio_exact"])):
                        nontrivial = record
            expected = (alphabet_size**a - (alphabet_size - 1)**a) * (
                alphabet_size**b - (alphabet_size - 1)**b)
            if count != expected:
                raise ValueError("ordered dimension coverage mismatch")
            summaries.append({"a": a, "b": b, "cases": count,
                              "violations": violations, "best": best,
                              "best_nontrivial": nontrivial})
    return {"alphabet_size": alphabet_size, "max_sum": max_sum,
            "scope": "All ordered a,b>=2 with a+b<=max_sum; minimum zero in each array.",
            "cases": sum(s["cases"] for s in summaries),
            "historical_a_le_b_cases": sum(s["cases"] for s in summaries if s["a"] <= s["b"]),
            "additional_a_gt_b_cases": sum(s["cases"] for s in summaries if s["a"] > s["b"]),
            "violations": sum(s["violations"] for s in summaries),
            "dimensions": summaries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--alphabet-size", type=int, choices=(2, 3))
    parser.add_argument("--max-sum", type=int, default=11)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.report:
        report = json.loads(args.report.read_text())
        records = report["leaderboard"] + report["nontrivial_leaderboard"]
        if report["first_exact_violation"] is not None:
            records.append(report["first_exact_violation"])
        for record in records:
            verify_record(record)
        print(f"independently verified {len(records)} retained records")
    else:
        if args.alphabet_size is None or args.output is None or args.max_sum < 4:
            parser.error("census requires --alphabet-size, --max-sum >= 4 and --output")
        report = census(args.alphabet_size, args.max_sum)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(f"{report['cases']} ordered cases; {report['violations']} violations")


if __name__ == "__main__":
    main()
