"""Exact fixed-corner scope and finite long-map frontier at Q(6,4).

Only standard-library arithmetic is used. Modular minors supply lower
bounds over Q; a small modular rank is never lifted to a Q upper bound.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json


PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
PRIME = 32003
SPEC = importlib.util.spec_from_file_location(
    'oblique_frontier_exact', PACKAGE.parent/'2026-10-23-oblique-paired-repair'/'exact.py')
EXACT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXACT)
GOOD_B = list(range(16))
GOOD_C = [5*alpha+j for alpha in range(4) for j in range(4)]


def matrix_inverse(matrix, prime=None):
    field = EXACT.Field(prime)
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError('Expected a square matrix')
    a = [[field.number(x) for x in row] + [field.number(int(i == j)) for j in range(size)]
         for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((i for i in range(column, size) if a[i][column]), None)
        if pivot is None:
            raise ArithmeticError('Singular product decoder')
        a[column], a[pivot] = a[pivot], a[column]
        inverse = field.inverse(a[column][column])
        a[column] = [field.reduce(x*inverse) for x in a[column]]
        for i in range(size):
            if i != column and a[i][column]:
                value = a[i][column]
                a[i] = [field.reduce(x-value*y) for x, y in zip(a[i], a[column])]
    return [row[size:] for row in a]


def determinant(matrix, prime=None):
    field = EXACT.Field(prime)
    a = [[field.number(x) for x in row] for row in matrix]
    if any(len(row) != len(a) for row in a):
        raise ValueError('Expected a square minor')
    result = field.number(1)
    for column in range(len(a)):
        pivot = next((i for i in range(column, len(a)) if a[i][column]), None)
        if pivot is None:
            return field.number(0)
        if pivot != column:
            a[pivot], a[column] = a[column], a[pivot]
            result = -result
        value = a[column][column]
        result = field.reduce(result*value)
        inverse = field.inverse(value)
        for i in range(column+1, len(a)):
            scale = field.reduce(a[i][column]*inverse)
            if scale:
                for j in range(column+1, len(a)):
                    a[i][j] = field.reduce(a[i][j]-scale*a[column][j])
            a[i][column] = 0
    return field.reduce(result)


def benchmark_maps():
    """Integer extension of (t,t2,t3,1-t4) by t5, with full long ranks."""
    outer = [[0]*6 for _ in range(5)]
    for i in range(3):
        outer[i][i+1] = 1
    outer[3][0], outer[3][4], outer[4][5] = 1, -1, 1
    w = [[int(y == 0) for y in range(4)], [int(y == 3) for y in range(4)]]
    products = [[0]*9 for _ in range(10)]
    for i, v, q, y in product(range(5), range(2), range(6), range(4)):
        products[2*i+v][q+y] += outer[i][q]*w[v][y]
    dual = [[0]*9 for _ in range(10)]
    for row, column, value in ((0, 1, 1), (1, 0, 1), (1, 4, 1), (2, 2, 1),
                               (3, 5, 1), (4, 3, 1), (4, 7, 1), (5, 6, 1),
                               (6, 0, 1), (7, 7, -1), (9, 8, 1)):
        dual[row][column] = value
    for selected in range(10):
        if selected != 8 and [sum(x*y for x, y in zip(row, products[selected])) for row in dual] != [
                int(i == selected) for i in range(10)]:
            raise ArithmeticError('Integer selected-product decoder failed')
    first = [[outer[j][p]*outer[i][q] for p, q in product(range(6), repeat=2)]
             for i, j in product(range(5), repeat=2)]
    second, third = [[0]*36 for _ in range(20)], [[0]*36 for _ in range(20)]
    for i, a, v, y, z in product(range(5), range(2), range(2), range(4), range(9)):
        second[4*i+2*a+v][9*y+z] = w[a][y]*dual[2*i+v][z]
    for a, v, j, z, vv in product(range(2), range(2), range(5), range(9), range(4)):
        third[5*(2*a+v)+j][4*z+vv] = dual[2*j+a][z]*w[v][vv]
    second[16][17], second[18][26] = 1, 1
    third[4][33], third[9][34] = 1, 1
    return [first, second, third]


def sparse_slices(second, third, prime=PRIME):
    """Contract all 576 native terms, keeping all 36 first coordinates."""
    field = EXACT.Field(prime)
    columns = [EXACT.sparse_columns([[field.number(x) for x in row] for row in matrix])
               for matrix in (second, third)]
    output = [defaultdict(int) for _ in range(36)]
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        for (ib, cb), (ic, cc) in product(columns[0][9*y+q+v], columns[1][4*(p+y)+v]):
            column = ib*len(third)+ic
            output[6*p+q][column] = field.reduce(output[6*p+q][column]+cb*cc)
    return [{k: v for k, v in row.items() if v} for row in output]


def rank_minor(rows, prime=PRIME, stop=None):
    """Sparse echelon search; retain original row indices for a rank minor."""
    basis, columns, selected = {}, [], []
    for index, original in enumerate(rows):
        row = {k: int(v) % prime for k, v in original.items() if int(v) % prime}
        while row:
            pivot = min(row)
            if pivot not in basis:
                inverse = pow(row[pivot], -1, prime)
                basis[pivot] = {k: value*inverse % prime for k, value in row.items()}
                columns.append(pivot)
                selected.append(index)
                break
            scale = row[pivot]
            for k, value in basis[pivot].items():
                updated = (row.get(k, 0)-scale*value) % prime
                if updated:
                    row[k] = updated
                else:
                    row.pop(k, None)
        if len(selected) == stop:
            break
    minor = [[rows[i].get(j, 0) for j in columns] for i in selected]
    return {'rows': selected, 'columns': columns,
            'determinant_mod_prime': determinant(minor, prime)}


def check_minor(rows, record, size, prime=PRIME):
    rr, cc = record['rows'], record['columns']
    if (len(rr) != size or len(cc) != size or len(set(rr)) != size or len(set(cc)) != size
            or any(type(i) is not int or not 0 <= i < len(rows) for i in rr)
            or any(type(j) is not int or j < 0 for j in cc)):
        raise ArithmeticError('Malformed rank minor')
    value = determinant([[rows[i].get(j, 0) for j in cc] for i in rr], prime)
    if value == 0 or value != record['determinant_mod_prime']:
        raise ArithmeticError('Nonzero modular rank minor failed')
    return True


def quotient_by_target(rows):
    """Delete one pivot from each of the 25 disjoint target slice rows."""
    output = []
    for original in rows:
        row = original.copy()
        for i, j in product(range(5), repeat=2):
            coefficient = row.pop(80*i+j, 0)
            if coefficient:
                for alpha in range(1, 4):
                    column = (4*i+alpha)*20+5*alpha+j
                    value = (row.get(column, 0)-coefficient) % PRIME
                    if value:
                        row[column] = value
                    else:
                        row.pop(column, None)
        output.append(row)
    return output


def shift_grid():
    return [(a, b, sb, sc, lb, lc, transpose_c)
            for a, b in product(range(4), repeat=2) if a != b
            for sb, sc, lb, lc, transpose_c in product((-1, 1), (-1, 1), (-1, 1), (-1, 1), (0, 1))]


def shifted_maps(parameters):
    if (len(parameters) != 7 or any(type(x) is not int for x in parameters)
            or tuple(parameters) not in shift_grid()):
        raise ValueError('Parameters are outside the registered finite shift grid')
    a, b, sb, sc, lb, lc, transpose_c = parameters
    maps = benchmark_maps()
    old_b, old_c = [row[:] for row in maps[1]], [row[:] for row in maps[2]]
    ca, cb = (b, a) if transpose_c else (a, b)
    for outer, y, z in product(range(5), range(4), range(9)):
        if 0 <= z+sb < 9:
            maps[1][4*outer+a][9*y+z] += lb*old_b[4*outer+b][9*y+z+sb]
        if 0 <= z+sc < 9:
            maps[2][5*ca+outer][4*z+y] += lc*old_c[5*cb+outer][4*(z+sc)+y]
    return maps


def corner_products(parameters):
    if len(parameters) != 4 or any(type(x) is not int or x not in (-1, 0, 1) for x in parameters):
        raise ValueError('Parameters are outside the registered mixed-corner grid')
    a, b, c, d = parameters
    u = [[0]*6 for _ in range(4)]
    for i in range(3):
        u[i][i+1] = 1
    u[3][0], u[3][4] = 1, -1
    h = [[[0]*2 for _ in range(4)] for _ in range(4)]
    h[0][0][0] = h[1][0][1] = h[2][3][0] = h[3][3][1] = 1
    h[1][1][0], h[1][2][0], h[2][1][1], h[2][2][1] = a, b, c, d
    db, dc = [[0]*8 for _ in range(8)], [[0]*16 for _ in range(16)]
    for i, v, q in product(range(4), range(2), range(5)):
        db[2*i+v][q+3*v] += u[i][q]
    for i, alpha, p, y, v in product(range(4), range(4), range(5), range(4), range(2)):
        dc[4*i+alpha][2*(p+y)+v] += u[i][p]*h[alpha][y][v]
    return u, h, db, dc


def mixed_corner_maps(parameters, prime=PRIME):
    u, h, db, dc = corner_products(parameters)
    field = EXACT.Field(prime)
    lb, lc = [matrix_inverse(list(map(list, zip(*matrix))), prime) for matrix in (db, dc)]
    first = [[u[j][p]*u[i][q] for p, q in product(range(6), repeat=2)]
             for i, j in product(range(4), repeat=2)]
    second, third = [[0]*36 for _ in range(16)], [[0]*36 for _ in range(16)]
    for i, alpha, y, z, v in product(range(4), range(4), range(4), range(8), range(2)):
        second[4*i+alpha][9*y+z] = field.reduce(second[4*i+alpha][9*y+z]+h[alpha][y][v]*lb[2*i+v][z])
    for alpha, j, z, v in product(range(4), range(4), range(8), range(2)):
        third[4*alpha+j][4*z+3*v] = lc[4*j+alpha][2*z+v]
    return [first, second, third]


def check_corner_identity(maps, rows):
    for a, weights in enumerate(maps[0]):
        actual = defaultdict(int)
        for weight, row in zip(weights, rows):
            if weight:
                for column, value in row.items():
                    actual[column] = (actual[column]+weight*value) % PRIME
        actual = {k: v for k, v in actual.items() if v}
        i, j = divmod(a, 4)
        expected = {(4*i+alpha)*16+4*alpha+j: 1 for alpha in range(4)}
        if actual != expected:
            raise ArithmeticError('Complete native M4 corner identity failed')
    return True


def fixed_good_certificate():
    maps = benchmark_maps()
    b, c = [maps[1][i] for i in GOOD_B], [maps[2][i] for i in GOOD_C]
    projected = EXACT.source_slices(6, 4, (4, 4, 4), b, c)
    # These select the six forms x0,x1,x2,x3,x0+x4,x5 on both factors.
    b_rows, c_rows = [12, 0, 4, 8, 1, 5], [3, 0, 1, 2, 8, 9]
    columns = [16*b_rows[v]+c_rows[u] for u, v in product(range(6), repeat=2)]
    one_factor = [[int(i == j)+int(i == 4 and j == 0) for j in range(6)] for i in range(6)]
    minor = [[row[j] for j in columns] for row in projected]
    expected = [[one_factor[u][p]*one_factor[v][q] for u, v in product(range(6), repeat=2)]
                for p, q in product(range(6), repeat=2)]
    value = determinant(minor)
    if minor != expected or value != 1:
        raise ArithmeticError('Expected the determinant-one fixed projection minor')
    report = EXACT.verify(6, 4, (5, 4, 5), maps, include_witness=False)
    image, _ = EXACT.contract(6, 4, (5, 4, 5), maps)
    residual = EXACT.subtract(EXACT.matrix_multiplication((5, 4, 5)), image, EXACT.Field())
    if any(a//5 < 4 and a % 5 < 4 for a, _, _ in residual):
        raise ArithmeticError('Benchmark residual leaves the nine bad first coordinates')
    _, optimum = EXACT.minimum_first_residual(6, 4, (5, 4, 5), maps[1], maps[2])
    long_minors = []
    for matrix in maps[1:]:
        rank_long, cols, _ = EXACT.row_space(matrix)
        det_long = determinant([[row[j] for j in cols] for row in matrix])
        if rank_long != 20 or abs(det_long) != 1:
            raise ArithmeticError('Benchmark long map is not integrally surjective')
        long_minors.append({'columns': cols, 'determinant': det_long})
    return EXACT.encode({
        'fixed_good_B_rows': GOOD_B, 'fixed_good_C_rows': GOOD_C,
        'projected_source_shape': [36, 256], 'unit_minor_columns': columns,
        'one_factor_unit_minor': one_factor,
        'unit_minor_determinant': value, 'projected_target_dimension': 16,
        'arbitrary_filler_first_residual_lower_bound': 9,
        'arbitrary_filler_equality_claimed': False,
        'benchmark': {'long_map_unit_minors': long_minors,
                      'minimum_first_map_report': optimum,
                      'given_first_map_residual_supported_on_nine_bad_coordinates': True,
                      'native_verification': report}})


def verify_fixed_good(record):
    if record != fixed_good_certificate():
        raise ArithmeticError('Fixed-good-row certificate does not replay')
    return True


def check_shift_record(record):
    maps = shifted_maps(record['parameters'])
    rows = quotient_by_target(sparse_slices(maps[1], maps[2]))
    return check_minor(rows, record['minor'], 20)


def check_corner_record(record):
    _, _, _, dc = corner_products(record['parameters'])
    dc_det = determinant(dc, PRIME)
    if record['status'] == 'singular_decoder_mod_prime':
        if dc_det != 0:
            raise ArithmeticError('False singular-decoder record')
        return True
    if record['status'] != 'exact_corner_and_injective' or dc_det == 0:
        raise ArithmeticError('Invalid mixed-corner status')
    if dc_det != record['decoder_determinant_mod_prime']:
        raise ArithmeticError('Mixed-corner decoder determinant changed')
    maps = mixed_corner_maps(record['parameters'])
    rows = sparse_slices(maps[1], maps[2])
    check_corner_identity(maps, rows)
    return check_minor(rows, record['minor'], 36)


def verify_sources(repository=ROOT, manifest=None):
    if manifest is None:
        manifest = json.loads((PACKAGE/'sources.json').read_text())
    for record in manifest['local_sources']:
        actual = hashlib.sha256((Path(repository)/record['path']).read_bytes()).hexdigest()
        if actual != record['sha256']:
            raise ArithmeticError('Pinned source hash changed: '+record['path'])
    return {'checked': len(manifest['local_sources']), 'all_match': True}


def build_certificate():
    shifts = []
    for parameters in shift_grid():
        maps = shifted_maps(parameters)
        rows = quotient_by_target(sparse_slices(maps[1], maps[2]))
        minor = rank_minor(rows, stop=20)
        if len(minor['rows']) != 20:
            raise ArithmeticError('A shift candidate survived; exact follow-up is required')
        shifts.append({'parameters': list(parameters), 'minor': minor})
    corners = []
    for parameters in product((-1, 0, 1), repeat=4):
        _, _, _, dc = corner_products(parameters)
        value = determinant(dc, PRIME)
        if not value:
            corners.append({'parameters': list(parameters), 'status': 'singular_decoder_mod_prime'})
            continue
        maps = mixed_corner_maps(parameters)
        rows = sparse_slices(maps[1], maps[2])
        check_corner_identity(maps, rows)
        minor = rank_minor(rows)
        if len(minor['rows']) != 36:
            raise ArithmeticError('A mixed corner lost injectivity; exact follow-up is required')
        corners.append({'parameters': list(parameters), 'status': 'exact_corner_and_injective',
                        'decoder_determinant_mod_prime': value, 'minor': minor})
    return {'schema': 1, 'source': [6, 4], 'target': [5, 4, 5], 'modulus': PRIME,
            'source_pin_verification': verify_sources(), 'fixed_good_rows': fixed_good_certificate(),
            'shift_controls': shifts, 'mixed_corner_controls': corners,
            'coverage': {'shift_candidates': 384, 'mixed_corner_candidates': 81,
                         'nonsingular_mixed_corners': 61, 'singular_modular_decoders': 20},
            'first_map_unrestricted_in_rank_bounds': True,
            'unrestricted_long_map_obstruction_claimed': False,
            'historical_novelty_claimed': False, 'improves_omega': False}


def verify_certificate(report):
    if (report.get('schema') != 1 or report.get('source') != [6, 4]
            or report.get('target') != [5, 4, 5] or report.get('modulus') != PRIME):
        raise ArithmeticError('Wrong certificate format or field')
    if [tuple(x['parameters']) for x in report['shift_controls']] != shift_grid():
        raise ArithmeticError('Incomplete or changed shift grid')
    if [tuple(x['parameters']) for x in report['mixed_corner_controls']] != list(product((-1, 0, 1), repeat=4)):
        raise ArithmeticError('Incomplete or changed mixed-corner grid')
    verify_fixed_good(report['fixed_good_rows'])
    if report['source_pin_verification'] != verify_sources():
        raise ArithmeticError('Source-pin receipt changed')
    for record in report['shift_controls']:
        check_shift_record(record)
    for record in report['mixed_corner_controls']:
        check_corner_record(record)
    expected = {'shift_candidates': 384, 'mixed_corner_candidates': 81,
                'nonsingular_mixed_corners': 61, 'singular_modular_decoders': 20}
    if (report['coverage'] != expected
            or sum(r['status'] == 'exact_corner_and_injective' for r in report['mixed_corner_controls']) != 61
            or report['first_map_unrestricted_in_rank_bounds'] is not True
            or any(report[key] is not False for key in ('unrestricted_long_map_obstruction_claimed',
                                                        'historical_novelty_claimed', 'improves_omega'))):
        raise ArithmeticError('Certificate scope or coverage changed')
    return {'unit_minor_replayed': True, **expected,
            'all_native_corner_identities_and_minors_replayed': True}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', type=Path)
    parser.add_argument('--check', type=Path, default=PACKAGE/'certificate.json')
    args = parser.parse_args()
    if args.write:
        report = build_certificate()
        args.write.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    else:
        report = json.loads(args.check.read_text())
    print(json.dumps(verify_certificate(report), indent=2))
