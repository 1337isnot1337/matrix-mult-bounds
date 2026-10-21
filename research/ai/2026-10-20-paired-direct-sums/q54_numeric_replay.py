"""Replay every coefficient of the numerical Q(5,4) -> M4 candidate.

This standard-library calculation checks floating-point evidence.  It
never upgrades approximate maps to an exact tensor restriction.
"""
import argparse
from itertools import product
import json
from math import fsum, sqrt
from pathlib import Path


def contract(n, b, outer, maps):
    """Reconstruct the native paired convolution at all target positions."""
    source_shape = [n*n, b*(n+b-1), b*(n+b-1)]
    target_shape = [outer*outer, outer*b, b*outer]
    if any(len(maps[k]) != target_shape[k] or
           any(len(row) != source_shape[k] for row in maps[k]) for k in range(3)):
        raise ValueError('Map dimensions disagree with the declared tensors.')
    aa, bb, cc = target_shape
    coefficients = [0]*(aa*bb*cc)
    for p, q, y, v in product(range(n), range(n), range(b), range(b)):
        source_a = n*p+q
        source_b = y*(n+b-1)+q+v
        source_c = b*(p+y)+v
        for i in range(aa):
            a = maps[0][i][source_a]
            if not a:
                continue
            for j in range(bb):
                ab = a*maps[1][j][source_b]
                if not ab:
                    continue
                offset = (i*bb+j)*cc
                for k in range(cc):
                    coefficients[offset+k] += ab*maps[2][k][source_c]
    desired = [0]*len(coefficients)
    for i, j, k in product(range(outer), range(b), range(outer)):
        ia, ib, ic = outer*i+k, b*i+j, outer*j+k
        desired[(ia*bb+ib)*cc+ic] = 1
    return coefficients, desired


def integer_control():
    """A known P2=Q(2,2) restriction, checked using integers only."""
    maps = [[[0]*size for _ in range(4)] for size in (4, 6, 6)]
    for p, q in product(range(2), repeat=2):
        maps[0][2*q+p][2*p+q] = 1
    for source, target in enumerate((3, 0, 2, 1, 3, 0)):
        maps[1][target][source] = 1
    for source, (sign, target) in enumerate(((-1, 1), (1, 0), (1, 2),
                                            (1, 1), (1, 3), (-1, 2))):
        maps[2][target][source] = sign
    actual, expected = contract(2, 2, 2, maps)
    if actual != expected:
        raise ArithmeticError('The exact integer P2 control failed.')
    maps[2][1][0] *= -1
    corrupted, _ = contract(2, 2, 2, maps)
    if corrupted == expected:
        raise ArithmeticError('The deliberate sign error was not detected.')
    return {'all_integer_positions_checked': 64, 'exact_positive_control_passed': True,
            'deliberate_sign_error_detected': True}


def replay(path):
    point = json.loads(Path(path).read_text())
    if point.get('exact_coefficient_certificate') is not False:
        raise ValueError('This artifact must be explicitly labelled numerical.')
    n, b, outer = point['n'], point['b'], point['target_outer']
    maps = [[[complex(r, i) for r, i in zip(rr, ii)] for rr, ii in zip(real, imag)]
            for real, imag in zip(point['maps_real'], point['maps_imag'])]
    actual, desired = contract(n, b, outer, maps)
    differences = [value-target for value, target in zip(actual, desired)]
    relative = sqrt(fsum(abs(v)**2 for v in differences)/sum(desired))
    maximum = max(map(abs, differences))
    norms = [sqrt(fsum(abs(value)**2 for row in matrix for value in row)) for matrix in maps]
    saved = point['reported_relative_coefficient_error']
    # Summation orders differ from the NumPy discovery calculation.  This
    # checks consistency of the saved floating-point evidence, not exactness.
    if relative > 1e-12 or maximum > 1e-12 or abs(relative-saved) > 1e-12:
        raise ArithmeticError('The numerical candidate did not replay at its stated scale.')
    if any(abs(a-b) > 1e-11 for a, b in zip(norms, point['reported_map_frobenius_norms'])):
        raise ArithmeticError('The saved map norms did not replay.')
    corrupted = [[row[:] for row in matrix] for matrix in maps]
    corrupted[0][0][0] += 1
    bad, _ = contract(n, b, outer, corrupted)
    corrupted_relative = sqrt(fsum(abs(x-y)**2 for x, y in zip(bad, desired))/sum(desired))
    if corrupted_relative < 1e-3:
        raise ArithmeticError('The deliberate map perturbation was not detected.')
    return {
        'source': 'Q(5,4)', 'target': 'M(4,4,4)',
        'source_shape': [25, 32, 32], 'target_shape': [16, 16, 16],
        'source_terms_reconstructed': n*n*b*b, 'all_target_positions_checked': len(actual),
        'target_nonzero_positions': sum(desired),
        'relative_coefficient_error': relative, 'maximum_absolute_coefficient_error': maximum,
        'map_frobenius_norms': norms, 'deliberate_perturbation_relative_error': corrupted_relative,
        'integer_control': integer_control(), 'numerical_replay_passes': True,
        'exact_coefficient_certificate': False, 'construction_proved': False,
        'all_n_family_proved': False, 'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = replay(args.candidate)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
