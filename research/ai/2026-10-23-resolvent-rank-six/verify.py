"""Exact integer replay of the fixed-resolvent rank-six locus certificate."""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
ROWS = [0, 7, 14, 21, 22, 23]


def multiply(a, b):
    result = [[0] * len(b[0]) for _ in a]
    for i, row in enumerate(a):
        for k, value in enumerate(row):
            if value:
                for j, coefficient in enumerate(b[k]):
                    result[i][j] += value * coefficient
    return result


def combine(basis, coefficients):
    return [[sum(c * m[i][j] for c, m in zip(coefficients, basis))
             for j in range(len(basis[0][0]))] for i in range(len(basis[0]))]


def source():
    """Reconstruct the literal outer slices and inverse over Q, without imports."""
    labels = [(i, s) for i in range(4) for s in range(4)]
    slices = []
    for i, s in labels:
        matrix = [[0] * 28 for _ in range(28)]
        for j in range(4):
            for r in range(4):
                matrix[7*j+s+r][4*(i+j)+r] = 1
        slices.append(matrix)
    unit = combine(slices, [int(i+s == 3) for i, s in labels])
    work = [[Fraction(x) for x in row] + [Fraction(i == j) for j in range(28)]
            for i, row in enumerate(unit)]
    for j in range(28):
        pivot = next(i for i in range(j, 28) if work[i][j])
        work[j], work[pivot] = work[pivot], work[j]
        scale = work[j][j]
        work[j] = [x/scale for x in work[j]]
        for i in range(28):
            if i != j:
                scale = work[i][j]
                work[i] = [x-scale*y for x,y in zip(work[i],work[j])]
    if any(x.denominator != 1 for row in work for x in row):
        raise ValueError('source inverse is not integral')
    inverse = [[int(x) for x in row[28:]] for row in work]
    identity = [[int(i == j) for j in range(28)] for i in range(28)]
    if multiply(unit,inverse) != identity or multiply(inverse,unit) != identity:
        raise ValueError('source inverse identity failed')
    high = [multiply(slices[0],multiply(inverse,m)) for m in slices]
    if combine(high,[int(i+s == 3) for i,s in labels]) != slices[0]:
        raise ValueError('gauge identity failed')
    return slices, high, inverse


def replay(certificate, slices, high):
    labels = [['g',i,s] for i in range(4) for s in range(4)]
    labels += [['f',i,s] for i in range(4) for s in range(4) if (i,s) != (0,3)]
    if (certificate.get('size') != 8 or certificate.get('dimension') != 31
            or certificate.get('labels') != labels
            or certificate.get('remaining_dimension') != 5
            or len(certificate.get('stages',[])) != 26):
        raise ValueError('wrong certificate coverage')
    basis = slices + [m for i,m in enumerate(high) if i != 3]
    coordinates = [[int(i == j) for i in range(31)] for j in range(31)]
    for stage in certificate['stages']:
        form, pivot, minor = stage['form'],stage['pivot'],stage['minor']
        if (len(form) != len(basis) or any(type(x) is not int for x in form)
                or type(pivot) is not int or not 0 <= pivot < len(basis)
                or form[pivot] not in (-1,1)):
            raise ValueError('invalid unit substitution')
        if (len(minor) != 8 or any(len(pair) != 2 for pair in minor)
                or any(type(x) is not int or not 0 <= x < 28 for pair in minor for x in pair)
                or len({r for r,c in minor}) != 8 or len({c for r,c in minor}) != 8):
            raise ValueError('invalid minor indices')
        for n,(r,c) in enumerate(minor):
            entries = [m[r][c] for m in basis]
            if entries != form and entries != [-x for x in form]:
                raise ValueError('wrong diagonal form')
            if any(m[r][cc] for _,cc in minor[n+1:] for m in basis):
                raise ValueError('nonzero upper triangle')
        coefficients = [(i,-form[i]//form[pivot]) for i in range(len(basis)) if i != pivot]
        basis = [combine([basis[i],basis[pivot]],[1,c]) for i,c in coefficients]
        coordinates = [[x+c*y for x,y in zip(coordinates[i],coordinates[pivot])]
                       for i,c in coefficients]
    expected = []
    for i in range(4):
        expected.append([int(label == ['f',i,0]) for label in labels])
    expected.append([-int(label == ['g',1,0]) + int(label in [['f',1,3],['f',2,2],['f',3,1]])
                     for label in labels])
    if coordinates != expected:
        raise ValueError('wrong residual parameter space')
    if any(m[r][c] for m in basis for r in range(28) if r not in ROWS for c in range(28)):
        raise ValueError('residual space escapes common six-dimensional image')
    if {r for m in basis for r in range(28) if any(m[r])} != set(ROWS):
        raise ValueError('common image coordinates are incomplete')
    return basis


def check_sources():
    pins = json.loads((PACKAGE/'sources.json').read_text())
    for item in pins['local_dependencies']:
        if hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('source pin mismatch: '+item['path'])
    return len(pins['local_dependencies'])


def verify(certificate=None):
    pins = check_sources()
    slices,high,inverse = source()
    certificate = certificate if certificate is not None else json.loads((PACKAGE/'certificate.json').read_text())
    basis = replay(certificate,slices,high)
    # Replay the predecessor's 31 six-minors separately in its unchanged tests.
    return {'schema':'resolvent-rank-six-verification-v1', 'source_pins':pins,
            'integer_inverse_verified':True, 'minor_size':8, 'elimination_stages':26,
            'mixed_low_rank_dimension':len(basis), 'pure_high_low_rank_dimension':4,
            'common_image_coordinates_before_unit_inverse':ROWS,
            'full_low_rank_dimension':17, 'nonzero_rank':6, 'rank_seven_exists':False,
            'field':'every field for the locus and rank gap',
            'critical_compression_field':'algebraically closed fields',
            'critical_compression_minimum_image_dimension':111,
            'independent_review':False, 'improves_omega':False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    result = json.dumps(verify(),indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(result)
    else:
        print(result,end='')
