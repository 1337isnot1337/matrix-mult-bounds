"""Replay the scalar-extended spin-1 construction with Python integers."""

import argparse
from itertools import product
import json
from pathlib import Path


def source_points():
    return [((i * 3 + p + q) * 2 + s,
             (j * 2 + p) * 3 + r + s,
             ((i + j) * 2 + q) * 2 + r)
            for i, j, p, q, r, s in product(range(2), repeat=6)]


def tensor_image(maps, points):
    columns = []
    for matrix in maps:
        columns.append([[(i, matrix[i][j]) for i in range(9) if matrix[i][j]]
                        for j in range(len(matrix[0]))])
    image = [0] * 729
    for x, y, z in points:
        for (i, a), (j, b), (k, c) in product(columns[0][x], columns[1][y], columns[2][z]):
            image[(i * 9 + j) * 9 + k] += a * b * c
    return image


def expected_tensor(trace_correction=0):
    tensor = [0] * 729
    for i, j, k in product(range(3), repeat=3):
        x, y, z = 3 * i + j, 3 * j + k, 3 * k + i
        tensor[(x * 9 + y) * 9 + z] += 1
    if trace_correction:
        for i, j, k in product((0, 4, 8), repeat=3):
            tensor[(i * 9 + j) * 9 + k] += trace_correction
    return tensor


def verify_certificate(certificate):
    if certificate.get('source') != 'A(2,2) direct sum one scalar tensor':
        raise ValueError('The source must include the explicitly declared scalar summand')
    denominator = certificate['common_map_denominator']
    if not isinstance(denominator, int) or denominator <= 0:
        raise ValueError('The map denominator must be a positive integer')
    maps = [certificate['map_numerators'][name] for name in 'ABC']
    if any(len(matrix) != 9 or any(len(row) != 13 for row in matrix) for matrix in maps):
        raise ValueError('The complete maps must have shape 9 by 13')
    if any(type(value) is not int for matrix in maps for row in matrix for value in row):
        raise ValueError('All map numerators must be Python integers')
    points = source_points()
    if len(points) != 64 or len(set(points)) != 64:
        raise ArithmeticError('The full A22 support did not reconstruct correctly')
    factor = denominator ** 3
    extended = tensor_image(maps, points + [(12, 12, 12)])
    target = expected_tensor()
    if extended != [factor * v for v in target]:
        raise ArithmeticError('The extended-source tensor identity failed')
    base = tensor_image(maps, points)
    defect = expected_tensor(trace_correction=1)
    if base != [factor * v for v in defect]:
        raise ArithmeticError('The asserted trace-cube defect identity failed')
    return {'arithmetic': 'Python integers; denominator cubed cleared exactly',
            'source_points_checked': 65, 'target_coefficients_checked': 729,
            'extended_source_exact_M3_identity': True,
            'base_source_exact_M3_plus_trace_cube_identity': True,
            'nonzero_target_coefficients': sum(v != 0 for v in target),
            'original_source_exact_M3_identity': False,
            'new_exponent_established': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify_certificate(json.loads(args.certificate.read_text())), indent=2))


if __name__ == '__main__':
    main()
