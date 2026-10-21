"""Exact monomial A(8,8) -> M12 + M3 seed for the live torus target.

The standard-library replay checks all 8**6 source coefficients.  The
embedded 27+7 maps are an exact partial target, not the requested full
restriction.  NumPy is imported only for the optional --npz export.
"""

import argparse
from collections import Counter
from copy import deepcopy
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPARSE = HERE / 'parity_structure_torus_seed_sparse.json'
A = B = 8
LONG = 15
SOURCE_DIMENSION = 960
CORE_U = (0, 1, 6, 7)
CORE_V = (0, 2, 4)
PROFILE_27 = (1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1)
PROFILE_7 = (1, 1, 1, 1, 1, 1, 1)


def source_index(leg, point):
    i, j, k = point
    if leg == 0:
        return (i * LONG + j) * B + k
    if leg == 1:
        return (i * A + j) * LONG + k
    return (i * B + j) * A + k


def source_charge(leg, column):
    if leg == 0:
        first, last = divmod(column, B)
        first, middle = divmod(first, LONG)
        return first + last - middle
    if leg == 1:
        first, middle = divmod(column, LONG)
        first, second = divmod(first, A)
        return first + second - middle
    middle, last = divmod(column, A)
    middle, second = divmod(middle, B)
    return second + last - middle


def source_terms():
    for i, j, p, q, r, s in product(range(8), repeat=6):
        yield (source_index(0, (i, p + q, s)),
               source_index(1, (j, p, r + s)),
               source_index(2, (i + j, q, r)))


def target_terms(blocks, embeddings=None):
    result = {}
    offset = 0
    for block, size in enumerate(blocks):
        vertices = range(size) if embeddings is None else embeddings[block]
        for i, j, k in product(vertices, repeat=3):
            result[offset + i * size + j, offset + j * size + k,
                   offset + k * size + i] = 1
        offset += size * size
    return result


def vertex_charges(counts):
    return [charge for charge, count in enumerate(counts) for _ in range(count)]


def extreme_corner_maps():
    physical_points = ((0, 7, 7), (0, 14, 0), (7, 0, 7), (7, 7, 0))
    result = [[], [], []]
    for row, (i, middle, s) in enumerate(physical_points):
        for leg, point in enumerate(((i, middle, s), (s, i, middle), (middle, s, i))):
            result[leg].append([row, source_index(leg, point), 1])
    return result


def build():
    maps = [[], [], []]
    vertices = list(product(range(4), range(3)))
    for I, (alpha, beta) in enumerate(vertices):
        for J, (gamma, delta) in enumerate(vertices):
            # X(I,J), Y(I,J), and Z(I,J) all use their own target edge.
            points = ((CORE_U[alpha], CORE_U[gamma] + CORE_V[beta], CORE_V[delta]),
                      (CORE_V[delta], CORE_U[alpha], CORE_U[gamma] + CORE_V[beta]),
                      (CORE_U[gamma] + CORE_V[beta], CORE_V[delta], CORE_U[alpha]))
            for leg, point in enumerate(points):
                maps[leg].append([12 * I + J, source_index(leg, point), 1])
    for i, j in product(range(3), repeat=2):
        points = ((7 - i, 14 - j, 7), (7, 7 - i, 14 - j),
                  (14 - j, 7, 7 - i))
        for leg, point in enumerate(points):
            maps[leg].append([144 + 3 * i + j, source_index(leg, point), 1])
    seed_charges = [[CORE_U[alpha] - CORE_V[beta] for alpha, beta in vertices],
                    [0, -1, -2]]
    full_charges = [vertex_charges(PROFILE_27), vertex_charges(PROFILE_7)]
    embeddings = [[full_charges[0].index(charge + 5) for charge in seed_charges[0]],
                  [full_charges[1].index(charge + 2) for charge in seed_charges[1]]]
    embedded = [[], [], []]
    for leg, entries in enumerate(maps):
        for row, column, value in entries:
            block, local_row, small_size = (0, row, 12) if row < 144 else (1, row - 144, 3)
            i, j = divmod(local_row, small_size)
            large_size = (27, 7)[block]
            offset = (0, 729)[block]
            new_row = offset + large_size * embeddings[block][i] + embeddings[block][j]
            embedded[leg].append([new_row, column, value])
    return {'format': 'exact-monomial-torus-seed-v1', 'source_lengths': [8, 8],
            'source_dimensions': [960] * 3, 'seed_blocks': [12, 3],
            'seed_dimensions': [153] * 3, 'seed_vertex_charges': seed_charges,
            'maps': maps, 'full_target_blocks': [27, 7],
            'full_target_dimensions': [778] * 3,
            'full_target_vertex_charges': full_charges,
            'seed_vertex_embeddings': embeddings, 'embedded_maps': embedded,
            'extreme_corner_vertex_charges': [0, 14],
            'extreme_corner_maps': extreme_corner_maps(),
            'source_charge_convention': ['i+s-k', 'j+p-u', 'q+r-v'],
            'full_target_witness': False, 'new_exponent_established': False}


def contract(maps, target_dimension):
    inverse = []
    for entries in maps:
        by_source, rows = {}, set()
        for row, column, value in entries:
            if not (isinstance(row, int) and 0 <= row < target_dimension and
                    isinstance(column, int) and 0 <= column < SOURCE_DIMENSION and
                    isinstance(value, int) and value != 0):
                raise ArithmeticError('Invalid sparse map entry')
            if row in rows or column in by_source:
                raise ArithmeticError('This monomial witness requires distinct rows and columns')
            rows.add(row)
            by_source[column] = row, value
        inverse.append(by_source)
    actual = Counter()
    for point in source_terms():
        if not all(point[leg] in inverse[leg] for leg in range(3)):
            continue
        entries = [inverse[leg][point[leg]] for leg in range(3)]
        actual[tuple(entry[0] for entry in entries)] += entries[0][1] * entries[1][1] * entries[2][1]
    return {point: value for point, value in actual.items() if value}


def target_row_charges(block_charges):
    return [i - j for block in block_charges for i in block for j in block]


def verify(witness=None, check_tamper=True):
    witness = json.loads(SPARSE.read_text()) if witness is None else witness
    if witness['source_lengths'] != [8, 8] or witness['seed_blocks'] != [12, 3]:
        raise ArithmeticError('Unexpected source or seed target')
    actual = contract(witness['maps'], 153)
    expected = target_terms([12, 3])
    if actual != expected:
        raise ArithmeticError('The complete seed tensor contraction failed')
    embedded = contract(witness['embedded_maps'], 778)
    expected_embedded = target_terms([27, 7], witness['seed_vertex_embeddings'])
    if embedded != expected_embedded:
        raise ArithmeticError('The complete embedded partial tensor contraction failed')
    corner = contract(witness['extreme_corner_maps'], 4)
    if corner != target_terms([2]):
        raise ArithmeticError('The exact extreme-charge M2 control failed')
    corner_charges = target_row_charges([witness['extreme_corner_vertex_charges']])
    for leg, entries in enumerate(witness['extreme_corner_maps']):
        if any(corner_charges[row] != source_charge(leg, column) for row, column, _ in entries):
            raise ArithmeticError('An extreme-charge M2 map has the wrong charge')
    for map_name, charge_name in [('maps', 'seed_vertex_charges'),
                                  ('embedded_maps', 'full_target_vertex_charges')]:
        row_charges = target_row_charges(witness[charge_name])
        for leg, entries in enumerate(witness[map_name]):
            for row, column, _ in entries:
                if row_charges[row] != source_charge(leg, column):
                    raise ArithmeticError('A supplied map mixes distinct torus charges')
    source_counts = [Counter(source_charge(leg, column) for column in range(960))
                     for leg in range(3)]
    if source_counts[0] != source_counts[1] or source_counts[0] != source_counts[2]:
        raise ArithmeticError('The cyclic source charge counts disagree')
    target_counts = Counter(target_row_charges(witness['full_target_vertex_charges']))
    if sum(target_counts.values()) != 778:
        raise ArithmeticError('Wrong target charge count')
    if any(target_counts[charge] > source_counts[0][charge] for charge in target_counts):
        raise ArithmeticError('The full target fails a charge-space capacity inequality')
    tamper_rejected = None
    if check_tamper:
        tampered = deepcopy(witness['maps'])
        tampered[0][0][2] += 1
        tamper_rejected = contract(tampered, 153) != expected
        if not tamper_rejected:
            raise ArithmeticError('A nonzero-to-nonzero map tamper was accepted')
    return {'source': 'A(8,8)', 'exact_seed': 'M12 direct sum M3',
            'source_terms_checked': 8 ** 6, 'seed_target_terms': len(expected),
            'seed_leg_dimensions': [153] * 3,
            'seed_map_nonzeros': [len(entries) for entries in witness['maps']],
            'complete_seed_contraction_passed': True,
            'all_mixed_seed_coefficients_zero': True,
            'complete_embedded_partial_contraction_passed': True,
            'extreme_charge_M2_control_terms': len(corner),
            'source_counts_by_absolute_charge': [source_counts[0][w] for w in range(15)],
            'full_target_counts_by_absolute_charge': [target_counts[w] for w in range(15)],
            'full_target_charge_slack': [source_counts[0][w] - target_counts[w] for w in range(15)],
            'full_target_charge_profile_fits': True,
            'torus_map_parameters_all_three_legs':
                3 * sum(source_counts[0][w] * count for w, count in target_counts.items()),
            'full_target_terms': 27 ** 3 + 7 ** 3,
            'embedded_squared_relative_residual': [27 ** 3 + 7 ** 3 - len(expected), 27 ** 3 + 7 ** 3],
            'nonzero_to_nonzero_tamper_rejected': tamper_rejected,
            'full_target_witness': False, 'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--npz', action='store_true')
    args = parser.parse_args()
    witness = build()
    SPARSE.write_text(json.dumps(witness, separators=(',', ':')) + '\n')
    report = verify(witness)
    (HERE / 'parity_structure_torus_seed_certificate.json').write_text(json.dumps(report, indent=2) + '\n')
    if args.npz:
        import numpy as np
        for name, dimension in [('maps', 153), ('embedded_maps', 778)]:
            matrices = [np.zeros((dimension, 960), dtype=np.int8) for _ in range(3)]
            for matrix, entries in zip(matrices, witness[name]):
                for row, column, value in entries:
                    matrix[row, column] = value
            suffix = 'seed' if name == 'maps' else 'target27_7'
            np.savez_compressed(HERE / ('parity_structure_torus_' + suffix + '_maps.npz'),
                                A=matrices[0], B=matrices[1], C=matrices[2])
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
