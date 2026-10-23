"""Exact exploratory follow-up; this file does not claim a target construction.

Use from the conjugation package beside verify.py and discovery.py.
Acceptance replays complete polynomial identities and invariant-subspace
equations over Q. The modular calculation only screens which principal
coordinate pairs require complete re-saturation.
"""
import argparse
from collections import Counter, defaultdict
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys

SIZE = 112


def add_shifted(target, source, coefficient=1, shift=0):
    for (degree, position), value in source.items():
        key = (degree + shift, position)
        target[key] = target.get(key, 0) + coefficient * value
        if not target[key]:
            del target[key]


def accept_basis(family, records):
    """Replay every coefficient, then certify all 112 independent constants."""
    if len(records) != SIZE:
        raise ValueError('full source dimension was lost')
    pivots = set()
    matrices = []
    for record in records:
        polynomial = {}
        for shift, source, coefficient in record['transform']:
            add_shifted(polynomial, family[source], coefficient, shift)
        degree = record['degree']
        actual = {position: value for (power, position), value in polynomial.items()
                  if power == degree}
        expected = dict(record['leading'])
        if (not polynomial or max(power for power, _ in polynomial) != degree
                or actual != expected):
            raise ValueError('the complete polynomial transformation failed replay')
        pivot = max(actual)
        if pivot != record['pivot'] or pivot in pivots:
            raise ValueError('the leading matrices are not certified independent')
        pivots.add(pivot)
        matrices.append(actual)
    return matrices


def scalar_coordinates(matrices):
    groups = defaultdict(list)
    for column in range(SIZE):
        if any(any(position // SIZE != column and position % SIZE == column
                       for position in matrix) for matrix in matrices):
            continue
        groups[tuple(matrix.get((SIZE + 1) * column, 0) for matrix in matrices)].append(column)
    return max(groups.values(), key=len, default=[])


def incompatible_invariant(matrices, holes):
    remaining = set(range(SIZE)) - set(holes)
    edges = {index: set() for index in remaining}
    for matrix in matrices:
        for position in matrix:
            row, column = divmod(position, SIZE)
            edges[column].add(row)
    for first in sorted(remaining):
        subspace = {first}
        pending = [first]
        while pending:
            column = pending.pop()
            for row in edges[column]:
                if row not in subspace:
                    subspace.add(row)
                    pending.append(row)
        if len(subspace) % 10:
            # This check uses literal integer zeroes, not modular entries.
            if any(any(position % SIZE in subspace and position // SIZE not in subspace
                       for position in matrix) for matrix in matrices):
                raise ValueError('claimed invariant coordinate subspace is not invariant')
            return sorted(subspace)
    return None


def two_square_zero_family(source, verifier):
    nilpotents = [source[0], source[111]]
    if any(verifier.matrix_product(matrix, matrix) for matrix in nilpotents):
        raise ValueError('a factor is not square zero')
    products = [verifier.matrix_product(*nilpotents), verifier.matrix_product(*reversed(nilpotents))]
    if not all(products):
        raise ValueError('a proposed degree-two leading factor is zero')
    if products[0] == products[1]:
        raise ValueError('the proposed factors commute')
    family = []
    for matrix in source:
        coefficients = {0: matrix}
        for nilpotent in nilpotents:
            polynomial = {}
            for degree, coefficient in coefficients.items():
                blocks = [(degree, coefficient, 1),
                          (degree + 1, verifier.matrix_product(coefficient, nilpotent), 1),
                          (degree + 1, verifier.matrix_product(nilpotent, coefficient), -1),
                          (degree + 2, verifier.matrix_product(
                              verifier.matrix_product(nilpotent, coefficient), nilpotent), -1)]
                for power, block, sign in blocks:
                    for position, value in block.items():
                        key = power, position
                        polynomial[key] = polynomial.get(key, 0) + sign * value
            coefficients = {}
            for (degree, position), value in polynomial.items():
                if value:
                    coefficients.setdefault(degree, {})[position] = value
        family.append({(degree, position): value for degree, matrix in coefficients.items()
                       for position, value in matrix.items()})
    return family, {
        'family': 'g^-1 H g; g=(I+z H_0,0,0)(I+z H_6,3,3)',
        'source_indices': [0, 111],
        'both_long_leading_maps_singular': True,
        'leading_map_rank_upper_bounds': [16, 16],
        'factors_do_not_commute': True,
    }


def nonnilpotent_family(source, verifier):
    source_sum = dict(source[0])
    verifier.add_multiple(source_sum, source[111])
    identity = {(SIZE + 1) * i: 1 for i in range(SIZE)}
    # This exact polynomial was discovered by rational dependence of N powers.
    # Acceptance needs its annihilation identity, not minimality.
    annihilator = [0, 0, 0, 6, 0, -65, 0, 141, 0, -127, 0, 56, 0, -12, 0, 1]
    degree = len(annihilator) - 1
    denominator = [(-1) ** j * annihilator[degree - j] for j in range(degree + 1)]
    numerator = [identity]
    for power in range(1, degree):
        matrix = {position: denominator[power] * value for position, value in identity.items()
                  if denominator[power]}
        verifier.add_multiple(matrix, verifier.matrix_product(source_sum, numerator[-1]), -1)
        numerator.append(matrix)
    residue = {position: denominator[-1] * value for position, value in identity.items()
               if denominator[-1]}
    verifier.add_multiple(residue, verifier.matrix_product(source_sum, numerator[-1]), -1)
    if residue:
        raise ValueError('the rational inverse numerator fails its exact identity')
    # The recurrence checks B(z)(I+zN)=D(z)I. Every B coefficient is a
    # polynomial in N, so the reversed identity follows as well.
    family = []
    for matrix in source:
        polynomial = {}
        for power, coefficient in enumerate(numerator):
            block = verifier.matrix_product(coefficient, matrix)
            for position, value in block.items():
                key = power, position
                polynomial[key] = polynomial.get(key, 0) + value
            for position, value in verifier.matrix_product(block, source_sum).items():
                key = power + 1, position
                polynomial[key] = polynomial.get(key, 0) + value
        family.append({key: value for key, value in polynomial.items() if value})
    upper_bound = len({position // SIZE for position in numerator[-1]})
    if not numerator[-1] or upper_bound >= SIZE:
        raise ValueError('the inverse leading map is not certified singular')
    return family, {
        'family': 'U^-1 H U; U=I+z(H_0,0,0+H_6,3,3)',
        'source_indices': [0, 111],
        'annihilating_polynomial_ascending': annihilator,
        'common_resolvent_denominator_ascending': denominator,
        'both_long_leading_maps_singular': True,
        'leading_map_rank_upper_bounds': [upper_bound, 32],
        'inverse_identity_checked_over': 'Q[z]',
    }


def investigate(family, metadata, verifier, discovery):
    records = discovery.polynomial_basis(family)
    leading = accept_basis(family, records)
    scalar = scalar_coordinates(leading)
    if len(scalar) <= 2:
        raise ValueError('the rank-loss theorem does not screen this case')
    histogram = Counter()
    candidates = []
    for holes in combinations(range(SIZE), 2):
        deleted = set(holes)
        projected = ({position: value for position, value in matrix.items()
                      if position // SIZE not in deleted and position % SIZE not in deleted}
                     for matrix in leading)
        rank = verifier.modular_rank(projected)
        histogram[rank] += 1
        if rank <= 103:
            candidates.append((holes, rank))
    witnesses = []
    survivors = []
    for holes, projected_rank in candidates:
        deleted = set(holes)
        projected_family = [{(degree, position): value for (degree, position), value in matrix.items()
                             if position // SIZE not in deleted and position % SIZE not in deleted}
                            for matrix in family]
        records = discovery.polynomial_basis(projected_family)
        matrices = accept_basis(projected_family, records)
        invariant = incompatible_invariant(matrices, holes)
        if invariant is None:
            survivors.append(list(holes))
        else:
            witnesses.append({'holes': list(holes), 'projected_modular_rank': projected_rank,
                              'invariant_coordinates': invariant,
                              'invariant_dimension': len(invariant)})
    return {
        **metadata,
        'full_limit_dimension': SIZE,
        'full_limit_scalar_coordinates': scalar,
        'principal_pairs_screened': sum(histogram.values()),
        'screening_prime': verifier.PRIME,
        'projected_modular_rank_histogram': {str(key): value for key, value in sorted(histogram.items())},
        'pairs_requiring_exact_resaturation': len(candidates),
        'complete_resaturation_coefficient_replays': len(candidates),
        'invariant_identities_checked_over': 'Q',
        'incompatible_invariant_witnesses': witnesses,
        'surviving_coordinate_pairs': survivors,
        'full_target_maps_constructed': 0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    for name in ('verify', 'discovery'):
        spec = importlib.util.spec_from_file_location(name, arguments.package / (name + '.py'))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    verifier, discovery = sys.modules['verify'], sys.modules['discovery']
    source, _ = verifier.build_source()
    results = []
    for constructor in (two_square_zero_family, nonnilpotent_family):
        family, metadata = constructor(source, verifier)
        results.append(investigate(family, metadata, verifier, discovery))
        print(metadata['family'], 'completed', flush=True)
    report = {
        'schema': 'a4-two-sided-escape-exploration-v1',
        'status': 'finite exact exploratory computation; no additional theorem claim',
        'source_order': 'k,i,s',
        'cases': results,
        'target_acceptance_condition': 'complete M(10,10,11) matrix-unit tensor identity',
        'full_target_maps_constructed': 0,
        'exponent_improvement_proved': False,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(report, separators=(',', ':'), sort_keys=True) + '\n')
    print(arguments.output, flush=True)


if __name__ == '__main__':
    main()
