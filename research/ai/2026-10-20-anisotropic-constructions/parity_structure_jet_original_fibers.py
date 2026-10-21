"""Exact original-source fibers in a Laurent chart, with a checked slice cover.

The maps use a full basis of the 960-dimensional original source. Their
limit is a constructive control with slice rank at most 126, so it cannot
produce the proposed matrix target. All arithmetic below is standard-library
integer or rational arithmetic; finite-field ranks certify lower bounds.
"""

import argparse
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPARSE = HERE / "parity_structure_jet_original_fibers_sparse.json"
SYSTEM = HERE / "parity_structure_jet_original_fibers_system.json"
CONSTANT = HERE / "parity_structure_jet_original_fibers_constant.json"
REPORT = HERE / "parity_structure_jet_original_fibers_certificate.json"
_SPEC = importlib.util.spec_from_file_location(
    "_original_jet_fibers_extension", HERE / "parity_structure_jet_extension.py")
_EXTENSION = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_EXTENSION)
SOURCE = _EXTENSION._HELPERS


def balanced_core():
    data = _EXTENSION.build(8)
    return [[[r, c, p + (-2 if leg < 2 else 4), v] for r, c, p, v in entries]
            for leg, entries in enumerate(data["maps"])]


def negative_system():
    """All one-new-row equations for a new t*q supported outside the old core."""
    core = balanced_core()
    selected = [{term[1] for term in entries} for entries in core]
    inverses = []
    for entries in core:
        columns = defaultdict(list)
        for row, column, power, value in entries:
            if power in (-2, 0):
                columns[column].append((row, power, value))
        inverses.append(columns)
    equations = [defaultdict(Counter) for _ in range(3)]
    for point in SOURCE.source_terms(8):
        for axis in range(3):
            if point[axis] in selected[axis]:
                continue
            other = [i for i in range(3) if i != axis]
            for r0, p0, v0 in inverses[other[0]].get(point[other[0]], ()):
                for r1, p1, v1 in inverses[other[1]].get(point[other[1]], ()):
                    if p0 + p1 < -1:
                        equations[axis][p0 + p1, r0, r1][point[axis]] += v0 * v1
    encoded = []
    for axis_equations in equations:
        rows = []
        for (power, row0, row1), coefficients in axis_equations.items():
            nonzero = [[c, v] for c, v in sorted(coefficients.items()) if v]
            if nonzero:
                rows.append({"other_leg_power_sum": power,
                             "other_target_rows": [row0, row1],
                             "coefficients": nonzero})
        encoded.append(rows)
    return {"source_lengths": [8, 8], "new_row_initial_power": 1,
            "old_target_dimensions": [134, 134, 134],
            "selected_old_source_columns": [sorted(s) for s in selected],
            "equations": encoded}


def rational_pivots(equations):
    """Sparse echelon rows; the exact pivot count is the rational rank."""
    pivots = {}
    for equation in sorted(equations, key=lambda e: len(e["coefficients"])):
        row = {c: Fraction(v) for c, v in equation["coefficients"]}
        while row:
            pivot = min(row)
            value = row[pivot]
            if pivot not in pivots:
                pivots[pivot] = {c: v / value for c, v in row.items()}
                break
            for column, coefficient in pivots[pivot].items():
                reduced = row.get(column, 0) - value * coefficient
                if reduced:
                    row[column] = reduced
                elif column in row:
                    del row[column]
    return pivots


def modular_row_basis(rows, modulus=1009):
    """A reproducible nonzero-minor lower bound, keeping earlier rows first."""
    if modulus != 1009:
        raise ValueError("The maintained finite-field certificate uses prime 1009")
    pivots, kept = {}, []
    for index, original in enumerate(rows):
        row = {column: value % modulus for column, value in original.items()
               if value % modulus}
        while row:
            pivot = min(row)
            value = row[pivot]
            if pivot not in pivots:
                inverse = pow(value, -1, modulus)
                pivots[pivot] = {c: v * inverse % modulus for c, v in row.items()}
                kept.append(index)
                break
            for column, coefficient in pivots[pivot].items():
                reduced = (row.get(column, 0) - value * coefficient) % modulus
                if reduced:
                    row[column] = reduced
                elif column in row:
                    del row[column]
    return kept


def nonpositive_contraction(maps):
    """Inspect all original source terms; collect every possibly nonpositive power."""
    inverses = []
    for entries in maps:
        columns = defaultdict(list)
        occupied = set()
        for term in entries:
            if len(term) != 4 or any(type(x) is not int for x in term):
                raise ValueError("Each Laurent map entry requires four integers")
            row, column, power, value = term
            if not (0 <= row < 960 and 0 <= column < 960 and value):
                raise ValueError("Invalid full-source Laurent entry")
            if (row, column, power) in occupied:
                raise ValueError("Repeated Laurent coefficient")
            occupied.add((row, column, power))
            columns[column].append((row, power, value))
        inverses.append(columns)
    coefficients, contributions = Counter(), Counter()
    examined = considered = 0
    for point in SOURCE.source_terms(8):
        examined += 1
        choices = [inverses[axis].get(point[axis], ()) for axis in range(3)]
        if any(not entries for entries in choices):
            continue
        if sum(min(term[1] for term in entries) for entries in choices) > 0:
            continue
        considered += 1
        for x, y, z in product(*choices):
            power = x[1] + y[1] + z[1]
            if power <= 0:
                coefficients[power, x[0], y[0], z[0]] += x[2] * y[2] * z[2]
                contributions[power] += 1
    return ({key: value for key, value in coefficients.items() if value},
            {"source_terms_examined": examined,
             "source_terms_meeting_nonpositive_lower_bound": considered,
             "individual_contributions_by_nonpositive_power": {
                 str(k): v for k, v in sorted(contributions.items())}})


def flattening_rows(constant, dimensions, axis):
    rows = [{} for _ in range(dimensions[axis])]
    other = [i for i in range(3) if i != axis]
    for point, value in constant.items():
        rows[point[axis]][tuple(point[i] for i in other)] = value
    return rows


def verify(data=None, check_tamper=True):
    data = json.loads(SPARSE.read_text()) if data is None else data
    if (data["source_lengths"] != [8, 8] or data["target_dimensions"] != [960] * 3
            or data["map_denominators"] != [1, 1, 2]
            or data["kernel_extension_dimensions"] != [362, 362, 363]):
        raise ValueError("Unexpected source, target, or coefficient convention")
    system = negative_system()
    if system != json.loads(SYSTEM.read_text()):
        raise ArithmeticError("The saved cancellation matrix differs from the full source replay")
    core = balanced_core()
    exact_ranks, nullities, map_ranks, powers = [], [], [], []
    for axis, entries in enumerate(data["maps"]):
        by_row = defaultdict(dict)
        row_powers = {}
        for row, column, power, value in entries:
            if column in by_row[row]:
                raise ValueError("A row/source coefficient is repeated")
            by_row[row][column] = value
            if row in row_powers and row_powers[row] != power:
                raise ValueError("The chart must use one Laurent power per target row")
            row_powers[row] = power
        if set(by_row) != set(range(960)):
            raise ValueError("The full source basis has a missing row")
        if sorted(term for term in entries if term[0] < 134) != sorted(core[axis]):
            raise ArithmeticError("The prescribed balanced matrix core was altered")
        pivots = rational_pivots(system["equations"][axis])
        rank = len(pivots)
        endpoint = data["kernel_extension_dimensions"][axis]
        exact_ranks.append(rank)
        nullities.append(endpoint - 134)
        if rank + endpoint - 134 != 826:
            raise ArithmeticError("The stored kernel size is not the complete nullity")
        old_columns = set(system["selected_old_source_columns"][axis])
        drops = {int(row): value for row, value in data["additional_row_drops"][axis].items()}
        for row in range(134, endpoint):
            vector = by_row[row]
            if old_columns.intersection(vector) or row_powers[row] != 1 - drops.get(row, 0):
                raise ArithmeticError("A new row leaves its declared source complement or valuation")
            for equation in system["equations"][axis]:
                if sum(value * vector.get(column, 0)
                       for column, value in equation["coefficients"]):
                    raise ArithmeticError("A new source direction fails an exact negative-power equation")
        for row, column in enumerate(sorted(pivots), endpoint):
            if by_row[row] != {column: 2 if axis == 2 else 1} or row_powers[row] != 4:
                raise ArithmeticError("The high-power source basis complement was altered")
        independent = modular_row_basis([by_row[row] for row in range(960)])
        if len(independent) != 960:
            raise ArithmeticError("The three full-source coefficient matrices must be invertible")
        map_ranks.append(len(independent))
        powers.append(row_powers)
    polynomial, metadata = nonpositive_contraction(data["maps"])
    if any(key[0] < 0 for key in polynomial):
        raise ArithmeticError("A negative-power coefficient survives")
    constant = {key[1:]: value for key, value in polynomial.items()}
    expected_entries = json.loads(CONSTANT.read_text())
    expected = {tuple(term[:3]): term[3] for term in expected_entries}
    if len(expected) != len(expected_entries) or any(not v for v in expected.values()):
        raise ValueError("The saved constant tensor has duplicates or zero coefficients")
    if constant != expected:
        raise ArithmeticError("The entire constant tensor differs from the saved integer certificate")
    kept = [modular_row_basis(flattening_rows(constant, [960] * 3, axis)) for axis in range(3)]
    projected_dimensions = list(map(len, kept))
    # These row selections also give explicit maps to a concise smaller-format limit.
    lookups = [{old: new for new, old in enumerate(indices)} for indices in kept]
    projected = {tuple(lookups[axis][point[axis]] for axis in range(3)): value
                 for point, value in constant.items()
                 if all(point[axis] in lookups[axis] for axis in range(3))}
    projected_ranks = [len(modular_row_basis(flattening_rows(projected, projected_dimensions, axis)))
                       for axis in range(3)]
    if projected_ranks != projected_dimensions:
        raise ArithmeticError("The displayed concise limit loses rank after coordinate projection")
    cover = [[row for row in range(960) if powers[axis][row] in (-2, 0)] for axis in range(3)]
    covers = list(map(set, cover))
    if any(not any(point[axis] in covers[axis] for axis in range(3)) for point in constant):
        raise ArithmeticError("The claimed slice cover misses a nonzero coefficient")
    tamper_rejected = None
    if check_tamper:
        altered = deepcopy(data["maps"])
        index = next(i for i, term in enumerate(altered[0]) if term[0] == 134)
        altered[0][index][3] *= 2
        tampered, _ = nonpositive_contraction(altered)
        tamper_rejected = tampered != polynomial
        if not tamper_rejected:
            raise ArithmeticError("A nonzero original-fiber coefficient tamper was accepted")
    return {
        "source": "A(8,8)", "full_map_dimensions": [960, 960, 960],
        "old_matrix_core_dimensions": [134, 134, 134],
        "exact_negative_system_rows": list(map(len, system["equations"])),
        "exact_negative_system_ranks": exact_ranks,
        "new_original_source_kernel_dimensions": nullities,
        "full_coefficient_map_ranks_mod1009": map_ranks,
        "row_power_multiplicities": [{str(k): v for k, v in sorted(Counter(p.values()).items())} for p in powers],
        "map_nonzero_monomials": list(map(len, data["maps"])),
        **metadata,
        "all_negative_powers_cancel_exactly": True,
        "constant_nonzero_coefficients": len(constant),
        "constant_coefficient_denominator": 2,
        "full_limit_flattening_rank_lower_bounds_mod1009": projected_dimensions,
        "concise_coordinate_projection_dimensions": projected_dimensions,
        "concise_projection_flattening_ranks_mod1009": projected_ranks,
        "concise_projection_retained_rows": kept,
        "explicit_slice_cover_rows": cover,
        "slice_cover_sizes_per_leg": list(map(len, cover)),
        "slice_rank_upper_bound": sum(map(len, cover)),
        "constant_tensor_sha256": hashlib.sha256(CONSTANT.read_bytes()).hexdigest(),
        "nonzero_to_nonzero_original_fiber_tamper_rejected": tamper_rejected,
        "standard_library_only": True,
        "this_limit_excludes_M27_by_slice_rank": True,
        "full_target_27_plus_7_witness": False,
        "new_exponent_established": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = verify()
    if args.write_report:
        REPORT.write_text(json.dumps(report, indent=2) + "\n")
    # Large exact row inventories are in the certificate rather than terminal output.
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ("concise_projection_retained_rows", "explicit_slice_cover_rows")}, indent=2))
