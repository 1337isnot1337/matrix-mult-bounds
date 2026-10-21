"""Replay complete ordinary or monomial-Laurent Q64 search coefficients.

The source is Q(6,4) plus exactly r scalar summands. Floating-point
replay does not turn any search result into an exact certificate.
"""
import argparse
from collections import Counter
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from math import fsum, sqrt
from pathlib import Path

from q54_numeric_replay import contract, integer_control


def contraction(maps, auxiliary_rank):
    shapes = [(25, 36+auxiliary_rank), (20, 36+auxiliary_rank), (20, 36+auxiliary_rank)]
    if len(maps) != 3 or any(len(matrix) != rows or any(len(row) != cols for row in matrix)
                             for matrix, (rows, cols) in zip(maps, shapes)):
        raise ValueError('Map dimensions do not match Q64 plus the declared scalar cost.')
    base = [[row[:36] for row in matrix] for matrix in maps]
    actual, target = contract(6, 4, 5, base)
    for term in range(auxiliary_rank):
        columns = [[(i, row[36+term]) for i, row in enumerate(matrix) if row[36+term]]
                   for matrix in maps]
        for (i,a), (j,b), (k,c) in product(*columns):
            actual[(i*20+j)*20+k] += a*b*c
    return actual, target


def row_powers():
    return [[-int(i==4)-int(k==4) for i in range(5) for k in range(5)],
            [int(i==4) for i in range(5) for j in range(4)],
            [int(k==4) for j in range(4) for k in range(5)]]


def degrees(powers):
    if list(map(len,powers)) != [25,20,20] or any(type(x) is not int for axis in powers for x in axis):
        raise ValueError('Every Laurent row power must be an integer in the stated format.')
    return [a+b+c for a,b,c in product(*powers)]


def exact_controls():
    # The auxiliary cost 101 is explicit: 100 naive matrix terms and one
    # extra positive-power term. This is a verifier calibration only.
    maps = [[[0]*137 for _ in range(rows)] for rows in [25,20,20]]
    for term,(i,j,k) in enumerate(product(range(5),range(4),range(5))):
        for axis,row in enumerate([5*i+k,4*i+j,5*j+k]):
            maps[axis][row][36+term] = 1
    for axis,row in enumerate([0,16,0]):
        maps[axis][row][136] = 1
    actual,target = contraction(maps,101)
    power = degrees(row_powers())
    if any(a != t for a,t,p in zip(actual,target,power) if p <= 0):
        raise ArithmeticError('The exact Laurent positive control failed.')
    if sum(a != t for a,t in zip(actual,target)) != 1:
        raise ArithmeticError('The positive-power control did not remain non-ordinary.')
    corrupted = deepcopy(maps)
    for matrix in corrupted:
        for row in matrix:
            row[136] = 0
    for axis,row in enumerate([24,0,0]):
        corrupted[axis][row][136] = 1
    bad,_ = contraction(corrupted,101)
    if not any(a != t for a,t,p in zip(bad,target,power) if p < 0):
        raise ArithmeticError('The deliberately introduced pole was not detected.')
    return {'integer_Q22_control':integer_control(),
            'laurent_control_source':'Q(6,4) direct sum D_101; all Q columns map to zero',
            'laurent_control_scalar_cost':101,'all_integer_positions_checked':10000,
            'nonzero_positive_power_permitted':True,'negative_power_error_detected':True,
            'control_is_exponent_improvement':False}


def replay(path):
    raw=Path(path).read_bytes()
    point=json.loads(raw)
    if point.get('exact_coefficient_certificate') is not False:
        raise ValueError('Search artifacts must remain explicitly numerical.')
    rank=point.get('auxiliary_rank',0)
    if type(rank) is not int or rank < 0:
        raise ValueError('A nonnegative integer scalar cost is required.')
    real,imag=point['maps_real'],point['maps_imag']
    if len(real)!=3 or len(imag)!=3 or any(len(rr)!=len(ii) or any(len(r)!=len(i) for r,i in zip(rr,ii))
                                        for rr,ii in zip(real,imag)):
        raise ValueError('Real and imaginary map arrays have different dimensions.')
    maps=[[[complex(r,i) for r,i in zip(rr,ii)] for rr,ii in zip(rm,im)] for rm,im in zip(real,imag)]
    actual,target=contraction(maps,rank)
    power=degrees(point['map_row_powers']) if 'map_row_powers' in point else [0]*10000
    if any(t for t,p in zip(target,power) if p != 0):
        raise ValueError('The declared powers do not preserve the target tensor.')
    differences=[a-t for a,t in zip(actual,target)]
    selected=[x for x,p in zip(differences,power) if p <= 0]
    relative=sqrt(fsum(abs(x)**2 for x in selected)/100)
    expected=point.get('relative_nonpositive_coefficient_error',point.get('relative_coefficient_error'))
    if expected is None or abs(relative-expected)>1e-9:
        raise ArithmeticError('The complete saved coefficient residual did not replay.')
    norms=[sqrt(fsum(abs(x)**2 for row in matrix for x in row)) for matrix in maps]
    return {'artifact':Path(path).name,'artifact_sha256':sha256(raw).hexdigest(),
            'source':'Q(6,4) direct sum D_r','auxiliary_rank':rank,
            'target':'M(5,4,5)','base_source_terms_reconstructed':576,
            'scalar_terms_reconstructed':rank,'all_target_positions_accounted':10000,
            'coefficient_position_counts_by_degree':dict(sorted(Counter(power).items())),
            'all_nonpositive_positions_checked':len(selected),
            'relative_nonpositive_coefficient_error':relative,
            'maximum_nonpositive_coefficient_error':max(map(abs,selected)),
            'reported_residual_difference':abs(relative-expected),
            'coefficient_norms_by_degree':{str(p):sqrt(fsum(abs(a)**2 for a,q in zip(actual,power) if p==q)) for p in sorted(set(power))},
            'map_frobenius_norms':norms,'numerical_replay_passes':True,
            'numerical_candidate_below_1e_minus_12':relative<1e-12,
            'exact_coefficient_certificate':False,'nonexistence_proved':False,'improves_omega':False}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints',type=Path,nargs='*')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report={'controls':exact_controls(),'replays':[replay(path) for path in args.checkpoints]}
    if args.output:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
