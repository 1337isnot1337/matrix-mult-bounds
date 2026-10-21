"""Complete standard-library screen of the seven-diagonal vertex family.

There are 1,290,240 ways to choose one physical state on each of seven
consecutive diagonals of the 8 by 8 physical grid.  Injectivity and a
monotone partial weight-zero rank bound reduce the search to 16 choices.
Their complete tensor images all contain unwanted coefficients.
"""

from collections import Counter
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROFILE = [1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1]


def vertex_image(first, second):
    size = len(first)
    columns = {}
    for u, v in product(range(size), repeat=2):
        point = first[u], second[u] + first[v], second[v]
        if point in columns:
            raise ArithmeticError('The proposed vertex map is not injective')
        columns[point] = u * size + v
    image, exposed = {}, set()
    for u, v, w, z in product(range(size), repeat=4):
        i = second[w] + first[z] - second[v]
        s = second[u] + first[v] - first[w]
        if 0 <= i < 8 and 0 <= s < 8:
            point = i, first[u] + second[z], s
            exposed.add(point)
            if point in columns:
                image[columns[point], u * size + v, w * size + z] = 1
    return image, exposed


def expected_tensor(size):
    return {(size * i + j, size * j + k, size * k + i): 1
            for i, j, k in product(range(size), repeat=3)}


def search(threshold=11):
    size = 7
    new_pairs = [[] for _ in range(size)]
    for u, v, w, z in product(range(size), repeat=4):
        if u + w == v + z:
            new_pairs[max(u, v, w, z)].append((u, v, w, z))
    counts = {'complete_choices': 0, 'visited_partial_choices': 0,
              'injectivity_pruned_choices': 0, 'rank_pruned_choices': 0}
    survivors = []
    first, second = [0] * size, [0] * size
    for shift in range(-7, 2):
        options = [[i for i in range(8) if 0 <= i - shift - v < 8] for v in range(size)]
        completions = [1] * (size + 1)
        for v in range(size - 1, -1, -1):
            completions[v] = completions[v + 1] * len(options[v])
        counts['complete_choices'] += completions[0]

        def visit(depth, equal_first, equal_second, exposed):
            for value in options[depth]:
                counts['visited_partial_choices'] += 1
                first[depth], second[depth] = value, value - shift - depth
                next_first, next_second = equal_first, equal_second
                for j in range(depth):
                    if first[j] == first[depth]:
                        next_first |= 1 << (depth - j)
                    if second[j] == second[depth]:
                        next_second |= 1 << (depth - j)
                if next_first & next_second:
                    counts['injectivity_pruned_choices'] += completions[depth + 1]
                    continue
                next_exposed = exposed
                for u, v, w, z in new_pairs[depth]:
                    i = second[w] + first[z] - second[v]
                    s = second[u] + first[v] - first[w]
                    if 0 <= i < 8 and 0 <= s < 8:
                        next_exposed |= 1 << (8 * i + s)
                rank = next_exposed.bit_count()
                if rank > threshold:
                    counts['rank_pruned_choices'] += completions[depth + 1]
                elif depth + 1 < size:
                    visit(depth + 1, next_first, next_second, next_exposed)
                else:
                    survivors.append({'shift': shift, 'first_indices': first.copy(),
                                      'second_indices': second.copy(), 'weight_zero_pair_rank': rank})

        visit(0, 0, 0, 0)
    if counts['complete_choices'] != counts['injectivity_pruned_choices'] + counts['rank_pruned_choices'] + len(survivors):
        raise ArithmeticError('The partial branches do not cover the complete search space')
    return counts, survivors


def verify():
    counts, survivors = search()
    if counts['complete_choices'] != 1290240 or len(survivors) != 16:
        raise ArithmeticError('The complete finite screen changed')
    expected = expected_tensor(7)
    source_counts = Counter(i + s - k for i, k, s in product(range(8), range(15), range(8)))
    charges = [w for w, multiplicity in enumerate(PROFILE) for _ in range(multiplicity)]
    large_counts = Counter(i - j for i in charges for j in charges)
    for record in survivors:
        actual, exposed = vertex_image(record['first_indices'], record['second_indices'])
        if not expected.keys() <= actual.keys() or actual == expected:
            raise ArithmeticError('A surviving choice has an unexpected tensor image')
        extras = actual.keys() - expected.keys()
        diagonal = next((point for point in sorted(extras)
                         if all(row // 7 == row % 7 for row in point)), None)
        if diagonal is None:
            raise ArithmeticError('The row-valuation obstruction is missing')
        orbit = [diagonal, diagonal[1:] + diagonal[:1], diagonal[2:] + diagonal[:2]]
        if not all(point in extras for point in orbit):
            raise ArithmeticError('An unwanted diagonal cyclic orbit is incomplete')
        desired = [(row, row, row) for row in diagonal]
        for leg in range(3):
            if Counter(point[leg] for point in orbit) != Counter(point[leg] for point in desired):
                raise ArithmeticError('The unwanted and desired valuation sums do not balance')
        ranks = Counter(i + s - k for i, k, s in exposed)
        record.update({'complete_neighbor_matrix_pairs_checked': 7 ** 4,
                       'image_terms': len(actual), 'desired_terms_retained': len(expected),
                       'unwanted_terms': len(extras), 'exact_M7': False,
                       'pair_contraction_rank': len(exposed),
                       'pair_ranks_by_weight_minus14_to14': [ranks[w] for w in range(-14, 15)],
                       'all_weight_capacity_gates_pass': all(source_counts[w] - ranks[w] >= large_counts[w]
                                                             for w in range(-14, 15)),
                       'unwanted_diagonal_cyclic_orbit': orbit,
                       'matching_desired_diagonal_terms': desired,
                       'coefficientwise_Laurent_rescaling_obstructed': True})
        if ranks[0] != 9 or len(actual) != 841:
            raise ArithmeticError('A near-seed rank or complete image count changed')

    # Positive control and a counterexample to the proposed 2n-1 rank bound.
    control_image, control_exposed = vertex_image([0, 7], [0, 6])
    if control_image != expected_tensor(2):
        raise ArithmeticError('The nontrivial M2 positive control failed')
    zero_exposed = sorted(point for point in control_exposed if point[0] + point[2] == point[1])
    if len(zero_exposed) != 2:
        raise ArithmeticError('The rank-zero-weight counterexample changed')
    return {'source': 'A(8,8)', 'small_target_vertex_charges': list(range(7)),
            'family': 'common physical vertices, one on each of seven consecutive charge diagonals',
            'maximum_allowed_weight_zero_pair_rank': 11,
            **counts, 'surviving_capacity_choices': len(survivors),
            'exact_M7_choices_passing_weight_zero_gate': 0,
            'near_seeds': survivors,
            'positive_M2_control': {'physical_vertices': [[0, 0], [7, 6]],
                                    'target_terms': 8, 'weight_zero_pair_rank': 2,
                                    'exposed_zero_weight_coordinates': zero_exposed,
                                    'counterexample_to_r0_at_least_2n_minus_1': True},
            'general_mixed_source_maps_excluded': False,
            'arbitrary_target_basis_changes_excluded': False,
            'standard_library_only': True, 'new_exponent_established': False}


if __name__ == '__main__':
    report = verify()
    (HERE / 'parity_structure_m7_vertex_screen.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'near_seeds'}, indent=2))
