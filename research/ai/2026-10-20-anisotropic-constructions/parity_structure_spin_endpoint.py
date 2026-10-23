"""Complete integer replay of a deformed M(3,3,27) core in A(8,8).

The actual exported Y map changes, while the first and Z maps are retained
from the spin construction after deleting channel27. The full response
vanishes at F(7,0,7) and remains supported on long indices0,1,2.
"""

from collections import Counter, defaultdict
import argparse
import hashlib
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
MAPS = DIRECTORY / "parity_structure_spin_endpoint_maps.json"
MINOR = DIRECTORY / "parity_structure_spin_endpoint_minor.json"
REPORT = DIRECTORY / "parity_structure_spin_endpoint_certificate.json"
PRIME = 65521


def coordinate(i, k, s):
    return (15*i+k)*8+s


def source_terms():
    for i, p, r, j, q, s in product(range(8), repeat=6):
        yield coordinate(i, p+q, s), coordinate(p, r+s, j), coordinate(r, i+j, q)


def parse_maps(data):
    if data.get("source") != [8, 8] or data.get("target") != [3, 3, 27]:
        raise ArithmeticError("Incorrect source or target format")
    maps, denominators = [], []
    for name, rows in zip("XYZ", (9, 81, 81)):
        item = data["maps"][name]
        if item.get("shape") != [rows, 960]:
            raise ArithmeticError("An actual map has an incorrect shape")
        denominator = item.get("denominator")
        if type(denominator) is not int or denominator <= 0:
            raise ArithmeticError("Invalid common denominator")
        seen, entries = set(), []
        for entry in item["entries"]:
            if not isinstance(entry, list) or len(entry) != 3 or any(type(v) is not int for v in entry):
                raise ArithmeticError("A sparse entry needs three integers")
            row, column, value = entry
            if not 0 <= row < rows or not 0 <= column < 960 or not value or (row, column) in seen:
                raise ArithmeticError("Invalid or repeated sparse coordinate")
            seen.add((row, column))
            entries.append((row, column, value))
        maps.append(entries)
        denominators.append(denominator)
    return maps, denominators


def inverse(entries):
    answer = defaultdict(list)
    for row, column, value in entries:
        answer[column].append((row, value))
    return answer


def full_response(y, z):
    yy, zz = inverse(y), inverse(z)
    values = defaultdict(Counter)
    count, contributions = 0, 0
    for x, cy, cz in source_terms():
        count += 1
        yvalues, zvalues = yy.get(cy, ()), zz.get(cz, ())
        for (ry, vy), (rz, vz) in product(yvalues, zvalues):
            values[x][81*ry+rz] += vy*vz
            contributions += 1
    answer = {x: {point: value for point, value in row.items() if value}
              for x, row in values.items()}
    return {x: row for x, row in answer.items() if row}, count, contributions


def determinant_mod(matrix, prime):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ArithmeticError("A square response minor is required")
    rows = [[value % prime for value in row] for row in matrix]
    determinant = 1
    for j in range(len(rows)):
        other = next((i for i in range(j, len(rows)) if rows[i][j]), None)
        if other is None:
            return 0
        if other != j:
            rows[j], rows[other] = rows[other], rows[j]
            determinant = -determinant
        pivot = rows[j][j]
        determinant = determinant*pivot % prime
        inverse_pivot = pow(pivot, -1, prime)
        for i in range(j+1, len(rows)):
            factor = rows[i][j]*inverse_pivot % prime
            if factor:
                rows[i] = [(a-factor*b) % prime for a, b in zip(rows[i], rows[j])]
    return determinant % prime


def verify(data, minor=None):
    maps, denominators = parse_maps(data)
    if any(column//120 > 1 for _, column, _ in maps[1]):
        raise ArithmeticError("The changed Y map escaped physical first indices0,1")
    if any(column % 8 > 1 for _, column, _ in maps[2]):
        raise ArithmeticError("The fixed Z map escaped physical last indices0,1")
    values, source_count, contributions = full_response(maps[1], maps[2])
    actual = Counter()
    for rx, column, vx in maps[0]:
        for yz, value in values.get(column, {}).items():
            ry, rz = divmod(yz, 81)
            actual[rx, ry, rz] += vx*value
    actual = {point: value for point, value in actual.items() if value}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(3*i+j, 27*j+a, 27*i+a): scale
                for i, j, a in product(range(3), range(3), range(27))}
    if actual != expected:
        errors = sum(actual.get(point, 0) != expected.get(point, 0)
                     for point in actual.keys() | expected.keys())
        raise ArithmeticError(f"The complete module identity has {errors} incorrect coefficients")
    allowed = {coordinate(i, k, s) for i in range(8) for k in range(3) for s in range(8)}
    endpoint = coordinate(7, 0, 7)
    if not set(values) <= allowed or endpoint in values:
        raise ArithmeticError("The full response does not obey the claimed support and endpoint cancellation")
    report = {"source": "A(8,8)", "target": "M(3,3,27)",
              "arithmetic": "complete Python-integer contraction of actual rational maps",
              "source_terms_checked": source_count, "all_target_coefficients_checked": 59049,
              "nonzero_target_coefficients": len(actual), "all_other_coefficients_zero": True,
              "map_denominators": denominators, "integer_coefficient_scale": scale,
              "sparse_map_entries": [len(m) for m in maps],
              "response_integer_contributions": contributions,
              "all_endpoint_response_coefficients_checked": 81*81,
              "vanishing_response_coordinate": [7, 0, 7],
              "actual_nonzero_response_rows": len(values),
              "full_response_rank_upper_bound": min(191, len(values)),
              "fixed_first_core_dimension": 9,
              "response_rank_needed_for_M27_plus_M7": 191,
              "passes_this_necessary_response_gate": True,
              "full_M27_plus_M7_constructed": False, "new_exponent_established": False,
              "external_independent_review": False}
    if minor is not None:
        if minor.get("prime") != PRIME or any(PRIME % d == 0 for d in range(2, 256)):
            raise ArithmeticError("Invalid response-minor prime")
        rows, columns = minor["source_columns"], minor["output_columns"]
        if len(rows) != len(columns) or len(set(rows)) != len(rows) or len(set(columns)) != len(columns):
            raise ArithmeticError("Malformed response-minor coordinates")
        if any(type(r) is not int or r not in allowed for r in rows) or any(type(c) is not int or not 0 <= c < 81*81 for c in columns):
            raise ArithmeticError("Out-of-range response-minor coordinates")
        determinant = determinant_mod([[values.get(r, {}).get(c, 0) for c in columns] for r in rows], PRIME)
        if not determinant:
            raise ArithmeticError("The regenerated response minor is singular")
        lower = len(rows)
        report.update({"response_lower_rank_prime": PRIME, "response_rank_lower_bound": lower,
                       "response_minor_integer_determinant_mod_prime": determinant})
        if lower == report["full_response_rank_upper_bound"]:
            report["full_response_rank_exact"] = lower
            report["full_response_kernel_dimension_exact"] = 960-lower
            report["fixed_core_first_preimage_dimension_exact"] = 960-lower+9
            if lower == 191:
                report["exact_kernel_coordinate_description"] = "all F(i,k,s) with k>=3, together with F(7,0,7)"
                report["exact_core_preimage_description"] = "the coordinate kernel plus the nine actual first-map images"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--without-minor", action="store_true")
    args = parser.parse_args()
    minor = None if args.without_minor else json.loads(MINOR.read_text())
    report = verify(json.loads(MAPS.read_text()), minor)
    report["maps_sha256"] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    if minor is not None:
        report["minor_sha256"] = hashlib.sha256(MINOR.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
