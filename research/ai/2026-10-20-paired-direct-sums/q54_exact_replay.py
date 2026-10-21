"""Replay the sparse integer Q(5,4) -> M(4,4,4) certificate.

This checker does not import the construction's generator.  Its native
source contraction was implemented for the preceding numerical search.
The replay uses Python integers and checks the full target tensor.
"""
import argparse
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

from q54_numeric_replay import contract, integer_control


def replay(path):
    raw = Path(path).read_bytes()
    witness = json.loads(raw)
    maps = witness['maps_target_by_source']
    if len(maps) != 3 or any(type(value) is not int
                            for matrix in maps for row in matrix for value in row):
        raise ValueError('Every map coefficient must be a Python integer.')
    actual, desired = contract(5, 4, 4, maps)
    differences = [value-target for value, target in zip(actual, desired)]
    failures = [i for i, value in enumerate(differences) if value]
    if failures:
        raise ArithmeticError(f'Exact contraction failed at {len(failures)} positions.')
    if any(type(value) is not int for value in actual):
        raise ArithmeticError('The contraction did not remain integral.')
    corrupted = deepcopy(maps)
    index = next((i, j) for i, row in enumerate(corrupted[0])
                 for j, value in enumerate(row) if value)
    corrupted[0][index[0]][index[1]] *= -1
    bad, _ = contract(5, 4, 4, corrupted)
    bad_positions = sum(value != target for value, target in zip(bad, desired))
    if not bad_positions:
        raise ArithmeticError('The deliberate sign error was not detected.')
    return {
        'source': 'Q(5,4)', 'target': 'M(4,4,4)',
        'source_formula': 'sum A[p,q] B[y,q+v] C[p+y,v], p,q<5, y,v<4',
        'target_formula': 'sum A[i,k] B[i,j] C[j,k], i,j,k<4',
        'source_dimensions': [25, 32, 32], 'target_dimensions': [16, 16, 16],
        'source_terms_reconstructed': 400,
        'all_target_coefficient_positions_checked': len(actual),
        'target_nonzero_coefficients': sum(desired),
        'off_support_coefficients_checked': sum(value == 0 for value in desired),
        'coefficient_failures': len(failures),
        'maximum_absolute_coefficient_error': max(map(abs, differences)),
        'map_nonzero_counts': [sum(value != 0 for row in matrix for value in row)
                              for matrix in maps],
        'map_coefficient_values': sorted(set(value for matrix in maps
                                            for row in matrix for value in row)),
        'deliberate_sign_error_positions': bad_positions,
        'integer_control': integer_control(),
        'certificate_sha256': sha256(raw).hexdigest(),
        'coefficient_ring': 'Z', 'exact_coefficient_certificate': True,
        'valid_over_every_field': True, 'ordinary_restriction_proved': True,
        'separately_implemented_contraction': True,
        'external_independent_review': False,
        'fixed_width_near_full_all_n_family_proved': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = replay(args.certificate)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
