#!/usr/bin/env python3
"""Exact necessary rank tests for saturated graded restriction blocks.

Discovery and verification use integer coordinates only.  A passing profile is
not a restriction, and this test does not apply to arbitrary border limits.
"""

import argparse
from collections import Counter
from functools import lru_cache
from itertools import product
import json
from pathlib import Path


def weight(point):
    i, k, s = point
    return i + s - k


@lru_cache(maxsize=None)
def source_spaces(a, b):
    if a < 1 or b < 1:
        raise ValueError('source parameters must be positive')
    spaces = {}
    for point in product(range(a), range(a + b - 1), range(b)):
        spaces.setdefault(weight(point), []).append(point)
    return {w: tuple(points) for w, points in spaces.items()}


def third_coordinate(a, b, x, y):
    """The unique common-coordinate Z paired with X,Y, or None."""
    i, k, s = x
    p, ell, j = y
    q, r = k - p, ell - s
    if 0 <= q < b and 0 <= r < a:
        return (r, i + j, q)
    return None


@lru_cache(maxsize=None)
def source_image(a, b, wx, wy):
    spaces = source_spaces(a, b)
    witnesses = {}
    for x in spaces.get(wx, ()):
        for y in spaces.get(wy, ()):
            z = third_coordinate(a, b, x, y)
            if z is not None:
                witnesses.setdefault(z, (x, y))
    return tuple((z, witnesses[z]) for z in sorted(witnesses))


def direct_source_images(a, b, requested):
    """Independent six-index source expansion, with no product helper."""
    images = {tuple(weights): set() for weights in requested}
    for i, p, r in product(range(a), repeat=3):
        for j, q, s in product(range(b), repeat=3):
            wx = i + s - p - q
            wy = p + j - r - s
            if (wx, wy) in images:
                images[wx, wy].add((r, i + j, q))
    return images


def validate_profile(blocks):
    normalized = []
    for block in blocks:
        if len(block) != 3 or any(not vertices for vertices in block):
            raise ValueError('each matrix summand needs three nonempty vertex lists')
        if any(type(c) is not int for vertices in block for c in vertices):
            raise ValueError('vertex charges must be integers')
        normalized.append(tuple(tuple(vertices) for vertices in block))
    if not normalized:
        raise ValueError('at least one matrix summand is required')
    return tuple(normalized)


def target_dimensions(blocks):
    blocks = validate_profile(blocks)
    return [Counter(left - right
                    for block in blocks
                    for left in block[leg]
                    for right in block[(leg + 1) % 3])
            for leg in range(3)]


def target_image(blocks, leg, wx, wy):
    image = set()
    for block_number, block in enumerate(validate_profile(blocks)):
        c0, c1, c2 = (block[(leg + offset) % 3] for offset in range(3))
        for i, ci in enumerate(c0):
            for j, cj in enumerate(c1):
                if ci - cj != wx:
                    continue
                for k, ck in enumerate(c2):
                    if cj - ck == wy:
                        image.add((block_number, k, i))
    return tuple(sorted(image))


def target_rank(blocks, leg, wx, wy):
    """Same exact image rank, counted by charge multiplicities."""
    result = 0
    for block in validate_profile(blocks):
        c0, c1, c2 = (Counter(block[(leg + offset) % 3]) for offset in range(3))
        result += sum(count * c2[c - wx - wy] for c, count in c0.items()
                      if c1[c - wx])
    return result


def saturated_block(a, b, blocks, leg, wx, wy):
    if leg not in range(3):
        raise ValueError('leg must be 0, 1, or 2')
    source = source_spaces(a, b)
    target = target_dimensions(blocks)
    weights = (wx, wy, -wx - wy)
    sd = [len(source.get(w, ())) for w in weights]
    td = [target[(leg + offset) % 3][w] for offset, w in enumerate(weights)]
    if sd[:2] != td[:2] or not all(sd[:2]):
        raise ValueError('both input weight spaces must be nonzero and saturated')
    if any(t > s for s, t in zip(sd, td)):
        raise ValueError('target dimensions exceed the source dimensions')
    si = source_image(a, b, wx, wy)
    ti = target_image(blocks, leg, wx, wy)
    delta = sd[2] - td[2]
    lower = max(0, len(si) - delta)
    return {
        'first_leg': leg,
        'weights': list(weights),
        'source_dimensions': sd,
        'target_dimensions': td,
        'source_third_flattening_rank': len(si),
        'target_third_flattening_rank': len(ti),
        'third_map_codimension': delta,
        'necessary_lower_rank': lower,
        'excluded': len(ti) < lower,
        'source_image_coordinates': [list(z) for z, _ in si],
        'target_image_units': [list(unit) for unit in ti],
    }


def screen(a, b, blocks):
    blocks = validate_profile(blocks)
    source = source_spaces(a, b)
    target = target_dimensions(blocks)
    capacity_failures = [
        {'leg': leg, 'weight': w, 'source_dimension': len(source.get(w, ())),
         'target_dimension': n}
        for leg, dimensions in enumerate(target)
        for w, n in sorted(dimensions.items()) if n > len(source.get(w, ()))
    ]
    records, upper_failures = [], []
    if not capacity_failures:
        for leg in range(3):
            # Flattening rank cannot increase under any linear restriction,
            # even when neither input space is saturated.
            for wx, wy in product(sorted(target[leg]), sorted(target[(leg + 1) % 3])):
                sr = len(source_image(a, b, wx, wy))
                tr = target_rank(blocks, leg, wx, wy)
                if tr > sr:
                    upper_failures.append({'first_leg': leg, 'weights': [wx, wy, -wx-wy],
                                           'source_rank': sr, 'target_rank': tr})
            left = [w for w in sorted(source) if target[leg][w] == len(source[w])]
            right = [w for w in sorted(source)
                     if target[(leg + 1) % 3][w] == len(source[w])]
            for wx, wy in product(left, right):
                records.append(saturated_block(a, b, blocks, leg, wx, wy))
    return {
        'capacity_failures': capacity_failures,
        'flattening_upper_bound_failures': upper_failures,
        'saturated_blocks': records,
        'excluded': bool(capacity_failures or upper_failures) or any(row['excluded'] for row in records),
    }


def width13_profile():
    big = [0] + [c for c in range(1, 14) for _ in range(2)]
    small = list(range(7))
    return [[big, big, big], [small, small, small]]


def report():
    blocks = width13_profile()
    screened = screen(8, 8, blocks)
    # All three legs agree. Keep the eight potentially nonzero first-leg
    # comparisons, and independently replay their source images.
    rows = [row for row in screened['saturated_blocks']
            if row['first_leg'] == 0 and row['source_third_flattening_rank']]
    requested = [(row['weights'][0], row['weights'][1]) for row in rows]
    direct = direct_source_images(8, 8, requested)
    for row in rows:
        key = tuple(row['weights'][:2])
        if direct[key] != {tuple(z) for z in row['source_image_coordinates']}:
            raise ArithmeticError('six-index expansion disagrees with product rank')
    decisive = saturated_block(8, 8, blocks, 0, -11, 11)
    expected = {(r, r + q, q) for r in range(4) for q in range(4, 8)}
    if {tuple(z) for z in decisive['source_image_coordinates']} != expected:
        raise ArithmeticError('decisive source image is not the claimed rectangle')
    witnesses = []
    for r, q in product(range(4), range(4, 8)):
        i = max(0, r + q - 7)
        x, y, z = (i, i + 11, 0), (11 + i - q, r, r + q - i), (r, r + q, q)
        if x not in source_spaces(8, 8)[-11] or y not in source_spaces(8, 8)[11]:
            raise ArithmeticError('rank witness lies outside the weight space')
        if third_coordinate(8, 8, x, y) != z:
            raise ArithmeticError('rank witness has wrong output coordinate')
        witnesses.append({'x': list(x), 'y': list(y), 'z': list(z)})
    control = saturated_block(1, 1, [[[0], [0], [0]]], 0, 0, 0)
    if control['excluded'] or control['necessary_lower_rank'] != 1:
        raise ArithmeticError('identity restriction failed the positive control')
    source = source_spaces(8, 8)
    target = target_dimensions(blocks)[0]
    return {
        'schema': 'torus-saturated-block-ranks-v1',
        'model': 'ordinary grading-preserving restriction',
        'field': 'arbitrary',
        'source': [8, 8],
        'target_square_sizes': [27, 7],
        'vertex_charges': blocks,
        'nonnegative_weights': list(range(15)),
        'source_dimensions': [len(source[w]) for w in range(15)],
        'target_dimensions': [target[w] for w in range(15)],
        'capacity_feasible': not screened['capacity_failures'],
        'flattening_upper_bound_failures': screened['flattening_upper_bound_failures'],
        'source_terms_independently_enumerated': 8 ** 6,
        'nonzero_saturated_first_leg_blocks': rows,
        'decisive_weights': [-11, 11, 0],
        'decisive_rank_comparison': {'source': 16, 'codimension': 4,
                                    'necessary_target_rank': 12, 'actual_target_rank': 9},
        'sixteen_source_rank_witnesses': witnesses,
        'positive_control': control,
        'profile_excluded': screened['excluded'],
        'improves_omega': False,
        'scope_exclusions': ['ungraded maps', 'other charge profiles',
                             'arbitrary singular Laurent degenerations'],
    }


def verify_saved(path):
    actual = report()
    if json.loads(Path(path).read_text()) != actual:
        raise ArithmeticError('saved saturated-block certificate mismatch')
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--verify', type=Path)
    args = parser.parse_args()
    result = verify_saved(args.verify) if args.verify else report()
    encoded = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(encoded)
    else:
        print(encoded, end='')


if __name__ == '__main__':
    main()
