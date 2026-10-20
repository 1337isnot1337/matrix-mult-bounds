"""Certified upper bounds for every whole-block matching on a finite grid."""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import cache
from itertools import product
import json
from math import isqrt, perm
from pathlib import Path

from verify_filtration import profile


@cache
def power_interval(value, bits=96):
    """Integer endpoints in units 2^-bits containing value^(3/4)."""
    value = Fraction(value)
    if value <= 0 or not isinstance(bits, int) or bits < 1:
        raise ValueError("positive value and positive integer precision required")
    scaled_numerator = value.numerator**3 << (4 * bits)
    denominator = value.denominator**3
    lower = isqrt(isqrt(scaled_numerator // denominator))
    exact = lower**4 * denominator == scaled_numerator
    return lower, lower if exact else lower + 1


def maximum_matching(weights):
    """Exact maximum integer weight, allowing any columns on the longer side."""
    if not weights or not weights[0] or any(len(r) != len(weights[0]) for r in weights):
        raise ValueError("nonempty rectangular weight matrix required")
    transposed = len(weights) > len(weights[0])
    table = list(map(list, zip(*weights))) if transposed else weights
    states = {0: (0, ())}
    for row in table:
        following = {}
        for mask, (value, choices) in states.items():
            for j, weight in enumerate(row):
                if mask & (1 << j):
                    continue
                next_mask = mask | (1 << j)
                candidate = (value + weight, choices + (j,))
                if next_mask not in following or candidate[0] > following[next_mask][0]:
                    following[next_mask] = candidate
        states = following
    best, choices = max(states.values(), key=lambda x: x[0])
    pairs = [(j, i) if transposed else (i, j) for i, j in enumerate(choices)]
    return best, pairs


def line_certificate(a, b, c, d, r=1, s=-1, u=0):
    if any(not isinstance(n, int) or n < 1 for n in (a, b, c, d)):
        raise ValueError("positive integer dimensions required")
    if any(not isinstance(n, int) for n in (r, s, u)) or r * s * (r - s) == 0:
        raise ValueError("integer line coefficients must distinguish all three labels")
    ni, nj, nk = min(a, c), min(b, d), min(a + b - 1, c + d - 1)
    x = [(r * r - r * s) * i * i + 2 * r * u * i + u * u for i in range(ni)]
    y = [(s * s - r * s) * j * j + 2 * s * u * j for j in range(nj)]
    z = [r * s * k * k for k in range(nk)]
    separation = 1 + sum(max(map(abs, weights)) for weights in (x, y, z))
    x = [weight - separation * i for i, weight in enumerate(x)]
    y = [weight - separation * j for j, weight in enumerate(y)]
    z = [weight + separation * k for k, weight in enumerate(z)]
    retained = []
    for i, j, k in product(range(ni), range(nj), range(nk)):
        if k < i + j:
            continue  # This entire block vanishes by the filtration theorem.
        weight = x[i] + y[j] + z[k]
        if weight < 0 or (k > i + j and weight == 0):
            raise ArithmeticError("invalid filtration weight certificate")
        if k == i + j and weight != (r * i + s * j + u)**2:
            raise ArithmeticError("square identity failed")
        if weight == 0:
            retained.append([i, j, k])
    for leg in range(3):
        if len({point[leg] for point in retained}) != len(retained):
            raise ArithmeticError("retained blocks are not a full direct sum")
    return {"source": [a, b, c, d], "line": [r, s, u],
            "x_weights": x, "y_weights": y, "z_weights": z,
            "separation_multiplier": separation, "retained_labels": retained}


def run(n=9, bits=96):
    if not isinstance(n, int) or n < 1:
        raise ValueError("positive integer grid size required")
    single = nontrivial = relaxed_matchings = 0
    best_ratio = Fraction()
    best = None
    for a, b, c, d in product(range(1, n + 1), repeat=4):
        aa = [a + c - 1 - 2 * i for i in range(min(a, c))]
        bb = [b + d - 1 - 2 * j for j in range(min(b, d))]
        source = profile(a, b) * profile(c, d)
        relaxed_matchings += perm(max(len(aa), len(bb)), min(len(aa), len(bb)))
        if min(len(aa), len(bb)) == 1:
            # Every possible target is at most the top-left cell.
            if profile(aa[0], bb[0]) > source:
                raise ArithmeticError("single-block violation")
            single += 1
            continue
        intervals = [[power_interval(profile(x, y), bits) for y in bb] for x in aa]
        upper, pairs = maximum_matching([[bound[1] for bound in row] for row in intervals])
        lower_source, upper_source = power_interval(source, bits)
        if upper > lower_source:
            raise ArithmeticError("interval upper bound does not certify compatibility",
                                  [a, b, c, d], upper, lower_source)
        nontrivial += 1
        ratio = Fraction(upper, lower_source)
        if ratio > best_ratio:
            best_ratio = ratio
            best = {"source": [a, b, c, d], "source_profile_product": str(source),
                    "chosen_matching": pairs,
                    "block_dimensions": [[aa[i], bb[j]] for i, j in pairs],
                    "block_profile_values": [str(profile(aa[i], bb[j])) for i, j in pairs],
                    "sum_upper_units": upper, "source_lower_units": lower_source,
                    "source_upper_units": upper_source,
                    "ratio_upper_bound": str(ratio)}
    return {"max_source_dimension": n, "source_quadruples": n**4,
            "single_block_cases_exact_rational": single,
            "nontrivial_matching_cases_certified": nontrivial,
            "maximal_relaxed_matchings_covered": relaxed_matchings,
            "interval_bits": bits, "violations": 0,
            "best_nontrivial_upper_bound": best,
            "smallest_diagonal_extraction": line_certificate(2, 2, 2, 2),
            "scope": "Finite whole-block matching upper bounds; no all-size or omega claim."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-size", type=int, default=9)
    parser.add_argument("--bits", type=int, default=96)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run(args.max_size, args.bits)
    content = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content)
    print(content, end="")
