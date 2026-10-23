"""Exact block-form acceptance for the remaining constant-compression question.

Default execution only accepts the retained coordinate certificate. The optional
--discover step reconstructs coordinates by rational elimination, separately
from their exact-entry acceptance. The mathematical low-rank deduction imports
the minimum-rank-six theorem pinned in sources.json; it is not a modular claim.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from pathlib import Path

SIZE = 112
OUTER = 28
ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / 'results/conjugation-limit-2026-10-23'


def add(target, source, scale=1):
    for key, value in source.items():
        target[key] = target.get(key, 0) + scale * value
        if not target[key]:
            del target[key]


def embed(matrix, row, column):
    return {(28 * row + key // 28) * SIZE + 28 * column + key % 28: value
            for key, value in matrix.items()}


def build_blocks(verifier):
    source, _ = verifier.build_source()
    outer = [{key: value for position, value in source[48 + index].items()
              for row, column in [divmod(position, SIZE)] if row < 28 and column < 28
              for key in [28 * row + column]} for index in range(16)]
    fixed = outer[0]
    identity = {29 * i: 1 for i in range(28)}
    matrices = []
    labels = []
    for name, matrix in [('identity', identity), ('fixed', fixed)]:
        block = {}
        for q in range(4):
            add(block, embed(matrix, q, q))
        labels.append(['diagonal', name]);matrices.append(block)
    for name in ['first_plain', 'first_mixed', 'second_plain', 'second_mixed', 'lowest_plain', 'lowest_commutator', 'lowest_sandwich']:
        for index, matrix in enumerate(outer):
            if name == 'lowest_commutator' and index in (0, 3):
                continue
            block = {}
            right = verifier.matrix_product(matrix, fixed, 28)
            left = verifier.matrix_product(fixed, matrix, 28)
            if name == 'first_plain':
                for row, column in [(1, 0), (2, 1), (3, 2)]:add(block, embed(matrix, row, column))
            elif name == 'first_mixed':
                add(block, embed(right, 1, 0));add(block, embed(left, 3, 2), -1)
            elif name == 'second_plain':
                add(block, embed(matrix, 2, 0));add(block, embed(matrix, 3, 1))
            elif name == 'second_mixed':
                add(block, embed(right, 2, 0));add(block, embed(left, 3, 1), -1)
            elif name == 'lowest_plain':add(block, embed(matrix, 3, 0))
            elif name == 'lowest_commutator':
                add(block, embed(right, 3, 0));add(block, embed(left, 3, 0), -1)
            elif name == 'lowest_sandwich':
                add(block, embed(verifier.matrix_product(fixed, right, 28), 3, 0))
            labels.append([name, index]);matrices.append(block)
    if len(matrices) != SIZE:
        raise ValueError('wrong number of explicit block generators')
    return matrices, labels, outer


def verify_transpose_identity(outer, verifier):
    # Q=R K; R changes (j,L) to (L,j). Thus Q is symmetric.
    form = {}
    for i, s, j, r in product(range(4), repeat=4):
        if i + s == 3:
            row = 4 * (s + r) + j
            column = 4 * (i + j) + r
            form[28 * row + column] = form.get(28 * row + column, 0) + 1
    transposed = {28 * (key % 28) + key // 28: value for key, value in form.items()}
    if form != transposed:
        raise ValueError('the source-unit form is not symmetric')
    inverse = verifier.integer_inverse(form, 28)
    for i, s in product(range(4), repeat=2):
        left = {28 * (key % 28) + key // 28: value for key, value in outer[4 * i + s].items()}
        right = verifier.matrix_product(verifier.matrix_product(form, outer[4 * s + i], 28), inverse, 28)
        if left != right:
            raise ValueError('the transpose-conjugation identity is false')
    return {'outer_transpose_identities_checked': 16, 'source_unit_form_symmetric': True}


def discover_coordinates(matrices, leading):
    pivots = {}
    for index, entries in enumerate(matrices):
        row = {key: Fraction(value) for key, value in entries.items()}
        coefficients = {index: Fraction(1)}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                scale = row[pivot]
                pivots[pivot] = ({key: value / scale for key, value in row.items()},
                                 {key: value / scale for key, value in coefficients.items()})
                break
            earlier, transformation = pivots[pivot]
            scale = -row[pivot]
            add(row, earlier, scale);add(coefficients, transformation, scale)
        else:
            raise ValueError('the proposed block generators are dependent')
    result = []
    for index, entries in enumerate(leading):
        row = {key: Fraction(value) for key, value in entries.items()}
        coefficients = {}
        while row:
            pivot = max(row)
            if pivot not in pivots:
                raise ValueError('a certified limiting matrix lies outside the block family')
            earlier, transformation = pivots[pivot]
            scale = row[pivot]
            add(row, earlier, -scale);add(coefficients, transformation, scale)
        result.append({'leading_index': index,
                       'coefficients': [[key, value.numerator, value.denominator]
                                        for key, value in sorted(coefficients.items())]})
    return result


def accept(certificate, parent, verifier, parent_hash):
    if (certificate.get('schema') != 'a4-conjugation-block-reduction-v1'
            or certificate.get('parent_certificate_sha256') != parent_hash):
        raise ValueError('wrong block certificate or parent pin')
    leading, _ = verifier.verify_limit(parent)
    matrices, labels, outer = build_blocks(verifier)
    if certificate.get('labels') != labels or len(certificate.get('coordinate_rows', [])) != SIZE:
        raise ValueError('wrong explicit block-basis labels or row coverage')
    for index, row in enumerate(certificate['coordinate_rows']):
        if row.get('leading_index') != index:
            raise ValueError('missing or reordered limiting matrix')
        actual = {}
        used = set()
        for entry in row['coefficients']:
            if (len(entry) != 3 or any(type(value) is not int for value in entry)
                    or not 0 <= entry[0] < SIZE or not entry[1] or entry[2] <= 0
                    or entry[0] in used):
                raise ValueError('invalid block coordinate')
            source, numerator, denominator = entry
            used.add(source)
            add(actual, matrices[source], Fraction(numerator, denominator))
        if actual != leading[index]:
            raise ValueError('an exact block-coordinate identity is false')
    transpose = verify_transpose_identity(outer, verifier)
    lowest = [matrix for matrix, label in zip(matrices, labels) if label[0].startswith('lowest_')]
    if len(lowest) != 46 or any(any(key // SIZE < 84 or key % SIZE >= 28 for key in matrix) for matrix in lowest):
        raise ValueError('the reduced space is not the stated bottom-left block')
    return {'full_limit_dimension': 112, 'independent_explicit_block_generators': 112,
            'exact_coordinate_identities_checked': 112, **transpose,
            'reduced_matrix_size': 28, 'reduced_space_dimension': 46,
            'compression_ranks_at_least': 26, 'necessary_kernel_dimension': 9,
            'necessary_reduced_image_dimension_at_most': 37,
            'remaining_dimension_bound_proved': False,
            'arbitrary_constant_compressions_excluded': False,
            'matrix_multiplication_target_constructed': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--parent', type=Path, default=RESULTS / 'certificate.json')
    parser.add_argument('--certificate', type=Path, default=RESULTS / 'block-certificate.json')
    parser.add_argument('--discover', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('conjugation_block_parent', args.package / 'verify.py')
    verifier = importlib.util.module_from_spec(spec);spec.loader.exec_module(verifier)
    parent = json.loads(args.parent.read_text());parent_hash=hashlib.sha256(args.parent.read_bytes()).hexdigest()
    if args.discover:
        leading, _ = verifier.verify_limit(parent)
        matrices, labels, _ = build_blocks(verifier)
        data = {'schema': 'a4-conjugation-block-reduction-v1', 'parent_certificate_sha256': parent_hash,
                'labels': labels, 'coordinate_rows': discover_coordinates(matrices, leading)}
        args.certificate.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    report = accept(json.loads(args.certificate.read_text()), parent, verifier, parent_hash)
    text=json.dumps(report, indent=2, sort_keys=True)+'\n'
    if args.output:args.output.write_text(text)
    print(text, end='')

if __name__ == '__main__':main()
