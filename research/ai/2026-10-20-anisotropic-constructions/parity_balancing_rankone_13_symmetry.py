"""Exact symmetries transferring the two-leg rank-one degree-13 theorem."""

from itertools import product
import json
from pathlib import Path


ROOT=Path(__file__).resolve().parents[3]
OUTPUT=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_symmetry.json'


def source_matrix(point):
    i,k,s=point
    return {(i,q,p,s) for p,q in product(range(8),repeat=2) if p+q==k}


def tau_point(point):
    i,k,s=point
    return s,k,i


def reflect_point(point):
    i,k,s=point
    return 7-i,14-k,7-s


def multiply(left,right):
    if left is None or right is None or left[1]!=right[0]:
        return None
    return left[0],right[1]


def sigma(n,unit):
    return None if unit is None else (n-1-unit[1],n-1-unit[0])


def kappa(n,unit):
    return None if unit is None else (n-1-unit[0],n-1-unit[1])


def report():
    source_basis=0;matrix_entries=0
    for point in product(range(8),range(15),range(8)):
        matrix=source_matrix(point)
        # S W^T S swaps the short physical factors after transposition.
        transformed={(s,p,q,i) for i,q,p,s in matrix}
        if transformed!=source_matrix(tau_point(point)):
            raise ArithmeticError('Transpose plus physical swap does not preserve the source')
        reflected={(7-i,7-q,7-p,7-s) for i,q,p,s in matrix}
        if reflected!=source_matrix(reflect_point(point)):
            raise ArithmeticError('Physical reflection does not preserve the source')
        i,k,s=point;it,kt,st=tau_point(point);ir,kr,sr=reflect_point(point)
        if it+st-kt!=i+s-k or ir+sr-kr!=-(i+s-k):
            raise ArithmeticError('A source symmetry has the wrong torus weight')
        source_basis+=1;matrix_entries+=len(matrix)
    target_pair_checks=0
    for n in (27,7):
        for i,j,k,l in product(range(n),repeat=4):
            left,right=(i,j),(k,l)
            if multiply(sigma(n,left),sigma(n,right))!=sigma(n,multiply(right,left)):
                raise ArithmeticError('Target transpose/reflection is not an anti-automorphism')
            if multiply(kappa(n,left),kappa(n,right))!=kappa(n,multiply(left,right)):
                raise ArithmeticError('Target reflection is not an automorphism')
            target_pair_checks+=1
    A=(6,0,7);plus=(7,0,7)
    if tau_point(plus)!=plus or tau_point(A)!=(7,0,6):
        raise ArithmeticError('The positive rank-one anchors transform incorrectly')
    if reflect_point(A)!=(1,14,0) or reflect_point(tau_point(A))!=(0,14,1):
        raise ArithmeticError('The negative rank-one anchors transform incorrectly')
    cases=[
        {'type':'positive_R','target_unit':[25,0],'source_coordinate':list(A),
         'extreme_target_unit':[26,0],'extreme_source_coordinate':list(plus)},
        {'type':'positive_Q','target_unit':list(sigma(27,(25,0))),
         'source_coordinate':list(tau_point(A)),
         'extreme_target_unit':[26,0],'extreme_source_coordinate':list(plus)},
        {'type':'negative_R','target_unit':list(kappa(27,(25,0))),
         'source_coordinate':list(reflect_point(A)),
         'extreme_target_unit':[0,26],'extreme_source_coordinate':list(reflect_point(plus))},
        {'type':'negative_Q','target_unit':list(kappa(27,sigma(27,(25,0)))),
         'source_coordinate':list(reflect_point(tau_point(A))),
         'extreme_target_unit':[0,26],'extreme_source_coordinate':list(reflect_point(plus))},
    ]
    return {'source_basis_coordinates_checked':source_basis,
            'source_matrix_basis_entries_checked':matrix_entries,
            'target_matrix_unit_pairs_checked_per_identity':target_pair_checks,
            'tau_preserves_source_weights':True,'reflection_reverses_source_weights':True,
            'tau_and_sigma_reverse_trace_order':True,
            'tau_transfer_requires_reversing_leg_order':True,
            'rank_one_types':cases,
            'each_type_can_occur_on_at_most_one_leg':True,
            'mixed_type_patterns_excluded':False,
            'general_torus_restriction_excluded':False,'new_exponent_established':False}


if __name__=='__main__':
    data=report();OUTPUT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(OUTPUT),**data},indent=2))
