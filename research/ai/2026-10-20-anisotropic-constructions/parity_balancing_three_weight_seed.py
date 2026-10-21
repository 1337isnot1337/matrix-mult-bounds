"""Exact balanced three-weight change of basis of A(8,8) -> M12 direct_sum M3.

This is a positive control for cross-weight tensor cancellation, not a new
larger target.  It replays the complete integer source contraction without
NumPy and checks rank by an explicit inverse target change of basis.
"""

import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location('three_weight_source', HERE / 'parity_balancing_newton_pruning_audit.py')
CORE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORE)
OUTPUT = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_three_weight_seed.json'
SOURCE_DIMENSION = 960
TARGET_DIMENSION = 153
U = (0, 1, 6, 7)
V = (0, 2, 4)
CHARGES = tuple(u - v for u in U for v in V)
SMALL_CHARGES = (0, -1, -2)


def original_column(leg, common_column):
    i, k, s = CORE.coordinates(common_column)
    if leg == 0:
        return common_column
    if leg == 1:
        return (s * 8 + i) * 15 + k
    return (k * 8 + s) * 8 + i


def source_weight(leg, column):
    if leg == 0:
        i, k, s = CORE.coordinates(column)
    elif leg == 1:
        pair, k = divmod(column, 15)
        s, i = divmod(pair, 8)
    else:
        pair, i = divmod(column, 8)
        k, s = divmod(pair, 8)
    return i + s - k


def target_weights():
    return [i - j for charges in (CHARGES, SMALL_CHARGES) for i in charges for j in charges]


def base_rows():
    vertices = list(product(range(4), range(3)))
    rows = []
    for alpha, beta in vertices:
        for gamma, delta in vertices:
            rows.append({CORE.index(U[alpha], U[gamma] + V[beta], V[delta]): 1})
    rows.extend({CORE.index(7 - i, 14 - j, 7): 1} for i, j in product(range(3), repeat=2))
    if len(rows) != TARGET_DIMENSION or len({next(iter(row)) for row in rows}) != TARGET_DIMENSION:
        raise ArithmeticError('The base maps do not have distinct source coordinates')
    return rows


def nilpotent_pairs():
    by_charge = {charge: index for index, charge in enumerate(CHARGES)}
    pairs = []
    for pair_index, low in enumerate(range(-4, 8, 2)):
        lower, upper = by_charge[low], by_charge[low + 1]
        pairs.append((lower, upper) if pair_index < 3 else (upper, lower))
    if len({i for pair in pairs for i in pair}) != 12:
        raise ArithmeticError('The nilpotent pairs must be disjoint')
    return pairs


def conjugate_unit(row, sign=1):
    """Coefficients of (I+sign*N) E_row (I-sign*N)."""
    if row >= 144:
        return {row: 1}
    i, j = divmod(row, 12)
    pairs = nilpotent_pairs()
    left = [(i, 1)] + [(a, sign) for a, b in pairs if b == i]
    right = [(j, 1)] + [(b, -sign) for a, b in pairs if a == j]
    result = Counter()
    for (a, x), (b, y) in product(left, right):
        result[12 * a + b] += x * y
    return {r: c for r, c in result.items() if c}


def compose_rows(rows, sign):
    result = []
    for row in range(TARGET_DIMENSION):
        coefficients = Counter()
        for base_row, factor in conjugate_unit(row, sign).items():
            for column, value in rows[base_row].items():
                coefficients[column] += factor * value
        result.append({column: value for column, value in coefficients.items() if value})
    return result


def build():
    transformed = compose_rows(base_rows(), 1)
    maps = [[[row, original_column(leg, column), value]
             for row, entries in enumerate(transformed)
             for column, value in sorted(entries.items())] for leg in range(3)]
    return {'format': 'exact-balanced-three-weight-seed-v1',
            'source_lengths': [8, 8], 'source_dimensions': [960] * 3,
            'target_blocks': [12, 3], 'target_dimensions': [153] * 3,
            'source_order': ['X(i,k,s)', 'Y(s,i,k)', 'Z(k,s,i)'],
            'target_vertex_charges': [list(CHARGES), list(SMALL_CHARGES)],
            'nilpotent_vertex_entries': [[a, b, 1] for a, b in nilpotent_pairs()],
            'maps': maps,
            'construction': 'J_new(A)=J_base((I+N)A(I-N)); N^2=0; M3 unchanged',
            'basis_change_of_a_known_smaller_seed': True,
            'full_A88_to_M27_plus_M7_witness': False,
            'new_exponent_established': False}


def validate_maps(maps):
    if not isinstance(maps, list) or len(maps) != 3:
        raise ArithmeticError('Exactly three maps are required')
    rows_by_leg = []
    for entries in maps:
        rows = [dict() for _ in range(TARGET_DIMENSION)]
        for entry in entries:
            if not isinstance(entry, list) or len(entry) != 3:
                raise ArithmeticError('A sparse entry must have three fields')
            row, column, value = entry
            if not (type(row) is int and 0 <= row < TARGET_DIMENSION and
                    type(column) is int and 0 <= column < SOURCE_DIMENSION and
                    type(value) is int and value != 0):
                raise ArithmeticError('An actual sparse map entry is invalid')
            if column in rows[row]:
                raise ArithmeticError('A duplicate sparse map entry is invalid')
            rows[row][column] = value
        rows_by_leg.append(rows)
    return rows_by_leg


def contract(maps, terms=None):
    rows_by_leg = validate_maps(maps)
    inverse = []
    for leg, rows in enumerate(rows_by_leg):
        by_source = defaultdict(list)
        original_to_common = {original_column(leg, c): c for c in range(960)}
        for row, entries in enumerate(rows):
            for column, value in entries.items():
                by_source[original_to_common[column]].append((row, value))
        inverse.append(by_source)
    actual = Counter()
    for x, y, z in CORE.source() if terms is None else terms:
        if x not in inverse[0] or y not in inverse[1] or z not in inverse[2]:
            continue
        for (r, a), (s, b), (t, c) in product(inverse[0][x], inverse[1][y], inverse[2][z]):
            actual[r, s, t] += a * b * c
    return {point: value for point, value in actual.items() if value}


def expected_tensor():
    result = {}
    offset = 0
    for n in (12, 3):
        for i, j, k in product(range(n), repeat=3):
            result[offset + n * i + j, offset + n * j + k, offset + n * k + i] = 1
        offset += n * n
    return result


def verify(data=None):
    data = json.loads(OUTPUT.read_text()) if data is None else data
    if data.get('source_lengths') != [8, 8] or data.get('target_blocks') != [12, 3]:
        raise ArithmeticError('Unexpected source or target format')
    if data.get('source_dimensions') != [960] * 3 or data.get('target_dimensions') != [153] * 3:
        raise ArithmeticError('Unexpected source or target dimensions')
    if data.get('target_vertex_charges') != [list(CHARGES), list(SMALL_CHARGES)]:
        raise ArithmeticError('The advertised target charges do not match this control')
    if data.get('nilpotent_vertex_entries') != [[a, b, 1] for a, b in nilpotent_pairs()]:
        raise ArithmeticError('The advertised vertex change of basis is incorrect')
    rows_by_leg = validate_maps(data['maps'])
    terms = CORE.source()
    actual = contract(data['maps'], terms)
    expected = expected_tensor()
    if actual != expected:
        raise ArithmeticError('The complete source coefficient identity failed')
    ranks = []
    histograms, offsets = [], []
    row_weights = target_weights()
    for leg, rows in enumerate(rows_by_leg):
        inverse_columns = {original_column(leg, c): c for c in range(960)}
        common_rows = [{inverse_columns[c]: v for c, v in row.items()} for row in rows]
        if compose_rows(common_rows, -1) != base_rows():
            raise ArithmeticError('The explicit inverse change of basis failed')
        ranks.append(TARGET_DIMENSION)
        histogram = Counter()
        differences = set()
        for row, entries in enumerate(rows):
            weights = {source_weight(leg, column) for column in entries}
            histogram[len(weights)] += 1
            differences.update(weight - row_weights[row] for weight in weights)
        histograms.append(dict(sorted(histogram.items())))
        offsets.append(sorted(differences))
    if histograms != [{1: 45, 2: 72, 3: 36}] * 3:
        raise ArithmeticError('The actual three-weight image counts changed')
    if offsets != [[-2, -1, 0, 1, 2]] * 3:
        raise ArithmeticError('The actual source offsets are not balanced')
    graded_maps = [[[row, column, value] for row, column, value in entries
                    if source_weight(leg, column) == row_weights[row]]
                   for leg, entries in enumerate(data['maps'])]
    graded = contract(graded_maps, terms)
    difference = {point: graded.get(point, 0) - expected.get(point, 0)
                  for point in set(graded) | set(expected)
                  if graded.get(point, 0) != expected.get(point, 0)}
    encoded = json.dumps(data['maps'], separators=(',', ':')).encode()
    return {'format': 'balanced-three-weight-complete-replay-v1',
            'complete_source_terms_enumerated': len(terms),
            'actual_nonzero_tensor_coefficients': len(actual),
            'complete_M12_plus_M3_identity_passed': True,
            'actual_map_ranks_by_inverse_basis_change': ranks,
            'actual_map_nonzero_counts': [len(entries) for entries in data['maps']],
            'actual_source_weight_count_histograms': histograms,
            'actual_source_minus_target_weight_offsets': offsets,
            'actual_sparse_maps_sha256': hashlib.sha256(encoded).hexdigest(),
            'grade_preserving_parts_alone_reproduce_target': not difference,
            'graded_part_error_nonzero_coefficients': len(difference),
            'graded_part_error_squared_norm': sum(value * value for value in difference.values()),
            'graded_part_error_first_ten_coefficients': [list(point) + [difference[point]] for point in sorted(difference)[:10]],
            'basis_change_of_a_known_smaller_seed': True,
            'full_A88_to_M27_plus_M7_witness': False,
            'new_exponent_established': False,
            'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    report = verify(data)
    data['replay_report'] = report
    args.output.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({'output': str(args.output), **report}, indent=2))


if __name__ == '__main__':
    main()
