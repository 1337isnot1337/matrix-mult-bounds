"""Full exact replay of explicit rational C(5,10) -> T4 Laurent maps."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json


def rank(matrix):
    matrix = [row.copy() for row in matrix]
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(pivot_row, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry/value for entry in matrix[pivot_row]]
        for i in range(pivot_row+1, len(matrix)):
            value = matrix[i][column]
            matrix[i] = [a-value*b for a, b in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            return pivot_row
    return pivot_row


def verify(data):
    assert data['source'] == 'C(5,10)' and data['target'] == 'T4'
    a_map, y_map, z_map = [[[Fraction(v) for v in row] for row in data[key]]
                         for key in ('a_map', 'y', 'z')]
    for matrix, rows, cols in ((a_map, 4, 5), (y_map, 10, 10), (z_map, 10, 14)):
        assert len(matrix) == rows and all(len(row) == cols for row in matrix)
    nodes = [(a, degree-a) for degree in range(4) for a in range(degree+1)]
    yw = [max(0, sum(node)-1) for node in nodes]
    zw = [-max(0, 2-sum(node)) for node in nodes]
    assert data['y_weights'] == yw and data['z_weights'] == zw
    # Accumulate the original 50 source monomials directly in target coordinates.
    tensor = [[[Fraction(0) for _ in range(10)] for _ in range(10)] for _ in range(4)]
    for i in range(5):
        for j in range(10):
            for x, y, z in product(range(4), range(10), range(10)):
                tensor[x][y][z] += a_map[x][i]*y_map[y][j]*z_map[z][i+j]
    negative = constant = 0
    target_terms, remainder = [], []
    natural_positions = 0
    for x, y, z in product(range(4), range(10), range(10)):
        a, b = nodes[y]
        c, d = nodes[z]
        desired = int(a+b+c+d == 3 and x == a+c)
        coefficient = tensor[x][y][z]
        weight = yw[y]+zw[z]
        if weight < 0:
            negative += 1
            assert coefficient == 0
        elif weight == 0:
            constant += 1
            assert coefficient == desired
            if coefficient:
                target_terms.append([x, y, z, 1])
        elif coefficient:
            remainder.append([x, y, z, weight, str(coefficient)])
        if a+b+c+d <= 3:
            assert weight <= 0 and coefficient == desired
            natural_positions += 1
    assert negative == 48 and constant == 124 and len(target_terms) == 20
    assert remainder == data['remainder'] and len(remainder) == 228
    assert natural_positions == 140
    ranks = [rank(matrix) for matrix in (a_map, y_map, z_map)]
    assert ranks == [4, 10, 10]
    assert all(row[2] == 0 for row in a_map)
    return {
        'status': 'explicit rational full-source coefficient replay passed',
        'source': 'C(5,10)', 'source_dimensions': [5, 10, 14],
        'target': 'canonical T4', 'target_dimensions': [4, 10, 10],
        'coefficient_field': 'rational numbers; hence every characteristic-zero field',
        'source_monomials': 50, 'target_coefficient_positions': 400,
        'negative_coefficients_checked': negative,
        'constant_coefficients_checked': constant,
        'nonzero_target_coefficients': len(target_terms),
        'nonzero_positive_remainder_coefficients': len(remainder),
        'maximum_remainder_degree': max(row[3] for row in remainder),
        'natural_degree_constraints_checked': natural_positions,
        'map_ranks': ranks, 'shared_monomial_2_omitted': True,
        'verifier_uses_only_standard_library': True,
        'external_mathematical_review': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raw = args.witness.read_bytes()
    report = verify(json.loads(raw))
    report['witness_sha256'] = hashlib.sha256(raw).hexdigest()
    content = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.write_text(content)
    print(content)
