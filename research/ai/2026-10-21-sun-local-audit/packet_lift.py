"""Exact obstruction to a packetwise lift of Sun's printed dense ledger.

This does not exclude a different construction mixing packet contributions.
The original source is https://arxiv.org/html/2610.13971v1, Section 5.
"""
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


B0 = (9, 4, 8, 6)
B1 = (8, 6, 4, 9)
TWISTS = {'A1': 3, 'A3': 0, 'B1': 5, 'B2': 9,
          'C1': 6, 'P': 10, 'Q': 12, 'R': 15}
SUPPORTS = {'A1': ('x0', 'y1', 'z1'),
            'A3': ('x0', 'y3', 'z3'),
            'B1': ('x1', 'y0', 'z1'),
            'B2': ('x2', 'y0', 'z2'),
            'C1': ('x1', 'y1', 'z0'),
            'P': ('x0', 'y0', 'zinf'),
            'Q': ('x0', 'yinf', 'z0'),
            'R': ('xinf', 'y0', 'z0')}


def linear_map(columns, value):
    result = 0
    for index, column in enumerate(columns):
        if value & (1 << index):
            result ^= column
    return result


def parity(first, second):
    return (first & second).bit_count() & 1


def central_defect(u, v, w):
    epsilon, a = u
    delta, b = v
    phi, c = w
    return (b ^ a ^ epsilon, phi ^ epsilon ^ delta,
            c ^ a ^ epsilon ^ delta)


def chart(defect, high_defect=0):
    right = linear_map((1, 2, 12), sum(bit << i
                       for i, bit in enumerate(defect)))
    candidates = [beta for beta in range(16)
                  if linear_map(B0, beta) ^ linear_map(B1, beta) == right]
    if len(candidates) != 2:
        raise ArithmeticError(('chart fibre', defect, candidates))
    # The choice with top bit zero is a linear section. The output identity
    # below also checks the other representative of every chart fibre.
    return [(high_defect ^ linear_map(B0, beta), beta)
            for beta in candidates]


def matrix_tensor_two():
    return {(2 * i + j, 2 * j + k, 2 * k + i): 1
            for i, j, k in product(range(2), repeat=3)}


def strassen_coefficient_control():
    terms = [({0: 1, 3: 1}, {0: 1, 3: 1}, {0: 1, 3: 1}),
             ({2: 1, 3: 1}, {0: 1}, {1: 1, 3: -1}),
             ({0: 1}, {1: 1, 3: -1}, {2: 1, 3: 1}),
             ({3: 1}, {2: 1, 0: -1}, {0: 1, 1: 1}),
             ({0: 1, 1: 1}, {3: 1}, {0: -1, 2: 1}),
             ({2: 1, 0: -1}, {0: 1, 1: 1}, {3: 1}),
             ({1: 1, 3: -1}, {2: 1, 3: 1}, {0: 1})]
    result = {}
    for first, second, third in terms:
        for (i, a), (j, b), (k, c) in product(first.items(), second.items(), third.items()):
            result[i, j, k] = result.get((i, j, k), 0) + a * b * c
    assert {index: value for index, value in result.items() if value} == matrix_tensor_two()
    return len(terms)


def koszul_rank_mod_prime(tensor, ambient=5, power=2, prime=65521):
    rows = {(subset, output): i
            for i, (subset, output) in enumerate(
                product(combinations(range(ambient), power + 1), range(4)))}
    pivots = {}
    for subset, contracted in product(combinations(range(ambient), power), range(4)):
        vector = {}
        for (first, second, third), value in tensor.items():
            if second != contracted or first in subset:
                continue
            inserted = tuple(sorted(subset + (first,)))
            row = rows[inserted, third]
            sign = (-1) ** sum(vertex < first for vertex in subset)
            vector[row] = (vector.get(row, 0) + sign * value) % prime
        vector = {row: value for row, value in vector.items() if value}
        while vector:
            pivot = min(vector)
            if pivot not in pivots:
                inverse = pow(vector[pivot], -1, prime)
                pivots[pivot] = {row: value * inverse % prime
                                 for row, value in vector.items()}
                break
            factor = vector[pivot]
            for row, value in pivots[pivot].items():
                replacement = (vector.get(row, 0) - factor * value) % prime
                if replacement:
                    vector[row] = replacement
                else:
                    vector.pop(row, None)
    return len(pivots)


def verify():
    generic_characters = [chi for chi in range(16) if chi not in {6, 7, 10, 11}]
    even = [theta for theta in range(16) if theta.bit_count() % 2 == 0]
    assert sorted(TWISTS.values()) == even
    annihilators = []
    for side in range(3):
        differences = set()
        for first, second in combinations(TWISTS, 2):
            if SUPPORTS[first][side] == SUPPORTS[second][side]:
                differences.add(TWISTS[first] ^ TWISTS[second])
        allowed = [beta for beta in range(16)
                   if all(parity(theta, beta) == 0 for theta in differences)]
        assert allowed == [0, 15]
        assert all(linear_map(B0, beta) == linear_map(B1, beta) for beta in allowed)
        annihilators.append({'side': 'XYZ'[side],
                             'shared_coordinate_twist_differences': sorted(differences),
                             'allowed_beta_values': allowed,
                             'image_under_B0_plus_B1': [0]})
    labels = list(product(range(2), repeat=2))
    expected = matrix_tensor_two()
    pointwise_checks = 0
    for chi in generic_characters:
        observed = {}
        for u, v, w in product(labels, repeat=3):
            epsilon, a = u
            delta, b = v
            phi, c = w
            # The physical H4 displacements are fixed to 1,2,3. None of the
            # three labels is punctured, and their high defect is zero.
            for rho, beta in chart(central_defect(u, v, w)):
                coefficient = Fraction(sum(
                    (-1) ** (parity(chi, rho ^ linear_map(B1, beta))
                              ^ parity(theta, beta))
                    for theta in TWISTS.values()), 128)
                index = (2 * a + (a ^ epsilon),
                         2 * b + (b ^ delta),
                         2 * c + (c ^ phi))
                assert coefficient == Fraction(expected.get(index, 0), 16)
                pointwise_checks += 1
                if coefficient:
                    observed[index] = int(16 * coefficient)
        assert observed == expected
    rank = koszul_rank_mod_prime(expected)
    assert rank == 32
    strassen_terms = strassen_coefficient_control()
    return {
        'source_url': 'https://arxiv.org/html/2610.13971v1',
        'scope': ('A packet-by-packet lift preserving the literal generic '
                  'layer-one contribution in equation (5.1). This does not '
                  'exclude different maps mixing packet contributions.'),
        'generic_layer_one_character_count': len(generic_characters),
        'retained_twists': TWISTS,
        'twists_are_the_even_weight_subspace': True,
        'additive_linear_phase_obstructions': annihilators,
        'nonzero_fixed_displacements': [1, 2, 3],
        'central_four_coordinates_tensor': '(1/16) M_2',
        'pointwise_checks_including_both_chart_representatives': pointwise_checks,
        'M2_coefficient_Koszul': {'ambient_first_dimension': 5, 'power': 2,
                                 'prime': 65521, 'rank': rank,
                                 'border_rank_5_maximum': 30,
                                 'inference_field_scope': 'characteristic zero'},
        'packetwise_C3_or_D4_lift_excluded': True,
        'optimistic_Strassen_replacement_bookkeeping': {
            'old_full_source_cost_per_row': 128,
            'generic_dense_modules': '7 C3 and 5 D4',
            'old_generic_dense_allocated_cost_per_row': 55,
            'new_12_M2_modules_cost_per_row': 12 * strassen_terms,
            'Strassen_integer_coefficient_identity_verified': True,
            'new_total_if_other_charges_unchanged': 2512,
            'largest_integer_below_32_to_9_over_4': 2435,
            'is_a_valid_global_construction': False,
            'remaining_issues': ['Completion outputs of replaced modules',
                                 'Source-resolved row and Weyl coupling']},
        'full_preprint_impossibility_claim': False,
        'improves_omega': False}


if __name__ == '__main__':
    report = verify()
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    destination = args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('retained_twists', 'additive_linear_phase_obstructions')}))
