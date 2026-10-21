"""Exact changed-core A(8,8) -> M(4,4,12) construction and full response.

The first eleven channels use one parity copy of the rational crossed
module.  One upper-corner channel changes the first map and has disjoint
mixed support.  Verification uses only the Python standard library.
"""

from collections import Counter, defaultdict
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/anisotropic-constructions-2026-10-20"
REDUCED = RESULTS / "crossed-module11-witness.json"
MAPS = RESULTS / "parity_structure_cross_module_corner_maps.json"
REPORT = RESULTS / "parity_structure_cross_module_corner_certificate.json"
PRIME = 65521


def coordinate(i, k, s):
    return (15*i+k)*8+s


def decode(column):
    temporary, s = divmod(column, 8)
    i, k = divmod(temporary, 15)
    return i, k, s


def source_terms():
    for i, p, r, j, q, s in product(range(8), repeat=6):
        yield (coordinate(i, p+q, s), coordinate(p, r+s, j),
               coordinate(r, i+j, q))


def construct(reduced):
    """Export actual maps, including the changed first map, in common F order."""
    dy, dz = reduced["Y"]["denominator"], reduced["Z"]["denominator"]
    if reduced["Y"]["shape"] != [22, 40] or reduced["Z"]["shape"] != [22, 36]:
        raise ArithmeticError("The construction requires the eleven-channel reduced maps")
    x, y, z = [], [], []
    for i, t, p, u in product(range(2), repeat=4):
        left, right = 2*i+t, 2*p+u
        x.append([4*left+right, coordinate(i, 2*p+t, 2*u), 1])
        x.append([4*left+right, coordinate(left, 14, right), 1])
    for row, column, value in reduced["Y"]["entries"]:
        u, alpha = divmod(row, 11)
        ell, j = divmod(column, 8)
        for p in range(2):
            y.append([12*(2*p+u)+alpha, coordinate(2*p, 2*ell, j), value])
    for row, column, value in reduced["Z"]["entries"]:
        i, alpha = divmod(row, 11)
        aa, h = divmod(column, 9)
        for t in range(2):
            z.append([4*alpha+2*i+t, coordinate(2*aa, h, t), value])
    for right in range(4):
        y.append([12*right+11, coordinate(7, 7+right, 7), dy])
    for left in range(4):
        z.append([44+left, coordinate(7, 7+left, 7), dz])
    return {
        "source": [8, 8], "target_shape": [4, 4, 12],
        "source_order": "common F(i,k,s): (15*i+k)*8+s on each leg",
        "maps": [{"shape": [rows, 960], "denominator": denominator,
                  "entries": sorted(entries)}
                 for rows, denominator, entries in zip((16, 48, 48), (1, dy, dz), (x, y, z))],
        "new_exponent_established": False,
    }


def parse_maps(data):
    if data.get("source") != [8, 8] or data.get("target_shape") != [4, 4, 12]:
        raise ArithmeticError("Incorrect source or target format")
    exports = data.get("maps")
    if not isinstance(exports, list) or len(exports) != 3:
        raise ArithmeticError("Three actual maps are required")
    maps, denominators = [], []
    for item, rows in zip(exports, (16, 48, 48)):
        if item.get("shape") != [rows, 960]:
            raise ArithmeticError("An actual map has the wrong shape")
        denominator = item.get("denominator")
        if type(denominator) is not int or denominator <= 0:
            raise ArithmeticError("Invalid common denominator")
        entries = item.get("entries")
        if not isinstance(entries, list):
            raise ArithmeticError("Missing actual sparse entries")
        seen, parsed = set(), []
        for entry in entries:
            if not isinstance(entry, list) or len(entry) != 3 or any(type(v) is not int for v in entry):
                raise ArithmeticError("A sparse map entry needs three integers")
            row, column, value = entry
            if not 0 <= row < rows or not 0 <= column < 960 or not value or (row, column) in seen:
                raise ArithmeticError("Invalid or repeated actual map coordinate")
            seen.add((row, column))
            parsed.append((row, column, value))
        maps.append(parsed)
        denominators.append(denominator)
    return maps, denominators


def inverse(entries):
    answer = defaultdict(list)
    for row, column, value in entries:
        answer[column].append((row, value))
    return answer


def response(y, z):
    """Contract the original source against the actual two non-first maps."""
    yy, zz = inverse(y), inverse(z)
    values = defaultdict(Counter)
    source_count, contributions = 0, 0
    for x, cy, cz in source_terms():
        source_count += 1
        if cy not in yy or cz not in zz:
            continue
        for (ry, vy), (rz, vz) in product(yy[cy], zz[cz]):
            values[x][48*ry+rz] += vy*vz
            contributions += 1
    cleaned = {x: {point: value for point, value in row.items() if value}
               for x, row in values.items()}
    return {x: row for x, row in cleaned.items() if row}, source_count, contributions


def modular_rank(rows, prime=PRIME):
    """Sparse exact elimination over the stated finite field."""
    basis = {}
    for row in rows:
        value = {j: v % prime for j, v in row.items() if v % prime}
        while value:
            pivot = min(value)
            if pivot not in basis:
                scale = pow(value[pivot], -1, prime)
                basis[pivot] = {j: v*scale % prime for j, v in value.items()}
                break
            factor = value[pivot]
            for j, v in basis[pivot].items():
                result = (value.get(j, 0)-factor*v) % prime
                if result:
                    value[j] = result
                else:
                    value.pop(j, None)
    return len(basis), sorted(basis)


def allowed_support():
    answer = {coordinate(i, k, s) for i in range(8) for k in range(4) for s in range(0, 8, 2)}
    answer.update(coordinate(i, k, 1) for i in range(8) for k in (7, 9))
    answer.update(coordinate(i, k, s) for i in range(2) for k in (7, 8) for s in range(1, 8))
    answer.update(coordinate(i, 14, s) for i in range(4) for s in range(4))
    return answer


def first_core_flattening(x):
    """Exact rank from equal or disjoint nonzero rows of the actual flattening."""
    xx = inverse(x)
    rows = defaultdict(Counter)
    contributions = 0
    for cx, cy, cz in source_terms():
        for target_x, value in xx.get(cx, ()):
            left, right = divmod(target_x, 4)
            rows[960*left+cy][960*right+cz] += value
            contributions += 1
    patterns = set()
    for row in rows.values():
        nonzero = {j: value for j, value in row.items() if value}
        if any(value != 1 for value in nonzero.values()):
            raise ArithmeticError("A first-core flattening row is not an indicator vector")
        if nonzero:
            patterns.add(tuple(sorted(nonzero)))
    seen = set()
    for support in patterns:
        if seen.intersection(support):
            raise ArithmeticError("Distinct first-core row patterns do not have disjoint supports")
        seen.update(support)
    if len(patterns) != 481:
        raise ArithmeticError("The changed first-core flattening rank is not 481")
    return {"flattening_groups": "(I, source Y) versus (J, source Z)",
            "all_original_source_terms_checked": 8**6,
            "integer_nonzero_contributions": contributions,
            "nonzero_rows": len(rows), "distinct_nonzero_indicator_rows": len(patterns),
            "distinct_row_supports_pairwise_disjoint": True,
            "exact_rational_rank": len(patterns),
            "target_M4_4_r_rank": "16*r", "resulting_middle_dimension_upper_bound": 30,
            "rank_needed_for_middle_dimension_27": 432,
            "passes_this_necessary_fixed_first_core_gate": True}


def verify(data, check_response_rank=True):
    maps, denominators = parse_maps(data)
    values, source_count, contributions = response(maps[1], maps[2])
    actual = Counter()
    for rx, column, vx in maps[0]:
        for yz, value in values.get(column, {}).items():
            ry, rz = divmod(yz, 48)
            actual[rx, ry, rz] += vx*value
    actual = {point: value for point, value in actual.items() if value}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(4*left+right, 12*right+alpha, 4*alpha+left): scale
                for left, right, alpha in product(range(4), range(4), range(12))}
    if actual != expected:
        errors = sum(actual.get(point, 0) != expected.get(point, 0)
                     for point in actual.keys() | expected.keys())
        raise ArithmeticError(f"The complete original-source identity has {errors} incorrect coefficients")
    support = allowed_support()
    if len(support) != 186 or not set(values) <= support:
        raise ArithmeticError("The actual response has support outside the proved 186-coordinate space")
    report = {
        "arithmetic": "Python integers; optional rank lower bound by exact finite-field elimination",
        "source": "A(8,8)", "target": "M(4,4,12)",
        "source_terms_checked": source_count,
        "all_target_coefficients_checked": 16*48*48,
        "nonzero_target_coefficients": len(actual), "all_other_coefficients_zero": True,
        "denominator_product": scale, "sparse_map_entries": [len(m) for m in maps],
        "response_integer_contributions": contributions,
        "proved_response_support_size": len(support), "actual_response_support_size": len(values),
        "response_support_counts_by_middle_coordinate": {
            str(k): sum(decode(c)[1] == k for c in values) for k in range(15)
            if any(decode(c)[1] == k for c in values)},
        "full_response_rank_upper_bound": len(values),
        "required_response_rank_upper_bound_for_fixed_core_in_M27_plus_M7": 198,
        "passes_this_necessary_response_gate": len(values) <= 198,
        "changed_first_core_flattening": first_core_flattening(maps[0]),
        "full_M27_plus_M7_constructed": False, "new_exponent_established": False,
        "external_independent_review": False,
    }
    if check_response_rank:
        rank, pivots = modular_rank(values[c] for c in sorted(values))
        report.update({"response_rank_lower_bound_prime": PRIME,
                       "full_response_rank_lower_bound": rank,
                       "response_pivot_columns": pivots})
        if rank == len(values):
            report["full_response_rank_exact"] = rank
            report["full_response_kernel_dimension_exact"] = 960-rank
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate", action="store_true")
    args = parser.parse_args()
    if args.generate:
        data = construct(json.loads(REDUCED.read_text()))
        MAPS.write_text(json.dumps(data, separators=(",", ":"))+"\n")
    else:
        data = json.loads(MAPS.read_text())
    report = verify(data)
    report["maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({k: v for k, v in report.items() if k != "response_pivot_columns"}, indent=2))


if __name__ == "__main__":
    main()
