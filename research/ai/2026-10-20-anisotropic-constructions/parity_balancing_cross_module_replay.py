"""Independent integer replay of a rational crossed convolution module.

Accepted input uses sparse Y_map/Z_map entries [row,column,numerator,denominator].
All target coefficients, including zeros, are checked in the reduced
source and after explicit lifts to A(4,8) and A(8,8). Stored result metadata is
not used for acceptance.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import json
from math import lcm
from pathlib import Path


def parse_map(entries, rows, columns):
    if not isinstance(entries, list):
        raise ArithmeticError('An exported map must be a sparse list')
    seen, rational = set(), []
    denominator = 1
    for item in entries:
        if not isinstance(item, list) or len(item) != 4 or any(type(x) is not int for x in item):
            raise ArithmeticError('A rational map entry needs four integers')
        row, column, numerator, divisor = item
        if not (0 <= row < rows and 0 <= column < columns and numerator and divisor > 0):
            raise ArithmeticError('Invalid rational map coordinate or denominator')
        if (row, column) in seen:
            raise ArithmeticError('Repeated rational map coordinate')
        seen.add((row, column))
        value = Fraction(numerator, divisor)
        rational.append((row, column, value))
        denominator = lcm(denominator, value.denominator)
    scaled = [(row, column, value.numerator * (denominator // value.denominator))
              for row, column, value in rational]
    return scaled, denominator


def inverse_map(entries):
    result = defaultdict(list)
    for row, column, value in entries:
        result[column].append((row, value))
    return result


def reduced_replay(y, z, scale, r):
    yy, zz = inverse_map(y), inverse_map(z)
    actual = Counter()
    for i, u, a, j in product(range(2), range(2), range(4), range(8)):
        x, cy, cz = 2 * i + u, 8 * (a + u) + j, 9 * a + j + i
        for (row_y, value_y), (row_z, value_z) in product(yy[cy], zz[cz]):
            actual[x, row_y, row_z] += value_y * value_z
    actual = {point: value for point, value in actual.items() if value}
    expected = {(2 * i + u, r * u + alpha, r * i + alpha): scale
                for i, u, alpha in product(range(2), range(2), range(r))}
    if actual != expected:
        errors = sum(actual.get(point, 0) != expected.get(point, 0)
                     for point in actual.keys() | expected.keys())
        raise ArithmeticError(f'The complete reduced identity has {errors} incorrect coefficients')
    return {'source_terms_checked': 128, 'target_shape': [2, 2, r],
            'all_target_coefficients_checked': 16 * r * r,
            'nonzero_target_coefficients': 4 * r, 'all_other_coefficients_zero': True}


def coordinate(i, k, s, a, b):
    return ((a + b - 1) * i + k) * b + s


def lift_maps(y, z, r, copies):
    a, b = (4 if copies == 1 else 8), 8
    target_r = copies * r
    x_full = []
    for i, t, p, u in product(range(2), repeat=4):
        row = 4 * (2 * i + t) + 2 * p + u
        x_full.append((row, coordinate(i, 2 * p + t, copies * u, a, b), 1))
    y_full, z_full = [], []
    for row, column, value in y:
        u, alpha = divmod(row, r)
        ell, j = divmod(column, 8)
        for e, p in product(range(copies), range(2)):
            output_row = (2 * p + u) * target_r + e * r + alpha
            y_full.append((output_row, coordinate(2 * p, e + copies * ell, j, a, b), value))
    for row, column, value in z:
        i, alpha = divmod(row, r)
        aa, h = divmod(column, 9)
        for e, t in product(range(copies), range(2)):
            output_row = 4 * (e * r + alpha) + 2 * i + t
            z_full.append((output_row, coordinate(e + copies * aa, h, t, a, b), value))
    return x_full, y_full, z_full


def contract_full_maps(maps, scale, a, b, target_r):
    xx, yy, zz = [inverse_map(entries) for entries in maps]
    actual = Counter()
    term_count = 0
    for i, p, rr, j, q, s in product(range(a), range(a), range(a), range(b), range(b), range(b)):
        term_count += 1
        x = coordinate(i, p + q, s, a, b)
        cy = coordinate(p, rr + s, j, a, b)
        cz = coordinate(rr, i + j, q, a, b)
        for (rx, vx), (ry, vy), (rz, vz) in product(xx[x], yy[cy], zz[cz]):
            actual[rx, ry, rz] += vx * vy * vz
    actual = {point: value for point, value in actual.items() if value}
    expected = {(4 * left + right, target_r * right + alpha, 4 * alpha + left): scale
                for left, right, alpha in product(range(4), range(4), range(target_r))}
    if actual != expected:
        errors = sum(actual.get(point, 0) != expected.get(point, 0)
                     for point in actual.keys() | expected.keys())
        raise ArithmeticError(f'The full-source lift has {errors} incorrect coefficients')
    leg = a * b * (a + b - 1)
    return {'source': [a, b], 'source_terms_checked': term_count,
            'source_leg_dimensions': [leg] * 3,
            'target_shape': [4, 4, target_r], 'target_leg_dimensions': [16, 4 * target_r, 4 * target_r],
            'all_target_coefficients_checked': 256 * target_r * target_r,
            'nonzero_target_coefficients': 16 * target_r, 'all_other_coefficients_zero': True,
            'sparse_map_entries': [len(entries) for entries in maps]}


def full_replay(y, z, scale, r, copies):
    return contract_full_maps(lift_maps(y, z, r, copies), scale,
                              4 if copies == 1 else 8, 8, copies * r)


def read_reduced_maps(data):
    if 'Y_map' in data or 'Z_map' in data:
        r = data.get('middle_dimension', 9)
        y_entries, z_entries = data['Y_map'], data['Z_map']
    else:
        shapes = [data[name]['shape'] for name in ('Y', 'Z')]
        if any(not isinstance(shape, list) or len(shape) != 2 or
               any(type(entry) is not int for entry in shape) for shape in shapes):
            raise ArithmeticError('Invalid recorded map shape')
        if shapes[0][0] != shapes[1][0] or shapes[0][0] % 2 or shapes[0][1] != 40 or shapes[1][1] != 36:
            raise ArithmeticError('The exported reduced map shapes do not match')
        r = shapes[0][0] // 2
        exports = []
        for name in ('Y', 'Z'):
            denominator = data[name]['denominator']
            if type(denominator) is not int or denominator <= 0:
                raise ArithmeticError('A common map denominator must be a positive integer')
            entries = data[name]['entries']
            if not isinstance(entries, list) or any(not isinstance(entry, list) or len(entry) != 3 for entry in entries):
                raise ArithmeticError('Malformed sparse common-denominator map')
            exports.append([entry + [denominator] for entry in entries])
        y_entries, z_entries = exports
    if type(r) is not int or not 1 <= r <= 18:
        raise ArithmeticError('Invalid positive middle dimension')
    y, dy = parse_map(y_entries, 2 * r, 40)
    z, dz = parse_map(z_entries, 2 * r, 36)
    return y, z, dy, dz, r


def verify(data):
    y, z, dy, dz, r = read_reduced_maps(data)
    return {'arithmetic': 'Python integers after exact denominator clearing',
            'reduced_source': reduced_replay(y, z, dy * dz, r),
            'full_sources': [full_replay(y, z, dy * dz, r, copies) for copies in (1, 2)],
            'ordinary_module_constructed': True,
            'full_M27_plus_M7_constructed': False,
            'new_exponent_established': False,
            'external_independent_review': False}


def export_lifts(data):
    y, z, dy, dz, r = read_reduced_maps(data)
    constructions = []
    for copies in (1, 2):
        a, b = (4 if copies == 1 else 8), 8
        source_dimension = a * b * (a + b - 1)
        maps = lift_maps(y, z, r, copies)
        dimensions = [16, 4 * copies * r, 4 * copies * r]
        constructions.append({'source': [a, b], 'target_shape': [4, 4, copies * r],
                              'maps': [{'shape': [rows, source_dimension], 'denominator': denominator,
                                        'entries': [list(entry) for entry in entries]}
                                       for rows, denominator, entries in zip(dimensions, (1, dy, dz), maps)]})
    return {'middle_dimension': r, 'constructions': constructions,
            'arithmetic': 'exact rational sparse maps', 'new_exponent_established': False}


def verify_exported_lifts(data):
    r = data['middle_dimension']
    if type(r) is not int or not 1 <= r <= 18 or len(data['constructions']) != 2:
        raise ArithmeticError('Invalid full-source export dimensions')
    reports = []
    for copies, construction in enumerate(data['constructions'], 1):
        a, b = (4 if copies == 1 else 8), 8
        source_dimension = a * b * (a + b - 1)
        if construction['source'] != [a, b] or construction['target_shape'] != [4, 4, copies * r]:
            raise ArithmeticError('The full-source export has an incorrect source or target')
        entries = construction['maps']
        if not isinstance(entries, list) or len(entries) != 3:
            raise ArithmeticError('A full-source restriction needs three maps')
        maps, scale = [], 1
        for exported, rows in zip(entries, (16, 4 * copies * r, 4 * copies * r)):
            if exported['shape'] != [rows, source_dimension]:
                raise ArithmeticError('Incorrect full-source map shape')
            denominator = exported['denominator']
            if type(denominator) is not int or denominator <= 0:
                raise ArithmeticError('Invalid full-source denominator')
            actual, d = parse_map([item + [denominator] for item in exported['entries']], rows, source_dimension)
            maps.append(actual)
            scale *= d
        reports.append(contract_full_maps(maps, scale, a, b, copies * r))
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('witness', type=Path)
    parser.add_argument('--report', type=Path)
    parser.add_argument('--full-maps', type=Path)
    args = parser.parse_args()
    data = json.loads(args.witness.read_text())
    report = verify(data)
    if args.full_maps:
        exported = export_lifts(data)
        report['actual_exported_maps_replayed'] = verify_exported_lifts(exported)
        args.full_maps.write_text(json.dumps(exported, indent=2) + '\n')
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
