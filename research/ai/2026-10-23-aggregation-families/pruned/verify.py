#!/usr/bin/env python3
"""Exact source-grade and all-n nonzero-position acceptance for pruned grids."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from math import comb, isqrt
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent


def read_source(source_id: str, path: Path | None = None) -> dict:
    registry = json.loads((HERE / "sources.json").read_text())
    record = next(row for row in registry["sources"] if row["id"] == source_id)
    path = HERE / record["file"] if path is None else path
    if hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
        raise ValueError("External source SHA256 mismatch")
    rows, corrections = [], []
    mode = ""
    dimension = None
    for line in path.read_text().splitlines():
        if line.startswith("d:"):
            dimension = int(line.split(":")[1])
        elif line in ("[products]", "[corrections]"):
            mode = line
        elif mode == "[products]" and re.match(r"^\d+\s*\|", line):
            fields = [field.strip() for field in line.split("|")]
            parts = [list(map(int, re.findall(r"\d+", field))) for field in fields[1:4]]
            rows.append({**dict(zip("UVW", parts)), "grades": [int(value) for value in fields[4:7]]})
        elif mode == "[corrections]" and line.startswith("{"):
            corrections.append(list(map(int, re.findall(r"\d+", line))))
    if len(rows) != record["products"]:
        raise ValueError("External product count differs from its pin")
    return {"source_id": source_id, "source_sha256": record["sha256"],
            "coordinate_count": dimension, "products": rows, "correction_subsets": corrections}


def verify_grades(data: dict) -> dict:
    d = data["coordinate_count"]
    if type(d) is not int or d <= 0:
        raise ValueError("Invalid coordinate count")
    universe = set(range(d))
    rows, grades = [], []
    for row in data["products"]:
        parts = [frozenset(row[leg]) for leg in "UVW"]
        if any(len(part) != len(row[leg]) or not part <= universe for leg, part in zip("UVW", parts)):
            raise ValueError("Malformed coordinate part")
        if set.union(*(set(p) for p in parts)) != universe or sum(map(len, parts)) != d:
            raise ValueError("Parts must form a complete partition")
        grade = row["grades"]
        if len(grade) != 3 or any(type(value) is not int for value in grade) or sum(grade):
            raise ValueError("Diagonal scalar grade must be zero")
        rows.append(parts)
        grades.append(grade)
    corrections = [frozenset(p) for p in data["correction_subsets"]]
    if len(corrections) != len(set(corrections)) or any(not p or not p <= universe for p in corrections):
        raise ValueError("Malformed correction list")
    counts = Counter()
    min_positive = None
    for i, j, k in product(range(len(rows)), repeat=3):
        if i == j == k:
            counts["diagonal"] += 1
            continue
        selected = rows[i][0], rows[j][1], rows[k][2]
        eta = [sum(r in part for part in selected) for r in range(d)]
        if 2 in eta:
            counts["centered"] += 1
            continue
        replicated = set.intersection(*(set(p) for p in selected))
        coefficient = 1 + sum((-1)**len(p) for p in corrections if p <= replicated)
        if coefficient == 0:
            counts["corrected"] += 1
            continue
        degree = grades[i][0] + grades[j][1] + grades[k][2]
        if degree <= 0:
            raise ValueError(f"Uncancelled nonpositive mixed grade at {(i, j, k)}")
        counts["positive_grade"] += 1
        min_positive = degree if min_positive is None else min(min_positive, degree)
    return {"accepted": True, "products": len(rows), "ordered_mixed_triples": len(rows)**3,
            "class_counts": dict(sorted(counts.items())), "minimum_remaining_grade": min_positive,
            "correction_counts_by_size": {str(size): count for size, count in sorted(Counter(map(len, corrections)).items())}}


def pruning_floor(p: int, d: int) -> dict:
    if type(p) is not int or p <= 0 or type(d) is not int or d <= 0:
        raise ValueError("Positive product and coordinate counts are required")
    left, right = p**4 * 3**(3*d), 4**(4*d)
    return {"products": p, "coordinates": d, "p_fourth_times_3_power_3d": left,
            "4_power_4d": right, "strict_integer_margin": right-left,
            "excluded_for_all_dimensions_with_common_support_condition": left < right}


def check_profiles(data: dict, profiles: list[int]) -> None:
    full = (1 << data["coordinate_count"]) - 1
    if len(profiles) != len(data["products"]) or any(type(h) is not int or h < 0 or h > full for h in profiles):
        raise ValueError("One valid dimension profile is required for every product")


def position_polynomials(data: dict, profiles: list[int]) -> dict:
    """Count every (P,L) by set membership; coefficients use v=n-1."""
    check_profiles(data, profiles)
    d = data["coordinate_count"]
    universe = frozenset(range(d))
    high = [frozenset(r for r in range(d) if h >> r & 1) for h in profiles]
    parts = [[frozenset(row[leg]) for leg in "UVW"] for row in data["products"]]
    total, main, corrections = Counter(), Counter(), []
    for values in [[]] + data["correction_subsets"]:
        p = frozenset(values)
        remaining = sorted(universe - p)
        eligible = [[t for t, row in enumerate(parts) if p <= row[leg]] for leg in range(3)]
        polynomial = Counter()
        surviving_types = 0
        for flags in product((False, True), repeat=len(remaining)):
            h = frozenset(r for r, keep in zip(remaining, flags) if keep)
            if all(any(h <= high[t] | parts[t][leg] for t in eligible[leg]) for leg in range(3)):
                polynomial[len(h)] += 2**(d-len(p)-len(h))
                surviving_types += 1
        total.update(polynomial)
        if not p:
            main = polynomial
        else:
            corrections.append({"P": sorted(p), "surviving_high_coordinate_types": surviving_types,
                                "coefficients_in_n_minus_one": render(polynomial)})
    return {"total_coefficients_in_n_minus_one": render(total),
            "main_coefficients_in_n_minus_one": render(main), "corrections": corrections,
            "target_volume_exponent_counts": render(Counter(h.bit_count() for h in profiles))}


def render(polynomial):
    return {str(power): value for power, value in sorted(polynomial.items(), reverse=True) if value}


def expand_in_n(polynomial: dict) -> dict:
    expanded = Counter()
    for power, coefficient in polynomial.items():
        power = int(power)
        for k in range(power+1):
            expanded[k] += coefficient*comb(power, k)*(-1)**(power-k)
    return render(expanded)


def featured_construction(data: dict, witness: dict) -> dict:
    if witness["source_id"] != data["source_id"] or len(data["products"]) != 22:
        raise ValueError("The featured construction must use the pinned 22-product source")
    profiles = witness["profiles"]
    polynomials = position_polynomials(data, profiles)
    expanded = expand_in_n(polynomials["total_coefficients_in_n_minus_one"])
    if expanded != witness["rank_polynomial_coefficients_n"]:
        raise ValueError("The featured multiplication count is understated or changed")
    if set(h.bit_count() for h in profiles) != {5}:
        raise ValueError("Every featured target must have volume n^5")
    shapes = Counter(tuple(sum(h >> r & 1 for r in row[leg]) for leg in "VWU")
                     for h, row in zip(profiles, data["products"]))
    delta = {k: 22*int(k == 5)-expanded.get(str(k), 0) for k in range(6)}
    shifted = {j: sum(coefficient*comb(power, j)*4**(power-j)
                      for power, coefficient in delta.items() if power >= j) for j in range(6)}
    if any(coefficient <= 0 for coefficient in shifted.values()):
        raise ValueError("The n>=4 comparison with classical cost is not certified")
    return {"rank_polynomial_coefficients_n": expanded,
            "main_polynomial_coefficients_n": expand_in_n(polynomials["main_coefficients_in_n_minus_one"]),
            "matrix_shape_exponent_counts": [{"A_B_C_exponents": list(shape), "products": count}
                                              for shape, count in sorted(shapes.items())],
            "classical_minus_pruned_coefficients_after_n_equals_4_plus_u": render(shifted),
            "all_n_scope": "Border-rank upper bound over characteristic zero for every integer n>=2",
            "classical_comparison_scope": "Smaller border-rank budget than the 22*n^5 classical rank upper bound for n>=4; no finite-precision runtime claim",
            "critical_mass": "22*n^(15/4)", "improves_omega": False}


def value(polynomial: dict, n: int) -> int:
    return sum(coefficient*(n-1)**int(power) for power, coefficient in polynomial.items())


def direct_grid_count(data: dict, profiles: list[int], n: int) -> dict:
    """Independent Cartesian grid enumeration, without high-type compression."""
    check_profiles(data, profiles)
    d, q = data["coordinate_count"], n+1
    counts = []
    for omitted in [[]] + data["correction_subsets"]:
        p = set(omitted)
        remaining = [r for r in range(d) if r not in p]
        count = 0
        for positions in product(range(q), repeat=len(remaining)):
            assignment = dict(zip(remaining, positions))
            factors = []
            for leg in "UVW":
                factor_nonzero = False
                for profile, row in zip(profiles, data["products"]):
                    part = set(row[leg])
                    if not p <= part:
                        continue
                    if all(r in part or profile >> r & 1 or assignment[r] in (0, q-1)
                           for r in remaining):
                        factor_nonzero = True
                        break
                factors.append(factor_nonzero)
            count += all(factors)
        counts.append(count)
    return {"n": n, "main_positions": counts[0], "correction_positions": counts[1:], "total_positions": sum(counts)}


def mass_interval(profiles: list[int], n: int) -> dict:
    if type(n) is not int or n < 2:
        raise ValueError("Use an integer base n>=2")
    scale = 10**16
    radicand = n**3 * scale**4
    lower = isqrt(isqrt(radicand))
    if not lower**4 <= radicand < (lower+1)**4:
        raise ValueError("Integer fourth-root interval failed")
    a = Fraction(lower, scale)
    b = a if lower**4 == radicand else Fraction(lower+1, scale)
    low = sum((a**h.bit_count() for h in profiles), Fraction())
    high = sum((b**h.bit_count() for h in profiles), Fraction())
    return {"lower": [low.numerator, low.denominator], "upper": [high.numerator, high.denominator],
            "method": "Exact integer fourth-root interval for n^(3/4), then positive integer powers"}


def sample(data: dict, row: dict) -> dict:
    profiles, n = row["profiles"], row["n"]
    polys = position_polynomials(data, profiles)
    budget = value(polys["total_coefficients_in_n_minus_one"], n)
    interval = mass_interval(profiles, n)
    return {"n": n, "profiles": profiles, "all_n_position_polynomials": polys,
            "main_positions_at_n": value(polys["main_coefficients_in_n_minus_one"], n),
            "total_positions_at_n": budget, "target_mass_interval": interval,
            "budget_strictly_above_critical_mass": budget > Fraction(*interval["upper"]),
            "no_full_ambient_centered_target": all(h < (1 << data["coordinate_count"])-1 for h in profiles)}


def build_report() -> dict:
    sources = {name: read_source(name) for name in ("general10", "general13", "general22")}
    discovery = json.loads((HERE / "discovery/dimension_profiles.json").read_text())
    samples = [sample(sources["general22"], row) for row in discovery["runs"]]
    floors = [pruning_floor(p, d) for p, d in ((10, 6), (13, 6), (22, 6), (29, 9), (106, 12))]
    return {"source_acceptance": {name: {"sha256": data["source_sha256"], **verify_grades(data)}
                                   for name, data in sources.items()},
            "featured_22_product_construction": featured_construction(sources["general22"],
                                                                       json.loads((HERE / "witness.json").read_text())),
            "all_dimension_common_support_cost_floors": floors,
            "six_coordinate_product_count_boundary": {"p29_excluded": pruning_floor(29, 6),
                                                      "p30_not_excluded_by_this_test": pruning_floor(30, 6)},
            "restricted_profile_samples": samples, "independent_review": False, "improves_omega": False,
            "scope": "Exact graded source acceptance, all-n nonzero position polynomials, and written common-support budget barrier; no actual rank lower bound"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = build_report()
    path = HERE / "report.json"
    if args.write_report:
        path.write_text(json.dumps(report, indent=2) + "\n")
    elif json.loads(path.read_text()) != report:
        raise ValueError("Saved report differs from exact acceptance")
    print(json.dumps({"accepted": True, "sources": len(report["source_acceptance"]),
                      "profile_samples": len(report["restricted_profile_samples"]),
                      "cost_floors": len(report["all_dimension_common_support_cost_floors"])}, indent=2))


if __name__ == "__main__":
    main()
