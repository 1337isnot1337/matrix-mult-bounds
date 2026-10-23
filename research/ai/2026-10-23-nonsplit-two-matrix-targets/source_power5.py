"""Exact five-power degree cover for the nonsplit SL(2,F5) source."""
from collections import Counter
import argparse
import json
from itertools import product
from math import comb, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]


POWER = 5
MATRIX_WEIGHTS = (1, 4, 3, 3, 3, 0)
CUTOFFS = ((1, 1, 1), (7, 7, 8), (7, 8, 8),
           (9, 9, 10), (11, 11, 11), (12, 13, 13))
EXPECTED_BOUND = 9_874_344_844


def convolve(left, right):
    result = Counter()
    for a, ca in left.items():
        for b, cb in right.items():
            result[a+b] += ca*cb
    return result


def block_polynomial(degrees, principal_factors, matrix_weight):
    counts = Counter({0: 1})
    for _ in range(principal_factors):
        counts = convolve(counts, Counter(degrees[:88]))
    for _ in range(POWER-principal_factors):
        counts = convolve(counts, Counter(d*matrix_weight for d in degrees[88:]))
    return counts


def export(degrees):
    if len(degrees) != 120:
        raise ValueError('source basis must have 120 degrees')
    rows = []
    for j in range(POWER+1):
        weight = MATRIX_WEIGHTS[j]
        maximum = 8*j+weight*(POWER-j)
        polynomial = block_polynomial(degrees, j, weight)
        degree_counts = [polynomial[d] for d in range(maximum+1)]
        cuts = CUTOFFS[j]
        cost = sum(sum(degree_counts[:cut+1]) for cut in cuts)
        rows.append({'principal_factors': j,
                     'matrix_weight': weight,
                     'maximum_total_degree': maximum,
                     'cutoffs': list(cuts),
                     'degree_counts': degree_counts,
                     'word_multiplicity': comb(POWER, j),
                     'per_word_slices': cost})
    bound = sum(row['word_multiplicity']*row['per_word_slices'] for row in rows)
    if bound != EXPECTED_BOUND:
        raise ArithmeticError(f'unexpected five-power source bound: {bound}')
    return {'group': 'SL(2,F5)', 'coefficient_field': 'F4',
            'power': POWER, 'principal_dimension': 88,
            'complement_dimension': 32, 'rows': rows,
            'slice_upper_bound': bound,
            'method': 'three grouped tensor legs with exact integer degree counts',
            'improves_omega': False}


def verify(certificate, degrees):
    expected = export(degrees)
    if certificate != expected:
        raise ValueError('five-power source certificate differs from exact reconstruction')
    classes = Counter((int(index < 88), degree)
                      for index, degree in enumerate(degrees))
    by_word_degree = Counter()
    for labels in product(classes.items(), repeat=POWER):
        word = tuple(label[0][0] for label in labels)
        j = sum(word)
        weight = MATRIX_WEIGHTS[j]
        degree = sum(d if principal else d*weight
                     for (principal, d), multiplicity in labels)
        by_word_degree[word, degree] += prod(multiplicity for label, multiplicity in labels)
    if sum(by_word_degree.values()) != 120**POWER:
        raise ValueError('incomplete ordered source coordinate-class census')

    total = 0
    for row in certificate['rows']:
        j = row['principal_factors']
        maximum = row['maximum_total_degree']
        words = [word for word in product((0, 1), repeat=POWER) if sum(word) == j]
        polynomial = [by_word_degree[words[0], d] for d in range(maximum+1)]
        if any([by_word_degree[word, d] for d in range(maximum+1)] != polynomial
               for word in words):
            raise ValueError('block-word degree distributions differ')
        if polynomial != row['degree_counts']:
            raise ValueError('wrong degree distribution')
        cuts = row['cutoffs']
        if sum(cuts) < maximum-2:
            raise ValueError('three cutoffs do not cover every total degree')
        for triple in product(range(maximum+1), repeat=3):
            if sum(triple) <= maximum and all(d > c for d, c in zip(triple, cuts)):
                raise ValueError('uncovered source degree triple')
        cost = sum(sum(polynomial[:cut+1]) for cut in cuts)
        if cost != row['per_word_slices']:
            raise ValueError('wrong per-word slice count')
        total += len(words)*cost
    if total != certificate['slice_upper_bound']:
        raise ValueError('wrong source five-power slice bound')
    return {'slice_upper_bound': total,
            'coordinate_classes': len(classes),
            'ordered_class_tuples_checked': len(classes)**POWER,
            'coordinate_tuple_multiplicity_checked': 120**POWER,
            'block_words_checked': 2**POWER,
            'degree_triples_checked': sum((row['maximum_total_degree']+1)**3
                                          for row in certificate['rows'])}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    source = json.loads((ROOT/'results/sl2-finite-slices-2026-10-21/cover-certificate.json').read_text())
    certificate = export(source['basis_degrees'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(verify(certificate, source['basis_degrees']), indent=2))
