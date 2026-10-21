"""Independent rational replay of the five- and six-sector degenerations."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json
from math import comb


def rank(matrix):
    work = [row.copy() for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next((row for row in range(pivot_row, len(work))
                      if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        value = work[pivot_row][column]
        work[pivot_row] = [entry/value for entry in work[pivot_row]]
        for row in range(pivot_row+1, len(work)):
            value = work[row][column]
            work[row] = [entry-value*base for entry, base
                         in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return pivot_row


def determinant(matrix):
    work = [row.copy() for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next((row for row in range(column, len(work))
                      if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result = -result
        value = work[column][column]
        result *= value
        for row in range(column+1, len(work)):
            multiplier = work[row][column]/value
            for j in range(column+1, len(work)):
                work[row][j] -= multiplier*work[column][j]
            work[row][column] = Fraction(0)
    return result


def matrix_from(data, key, rows, columns):
    values = data[key]
    assert len(values) == rows and all(len(row) == columns for row in values)
    return [[Fraction(value) for value in row] for row in values]


def verify(data):
    if data['source'] == 'C(6,20)':
        m, a_source, b_source = 5, 6, 20
        assert data['target'] == 'm5 degree sectors with separate invertible shared maps'
    else:
        assert data['source'] == [7, 28] and data['target_m'] == 6
        m, a_source, b_source = 6, 7, 28
    size = m*(m+1)//2
    a_map = matrix_from(data, 'a_map', m, a_source)
    y_map = matrix_from(data, 'y', size, b_source)
    z_map = matrix_from(data, 'z', size, a_source+b_source-1)
    assert len(data['shared_sector_maps']) == m
    blocks = [matrix_from({'block': values}, 'block', m, m)
              for values in data['shared_sector_maps']]
    block_determinants = [determinant(block) for block in blocks]
    assert all(block_determinants)
    assert [str(value) for value in block_determinants] == data['shared_sector_determinants']
    degrees = list(range(m))
    nodes = [(a, degree-a) for degree in degrees for a in range(degree+1)]
    if m == 5:
        assert data['y_degree_weights'] == [degree-2 for degree in degrees]
        assert data['z_degree_weights'] == [degree-2 for degree in degrees]
    else:
        assert data['y_weights'] == [sum(node) for node in nodes]
        assert data['z_weights'] == [sum(node)-(m-1) for node in nodes]

    # This replay does not use the moment functional, the construction's
    # nullspaces, or its Hankel/pencil identities. It substitutes directly
    # into each original convolution monomial.
    tensor = [[[Fraction(0) for _ in range(size)] for _ in range(size)] for _ in range(m)]
    for i in range(a_source):
        for j in range(b_source):
            for x in range(m):
                if not a_map[x][i]:
                    continue
                for y in range(size):
                    value = a_map[x][i]*y_map[y][j]
                    if not value:
                        continue
                    for z in range(size):
                        tensor[x][y][z] += value*z_map[z][i+j]

    negative = constant = nonzero_constant = positive_nonzero = 0
    remainder_counts = {degree: 0 for degree in range(1, m)}
    retained_per_sector = [0]*m
    for x, y, z in product(range(m), range(size), range(size)):
        a, b = nodes[y]
        c, d = nodes[z]
        exponent = a+b+c+d-(m-1)
        coefficient = tensor[x][y][z]
        if exponent < 0:
            assert coefficient == 0, ('negative', x, y, z, coefficient)
            negative += 1
        elif exponent == 0:
            expected = blocks[a+b][x][a+c]
            assert coefficient == expected, ('constant', x, y, z, coefficient, expected)
            constant += 1
            nonzero_constant += bool(coefficient)
            retained_per_sector[a+b] += 1
        elif coefficient:
            positive_nonzero += 1
            remainder_counts[exponent] += 1
    assert negative == m*comb(m+2, 4) and constant == m*comb(m+2, 3)
    assert negative+constant == data['nonpositive_coefficients_checked']
    assert retained_per_sector == [m*(p+1)*(m-p) for p in range(m)]
    map_ranks = [rank(matrix) for matrix in (a_map, y_map, z_map)]
    assert map_ranks == [m, size, size]
    return {
        'status': 'exact full-source rational coefficient replay passed',
        'source': f'C({a_source},{b_source})',
        'source_dimensions': [a_source, b_source, a_source+b_source-1],
        'target': f'{m} matched convolution sectors with independent shared bases',
        'target_dimensions': [m, size, size],
        'coefficient_field': 'rational numbers; hence every characteristic-zero field',
        'source_monomials': a_source*b_source, 'target_coefficient_positions': m*size*size,
        'negative_coefficients_checked': negative,
        'constant_coefficients_checked': constant,
        'nonzero_constant_coefficients': nonzero_constant,
        'constant_positions_per_sector': retained_per_sector,
        'nonzero_positive_remainder_coefficients': positive_nonzero,
        'nonzero_remainder_coefficients_by_degree': {str(key): value
                                                   for key, value in remainder_counts.items()},
        'shared_sector_determinants': [str(value) for value in block_determinants],
        'map_ranks': map_ranks,
        'verifier_uses_only_standard_library': True,
        'unbounded_family_constructed': False,
        'external_mathematical_review': False,
        'improves_omega': False,
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
