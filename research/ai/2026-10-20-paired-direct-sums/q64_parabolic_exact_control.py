"""Exact integer orientation controls for physical parabolic target gauges."""
from copy import deepcopy
from itertools import product
import json
from pathlib import Path
import sys

from q64_experiment_replay import contraction, degrees


def powers(grading='lexicographic'):
    alpha=[20*i for i in range(5)]; beta=[5*j for j in range(4)]; gamma=list(range(5))
    if grading=='refined':
        alpha[-1]+=1000
        gamma[-1]+=1000
    elif grading!='lexicographic':
        raise ValueError('Unknown grading')
    return [[-alpha[i]-gamma[k] for i in range(5) for k in range(5)],
            [alpha[i]-beta[j] for i in range(5) for j in range(4)],
            [beta[j]+gamma[k] for j in range(4) for k in range(5)]]


def control_maps():
    # All native Q64 columns are zero. Cost 103 is an explicit calibration.
    maps=[[[0]*139 for _ in range(rows)] for rows in [25,20,20]]
    for term,(i,j,k) in enumerate(product(range(5),range(4),range(5))):
        for axis,row in enumerate([5*i+k,4*i+j,5*j+k]):
            maps[axis][row][36+term]=1
    for term,point in enumerate([(0,4,0),(0,0,5),(0,0,1)],136):
        for axis,row in enumerate(point):
            maps[axis][row][term]=1
    return maps


def shear(maps,factor,new,old,value):
    out=deepcopy(maps)
    if factor=='i':
        pairs=[(0,5*new+k,5*old+k,value) for k in range(5)]
        pairs += [(1,4*old+j,4*new+j,-value) for j in range(4)]
    elif factor=='j':
        pairs=[(1,4*i+new,4*i+old,value) for i in range(5)]
        pairs += [(2,5*old+k,5*new+k,-value) for k in range(5)]
    elif factor=='k':
        pairs=[(0,5*i+new,5*i+old,value) for i in range(5)]
        pairs += [(2,5*j+old,5*j+new,-value) for j in range(4)]
    else:
        raise ValueError('Unknown physical factor')
    for axis,target,source,coefficient in pairs:
        out[axis][target]=[a+coefficient*b for a,b in zip(maps[axis][target],maps[axis][source])]
    return out


def exact_controls():
    source=control_maps(); exponent=degrees(powers())
    actual,target=contraction(source,103)
    assert all(a==t for a,t,p in zip(actual,target,exponent) if p<=0)
    transformed=source
    for factor,value in [('i',2),('j',-1),('k',3)]:
        transformed=shear(transformed,factor,1,2,value)
    actual,_=contraction(transformed,103)
    assert all(a==t for a,t,p in zip(actual,target,exponent) if p<=0)
    positive=sum(a!=0 for a,p in zip(actual,exponent) if p>0)
    rejected={}
    for factor in ['i','j','k']:
        bad,_=contraction(shear(source,factor,1,0,1),103)
        rejected[factor]=sum(a!=t for a,t,p in zip(bad,target,exponent) if p<=0)
        assert rejected[factor]>0
    return {'source':'Q(6,4) direct sum D_103; Q columns vanish','scalar_cost':103,
            'all_target_positions_checked_per_control':10000,
            'upper_triangular_physical_shears_preserve_exact_acceptance':True,
            'nonzero_positive_coefficients_after_shears':positive,
            'opposite_shear_nonpositive_failure_counts':rejected,
            'control_is_exponent_improvement':False}


if __name__=='__main__':
    print(json.dumps(exact_controls(),indent=2))
