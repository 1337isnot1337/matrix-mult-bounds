"""Exact binary projective orbits and quadratic-defect controls.

The finite size profiles do not themselves prove periodicity or torsion.
Small cohomology kernels are recorded separately from literal source ranks.
"""
import argparse
from collections import Counter
import importlib.util
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    'quadratic_torsion_base', HERE.parent / '2026-10-23-quadratic-kernel-indices/verify.py')
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)
SIZES = [3, 4, 5, 7, 8, 9, 11, 12, 13, 14, 15]


def rank_binary(rows):
    """Exact binary elimination using packed rows, independent of base.rank."""
    pivots = {}
    for coefficients in rows:
        row = sum((value & 1) << i for i, value in enumerate(coefficients))
        while row:
            column = row.bit_length() - 1
            if column not in pivots:
                pivots[column] = row
                break
            row ^= pivots[column]
    return len(pivots)


def triple(coefficients):
    return [list(coefficients[3 * j:3 * j + 3]) for j in range(3)]


def candidates():
    result = set()
    for coefficients in product(range(2), repeat=9):
        if not any(coefficients):
            continue
        primitive, gcd = base.primitive_triple(triple(coefficients), 2)
        if len(gcd) == 1 and max(map(len, primitive)) == 3 and not base.fixed_roots(primitive, 2):
            result.add(coefficients)
    return result


def projective_group():
    return [matrix for matrix in product(range(2), repeat=4)
            if (matrix[0] * matrix[3] - matrix[1] * matrix[2]) % 2]


def quadratic_action(matrix):
    """Columns are substituted X0^2, X0 X1 and X1^2 over F2."""
    a, b, c, d = matrix
    if (a * d - b * c) % 2 != 1:
        raise ValueError('projective substitution must be invertible over F2')
    return [[a, a * c, c], [0, (a * d + b * c) % 2, 0], [b, b * d, d]]


def transform(coefficients, x_matrix, z_matrix):
    x_action, z_action = quadratic_action(x_matrix), quadratic_action(z_matrix)
    return tuple(sum(z_action[k][l] * coefficients[3 * l + j] * x_action[i][j]
                     for l in range(3) for j in range(3)) % 2
                 for k in range(3) for i in range(3))


def orbits():
    remaining = candidates()
    group = projective_group()
    result = []
    while remaining:
        representative = min(remaining)
        members = {transform(representative, x, z) for x in group for z in group}
        if not members <= remaining:
            raise ArithmeticError('projective orbit overlaps or leaves the candidate set')
        result.append({'representative': list(representative),
                       'members': [list(member) for member in sorted(members)]})
        remaining -= members
    return result


def check_kernel_polynomials(matrix, a, polynomials):
    if len(polynomials) != a + 2 or any(len(item) > a for item in polynomials):
        raise ArithmeticError('kernel witness has invalid coordinate degrees')
    vector = [value for item in polynomials for value in list(item) + [0] * (a - len(item))]
    if not any(value % 2 for value in vector) or any(
            sum(value * entry for value, entry in zip(row, vector)) % 2 for row in matrix):
        raise ArithmeticError('recorded kernel witness does not satisfy the equations')


def kernel_record(a, coefficients):
    """C_(a-1) on a recurrence; a may be small for cohomology-only controls."""
    polynomials = triple(coefficients)
    matrix = base.recurrence_matrix(a, polynomials, a - 1)
    width = a * (a + 2)
    if len(matrix) != width or any(len(row) != width for row in matrix):
        raise ArithmeticError('degree-two cohomology matrix is not square')
    nullity = width - rank_binary(matrix)
    if nullity not in (0, 1):
        raise ArithmeticError('unexpected binary quadratic defect')
    record = {'a': a, 'n': a + 1, 'matrix_size': width, 'nullity': nullity}
    if nullity:
        vector = base.kernel_vector(matrix, 2)
        record['kernel_polynomials'] = [base.polynomial(vector[j * a:(j + 1) * a], 2)
                                        for j in range(a + 2)]
        check_kernel_polynomials(matrix, a, record['kernel_polynomials'])
    return record


def source_control(a, coefficients):
    if a < 3:
        raise ValueError('literal degree-two source controls require a>=3')
    record = kernel_record(a, coefficients)
    source_rank = rank_binary(base.source_matrix(a, a, triple(coefficients)))
    if source_rank != a * (a + 2) - record['nullity']:
        raise ArithmeticError('literal source rank disagrees with recurrence defect')
    record['literal_source_rank'] = source_rank
    return record


def cohomology_controls(orbit_records):
    result = []
    for index, orbit in enumerate(orbit_records):
        controls = [kernel_record(n - 1, orbit['representative']) for n in (2, 3)]
        # The n=4,5 matrices were already computed with the a=3,4 sources.
        controls.extend({key: value for key, value in record.items() if key != 'literal_source_rank'}
                        for record in orbit['source_controls'] if record['n'] in (4, 5))
        nonzero = [control['n'] for control in controls if control['nullity']]
        if not nonzero:
            raise ArithmeticError('no low-power cohomology kernel for this orbit')
        power = min(nonzero)
        if any(record['nullity'] != int(record['n'] % power == 0)
               for record in orbit['source_controls']):
            raise ArithmeticError('finite source profile disagrees with the low-power certificate')
        result.append({'orbit': index, 'first_nonzero_power_checked': power,
                       'finite_profile_matches_divisibility': True,
                       'controls': controls})
    return result


def report():
    orbit_records = orbits()
    for orbit in orbit_records:
        orbit['size'] = len(orbit['members'])
        orbit['source_controls'] = [source_control(a, orbit['representative']) for a in SIZES]
    low_powers = cohomology_controls(orbit_records)
    orbit_counts = Counter(str(record['first_nonzero_power_checked']) for record in low_powers)
    candidate_counts = Counter()
    for orbit, record in zip(orbit_records, low_powers):
        candidate_counts[str(record['first_nonzero_power_checked'])] += orbit['size']
    witnesses = []
    for index, power in ((0, 2), (5, 3), (8, 5)):
        certificate = next(record for record in low_powers[index]['controls'] if record['n'] == power)
        if not certificate['nullity']:
            raise ArithmeticError('prime-power witness lost its kernel')
        witnesses.append({'power': power, 'coefficients': orbit_records[index]['representative'],
                          'certificate': certificate})
    return {
        'scope': 'Exact finite F2 orbit, source-rank and cohomology-kernel controls. '
                 'All-size torsion implications require the written geometric argument.',
        'coefficient_order': ['u0', 'u1', 'u2', 'v0', 'v1', 'v2', 'w0', 'w1', 'w2'],
        'candidate_count': sum(orbit['size'] for orbit in orbit_records),
        'orbit_count': len(orbit_records), 'coordinate_group_order': 36,
        'representative_transforms_checked': 36 * len(orbit_records),
        'source_sizes': SIZES,
        'previous_sizes_not_recomputed': [6, 10],
        'literal_source_comparisons': len(orbit_records) * len(SIZES),
        'additional_small_cohomology_matrices': 2 * len(orbit_records),
        'orbits': orbit_records,
        'cohomology_controls': low_powers,
        'first_nonzero_power_counts': {'orbits': dict(sorted(orbit_counts.items())),
                                       'candidate_triples': dict(sorted(candidate_counts.items()))},
        'prime_order_witnesses': witnesses,
        'cohomology_control_scope': 'Powers n=2,3,4,5; a=n-1. Small a is a cohomology '
                                    'coefficient matrix only, not a source-rank claim.',
        'independent_review': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    payload = json.dumps(report(), indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    else:
        print(payload, end='')
