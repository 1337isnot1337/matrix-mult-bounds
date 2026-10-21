"""Exact coordinate controls for the rank-one degree-13 rowspace proof.

The proof is in the accompanying note. This standard-library replay
checks its source slice identities, shared coordinates, target-form
independence and dimension counts; it is not a formal proof assistant.
"""

from collections import Counter
from itertools import product
import json
from pathlib import Path


PROFILE=[1,1,2,2,2,2,2,3,2,2,2,2,2,1,1]
CHARGES=[q for q,m in enumerate(PROFILE) for _ in range(m)]
ROOT=Path(__file__).resolve().parents[3]
OUTPUT=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_rankone_13_chain.json'


def coordinate(i,k,s):
    return [i,k,s]


def physical_basis(q):
    return [(i,j) for i,j in product(range(8),repeat=2) if i-j==q-7]


def r_coordinates(q):
    return [coordinate(0,7+i,j) for i,j in physical_basis(q)]


def c_coordinates(q):
    return [coordinate(i,7+j,0) for i,j in physical_basis(q)]


def k_coordinates(q):
    return [coordinate(i,6+j,0) for i,j in physical_basis(q)]


def physical_matrix(point):
    i,k,s=point
    return {(i,q,p,s):1 for p,q in product(range(8),repeat=2) if p+q==k}


def full_source_slice(point):
    actual=Counter()
    for i,p,r in product(range(8),repeat=3):
        for q,s,j in product(range(8),repeat=3):
            if (i,p+q,s)==tuple(point):
                actual[((p,r+s,j),(r,i+j,q))]+=1
    return actual


def sliced_factorization(kind):
    right=c_coordinates if kind=='extreme' else k_coordinates
    return Counter((tuple(left),tuple(other)) for q in range(15)
                   for left,other in zip(r_coordinates(q),right(q)))


def build():
    vertices={q:[i for i,charge in enumerate(CHARGES) if charge==q] for q in range(15)}
    low,pred,high=vertices[0][0],vertices[13][0],vertices[14][0]
    low_forms=[v*27+high for v in vertices[2]]+[v*27+pred for v in vertices[1]]
    excluded_forms=[low*27+v for v in vertices[12]]
    high_forms=[v*27+pred for v in vertices[12]]+[pred*27+high]
    return {'source_lengths':[8,8],'target_vertex_charges':CHARGES,
            'extreme_source_anchor':[7,0,7],'rank_one_source_anchor':[6,0,7],
            'target_extreme_unit':[high,low],'target_rank_one_unit':[pred,low],
            'low_recurrences':[{'q':q,'K_q':k_coordinates(q),'C_next':c_coordinates(q+1),
                                'multiplicity_sum':PROFILE[q]+PROFILE[q+1],
                                'available_rows':q+2} for q in range(7)],
            'C2':c_coordinates(2),'R12':r_coordinates(12),
            'K12':k_coordinates(12),'C13':c_coordinates(13),
            'forced_C2_target_forms':low_forms,
            'U12_target_forms':excluded_forms,
            'forced_C13_target_forms':high_forms,
            'fixed_rank_one_anchors_needed_on_adjacent_legs':2,
            'negative_extreme_assumptions_used':False,
            'third_rank_one_anchor_assumption_used':False,
            'nonzero_scalar_multiples_allowed':True,
            'arbitrary_degree13_pencils_excluded':False,
            'new_exponent_established':False}


def verify(data):
    if data['source_lengths']!=[8,8] or data['target_vertex_charges']!=CHARGES:
        raise ValueError('The certificate uses the stated source and target profile')
    if physical_matrix(data['extreme_source_anchor'])!={(7,0,0,7):1}:
        raise ArithmeticError('The extreme source anchor is not its stated rank-one matrix')
    if physical_matrix(data['rank_one_source_anchor'])!={(6,0,0,7):1}:
        raise ArithmeticError('The degree-13 source anchor is not its stated rank-one matrix')
    for name,point in [('extreme',data['extreme_source_anchor']),
                       ('predecessor',data['rank_one_source_anchor'])]:
        if full_source_slice(point)!=sliced_factorization(name):
            raise ArithmeticError('The full source slice disagrees with the R/C coordinate identity')
    expected=build()
    for key in ('low_recurrences','C2','R12','K12','C13','forced_C2_target_forms',
                'U12_target_forms','forced_C13_target_forms','target_extreme_unit','target_rank_one_unit'):
        if data[key]!=expected[key]:
            raise ArithmeticError('A stored coordinate or target-form identity is incorrect: '+key)
    for item in data['low_recurrences']:
        q=item['q']
        if item['K_q']!=item['C_next'][:q+1]:
            raise ArithmeticError('The low adjacent-charge recurrence has the wrong shift')
        if item['multiplicity_sum']>item['available_rows']:
            raise ArithmeticError('This profile already violates the low adjacent-charge dimension inequality')
    if data['R12'][0]!=data['C2'][0]:
        raise ArithmeticError('The first R12/C2 source coordinate is not shared')
    if data['K12'][1:]!=data['C13']:
        raise ArithmeticError('The high adjacent-charge identity has the wrong shift')
    low_forms=data['forced_C2_target_forms'];u12=data['U12_target_forms']
    high_forms=data['forced_C13_target_forms']
    if len(set(low_forms))!=len(data['C2']) or set(low_forms)&set(u12):
        raise ArithmeticError('The C2 rowspace saturation or disjointness check fails')
    if len(u12)!=len(data['R12'])-1:
        raise ArithmeticError('The remaining R12 square block has the wrong dimension')
    if len(set(high_forms))<=len(data['C13']):
        raise ArithmeticError('The final rowspace dimension contradiction is absent')
    return {'both_symbolic_source_slice_identities_exact':True,
            'source_terms_enumerated_per_slice':262144,'nonzero_slice_terms_per_slice':64,
            'all_seven_low_coordinate_shifts_exact':True,
            'low_adjacent_inequality':'m_q + m_(q+1) <= q+2, for 0 <= q <= 6',
            'C2_rowspace_dimension_forced':len(set(low_forms)),
            'C2_U12_coefficients_forced_zero':True,
            'remaining_R12_square_block_order':len(u12),
            'C13_physical_row_count':len(data['C13']),
            'C13_independent_target_forms_required':len(set(high_forms)),
            'rowspace_dimension_contradiction':[len(set(high_forms)),len(data['C13'])],
            'proof_scope':'Two adjacent fixed rank-one +13 maps and their +14 partners.',
            'arbitrary_degree13_pencils_excluded':False,'new_exponent_established':False}


def main():
    data=build();data['verification']=verify(data)
    OUTPUT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(OUTPUT),'verification':data['verification']},indent=2))


if __name__=='__main__':
    main()
