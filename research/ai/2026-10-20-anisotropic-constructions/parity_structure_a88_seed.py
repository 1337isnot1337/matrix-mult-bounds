"""Compact integral A(8,8) -> M15 seed with a complete exact replay.

All code uses the Python standard library.  The local multiplication
basis is unimodular, so every map entry is zero, one, or minus one.
This is a seed, not the larger M27+M7 target or an exponent improvement.
"""

from itertools import product
import json
from pathlib import Path

from parity_structure_full_residual_stdlib import contract, source_tensor


def monomial(degree, size=8):
    return [int(i == degree) for i in range(size)]


def local_data():
    u = [monomial(degree) for degree in (0, 4, 7)]
    v = [monomial(degree) for degree in (0, 1, 2, 3, 7)]
    v[0][5] = v[3][6] = 1
    supports = ({0: 1}, {1: 1}, {2: 1}, {3: 1}, {7: 1, 10: -1, 12: -1, 13: 1},
                {4: 1}, {5: 1, 0: -1}, {6: 1, 3: -1}, {10: 1, 13: -1}, {11: 1},
                {12: 1}, {8: 1}, {9: 1, 4: -1}, {13: 1}, {14: 1})
    r = [[support.get(i, 0) for i in range(15)] for support in supports]
    return u, v, r


def convolution(left, right):
    result = [0]*15
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            result[i+j] += first*second
    return result


def verify_local():
    u, v, r = local_data()
    products = [convolution(left, right) for left, right in product(u, v)]
    for row, col in product(range(15), repeat=2):
        if sum(r[row][i]*products[col][i] for i in range(15)) != int(row == col):
            raise ValueError('The local product left inverse failed.')
        if sum(products[i][row]*r[i][col] for i in range(15)) != int(row == col):
            raise ValueError('The local product right inverse failed.')
    return u, v, r


def nonzeros(vector):
    return [(index, value) for index, value in enumerate(vector) if value]


def sparse_maps():
    u, v, r = verify_local()
    vertices = list(product(range(3), range(5)))
    matrices = [[] for _ in range(3)]
    for alpha_left, beta_left in vertices:
        for alpha_right, beta_right in vertices:
            rows = [[], [], []]
            for i, ci in nonzeros(u[alpha_left]):
                for t, ct in nonzeros(r[5*alpha_right+beta_left]):
                    for s, cs in nonzeros(v[beta_right]):
                        coefficient = ci*ct*cs
                        rows[0].append([(i*15+t)*8+s, coefficient])
                        rows[1].append([(s*8+i)*15+t, coefficient])
                        rows[2].append([(t*8+s)*8+i, coefficient])
            for axis in range(3):
                matrices[axis].append(sorted(rows[axis]))
    return matrices


def verify(matrices=None):
    u, v, r = verify_local()
    matrices = sparse_maps() if matrices is None else matrices
    if len(matrices) != 3 or any(len(matrix) != 225 for matrix in matrices):
        raise ValueError('The three maps must each have 225 rows.')
    by_columns, nonzero_counts = [], []
    for matrix in matrices:
        columns = [[] for _ in range(960)]
        count = 0
        for row, entries in enumerate(matrix):
            previous = -1
            for col, value in entries:
                if type(col) is not int or type(value) is not int or not previous < col < 960 or not value:
                    raise ValueError('Malformed sparse integer map.')
                columns[col].append((row, value))
                previous = col
                count += 1
        by_columns.append(columns)
        nonzero_counts.append(count)
    source = source_tensor(8, 8)
    image = contract(source, by_columns)
    expected = {(15*i+j, 15*j+k, 15*k+i): 1
                for i, j, k in product(range(15), repeat=3)}
    if image != expected:
        raise ValueError('The complete A88-to-M15 coefficient identity failed.')
    return {'source': 'A(8,8)', 'source_format': [960]*3,
            'source_terms': len(source), 'target': 'M15', 'target_format': [225]*3,
            'target_terms': len(image), 'sparse_map_shapes': [[225, 960]]*3,
            'map_nonzero_counts': nonzero_counts,
            'map_max_absolute_entry': max(abs(value) for matrix in matrices for row in matrix for _, value in row),
            'both_local_inverse_identities_exact': True,
            'all_output_coefficients_exact': True,
            'U': u, 'V': v, 'R': r,
            'arithmetic': 'Python exact integers; standard library only',
            'larger_target_constructed': False, 'new_exponent_established': False}


if __name__ == '__main__':
    matrices = sparse_maps()
    result = verify(matrices)
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    witness = {'source_parameters': [8, 8], 'matrix_block': 15,
               'source_coordinate_order': ['i,t,s', 'j,p,u', 'v,q,r'],
               'target_order': 'standard matrix-index order',
               'integer_maps': matrices, 'U': result['U'], 'V': result['V'], 'R': result['R']}
    prefix.with_name(prefix.name+'_sparse.json').write_text(json.dumps(witness, separators=(',', ':'))+'\n')
    print(json.dumps({key: value for key, value in result.items() if key not in {'U', 'V', 'R'}}, indent=2))
