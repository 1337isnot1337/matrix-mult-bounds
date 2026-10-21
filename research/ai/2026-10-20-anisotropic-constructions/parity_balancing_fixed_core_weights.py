"""Exact graded extension bounds for specified monomial matrix cores.

The general bound is N_w-r_w+c_w. For these particular controls each
pair of core source selectors has at most one compatible source point
on the third leg, so r_w is an exact support count, not a numerical rank.
Only extensions keeping the two specified core maps are screened.
"""

import argparse
from collections import Counter
from itertools import product
import json
from pathlib import Path


PROFILE=[1,1,2,2,2,2,2,3,2,2,2,2,2,1,1]
TARGET_CHARGES=[[q for q,m in enumerate(PROFILE) for _ in range(m)],list(range(7))]
ROOT=Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT=ROOT/'results/anisotropic-constructions-2026-10-20/parity_balancing_fixed_core_weights.json'


def common_index(a,b,point):
    i,k,s=point
    return (i*(a+b-1)+k)*b+s


def common_coordinate(a,b,column):
    m=a+b-1
    return column//(m*b),(column//b)%m,column%b


def original_column(a,b,leg,column):
    i,k,s=common_coordinate(a,b,column)
    return (column,(s*a+i)*(a+b-1)+k,(k*b+s)*a+i)[leg]


def third_coordinate(a,b,x,y):
    """The unique third common coordinate, or None if the pair is absent."""
    i,k,s=common_coordinate(a,b,x)
    p,u,j=common_coordinate(a,b,y)
    q=k-p
    r=u-s
    if not (0<=q<b and 0<=r<a):
        return None
    return common_index(a,b,(r,i+j,q))


def build_case(name,vertices,embedding):
    a=b=8;n=len(vertices)
    common=[]
    for row,((i,q),(p,s)) in enumerate(product(vertices,repeat=2)):
        common.append([row,common_index(a,b,(i,q+p,s)),1])
    maps=[[[row,original_column(a,b,leg,column),value]
           for row,column,value in common] for leg in range(3)]
    return {'name':name,'source_lengths':[a,b],'physical_vertices':[list(v) for v in vertices],
            'core_order':n,'core_vertex_charges':[i-q+7 for i,q in vertices],
            'core_embedding_in_M27':embedding,'target_vertex_charges':TARGET_CHARGES,
            'common_coordinate_map':common,'maps':maps}


def validate_maps(data):
    a,b=data['source_lengths'];n=data['core_order'];N=a*b*(a+b-1)
    if any(type(x) is not int or x<1 for x in (a,b,n)):
        raise ValueError('Positive integer dimensions are required')
    common=data['common_coordinate_map']
    if not isinstance(common,list) or len(common)!=n*n:
        raise ValueError('Exactly one source selector per core matrix unit is required')
    rows={};columns=set()
    for row,column,value in common:
        if any(type(x) is not int for x in (row,column,value)):
            raise ValueError('Integer selector triples are required')
        if not (0<=row<n*n and 0<=column<N) or value!=1:
            raise ValueError('A source selector is out of range or has a nonunit coefficient')
        if row in rows or column in columns:
            raise ValueError('Core selectors must have distinct rows and source columns')
        rows[row]=column;columns.add(column)
    if set(rows)!=set(range(n*n)):
        raise ValueError('A core target row is missing')
    if not isinstance(data.get('maps'),list) or len(data['maps'])!=3:
        raise ValueError('Exactly three original-order maps are required')
    for leg in range(3):
        expected=sorted((row,original_column(a,b,leg,column),1) for row,column in rows.items())
        if sorted(tuple(entry) for entry in data['maps'][leg])!=expected:
            raise ValueError('The actual map disagrees with its common-coordinate selectors')
    charges=data['core_vertex_charges'];embedding=data['core_embedding_in_M27']
    if len(charges)!=n or len(embedding)!=n or len(set(embedding))!=n:
        raise ValueError('Unexpected core vertex data')
    if data['target_vertex_charges']!=TARGET_CHARGES:
        raise ValueError('This certificate uses the specified M27 plus M7 torus profile')
    if any(not 0<=vertex<27 or TARGET_CHARGES[0][vertex]!=charge
           for vertex,charge in zip(embedding,charges)):
        raise ValueError('The core embedding has the wrong vertex charges')
    for row,column in rows.items():
        i,k,s=common_coordinate(a,b,column)
        if i+s-k!=charges[row//n]-charges[row%n]:
            raise ArithmeticError('A core selector violates the torus weights')
    return rows


def complete_source_replay(a,b,rows):
    inverse={column:row for row,column in rows.items()};actual=Counter();count=0
    for i,p,r in product(range(a),repeat=3):
        for q,s,j in product(range(b),repeat=3):
            point=(common_index(a,b,(i,p+q,s)),common_index(a,b,(p,r+s,j)),
                   common_index(a,b,(r,i+j,q)))
            count+=1
            if all(column in inverse for column in point):
                actual[tuple(inverse[column] for column in point)]+=1
    return actual,count


def verify_case(data,full_source_check=True):
    a,b=data['source_lengths'];n=data['core_order'];N=a*b*(a+b-1)
    rows=validate_maps(data);inverse={column:row for row,column in rows.items()}
    actual=Counter();supported=set();pair_count=0
    for xrow,yrow in product(range(n*n),repeat=2):
        z=third_coordinate(a,b,rows[xrow],rows[yrow]);pair_count+=1
        if z is None:
            continue
        supported.add(z)
        if z in inverse:
            actual[xrow,yrow,inverse[z]]+=1
    expected=Counter({(i*n+j,j*n+k,k*n+i):1 for i,j,k in product(range(n),repeat=3)})
    if actual!=expected:
        raise ArithmeticError('The complete core matrix tensor identity fails')
    source_count=None
    if full_source_check:
        replayed,source_count=complete_source_replay(a,b,rows)
        if replayed!=actual:
            raise ArithmeticError('The independent full source replay disagrees with the pair formula')
    source_by_weight=Counter()
    support_by_weight={}
    for column in range(N):
        i,k,s=common_coordinate(a,b,column);source_by_weight[i+s-k]+=1
    for column in sorted(supported):
        i,k,s=common_coordinate(a,b,column)
        support_by_weight.setdefault(i+s-k,[]).append(column)
    core_by_weight=Counter(x-y for x,y in product(data['core_vertex_charges'],repeat=2))
    target_by_weight=Counter()
    for charges in data['target_vertex_charges']:
        target_by_weight.update(x-y for x,y in product(charges,repeat=2))
    blocks=[]
    for weight in sorted(target_by_weight):
        rank=len(support_by_weight.get(weight,[]))
        limit=source_by_weight[weight]-rank+core_by_weight[weight]
        blocks.append({'weight':weight,'source_dimension':source_by_weight[weight],
                       'exact_pair_contraction_rank':rank,
                       'core_target_dimension':core_by_weight[weight],
                       'required_full_target_dimension':target_by_weight[weight],
                       'fixed_core_extension_dimension_upper_bound':limit,
                       'violated':limit<target_by_weight[weight],
                       'supported_common_source_columns':support_by_weight.get(weight,[])})
    return {'core_matrix_identity_exact':True,'nonzero_core_coefficients':len(actual),
            'all_core_target_coefficients_accounted_for':n**6,
            'source_pair_rows_checked':pair_count,'full_source_terms_enumerated':source_count,
            'pair_rank_is_exact_coordinate_support_count':True,
            'total_pair_contraction_rank':len(supported),
            'global_fixed_core_dimension_upper_bound':N-len(supported)+n*n,
            'weight_blocks':blocks,
            'violated_weights':[block['weight'] for block in blocks if block['violated']],
            'fixed_core_extension_to_current_torus_profile_excluded':any(block['violated'] for block in blocks),
            'changing_core_maps_excluded':False,'arbitrary_source_degenerations_excluded':False,
            'new_exponent_established':False}


def build_report():
    definitions=[
        ('endpoint_M2',[(0,7),(7,0)],[0,26]),
        ('endpoint_M4',[(0,7),(1,7),(6,0),(7,0)],[0,1,25,26]),
        ('monotone_M6',[(0,7),(1,7),(2,7),(5,0),(6,0),(7,0)],[0,1,2,23,25,26]),
        ('repeated_short_index_M6',[(0,7),(1,7),(0,5),(7,2),(6,0),(7,0)],[0,1,2,24,25,26]),
        ('monotone_M8',[(i,7 if i<4 else 0) for i in range(8)],[0,1,2,4,21,23,25,26]),
    ]
    cases=[]
    for args in definitions:
        data=build_case(*args);data['verification']=verify_case(data);cases.append(data)
    return {'format':'graded-fixed-matrix-core-extension-v1',
            'general_bound':'D_w <= N_w - rank(Phi_w) + c_w',
            'scope':'The two specified core maps remain fixed; the rest of all maps may vary.',
            'cases':cases,'arbitrary_source_restriction_exclusion_claimed':False,
            'new_exponent_established':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=DEFAULT_OUTPUT)
    args=parser.parse_args();data=build_report()
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'controls':[
        {'name':case['name'],'pair_rank':case['verification']['total_pair_contraction_rank'],
         'global_dimension_bound':case['verification']['global_fixed_core_dimension_upper_bound'],
         'violated_weights':case['verification']['violated_weights'],
         'weight_zero':case['verification']['weight_blocks'][14]}
        for case in data['cases']]},indent=2))


if __name__=='__main__':
    main()
