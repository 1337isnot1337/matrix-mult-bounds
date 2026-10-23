"""Separate integer-class replay of the full nonsplit source cube cover."""
from collections import Counter
from itertools import product
from math import comb, prod


def export(degrees):
    rows = []
    for j, a, cuts in [(0, 1, (0, 0, 1)), (1, 2, (3, 3, 4)),
                       (2, 3, (5, 6, 6)), (3, 0, (7, 7, 8))]:
        counts = Counter({0: 1})
        for labels, scale, times in [(degrees[:88], 1, j), (degrees[88:], a, 3-j)]:
            histogram = Counter(d*scale for d in labels)
            for _ in range(times):
                following = Counter()
                for left, x in counts.items():
                    for right, y in histogram.items():
                        following[left+right] += x*y
                counts = following
        maximum = 8*j+a*(3-j)
        polynomial = [counts[d] for d in range(maximum+1)]
        cost = sum(sum(polynomial[:c+1]) for c in cuts)
        rows.append({'principal_factors': j, 'matrix_weight': a,
                     'maximum_total_degree': maximum, 'cutoffs': list(cuts),
                     'degree_counts': polynomial, 'word_multiplicity': comb(3, j),
                     'per_word_slices': cost})
    return {'group': 'SL(2,F5)', 'coefficient_field': 'F4', 'power': 3,
            'extra_C2': False, 'rows': rows,
            'slice_upper_bound': sum(row['word_multiplicity']*row['per_word_slices']
                                     for row in rows), 'improves_omega': False}


def verify(certificate, degrees):
    if (certificate['group'] != 'SL(2,F5)' or certificate['coefficient_field'] != 'F4'
            or certificate['power'] != 3 or certificate['extra_C2'] is not False):
        raise ValueError('wrong source cube')
    rows = certificate['rows']
    if [row['principal_factors'] for row in rows] != [0, 1, 2, 3]:
        raise ValueError('missing cube block')
    classes = Counter((int(a < 88), degrees[a]) for a in range(120))
    counts = Counter()
    for triple in product(classes.items(), repeat=3):
        word = tuple(label[0] for label, count in triple)
        j = sum(word)
        a = rows[j]['matrix_weight']
        degree = sum(d*(1 if principal else a) for (principal, d), count in triple)
        counts[word, degree] += prod(count for label, count in triple)
    if sum(counts.values()) != 120**3:
        raise ValueError('incomplete cube class multiplicity')
    total = 0
    for j, row in enumerate(rows):
        a = row['matrix_weight']
        if type(a) is not int or a < 0:
            raise ValueError('wrong nonnegative matrix weight')
        maximum = 8*j+a*(3-j)
        words = [word for word in product((0, 1), repeat=3) if sum(word) == j]
        polynomial = [counts[words[0], d] for d in range(maximum+1)]
        if (any([counts[word, d] for d in range(maximum+1)] != polynomial for word in words)
                or polynomial != row['degree_counts']
                or row['maximum_total_degree'] != maximum
                or row['word_multiplicity'] != len(words)):
            raise ValueError('wrong cube block counts')
        cuts = row['cutoffs']
        if len(cuts) != 3 or any(type(c) is not int or c < -1 for c in cuts):
            raise ValueError('wrong cube cutoff format')
        for triple in product(range(maximum+1), repeat=3):
            if sum(triple) <= maximum and all(d > c for d, c in zip(triple, cuts)):
                raise ValueError('uncovered cube degree triple')
        cost = sum(sum(count for d, count in enumerate(polynomial) if d <= c) for c in cuts)
        if cost != row['per_word_slices']:
            raise ValueError('wrong cube slice count')
        total += len(words)*cost
    if total != certificate['slice_upper_bound']:
        raise ValueError('wrong total cube slice count')
    return {'slice_upper_bound': total, 'coordinate_classes': len(classes),
            'class_triples_checked': len(classes)**3,
            'one_leg_coordinate_multiplicity_checked': 120**3}


def joint_target_cube(shape, scalars):
    a, b, c = shape
    volume = a*b*c
    return volume**2+3*scalars*volume*min(shape)+3*scalars**2*min(a*b, b*c, c*a)+scalars**3
