"""Exact pair-contraction ranks of the available free-interior M7 maps.

The two pure M7 maps and their charge-compatible diagonal mixtures
cannot be frozen as the small block of A88 -> M27 + M7.  This is a
scope test of those maps, not an exclusion of movable small-block maps.
All computations use the standard library and the complete source.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

from parity_structure_free_interior import common_point, source_terms


HERE = Path(__file__).resolve().parent
PROFILE = [1, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 1, 1]


def maps_for_channel(data, channel):
    result = []
    for entries in data['maps']:
        selected = []
        for row, column, value in entries:
            if channel == 'low' and row < 49:
                selected.append((row, column, value))
            elif channel == 'high' and 49 <= row < 98:
                i, j = divmod(row - 49, 7)
                selected.append(((6 - i) * 7 + 6 - j, column, value))
        result.append(selected)
    return result


def pair_flattenings(maps):
    inverse = []
    for entries in maps:
        by_column = defaultdict(list)
        for row, column, value in entries:
            by_column[column].append((row, value))
        inverse.append(by_column)
    flattened = [defaultdict(Counter) for _ in range(3)]
    for point in source_terms(8):
        for leg in range(3):
            other, last = (leg + 1) % 3, (leg + 2) % 3
            if point[other] not in inverse[other] or point[last] not in inverse[last]:
                continue
            for left, right in product(inverse[other][point[other]], inverse[last][point[last]]):
                flattened[leg][left[0], right[0]][point[leg]] += left[1] * right[1]
    return [{row: {column: value for column, value in values.items() if value}
             for row, values in leg.items()} for leg in flattened]


def exact_rank(rows):
    basis = {}
    for coefficients in rows:
        row = {column: Fraction(value) for column, value in coefficients.items() if value}
        while row:
            pivot = min(row)
            if pivot not in basis:
                coefficient = row[pivot]
                basis[pivot] = {column: value / coefficient for column, value in row.items()}
                break
            coefficient = row[pivot]
            for column, value in basis[pivot].items():
                row[column] = row.get(column, 0) - coefficient * value
                if not row[column]:
                    del row[column]
    return len(basis)


def report_channel(maps):
    source_counts = Counter(i + s - k for i, k, s in product(range(8), range(15), range(8)))
    charges = [weight for weight, count in enumerate(PROFILE) for _ in range(count)]
    target_counts = Counter(i - j for i in charges for j in charges)
    all_reports = []
    for leg, flattened in enumerate(pair_flattenings(maps)):
        by_weight = defaultdict(list)
        for coefficients in flattened.values():
            weights = {i + s - k for column in coefficients
                       for i, k, s in [common_point(8, leg, column)]}
            if len(weights) > 1:
                raise ArithmeticError('A pair row mixes source weights')
            if weights:
                by_weight[weights.pop()].append(coefficients)
        ranks = {weight: exact_rank(by_weight[weight]) for weight in range(-14, 15)}
        total = sum(ranks.values())
        inequalities = [{'weight': weight, 'source_dimension': source_counts[weight],
                         'pair_contraction_rank': ranks[weight],
                         'remaining_source_dimension': source_counts[weight] - ranks[weight],
                         'required_M27_dimension': target_counts[weight],
                         'passes': source_counts[weight] - ranks[weight] >= target_counts[weight]}
                        for weight in range(-14, 15)]
        all_reports.append({'remaining_leg': leg, 'source_terms_checked': 8 ** 6,
                            'pair_contraction_rank': total,
                            'remaining_source_dimension': 960 - total,
                            'required_M27_dimension': 729,
                            'total_dimension_inequality_passes': 960 - total >= 729,
                            'weight_inequalities': inequalities,
                            'failed_weights': [row['weight'] for row in inequalities if not row['passes']]})
    return all_reports


def verify():
    data = json.loads((HERE / 'parity_structure_free_interior_sparse.json').read_text())
    low, high = maps_for_channel(data, 'low'), maps_for_channel(data, 'high')
    mixed = [left + right for left, right in zip(low, high)]
    reports = {name: report_channel(maps) for name, maps in [('low', low), ('high', high), ('equal_diagonal_mix', mixed)]}
    for name, legs in reports.items():
        wanted = 637 if name == 'equal_diagonal_mix' else 343
        for leg in legs:
            if leg['pair_contraction_rank'] != wanted:
                raise ArithmeticError('An exact pair-contraction rank disagrees with the formula')
            zero = next(row for row in leg['weight_inequalities'] if row['weight'] == 0)
            expected_zero = 49 if name == 'equal_diagonal_mix' else 28
            if zero['pair_contraction_rank'] != expected_zero or zero['required_M27_dimension'] != 53:
                raise ArithmeticError('The weight-zero screen disagrees with the formula')
    return {'source': 'A(8,8)', 'target': 'M27 direct sum M7',
            'M27_vertex_charge_multiplicities': PROFILE,
            'standard_library_exact_ranks': True,
            'small_block_maps_fixed': True,
            'screens': reports,
            'all_scalar_diagonal_mixtures_excluded_by_projected_rank_343': True,
            'generic_equal_mixture_tensor_before_rescaling': '2 times M7; rescale one leg by 1/2',
            'general_movable_M7_maps_excluded': False,
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    (HERE / 'parity_structure_free_m7_screen.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key != 'screens'}, indent=2))
    print(json.dumps({name: [{key: value for key, value in leg.items() if key != 'weight_inequalities'}
                              for leg in legs] for name, legs in result['screens'].items()}, indent=2))
