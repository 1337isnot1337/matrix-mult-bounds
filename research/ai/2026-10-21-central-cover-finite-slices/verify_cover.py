"""Replay the full A5 source and count every coordinate in the finite covers.

Uses the maintained F4 scalar/convolution primitives from the preceding
certificate, but no discovery data, producer polynomial code or optimizer.
"""
import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIELD_PATH = ROOT/'research/ai/2026-10-21-a5-peirce/verify_tight.py'
spec = importlib.util.spec_from_file_location('finite_cover_F4', FIELD_PATH)
field = importlib.util.module_from_spec(spec)
spec.loader.exec_module(field)


def source_support(basis):
    _, multiplication, inverse = field.alternating_group()
    for a in range(60):
        for b in range(60):
            value = field.convolution(basis[a], basis[b], multiplication)
            active = [(g, v) for g, v in enumerate(value) if v]
            for c in range(60):
                coefficient = 0
                for g, v in active:
                    coefficient ^= field.TABLE[v][basis[c][inverse[g]]]
                if coefficient:
                    yield a, b, c, coefficient


def count_cover(degrees, n, rows):
    if len(rows) != n+1 or [row['principal_factors'] for row in rows] != list(range(n+1)):
        raise ValueError('wrong block-word rows')
    # Enumerate every one-leg coordinate, including all central and matrix
    # choices. This is separate from the producer's polynomial multiplication.
    counts = Counter()
    labels = [(int(a < 44), degrees[a]+epsilon)
              for a in range(60) for epsilon in range(2)]
    for coordinates in product(labels, repeat=n):
        word = tuple(principal for principal, _ in coordinates)
        counts[word, sum(degree for _, degree in coordinates)] += 1
    total = 0
    details = []
    for j, row in enumerate(rows):
        words = [word for word in product((0, 1), repeat=n) if sum(word) == j]
        if row['word_multiplicity'] != len(words):
            raise ValueError('wrong word multiplicity')
        maximum = 4*j+n
        polynomial = [counts[words[0], d] for d in range(maximum+1)]
        for word in words:
            if [counts[word, d] for d in range(maximum+1)] != polynomial:
                raise ValueError('block-word degree distributions differ')
        matrix_factor = 16**(n-j)
        if polynomial != [matrix_factor*c for c in row['degree_counts_without_matrix']]:
            raise ValueError('wrong degree polynomial')
        cuts = row['cutoffs']
        if len(cuts) != 3 or any(type(c) is not int for c in cuts):
            raise ValueError('wrong cutoff format')
        # Check the cover itself, not just a claimed cutoff sum.
        for triple in product(range(maximum+1), repeat=3):
            if sum(triple) <= maximum and all(d > c for d, c in zip(triple, cuts)):
                raise ValueError('cutoffs leave a possible source term uncovered')
        slices = sum(sum(count for degree, count in enumerate(polynomial) if degree <= cut)
                     for cut in cuts)
        leg_dimension = sum(polynomial)
        if (row['degree_cover_slices'] != slices or row['whole_leg_slices'] != leg_dimension
                or row['selected_slices'] != min(slices, leg_dimension)):
            raise ValueError('wrong slice count')
        total += len(words)*min(slices, leg_dimension)
        details.append({'principal_factors': j, 'words': len(words),
                        'per_word_slices': min(slices, leg_dimension)})
    if sum(counts.values()) != 120**n:
        raise ValueError('one-leg enumeration is incomplete')
    return total, details


def verify(certificate):
    if (certificate['schema'] != 'central-cover-finite-slices-v1'
            or certificate['group'] != 'A5 x C2'
            or certificate['coefficient_field'] != 'F2[w]/(w^2+w+1)'):
        raise ValueError('wrong source or field')
    origin = certificate['basis_source']
    if origin['path'] != 'results/a5-peirce-2026-10-21/tight-certificate.json':
        raise ValueError('wrong basis source path')
    raw = (ROOT/origin['path']).read_bytes()
    prior = json.loads(raw)
    if origin['sha256'] != sha256(raw).hexdigest() or certificate['basis'] != prior['basis']:
        raise ValueError('wrong pinned basis source')
    basis = [field.decode(v) for v in certificate['basis']]
    if len(basis) != 60 or field.rank(basis) != 60:
        raise ValueError('basis is singular')
    degrees = certificate['degrees']
    if (len(degrees) != 60 or any(type(d) is not int or d < 0 for d in degrees)
            or Counter(degrees[:44]) != Counter({0: 9, 1: 8, 2: 10, 3: 8, 4: 9})
            or any(degrees[44:])):
        raise ValueError('wrong principal degree dimensions')
    terms = Counter()
    matrix = set()
    for a, b, c, coefficient in source_support(basis):
        if max(a, b, c) < 44:
            degree = degrees[a]+degrees[b]+degrees[c]
            if degree > 4:
                raise ValueError('principal source term exceeds degree four')
            terms['principal', degree] += 1
        elif min(a, b, c) >= 44:
            matrix.add((a, b, c, coefficient))
        else:
            raise ValueError('source has a cross-block term')
    expected_matrix = {(44+4*i+j, 44+4*j+k, 44+4*k+i, 1)
                       for i, j, k in product(range(4), repeat=3)}
    if matrix != expected_matrix:
        raise ValueError('wrong full matrix block')
    # In F4[C2], epsilon=1+z has square zero. The coefficient-of-identity
    # trace of epsilon^d is one exactly for d=0 or d=1.
    central = []
    for triple in product((0, 1), repeat=3):
        value = [1, 0]
        for epsilon in triple:
            factor = [1, epsilon]
            value = [value[0]*factor[0] ^ value[1]*factor[1],
                     value[0]*factor[1] ^ value[1]*factor[0]]
        if value[0]:
            central.append(list(triple))
    if any(sum(triple) > 1 for triple in central) or len(central) != 4:
        raise ValueError('wrong central source support')
    covers = certificate['covers']
    if [cover['power'] for cover in covers] != [1, 2, 3]:
        raise ValueError('wrong finite power inventory')
    reports = []
    for cover in covers:
        n = cover['power']
        bound, rows = count_cover(degrees, n, cover['rows'])
        if bound != cover['slice_upper_bound'] or cover['M10_power_slice_rank'] != 100**n:
            raise ValueError('wrong source or target comparison')
        reports.append({'power': n, 'slice_upper_bound': bound,
                        'target_slice_rank': 100**n, 'below_target': bound < 100**n,
                        'one_leg_coordinates_checked': 120**n, 'blocks': rows})
    if reports[-1]['slice_upper_bound'] != 973422 or not reports[-1]['below_target']:
        raise ValueError('cube exclusion failed')
    volume = certificate['rectangular_volume_upper_bound']
    if type(volume) is not int or not volume**2 <= 973422 < (volume+1)**2:
        raise ValueError('wrong rectangular volume bound')
    if certificate['exponent_improvement'] is not False:
        raise ValueError('not an exponent improvement')
    return {'source': 'F4[A5 x C2]', 'basis_rank': 60,
            'A5_coefficients_checked': 216000,
            'full_source_principal_terms_by_degree': {str(d): terms['principal', d] for d in (0, 2, 4)},
            'full_source_matrix_terms': len(matrix), 'central_support': central,
            'finite_covers': reports, 'cube_gap': 1000000-973422,
            'rectangular_volume_upper_bound': volume,
            'excluded_rectangular_examples': [[10, 10, 10], [9, 10, 11]],
            'scope': 'Excludes every M(a,b,c) with abc >= 987 from this split source by characteristic-two '
                     'degeneration, and coefficient-one coordinate/potential '
                     'constructions over C. Does not exclude general complex '
                     'degenerations or targets from the nonsplit central covers.',
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
