"""Regenerate finite response witnesses; acceptance is in spin_rectangle_budget.

The four full-channel Y-kernel vectors are recovered inside the published
seven-dimensional kernel after one channel was deleted.  Fraction arithmetic
is confined to that seven-column system.  No numerical dependency is used.
"""

from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import gcd, lcm

import spin_rectangle_budget as core


def pivot_minor(response, support):
    columns = sorted({column for row in response.values() for column in row})
    labels = sorted(support)
    matrix = [[response.get(row, {}).get(column, 0) % core.assembly.PRIME
               for column in columns] for row in labels]
    rank, selected_columns = 0, []
    prime = core.assembly.PRIME
    for j, column in enumerate(columns):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        labels[rank], labels[pivot] = labels[pivot], labels[rank]
        scale = pow(matrix[rank][j], -1, prime)
        matrix[rank] = [value * scale % prime for value in matrix[rank]]
        for i in range(rank + 1, len(matrix)):
            factor = matrix[i][j]
            if factor:
                matrix[i] = [(value - factor * base) % prime
                             for value, base in zip(matrix[i], matrix[rank])]
        selected_columns.append(column)
        rank += 1
        if rank == len(matrix):
            break
    return labels[:rank], selected_columns


def small_kernel(rows, width):
    basis = []
    pivots = []
    for raw in rows:
        row = [Fraction(value) for value in raw]
        for pivot, base in zip(pivots, basis):
            factor = row[pivot]
            if factor:
                row = [value - factor * item for value, item in zip(row, base)]
        pivot = next((j for j, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        factor = row[pivot]
        row = [value / factor for value in row]
        # Keep the pivot order increasing, and remove the new pivot upstairs.
        for i, base in enumerate(basis):
            factor = base[pivot]
            if factor:
                basis[i] = [value - factor * item for value, item in zip(base, row)]
        place = next((i for i, old in enumerate(pivots) if old > pivot), len(pivots))
        pivots.insert(place, pivot)
        basis.insert(place, row)
    result = []
    for free in range(width):
        if free in pivots:
            continue
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = 1
        for pivot, row in zip(pivots, basis):
            vector[pivot] = -row[free]
        result.append(vector)
    return result


def full_y_kernel(response, old_certificate):
    vectors = old_certificate['new_Y_against_saved_X_Z']['integer_kernel_vectors']
    images = []
    for vector in vectors:
        image = Counter()
        for column, value in vector:
            for output, coefficient in response.get(column, {}).items():
                image[output] += value * coefficient
        images.append(image)
    outputs = sorted(set().union(*(image.keys() for image in images)))
    coefficients = small_kernel([[image[output] for image in images] for output in outputs], len(vectors))
    result = []
    for combination in coefficients:
        vector = Counter()
        for factor, old in zip(combination, vectors):
            for column, value in old:
                vector[column] += factor * value
        denominator = lcm(*(value.denominator for value in vector.values()))
        integers = {column: int(value * denominator) for column, value in vector.items() if value}
        divisor = gcd(*integers.values())
        result.append([[column, value // divisor] for column, value in sorted(integers.items())])
    return result


def generate():
    maps, denominators = core.load_maps()
    first, pairs = core.assembly.first_response(maps[1], maps[2], 28)
    responses = (first, core.other_response(maps, 1), core.other_response(maps, 2))
    old = json.loads(core.assembly.CERTIFICATE.read_text())
    kernels = ([], full_y_kernel(responses[1], old), [])
    certificate = {'scope': 'Original full 28-channel spin maps, all three response ranks',
                   'prime': core.assembly.PRIME, 'new_exponent_established': False,
                   'reconstruction': 'Regenerated from published maps after local executor snapshot loss'}
    for leg, response, support, kernel in zip('XYZ', responses, core.response_supports(), kernels):
        if leg == 'X':
            rows = sorted(support)
            columns = old['disjoint_channel_minor_controls'][0]['columns']
        else:
            rows, columns = pivot_minor(response, support)
        certificate[leg] = {'rank': len(rows), 'support': sorted(support),
                            'minor_rows': rows, 'minor_columns': columns,
                            'integer_kernel_vectors': kernel}
    core.CERTIFICATE.write_text(json.dumps(certificate, indent=2) + '\n')
    report = core.verify(certificate=certificate)
    report['input_sha256'] = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                              for path in (core.FULL_MAPS, core.CERTIFICATE)}
    core.REPORT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'ranks': [certificate[leg]['rank'] for leg in 'XYZ'],
                      'kernel_vectors': [len(certificate[leg]['integer_kernel_vectors']) for leg in 'XYZ'],
                      'three_leg_budgets': report['three_leg_budgets']}))


if __name__ == '__main__':
    generate()
