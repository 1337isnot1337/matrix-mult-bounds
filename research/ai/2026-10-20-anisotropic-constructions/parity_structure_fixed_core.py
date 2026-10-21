"""Exact two-core contraction kernel for the fixed A78 M12 seed.

Uses only the standard library.  The complete two-core contraction is
compared with its three-factor formula; cyclic identities cover all legs.
The result constrains extensions with these core row spaces held fixed.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

from parity_structure_full_residual_stdlib import load_certificate, source_tensor


def convolution(left, right):
    result = [0]*(len(left)+len(right)-1)
    for i, value in enumerate(left):
        for j, other in enumerate(right):
            result[i+j] += value*other
    return result


def exact_rank(matrix):
    pivots = {}
    for values in matrix:
        row = [Fraction(value) for value in values]
        for col, pivot in sorted(pivots.items()):
            value = row[col]
            if value:
                row = [left-value*right for left, right in zip(row, pivot)]
        col = next((j for j, value in enumerate(row) if value), None)
        if col is None:
            continue
        value = row[col]
        pivots[col] = [entry/value for entry in row]
    return len(pivots)


def local_data():
    a, b, d, m = 7, 8, 6, 14
    u = [[0]*a for _ in range(2)]
    u[0][0] = u[1][d] = 1
    v = [[0]*b for _ in range(d)]
    for j in range(1, d):
        v[j-1][j] = 1
    v[0][d] = -1
    v[-1][0] = v[-1][d+1] = 1
    r = [[0]*m for _ in range(2*d)]
    for j in range(1, d):
        r[j-1][j] = r[d+j-1][d+j] = 1
    r[d-1][0] = 1
    r[d][0] = -1
    r[-1][1] = r[-1][d] = 1
    h = [[0]*m for _ in range(2)]
    h[0][0] = -1
    h[0][d+1] = h[0][2*d] = 1
    h[1][1] = h[1][d] = -1
    h[1][2*d+1] = 1
    return u, v, r, h


def nonzeros(vector):
    return [(index, value) for index, value in enumerate(vector) if value]


def apply_axis(tensor, matrix, axis):
    by_column = [[] for _ in range(784)]
    for row, entries in enumerate(matrix):
        for col, value in entries:
            by_column[col].append((row, value))
    image = defaultdict(int)
    for point, value in tensor.items():
        for row, coefficient in by_column[point[axis]]:
            image[point[:axis]+(row,)+point[axis+1:]] += value*coefficient
    return {point: value for point, value in image.items() if value}


def verify():
    u, v, r, h = local_data()
    witness = load_certificate()
    core = [matrix[:144] for matrix in witness['numerator_maps']]
    vertices = list(product(range(2), range(6)))

    # Verify that the local data describe the actual exported core rows.
    for left, (alpha_left, beta_left) in enumerate(vertices):
        for right, (alpha_right, beta_right) in enumerate(vertices):
            row = 12*left+right
            expected = [[], [], []]
            for i, ci in nonzeros(u[alpha_left]):
                for t, ct in nonzeros(r[6*alpha_right+beta_left]):
                    for s, cs in nonzeros(v[beta_right]):
                        coefficient = ci*ct*cs
                        expected[0].append([(i*14+t)*8+s, coefficient])
                        expected[1].append([(s*7+i)*14+t, coefficient])
                        expected[2].append([(t*8+s)*7+i, coefficient])
            for axis in range(3):
                if core[axis][row] != sorted(expected[axis]):
                    raise ValueError('The sparse witness does not have the stated cyclic core.')

    # Row factors of the X-versus-(Ycore,Zcore) contraction.
    long = {(alpha, beta): convolution(u[alpha], v[beta])
            for alpha, beta in vertices}
    first = {(alpha_i, beta_l, beta_k):
             [sum(r[6*alpha_i+beta_l][i+j]*v[beta_k][j] for j in range(8))
              for i in range(7)]
             for alpha_i, beta_l, beta_k in product(range(2), range(6), range(6))}
    second = {(alpha_k, beta_j, alpha_l):
              [sum(r[6*alpha_k+beta_j][rr+s]*u[alpha_l][rr] for rr in range(7))
               for s in range(8)]
              for alpha_k, beta_j, alpha_l in product(range(2), range(6), range(2))}
    ranks = [exact_rank(list(first.values())), exact_rank(list(long.values())),
             exact_rank(list(second.values()))]
    if ranks != [7, 12, 8]:
        raise ValueError('Unexpected local factor ranks.')
    if any(sum(functional[t]*polynomial[t] for t in range(14))
           for functional, polynomial in product(h, long.values())):
        raise ValueError('The two long functionals do not annihilate the core products.')
    if exact_rank(h) != 2:
        raise ValueError('The kernel basis has the wrong dimension.')

    # All eight short vertex indices separate into the three factors above.
    factored = {}
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            for ell, (al, bl) in enumerate(vertices):
                for i, (ai, bi) in enumerate(vertices):
                    for ii, ci in nonzeros(first[ai, bl, bk]):
                        for tt, ct in nonzeros(long[aj, bi]):
                            for ss, cs in nonzeros(second[ak, bj, al]):
                                point = ((ii*14+tt)*8+ss, 12*j+k, 12*ell+i)
                                factored[point] = ci*ct*cs
    source = source_tensor(7, 8)
    actual = apply_axis(apply_axis(source, core[1], 1), core[2], 2)
    if actual != factored:
        raise ValueError('The complete two-core contraction does not factor as claimed.')

    # The source and all three core maps have the same exact cyclic symmetry.
    def x_to_y(index):
        i, remainder = divmod(index, 14*8)
        t, s = divmod(remainder, 8)
        return (s*7+i)*14+t

    def y_to_z(index):
        j, remainder = divmod(index, 7*14)
        p, t = divmod(remainder, 14)
        return (t*8+j)*7+p

    def z_to_x(index):
        t, remainder = divmod(index, 8*7)
        q, rr = divmod(remainder, 7)
        return (rr*14+t)*8+q

    if {(z_to_x(z), x_to_y(x), y_to_z(y)): value
        for (x, y, z), value in source.items()} != source:
        raise ValueError('The source cyclic identification failed.')

    rank, kernel_dimension = 7*12*8, 7*2*8
    if rank+kernel_dimension != 784:
        raise ValueError('Rank-nullity failed.')
    return {'source': 'A(7,8)', 'fixed_core': 'the exported M12 product core',
            'source_format': [784]*3, 'core_format': [144]*3,
            'local_factor_ranks': ranks, 'two_core_contraction_ranks': [rank]*3,
            'two_core_kernel_dimensions': [kernel_dimension]*3,
            'source_terms_replayed': len(source),
            'nonzero_two_core_contraction_coefficients': len(actual),
            'complete_two_core_factorization_exact': True,
            'source_and_all_core_cyclic_identifications_exact': True,
            'kernel': 'full first short space tensor span(h0,h1) tensor full second short space, in each cyclic order',
            'fixed_core_target_leg_dimension_max': 144+kernel_dimension,
            'fixed_core_single_square_block_size_max': 16,
            'fixed_core_large_block_size_max_with_M5_summand': 15,
            'scope': 'ordinary restrictions extending the specified core row spaces; movable cores are not excluded',
            'arithmetic': 'Python exact integers and rational row reduction; standard library only',
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
