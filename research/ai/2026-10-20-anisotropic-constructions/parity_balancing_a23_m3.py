"""Compose the certified corner extension with the scalar-corrected M3 map."""

import argparse
import hashlib
import io
import json
from pathlib import Path

import numpy as np

from parity_balancing_spin1_verify import verify_a23_certificate, verify_certificate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scalar-certificate', type=Path, required=True)
    parser.add_argument('--corner-maps', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    scalar_bytes, corner_bytes = args.scalar_certificate.read_bytes(), args.corner_maps.read_bytes()
    scalar = json.loads(scalar_bytes)
    verify_certificate(scalar)
    with np.load(io.BytesIO(corner_bytes)) as archive:
        corner = [archive[name].copy() for name in 'ABC']
    if any(matrix.shape != (13, 24) or np.any(matrix != matrix.astype(np.int64)) for matrix in corner):
        raise ValueError('The corner restriction must have integral maps of shape 13 by 24')
    maps = [np.asarray(scalar['map_numerators'][name], dtype=np.int64) @ right.astype(np.int64)
            for name, right in zip('ABC', corner)]
    denominator = scalar['common_map_denominator']
    certificate = {
        'source': 'full A(2,3)', 'source_dimensions': [24, 24, 24],
        'target': 'M3', 'target_dimensions': [9, 9, 9], 'field': 'Q',
        'common_map_denominator': denominator,
        'map_numerators': {name: matrix.tolist() for name, matrix in zip('ABC', maps)},
        'composition': 'A(2,3) -> A(2,2) direct sum one scalar -> M3',
        'scalar_certificate_sha256': hashlib.sha256(scalar_bytes).hexdigest(),
        'corner_maps_sha256': hashlib.sha256(corner_bytes).hexdigest(),
        'extra_scalar_source': False, 'exact_witness_found': True,
        'new_exponent_established': False,
        'review_status': 'Author-checked exact composition; no external independent review or formalization',
    }
    certificate['verification'] = verify_a23_certificate(certificate)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2) + '\n')
    np.savez_compressed(args.output.with_suffix('.npz'),
                        **{name: matrix / denominator for name, matrix in zip('ABC', maps)},
                        **{name + '_numerator': matrix for name, matrix in zip('ABC', maps)},
                        denominator=denominator)
    print(json.dumps(certificate['verification'], indent=2))


if __name__ == '__main__':
    main()
