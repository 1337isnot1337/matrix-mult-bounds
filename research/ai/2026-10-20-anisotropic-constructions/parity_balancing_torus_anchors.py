"""Exact endpoint-slice initialization for the live A88 -> M27 plus M7 search.

All coefficients containing a target matrix unit of weight +14 or -14
are enforced, including their zero coefficients. Other coefficients are
not claimed to agree. The maps are concise and have denominator 64.
The entire source boundary is retained explicitly; no quotient or fixed
physical compression equation is asserted.
"""

import argparse
from collections import Counter,defaultdict
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


PROFILE=[1,1,2,2,2,2,2,3,2,2,2,2,2,1,1]
CHARGES=[[q for q,m in enumerate(PROFILE) for _ in range(m)],list(range(7))]
DENOMINATOR=64
ROOT=Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT=ROOT/'results/anisotropic-constructions-2026-10-20'/'parity_balancing_torus_anchor_seed.json'


def source_index(i,k,s):
    return (i*15+k)*8+s


def source_coordinate(index):
    return index//120,(index//8)%15,index%8


def original_column(axis,column):
    i,k,s=source_coordinate(column)
    if axis==0:
        return column
    if axis==1:
        return (s*8+i)*15+k
    return (k*8+s)*8+i


def boundary_columns():
    """Coordinates meeting a row or column of either physical endpoint."""
    boundary=set()
    for p,s in product(range(8),repeat=2):
        boundary.add(source_index(0,7+p,s))
        boundary.add(source_index(7,p,s))
    for i,q in product(range(8),repeat=2):
        boundary.add(source_index(i,7+q,0))
        boundary.add(source_index(i,q,7))
    return sorted(boundary)


def target_data():
    units=[];groups=defaultdict(list);offset=0
    for block,charges in enumerate(CHARGES):
        n=len(charges)
        for i,j in product(range(n),repeat=2):
            row=offset+i*n+j
            units.append((block,i,j));groups[charges[i]-charges[j]].append(row)
        offset+=n*n
    vertices={q:[i for i,x in enumerate(CHARGES[0]) if x==q] for q in range(15)}
    return units,dict(groups),vertices


def physical_charge_basis(q):
    return [(i,j) for i,j in product(range(8),repeat=2) if i-j==q-7]


def vector(*terms):
    result=defaultdict(F)
    for coefficient,row in terms:
        result[row]+=F(coefficient)
    return dict(result)


def row_pivots(matrix,prime=65521):
    basis={};indices=[]
    for index,row in enumerate(matrix):
        values=[x%prime for x in row]
        for column,pivot in sorted(basis.items()):
            scale=values[column]
            if scale:
                values=[(x-scale*y)%prime for x,y in zip(values,pivot)]
        column=next((i for i,x in enumerate(values) if x),None)
        if column is not None:
            scale=pow(values[column],-1,prime)
            basis[column]=[scale*x%prime for x in values]
            indices.append(index)
    return indices


def build(q1_mode='m4'):
    units,groups,vertices=target_data();low,high=0,26
    constraints={}
    def assign(row,column,value):
        key=(row,column);value=F(value)
        if key in constraints and constraints[key]!=value:
            raise ArithmeticError('Incompatible source boundary assignments')
        constraints[key]=value
    def assign_r(q,channels):
        basis=physical_charge_basis(q)
        if len(basis)!=len(channels):
            raise ValueError('Unexpected physical weight dimension')
        for (p,s),channel in zip(basis,channels):
            for row in groups[-q]:
                assign(row,source_index(0,7+p,s),channel.get(row,0))
    def assign_c(q,channels):
        basis=physical_charge_basis(q)
        if len(basis)!=len(channels):
            raise ValueError('Unexpected physical weight dimension')
        for (i,j),channel in zip(basis,channels):
            for row in groups[q-14]:
                assign(row,source_index(i,7+j,0),channel.get(row,0))
    def left(q):
        return [low*27+t for t in vertices[q]]
    def right(q):
        return [t*27+high for t in vertices[q]]
    assign_r(0,[vector((1,low*27+low))])
    assign_c(0,[vector((1,low*27+high))])
    assign_r(14,[vector((1,low*27+high))])
    assign_c(14,[vector((1,high*27+high))])
    # q=1 and13: the default agrees with the actual four-vertex M4
    # endpoint control. The old Hadamard choice is retained only as a
    # six-slice control; a fixed pair relation obstructs its completion.
    a,b=left(13)[0],right(1)[0]
    if q1_mode=='m4':
        assign_r(13,[vector((1,a)),{}])
        assign_c(1,[vector((1,a)),vector((1,b))])
        assign_r(1,[{},vector((1,left(1)[0]))])
        assign_c(13,[vector((1,right(13)[0])),{}])
    elif q1_mode=='hadamard':
        shared=vector((1,a),(1,b));difference=vector((1,a),(-1,b))
        assign_r(13,[shared,difference]);assign_c(1,[shared,difference])
        assign_r(1,[vector((F(1,2),left(1)[0])),vector((F(-1,2),left(1)[0]))])
        assign_c(13,[vector((F(1,2),right(13)[0])),vector((F(1,2),right(13)[0]))])
    else:
        raise ValueError('Unknown q1 channel mode')
    # q=2,...,6: one shared slack channel and disjoint additional
    # channels permit full rank high-R and low-C boundary matrices.
    channels_report=[]
    for q in range(2,7):
        other=14-q;d=q+1;c=PROFILE[q]
        arows,brows=left(other),right(q)
        rest=[row for row in groups[-other] if row not in arows+brows]
        extra=d-1-c
        if len(rest)<1+2*extra:
            raise ArithmeticError('Insufficient target slack coordinates')
        shared=rest[0];rslack=rest[1:1+extra];cslack=rest[1+extra:1+2*extra]
        if q==2 and q1_mode=='m4':
            # Keep E_(charge1,charge13) on its actual monotone-M4
            # physical coordinate. The shared channel can carry b_1;
            # it need not carry the interior target row s.
            assign_r(other,[vector((1,brows[0]))]+[vector((1,row)) for row in arows])
            assign_c(q,[vector((1,brows[0])),vector((1,shared)),vector((1,brows[1]))])
            assign_r(q,[vector((1,left(q)[0])),{},vector((1,left(q)[1]))])
            assign_c(other,[{}]+[vector((1,row)) for row in right(other)])
            channels_report.append({'vertex_charge':q,'shared_target_row':brows[0],
                                    'interior_M4_target_row':shared,
                                    'high_R_extra_rows':[],'low_C_extra_rows':[]})
            continue
        assign_r(other,[vector((1,row)) for row in [shared]+arows+rslack])
        assign_c(q,[vector((1,row)) for row in [shared]+brows+cslack])
        low_r=[{} for _ in range(d)];high_c=[{} for _ in range(d)]
        for channel,(u,v) in enumerate(zip(left(q),right(other)),1):
            low_r[channel]=vector((1,u));high_c[channel]=vector((1,v))
        assign_r(q,low_r);assign_c(other,high_c)
        channels_report.append({'vertex_charge':q,'shared_target_row':shared,
                                'high_R_extra_rows':rslack,'low_C_extra_rows':cslack})
    # The central charge pairs with itself. Two slack channels cancel
    # s*s^T exactly; three separate channels carry the target dot product.
    rest=[row for row in groups[-7] if row not in left(7)+right(7)]
    shared=rest[0]
    rs=[{}, {}, {}, {}, {}, {}, {}, {}]
    cs=[{}, {}, {}, {}, {}, {}, {}, {}]
    rs[0]=rs[1]=vector((1,shared))
    cs[0]=vector((1,shared));cs[1]=vector((-1,shared))
    for channel,(u,v) in enumerate(zip(left(7),right(7)),2):
        rs[channel]=vector((1,u));cs[channel]=vector((1,v))
    assign_r(7,rs);assign_c(7,cs)
    # Reversing both physical tensor indices preserves W and exchanges
    # the two endpoints. The target charge reversal preserves each MM block.
    for (row,column),value in list(constraints.items()):
        block,i,j=units[row];n=len(CHARGES[block]);offset=0 if block==0 else 729
        target_row=offset+(n-1-i)*n+(n-1-j)
        x,k,s=source_coordinate(column)
        assign(target_row,source_index(7-x,14-k,7-s),value)
    boundary=sorted({column for _,column in constraints})
    if boundary!=boundary_columns():
        raise ArithmeticError('The construction did not prescribe the full endpoint boundary')
    free=[column for column in range(960) if column not in set(boundary)]
    if len(boundary)!=238 or len(free)!=722:
        raise ArithmeticError('Unexpected source boundary size')
    numerators={(row,column):int(value*DENOMINATOR) for (row,column),value in constraints.items() if value}
    pinned_free={}
    if q1_mode=='m4':
        pinned_free={(1*27+1,source_index(1,8,7)):DENOMINATOR,
                     (25*27+25,source_index(6,6,0)):DENOMINATOR}
        numerators.update(pinned_free)
    reserved_columns={column for _,column in pinned_free}
    rank_report=[]
    for weight,rows in sorted(groups.items()):
        columns=[column for column in boundary
                 if (lambda c:c[0]+c[2]-c[1])(source_coordinate(column))==weight]
        matrix=[[numerators.get((row,column),0) for column in columns] for row in rows]
        boundary_rank=len(row_pivots(matrix))
        free_columns=[column for column in free
                      if (lambda c:c[0]+c[2]-c[1])(source_coordinate(column))==weight]
        preassigned_columns=columns+[column for column in free_columns if column in reserved_columns]
        matrix=[[numerators.get((row,column),0) for column in preassigned_columns] for row in rows]
        pivots=set(row_pivots(matrix))
        missing=[row for i,row in enumerate(rows) if i not in pivots]
        available=[column for column in free_columns if column not in reserved_columns]
        if len(missing)>len(available):
            raise ArithmeticError('The free source coordinates cannot make this map concise')
        for row,column in zip(missing,available):
            numerators[row,column]=1
        all_columns=columns+free_columns
        final=[[numerators.get((row,column),0) for column in all_columns] for row in rows]
        rank=len(row_pivots(final))
        if rank!=len(rows):
            raise ArithmeticError('A completed weight block is not injective')
        rank_report.append({'weight':weight,'target_dimension':len(rows),
                            'boundary_rank_mod65521':boundary_rank,
                            'free_source_dimension':len(free_columns),
                            'completed_rank_mod65521':rank})
    common=[[row,column,value] for (row,column),value in sorted(numerators.items())]
    maps=[[[row,original_column(axis,column),value] for row,column,value in common] for axis in range(3)]
    return {'format':'A88-extreme-slice-affine-seed-v1','source_lengths':[8,8],
            'source_dimensions':[960]*3,'target_blocks':[27,7],
            'target_dimensions':[778]*3,'target_vertex_charges':CHARGES,
            'map_denominator':DENOMINATOR,'common_map_numerators':common,'maps':maps,
            'fixed_boundary_source_columns_common_order':boundary,
            'free_source_columns_common_order':free,
            'source_boundary_count':238,'free_source_coordinate_count':722,
            'anchor_target_units':[high*27+low,low*27+high],
            'high_low_slack_channels':channels_report,'central_shared_target_row':shared,
            'weight_block_rank_checks':rank_report,
            'q1_channel_mode':q1_mode,
            'historical_nonextendable_boundary_control':q1_mode=='hadamard',
            'exact_embedded_M4_claimed':q1_mode=='m4',
            'm4_target_vertices':[0,1,25,26] if q1_mode=='m4' else [],
            'all_extreme_slice_equations_claimed':True,
            'full_target_tensor_identity_claimed':False,
            'quotient_equations_imposed':False,
            'new_exponent_established':False}


def verify_m4(data):
    """Replay the full tensor on the four endpoint target vertices."""
    vertices=[0,1,25,26]
    if data.get('m4_target_vertices')!=vertices:
        raise ValueError('Unexpected endpoint M4 vertices')
    target_rows={i*27+j for i,j in product(vertices,repeat=2)}
    maps=[]
    for entries in data['maps']:
        inverse=defaultdict(list)
        for row,column,value in entries:
            if row in target_rows:
                inverse[column].append((row,value))
        maps.append(inverse)
    actual=Counter()
    for i,j,p,q,r,s in product(range(8),repeat=6):
        point=((i*15+p+q)*8+s,(j*8+p)*15+r+s,((i+j)*8+q)*8+r)
        for x,y,z in product(*(maps[axis].get(point[axis],[]) for axis in range(3))):
            actual[x[0],y[0],z[0]]+=x[1]*y[1]*z[1]
    actual=Counter({point:value for point,value in actual.items() if value})
    expected=Counter({(i*27+j,j*27+k,k*27+i):data['map_denominator']**3
                      for i,j,k in product(vertices,repeat=3)})
    if actual!=expected:
        raise ArithmeticError('The endpoint M4 tensor identity fails')
    return {'vertices':vertices,'source_terms_enumerated':262144,
            'full_target_coefficients_checked':4096,'nonzero_target_coefficients':64,
            'all_M4_coefficients_exact':True}


def verify(data):
    """Replay the partial identity and conciseness from the actual sparse maps.

    The recorded rank report is deliberately not used. A rank over the prime
    field certifies the same lower bound over the rationals because the
    exported map numerators are integers.
    """
    if data.get('full_target_tensor_identity_claimed'):
        raise ValueError('This seed certifies only the two extreme slice families')
    units,groups,vertices=target_data();den=data['map_denominator']
    if type(den) is not int or den<=0:
        raise ValueError('The common map denominator must be a positive integer')
    if (data.get('source_lengths')!=[8,8] or
        data.get('source_dimensions')!=[960]*3 or
        data.get('target_dimensions')!=[778]*3 or
        data.get('target_blocks')!=[27,7]):
        raise ValueError('Unexpected source or target dimensions')
    if data['target_vertex_charges']!=CHARGES:
        raise ValueError('Unexpected target vertex profile')
    if not isinstance(data.get('maps'),list) or len(data['maps'])!=3:
        raise ValueError('Exactly three sparse maps are required')
    boundary=boundary_columns();boundary_set=set(boundary)
    free=[column for column in range(960) if column not in boundary_set]
    if (data.get('fixed_boundary_source_columns_common_order')!=boundary or
        data.get('free_source_columns_common_order')!=free or
        data.get('source_boundary_count')!=len(boundary) or
        data.get('free_source_coordinate_count')!=len(free)):
        raise ValueError('The recorded boundary/free partition is incorrect')
    if data.get('anchor_target_units')!=[26*27,26]:
        raise ValueError('Unexpected extreme target units')
    maps=[defaultdict(dict) for _ in range(3)]
    source_weights=[{} for _ in range(3)]
    original_to_common=[{} for _ in range(3)]
    common_weight_groups=defaultdict(list)
    for column in range(960):
        i,k,s=source_coordinate(column)
        common_weight_groups[i+s-k].append(column)
        for axis in range(3):
            source_weights[axis][original_column(axis,column)]=i+s-k
            original_to_common[axis][original_column(axis,column)]=column
    target_weights={row:weight for weight,rows in groups.items() for row in rows}
    for axis,entries in enumerate(data['maps']):
        if not isinstance(entries,list):
            raise ValueError('A sparse map must be a list of integer triples')
        for row,column,value in entries:
            if any(type(x) is not int for x in (row,column,value)):
                raise ValueError('Sparse map entries must be integer triples')
            if not (0<=row<778 and 0<=column<960):
                raise ValueError('A sparse map entry is out of range')
            if not value:
                raise ValueError('Stored sparse map entries must be nonzero')
            if target_weights[row]!=source_weights[axis][column]:
                raise ArithmeticError('A seed map violates the torus weights')
            if row in maps[axis][column]:
                raise ArithmeticError('Duplicate sparse map entry')
            maps[axis][column][row]=value
    # The common-order copy is optional when experimenting with three
    # distinct free maps. If supplied, it must reproduce every actual map.
    if 'common_map_numerators' in data:
        common=data['common_map_numerators'];seen=set()
        if not isinstance(common,list):
            raise ValueError('The common sparse map must be a list')
        for row,column,value in common:
            if (any(type(x) is not int for x in (row,column,value)) or
                not 0<=row<778 or not 0<=column<960 or not value):
                raise ValueError('Invalid common-order sparse map entry')
            if (row,column) in seen:
                raise ArithmeticError('Duplicate common-order sparse map entry')
            seen.add((row,column))
        for axis in range(3):
            expected=sorted((row,original_column(axis,column),value)
                            for row,column,value in common)
            if expected!=sorted(tuple(entry) for entry in data['maps'][axis]):
                raise ArithmeticError('The common and original-order maps disagree')
    rank_reports=[]
    for axis in range(3):
        for weight,rows in sorted(groups.items()):
            columns=[original_column(axis,column) for column in common_weight_groups[weight]]
            matrix=[[maps[axis].get(column,{}).get(row,0) for column in columns]
                    for row in rows]
            rank=len(row_pivots(matrix))
            if rank!=len(rows):
                raise ArithmeticError('A map is not concise: leg %s, weight %s, rank %s < %s'
                                      %(axis,weight,rank,len(rows)))
            rank_reports.append({'leg':axis,'weight':weight,
                                 'target_dimension':len(rows),'rank_mod65521':rank})
    anchor_rows=[26*27,26]
    anchor_source=[source_index(7,0,7),source_index(0,14,0)]
    for axis in range(3):
        for row,common_column in zip(anchor_rows,anchor_source):
            entries=[(column,values[row]) for column,values in maps[axis].items() if row in values]
            if entries!=[(original_column(axis,common_column),den)]:
                raise ArithmeticError('An extreme target unit is not its required source corner')
    supports={(axis,orientation):[] for axis in range(3) for orientation in range(2)}
    count=0
    for i,j,p,q,r,s in product(range(8),repeat=6):
        point=((i*15+p+q)*8+s,(j*8+p)*15+r+s,((i+j)*8+q)*8+r)
        count+=1
        for axis in range(3):
            for orientation in range(2):
                if point[axis]==original_column(axis,anchor_source[orientation]):
                    if any(original_to_common[other][point[other]] not in boundary_set
                           for other in range(3) if other!=axis):
                        raise ArithmeticError('A free coordinate occurs beside an extreme source point')
                    supports[axis,orientation].append(point)
    reports=[]
    for (axis,orientation),points in supports.items():
        other=(axis+1)%3;last=(axis+2)%3;actual=Counter()
        for point in points:
            for row,b in maps[other].get(point[other],{}).items():
                for column,c in maps[last].get(point[last],{}).items():
                    actual[row,column]+=den*b*c
        actual=Counter({key:value for key,value in actual.items() if value})
        first,last_vertex=(0,26) if orientation==0 else (26,0)
        expected=Counter({(first*27+t,t*27+last_vertex):den**3 for t in range(27)})
        if actual!=expected:
            differences=[(key,actual[key]-expected[key]) for key in set(actual)|set(expected)
                         if actual[key]!=expected[key]]
            raise ArithmeticError('An extreme slice equation failed: '+str(differences[:3]))
        reports.append({'anchor_leg':axis,'orientation':orientation,
                        'source_slice_terms':len(points),'nonzero_target_coefficients':len(actual),
                        'all_other_target_coefficients_zero':True})
    report={'source_terms_enumerated':count,'exact_extreme_slice_checks':reports,
            'three_actual_maps_concise_by_recomputed_modular_ranks':True,
            'actual_map_rank_checks':rank_reports,
            'boundary_partition_recomputed':True,
            'free_columns_never_occur_beside_an_extreme_source_point':True,
            'partial_equations_only':True,'full_target_witness':False,
            'new_exponent_established':False}
    if data.get('exact_embedded_M4_claimed'):
        report['exact_embedded_M4']=verify_m4(data)
    return report


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument('--q1-mode',choices=('m4','hadamard'),default='m4')
    args=parser.parse_args();data=build(args.q1_mode);data['verification']=verify(data)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'output':str(args.output),'source_boundary_count':data['source_boundary_count'],
                      'free_source_coordinate_count':data['free_source_coordinate_count'],
                      'nonzero_map_entries_per_leg':len(data['maps'][0]),
                      'exact_extreme_slice_checks':data['verification']['exact_extreme_slice_checks'],
                      'actual_map_weight_blocks_replayed':len(data['verification']['actual_map_rank_checks']),
                      'three_actual_maps_concise':True,
                      'full_target_witness':False,'new_exponent_established':False},indent=2))


if __name__=='__main__':
    main()
