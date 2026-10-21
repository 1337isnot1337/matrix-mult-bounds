"""Optional numerical layout and initialization controls; no fitting updates."""
from hashlib import sha256
import json
from pathlib import Path

from q_metaplectic_blocks import control, expand, initialize
from q_metaplectic_nonproduct import initialize as nonproduct_initialize


def report():
    root = Path(__file__).resolve().parents[3]
    results = root/'results/paired-direct-sums-2026-10-20'
    audit = json.loads((results/'q-metaplectic-history-audit.json').read_text())
    points = []
    for pilot in audit['pilots']:
        point = json.loads((results/pilot['artifact']).read_text())
        nonproduct = 'nonproduct' in pilot['artifact']
        initial = nonproduct_initialize if nonproduct else initialize
        first, x, z, basis, names = initial(point['n'], point['seed'], 0.03 if nonproduct else 0.15)
        maps = expand(first, x, z, basis)
        payload = {'maps_real': [m.real.tolist() for m in maps],
                   'maps_imag': [m.imag.tolist() for m in maps]}
        digest = sha256(json.dumps(payload, separators=(',', ':')).encode()).hexdigest()
        expected = pilot['initial_maps_canonical_sha256']
        if digest != expected:
            raise ArithmeticError('Initial arrays did not reproduce byte-for-byte in this numerical runtime.')
        points.append({'artifact': pilot['artifact'], 'initial_maps_sha256': digest,
                       'matches_original_initial_arrays_in_recorded_runtime': True,
                       'optimization_updates_rerun': 0})
    return {'known_integer_source_floating_layout_control': control(),
            'initializations': points,
            'different_linear_algebra_runtimes_may_not_match_array_hashes': True,
            'saved_coefficient_replays_are_separate': True,
            'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = report()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
