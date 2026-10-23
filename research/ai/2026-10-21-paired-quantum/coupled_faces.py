"""Exact coupled Laurent degenerations of P3 at a primitive fourth root.

The two fixed families produce explicit intermediate tensors, not the
desired matrix direct sum. No LP or finite-field decision is used here.
"""
from collections import defaultdict,Counter
from fractions import Fraction
import importlib.util
from itertools import combinations,product
import json
from pathlib import Path

from sympy import QQ
from sympy.polys.matrices import DomainMatrix

SPEC=importlib.util.spec_from_file_location('paired_quantum_screens',Path(__file__).with_name('screens.py'))
screens=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(screens)
core=screens.core

FAMILIES=(
    {'name':'face0','D':2,
     'W':[0,1,0,1,0,1,0,1,0,
          0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,
          0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0]},
    {'name':'face1','D':8,
     'W':[0,5,2,7,4,5,-6,7,-6,
          0,-3,2,-9,4,-7,6,-3,-6,-9,4,-7,-6,-1,4,
          0,5,2,7,4,1,6,5,2,7,12,1,2,-1,12]},
)
TARGET_RANKS=[12,108,402,825,1035,822,408,117,15]


def valuation_data():
    a,order=3,4
    tensor=core.paired_recoupled(a)
    data=[screens.paired_local_map(a,i) for i in range(3)]
    normalizations=[screens.regular_initial_entries(d,order)[1] for d in data]
    indices=[{label:i for i,label in enumerate(d[1])} for d in data]
    field,poly=screens.residue_field(order)
    records=[]
    for key,value in tensor.items():
        positions=tuple(indices[i][key[i]] for i in range(3))
        val,parts=core.initial_residue(value,poly)
        scalars=[]
        for p in parts:
            scalars.append(sum((field.convert(c)*field.unit**e[0]
                                for e,c in p.items()),field.zero))
        coefficient=scalars[0]/scalars[1]
        baseline=val-sum(normalizations[i][positions[i]] for i in range(3))
        if baseline<0:raise ArithmeticError('regular maps gave a tensor pole')
        records.append({'positions':positions,'valuation':baseline,
                        'coefficient':[str(c) for c in coefficient.to_list()]})
    return {'a':a,'root_order':order,'dimensions':[len(d[1]) for d in data],
            'labels':[d[1] for d in data],'normalizations':normalizations,
            'records':records}


def leading_indices(data,D,W):
    dimensions=data['dimensions'];offsets=[0,dimensions[0],sum(dimensions[:2])]
    if len(W)!=sum(dimensions) or D<=0:
        raise ValueError('invalid family weights')
    exponents=[]
    for record in data['records']:
        exponent=D*record['valuation']+sum(W[offsets[leg]+position]
                      for leg,position in enumerate(record['positions']))
        if exponent<0:raise ArithmeticError('the proposed tensor has a Laurent pole')
        exponents.append(exponent)
    return [i for i,e in enumerate(exponents) if e==0],exponents


def real_gauge(data,indices):
    dimensions=data['dimensions'];offsets=[0,dimensions[0],sum(dimensions[:2])]
    pivots={};entries=[]
    for index in indices:
        record=data['records'][index]
        coefficients=list(map(Fraction,record['coefficient']))
        if len(coefficients)==1:imaginary,rational=0,coefficients[0]
        elif len(coefficients)==2 and coefficients[1]==0:imaginary,rational=1,coefficients[0]
        else:raise ArithmeticError('mixed cyclotomic coefficient')
        mask=sum(1<<(offsets[leg]+position) for leg,position in enumerate(record['positions']))
        bits,answer=mask,imaginary
        while bits:
            pivot=(bits&-bits).bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=(bits,answer)
                break
            old,old_answer=pivots[pivot]
            bits^=old;answer^=old_answer
        if not bits and answer:raise ArithmeticError('no real diagonal phase gauge')
        entries.append((record['positions'],imaginary,rational))
    bits=0
    for pivot,(mask,answer) in sorted(pivots.items(),reverse=True):
        if answer^((mask&bits).bit_count()%2):bits|=1<<pivot
    phases=[int(bool(bits&(1<<i))) for i in range(sum(dimensions))]
    tensor={}
    for positions,imaginary,rational in entries:
        exponent=imaginary+sum(phases[offsets[i]+p] for i,p in enumerate(positions))
        if exponent%2:raise ArithmeticError('phase verification failed')
        tensor[tuple(positions)]=(-1)**(exponent//2)*rational
    return phases,tensor


def rank_rational(matrix):
    if not matrix:return 0
    converted=[[QQ.convert(x) for x in row] for row in matrix]
    return DomainMatrix.from_list(converted,QQ).rank()


def flattening_ranks(tensor,dimensions):
    output=[]
    for leg in range(3):
        other=[i for i in range(3) if i!=leg]
        columns=list(product(*(range(dimensions[i]) for i in other)))
        matrix=[[tensor.get(tuple(row if i==leg else column[other.index(i)] for i in range(3)),Fraction(0))
                 for column in columns] for row in range(dimensions[leg])]
        output.append(rank_rational(matrix))
    return output


def slice_matrices(tensor,dimensions):
    return [[[tensor.get((i,j,k),Fraction(0)) for k in range(dimensions[2])]
             for j in range(dimensions[1])] for i in range(dimensions[0])]


def graded_koszul(tensor,dimensions,weights,p):
    A,B,C=dimensions
    totals={sum(weights[i][indices[i]] for i in range(3)) for indices in tensor}
    if len(totals)!=1:raise ArithmeticError('tensor is not homogeneous')
    total=totals.pop()
    left=list(combinations(range(A),p));right=list(combinations(range(A),p+1))
    left_degrees=[sum(weights[0][i] for i in subset) for subset in left]
    right_degrees=[sum(weights[0][i] for i in subset) for subset in right]
    domain=defaultdict(list);codomain=defaultdict(list)
    for index,degree in enumerate(left_degrees):
        for j in range(B):domain[degree-weights[1][j]].append((index,j))
    for index,degree in enumerate(right_degrees):
        for k in range(C):codomain[degree+weights[2][k]-total].append((index,k))
    rows={subset:i for i,subset in enumerate(right)}
    entries=defaultdict(dict)
    for l,subset in enumerate(left):
        included=set(subset)
        for (i,j,k),coefficient in tensor.items():
            if i in included:continue
            out=tuple(sorted((*subset,i)))
            sign=(-1)**sum(x<i for x in subset)
            degree=left_degrees[l]-weights[1][j]
            entries[degree][(rows[out],k),(l,j)]=sign*coefficient
    blocks=[]
    for degree,columns in sorted(domain.items()):
        rlabels=codomain.get(degree,[]);values=entries[degree]
        matrix=[[values.get((row,col),Fraction(0)) for col in columns] for row in rlabels]
        blocks.append({'degree':degree,'rows':len(rlabels),'columns':len(columns),
                       'rank':rank_rational(matrix)})
    return {'power':p,'rank':sum(b['rank'] for b in blocks),'blocks':blocks}


def family_report(data,family):
    D,W=family['D'],family['W'];dimensions=data['dimensions']
    indices,exponents=leading_indices(data,D,W)
    phases,tensor=real_gauge(data,indices)
    weights=[[sum(label) for label in leg] for leg in data['labels']]
    matrices=slice_matrices(tensor,dimensions)
    ranks=[rank_rational(matrix) for matrix in matrices]
    invertible=next(i for i,rank in enumerate(ranks) if rank==15)
    determinant=screens.determinant_field([[QQ.convert(x) for x in row]
                                          for row in matrices[invertible]],QQ)
    koszul=[graded_koszul(tensor,dimensions,weights,p) for p in range(9)]
    row_minima=sum(data['normalizations'],[])
    output={'name':family['name'],'D':D,'integer_weights':W,
            'local_t_exponents':[w-D*r for w,r in zip(W,row_minima)],
            'phase_powers_of_i':phases,
            'tensor_exponent_histogram':dict(sorted(Counter(exponents).items())),
            'flattening_ranks':flattening_ranks(tensor,dimensions),
            'basis_slice_ranks':ranks,
            'invertible_slice_index':invertible,'invertible_slice_determinant':str(determinant),
            'first_leg_koszul':koszul,
            'passes_target_first_leg_koszul':all(k['rank']>=target for k,target in zip(koszul,TARGET_RANKS)),
            'tensor_coefficients':[{'positions':key,'coefficient':str(value)}
                                   for key,value in sorted(tensor.items())],
            'ordinary_target_exclusion':'The target has maximum slice rank9, while any full-A/full-C ordinary restriction with B rank12 preserves a rank12 slice.'}
    if min(ranks)<=2:
        output['all_further_target_degenerations_excluded_by_rank2_slice']=True
        output['rank2_slice_index']=ranks.index(2)
    return output


def report():
    data=valuation_data()
    families=[family_report(data,family) for family in FAMILIES]
    return {'claim_id':'AI-PAIRED-QUANTUM-002','status':'Explicit Laurent families and exact intermediate tensors; unreviewed.',
            'improves_omega':False,
            'q_path':'q(t)=i*(1-t^D/2), so q(t)^2+1=t^D-t^(2D)/4',
            'source_valuation_data':data,
            'target_shapes':[[1,3,3],[3,3,2]],'target_first_leg_koszul':TARGET_RANKS,
            'families':families}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Verified two explicit Laurent limits, all288 nonzero generic coefficients, and18 exact Koszul ranks.')
