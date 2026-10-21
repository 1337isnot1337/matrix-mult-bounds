"""Exact matrix blocks in the source fiber with both endpoints deleted.

This standard-library module exports and completely replays
A(a,a)|free -> M_(a-1) + M_(a-1) + M_(a-2), for a >= 3.
The source restriction is the one fixing both physical endpoint rows
and columns to zero.  No completion of the larger 27+7 target is claimed.
"""

import argparse
from collections import Counter
from copy import deepcopy
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPARSE = HERE / 'parity_structure_free_interior_sparse.json'


def original_column(a, leg, i, middle, s):
    long = 2 * a - 1
    return ((i * long + middle) * a + s,
            (s * a + i) * long + middle,
            (middle * a + s) * a + i)[leg]


def common_point(a, leg, column):
    long = 2 * a - 1
    if leg == 0:
        im, s = divmod(column, a)
        i, middle = divmod(im, long)
    elif leg == 1:
        si, middle = divmod(column, long)
        s, i = divmod(si, a)
    else:
        ms, i = divmod(column, a)
        middle, s = divmod(ms, a)
    return i, middle, s


def is_free(a, i, middle, s):
    last = a - 1
    return not ((i == last and middle <= last)
                or (i == 0 and middle >= last)
                or (s == 0 and middle >= last)
                or (s == last and middle <= last))


def source_terms(a):
    long = 2 * a - 1
    for i, j, p, q, r, s in product(range(a), repeat=6):
        yield ((i * long + p + q) * a + s,
               (j * a + p) * long + r + s,
               ((i + j) * a + q) * a + r)


def target_terms(blocks):
    expected, offset = {}, 0
    for size in blocks:
        for i, j, k in product(range(size), repeat=3):
            expected[offset + size * i + j,
                     offset + size * j + k,
                     offset + size * k + i] = 1
        offset += size * size
    return expected


def build(a=8):
    if not isinstance(a, int) or a < 3:
        raise ValueError('This family requires an integer a >= 3')
    blocks = [a - 1, a - 1, a - 2]
    maps = [[], [], []]
    row = 0
    for block, size in enumerate(blocks):
        for i, j in product(range(size), repeat=2):
            if block == 0:
                point = i, j, 0
            elif block == 1:
                point = a - 1 - i, 2 * a - 2 - j, a - 1
            else:
                # The transpose in the center block fixes the trace orientation.
                point = j + 1, a - 1, a - 2 - i
            for leg in range(3):
                maps[leg].append([row, original_column(a, leg, *point), 1])
            row += 1
    return {'format': 'exact-free-interior-matrix-blocks-v1',
            'source_lengths': [a, a], 'source_leg_dimension': a * a * (2 * a - 1),
            'free_source_dimension': 2 * (a - 1) ** 3 + (a - 2) ** 2,
            'physical_endpoint_states': [[a - 1, 0], [0, a - 1]],
            'target_blocks': blocks, 'target_leg_dimension': sum(n * n for n in blocks),
            'target_vertex_charges': [list(range(a - 1)),
                                      [-i for i in range(a - 1)],
                                      [-i for i in range(a - 2)]],
            'maps': maps, 'map_denominator': 1,
            'full_target_27_plus_7_witness': False, 'new_exponent_established': False}


def contract(witness):
    a, second = witness['source_lengths']
    if second != a or a < 3:
        raise ArithmeticError('Unexpected square source')
    dimension = a * a * (2 * a - 1)
    target_dimension = witness['target_leg_dimension']
    inverse = []
    for leg, entries in enumerate(witness['maps']):
        columns, rows = {}, set()
        for row, column, value in entries:
            if not (isinstance(row, int) and 0 <= row < target_dimension
                    and isinstance(column, int) and 0 <= column < dimension
                    and isinstance(value, int) and value != 0):
                raise ArithmeticError('Invalid integral map entry')
            if row in rows or column in columns:
                raise ArithmeticError('This witness requires distinct monomial rows and columns')
            if not is_free(a, *common_point(a, leg, column)):
                raise ArithmeticError('A map coefficient changes a physical endpoint boundary')
            rows.add(row)
            columns[column] = row, value
        if len(rows) != target_dimension:
            raise ArithmeticError('A target row is missing')
        inverse.append(columns)
    if len(inverse) != 3:
        raise ArithmeticError('Exactly three maps are required')
    actual = Counter()
    for point in source_terms(a):
        if all(point[leg] in inverse[leg] for leg in range(3)):
            terms = [inverse[leg][point[leg]] for leg in range(3)]
            actual[tuple(term[0] for term in terms)] += terms[0][1] * terms[1][1] * terms[2][1]
    return {point: value for point, value in actual.items() if value}


def verify(witness=None, check_tamper=True):
    witness = json.loads(SPARSE.read_text()) if witness is None else witness
    a = witness['source_lengths'][0]
    if witness['target_blocks'] != [a - 1, a - 1, a - 2]:
        raise ArithmeticError('Unexpected target blocks')
    expected = target_terms(witness['target_blocks'])
    if contract(witness) != expected:
        raise ArithmeticError('The complete interior tensor contraction failed')
    free_points = [point for point in product(range(a), range(2 * a - 1), range(a))
                   if is_free(a, *point)]
    categories = [0, 0, 0]
    for i, middle, s in free_points:
        if middle < a - 1:
            if i == a - 1 or s == a - 1:
                raise ArithmeticError('The low free cube was misidentified')
            categories[0] += 1
        elif middle > a - 1:
            if i == 0 or s == 0:
                raise ArithmeticError('The high free cube was misidentified')
            categories[2] += 1
        else:
            if not (0 < i < a - 1 and 0 < s < a - 1):
                raise ArithmeticError('The central free plane was misidentified')
            categories[1] += 1
    if categories != [(a - 1) ** 3, (a - 2) ** 2, (a - 1) ** 3]:
        raise ArithmeticError('The free source category counts disagree')
    row_charges = [i - j for charges in witness['target_vertex_charges']
                   for i in charges for j in charges]
    for leg, entries in enumerate(witness['maps']):
        for row, column, _ in entries:
            i, middle, s = common_point(a, leg, column)
            if row_charges[row] != i + s - middle:
                raise ArithmeticError('A map violates the common torus grading')
    tamper_rejected = None
    if check_tamper:
        tampered = deepcopy(witness)
        tampered['maps'][0][0][2] = 2
        tamper_rejected = contract(tampered) != expected
        if not tamper_rejected:
            raise ArithmeticError('A nonzero-to-nonzero map tamper was accepted')
    return {'source': f'A({a},{a}) with two physical endpoints deleted',
            'target_blocks': witness['target_blocks'],
            'source_terms_checked': a ** 6,
            'source_leg_dimension': a * a * (2 * a - 1),
            'physical_interior_dimension': a * a - 2,
            'free_source_dimension': len(free_points),
            'free_categories_low_center_high': categories,
            'target_leg_dimension': witness['target_leg_dimension'],
            'map_nonzeros': [len(entries) for entries in witness['maps']],
            'exact_target_terms': len(expected),
            'complete_contraction_passed': True,
            'all_mixed_block_coefficients_zero': True,
            'every_map_coordinate_is_free': True,
            'torus_grading_preserved': True,
            'nonzero_to_nonzero_tamper_rejected': tamper_rejected,
            'full_target_27_plus_7_witness': False, 'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--a', type=int, default=8)
    args = parser.parse_args()
    witness = build(args.a)
    report = verify(witness)
    if args.a == 8:
        SPARSE.write_text(json.dumps(witness, separators=(',', ':')) + '\n')
        (HERE / 'parity_structure_free_interior_certificate.json').write_text(
            json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
