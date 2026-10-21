"""Verify the complete A_2 -> M(2,3,4) identity using rational arithmetic."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/cyclic-mixed-map-2026-10-20"


def source_terms(a):
    """Cyclic product, in X=(i,p+q,s), Y=(j,p,r+s), Z=(i+j,q,r)."""
    m = 2*a-1
    for i, j, p, q, r, s in product(range(a), repeat=6):
        yield ((i*m+p+q)*a+s, (j*a+p)*m+r+s, ((i+j)*a+q)*a+r)


def target_terms(l, h, n):
    return {(i*h+j, j*n+k, k*l+i): Fraction(1)
            for i, j, k in product(range(l), range(h), range(n))}


def contract(a, maps):
    by_column = []
    for entries in maps:
        columns = defaultdict(list)
        for row, column, coefficient in entries:
            columns[column].append((row, Fraction(coefficient)))
        by_column.append(columns)
    coefficients = defaultdict(Fraction)
    for x, y, z in source_terms(a):
        for (i, u), (j, v), (k, w) in product(
                by_column[0][x], by_column[1][y], by_column[2][z]):
            coefficients[i, j, k] += u*v*w
    return {key: value for key, value in coefficients.items() if value}


def load_maps(path=RESULTS / "witness.json"):
    data = json.loads(path.read_text())
    return [data["maps"][name] for name in ("A", "B", "C")]


def report(maps):
    shapes = (6, 12, 8)
    for entries, rows in zip(maps, shapes):
        positions = [(i, j) for i, j, _ in entries]
        if len(set(positions)) != len(positions):
            raise ValueError("Duplicate map entry")
        if any(not (0 <= i < rows and 0 <= j < 12) for i, j in positions):
            raise ValueError("Map entry outside its matrix")
    if any(Fraction(v).denominator != 1 for entries in maps for _, _, v in entries):
        raise ValueError("The all-field certificate requires integer entries")
    actual = contract(2, maps)
    expected = target_terms(2, 3, 4)
    errors = {key: actual.get(key, 0)-expected.get(key, 0)
              for key in set(actual) | set(expected)
              if actual.get(key, 0) != expected.get(key, 0)}
    return {
        "source": "A_2", "target": "M(2,3,4)",
        "source_terms": 64, "source_leg_dimensions": [12, 12, 12],
        "target_leg_dimensions": list(shapes),
        "map_nonzero_entries": [len(entries) for entries in maps],
        "coefficient_count": 6*12*8,
        "expected_nonzero_coefficients": len(expected),
        "actual_nonzero_coefficients": len(actual),
        "incorrect_coefficients": len(errors),
        "full_exact_equality": not errors,
        "arithmetic": "fractions.Fraction over Q",
        "coefficient_values": sorted({str(Fraction(v))
                                      for entries in maps for _, _, v in entries}),
        "valid_fields": "Every field (all witness entries are integers)",
        "independent_mathematical_review": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    result = report(load_maps())
    print(json.dumps(result, indent=2))
    if not result["full_exact_equality"]:
        raise SystemExit(1)
