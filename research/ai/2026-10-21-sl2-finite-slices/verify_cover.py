"""Independent dense-field replay against the original nonsplit group.

No NumPy, optimizer, Peirce lift, radical pilot or prior support is used.
"""
import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path

N = 120


def field_product(a, b):
    polynomial = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                polynomial ^= 1 << (i+j)
    return polynomial ^ 7 if polynomial & 4 else polynomial


TABLE = [[field_product(a, b) for b in range(4)] for a in range(4)]
INVERSE = {1: 1, 2: 3, 3: 2}


def source_group():
    identity = (1, 0, 0, 1)
    matrices = [identity]+sorted(A for A in product(range(5), repeat=4)
                                 if (A[0]*A[3]-A[1]*A[2]) % 5 == 1 and A != identity)
    lookup = {A: i for i, A in enumerate(matrices)}
    multiplication = []
    for a, b, c, d in matrices:
        row = []
        for e, f, g, h in matrices:
            row.append(lookup[((a*e+b*g) % 5, (a*f+b*h) % 5,
                               (c*e+d*g) % 5, (c*f+d*h) % 5)])
        multiplication.append(row)
    return multiplication, [row.index(0) for row in multiplication]


def decode(text):
    value = int(text, 16)
    if value < 0 or value >> (2*N):
        raise ValueError('basis vector exceeds the coefficient field format')
    return [((value >> i) & 1) | (((value >> (N+i)) & 1) << 1) for i in range(N)]


def rank(vectors):
    span = {}
    for vector in vectors:
        row = list(vector)
        while any(row):
            pivot = max(i for i, value in enumerate(row) if value)
            a = row[pivot]
            if pivot not in span:
                span[pivot] = [TABLE[INVERSE[a]][b] for b in row]
                break
            row = [x ^ TABLE[a][y] for x, y in zip(row, span[pivot])]
    return len(span)


def coefficients(basis, multiplication, inverse):
    sparse = [[(g, value) for g, value in enumerate(row) if value] for row in basis]
    inverted = [[row[inverse[g]] for g in range(N)] for row in basis]
    for a in range(N):
        for b in range(N):
            value = [0]*N
            for g, x in sparse[a]:
                for h, y in sparse[b]:
                    value[multiplication[g][h]] ^= TABLE[x][y]
            active = [(g, x) for g, x in enumerate(value) if x]
            for c in range(N):
                coefficient = 0
                for g, x in active:
                    coefficient ^= TABLE[x][inverted[c][g]]
                if coefficient:
                    yield a, b, c, coefficient


def verify_cube(cube, degrees):
    if cube['power'] != 3 or cube['extra_C2'] is not True:
        raise ValueError('wrong cube source')
    rows = cube['rows']
    if [row['principal_factors'] for row in rows] != [0, 1, 2, 3]:
        raise ValueError('wrong cube block inventory')
    for row in rows:
        w = row['weights']
        if (set(w) != {'principal_scale', 'matrix_central', 'extra_C2'}
                or any(type(value) is not int or value <= 0 for value in w.values())):
            raise ValueError('wrong positive integer cube weights')
    # Count explicit one-leg coordinate classes with integer multiplicities.
    # This independent tuple count does not call polynomial multiplication.
    classes = Counter((int(a < 88), degrees[a], epsilon)
                      for a in range(N) for epsilon in range(2))
    counts = Counter()
    for triple in product(classes.items(), repeat=3):
        word = tuple(label[0] for label, count in triple)
        j = sum(word)
        w = rows[j]['weights']
        degree = sum(d*(w['principal_scale'] if principal else w['matrix_central'])
                     +epsilon*w['extra_C2'] for (principal, d, epsilon), count in triple)
        multiplicity = triple[0][1]*triple[1][1]*triple[2][1]
        counts[word, degree] += multiplicity
    if sum(counts.values()) != 240**3:
        raise ValueError('incomplete cube coordinate count')
    total, reports = 0, []
    for j, row in enumerate(rows):
        words = [word for word in product((0, 1), repeat=3) if sum(word) == j]
        w = row['weights']
        maximum = 8*w['principal_scale']*j+w['matrix_central']*(3-j)+3*w['extra_C2']
        polynomial = [counts[words[0], d] for d in range(maximum+1)]
        if any([counts[word, d] for d in range(maximum+1)] != polynomial for word in words):
            raise ValueError('cube block-word distributions differ')
        if row['word_multiplicity'] != len(words) or row['degree_counts'] != polynomial:
            raise ValueError('wrong cube multiplicity or degree counts')
        cuts = row['cutoffs']
        if len(cuts) != 3 or any(type(c) is not int or c < -1 for c in cuts):
            raise ValueError('wrong cube cutoff format')
        for triple in product(range(maximum+1), repeat=3):
            if sum(triple) <= maximum and all(d > c for d, c in zip(triple, cuts)):
                raise ValueError('cube cutoffs leave a possible source term uncovered')
        cost = sum(sum(value for degree, value in enumerate(polynomial) if degree <= cut) for cut in cuts)
        if cost != row['per_word_slices']:
            raise ValueError('wrong cube slice count')
        total += len(words)*cost
        reports.append({'principal_factors': j, 'word_multiplicity': len(words),
                        'per_word_slices': cost})
    volume = cube['rectangular_volume_upper_bound']
    if (total != cube['slice_upper_bound'] or total != 6155844
            or type(volume) is not int or not volume**2 <= total < (volume+1)**2):
        raise ValueError('wrong cube target or volume comparison')
    return {'power': 3, 'extra_C2': True, 'slice_upper_bound': total,
            'one_leg_coordinate_multiplicity_checked': 240**3,
            'coordinate_classes': len(classes), 'class_triples_counted': len(classes)**3,
            'blocks': reports, 'rectangular_volume_upper_bound': volume,
            'selected_target_volume': 2535, 'selected_cyclic_target_slice_rank': 2535**2,
            'strict_gap': 2535**2-total}


def verify(certificate):
    if (certificate['schema'] != 'nonsplit-coordinate-slice-cover-v1'
            or certificate['coefficient_field'] != 'F2[w]/(w^2+w+1)'
            or certificate['group'] != 'SL(2,F5)'
            or certificate['group_ordering'] != 'identity followed by lexicographic determinant-one matrices'):
        raise ValueError('wrong source or coefficient field')
    basis = [decode(value) for value in certificate['basis']]
    if len(basis) != N or rank(basis) != N:
        raise ValueError('basis is singular')
    degrees = certificate['basis_degrees']
    if (len(degrees) != N or any(type(d) is not int or d < 0 for d in degrees)
            or Counter(degrees[:88]) != Counter({0: 9, 1: 8, 2: 10, 3: 8, 4: 18,
                                                5: 8, 6: 10, 7: 8, 8: 9})
            or Counter(degrees[88:]) != Counter({0: 16, 1: 16})):
        raise ValueError('wrong block degree dimensions')
    covers = certificate['covers']
    if not covers or len({cover['extra_C2'] for cover in covers}) != len(covers):
        raise ValueError('missing or duplicate source cover')
    checked = []
    for cover in covers:
        extra = cover['extra_C2']
        if type(extra) is not bool:
            raise ValueError('wrong extra-factor format')
        selected = cover['selected_coordinates']
        dimension = N*(2 if extra else 1)
        if (len(selected) != 3 or any(len(row) != len(set(row)) for row in selected)
                or any(type(a) is not int or not 0 <= a < dimension for row in selected for a in row)):
            raise ValueError('wrong selected coordinate format')
        count = sum(map(len, selected))
        if count != cover['slice_upper_bound']:
            raise ValueError('wrong declared slice count')
        checked.append((extra, [set(row) for row in selected], count))
    multiplication, inverse = source_group()
    central = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0))
    # Recompute the full extra C2 trace in (1,1+z); retain the 000 term.
    actual_central = []
    for triple in product((0, 1), repeat=3):
        row = [1, 0]
        for epsilon in triple:
            row = [row[0] ^ row[1]*epsilon, row[1] ^ row[0]*epsilon]
        if row[0]:
            actual_central.append(triple)
    if tuple(actual_central) != central:
        raise ValueError('wrong full central trace')
    nonzero, covered = 0, [0]*len(checked)
    for a, b, c, coefficient in coefficients(basis, multiplication, inverse):
        nonzero += 1
        if max(a, b, c) < 88:
            maximum = 8
        elif min(a, b, c) >= 88:
            maximum = 1
        else:
            raise ValueError('cross-block original source term')
        if degrees[a]+degrees[b]+degrees[c] > maximum:
            raise ValueError('original source exceeds the claimed block degree')
        for i, (extra, selected, count) in enumerate(checked):
            triples = [(a, b, c)] if not extra else [tuple(2*x+d for x, d in zip((a, b, c), digits))
                                                   for digits in central]
            for triple in triples:
                if all(label not in selected[leg] for leg, label in enumerate(triple)):
                    raise ValueError('uncovered original source coefficient')
                covered[i] += 1
    if certificate['exponent_improvement'] is not False:
        raise ValueError('not an exponent improvement')
    cube = verify_cube(certificate['cube'], degrees)
    return {'coefficient_field': 'F4', 'group': 'SL(2,F5)', 'basis_rank': N,
            'original_group_coefficients_checked': N**3,
            'original_group_nonzero_coefficients': nonzero,
            'covers': [{'extra_C2': extra, 'source_dimension': N*(2 if extra else 1),
                        'slice_upper_bound': count, 'nonzero_terms_covered': covered[i]}
                       for i, (extra, selected, count) in enumerate(checked)],
            'extra_C2_cube': cube,
            'scope': 'Explicit finite slice upper bounds only. Target exclusions '
                     'require the stated field-transfer and finite target lower-bound proof.',
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
