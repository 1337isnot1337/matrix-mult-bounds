"""Independent exact acceptance for ordered monomial support certificates."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from math import factorial, prod
from pathlib import Path
import argparse


def profile(a, b):
    a, b = sorted((a, b))
    h = Fraction(prod(3 * k + 1 for k in range(1, a)),
                 3 ** (a - 1) * factorial(a - 1))
    return h * Fraction(2 * b + a - 1, 2)


def normalized_arrays(q, n):
    return q ** n - (q - 1) ** n


def coverage(q, max_sum):
    counts = {"historical": 0, "omitted": 0}
    for a in range(2, max_sum - 1):
        for b in range(2, max_sum - a + 1):
            kind = "historical" if a <= b else "omitted"
            counts[kind] += normalized_arrays(q, a) * normalized_arrays(q, b)
    return {**counts, "ordered": sum(counts.values())}


def check_record(record):
    """Reconstruct support by diagonals and sectors by graph traversal.

    This imports neither the discovery code nor the archived implementation.
    Convolution recognition compares whole Cartesian supports, not termwise
    tests of the discovery program's proposed output equation.
    """
    x, y = record["weights"]
    if not x or not y or any(type(w) is not int for w in x + y):
        raise ValueError("weights must be nonempty integer arrays")
    if min(x) != 0 or min(y) != 0:
        raise ValueError("weights must be normalized")
    dims = [len(x), len(y), len(x) + len(y) - 1]
    diagonal = [[] for _ in range(dims[2])]
    for i, u in enumerate(x):
        for j, v in enumerate(y):
            diagonal[i + j].append((u + v, (i, j, i + j)))
    minima = [min(weight for weight, _ in entries) for entries in diagonal]
    support = {term for k, entries in enumerate(diagonal)
               for weight, term in entries if weight == minima[k]}
    adjacency = {}
    for _, j, k in support:
        left, right = (1, j), (2, k)
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)
    unseen = set(adjacency)
    sectors = []
    while unseen:
        reached, stack = set(), [min(unseen)]
        while stack:
            vertex = stack.pop()
            if vertex not in reached:
                reached.add(vertex)
                stack.extend(adjacency[vertex] - reached)
        unseen -= reached
        sectors.append(sorted(term for term in support if (1, term[1]) in reached))
    sectors.sort()
    expected_support = {
        "dimensions": dims,
        "output_weights": [-v for v in minima],
        "terms": [list(term) for term in sorted(support)],
        "sectors": [[list(term) for term in sector] for sector in sectors],
    }
    if record["support"] != expected_support:
        raise ValueError("support or shared-first-leg partition mismatch")
    if len(record["blocks"]) != len(sectors):
        raise ValueError("block count mismatch")
    scores = []
    for sector, block in zip(sectors, record["blocks"]):
        axes = [sorted({term[k] for term in sector}) for k in range(3)]
        dimensions = list(map(len, axes))
        recognized = []
        for out in range(3):
            ins = [k for k in range(3) if k != out]
            a, b = (dimensions[k] for k in ins)
            if dimensions[out] != a + b - 1:
                continue
            for flips in product((False, True), repeat=3):
                ordered = [axis[::-1] if flip else axis
                           for axis, flip in zip(axes, flips)]
                model = set()
                for i in range(a):
                    for j in range(b):
                        triple = [None] * 3
                        triple[ins[0]], triple[ins[1]], triple[out] = (
                            ordered[ins[0]][i], ordered[ins[1]][j], ordered[out][i + j])
                        model.add(tuple(triple))
                if model == set(sector):
                    recognized.append({"kind": "convolution", "a": a, "b": b,
                                       "output_axis": out, "reversals": list(flips),
                                       "dimensions": dimensions})
        if recognized:
            if block != recognized[0]:
                raise ValueError("convolution certificate mismatch")
            score = profile(block["a"], block["b"])
        else:
            width = max(max(Counter(term[k] for term in sector).values()) for k in range(3))
            expected = {"kind": "slice_lower_bound", "a": 1, "b": width,
                        "dimensions": dimensions}
            if block != expected:
                raise ValueError("slice lower bound mismatch")
            score = Fraction(width)
        scores.append(score)
    source, target = profile(*dims[:2]), sum(scores, Fraction())
    expected = {"source": str(source), "target": str(target), "ratio": str(target / source)}
    if record["score"] != expected:
        raise ValueError("exact score mismatch")
    return target / source


def check_report(report):
    if report["schema_version"] != 1:
        raise ValueError("unsupported report version")
    q, max_sum = report["alphabet_size"], report["max_sum"]
    if report["coverage"] != coverage(q, max_sum):
        raise ValueError("ordered coverage mismatch")
    checked = 0
    for scope in ("historical", "omitted"):
        rows = report["dimension_summaries"][scope]
        expected_dims = {(a, b) for a in range(2, max_sum - 1)
                         for b in range(2, max_sum - a + 1)
                         if (a <= b) == (scope == "historical")}
        if len(rows) != len(expected_dims) or {tuple(r["dimensions"]) for r in rows} != expected_dims:
            raise ValueError("dimension inventory mismatch")
        for row in rows:
            a, b = row["dimensions"]
            if row["cases"] != normalized_arrays(q, a) * normalized_arrays(q, b):
                raise ValueError("dimension coverage mismatch")
            if not 0 <= row["violations"] <= row["cases"] or (
                Fraction(row["best_ratio"]) > 1) != (row["violations"] > 0):
                raise ValueError("dimension score summary mismatch")
        ratios = []
        for record in report["leaders"][scope]:
            ratios.append(check_record(record))
            a, b = record["support"]["dimensions"][:2]
            if (a, b) not in expected_dims or any(w >= q for axis in record["weights"] for w in axis):
                raise ValueError("leader outside declared search scope")
            checked += 1
        if rows and (not ratios or ratios != sorted(ratios, reverse=True) or
                     ratios[0] != max(Fraction(r["best_ratio"]) for r in rows)):
            raise ValueError("leader and dimension maximum mismatch")
    directional = report["orientation_comparison"]
    if sum(directional[k] for k in ("same", "omitted_better", "historical_better")) != report["coverage"]["omitted"]:
        raise ValueError("orientation census mismatch")
    for relation, pair in directional["witnesses"].items():
        left, right = pair
        left_score, right_score = check_record(left), check_record(right)
        if left["weights"] != right["weights"][::-1]:
            raise ValueError("orientation witness is not an input swap")
        expected = "omitted_better" if right_score > left_score else "historical_better"
        if left_score == right_score or relation != expected:
            raise ValueError("orientation witness inequality mismatch")
        checked += 2
    return {"retained_records_checked": checked,
            "coverage_arithmetic_checked": True,
            "limit": "Retained certificates and count formulas only; census maxima require a completed search replay."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+", type=Path)
    args = parser.parse_args()
    for path in args.reports:
        print(json.dumps({"report": str(path), **check_report(json.loads(path.read_text()))}))
