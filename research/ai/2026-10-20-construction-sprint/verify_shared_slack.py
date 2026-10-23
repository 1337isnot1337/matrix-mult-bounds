"""Exact conditional arithmetic; no tensor construction is certified."""

from fractions import Fraction
import json


def compare(u, v, p, q):
    assert u >= v > 0 and p > q > 0
    left = u ** (p - q) * (p * (p + q)) ** q * 2 ** p
    right = v ** (p - q) * q ** (2 * q) * 2 ** (3 * q)
    return {
        'sigma': str(Fraction(u, v)),
        'd': str(Fraction(p, q)),
        'conditional_omega': str(Fraction(3 * q, p)),
        'comparison': (left > right) - (left < right),
        'left_bit_length': left.bit_length(),
        'right_bit_length': right.bit_length(),
    }


def verify():
    cases = [compare(1, 1, 168, 125), compare(21, 20, 1000, 749),
             compare(729, 686, 4, 3), compare(21, 20, 600, 449)]
    assert [case['comparison'] for case in cases] == [-1, -1, 0, 1]
    return {
        'status': 'exact-conditional-comparisons-passed',
        'rho': '1',
        'cases': cases,
        'constructs_tensor_maps': False,
        'improves_omega': False,
    }


if __name__ == '__main__':
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(verify(), indent=2) + '\n')
    print('Exact conditional comparisons passed; required maps are unconstructed.')
