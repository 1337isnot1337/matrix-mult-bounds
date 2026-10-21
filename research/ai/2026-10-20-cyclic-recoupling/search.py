"""Exact scores for sampled or binary outer-weight cyclic recoupling searches."""
import argparse
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
from pathlib import Path
import random

from coefficients import read_json, uniform_certificate, convolution_isomorphism, profile
from cg_search import components, cuberoot, direct_sum_interval

BITS = 80
SCALE = 1 << BITS


def leaf_interval(dims, iso, factor=Fraction(1)):
    rank = min(dims)
    low = cuberoot(rank**4*SCALE**3)
    high = low+(low**3 != rank**4*SCALE**3)
    if iso:
        value = profile(*iso["convolution_lengths"])
        other = value.numerator*SCALE//value.denominator
        low = max(low, other)
        high = max(high, other+(other*value.denominator != value.numerator*SCALE))
    return (low*factor.numerator//factor.denominator,
            (high*factor.numerator+factor.denominator-1)//factor.denominator)


def prepare(data, grouped):
    blocks, leaves = [], []
    if grouped:
        labels = [[d, 0] for d in data["degrees"]]
        for block in data["blocks"]:
            dims = tuple(d+1 for d in block["degrees"])
            leaves.append(leaf_interval(dims, block["cg_convolution_isomorphism"],
                                       Fraction(block["multiplicity_matching_profile_lower"])))
            blocks.append({"labels": tuple(block["labels"])})
    else:
        labels = [b["label"] for b in data["labels"]]
        for block in data["blocks"]:
            dims = tuple(data["labels"][i]["dimension"] for i in block["labels"])
            terms = [(i, j, k, Fraction(v)) for i, j, k, v in block["terms"]]
            uniform_certificate(dims, terms)
            iso = convolution_isomorphism({"dims": dims, "terms": terms})
            leaves.append(leaf_interval(dims, iso))
            blocks.append({"labels": tuple(block["labels"])})
    return labels, blocks, leaves


def indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def score_functions(blocks, leaves):
    def options(mask):
        chosen = tuple(indices(mask))
        for i in chosen:
            yield leaves[i], {"type": "block", "index": i}
        for axes in ((0, 1, 2), (0, 1), (0, 2), (1, 2)):
            pieces = components(blocks, chosen, axes)
            if len(pieces) <= 1:
                continue
            children = [score(piece) for piece in pieces]
            interval = (direct_sum_interval(children, BITS) if len(axes) == 3 else
                        (sum(c[0] for c in children), sum(c[1] for c in children)))
            yield interval, {"type": "direct" if len(axes) == 3 else "shared",
                             "axes": axes, "pieces": pieces}

    @lru_cache(maxsize=100000)
    def score(mask):
        bounds = [v for v, _ in options(mask)]
        return max(v[0] for v in bounds), max(v[1] for v in bounds)

    def expression(mask):
        _, tree = max(options(mask), key=lambda item: item[0][0])
        if "pieces" in tree:
            tree["children"] = [expression(piece) for piece in tree.pop("pieces")]
        return tree

    return score, expression


def candidates(labels, blocks, mode, a, trials):
    n = len(labels)
    by_z = [[i for i, b in enumerate(blocks) if b["labels"][2] == k] for k in range(n)]
    z_masks = [sum(1 << i for i, b in enumerate(blocks) if mask & (1 << b["labels"][2]))
               for mask in range(1, 1 << n)] if mode == "grouped-binary" else None
    records = {}
    seed = None if mode == "grouped-binary" else (202610214 if mode == "grouped-sampled" else 202610204)+a
    rng = random.Random(seed)
    count = 0
    if mode == "grouped-binary":
        weight_pairs = ((x, y) for x in product((0, 1), repeat=n) if min(x) == 0
                        for y in product((0, 1), repeat=n) if min(y) == 0)
    else:
        def sample_pairs():
            coefficients = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1))
            for trial in range(trials):
                if trial < 36:
                    yield tuple(sum(v*c for v, c in zip(l, coefficients[trial//6])) for l in labels), tuple(
                        sum(v*c for v, c in zip(l, coefficients[trial % 6])) for l in labels)
                else:
                    yield tuple(rng.randrange(-7, 8) for _ in labels), tuple(rng.randrange(-7, 8) for _ in labels)
        weight_pairs = sample_pairs()
    for x, y in weight_pairs:
        count += 1
        minima = [min(x[blocks[i]["labels"][0]]+y[blocks[i]["labels"][1]] for i in group) for group in by_z]
        face = sum(1 << i for i, b in enumerate(blocks)
                   if x[b["labels"][0]]+y[b["labels"][1]] == minima[b["labels"][2]])
        if z_masks is not None:
            xm = sum(v << i for i, v in enumerate(x))
            ym = sum(v << i for i, v in enumerate(y))
            for output_mask, z_mask in enumerate(z_masks, 1):
                mask = face & z_mask
                if mask and mask not in records:
                    records[mask] = (xm << (2*n)) | (ym << n) | output_mask
        else:
            for output_mask in [(1 << n)-1]+[rng.randrange(1, 1 << n) for _ in range(7)]:
                mask = sum(1 << i for i in indices(face) if output_mask & (1 << blocks[i]["labels"][2]))
                if mask and mask not in records:
                    records[mask] = (x, y, output_mask)
    return records, count, seed


def decode_weights(value, n, blocks):
    if isinstance(value, int):
        output_mask = value & ((1 << n)-1)
        ym = (value >> n) & ((1 << n)-1)
        xm = value >> (2*n)
        x = tuple((xm >> i) & 1 for i in range(n))
        y = tuple((ym >> i) & 1 for i in range(n))
    else:
        x, y, output_mask = value
    z = [-min(x[b["labels"][0]]+y[b["labels"][1]] for b in blocks if b["labels"][2] == k)
         for k in range(n)]
    return {"x": x, "y": y, "z": z, "output_mask": output_mask}


def search(data, mode, trials=3000):
    a = data["a"]
    labels, blocks, leaves = prepare(data, mode != "scalar-sampled")
    records, input_pairs, seed = candidates(labels, blocks, mode, a, trials)
    score, expression = score_functions(blocks, leaves)
    source = profile(a, a)**3
    best, best_mask, global_upper = (0, 0), None, 0
    violations, ambiguous = [], []
    for mask in records:
        interval = score(mask)
        global_upper = max(global_upper, interval[1])
        if interval > best:
            best, best_mask = interval, mask
        if Fraction(interval[0], SCALE) > source:
            violations.append(mask)
        elif Fraction(interval[1], SCALE) > source:
            ambiguous.append(mask)
    return {"a": a, "mode": mode, "seed": seed, "input_weight_pairs": input_pairs,
        "distinct_scored_supports": len(records), "interval_bits": BITS,
        "source_matching_profile_cubed": str(source),
        "global_ratio_upper": str(Fraction(global_upper, SCALE)/source),
        "violations": violations, "unresolved_interval_comparisons": ambiguous,
        "new_exponent_established": False,
        "best": {"weights": decode_weights(records[best_mask], len(labels), blocks),
            "retained_blocks": list(indices(best_mask)),
            "score_interval": [str(Fraction(v, SCALE)) for v in best],
            "ratio_interval": [str(Fraction(v, SCALE)/source) for v in best],
            "expression": expression(best_mask)}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--mode", choices=("scalar-sampled", "grouped-sampled", "grouped-binary"), required=True)
    parser.add_argument("--trials", type=int, default=3000)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = search(read_json(args.input), args.mode, args.trials)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print({k: v for k, v in result.items() if k != "best"})
