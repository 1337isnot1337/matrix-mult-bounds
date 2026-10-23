"""Exact finite controls for the all-size width-two support score proof."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def profile(a, b):
    a, b = sorted((a, b))
    h = Fraction(1)
    for k in range(1, a):
        h *= Fraction(3 * k + 1, 3 * k)
    return h * Fraction(2 * b + a - 1, 2)


def components(terms):
    """Traverse the actual Y-Z incidence graph, without a path assumption."""
    incident = {}
    for term in terms:
        for vertex in ((1, term[1]), (2, term[2])):
            incident.setdefault(vertex, set()).add(term)
    unseen = set(terms)
    groups = []
    while unseen:
        pending = [min(unseen)]
        group = set()
        while pending:
            term = pending.pop()
            if term not in unseen:
                continue
            unseen.remove(term)
            group.add(term)
            for vertex in ((1, term[1]), (2, term[2])):
                pending.extend(incident[vertex] & unseen)
        groups.append(tuple(sorted(group)))
    return groups


def recognize_score(terms):
    """Compare full coordinate sets with convolution supports, then slices."""
    axes = [sorted({term[k] for term in terms}) for k in range(3)]
    dims = list(map(len, axes))
    indexes = [{v: i for i, v in enumerate(axis)} for axis in axes]
    for output in range(3):
        left, right = [k for k in range(3) if k != output]
        a, b = dims[left], dims[right]
        if dims[output] != a + b - 1 or len(terms) != a * b:
            continue
        for signs in product((1, -1), repeat=3):
            actual = {
                tuple(indexes[k][term[k]] if signs[k] == 1
                      else dims[k] - 1 - indexes[k][term[k]]
                      for k in range(3))
                for term in terms
            }
            expected = set()
            for i, j in product(range(a), range(b)):
                row = [0, 0, 0]
                row[left], row[right], row[output] = i, j, i + j
                expected.add(tuple(row))
            if actual == expected:
                return profile(a, b)
    return Fraction(max(max(Counter(t[k] for t in terms).values())
                        for k in range(3)))


def score(terms):
    return sum((recognize_score(group) for group in components(terms)), Fraction(0))


def path_gap(b, terms):
    """The proved identity, evaluated independently of block recognition."""
    used_y = {t[1] for t in terms}
    used_z = {t[2] for t in terms}
    odd_y = sum(len({t[1] for t in group})
                for group in components(terms) if len(group) % 2)
    return Fraction(2 * ((b - len(used_y)) + (b + 1 - len(used_z))) + odd_y, 3)


def all_supports(b, reverse=False):
    source = [(i, j, i + j) for i in range(2) for j in range(b)]
    if reverse:
        source = [(j, i, k) for i, j, k in source]
    for mask in range(1 << len(source)):
        yield tuple(term for index, term in enumerate(source) if mask >> index & 1)


def verify(max_b):
    rows = []
    for b in range(2, max_b + 1):
        for reverse in (False, True):
            best = Fraction(0)
            equality = 0
            cases = 0
            for terms in all_supports(b, reverse):
                value = score(terms)
                if value > profile(2, b):
                    raise ValueError("support score exceeds the claimed bound")
                if not reverse and profile(2, b) - value != path_gap(b, terms):
                    raise ValueError("path deficit identity fails")
                if reverse and (value == profile(2, b)) != (len(terms) == 2 * b):
                    raise ValueError("reversed equality classification fails")
                equality += value == profile(2, b)
                best = max(best, value)
                cases += 1
            rows.append({"b": b, "shared_axis": "large" if reverse else "two",
                         "supports": cases, "maximum_exact": str(best),
                         "equality_supports": equality})
    return {"schema": "width-two-support-controls-v1", "max_b": max_b,
            "supports_checked": sum(row["supports"] for row in rows),
            "rows": rows, "universal_proof_status": "written-unreviewed",
            "improves_omega": False}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-b", type=int, default=7)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.max_b < 2:
        parser.error("max-b must be at least two")
    report = verify(args.max_b)
    data = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(data)
    print(data, end="")
