#!/usr/bin/env python3
"""Exact compressed convolution maps and their entire Laurent tensor."""

import argparse
from collections import Counter
from math import comb
import json
from pathlib import Path


def source_maps(m):
    if m < 2 or m % 2:
        raise ValueError("m must be a positive even integer at least two")
    s, d = m // 2, m - 1
    y, z = {}, {}
    for i in range(s):
        start = i * (m + 1)
        for degree, block_start, weight in ((i, start, 0),
                                             (d - i, start + i + 1, 1)):
            for a in range(degree + 1):
                index = block_start + degree - a
                assert index not in y
                y[index] = (a, degree - a, weight)
            for c in range(d - degree + 1):
                index = block_start + degree + c
                assert index not in z
                z[index] = (c, d - degree - c, -weight)
    n = m * (m + 1) // 2
    assert set(y) == set(range(n))
    assert len(z) == n and max(z) == n + s - 2
    assert max(z) < n + m - 1
    return y, z


def transform(m, scale_edges=False):
    """Enumerate every nonzero source term; keys are (power,X,a,b,c,d)."""
    y, z = source_maps(m)
    central = set(range(max(0, m // 2 - 2), m // 2 + 1))
    result = Counter()
    source_terms = 0
    for x in range(m):
        for j in range(m * (m + 1) // 2):
            source_terms += 1
            if x + j not in z:
                continue
            a, b, yw = y[j]
            c, d, zw = z[x + j]
            power = yw + zw + int(scale_edges and x not in central)
            result[(power, x, a, b, c, d)] += 1
    return result, source_terms


def fatpoint(m):
    out = Counter()
    for a in range(m):
        for b in range(m - a):
            for c in range(m - a - b):
                d = m - 1 - a - b - c
                out[(a + c, a, b, c, d)] += 1
    return out


def negative_formula(m):
    """The two explicit low-degree error families, independent of maps."""
    out = Counter()
    for i in range(1, m // 2):
        for a in range(i + 1):
            for c in range(i + 1):
                if a + c <= i - 1:
                    out[(m - i + a + c, a, i - a, c, i - c)] += 1
            for c in range(i):
                if a + c >= i + 1:
                    out[(a + c - i - 1, a, i - a, c, i - 1 - c)] += 1
    return out


def coefficient(tensor, power):
    return Counter({key[1:]: value for key, value in tensor.items()
                    if key[0] == power and value})


def check(m):
    original, count = transform(m)
    assert set(key[0] for key in original) <= {-1, 0, 1}
    expected_target = fatpoint(m)
    expected_negative = negative_formula(m)
    assert coefficient(original, 0) == expected_target
    assert coefficient(original, -1) == expected_negative
    s = m // 2
    assert len(expected_target) == comb(m + 2, 3)
    assert len(expected_negative) == s * (s - 1) * (2 * s - 1) // 6
    central = set(range(max(0, s - 2), s + 1))
    assert not (central & {key[0] for key in expected_negative})
    scaled, scaled_count = transform(m, scale_edges=True)
    assert count == scaled_count
    assert min(key[0] for key in scaled) == 0
    expected_limit = expected_negative.copy()
    expected_limit.update({key: value for key, value in expected_target.items()
                           if key[0] in central})
    assert coefficient(scaled, 0) == expected_limit
    assert set(key[0] for key in scaled) <= {0, 1, 2}
    return {
        "m": m, "source_B": m * (m + 1) // 2,
        "source_terms_enumerated": count,
        "fatpoint_terms": len(expected_target),
        "negative_terms": len(expected_negative),
        "positive_terms": len(coefficient(original, 1)),
        "central_shared_indices": sorted(central),
        "negative_shared_indices": sorted({key[0] for key in expected_negative}),
        "alternate_limit_terms": len(expected_limit),
        "exact_laurent_identity": True,
        "exact_alternate_degeneration": True,
    }


def report(max_m):
    if max_m < 2:
        raise ValueError("max_m must be at least two")
    cases = [check(m) for m in range(2, max_m + 1, 2)]
    original, _ = transform(4)
    alternate, _ = transform(4, scale_edges=True)
    return {
        "status": "exact alternative tensor construction; no exponent improvement",
        "field": "integers, hence valid over every field",
        "cases": cases,
        "totals": {"cases": len(cases),
                   "source_terms_enumerated": sum(c["source_terms_enumerated"] for c in cases)},
        "m4_original_terms": [list(key) + [value] for key, value in sorted(original.items())],
        "m4_alternate_constant_terms": [list(key) + [value] for key, value in
                                         sorted(coefficient(alternate, 0).items())],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-m", type=int, default=40)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = report(args.max_m)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
