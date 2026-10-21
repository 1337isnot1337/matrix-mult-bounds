"""Exact three-leg assembly budgets for the original 28-channel spin core.

Acceptance uses only Python integers and the standard library.  The complete
source contraction is rebuilt from the published maps.  Nonzero modular
minors and exact integer kernels certify all three rational response ranks.
The larger rectangular target remains unconstructed.
"""

import argparse
from collections import Counter, defaultdict
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path


DIRECTORY = Path(__file__).resolve().parent
ROOT = DIRECTORY.parents[2]
RESULTS = ROOT / 'results/anisotropic-constructions-2026-10-20'
FULL_MAPS = RESULTS / 'spin-module14-full-maps.json'
CERTIFICATE = RESULTS / 'spin-rectangle-budget-certificate.json'
REPORT = RESULTS / 'spin-rectangle-budget-report.json'
SPEC = importlib.util.spec_from_file_location(
    'spin_rectangle_assembly_dependency', DIRECTORY / 'parity_balancing_spin_assembly.py')
assembly = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assembly)


def load_maps(exported=None):
    exported = json.loads(FULL_MAPS.read_text()) if exported is None else exported
    entries = [item for item in exported.get('restrictions', [])
               if item.get('source') == [8, 8]]
    if len(entries) != 1 or entries[0].get('target') != [3, 3, 28]:
        raise ArithmeticError('The published A88 to M(3,3,28) map is required')
    parsed = [assembly.parse(entries[0]['maps'][name], (rows, 960))
              for name, rows in zip('XYZ', (9, 84, 84))]
    return [matrix for matrix, denominator in parsed], [d for matrix, d in parsed]


def other_response(maps, free_leg):
    """Contract every original source term against the other two fixed maps."""
    if free_leg not in (1, 2):
        raise ValueError('Use first_response for the first leg')
    fixed = [leg for leg in range(3) if leg != free_leg]
    inverses = [assembly.inverse(matrix) for matrix in maps]
    response = defaultdict(Counter)
    for point in assembly.source(8, 8):
        first, second = (inverses[leg].get(point[leg], ()) for leg in fixed)
        for (a, va), (b, vb) in product(first, second):
            response[point[free_leg]][84 * a + b] += va * vb
    return {column: {output: value for output, value in row.items() if value}
            for column, row in response.items() if any(row.values())}


def response_supports():
    coordinate = assembly.coordinate
    return (
        {coordinate(i, k, s) for i, k, s in product(range(8), range(3), range(8))},
        {coordinate(p, ell, j) for p, ell, j in product(range(3), range(10), range(8))},
        {coordinate(r, h, q) for r, h, q in product(range(8), range(9), range(3))},
    )


def check_rank_certificate(response, data, support, rank, width):
    if data.get('rank') != rank or data.get('support') != sorted(support):
        raise ArithmeticError('Incorrect response support or rank certificate')
    if not set(response) <= support:
        raise ArithmeticError('Actual coefficients escape the stated response support')
    assembly.check_minor(response, data['minor_rows'], data['minor_columns'], rank, width)
    vectors = data['integer_kernel_vectors']
    if not isinstance(vectors, list) or len(vectors) != len(support) - rank:
        raise ArithmeticError('Incorrect number of exact kernel vectors')
    dense = []
    for vector in vectors:
        if not isinstance(vector, list):
            raise ArithmeticError('Malformed integer kernel vector')
        entries = {}
        for entry in vector:
            if (not isinstance(entry, list) or len(entry) != 2
                    or any(type(value) is not int for value in entry)):
                raise ArithmeticError('Kernel entries must be integer pairs')
            column, value = entry
            if column not in support or not value or column in entries:
                raise ArithmeticError('Invalid integer kernel coordinate')
            entries[column] = value
        contraction = Counter()
        for column, value in entries.items():
            for output, coefficient in response.get(column, {}).items():
                contraction[output] += value * coefficient
        if any(contraction.values()):
            raise ArithmeticError('An integer kernel vector has a nonzero exact coefficient')
        dense.append([entries.get(column, 0) for column in sorted(support)])
    if assembly.modular_rank(dense) != len(vectors):
        raise ArithmeticError('The exact kernel vectors are dependent')
    return {'response_rank': rank, 'response_support_size': len(support),
            'integer_kernel_vectors_inside_support': len(vectors),
            'zero_coordinate_directions_outside_support': 960 - len(support),
            'full_kernel_dimension': 960 - rank}


def budgets(response_ranks=(192, 236, 216), target=(27, 28, 28), core=(3, 3, 28)):
    a, b, c = target
    p, q, r = core
    target_dimensions = (a * b, b * c, c * a)
    core_dimensions = (p * q, q * r, r * p)
    result = []
    for leg, rank, kept, needed in zip('XYZ', response_ranks, core_dimensions, target_dimensions):
        result.append({
            'leg': leg, 'response_rank': rank, 'retained_leg_dimension': kept,
            'target_leg_dimension': needed, 'kernel_dimension': 960 - rank,
            'preimage_dimension': 960 - rank + kept,
            'additional_rows_required': needed - kept,
            'excess_response_rank': rank - kept,
            'allowed_excess_response_rank': 960 - needed,
            'remaining_excess_rank_budget': 960 - needed - rank + kept,
            'necessary_preimage_test_passes': needed <= 960 - rank + kept,
        })
    return result


def hankel_checks(target=(27, 28, 28)):
    """Only the already proved r=1,...,5 fixed-symbol conditions are used."""
    a, b, c = target
    dimensions = (a * b, b * c, c * a)
    slice_ranks = (c, a, b)
    losses = tuple(960 - dimension for dimension in dimensions)
    result = []
    for leg in range(3):
        for r in range(1, 6):
            lhs = slice_ranks[leg] + sum(losses[j] for j in range(3) if j != leg)
            required = 64 * (r + 1)
            antecedent = dimensions[leg] > 64 * r
            result.append({'leg': 'XYZ'[leg], 'symbol_rank_parameter': r,
                           'dimension_antecedent_holds': antecedent,
                           'lifted_slice_rank_upper_bound': lhs,
                           'required_lower_bound': required,
                           'necessary_test_passes': not antecedent or lhs >= required})
    return result


def verify(certificate=None, exported=None):
    certificate = json.loads(CERTIFICATE.read_text()) if certificate is None else certificate
    if certificate.get('new_exponent_established') is not False:
        raise ArithmeticError('The certificate must preserve the conditional status')
    if certificate.get('prime') != assembly.PRIME:
        raise ArithmeticError('The certificate uses an unsupported modulus')
    maps, denominators = load_maps(exported)
    replay = assembly.full_contraction(assembly.source(8, 8), maps, denominators, 28)
    first, pairs = assembly.first_response(maps[1], maps[2], 28)
    responses = (first, other_response(maps, 1), other_response(maps, 2))
    ranks = (192, 236, 216)
    checked = [check_rank_certificate(response, certificate[leg], support, rank, width)
               for leg, response, support, rank, width in zip(
                   'XYZ', responses, response_supports(), ranks, (84 * 84, 9 * 84, 9 * 84))]
    budget = budgets(ranks)
    if not all(row['necessary_preimage_test_passes'] for row in budget):
        raise ArithmeticError('The recorded rectangular preimage budget fails')
    hankel = hankel_checks()
    if not all(row['necessary_test_passes'] for row in hankel):
        raise ArithmeticError('A recorded necessary Hankel condition fails')
    volume, numerator, denominator = 27 * 28 * 28, 2247, 1000
    if not pow(216 * volume, numerator) > pow(46, 9 * denominator):
        raise ArithmeticError('The exact conditional exponent comparison fails')
    grown = budgets((192, 236, 216), core=(3, 4, 28))[0]
    return {
        'scope': 'Exact response ranks of the published full 28-channel spin core; ordinary fixed-core extension budgets',
        'arithmetic': 'Python integers; nonzero response minors modulo 65521; exact integer kernel vectors',
        'source': [8, 8], 'source_leg_dimension': 960,
        'actual_retained_core': [3, 3, 28], 'conditional_target': [27, 28, 28],
        'complete_source_replay': replay, 'first_response_contributing_coordinate_pairs': pairs,
        'response_certificates': dict(zip('XYZ', checked)), 'three_leg_budgets': budget,
        'known_necessary_hankel_tests': hankel,
        'conditional_exponent': {'numerator': numerator, 'denominator': denominator,
                                 'target_volume': volume,
                                 'integer_inequality': '(216*21168)^2247 > 46^9000',
                                 'inequality_passes': True, 'requires_full_target_construction': True},
        'one_complete_new_second_vertex': {
            'core': [3, 4, 28], 'first_retained_span_dimension': grown['retained_leg_dimension'],
            'first_response_rank_cap': 960 - 756 + grown['retained_leg_dimension'],
            'raw_rank_growth_allowed_from_original_seed': 24,
            'unchanged_excess_response_budget': 204,
        },
        'fixed_map_tests_are_necessary_only': True,
        'full_rectangular_target_constructed': False,
        'new_exponent_established': False, 'external_independent_review': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=REPORT)
    args = parser.parse_args()
    report = verify()
    report['input_sha256'] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                              for path in (FULL_MAPS, CERTIFICATE)}
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
