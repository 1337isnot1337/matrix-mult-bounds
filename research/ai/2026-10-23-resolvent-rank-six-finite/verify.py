"""Reconstruct the source and accept exact rank-six locus certificates over Z.

Discovery is not imported. The source convention and mixed gauge are credited
to the pinned predecessor; the inverse here uses rational Gauss-Jordan directly.
"""
import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent
RESULTS = ROOT / 'results/resolvent-rank-six-finite-2026-10-23'
SUPPORT = [0, 7, 14, 21, 22, 23]


def add(matrices, weights):
    return [[sum(w * m[r][c] for w, m in zip(weights, matrices))
             for c in range(28)] for r in range(28)]


def multiply(a, b):
    out = [[0] * 28 for _ in range(28)]
    for r, row in enumerate(a):
        for k, value in enumerate(row):
            if value:
                for c, other in enumerate(b[k]):
                    out[r][c] += value * other
    return out


def source():
    rows = list(product(range(4), range(7)))
    cols = list(product(range(7), range(4)))
    raw = [[[int(H - j == i and L - r == s) for H, r in cols]
            for j, L in rows] for i, s in product(range(4), repeat=2)]
    unit = add(raw, [int(i + s == 3) for i, s in product(range(4), repeat=2)])
    identity = [[int(r == c) for c in range(28)] for r in range(28)]
    augmented = [[Fraction(x) for x in a + b] for a, b in zip(unit, identity)]
    for c in range(28):
        pivot = next(r for r in range(c, 28) if augmented[r][c])
        augmented[c], augmented[pivot] = augmented[pivot], augmented[c]
        scale = augmented[c][c]
        augmented[c] = [x / scale for x in augmented[c]]
        for r in range(28):
            if r != c:
                scale = augmented[r][c]
                augmented[r] = [x - scale * y for x, y in zip(augmented[r], augmented[c])]
    inverse = [row[28:] for row in augmented]
    if any(x.denominator != 1 for row in inverse for x in row):
        raise ValueError('source inverse is not integral')
    inverse = [[int(x) for x in row] for row in inverse]
    if multiply(unit, inverse) != identity or multiply(inverse, unit) != identity:
        raise ValueError('source inverse identity failed')
    high = [multiply(raw[0], multiply(inverse, m)) for m in raw]
    if add(high, [int(i + s == 3) for i, s in product(range(4), repeat=2)]) != raw[0]:
        raise ValueError('mixed gauge identity failed')
    labels = [['g', i, s] for i, s in product(range(4), repeat=2)]
    labels += [['f', i, s] for i, s in product(range(4), repeat=2) if (i, s) != (0, 3)]
    basis = raw + [m for j, m in enumerate(high) if j != 3]
    return raw, unit, high, labels, basis


def eliminate(basis, labels, stages, size):
    for stage in stages:
        form, pivot, minor = stage['form'], stage['pivot'], stage['minor']
        if (len(form) != len(basis) or any(type(x) is not int for x in form)
                or type(pivot) is not int or not 0 <= pivot < len(basis)
                or form[pivot] not in (-1, 1)):
            raise ValueError('invalid unit substitution')
        if (len(minor) != size or any(len(pair) != 2 for pair in minor)
                or any(type(x) is not int or not 0 <= x < 28 for pair in minor for x in pair)
                or len({r for r, _ in minor}) != size or len({c for _, c in minor}) != size):
            raise ValueError('invalid minor')
        for j, (r, c) in enumerate(minor):
            entry = [m[r][c] for m in basis]
            if entry != form and entry != [-x for x in form]:
                raise ValueError('incorrect diagonal form')
            if any(m[r][later_c] for _, later_c in minor[j + 1:] for m in basis):
                raise ValueError('nonzero entry above diagonal')
        chosen = basis[pivot]
        basis = [add([m, chosen], [1, -form[j] // form[pivot]])
                 for j, m in enumerate(basis) if j != pivot]
        labels = [label for j, label in enumerate(labels) if j != pivot]
    return basis, labels


def compression_rank(raw, unit, high):
    """Unit-pivot elimination on the 112 flattened compressed generators.

    Output coordinates are first changed by diag(K,K,K,K). Delete rows
    105,106,107 and columns 3,7,11, then pad each compression map by zero.
    """
    blocks = [[(j, j, unit) for j in range(4)]]
    for shift in (1, 2):
        blocks += [[(j + shift, j, m) for j in range(4 - shift)] for m in raw]
    blocks += [[(3, 0, m)] for m in raw]
    blocks += [[(3, 0, m)] for j, m in enumerate(high) if j != 3]
    for j in (1, 2, 3):
        blocks += [[(3, j, m)] for m in high]
    pivots = {}
    zero_generators = []
    for number, entries in enumerate(blocks):
        vector = {}
        for br, bc, matrix in entries:
            for r, row in enumerate(matrix):
                for c, x in enumerate(row):
                    row_index, col_index = 28 * br + r, 28 * bc + c
                    if x and row_index not in (105, 106, 107) and col_index not in (3, 7, 11):
                        key = row_index * 112 + col_index
                        vector[key] = vector.get(key, 0) + x
        while vector:
            key = min(vector)
            scale = vector[key]
            if key not in pivots:
                if scale not in (-1, 1):
                    raise ValueError('nonunit compression pivot')
                pivots[key] = {k: x // scale for k, x in vector.items()}
                break
            for k, x in pivots[key].items():
                vector[k] = vector.get(k, 0) - scale * x
                if not vector[k]:
                    del vector[k]
        if not vector:
            zero_generators.append(number)
    if len(blocks) != 112 or len(pivots) != 111 or len(zero_generators) != 1:
        raise ValueError('wrong compression dimension')
    return {'generators': len(blocks), 'image_dimension': len(pivots),
            'unit_pivots': True, 'zero_after_elimination': zero_generators,
            'deleted_rows': [105, 106, 107], 'deleted_columns': [3, 7, 11]}


def verify(certificate):
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for entry in sources['local_dependencies']:
        if hashlib.sha256((ROOT / entry['path']).read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError('source pin changed: ' + entry['path'])
    raw, unit, high, labels, basis = source()
    if (certificate.get('schema') != 'resolvent-rank-six-locus-v1'
            or certificate.get('labels') != labels
            or len(certificate.get('seven_minors', [])) != 26
            or len(certificate.get('six_minors', [])) != 5):
        raise ValueError('incomplete locus certificate')
    reduced, remaining = eliminate(basis, labels, certificate['seven_minors'], 7)
    expected = [high[4 * i] for i in range(4)]
    expected.append(add([high[7], high[10], high[13], raw[4]], [1, 1, 1, -1]))
    if reduced != expected or remaining != certificate['remaining_labels']:
        raise ValueError('wrong reduced locus basis')
    if any(m[r][c] for m in reduced for r in range(28) if r not in SUPPORT for c in range(28)):
        raise ValueError('locus escapes the common six rows')
    exhausted, _ = eliminate(reduced, remaining, certificate['six_minors'], 6)
    if exhausted:
        raise ValueError('rank-five elimination incomplete')
    return {'seven_minor_eliminations': 26, 'six_minor_eliminations': 5,
            'mixed_locus_dimension': 5, 'high_locus_dimension': 4,
            'full_rank_six_locus_dimension': 17, 'common_image_dimension': 6,
            'transformed_outer_image_rows': SUPPORT,
            'explicit_rank109_compression': compression_rank(raw, unit, high),
            'universal_complex_compressed_dimension_lower_bound': 111,
            'universal_bound_status': 'written proof, not machine formalized',
            'independent_review': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, default=RESULTS / 'certificate.json')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    text = json.dumps(report, indent=2) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(text, end='')
