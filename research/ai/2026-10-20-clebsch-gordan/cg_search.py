"""Search full recoupling-block degenerations with certified score intervals."""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import cache
from itertools import permutations, product
import json
from math import isqrt
from pathlib import Path
import sys

from cg_blocks import full_blocks, convolution_isomorphism, dot_slice_bound

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "2026-10-20-affine-direct-sums"))
from verify_filtration import profile


@cache
def coordinate_convolution_bound(dims, terms):
    """Check exact interval-coordinate restrictions, beyond whole-block recognition."""
    best = Fraction(1)
    witness = None
    for axes in permutations(range(3)):
        oriented = [dims[axis] for axis in axes]
        for aa in range(2, oriented[0] + 1):
            for bb in range(2, oriented[1] + 1):
                cc = aa + bb - 1
                if cc > oriented[2] or profile(aa, bb) <= best:
                    continue
                target = (aa, bb, cc)
                for starts in product(*(range(n - m + 1) for n, m in zip(oriented, target))):
                    selected = []
                    for *coordinates, coefficient in terms:
                        point = tuple(coordinates[axis] - start for axis, start in zip(axes, starts))
                        if all(0 <= value < size for value, size in zip(point, target)):
                            selected.append((*point, coefficient))
                    if len(selected) != aa * bb:
                        continue
                    iso = convolution_isomorphism({"dims": target, "terms": selected})
                    if iso:
                        best = profile(aa, bb)
                        witness = {"source_axes": list(axes), "starts": list(starts),
                                   "target_dimensions": list(target), "isomorphism": iso}
    return best, witness


def cuberoot(n):
    if n < 2:
        return n
    x = 1 << ((n.bit_length() + 2) // 3)
    while True:
        y = (2 * x + n // (x * x)) // 3
        if y >= x:
            return x
        x = y


def direct_sum_interval(intervals, bits):
    q = 1 << bits
    low = high = 0
    for lower, upper in intervals:
        n = lower**3 * q
        r = isqrt(isqrt(n))
        low += r
        n = upper**3 * q
        r = isqrt(isqrt(n))
        high += r + (r**4 != n)
    lower = cuberoot(low**4 // q)
    upper = cuberoot(high**4 // q)
    upper += upper**3 * q != high**4
    return lower, upper


def components(blocks, selected, axes):
    parents = {}

    def find(x):
        parents.setdefault(x, x)
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x

    def union(x, y):
        parents[find(x)] = find(y)

    for n in selected:
        labels = blocks[n]["labels"]
        vertices = [(axis, labels[axis]) for axis in axes]
        for vertex in vertices[1:]:
            union(vertices[0], vertex)
    parts = {}
    for n in selected:
        first = (axes[0], blocks[n]["labels"][axes[0]])
        parts.setdefault(find(first), 0)
        parts[find(first)] |= 1 << n
    return list(parts.values())


def search_source(dims, alphabet=(0, 1), bits=80, strengthen=False):
    blocks = full_blocks(*dims)
    q = 1 << bits
    leaf_intervals = []
    recognition = []
    for block in blocks:
        iso = convolution_isomorphism(block)
        if iso:
            value = profile(*iso["convolution_lengths"])
            recognition.append({"kind": "convolution", "isomorphism": iso})
        else:
            value = Fraction(dot_slice_bound(block))
            recognition.append({"kind": "coordinate-dot-slice", "lower_bound": str(value)})
            if strengthen:
                stronger, witness = coordinate_convolution_bound(tuple(block["dims"]), tuple(block["terms"]))
                if stronger > value:
                    value = stronger
                    recognition[-1] = {"kind": "coordinate-convolution-restriction",
                                       "lower_bound": str(value), "restriction": witness}
        lower = value.numerator * q // value.denominator
        upper = lower + (lower * value.denominator != value.numerator * q)
        leaf_intervals.append((lower, upper))

    @cache
    def score(mask):
        chosen = [i for i in range(len(blocks)) if mask & (1 << i)]
        options = [(leaf_intervals[i], {"type": "block", "index": i}) for i in chosen]
        if len(chosen) > 1:
            partitions = [("direct", components(blocks, chosen, (0, 1, 2)))]
            partitions += [("shared", components(blocks, chosen, axes))
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
        best = max(options, key=lambda option: option[0][0])
        return (max(v[0][0] for v in options), max(v[0][1] for v in options)), best[1]

    ni = min(dims[0], dims[2])
    nj = min(dims[1], dims[3])
    nk = min(dims[0] + dims[1] - 1, dims[2] + dims[3] - 1)
    z_masks = [sum((1 << n) for n, block in enumerate(blocks) if subset & (1 << block["labels"][2]))
               for subset in range(1, 1 << nk)]
    records = {}
    for x in product(alphabet, repeat=ni):
        if min(x) != 0:
            continue
        for y in product(alphabet, repeat=nj):
            if min(y) != 0:
                continue
            minima = [min(x[i] + y[j] for block in blocks
                          for i, j, kk in [block["labels"]] if kk == k)
                      for k in range(nk)]
            face = sum(1 << n for n, block in enumerate(blocks)
                       if x[block["labels"][0]] + y[block["labels"][1]] == minima[block["labels"][2]])
            for z_mask in z_masks:
                mask = face & z_mask
                if mask and mask not in records:
                    records[mask] = {"x": x, "y": y, "z": [-v for v in minima],
                                     "kept_output_labels": [k for k in range(nk)
                                                            if any(mask & (1 << n)
                                                                   for n, block in enumerate(blocks)
                                                                   if block["labels"][2] == k)]}
    source = profile(dims[0], dims[1]) * profile(dims[2], dims[3])
    best_upper = Fraction()
    best = None
    violations = []
    ambiguous = []
    for mask, weights in records.items():
        interval, witness = score(mask)
        lower = Fraction(interval[0], q)
        upper = Fraction(interval[1], q)
        if upper / source > best_upper:
            best_upper = upper / source
            best = {"ratio_lower": str(lower / source), "ratio_upper": str(upper / source),
                    "weights": weights, "support_mask": mask, "expression": witness}
        if lower > source:
            violations.append({"mask": mask, "weights": weights, "expression": witness,
                               "ratio_lower": str(lower / source)})
        elif upper > source:
            ambiguous.append(mask)
    return {"source": list(dims), "source_profile": str(source),
            "outer_nonzero_blocks": len(blocks),
            "off_leading_blocks": sum(b["labels"][2] > sum(b["labels"][:2]) for b in blocks),
            "recognized_convolution_blocks": sum(v["kind"] == "convolution" for v in recognition),
            "distinct_scored_supports": len(records), "interval_bits": bits,
            "coordinate_restrictions_enabled": strengthen,
            "best": best, "violations": violations, "unresolved_interval_comparisons": ambiguous,
            "blocks": [{"labels": b["labels"], "dimensions": b["dims"],
                        "terms": [[i, j, k, str(v)] for i, j, k, v in b["terms"]],
                        **recognition[n]} for n, b in enumerate(blocks)]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", default="2,2,2,2;3,3,3,3;4,4,4,4;2,3,3,2;2,4,4,2;3,4,4,3")
    parser.add_argument("--alphabet", default="0,1")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--strengthen", action="store_true")
    args = parser.parse_args()
    reports = []
    for source in args.sources.split(";"):
        dims = tuple(map(int, source.split(",")))
        report = search_source(dims, tuple(map(int, args.alphabet.split(","))), strengthen=args.strengthen)
        reports.append(report)
        print({key: value for key, value in report.items() if key not in ("blocks", "best")}, flush=True)
    data = {"scope": "Finite full-CG outer-weight supports and recursive component scores; no omega bound.",
            "sources": reports}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2) + "\n")
