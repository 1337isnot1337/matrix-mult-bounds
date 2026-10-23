"""Exact finite support checks for alternating convolution sectors."""
from __future__ import annotations

import argparse
from itertools import product
import json
from pathlib import Path


def layout(a: int, widths: tuple[int, ...]):
    d = a - 1
    y_blocks = []
    z_blocks = []
    y_start = z_start = 0
    for i, b in enumerate(widths):
        y_length = b + (d if i % 2 else 0)
        z_length = b + (0 if i % 2 else d)
        y_blocks.append((y_start, y_start + y_length))
        z_blocks.append((z_start, z_start + z_length))
        y_start += y_length
        z_start += z_length

    source_width = sum(widths) + (len(widths) // 2) * d
    if y_start != source_width:
        raise AssertionError('the second-leg block lengths do not sum to B')
    source_output_length = source_width + d
    expected_output_length = sum(widths) + ((len(widths) + 1) // 2) * d
    if z_start != expected_output_length:
        raise AssertionError('the third-leg block lengths have the wrong total')
    if source_output_length - z_start != (d if len(widths) % 2 == 0 else 0):
        raise AssertionError('unexpected trailing output interval')
    return source_width, y_blocks, z_blocks


def verify_case(a: int, widths: tuple[int, ...]) -> tuple[int, int, int]:
    if a < 1 or not widths or any(b < 1 for b in widths):
        raise ValueError('a and every sector width must be positive')
    d = a - 1
    source_width, y_blocks, z_blocks = layout(a, widths)

    zero_support = set()
    source_terms = 0
    for x in range(a):
        for y in range(source_width):
            z = x + y
            source_terms += 1
            yi = next(i for i, (lo, hi) in enumerate(y_blocks) if lo <= y < hi)
            zi = next((i for i, (lo, hi) in enumerate(z_blocks)
                       if lo <= z < hi), None)
            y_weight = 1 if yi % 2 else 0
            z_weight = -1 if zi is not None and zi % 2 else 0
            weight = y_weight + z_weight
            if weight < 0:
                raise AssertionError(f'negative support weight at {(x, y, z)}')
            if weight == 0:
                zero_support.add((x, y, z))

    expected_support = set()
    for i, b in enumerate(widths):
        y_start = y_blocks[i][0]
        z_start = z_blocks[i][0]
        if i % 2 == 0:
            for x in range(a):
                for u in range(b):
                    expected_support.add((x, y_start + u, z_start + x + u))
        else:
            for x in range(a):
                for v in range(b):
                    u = d - x + v
                    expected_support.add((x, y_start + u, z_start + v))

    if zero_support != expected_support:
        missing = expected_support - zero_support
        extra = zero_support - expected_support
        raise AssertionError(
            f'weight-zero support mismatch: {len(missing)} missing, {len(extra)} extra')
    return source_width, source_terms, len(zero_support)


def run() -> dict:
    cases = 0
    source_terms = 0
    zero_terms = 0
    for a in range(1, 7):
        for k in range(1, 7):
            for widths in product((1, 2, 3), repeat=k):
                _, checked, zero = verify_case(a, widths)
                cases += 1
                source_terms += checked
                zero_terms += zero
    return {
        'status': 'passed',
        'a_range': [1, 6],
        'sector_count_range': [1, 6],
        'sector_widths': [1, 2, 3],
        'cases_checked': cases,
        'source_terms_checked': source_terms,
        'zero_weight_terms_checked': zero_terms,
        'scope': 'finite support replay only; the interval proof covers all positive sizes',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
