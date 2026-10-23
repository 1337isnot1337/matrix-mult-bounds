"""Standard-library full coefficient replay for the nonlocal Q-source pilots."""
from hashlib import sha256
import json
from math import fsum, sqrt
from pathlib import Path

from q54_numeric_replay import contract


def replay(path):
    raw = Path(path).read_bytes()
    point = json.loads(raw)
    n, r = point['n'], point['target_outer']
    if point['b'] != 4 or r != n-1 or point['auxiliary_rank'] != 0:
        raise ValueError('The source, near-full target, or scalar cost changed.')
    if point['exact_coefficient_certificate'] is not False:
        raise ValueError('A floating-point search artifact must remain numerical.')
    maps = [[[complex(x, y) for x, y in zip(real_row, imag_row)]
             for real_row, imag_row in zip(real, imag)]
            for real, imag in zip(point['maps_real'], point['maps_imag'])]
    actual, target = contract(n, 4, r, maps)
    error = [x-y for x, y in zip(actual, target)]
    relative = sqrt(fsum(abs(x)**2 for x in error)/(4*r*r))
    discrepancy = abs(relative-point['relative_coefficient_error'])
    if discrepancy > 1e-10:
        raise ArithmeticError('The saved full coefficient error did not replay.')
    return {'artifact': Path(path).name, 'artifact_sha256': sha256(raw).hexdigest(),
            'n': n, 'source': f'Q({n},4)', 'target': f'M({r},4,{r})',
            'auxiliary_rank': 0, 'all_source_terms_reconstructed': 16*n*n,
            'all_target_positions_checked': len(actual),
            'target_nonzero_positions': 4*r*r,
            'relative_full_coefficient_error': relative,
            'maximum_coefficient_error': max(map(abs, error)),
            'reported_error_discrepancy': discrepancy,
            'map_norms': [sqrt(fsum(abs(x)**2 for row in matrix for x in row)) for matrix in maps],
            'actual_stop_reason': point['completed_run']['actual_stop_reason'],
            'iterations_completed': point['completed_run']['iterations_completed'],
            'numerical_replay_passes': True,
            'exact_coefficient_certificate': False,
            'nonexistence_proved': False, 'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints', type=Path, nargs='+')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = {'replays': [replay(path) for path in args.checkpoints]}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
