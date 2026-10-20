"""Exact-score searches for degenerations of truncated polynomial algebras.

W_r=sum_{i+j+k=r-1} x_i y_j z_k has border rank r over C. Unlike an
ordinary convolution, this source can be compared directly with r^(4/3).
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import product
import json
from pathlib import Path
import sys

AI = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(AI / "2026-10-20-clebsch-gordan"))
sys.path.insert(0, str(AI / "2026-10-20-affine-direct-sums"))
from cg_blocks import convolution_isomorphism
from verify_filtration import profile
from cg_search import direct_sum_interval, components


def search_size(r, alphabet=(0, 1), bits=80, delete_outputs=False):
    terms = [(i, j, r - 1 - i - j) for i in range(r) for j in range(r - i)]
    blocks = [{"labels": term} for term in terms]
    q = 1 << bits

    @cache
    def score(mask):
        selected = [n for n in range(len(terms)) if mask & (1 << n)]
        selected_terms = [terms[n] for n in selected]
        labels = [sorted({point[axis] for point in selected_terms}) for axis in range(3)]
        maps = [{v: n for n, v in enumerate(axis)} for axis in labels]
        compressed = [(*(maps[axis][point[axis]] for axis in range(3)), Fraction(1))
                      for point in selected_terms]
        iso = convolution_isomorphism({"dims": tuple(map(len, labels)), "terms": compressed})
        if iso:
            value = profile(*iso["convolution_lengths"])
            expr = {"type": "convolution", "terms": selected_terms, "isomorphism": iso}
        else:
            value = Fraction(max(max(Counter(point[axis] for point in selected_terms).values())
                                 for axis in range(3)))
            expr = {"type": "dot-slice", "terms": selected_terms, "rank": int(value)}
        lower = value.numerator * q // value.denominator
        upper = lower + (lower * value.denominator != value.numerator * q)
        options = [((lower, upper), expr)]
        if len(selected) > 1:
            partitions = [("direct", components(blocks, selected, (0, 1, 2)))]
            partitions += [("shared", components(blocks, selected, axes))
                           for axes in ((1, 2), (0, 2), (0, 1))]
            for kind, pieces in partitions:
                if len(pieces) <= 1:
                    continue
                children = [score(piece) for piece in pieces]
                bounds = [child[0] for child in children]
                interval = (sum(v[0] for v in bounds), sum(v[1] for v in bounds))
                if kind == "direct":
                    interval = direct_sum_interval(bounds, bits)
                options.append((interval, {"type": kind, "children": [child[1] for child in children]}))
            if delete_outputs:
                for label in sorted({point[2] for point in selected_terms}):
                    restricted = sum(1 << n for n in selected if terms[n][2] != label)
                    if not restricted:
                        continue
                    child = score(restricted)
                    options.append((child[0], {"type": "restriction", "axis": 2,
                                               "deleted_label": label, "child": child[1]}))
        best = max(options, key=lambda option: option[0][0])
        return (max(v[0][0] for v in options), max(v[0][1] for v in options)), best[1]

    seen = set()
    best = None
    best_lower = 0
    cases = 0
    violations = []
    ambiguous = []
    for x in product(alphabet, repeat=r):
        if min(x) != 0:
            continue
        for y in product(alphabet, repeat=r):
            if min(y) != 0:
                continue
            cases += 1
            minima = [min(x[i] + y[r - 1 - k - i] for i in range(r - k)) for k in range(r)]
            mask = sum(1 << n for n, (i, j, k) in enumerate(terms) if x[i] + y[j] == minima[k])
            if mask in seen:
                continue
            seen.add(mask)
            interval, expr = score(mask)
            candidate = {"x_weights": x, "y_weights": y, "z_weights": [-v for v in minima],
                         "score_lower": str(Fraction(interval[0], q)),
                         "score_upper": str(Fraction(interval[1], q)), "expression": expr}
            if interval[0] > best_lower:
                best_lower = interval[0]
                best = candidate
            if interval[0]**3 > r**4 * q**3:
                violations.append(candidate)
            elif interval[1]**3 > r**4 * q**3:
                ambiguous.append({"x": x, "y": y, "interval": interval})
    return {"source": "truncated-polynomial", "r": r, "border_rank_upper": r,
            "alphabet": list(alphabet), "candidate_cases": cases,
            "distinct_supports": len(seen), "interval_bits": bits,
            "recursive_output_deletions": delete_outputs,
            "best": best, "strict_critical_parameter_violations": violations,
            "unresolved_interval_comparisons": ambiguous,
            "scope": "Finite normalized input-weight arrays, optional coordinate output deletions; no arbitrary bases."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-size", type=int, default=2)
    parser.add_argument("--max-size", type=int, default=7)
    parser.add_argument("--alphabet", default="0,1")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--delete-outputs", action="store_true")
    args = parser.parse_args()
    reports = []
    for r in range(args.min_size, args.max_size + 1):
        report = search_size(r, tuple(map(int, args.alphabet.split(","))), delete_outputs=args.delete_outputs)
        reports.append(report)
        print({key: value for key, value in report.items() if key != "best"}, flush=True)
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps({"sources": reports}, indent=2) + "\n")
