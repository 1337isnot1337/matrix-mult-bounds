"""Standard-library full coefficient replay for the reduced endpoint corner."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from math import fsum, sqrt
from pathlib import Path


REPO = Path(__file__).resolve().parents[3]
SOURCE = REPO/'research/ai/2026-10-20-paired-construction/m1-endpoint-corner.json'


def source_terms():
    return json.loads(SOURCE.read_text())['corner_terms']


def contraction(maps):
    if len(maps) != 3 or any(any(len(row) != columns for row in matrix)
                             for matrix, columns in zip(maps, [16, 18, 18])):
        raise ValueError('Map dimensions do not match the stated reduced source.')
    shapes = list(map(len, maps))
    sparse = [[[(row, matrix[row][column]) for row in range(len(matrix)) if matrix[row][column]]
               for column in range(columns)]
              for matrix, columns in zip(maps, [16, 18, 18])]
    actual = [0]*(shapes[0]*shapes[1]*shapes[2])
    for a, b, c, coefficient in source_terms():
        for (i, x), (j, y), (k, z) in product(sparse[0][a], sparse[1][b], sparse[2][c]):
            actual[(i*shapes[1]+j)*shapes[2]+k] += coefficient*x*y*z
    return actual


def target(outer, pairs):
    long = 4*outer
    result = [0]*(len(pairs)*long*long)
    for row, (i, k) in enumerate(pairs):
        for j in range(4):
            result[(row*long+4*i+j)*long+outer*j+k] = 1
    return result


def positive_control():
    """The six independent endpoint products give an exact M(3,4,3)."""
    inverse = [[0]*7 for _ in range(6)]
    for row, column, value in [(0, 0, 1), (1, 5, -1), (2, 1, 1),
                               (3, 3, 1), (4, 2, 1), (4, 5, 1), (5, 4, 1)]:
        inverse[row][column] = value
    maps = [[[0]*columns for _ in range(rows)] for rows, columns in [(9, 16), (12, 18), (12, 18)]]
    pairs = list(product(range(3), repeat=2))
    for row, (i, k) in enumerate(pairs):
        maps[0][row][4*k+i] = 1
    for i, y, v, s in product(range(3), range(2), range(2), range(7)):
        maps[1][4*i+2*y+v][7*y+s] = inverse[2*i+v][s]
    for k, y, v, s in product(range(3), range(2), range(2), range(7)):
        maps[2][3*(2*y+v)+k][2*s+v] = inverse[2*k+y][s]
    actual, wanted = contraction(maps), target(3, pairs)
    if actual != wanted:
        raise ArithmeticError('The exact reduced-corner M(3,4,3) control failed.')
    damaged = deepcopy(maps)
    damaged[0][0][0] *= -1
    differences = sum(a != b for a, b in zip(contraction(damaged), wanted))
    if differences != 4:
        raise ArithmeticError('The deliberately damaged A map was not detected.')
    return {'source': 'R16x18x18', 'target': 'M(3,4,3)',
            'source_terms_checked': 90, 'all_coefficient_positions_checked': 1296,
            'nonzero_target_positions': 36, 'integer_control_passes': True,
            'deliberate_A_sign_error_positions': differences,
            'auxiliary_rank': 0, 'improves_omega': False}


def replay(path):
    raw = Path(path).read_bytes()
    point = json.loads(raw)
    if point.get('auxiliary_rank') != 0 or point.get('exact_coefficient_certificate') is not False:
        raise ValueError('This artifact must be a zero-auxiliary numerical search.')
    pairs = [(i, k) for i, k in product(range(4), repeat=2) if i != k]
    if point['target_A_pairs'] != [list(pair) for pair in pairs]:
        raise ValueError('The target A-coordinate convention changed.')
    maps = [[[complex(r, i) for r, i in zip(rr, ii)] for rr, ii in zip(rm, im)]
            for rm, im in zip(point['maps_real'], point['maps_imag'])]
    if list(map(len, maps)) != [12, 16, 16]:
        raise ValueError('The target format changed.')
    actual, wanted = contraction(maps), target(4, pairs)
    error = [a-b for a, b in zip(actual, wanted)]
    residual = sqrt(fsum(abs(x)**2 for x in error)/48)
    difference = abs(residual-point['relative_full_coefficient_error'])
    if difference > 1e-10:
        raise ArithmeticError('The saved complete coefficient error did not replay.')
    return {'artifact': Path(path).name, 'artifact_sha256': sha256(raw).hexdigest(),
            'source_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
            'all_source_terms_reconstructed': 90,
            'all_target_coefficient_positions_checked': 3072,
            'nonzero_target_coefficients': 48, 'auxiliary_rank': 0,
            'relative_full_coefficient_error': residual,
            'maximum_coefficient_error': max(map(abs, error)),
            'reported_residual_difference': difference,
            'map_norms': [sqrt(fsum(abs(x)**2 for row in matrix for x in row)) for matrix in maps],
            'numerical_replay_passes': True, 'exact_coefficient_certificate': False,
            'nonexistence_proved': False, 'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoint', type=Path, nargs='?')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = {'control': positive_control()}
    if args.checkpoint:
        report['replay'] = replay(args.checkpoint)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
