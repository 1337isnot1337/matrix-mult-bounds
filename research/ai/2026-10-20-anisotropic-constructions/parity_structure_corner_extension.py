"""Exact monomial corner splits for cyclic convolution tensors.

A(a,b) -> A(s,t) direct-sum A(c,d) when the two long degree intervals
are disjoint.  Includes A(2,3) -> A(2,2) direct-sum one scalar.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, source_coordinates, source_tensor


def corner_maps(a, b, s, t, c, d):
    assert min(a, b, s, t, c, d) >= 1
    assert max(s, c) <= a and max(t, d) <= b
    assert s+t+c+d <= a+b+1
    source_axes = source_coordinates(a, b)
    indices = [{point: i for i, point in enumerate(axis)} for axis in source_axes]
    old_axes = source_coordinates(s, t)
    new_axes = source_coordinates(c, d)
    alpha, beta = a-c, b-d
    shifts = ((alpha, alpha+beta, beta), (beta, alpha, alpha+beta),
              (alpha+beta, beta, alpha))
    old_size, new_size = s*t*(s+t-1), c*d*(c+d-1)
    matrices = [np.zeros((old_size+new_size, a*b*(a+b-1)), dtype=np.int64)
                for _ in range(3)]
    for axis in range(3):
        for row, point in enumerate(old_axes[axis]):
            matrices[axis][row, indices[axis][point]] = 1
        for row, point in enumerate(new_axes[axis]):
            shifted = tuple(value+offset for value, offset in zip(point, shifts[axis]))
            matrices[axis][old_size+row, indices[axis][shifted]] = 1
    return matrices


def target_tensor(s, t, c, d):
    result = source_tensor(s, t)
    offset = s*t*(s+t-1)
    result.update({tuple(index+offset for index in point): value
                   for point, value in source_tensor(c, d).items()})
    return result


def verify_example(parameters):
    a, b, s, t, c, d = parameters
    maps = corner_maps(*parameters)
    source = source_tensor(a, b)
    image = apply_sparse(source, maps)
    assert image == target_tensor(s, t, c, d)
    return {'source_lengths': [a, b], 'first_block_lengths': [s, t],
            'second_block_lengths': [c, d],
            'source_format': [a*b*(a+b-1)]*3,
            'target_format': [len(maps[0])]*3,
            'target_terms': len(image), 'all_coefficients_exact': True,
            'all_mixed_coefficients_zero': True,
            'first_long_interval': [0, s+t-2],
            'second_long_interval': [a+b-c-d, a+b-2]}


def verify():
    parameters = [(2, 3, 2, 2, 1, 1), (3, 3, 2, 2, 1, 2),
                  (4, 5, 3, 3, 2, 2), (5, 6, 4, 4, 2, 2)]
    reports = [verify_example(values) for values in parameters]
    return {'scope': 'exact monomial direct-sum constructions',
            'examples': reports,
            'scalar_extension': 'A(2,3) -> A(2,2) direct-sum one scalar',
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    maps = corner_maps(2, 3, 2, 2, 1, 1)
    np.savez_compressed(prefix.with_name(prefix.name+'_a23_maps.npz'),
                        A=maps[0], B=maps[1], C=maps[2],
                        x=maps[0], y=maps[1], z=maps[2],
                        block_offsets=np.array([0, 12]), block_lengths=np.array([[2, 2], [1, 1]]))
    print(json.dumps(result, indent=2))
