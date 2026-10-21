"""Complete exact A78 -> M12 direct-sum A25 replay, standard library only.

The adjacent compact JSON contains all three sparse integer numerator maps.
Every coefficient of their full contraction is checked, including mixed
blocks.  A one-entry tamper must fail the same complete contraction check.
"""

from __future__ import annotations

from collections import defaultdict
from copy import deepcopy
from itertools import product
import json
from pathlib import Path


CERTIFICATE = Path(__file__).with_name('parity_structure_full_residual_a78_sparse.json')


def load_certificate(path=None):
    return json.loads(Path(path or CERTIFICATE).read_text())


def source_tensor(a, b):
    m = a+b-1
    result = {}
    for i, p, r in product(range(a), repeat=3):
        for j, q, s in product(range(b), repeat=3):
            point = ((i*m+p+q)*b+s,
                     (j*a+p)*m+r+s,
                     ((i+j)*b+q)*a+r)
            result[point] = 1
    if len(result) != (a*b)**3:
        raise ValueError('Source coordinate collision.')
    return result


def decode_maps(witness):
    if (witness.get('source_parameters') != [7, 8]
            or witness.get('matrix_block') != 12
            or witness.get('residual_parameters') != [2, 5]
            or witness.get('source_coordinate_order') != ['i,t,s', 'j,p,u', 'v,q,r']):
        raise ValueError('The certificate must describe the stated A78 restriction.')
    denominators = witness.get('row_denominators')
    if denominators != [1]*144+[2]*60:
        raise ValueError('Incorrect row denominators for this witness.')
    matrices = witness.get('numerator_maps')
    if not isinstance(matrices, list) or len(matrices) != 3:
        raise ValueError('Expected three numerator maps.')
    decoded, counts = [], []
    for matrix in matrices:
        if not isinstance(matrix, list) or len(matrix) != 204:
            raise ValueError('Every map must have exactly 204 rows.')
        by_column = [[] for _ in range(784)]
        nonzeros = 0
        for row_index, row in enumerate(matrix):
            previous = -1
            if not isinstance(row, list):
                raise ValueError('A sparse row must be a list.')
            for entry in row:
                if (not isinstance(entry, list) or len(entry) != 2
                        or any(type(value) is not int for value in entry)):
                    raise ValueError('Sparse entries must be integer [column,value] pairs.')
                col, value = entry
                if not previous < col < 784 or not value:
                    raise ValueError('Columns must be increasing, in range, and nonzero.')
                previous = col
                by_column[col].append((row_index, value))
                nonzeros += 1
        decoded.append(by_column)
        counts.append(nonzeros)
    return decoded, counts


def contract(source, by_columns):
    tensor = source
    for axis, by_column in enumerate(by_columns):
        transformed = defaultdict(int)
        for point, value in tensor.items():
            for row, coefficient in by_column[point[axis]]:
                transformed[point[:axis]+(row,)+point[axis+1:]] += value*coefficient
        tensor = {point: value for point, value in transformed.items() if value}
    return tensor


def expected_tensor():
    result = {(12*i+j, 12*j+k, 12*k+i): 1
              for i, j, k in product(range(12), repeat=3)}
    result.update({tuple(index+144 for index in point): 8*value
                   for point, value in source_tensor(2, 5).items()})
    return result


def verify_contraction(witness):
    by_columns, counts = decode_maps(witness)
    source = source_tensor(7, 8)
    image, expected = contract(source, by_columns), expected_tensor()
    if image != expected:
        mismatches = sum(image.get(point, 0) != expected.get(point, 0)
                         for point in image.keys() | expected.keys())
        raise ValueError(f'Complete tensor contraction failed at {mismatches} coefficients.')
    # Each retained coefficient becomes one after all three row denominators.
    denominators = witness['row_denominators']
    if any(value != denominators[x]*denominators[y]*denominators[z]
           for (x, y, z), value in image.items()):
        raise ValueError('The rational row normalization does not give unit coefficients.')
    return {'source_parameters': [7, 8], 'source_format': [784]*3,
            'source_terms': len(source), 'matrix_block': 12,
            'residual_parameters': [2, 5], 'target_format': [204]*3,
            'target_terms': len(image), 'matrix_block_terms': 1728,
            'residual_terms': 1000, 'numerator_nonzero_counts': counts,
            'all_output_coefficients_exact': True,
            'all_mixed_coefficients_zero': True,
            'arithmetic': 'Python exact integers; standard library only',
            'new_exponent_established': False}


def verify(witness=None, check_tamper=True):
    witness = load_certificate() if witness is None else witness
    result = verify_contraction(witness)
    if check_tamper:
        tampered = deepcopy(witness)
        tampered['numerator_maps'][0][0][0][1] += 1
        # A nonzero-to-nonzero edit passes format validation, and must be
        # rejected by the coefficient comparison itself.
        decode_maps(tampered)
        try:
            verify_contraction(tampered)
        except ValueError as error:
            if not str(error).startswith('Complete tensor contraction failed'):
                raise
            result['one_entry_tamper_rejected_by_complete_contraction'] = True
        else:
            raise ValueError('The deliberately tampered map was incorrectly accepted.')
    return result


if __name__ == '__main__':
    result = verify()
    report = Path(__file__).with_name('parity_structure_full_residual_stdlib_certificate.json')
    report.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
