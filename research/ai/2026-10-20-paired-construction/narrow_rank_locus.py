"""Exact controls for minimum-rank slices and the crossed-jet obstruction.

The symbolic rank bound and its quantifiers are in narrow_rank_locus.md.
The additional Laurent-family conclusion is limited to regular, surjective
leading maps on both long legs; arbitrary border restriction remains open.
"""

import argparse
from collections import Counter
from itertools import product
import importlib.util
import json
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    'narrow_rank_locus_helpers', Path(__file__).with_name('narrow_kernel_controls.py'))
helpers = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helpers)
rank = helpers.rank


def source_slice(n, m, x):
    long = n + m - 1
    matrix = [[0] * (m * long) for _ in range(m * long)]
    for p, q, y, v in product(range(n), range(n), range(m), range(m)):
        matrix[y * long + q + v][m * (p + y) + v] += x[p][q]
    return matrix


def bound_control(n, m, x, check_blocks=True):
    r = rank(x)
    if not r:
        raise ValueError('The rank bound is stated for a nonzero A matrix.')
    matrix = source_slice(n, m, x)
    full_rank = rank(matrix)
    lower_bound = r + m * m - 1
    assert full_rank >= lower_bound
    assert (full_rank == m * m) == (r == 1)
    result = {'n': n, 'm': m, 'a_rank': r, 'source_slice_rank': full_rank,
              'proved_lower_bound': lower_bound, 'passes': True}
    if check_blocks:
        long = n + m - 1
        block_ranks = [rank(matrix[y * long:]) for y in range(m - 1, -1, -1)]
        assert block_ranks[0] >= r + m - 1
        assert all(b - a >= m for a, b in zip(block_ranks, block_ranks[1:]))
        result['successive_descending_b_block_ranks'] = block_ranks
    return result


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def crossed_jet(n):
    if n < 3:
        raise ValueError('The rank-five slice uses n >= 3.')
    long, dim = n + 1, 2 * (n + 1)
    kb = [[0] * dim for _ in range(2)]
    kc = [[0] * dim for _ in range(2)]
    kb[0][long] = 1                 # B10
    kb[1][0] = kb[1][long + 1] = 1 # B00+B11
    kc[0][1] = 1                  # C01
    kc[1][0], kc[1][3] = 1, -1    # C00-C11
    bmap = helpers.quotient_map(kb)
    cmap = helpers.quotient_map(kc)
    slices = helpers.source_slices(n, bmap, cmap)
    flattened = [[value for row in matrix for value in row] for matrix in slices]
    a_rank = rank(flattened)
    assert a_rank == n * n - 1
    assert not any(flattened[0])
    offending = [[slices[n + 2][i][j] + slices[2 * n][i][j]
                  for j in range(2 * n)] for i in range(2 * n)]
    assert rank(offending) == 5
    # Quotient basis B: B01,...,B0n,B11,...,B1n.
    # Quotient basis C: C10,C11,...,Cn0,Cn1.
    expected = [[0] * (2 * n) for _ in range(2 * n)]
    for i, j, coefficient in [(1, 0, 1), (2, 1, 1), (n + 1, 2, 1),
                              (n, 2, -1), (n + 2, 3, 1), (0, 3, 1),
                              (n, 5, 1)]:
        expected[i][j] += coefficient
    assert offending == expected
    row_ids, col_ids = [1, 2, n + 1, n + 2, n], [0, 1, 2, 3, 5]
    minor = [[offending[i][j] for j in col_ids] for i in row_ids]
    det = helpers.determinant(minor)
    assert det == 1
    assert sum(any(row[j] for row in offending) for j in range(2 * n)) == 5
    result = {'n': n, 'source_dimensions': [n * n, dim, dim],
              'quotient_dimensions': [n * n, 2 * n, 2 * n],
              'a_flattening_rank': a_rank, 'a_kernel_parameter': [0, 0],
              'offending_parameter': [[1, 2], [2, 0]],
              'offending_rank': 5, 'nonzero_columns': 5,
              'minor_rows': row_ids, 'minor_columns': col_ids,
              'minor': [[int(x) for x in row] for row in minor],
              'minor_determinant': int(det)}
    if n == 3:
        result['offending_full_matrix'] = [[int(x) for x in row] for row in offending]
        result['basis_slice_ranks'] = [rank(matrix) for matrix in slices]
    return result


def run():
    histogram = Counter()
    for entries in product((0, 1), repeat=9):
        if not any(entries):
            continue
        x = [list(entries[3 * i:3 * i + 3]) for i in range(3)]
        record = bound_control(3, 2, x, check_blocks=False)
        histogram[record['a_rank'], record['source_slice_rank']] += 1
    block_controls = []
    for n, m in product(range(2, 6), range(2, 5)):
        for r in range(1, n + 1):
            x = [[int(i == j and i < r) * (i + 1) for j in range(n)] for i in range(n)]
            block_controls.append(bound_control(n, m, x))
    return {
        'scope': 'Finite exact coefficient controls; symbolic statements and singular-family limitations are in the companion notes.',
        'field': 'Q', 'improves_omega': False,
        'binary_q3_a_parameters_checked': 511,
        'binary_q3_rank_histogram': [{'a_rank': a, 'slice_rank': s, 'count': count}
                                   for (a, s), count in sorted(histogram.items())],
        'triangular_block_controls': block_controls,
        'crossed_jet_controls': [crossed_jet(n) for n in (3, 4, 5)],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = run()
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'binary_parameters': report['binary_q3_a_parameters_checked'],
                      'block_controls': len(report['triangular_block_controls']),
                      'crossed_jet_controls': len(report['crossed_jet_controls']),
                      'all_pass': True, 'improves_omega': False, 'output': str(args.output)}))
