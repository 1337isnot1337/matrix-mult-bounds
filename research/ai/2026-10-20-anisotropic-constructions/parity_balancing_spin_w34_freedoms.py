"""Exact affine freedoms of the stored W34 spin core.

The retained maps, their complete source contraction, their response
minors, and every kernel vector are replayed with integer arithmetic.
This certificate gives explicit core-preserving map families; it does
not construct the larger square matrix target.
"""

from collections import Counter, defaultdict
import hashlib
from itertools import product
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import parity_balancing_spin_assembly as source


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'results/anisotropic-constructions-2026-10-20'
MAPS = DIRECTORY / 'parity_structure_spin_w34_full_maps.json'
CERTIFICATE = DIRECTORY / 'parity_balancing_spin_w34_freedoms_certificate.json'
REPORT = DIRECTORY / 'parity_balancing_spin_w34_freedoms_report.json'
PRIME = 1000000007


def minor(response, rows, columns, size, width):
    if (not source.distinct_indices(rows, 960)
            or not source.distinct_indices(columns, width)
            or len(rows) != size or len(columns) != size):
        raise ArithmeticError('Malformed response minor')
    matrix = [[response.get(row, {}).get(column, 0) for column in columns] for row in rows]
    if source.modular_rank(matrix, PRIME) != size:
        raise ArithmeticError('An actual response minor is singular')


def kernel(response, specification, width, expected_rank):
    support = specification['response_support_coordinates']
    if (not source.distinct_indices(support, 960) or support != sorted(response)
            or specification['rank'] != expected_rank
            or specification['minor_prime'] != PRIME):
        raise ArithmeticError('The actual response support or kernel rank differs')
    minor(response, specification['minor_rows'], specification['minor_columns'],
          expected_rank, width)
    vectors = specification['integer_kernel_vectors']
    if len(vectors) != len(support)-expected_rank:
        raise ArithmeticError('Wrong number of complementary kernel vectors')
    dense = []
    for vector in vectors:
        entries = {}
        for entry in vector:
            if (not isinstance(entry, list) or len(entry) != 2
                    or any(type(v) is not int for v in entry)):
                raise ArithmeticError('Kernel entries must be integer pairs')
            column, value = entry
            if column not in response or not value or column in entries:
                raise ArithmeticError('Invalid actual kernel coordinate')
            entries[column] = value
        total = Counter()
        for column, value in entries.items():
            for output, coefficient in response[column].items():
                total[output] += value*coefficient
        if any(total.values()):
            raise ArithmeticError('A saved kernel vector has a nonzero exact coefficient')
        dense.append([entries.get(column, 0) for column in support])
    if source.modular_rank(dense, PRIME) != len(vectors):
        raise ArithmeticError('Saved kernel vectors are dependent')
    return vectors


def common_Y_response(maps):
    """Use all84 third rows, before deleting the middle channel."""
    xx, zz = source.inverse(maps[0]), source.inverse(maps[2])
    low = {source.coordinate(p, ell, j)
           for p, ell, j in product(range(2), range(10), range(8))}
    answer = defaultdict(Counter)
    for x, y, z in source.source(8, 8):
        if y not in low:
            continue
        for (tx, vx), (tz, vz) in product(xx.get(x, ()), zz.get(z, ())):
            answer[y][84*tx+tz] += vx*vz
    return {y: {output: value for output, value in row.items() if value}
            for y, row in answer.items() if any(row.values())}


def verify(certificate=None, exported=None):
    certificate = json.loads(CERTIFICATE.read_text()) if certificate is None else certificate
    exported = json.loads(MAPS.read_text()) if exported is None else exported
    if certificate.get('new_exponent_established') is not False:
        raise ArithmeticError('This affine family is not a new exponent')
    if certificate.get('deleted_channel') != 0:
        raise ArithmeticError('The stated deleted channel changed')
    restrictions = exported.get('restrictions')
    if not isinstance(restrictions, list) or len(restrictions) != 2:
        raise ArithmeticError('Both exact source exports are required')
    replays = []
    for item, a, middle in zip(restrictions, (4, 8), (14, 28)):
        if item.get('source') != [a, 8] or item.get('target') != [3, 3, middle]:
            raise ArithmeticError('The source or target format changed')
        parsed = [source.parse(item['maps'][name], (rows, a*8*(a+7)))
                  for name, rows in zip('XYZ', (9, 3*middle, 3*middle))]
        maps, denominators = [m for m, d in parsed], [d for m, d in parsed]
        replays.append(source.full_contraction(source.source(a, 8), maps, denominators, middle))

    if (any(source.decode(column)[0] >= 2 for row, column, value in maps[1])
            or any(source.decode(column)[2] >= 2 for row, column, value in maps[2])):
        raise ArithmeticError('The saved second/third maps escape their two short-index values')

    low_first = {source.coordinate(i, k, s)
                 for i, k, s in product(range(8), range(3), range(8))}
    response, _ = source.first_response(maps[1], maps[2])
    if set(response) != low_first:
        raise ArithmeticError('The full first response support changed')
    record = certificate['first_response']
    if record['rank'] != 192 or record['minor_prime'] != PRIME:
        raise ArithmeticError('Invalid full response rank specification')
    minor(response, record['minor_rows'], record['minor_columns'], 192, 84**2)
    trim = source.deleted_maps(maps, 0)
    trimmed_response, _ = source.first_response(trim[1], trim[2], 27)
    if set(trimmed_response) != low_first:
        raise ArithmeticError('The retained first response support changed')
    record = certificate['deleted_first_response']
    if record['rank'] != 192 or record['minor_prime'] != PRIME:
        raise ArithmeticError('Invalid retained response rank specification')
    minor(trimmed_response, record['minor_rows'], record['minor_columns'], 192, 81**2)

    ranks = {}
    for leg, name, rank in ((1, 'Y', 224), (2, 'Z', 213)):
        actual, _ = source.added_row_response(trim, leg)
        vectors = kernel(actual, certificate['added_'+name], 729, rank)
        ranks[name] = {'exact_constraint_rank': rank, 'actual_support_size': len(actual),
                       'complete_kernel_dimension': 960-rank,
                       'noncoordinate_kernel_vectors': len(vectors)}
        if name == 'Z':
            low_Z = {source.coordinate(r, h, q)
                     for r, h, q in product(range(8), range(9), range(3))}
            if set(actual) != low_Z:
                raise ArithmeticError('The low third-leg domain changed')
            removed_Z = [[I, column, value] for I in range(3)
                         for row, column, value in maps[2] if row == 28*I]
            if any(column not in low_Z for row, column, value in removed_Z):
                raise ArithmeticError('An omitted third row escapes the stated low domain')
            removed_rows = [[next((value for row, cc, value in removed_Z
                                  if row == I and cc == column), 0)
                             for column in sorted(low_Z)] for I in range(3)]
            if source.modular_rank(removed_rows, PRIME) != 3:
                raise ArithmeticError('The three omitted third rows are dependent')
            for I in range(3):
                total = Counter()
                for row, column, value in removed_Z:
                    if row == I:
                        for output, coefficient in actual.get(column, {}).items():
                            total[output] += value*coefficient
                if any(total.values()):
                    raise ArithmeticError('An omitted third row violates a retained coefficient')

    common = common_Y_response(maps)
    common_vectors = kernel(common, certificate['common_low_Y_kernel'], 756, 152)
    if len(common) != 160 or len(common_vectors) != 8:
        raise ArithmeticError('The common low second-leg fiber changed')
    fiber_maps = [[row, column, value] for row, vector in enumerate(common_vectors)
                  for column, value in vector]
    endpoint_fiber, _ = source.first_response(fiber_maps, trim[2], 27)
    endpoint_cross, _ = source.first_response(fiber_maps, removed_Z, 1)
    endpoint_old_deleted, _ = source.first_response(trim[1], removed_Z, 1)
    endpoint_reports = []
    controls = certificate['endpoint_controls']
    if len(controls) != 2:
        raise ArithmeticError('Both endpoint controls are required')
    for item, k in zip(controls, (0, 2)):
        if item['coordinate'] != [7, k, 7]:
            raise ArithmeticError('The endpoint coordinates changed')
        x = source.coordinate(7, k, 7)
        if endpoint_cross.get(x) or endpoint_old_deleted.get(x):
            raise ArithmeticError('An endpoint acquires a deleted-channel cross coefficient')
        nonzero = sorted({output//81 for output in endpoint_fiber.get(x, {})})
        if nonzero != item['fiber_nonzero_rows'] or len(nonzero) != 4:
            raise ArithmeticError('The endpoint fiber is not supported on four rows')
        rows, columns = item['old_response_minor_rows'], item['old_response_minor_columns']
        if (not source.distinct_indices(rows, 81) or not source.distinct_indices(columns, 81)
                or len(rows) != 6 or len(columns) != 6):
            raise ArithmeticError('Malformed endpoint minor')
        small = [[trimmed_response[x].get(81*y+z, 0) for z in columns] for y in rows]
        if source.modular_rank(small, PRIME) != 6:
            raise ArithmeticError('The actual endpoint response has lost its rank-six minor')
        endpoint_reports.append({'coordinate': [7, k, 7], 'old_response_rank_at_least': 6,
                                 'adjustable_fiber_rank_at_most': 4,
                                 'deleted_channel_cross_matrices_zero': True})

    return {'source': 'A(8,8)', 'retained_target': 'M(3,3,27)',
            'deleted_original_middle_channel': 0, 'source_replays': replays,
            'first_response_rank_before_and_after_deletion': [192, 192],
            'first_preimage_of_nine_target_slices_dimension': 777,
            'added_row_kernels': ranks,
            'low_Z_kernel_is_exactly_three_omitted_Z_rows': True,
            'common_low_Y_fiber_dimension_against_all84_Z_rows': 8,
            'explicit_core_preserving_joint_family_parameters': 81*(8+3),
            'endpoint_controls': endpoint_reports,
            'larger_square_target_constructed': False, 'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    result['actual_maps_sha256'] = hashlib.sha256(MAPS.read_bytes()).hexdigest()
    result['certificate_sha256'] = hashlib.sha256(CERTIFICATE.read_bytes()).hexdigest()
    REPORT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
