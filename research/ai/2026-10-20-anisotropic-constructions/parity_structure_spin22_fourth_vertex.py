"""Exact replay of A(2d,2d) -> M(3,4,2d^2) and its channel sections.

The accepted verifier uses only the standard library.  It reads the actual
rational maps, checks every source coefficient, and regenerates all three
full-source response matrices before checking saved nonzero minors.
"""

from collections import Counter, defaultdict
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
PREFIX = "parity_structure_spin22_fourth_vertex"
WITNESS = DIRECTORY / (PREFIX + "_witness.json")
MAPS = DIRECTORY / (PREFIX + "_maps.json")
MINORS = DIRECTORY / (PREFIX + "_response_minors.json")
REPORT = DIRECTORY / (PREFIX + "_certificate.json")
PRIME = 65521


def coordinate(i, k, s, n):
    return (i*(2*n-1)+k)*n+s


def source_terms(n, tiny=False):
    for i, p, r, j, q, s in product(range(n), repeat=6):
        x = coordinate(i, p+q, s, n)
        y = coordinate(p, r+s, j, n)
        z = (q*2+r)*3+i+j if tiny else coordinate(r, i+j, q, n)
        yield x, y, z


def parse_maps(data):
    source, target = data.get("source"), data.get("target")
    if (not isinstance(source, list) or len(source) != 2 or source[0] != source[1]
            or type(source[0]) is not int or source[0] < 2):
        raise ArithmeticError("Invalid square convolution source")
    if (not isinstance(target, list) or len(target) != 3 or target[:2] != [3, 4]
            or type(target[2]) is not int or target[2] < 1):
        raise ArithmeticError("Invalid rectangular target")
    n, middle = source[0], target[2]
    size = n*n*(2*n-1)
    result, denominators = [], []
    for name, rows in zip("XYZ", (12, 4*middle, 3*middle)):
        item = data["maps"][name]
        if item.get("shape") != [rows, size]:
            raise ArithmeticError("Incorrect actual map shape")
        denominator = item.get("denominator")
        if type(denominator) is not int or denominator <= 0:
            raise ArithmeticError("A positive integer denominator is required")
        entries, seen = [], set()
        for entry in item["entries"]:
            if (not isinstance(entry, list) or len(entry) != 3
                    or any(type(v) is not int for v in entry)):
                raise ArithmeticError("A sparse map entry needs three integers")
            row, column, value = entry
            if (not 0 <= row < rows or not 0 <= column < size or not value
                    or (row, column) in seen):
                raise ArithmeticError("Invalid or duplicate sparse map entry")
            seen.add((row, column))
            entries.append(tuple(entry))
        result.append(entries)
        denominators.append(denominator)
    return result, denominators


def by_column(entries):
    answer = defaultdict(list)
    for row, column, value in entries:
        answer[column].append((row, value))
    return answer


def response_matrices(data, tiny=False):
    maps, denominators = parse_maps(data)
    n, middle = data["source"][0], data["target"][2]
    inverses = [by_column(entries) for entries in maps]
    dimensions = (12, 4*middle, 3*middle)
    responses = [defaultdict(Counter) for _ in range(3)]
    count = 0
    for columns in source_terms(n, tiny):
        count += 1
        values = [inverses[axis].get(columns[axis], ()) for axis in range(3)]
        for axis in range(3):
            other = [j for j in range(3) if j != axis]
            a, b = other
            if values[a] and values[b]:
                row = responses[axis][columns[axis]]
                for (ra, va), (rb, vb) in product(values[a], values[b]):
                    row[ra*dimensions[b]+rb] += va*vb
    clean = []
    for response in responses:
        rows = {c: {j: v for j, v in row.items() if v} for c, row in response.items()}
        clean.append({c: row for c, row in rows.items() if row})
    return clean, maps, denominators, count


def determinant_mod(matrix, prime=PRIME):
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ArithmeticError("A nonempty square minor is required")
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
        inverse = pow(pivot, -1, prime)
        for i in range(j+1, len(rows)):
            factor = rows[i][j]*inverse % prime
            if factor:
                for k in range(j+1, len(rows)):
                    rows[i][k] = (rows[i][k]-factor*rows[j][k]) % prime
                rows[i][j] = 0
    return determinant % prime


def make_minor(response):
    """Discovery helper; acceptance recomputes its entire square minor."""
    basis, selected_rows, selected_columns = {}, [], []
    for source in sorted(response):
        row = {c: v % PRIME for c, v in response[source].items() if v % PRIME}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inverse = pow(row[pivot], -1, PRIME)
                basis[pivot] = {c: value*inverse % PRIME for c, value in row.items()}
                selected_rows.append(source)
                selected_columns.append(pivot)
                break
            factor = row[pivot]
            for column, value in basis[pivot].items():
                new = (row.get(column, 0)-factor*value) % PRIME
                if new:
                    row[column] = new
                else:
                    row.pop(column, None)
    matrix = [[response[r].get(c, 0) for c in selected_columns] for r in selected_rows]
    return {"prime": PRIME, "source_columns": selected_rows,
            "output_columns": selected_columns,
            "determinant_mod_prime": determinant_mod(matrix)}


def check(data, minors=None, tiny=False):
    responses, maps, denominators, count = response_matrices(data, tiny)
    middle = data["target"][2]
    actual = Counter()
    for row, column, value in maps[0]:
        for yz, response in responses[0].get(column, {}).items():
            y, z = divmod(yz, 3*middle)
            actual[row, y, z] += value*response
    actual = {point: value for point, value in actual.items() if value}
    scale = denominators[0]*denominators[1]*denominators[2]
    expected = {(4*i+j, middle*j+a, middle*i+a): scale
                for i, j, a in product(range(3), range(4), range(middle))}
    if actual != expected:
        errors = sum(actual.get(p, 0) != expected.get(p, 0)
                     for p in actual.keys() | expected.keys())
        raise ArithmeticError(f"Complete rectangular identity has {errors} incorrect coefficients")
    n = data["source"][0]
    if not tiny and any((column//n) % (2*n-1) >= 3 for column in responses[0]):
        raise ArithmeticError("First response escaped the three claimed long layers")
    result = {"source": data["source"], "target": data["target"],
              "source_terms_checked": count,
              "all_target_coefficients_checked": 12*(4*middle)*(3*middle),
              "nonzero_target_coefficients": len(actual),
              "all_other_coefficients_zero": True,
              "map_denominators": denominators,
              "sparse_map_entries": [len(m) for m in maps],
              "response_support_sizes": [len(r) for r in responses]}
    if minors is not None:
        ranks, determinants = [], []
        dimensions = (12, 4*middle, 3*middle)
        if set(minors) != set("XYZ"):
            raise ArithmeticError("All three response minors are required")
        for axis, name in enumerate("XYZ"):
            response, minor = responses[axis], minors[name]
            rows, columns = minor["source_columns"], minor["output_columns"]
            other = [i for i in range(3) if i != axis]
            output_size = dimensions[other[0]]*dimensions[other[1]]
            if (minor.get("prime") != PRIME or len(rows) != len(columns)
                    or len(rows) != len(response) or len(set(rows)) != len(rows)
                    or len(set(columns)) != len(columns)
                    or any(type(r) is not int or r not in response for r in rows)
                    or any(type(c) is not int or not 0 <= c < output_size for c in columns)):
                raise ArithmeticError("Malformed full-support response minor")
            determinant = determinant_mod([[response[r].get(c, 0) for c in columns] for r in rows])
            if not determinant or determinant != minor.get("determinant_mod_prime"):
                raise ArithmeticError("The saved response minor failed exact replay")
            ranks.append(len(rows))
            determinants.append(determinant)
        size = n*n*(2*n-1)
        result.update({"full_response_ranks_exact": ranks,
                       "response_minor_determinants_mod_65521": determinants,
                       "exact_core_preimage_dimensions": [size-r+d for r, d in zip(ranks, dimensions)]})
    return result


def lift(witness, d, channels=None):
    tiny_maps, denominators = parse_maps(witness)
    if witness["source"] != [2, 2] or witness["target"] != [3, 4, 2] or type(d) is not int or d < 1:
        raise ArithmeticError("Invalid tiny witness or residue modulus")
    maximum, n = 2*d*d, 2*d
    channels = list(range(maximum)) if channels is None else list(channels)
    if (not channels or len(set(channels)) != len(channels)
            or any(type(c) is not int or not 0 <= c < maximum for c in channels)):
        raise ArithmeticError("Invalid same-channel section")
    channel_index = {c: i for i, c in enumerate(channels)}
    middle, entries = len(channels), [[], [], []]
    for row, column, value in tiny_maps[0]:
        ik, s = divmod(column, 2)
        i, k = divmod(ik, 3)
        entries[0].append([row, coordinate(d*i, k, d*s, n), value])
    for e, f in product(range(d), repeat=2):
        for axis in (1, 2):
            for row, column, value in tiny_maps[axis]:
                vertex, alpha = divmod(row, 2)
                channel = 2*(d*e+f)+alpha
                if channel not in channel_index:
                    continue
                if axis == 1:
                    pL, j = divmod(column, 2)
                    p, L = divmod(pL, 3)
                    source = coordinate(p, e+d*L, f+d*j, n)
                else:
                    qr, H = divmod(column, 3)
                    q, r = divmod(qr, 2)
                    source = coordinate(e+d*r, f+d*H, q, n)
                entries[axis].append([middle*vertex+channel_index[channel], source, value])
    return {"source": [n, n], "target": [3, 4, middle], "residue_modulus": d,
            "retained_channels": channels,
            "maps": {name: {"shape": [rows, n*n*(2*n-1)], "denominator": denominator,
                            "entries": sorted(values)}
                     for name, rows, denominator, values in
                     zip("XYZ", (12, 4*middle, 3*middle), denominators, entries)}}


def verify(witness=None, exported=None, minors=None):
    witness = json.loads(WITNESS.read_text()) if witness is None else witness
    exported = json.loads(MAPS.read_text()) if exported is None else exported
    minors = json.loads(MINORS.read_text()) if minors is None else minors
    if (witness.get("new_exponent_established") is not False
            or exported.get("new_exponent_established") is not False):
        raise ArithmeticError("The recorded mathematical scope changed")
    tiny = check(witness, tiny=True)
    reports = {}
    for middle in (32, 28):
        key = str(middle)
        generated = lift(witness, 4, range(middle))
        if generated != exported["targets"][key]:
            raise ArithmeticError("An exported map differs from the exact residue lift")
        reports[key] = check(exported["targets"][key], minors["targets"][key])
    return {"claim_id": "AI-SPIN-FOURTH-VERTEX-122", "tiny": tiny, "targets": reports,
            "general_family": "A(2d,2d) -> M(3,4,2d^2), for every integer d>=1",
            "field": "Q, hence C", "arithmetic": "Python integers and nonzero finite-field minors",
            "full_improving_target_constructed": False, "new_exponent_established": False,
            "external_independent_review": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    report = verify()
    for name, path in (("witness", WITNESS), ("maps", MAPS), ("response_minors", MINORS)):
        report[name+"_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
