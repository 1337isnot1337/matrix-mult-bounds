"""Exact unequal-source Laurent faces and matrix-target obstructions.

The fixed weights were proposed numerically. Replay uses only exact
Q(q) contractions, cyclotomic residues, and exact field arithmetic.
"""
from collections import Counter,defaultdict
from fractions import Fraction
from functools import lru_cache
import importlib.util
from itertools import combinations
import json
from math import comb
from pathlib import Path

from sympy import QQ
from sympy.polys.matrices import DomainMatrix

SPEC=importlib.util.spec_from_file_location('narrow_quantum_core',Path(__file__).with_name('quantum.py'))
quantum=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(quantum)
screen,core=quantum.screen,quantum.core
FAMILIES=json.loads(Path(__file__).with_name('families.json').read_text())['families']


def exact_rank(matrix,field):
    if not matrix:return 0
    converted=[[field.convert(x) for x in row] for row in matrix]
    return DomainMatrix(converted,(len(converted),len(converted[0])),field).rank()


def decode(coefficients,field):
    value=field.zero
    for c in coefficients:value=value*field.unit+field.convert(Fraction(c))
    return value


def leading_indices(data,D,W):
    dimensions=data['source_format'];offsets=[0,dimensions[0],sum(dimensions[:2])]
    if D<=0 or len(W)!=sum(dimensions):raise ValueError('invalid Laurent weights')
    exponents=[D*r['baseline_valuation']+sum(W[offsets[k]+p] for k,p in enumerate(r['positions']))
               for r in data['coefficients']]
    if any(e<0 for e in exponents):raise ArithmeticError('Laurent pole in proposed tensor')
    return [i for i,e in enumerate(exponents) if e==0],exponents


def compress(tensor,dimensions,field):
    support=[]
    for axis in range(3):
        other=[k for k in range(3) if k!=axis]
        columns=sorted({tuple(key[k] for k in other) for key in tensor})
        matrix=[[tensor.get(tuple(row if k==axis else col[other.index(k)] for k in range(3)),field.zero)
                 for col in columns] for row in range(dimensions[axis])]
        support.append(screen.independent_rows(matrix,field.zero)[0])
    compressed={tuple(support[k].index(p) for k,p in enumerate(positions)):value
                for positions,value in tensor.items()
                if all(p in support[k] for k,p in enumerate(positions))}
    return support,compressed


def graded_koszul(tensor,dimensions,weights,p,field):
    A,B,C=dimensions
    totals={sum(weights[k][indices[k]] for k in range(3)) for indices in tensor}
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
    rows={subset:i for i,subset in enumerate(right)};entries=defaultdict(dict)
    for l,subset in enumerate(left):
        included=set(subset)
        for (i,j,k),coefficient in tensor.items():
            if i in included:continue
            out=tuple(sorted((*subset,i)))
            sign=(-1)**sum(x<i for x in subset)
            degree=left_degrees[l]-weights[1][j]
            entries[degree][(rows[out],k),(l,j)]=sign*coefficient
    result=0
    for degree,columns in domain.items():
        rlabels=codomain.get(degree,[]);values=entries[degree]
        matrix=[[values.get((row,col),field.zero) for col in columns] for row in rlabels]
        result+=exact_rank(matrix,field)
    return result


@lru_cache(None)
def intrinsic_target_ranks():
    """Construct the complete M(3,2,3) coefficient tensor independently."""
    dimensions=[9,6,6]
    tensor={(i*3+j,j*2+k,k*3+i):QQ.one
            for i in range(3) for j in range(3) for k in range(2)}
    weights=[[i+j for i in range(3) for j in range(3)],
             [2-j+k for j in range(3) for k in range(2)],
             [3-i-k for k in range(2) for i in range(3)]]
    ranks=[]
    for axis in range(3):
        order=[axis]+[k for k in range(3) if k!=axis]
        permuted={tuple(key[k] for k in order):value for key,value in tensor.items()}
        local_dimensions=[dimensions[k] for k in order];local_weights=[weights[k] for k in order]
        ranks.append([graded_koszul(permuted,local_dimensions,local_weights,p,QQ)
                      for p in range(local_dimensions[0])])
    return ranks


def padded_target_ranks(axis,ambient):
    intrinsic=intrinsic_target_ranks()[axis]
    difference=ambient-len(intrinsic)
    if difference<0:raise ValueError('source leg is smaller than the target')
    return [sum(comb(difference,j)*intrinsic[p-j]
                for j in range(difference+1) if 0<=p-j<len(intrinsic))
            for p in range(ambient)]


def family_report(data,family):
    field,_=screen.residue_field(data['order'])
    dimensions=data['source_format'];D,W=family['D'],family['W']
    indices,exponents=leading_indices(data,D,W)
    tensor={tuple(data['coefficients'][i]['positions']):decode(data['coefficients'][i]['leading_residue_coefficients'],field)
            for i in indices}
    basis_ranks=[exact_rank([[tensor.get((i,j,k),field.zero) for k in range(dimensions[2])]
                            for j in range(dimensions[1])],field) for i in range(dimensions[0])]
    support,compressed=compress(tensor,dimensions,field)
    concise=list(map(len,support))
    weights=[[sum(data['labels'][k][i]) for i in support[k]] for k in range(3)]
    output={'name':family['name'],'D':D,'W':W,
            'local_t_exponents':[w-D*r for w,r in zip(W,sum(data['row_minima'],[]))],
            'tensor_exponent_histogram':dict(sorted(Counter(exponents).items())),
            'original_basis_slice_ranks':basis_ranks,'concise_format':concise,
            'compression_row_indices':support,'concise_weights':weights,
            'coefficients':[{'positions':positions,'coefficient':screen.encode_field(value)}
                            for positions,value in sorted(compressed.items())]}
    if concise[0]<9:
        output['exclusion']={'type':'ordinary flattening rank','axis':0,
                             'source_rank':concise[0],'target_rank':9}
    elif 1 in basis_ranks:
        output['exclusion']={'type':'closed rank-one slice incidence',
                             'original_slice_index':basis_ranks.index(1),'target_minimum_nonzero_slice_rank':2}
    else:
        koszul=[];obstructions=[]
        for axis in range(3):
            order=[axis]+[k for k in range(3) if k!=axis]
            permuted={tuple(key[k] for k in order):value for key,value in compressed.items()}
            local_dimensions=[concise[k] for k in order];local_weights=[weights[k] for k in order]
            source=[graded_koszul(permuted,local_dimensions,local_weights,p,field)
                    for p in range(local_dimensions[0])]
            target=padded_target_ranks(axis,local_dimensions[0])
            koszul.append({'axis':axis,'source_ranks':source,'target_ranks':target})
            for p,(s,t) in enumerate(zip(source,target)):
                if s<t:obstructions.append({'axis':axis,'power':p,'source_rank':s,'target_rank':t})
        output['all_legs_koszul']=koszul
        if obstructions:output['exclusion']={'type':'Koszul rank','witnesses':obstructions}
    output['target_excluded']=bool(output.get('exclusion'))
    return output


def report():
    data,*_=quantum.initial_tensor(3,2,8,False)
    regular=[]
    for recouple_A in (False,True):
        row,*_=quantum.initial_tensor(3,2,8,recouple_A)
        regular.append({key:row[key] for key in ['recouple_A','source_format','regular_tensor_flattening_ranks',
                       'regular_tensor_nonzero_coefficients','local_map_records']})
    checks=sum(quantum.source_control(n,m) for n in range(2,5) for m in range(2,5))
    families=[family_report(data,family) for family in FAMILIES]
    return {'claim_id':'AI-NARROW-QUANTUM-001','status':'Exact fixed Laurent families and written scope arguments; unreviewed.',
            'improves_omega':False,'q_path':'zeta8*(1-t^D/4), with zeta8^4=-1',
            'generic_source_identity_checks':checks,'source_valuation_data':data,
            'regular_calibrations':regular,'target_intrinsic_koszul_ranks':intrinsic_target_ranks(),
            'families':families,'all_fixed_faces_excluded':all(row['target_excluded'] for row in families),
            'scope':'Only the 23 fixed weight vectors. This does not exclude other bases, weights, or Q(3,2) degenerations.'}


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=report()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Verified',result['generic_source_identity_checks'],'formal source identities and',
          len(result['families']),'exact Laurent faces; target excluded for every fixed face:',result['all_fixed_faces_excluded'])
