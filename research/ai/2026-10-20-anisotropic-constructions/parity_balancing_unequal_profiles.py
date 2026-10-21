"""Exact unequal vertex-charge profiles and a partial M12 + M3 seed.

All three target vertex lists are explicit.  These historical profiles are
excluded for full ordinary homogeneous maps by the separate Newton-pruning
proof, even when the earlier elementary screens pass.  The exact partial
source-map identity is replayed over all 8**6 source terms.
Only the optional --npz export imports NumPy.
"""

import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DEFAULT = ROOT / 'results/anisotropic-constructions-2026-10-20/parity_balancing_unequal_profiles.json'
PROFILES = (
    (1, 1, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 0),
    (1, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 0),
    (1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 1, 2, 2, 0),
)
SEED_U = (0, 1, 6, 7)
SEED_V = (0, 2, 4)


def expand(profile):
    return [charge for charge, count in enumerate(profile) for _ in range(count)]


def source_index(leg, i, k, s):
    """Original source column for common W-coordinate F(i,k,s)."""
    return ((i * 15 + k) * 8 + s,
            (s * 8 + i) * 15 + k,
            (k * 8 + s) * 8 + i)[leg]


def source_charge(leg, column):
    if leg == 0:
        i, rem = divmod(column, 120)
        k, s = divmod(rem, 8)
    elif leg == 1:
        rem, k = divmod(column, 15)
        s, i = divmod(rem, 8)
    else:
        rem, i = divmod(column, 8)
        k, s = divmod(rem, 8)
    return i + s - k


def source_terms():
    for i, p, r, j, q, s in product(range(8), repeat=6):
        yield (source_index(0, i, p + q, s),
               source_index(1, p, r + s, j),
               source_index(2, r, i + j, q))


def target_row_charges(vertex_charges, leg):
    left, right = vertex_charges[leg], vertex_charges[(leg + 1) % 3]
    return [x - y for block in range(2)
            for x in left[block] for y in right[block]]


def profile_screens(profiles, small_profiles):
    if len(profiles) != 3 or len(small_profiles) != 3:
        raise ValueError('Exactly three vertex profiles per matrix block are required')
    for profile, size in [(p, 27) for p in profiles] + [(p, 7) for p in small_profiles]:
        if len(profile) != 15 or any(type(x) is not int or x < 0 for x in profile):
            raise ValueError('Profiles require fifteen nonnegative integer multiplicities')
        if sum(profile) != size:
            raise ValueError('A vertex profile has the wrong dimension')
    charges = [[expand(profiles[i]), expand(small_profiles[i])] for i in range(3)]
    source_counts = Counter(source_charge(0, column) for column in range(960))
    target_counts = [Counter(target_row_charges(charges, leg)) for leg in range(3)]
    capacity_failures = []
    for leg, counts in enumerate(target_counts):
        for weight, count in counts.items():
            if count > source_counts[weight]:
                capacity_failures.append([leg, weight, count, source_counts[weight]])
    # For the uniform seven-vertex block, T_000 has target rank-one slices.
    # The separately proved source T_000 minimum slice rank is eight.
    uniform_small = all(p == [1] * 7 + [0] * 8 for p in small_profiles)
    zeros = [counts[0] for counts in target_counts]
    zero_failures = [[leg, zeros[(leg + 1) % 3] + zeros[(leg + 2) % 3], 121]
                     for leg in range(3)
                     if uniform_small and zeros[(leg + 1) % 3] + zeros[(leg + 2) % 3] > 121]
    # The determinant of the full degree -13/+13 source pair grid is a**3.
    # This screen only uses full 3-by-3 adjacent target blocks and unit extrema.
    cube_failures = []
    sylvester_failures = []
    unit_extrema = all(p[0] == p[14] == 1 for p in profiles)
    if unit_extrema and uniform_small:
        for vertex in range(3):
            previous, following = (vertex - 1) % 3, (vertex + 1) % 3
            for inside, outside in ((13, 1), (1, 13)):
                first = profiles[vertex][inside] + profiles[previous][outside]
                second = profiles[vertex][inside] + profiles[following][outside]
                rank = profiles[vertex][inside]
                if first == second == 3 and rank != 3:
                    cube_failures.append({'middle_vertex': vertex,
                                          'middle_charge': inside,
                                          'source_slice_rank': 3,
                                          'required_target_slice_rank': rank})
                lower = first + second - 3
                if rank < lower:
                    sylvester_failures.append({'middle_vertex': vertex,
                                                'middle_charge': inside,
                                                'first_dimension': first,
                                                'second_dimension': second,
                                                'required_target_slice_rank': rank,
                                                'source_slice_rank_lower_bound': lower})
    return {'vertex_charges': charges,
            'signed_weights': list(range(-14, 15)),
            'source_dimensions': [source_counts[w] for w in range(-14, 15)],
            'target_dimensions': [[counts[w] for w in range(-14, 15)] for counts in target_counts],
            'target_zero_dimensions': zeros,
            'capacity_failures': capacity_failures,
            'zero_weight_min_slice_failures': zero_failures,
            'full_degree13_cube_failures': cube_failures,
            'degree13_endpoint_sylvester_failures': sylvester_failures,
            'recorded_screens_pass': not (capacity_failures or zero_failures or cube_failures or sylvester_failures),
            'all_obstructions_exhausted': False}


def seed_coordinates():
    vertices = list(product(range(4), range(3)))
    entries = []
    for I, (alpha, beta) in enumerate(vertices):
        for J, (gamma, delta) in enumerate(vertices):
            entries.append((0, I, J, (SEED_U[alpha],
                                      SEED_U[gamma] + SEED_V[beta],
                                      SEED_V[delta])))
    for i, j in product(range(3), repeat=2):
        entries.append((1, i, j, (7 - i, 14 - j, 7)))
    return entries


def build():
    profiles = [list(p) for p in PROFILES]
    small_profiles = [[1] * 7 + [0] * 8 for _ in range(3)]
    screens = profile_screens(profiles, small_profiles)
    charges = screens['vertex_charges']
    # The common +6 shift places all M12 vertices at charges 2,...,13.
    # A common shift changes no target leg weight.
    seed_charges = [[u - v + 6 for u, v in product(SEED_U, SEED_V)], [2, 1, 0]]
    embeddings = [[[charges[leg][block].index(charge) for charge in seed_charges[block]]
                   for block in range(2)] for leg in range(3)]
    maps = [[], [], []]
    for block, i, j, coordinate in seed_coordinates():
        n, offset = ((27, 0), (7, 729))[block]
        for leg in range(3):
            row = offset + n * embeddings[leg][block][i] + embeddings[(leg + 1) % 3][block][j]
            maps[leg].append([row, source_index(leg, *coordinate), 1])
    return {'format': 'unequal-torus-profile-with-partial-seed-v1',
            'source_lengths': [8, 8], 'source_dimensions': [960, 960, 960],
            'target_blocks': [27, 7], 'target_dimensions': [778, 778, 778],
            'large_vertex_profiles': profiles, 'small_vertex_profiles': small_profiles,
            'vertex_charges': charges,
            'target_leg_convention': ['V0 tensor V1*', 'V1 tensor V2*', 'V2 tensor V0*'],
            'seed_blocks': [12, 3], 'seed_vertex_charges': seed_charges,
            'seed_vertex_embeddings': embeddings, 'partial_maps': maps,
            'screen_report': screens,
            'full_target_ordinary_homogeneous_maps_excluded': True,
            'exclusion_replay': 'parity_balancing_newton_pruning_audit.py',
            'exclusion_replayed_by_partial_tensor_verifier': False,
            'full_target_witness': False, 'new_exponent_established': False,
            'external_independent_review': False}


def contract(maps):
    if not isinstance(maps, list) or len(maps) != 3:
        raise ValueError('Exactly three actual maps are required')
    inverse = []
    for entries in maps:
        if len(entries) != 153:
            raise ValueError('Each partial map requires exactly 153 selected rows')
        rows, columns = set(), {}
        for entry in entries:
            if not isinstance(entry, list) or len(entry) != 3:
                raise ValueError('Sparse entries require three integers')
            row, column, coefficient = entry
            if any(type(x) is not int for x in entry) or not (0 <= row < 778 and 0 <= column < 960) or not coefficient:
                raise ValueError('Invalid sparse map entry')
            if row in rows or column in columns:
                raise ValueError('The monomial seed requires distinct rows and columns')
            rows.add(row)
            columns[column] = (row, coefficient)
        inverse.append(columns)
    actual = Counter()
    for point in source_terms():
        if all(point[leg] in inverse[leg] for leg in range(3)):
            terms = [inverse[leg][point[leg]] for leg in range(3)]
            actual[tuple(term[0] for term in terms)] += terms[0][1] * terms[1][1] * terms[2][1]
    return {point: coefficient for point, coefficient in actual.items() if coefficient}


def expected_partial(embeddings):
    expected = {}
    for block, (n, offset, core) in enumerate(((27, 0, 12), (7, 729, 3))):
        for i, j, k in product(range(core), repeat=3):
            v = (embeddings[0][block][i], embeddings[1][block][j], embeddings[2][block][k])
            expected[offset + n * v[0] + v[1],
                     offset + n * v[1] + v[2],
                     offset + n * v[2] + v[0]] = 1
    return expected


def verify(data):
    if data.get('source_lengths') != [8, 8] or data.get('target_blocks') != [27, 7] or data.get('seed_blocks') != [12, 3]:
        raise ValueError('Unexpected source, full target, or partial target')
    screens = profile_screens(data['large_vertex_profiles'], data['small_vertex_profiles'])
    if data['vertex_charges'] != screens['vertex_charges']:
        raise ArithmeticError('The supplied charge lists disagree with the actual profiles')
    embeddings = data['seed_vertex_embeddings']
    if len(embeddings) != 3 or len(data['seed_vertex_charges']) != 2:
        raise ValueError('Unexpected seed vertex data')
    for leg in range(3):
        if len(embeddings[leg]) != 2:
            raise ValueError('Two matrix blocks are required in each seed vertex space')
        for block, size in enumerate((12, 3)):
            positions = embeddings[leg][block]
            if len(positions) != size or len(set(positions)) != size:
                raise ValueError('Seed vertex embeddings must have the required distinct entries')
            for position, charge in zip(positions, data['seed_vertex_charges'][block]):
                if type(position) is not int or not 0 <= position < (27, 7)[block]:
                    raise ValueError('A seed vertex index is out of range')
                if screens['vertex_charges'][leg][block][position] != charge:
                    raise ArithmeticError('A seed vertex embedding has the wrong charge')
    actual = contract(data['partial_maps'])
    expected = expected_partial(embeddings)
    if actual != expected:
        raise ArithmeticError('The complete partial tensor coefficient identity fails')
    for leg in range(3):
        row_charges = target_row_charges(screens['vertex_charges'], leg)
        for row, column, _ in data['partial_maps'][leg]:
            if row_charges[row] != source_charge(leg, column):
                raise ArithmeticError('A partial map mixes distinct torus weights')
    parameters = sum(s * t for row in screens['target_dimensions']
                     for s, t in zip(screens['source_dimensions'], row))
    return {'profile_screens_recomputed': screens,
            'complete_source_terms_enumerated': 8 ** 6,
            'actual_partial_tensor': 'M12 direct sum M3',
            'nonzero_partial_tensor_coefficients': len(actual),
            'all_other_partial_coefficients_zero': True,
            'actual_map_ranks': [153, 153, 153],
            'full_target_map_rank_required': 778,
            'all_three_maps_respect_actual_unequal_vertex_charges': True,
            'known_recorded_profile_obstruction_detected': not screens['recorded_screens_pass'],
            'torus_map_parameters_all_three_legs': parameters,
            'squared_relative_residual_of_partial_seed': [20026 - len(actual), 20026],
            'full_target_witness': False, 'new_exponent_established': False,
            'external_independent_review': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT)
    parser.add_argument('--npz', type=Path)
    args = parser.parse_args()
    data = build()
    data['verification'] = verify(data)
    args.output.write_text(json.dumps(data, separators=(',', ':')) + '\n')
    if args.npz:
        import numpy as np
        matrices = [np.zeros((778, 960), dtype=np.int8) for _ in range(3)]
        for matrix, entries in zip(matrices, data['partial_maps']):
            for row, column, coefficient in entries:
                matrix[row, column] = coefficient
        np.savez_compressed(args.npz, A=matrices[0], B=matrices[1], C=matrices[2])
    print(json.dumps({'output': str(args.output), **data['verification']}, indent=2))


if __name__ == '__main__':
    main()
