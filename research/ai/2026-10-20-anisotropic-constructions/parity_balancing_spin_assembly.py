"""Exact response preimages and added-row kernels of the saved spin core.

This separate replay contracts the actual exported maps with the original
source.  Rank lower bounds use two small finite-field minors; the matching
upper bounds use coordinate support and explicit integer kernel vectors.
No numerical dependency is imported by acceptance.
"""

import argparse
from collections import Counter, defaultdict
import hashlib
from itertools import product
import json
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'
FULL_MAPS = RESULTS / 'spin-module14-full-maps.json'
WITNESS = RESULTS / 'spin-module14-witness.json'
CERTIFICATE = RESULTS / 'parity_balancing_spin_assembly_certificate.json'
REPORT = RESULTS / 'parity_balancing_spin_assembly_report.json'
PRIME = 65521


def coordinate(i, k, s, a=8, b=8):
    return (i * (a + b - 1) + k) * b + s


def decode(column, a=8, b=8):
    ik, s = divmod(column, b)
    i, k = divmod(ik, a + b - 1)
    return i, k, s


def source(a, b):
    for i, p, r, j, q, s in product(range(a), range(a), range(a),
                                   range(b), range(b), range(b)):
        yield (coordinate(i, p + q, s, a, b),
               coordinate(p, r + s, j, a, b),
               coordinate(r, i + j, q, a, b))


def reduced_source():
    for i, p, q, s, a, j in product(range(2), range(2), range(2),
                                   range(2), range(4), range(8)):
        yield ((i * 3 + p + q) * 2 + s,
               (p * 5 + a + s) * 8 + j,
               (q * 4 + a) * 9 + i + j)


def parse(item, shape):
    if item.get('shape') != list(shape):
        raise ArithmeticError('Incorrect actual map shape')
    denominator = item.get('denominator')
    if type(denominator) is not int or denominator <= 0:
        raise ArithmeticError('A positive integer denominator is required')
    entries, seen = [], set()
    if not isinstance(item.get('entries'), list):
        raise ArithmeticError('Missing actual sparse map entries')
    for entry in item['entries']:
        if not isinstance(entry, list) or len(entry) != 3 or any(type(v) is not int for v in entry):
            raise ArithmeticError('Sparse entries must contain three integers')
        row, column, value = entry
        if not 0 <= row < shape[0] or not 0 <= column < shape[1] or not value:
            raise ArithmeticError('Invalid actual map coordinate')
        if (row, column) in seen:
            raise ArithmeticError('Duplicate actual map coordinate')
        seen.add((row, column))
        entries.append((row, column, value))
    return entries, denominator


def inverse(entries):
    result = defaultdict(list)
    for row, column, value in entries:
        result[column].append((row, value))
    return result


def expected(middle, scale):
    return {(3 * i + j, middle * j + alpha, middle * i + alpha): scale
            for i, j, alpha in product(range(3), range(3), range(middle))}


def full_contraction(terms, maps, denominators, middle):
    inverses = [inverse(matrix) for matrix in maps]
    actual, source_count = Counter(), 0
    for point in terms:
        source_count += 1
        if not all(point[leg] in inverses[leg] for leg in range(3)):
            continue
        for (x, vx), (y, vy), (z, vz) in product(*(inverses[leg][point[leg]] for leg in range(3))):
            actual[x, y, z] += vx * vy * vz
    actual = {point: value for point, value in actual.items() if value}
    if actual != expected(middle, prod(denominators)):
        raise ArithmeticError('Independent complete source contraction failed')
    return {'source_terms_checked': source_count,
            'target_coefficients_checked': 9 * (3 * middle) ** 2,
            'nonzero_target_coefficients': len(actual),
            'all_other_target_coefficients_zero': True}


def first_response(y_map, z_map, middle=28):
    """Pair two actual source coordinates; the original six indices are unique."""
    y_inverse, z_inverse = inverse(y_map), inverse(z_map)
    answer = defaultdict(Counter)
    contributing_pairs = 0
    for cy, y_values in y_inverse.items():
        p, ell, j = decode(cy)
        for cz, z_values in z_inverse.items():
            r, h, q = decode(cz)
            i, s = h - j, ell - r
            if not (0 <= i < 8 and 0 <= s < 8):
                continue
            contributing_pairs += 1
            x = coordinate(i, p + q, s)
            for (ty, vy), (tz, vz) in product(y_values, z_values):
                answer[x][3 * middle * ty + tz] += vy * vz
    cleaned = {x: {point: value for point, value in row.items() if value}
               for x, row in answer.items()}
    return {x: row for x, row in cleaned.items() if row}, contributing_pairs


def deleted_maps(maps, alpha=27):
    result = [maps[0], [], []]
    for leg in (1, 2):
        for row, column, value in maps[leg]:
            vertex, channel = divmod(row, 28)
            if channel != alpha:
                new_channel = channel - (channel > alpha)
                result[leg].append((27 * vertex + new_channel, column, value))
    return result


def added_row_response(maps, free_leg):
    fixed = [leg for leg in range(3) if leg != free_leg]
    inverses = [inverse(matrix) for matrix in maps]
    answer = defaultdict(Counter)
    source_count = 0
    for point in source(8, 8):
        source_count += 1
        first, second = (inverses[leg].get(point[leg], ()) for leg in fixed)
        for (a, va), (b, vb) in product(first, second):
            answer[point[free_leg]][81 * a + b] += va * vb
    cleaned = {x: {point: value for point, value in row.items() if value}
               for x, row in answer.items()}
    return {x: row for x, row in cleaned.items() if row}, source_count


def modular_rank(matrix, prime=PRIME):
    if not matrix:
        return 0
    rows = [[value % prime for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][column], -1, prime)
        rows[rank] = [(v * scale) % prime for v in rows[rank]]
        for r in range(rank + 1, len(rows)):
            if rows[r][column]:
                factor = rows[r][column]
                rows[r] = [(v - factor * w) % prime for v, w in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def distinct_indices(values, maximum):
    return (isinstance(values, list) and all(type(v) is int and 0 <= v < maximum for v in values)
            and len(values) == len(set(values)))


def check_minor(response, rows, columns, size, width):
    if (not distinct_indices(rows, 960) or not distinct_indices(columns, width)
            or len(rows) != size or len(columns) != size):
        raise ArithmeticError('Malformed exact rank minor')
    matrix = [[response.get(row, {}).get(column, 0) for column in columns] for row in rows]
    if modular_rank(matrix) != size:
        raise ArithmeticError('The stated response minor is singular')


def check_kernel(response, data, support, rank):
    if data.get('rank') != rank or data.get('response_support_coordinates') != sorted(support):
        raise ArithmeticError('Incorrect kernel support or rank certificate')
    if not set(response) <= support:
        raise ArithmeticError('Actual coefficients escape the claimed response support')
    check_minor(response, data['minor_rows'], data['minor_columns'], rank, 729)
    vectors = data['integer_kernel_vectors']
    if len(vectors) != len(support) - rank:
        raise ArithmeticError('Incorrect number of exact kernel vectors')
    dense_vectors = []
    for vector in vectors:
        if not isinstance(vector, list):
            raise ArithmeticError('Malformed kernel vector')
        entries = {}
        for entry in vector:
            if (not isinstance(entry, list) or len(entry) != 2
                    or any(type(v) is not int for v in entry)):
                raise ArithmeticError('Kernel entries must be integer pairs')
            column, value = entry
            if column not in support or not value or column in entries:
                raise ArithmeticError('Invalid kernel vector coordinate')
            entries[column] = value
        contraction = Counter()
        for column, value in entries.items():
            for output, coefficient in response.get(column, {}).items():
                contraction[output] += value * coefficient
        if any(contraction.values()):
            raise ArithmeticError('An exported kernel vector has a nonzero exact coefficient')
        dense_vectors.append([entries.get(column, 0) for column in sorted(support)])
    if modular_rank(dense_vectors) != len(vectors):
        raise ArithmeticError('The exact kernel vectors are dependent')
    return {'response_support_size': len(support), 'exact_rational_response_rank': rank,
            'zero_coordinate_basis_vectors': 960 - len(support),
            'additional_integral_basis_vectors': len(vectors),
            'exact_kernel_dimension': 960 - rank}


def verify(certificate=None, full_export=None, witness=None):
    certificate = json.loads(CERTIFICATE.read_text()) if certificate is None else certificate
    full_export = json.loads(FULL_MAPS.read_text()) if full_export is None else full_export
    witness = json.loads(WITNESS.read_text()) if witness is None else witness
    reduced = [parse(witness[name], shape) for name, shape in
               zip('XYZ', ((9, 12), (42, 80), (42, 72)))]
    reduced_report = full_contraction(reduced_source(), [m for m, d in reduced],
                                      [d for m, d in reduced], 14)
    restrictions = full_export.get('restrictions')
    if not isinstance(restrictions, list) or len(restrictions) != 2:
        raise ArithmeticError('Both actual full-source exports are required')
    full_reports = []
    for entry, a, middle in zip(restrictions, (4, 8), (14, 28)):
        if entry.get('source') != [a, 8] or entry.get('target') != [3, 3, middle]:
            raise ArithmeticError('Incorrect actual source or target format')
        parsed = [parse(entry['maps'][name], (rows, a * 8 * (a + 7)))
                  for name, rows in zip('XYZ', (9, 3 * middle, 3 * middle))]
        maps, denominators = [m for m, d in parsed], [d for m, d in parsed]
        full_reports.append(full_contraction(source(a, 8), maps, denominators, middle))
    response, pairs = first_response(maps[1], maps[2])
    support = {coordinate(i, k, s) for i, k, s in product(range(8), range(3), range(8))}
    if not set(response) <= support or len(support) != 192:
        raise ArithmeticError('The complete first response escapes the proved low-long-index support')
    if any(column not in support for row, column, value in maps[0]):
        raise ArithmeticError('The particular first preimages have changed support')
    # Rebuild the full target once more from the independently assembled response.
    contraction = Counter()
    for row, column, value in maps[0]:
        for output, coefficient in response.get(column, {}).items():
            y, z = divmod(output, 84)
            contraction[row, y, z] += value * coefficient
    if {p: v for p, v in contraction.items() if v} != expected(28, prod(denominators)):
        raise ArithmeticError('The independent response and complete contraction disagree')
    halves = certificate['disjoint_channel_minor_controls']
    if len(halves) != 2:
        raise ArithmeticError('Two disjoint retained channel sets are required')
    channel_sets = []
    for control in halves:
        channels = control['channels']
        if not distinct_indices(channels, 28):
            raise ArithmeticError('Invalid retained middle coordinates')
        channel_sets.append(set(channels))
        columns = control['columns']
        for column in columns:
            if (column // 84) % 28 not in channels or (column % 84) % 28 not in channels:
                raise ArithmeticError('A rank minor uses a deleted middle coordinate')
        check_minor(response, sorted(support), columns, 192, 84 ** 2)
    if channel_sets[0] & channel_sets[1]:
        raise ArithmeticError('The two rank controls are not disjoint')
    trimmed = deleted_maps(maps)
    trim_report = full_contraction(source(8, 8), trimmed, denominators, 27)
    y_response, y_count = added_row_response(trimmed, 1)
    z_response, z_count = added_row_response(trimmed, 2)
    y_support = {coordinate(p, ell, j) for p, ell, j in product(range(3), range(10), range(8))}
    z_support = {coordinate(r, h, q) for r, h, q in product(range(8), range(9), range(3))}
    y_result = check_kernel(y_response, certificate['new_Y_against_saved_X_Z'], y_support, 233)
    z_result = check_kernel(z_response, certificate['new_Z_against_saved_X_Y'], z_support, 213)
    return {'arithmetic': 'Python integers; exact rank minors modulo 65521',
            'independent_reduced_replay': reduced_report,
            'independent_full_source_replays': full_reports,
            'trimmed_middle_coordinate': 27, 'trimmed_complete_replay': trim_report,
            'first_response_source_coordinate_pairs': pairs,
            'first_response_exact_rank': 192, 'first_response_kernel_dimension': 768,
            'first_kernel_is_exactly_all_long_indices_at_least_three': True,
            'all_28_single_coordinate_deletions_keep_rank_192': True,
            'first_preimage_dimension_of_nine_target_matrices': 777,
            'first_preimages_are_saved_maps_plus_high_long_index_kernel': True,
            'added_Y_rows_with_saved_X_Z': y_result,
            'added_Z_rows_with_saved_X_Y': z_result,
            'source_terms_checked_for_each_added_row_system': [y_count, z_count],
            'candidate_target_blocks': [27, 6, 3],
            'candidate_target_common_leg_dimension': 774,
            'remaining_target_rows': {'X': 765, 'Y': 693, 'Z': 693},
            'saved_X_rows_required_for_added_Y_Z_kernel_claims': True,
            'full_square_assembly_constructed': False,
            'new_exponent_established': False,
            'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=REPORT)
    args = parser.parse_args()
    report = verify()
    report['actual_input_sha256'] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                                      for path in (WITNESS, FULL_MAPS, CERTIFICATE)}
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
